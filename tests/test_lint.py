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
