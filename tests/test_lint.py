"""Le corpus complet des fiches doit passer le linter — et le linter doit
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
    perdue dans le process — le linter doit le signaler."""
    src = next(_DEFAULT_CARD_DIR.rglob("QNA_summer.yaml"))
    damaged = src.read_text().replace(
        'sampling_period: ["05-01", "11-30"]\n    NApct_lim',
        'sampling_period: "05-01"\n    NApct_lim',
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
        "process:\n  P1:\n    funct:\n      X: [fonction_inconnue, \"Q\"]\n"
    )
    issues = validate_card(bad)
    assert any("fonction inconnue" in i for i in issues), issues
