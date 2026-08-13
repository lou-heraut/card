"""Le corpus complet des fiches doit passer le linter, et le linter doit
détecter les défauts qu'il prétend détecter."""


from card.extraction import _DEFAULT_CARD_DIR
from card.loader import load_card
from card.schema import lint_cards, validate_card


def test_corpus_is_valid():
    report = lint_cards()
    assert report == {}, f"fiches en défaut : {report}"


def test_corpus_loads_completely():
    paths = list(_DEFAULT_CARD_DIR.rglob("*.yaml"))
    assert len(paths) >= 210
    for p in paths:
        load_card(p)


def test_linter_catches_lost_window_bound(tmp_path):
    """Reproduit le bug historique des 29 fiches : borne de fin de fenêtre
    perdue dans le process : le linter doit le signaler."""
    src = next(_DEFAULT_CARD_DIR.rglob("QNA_summer.yaml"))
    damaged = src.read_text().replace(
        'sampling_period: ["05-01", "11-30"]\n    max_na_pct',
        'sampling_period: "05-01"\n    max_na_pct',
    )
    assert damaged != src.read_text(), "fixture invalide"
    bad = tmp_path / "QNA_summer.yaml"
    bad.write_text(damaged)
    issues = validate_card(bad)
    assert any("fenêtre partielle" in i for i in issues), issues


def test_linter_catches_unknown_function(tmp_path):
    bad = tmp_path / "X.yaml"
    bad.write_text(
        "id: X\nmeta: {en: {variable: X}, fr: {variable: X}, global: {}}\n"
        "process:\n  P1:\n    func:\n      X: [fonction_inconnue, \"Q\"]\n"
    )
    issues = validate_card(bad)
    assert any("fonction inconnue" in i for i in issues), issues


def test_linter_catches_malformed_version(tmp_path):
    """La version d'une fiche est majeur.mineur[.patch], et citée : sans
    guillemets, YAML lit 1.10 comme le nombre 1.1 et deux versions
    distinctes se confondent."""
    base = ("id: X\nmeta: {en: {variable: X}, fr: {variable: X}, global: {}}\n"
            "process:\n  P1:\n    func:\n      X: [nanmean, \"Q\"]\n")
    cas = {
        "version: 1.10\n": "non citée",        # nombre, pas chaîne
        'version: "1.1.0"\n': "patch nul",     # .0 explicite
        'version: "v2"\n': "mal formée",
        "": "manquant",
    }
    for ligne, attendu in cas.items():
        bad = tmp_path / "X.yaml"
        bad.write_text(ligne + base)
        issues = validate_card(bad)
        assert any(attendu in i for i in issues), (ligne, issues)


def test_card_version_reaches_the_metadata():
    """La version d'une fiche doit voyager jusqu'aux métadonnées de
    sortie : sinon un résultat ne peut pas dire avec quelle définition il
    a été calculé, et la discipline de version ne sert à rien."""
    from card.extraction import extract
    meta = extract(None, cards=["QA", "KGE"], metadata_only=True)["meta"]
    assert "version" in meta.columns
    assert meta["version"].notna().all()


def test_ambiguous_aggregation_names_rejected():
    """Les fiches doivent porter la sémantique NaN dans le nom de la
    fonction : les noms nus (mean, max...) sont refusés par le linter."""
    from card.schema import _check_process
    proc = {"name": "P1", "time_step": "year", "keep": None,
            "max_na_pct": None, "sampling_period": None,
            "func": [{"name": "X", "fn_name": "mean"}]}
    issues = []
    _check_process(proc, issues)
    assert any("nanmean" in i for i in issues)


def test_swhid_de_fiche_est_le_hash_git_du_fichier():
    """Le SWHID de contenu d'un fichier est son hash de blob git : on le
    calcule donc sans réseau ni dépôt. C'est ce qui permet de retrouver
    la DÉFINITION exacte employée dans un résultat archivé."""
    import hashlib

    from card.extraction import extract
    from card.loader import load_card

    src = next(_DEFAULT_CARD_DIR.rglob("QA.yaml"))
    octets = src.read_bytes()
    attendu = hashlib.sha1(b"blob %d\0" % len(octets) + octets).hexdigest()

    assert load_card(src)["swhid"] == f"swh:1:cnt:{attendu}"

    meta = extract(None, cards=["QA"], metadata_only=True)["meta"]
    assert meta["swhid"].iloc[0] == f"swh:1:cnt:{attendu}"
    # le chemin publié est celui du corpus, pas celui de la machine
    assert meta["script_path"].iloc[0] == "flow/mean-flows/series/QA.yaml"


