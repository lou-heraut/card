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
