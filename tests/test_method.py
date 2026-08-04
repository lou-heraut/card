"""`method` : une phrase par colonne produite (docs/dev/archive/PLAN_METHOD.md).

Deux choses se mesurent ici, et elles se répondent. D'abord que les
colonnes produites par un process se calculent JUSTE depuis le seul
YAML, sans données : c'est sur cette liste que reposent l'indexation de
`method`, la règle du linter et l'ordre de publication, et si elle est
fausse les trois le sont ensemble. Ensuite que la publication garde la
forme qu'elle a toujours eue, une étape numérotée par process, parce que
seule la fiche change de forme, jamais sa sortie.
"""

from pathlib import Path

import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import method as M
from card.loader import load_card

CARDS = sorted((Path(__file__).parent.parent
                / "src" / "card" / "cards").rglob("*.yaml"))
IDS = [p.stem for p in CARDS]


@pytest.mark.parametrize("chemin", CARDS, ids=IDS)
def test_les_colonnes_du_dernier_process_sont_les_sorties(chemin):
    """La liste calculée doit être celle que la fiche déclare, ordre compris.

    C'est le pivot de tout le dispositif : `meta.en.variable` est écrit à
    la main, `output_columns` est déduit du `process`. Les deux disent la
    même chose ou l'un des deux ment.
    """
    c = load_card(chemin)
    declare = c["meta"]["en"].get("variable")
    declare = declare if isinstance(declare, list) else [declare]
    assert M.output_columns(c) == declare


def test_compress_est_ce_qui_demultiplie_et_rien_d_autre():
    """Une fiche saisonnière sans `compress` produit UNE colonne.

    Mesuré par extraction réelle : avec `compress`, quatre colonnes
    `QSA_DJF`… ; sans lui, une colonne `QSA` et une ligne par saison.
    Le pas de temps ne suffit donc pas à conclure.
    """
    saisonnier = {"func": [{"name": "QSA"}], "time_step": "year-season",
                  "seasons": ["DJF", "MAM", "JJA", "SON"], "compress": True}
    assert M.produced_columns(saisonnier) == [
        "QSA_DJF", "QSA_MAM", "QSA_JJA", "QSA_SON"]
    assert M.produced_columns({**saisonnier, "compress": False}) == ["QSA"]
    # `compress` sans dimension à aplatir n'aplatit rien (median-allLF P5).
    assert M.produced_columns(
        {**saisonnier, "time_step": "none"}) == ["QSA"]


@pytest.mark.parametrize("chemin", CARDS, ids=IDS)
@pytest.mark.parametrize("lang", ["fr", "en"])
def test_la_publication_a_une_etape_par_process(chemin, lang):
    c = load_card(chemin)
    publie = M.published(c, lang)
    assert len(publie) == len(M.output_columns(c))
    for texte in publie:
        assert len(str(texte).split("\n")) == len(c["processes"])


def test_la_regle_de_chaine_rougit_sur_une_reference_pendante(tmp_path):
    """Éprouvée en cassant la chaîne, sinon elle ne garantit rien.

    P1 produit X et P2 le cite : si la phrase de P1 ne dit pas `X`, la
    chaîne publiée envoie le lecteur vers un nom qu'il n'a jamais lu.
    """
    from card.schema import validate_card

    def fiche(phrase_p1):
        p = tmp_path / f"chaine{abs(hash(phrase_p1))}.yaml"
        p.write_text(
            'id: ' + p.stem + '\nversion: "1.0"\nauthors: ["t"]\n'
            'date: "2026-08-03"\n'
            "meta:\n"
            "  en:\n    variable: a\n    unit: m\n    name: A\n"
            "    method:\n      P1:\n        X: no temporal aggregation - "
            f"{phrase_p1}\n"
            "      P2:\n        a: annual aggregation - maximum of X\n"
            "    classification: {domain: flow, season: annual, output: series}\n"
            "  fr:\n    variable: a\n    unit: m\n    name: A\n"
            "    method:\n      P1:\n        X: aucune agrégation temporelle - "
            f"{phrase_p1}\n"
            "      P2:\n        a: agrégation annuelle - maximum de X\n"
            "    classification: {domain: débit, season: annuelle, output: série}\n"
            "  global:\n    input_vars: Q\n"
            "process:\n"
            "  P1:\n    func:\n      X: [nanmean, \"Q\"]\n    time_step: none\n"
            "  P2:\n    func:\n      a: [nanmax, \"X\"]\n",
            encoding="utf-8")
        return validate_card(p)

    pendante = fiche("moyenne mobile")
    assert any("ne se lit pas seule" in i for i in pendante), pendante
    assert not any("ne se lit pas seule" in i
                   for i in fiche("moyenne mobile (X)"))