def test_linter_refuse_une_metadonnee_en_liste_pour_une_variable_unique(tmp_path):
    """Le défaut du 2026-07-22 : 14 fiches d'horizon avaient gardé un
    `name` en liste de trois après leur passage à une sortie unique. Seul
    le premier était publié, donc elles annonçaient « l'horizon proche »
    quel que soit l'horizon calculé."""
    bad = tmp_path / "X.yaml"
    bad.write_text(
        'id: X\nversion: "1.0"\n'
        "meta:\n"
        "  en: {variable: X, name: [premier, deuxieme, troisieme]}\n"
        "  fr: {variable: X, name: [premier, deuxieme, troisieme]}\n"
        "  global: {}\n"
        'process:\n  P1:\n    func:\n      X: [nanmean, "Q"]\n'
    )
    issues = validate_card(bad)
    assert any("seul le premier serait publié" in i for i in issues), issues


def test_linter_catches_two_wordings_for_one_variable(tmp_path):
    """Deux fiches produisant la même variable en disent la même chose.

    Défaut réel du corpus, trouvé le 2026-08-12 : sept variables portaient
    deux `name` ou `description` anglais selon la fiche qui les produit,
    le français restant d'accord. Aucune fiche prise seule n'était fautive,
    donc `validate_card` ne pouvait rien voir : la règle est inter-fiches
    et vit dans `lint_cards`.
    """
    commun = ("meta:\n  en: {{variable: vX, name: {nom}}}\n"
              "  global: {{}}\nprocess: {{}}\n")
    for fiche, nom in (("seule", "Deficit volume of low flows"),
                       ("groupee", "Low flow deficit volume")):
        (tmp_path / f"{fiche}.yaml").write_text(
            f'id: {fiche}\nversion: "1.0"\n' + commun.format(nom=nom))
    report = lint_cards(tmp_path)
    for fiche in ("seule", "groupee"):
        assert any("meta.en.name de 'vX'" in i for i in report[fiche]), report

    # même variable, même libellé : la règle se tait
    (tmp_path / "groupee.yaml").write_text(
        'id: groupee\nversion: "1.0"\n'
        + commun.format(nom="Deficit volume of low flows"))
    report = lint_cards(tmp_path)
    assert not any("deux valeurs selon la fiche" in i
                   for issues in report.values() for i in issues), report


def test_linter_catches_two_classifications_for_one_variable(tmp_path):
    """`RAs` était `snow` dans sa fiche seule et `mean precipitation`
    dans la fiche groupée `RA_all` : la même variable rangée dans deux
    phénomènes selon qui la produit (corrigé le 2026-08-13)."""
    for fiche, phen in (("RAs", "snow"), ("RA_all", "mean precipitation")):
        (tmp_path / f"{fiche}.yaml").write_text(
            f'id: {fiche}\nversion: "1.0"\nmeta:\n'
            f"  en: {{variable: RAs, classification: {{phenomenon: {phen}}}}}\n"
            "  global: {}\nprocess: {}\n")
    report = lint_cards(tmp_path)
    assert any("classification.en.phenomenon de 'RAs'" in i
               for i in report["RAs"]), report


def test_linter_catches_a_stale_global_list(tmp_path):
    """La cause racine du défaut des trois fiches `delta-allLF_*`.

    Leurs listes de `meta.global` gardaient 15 valeurs pour 5 variables,
    restées du temps où elles sortaient 5 variables fois 3 horizons. Le
    contrôle de longueur existait, mais seulement sur les blocs de
    LANGUE : `meta.global` n'avait jamais été mesuré, donc rien ne
    rougissait pendant que deux variables se publiaient en dates.
    """
    bad = tmp_path / "X.yaml"
    bad.write_text(
        'id: X\nversion: "1.0"\nmeta:\n'
        "  en: {variable: [a, b], classification: {aspect: [timing, timing]}}\n"
        "  fr: {variable: [a, b]}\n"
        "  global: {is_date: [true, true, true, true, true, true]}\n"
        "process:\n  P1:\n    time_step: year\n    func:\n"
        '      a: [nanmean, "Q"]\n      b: [nanmean, "Q"]\n')
    issues = validate_card(bad)
    assert any("6 valeurs pour 2 variable(s)" in i for i in issues), issues


def test_linter_catches_is_date_disagreeing_with_aspect(tmp_path):
    """`is_date` vaut exactement « aspect timing », mesuré sur les 457
    variables saines du corpus le 2026-08-13. Une durée déclarée date
    sort avec la palette des dates, ce qui est arrivé à `delta-dtLF`."""
    bad = tmp_path / "X.yaml"
    bad.write_text(
        'id: X\nversion: "1.0"\nmeta:\n'
        "  en: {variable: [tX, dX], classification: {aspect: [timing, duration]}}\n"
        "  fr: {variable: [tX, dX]}\n"
        "  global: {is_date: [true, true]}\n"
        "process:\n  P1:\n    time_step: year\n    func:\n"
        '      tX: [nanmean, "Q"]\n      dX: [nanmean, "Q"]\n')
    issues = validate_card(bad)
    assert any("is_date de 'dX'" in i for i in issues), issues
    assert not any("is_date de 'tX'" in i for i in issues), issues


def test_linter_requires_relative_to_be_written(tmp_path):
    """`relative` s'écrit toujours, `true` compris, comme `time_step`.

    Avant le 2026-08-13, `true` n'existait que comme défaut et n'était
    écrit dans aucune fiche : « j'ai décidé que oui » et « personne n'a
    rien écrit » étaient indiscernables. Pour un champ dont tout le rôle
    est de porter une décision à destination des consommateurs, c'est le
    pire défaut possible, et il a laissé `RMAs_month` annoncer douze
    variables relatives, seule de sa famille.
    """
    bad = tmp_path / "X.yaml"
    bad.write_text(
        'id: X\nversion: "1.0"\nmeta:\n'
        '  en: {variable: X, unit: "m^{3}.s^{-1}"}\n'
        "  fr: {variable: X}\n  global: {}\n"
        'process:\n  P1:\n    time_step: year\n    func:\n'
        '      X: [nanmean, "Q"]\n'
    )
    issues = validate_card(bad)
    assert any("relative: non écrit" in i for i in issues), issues


def test_linter_catches_relative_disagreeing_with_the_unit(tmp_path):
    """L'unité détermine la propriété : elle sert de vérificateur.

    Le champ reste dans la fiche, c'est un raccourci volontaire pour que
    stase, une figure ou l'API n'aient pas à raisonner sur l'unité. Mais
    un raccourci ne vaut que si on peut lui faire confiance sans le
    vérifier, d'où cette garde. Un débit admet une expression relative,
    une durée non : on ne sait pas lire « 10 % de jours ».
    """
    def fiche(unit, relative):
        p = tmp_path / "X.yaml"
        p.write_text(
            f'id: X\nversion: "1.0"\nmeta:\n'
            f'  en: {{variable: X, unit: "{unit}"}}\n'
            f"  fr: {{variable: X}}\n  global: {{relative: {relative}}}\n"
            'process:\n  P1:\n    time_step: year\n    func:\n'
            '      X: [nanmean, "Q"]\n'
        )
        return validate_card(p)

    assert any("attendu False" in i for i in fiche("day", "true"))
    assert any("attendu True" in i for i in fiche("m^{3}.s^{-1}", "false"))
    # le verdict d'un test n'est pas une grandeur mesurée : sans objet
    assert any("attendu None" in i for i in fiche("bool", "false"))
    # et ce qui s'accorde ne dit rien
    for unit, val in (("day", "false"), ("m^{3}.s^{-1}", "true"),
                      ("bool", "null"), ("yearday", "false"), ("%", "true")):
        assert not any("relative de" in i for i in fiche(unit, val)), (unit, val)


def test_linter_refuses_an_unclassified_unit(tmp_path):
    """Une unité inconnue de la table force une décision au lieu de
    passer en silence : c'est la seule façon que la garde reste vraie
    quand le corpus s'étend."""
    bad = tmp_path / "X.yaml"
    bad.write_text(
        'id: X\nversion: "1.0"\nmeta:\n'
        '  en: {variable: X, unit: "furlong par quinzaine"}\n'
        "  fr: {variable: X}\n  global: {relative: true}\n"
        'process:\n  P1:\n    time_step: year\n    func:\n'
        '      X: [nanmean, "Q"]\n'
    )
    assert any("hors de la table" in i for i in validate_card(bad))