def test_la_moitie_gauche_est_confrontee_au_process(tmp_path):
    """Le seul contrôle croisé qui existe sur `method`.

    Il n'existe que parce que la phrase est ÉCRITE : une phrase générée
    serait d'accord avec le code par construction, y compris quand le
    code a tort. Éprouvé en faisant mentir la fiche.
    """
    from card.schema import validate_card

    def fiche(gauche):
        p = tmp_path / f"gauche{abs(hash(gauche))}.yaml"
        p.write_text(
            'id: ' + p.stem + '\nversion: "1.0"\nauthors: ["t"]\n'
            'date: "2026-08-03"\n'
            "meta:\n"
            "  en:\n    variable: a\n    unit: m\n    name: A\n"
            f"    method:\n      P1:\n        a: {gauche} - mean\n"
            "    classification: {domain: flow, season: annual, output: series}\n"
            "  fr:\n    variable: a\n    unit: m\n    name: A\n"
            "    method:\n      P1:\n        a: agrégation annuelle - moyenne\n"
            "    classification: {domain: débit, season: annuelle, output: série}\n"
            "  global:\n    input_vars: Q\n"
            "process:\n  P1:\n    func:\n      a: [nanmean, \"Q\"]\n",
            encoding="utf-8")
        return validate_card(p)

    assert not any("moitié gauche" in i for i in fiche("annual aggregation"))
    faux = fiche("no temporal aggregation")
    assert any("moitié gauche" in i for i in faux), faux


def test_un_process_qui_n_agrege_pas_le_dit(tmp_path):
    """`time_step` ne suffit pas à conclure.

    `RAl_ratio` P2 divise deux séries déjà annuelles : son `time_step`
    est `year` et pourtant l'étape n'agrège rien. Sans la lecture du
    grain amont, sa moitié gauche paraîtrait fausse.
    """
    from card.schema import validate_card
    p = tmp_path / "sansagreg.yaml"
    p.write_text(
        'id: sansagreg\nversion: "1.0"\nauthors: ["t"]\ndate: "2026-08-03"\n'
        "meta:\n"
        "  en:\n    variable: r\n    unit: m\n    name: R\n"
        "    method:\n      P1:\n        a: annual aggregation - sum of Q\n"
        "        b: annual aggregation - sum of R\n"
        "      P2:\n        r: no temporal aggregation - ratio of a to b\n"
        "    classification: {domain: flow, season: annual, output: series}\n"
        "  fr:\n    variable: r\n    unit: m\n    name: R\n"
        "    method:\n      P1:\n        a: agrégation annuelle - somme de Q\n"
        "        b: agrégation annuelle - somme de R\n"
        "      P2:\n        r: aucune agrégation temporelle - rapport de a sur b\n"
        "    classification: {domain: débit, season: annuelle, output: série}\n"
        "  global:\n    input_vars: \"Q, R\"\n"
        "process:\n"
        "  P1:\n    func:\n      a: [nansum, \"Q\"]\n      b: [nansum, \"R\"]\n"
        "  P2:\n    func:\n      r: [ratio, \"a\", \"b\"]\n",
        encoding="utf-8")
    issues = validate_card(p)
    assert not any("moitié gauche" in i for i in issues), issues


def _ecrire(tmp_path, method_en, method_fr):
    """Fiche minimale à deux process, le second produisant deux colonnes."""
    p = tmp_path / "essai.yaml"
    p.write_text(
        'id: essai\nversion: "1.0"\nauthors: ["t"]\ndate: "2026-08-03"\n'
        "meta:\n"
        "  en:\n    variable: [a, b]\n    unit: [m, m]\n"
        "    name: [A, B]\n"
        f"    method:\n{method_en}"
        "    classification: {domain: flow, season: annual, output: series}\n"
        "  fr:\n    variable: [a, b]\n    unit: [m, m]\n"
        "    name: [A, B]\n"
        f"    method:\n{method_fr}"
        "    classification: {domain: débit, season: annuelle, output: série}\n"
        "  global:\n    input_vars: Q\n"
        "process:\n"
        "  P1:\n    func:\n      X: [nanmean, \"Q\"]\n    time_step: none\n"
        "  P2:\n    func:\n      a: [nanmax, \"X\"]\n      b: [nanmin, \"X\"]\n",
        encoding="utf-8")
    return load_card(p)


def test_le_collage_suit_la_colonne_demandee(tmp_path):
    """Chaque sortie reçoit SA phrase au process qui la produit.

    Le process amont n'en a qu'une, il la donne aux deux : c'est le
    défaut d'allLF, dont les P1 à P3 étaient recopiés cinq fois puis
    édités à la main, et avaient divergé.
    """
    c = _ecrire(
        tmp_path,
        "      P1:\n        X: no temporal aggregation - centered moving average\n"
        "      P2:\n        a: annual aggregation - maximum of X\n"
        "        b: annual aggregation - minimum of X\n",
        "      P1:\n        X: aucune agrégation temporelle - moyenne mobile centrée\n"
        "      P2:\n        a: agrégation annuelle - maximum de X\n"
        "        b: agrégation annuelle - minimum de X\n")
    assert M.published(c, "fr") == [
        "1. aucune agrégation temporelle - moyenne mobile centrée\n"
        "2. agrégation annuelle - maximum de X",
        "1. aucune agrégation temporelle - moyenne mobile centrée\n"
        "2. agrégation annuelle - minimum de X",
    ]
    assert M.published(c, "en")[1].endswith("minimum of X")
