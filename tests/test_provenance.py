"""Un résultat doit dire avec quel LOGICIEL il a été calculé.

La difficulté de ce test est qu'il tourne dans UN mode d'installation
(éditable, ici) alors que la fonction en couvre quatre. On n'éprouve donc
pas l'environnement courant, on éprouve la RÈGLE : chaque étape de la
résolution est mise face à une situation fabriquée, et la seule chose
demandée à l'environnement réel est de ne jamais mentir.

Doctrine et ordre de résolution : docstring de `card/provenance.py`.
"""

import json
import sys

import pytest

import card  # noqa: F401  (importe card.provenance au passage)
from card.provenance import _SHA1, _commit, _commit_du_depot, provenance, swhid

# `card.provenance` est la FONCTION (exportée par `__init__`), donc on
# atteint le module par sys.modules plutôt que par le paquet : un
# `import card.provenance` rebrancherait l'attribut sur le module et
# casserait `card.provenance()` pour les tests suivants.
MODULE = sys.modules["card.provenance"]

FAUX = "0" * 40
AUTRE = "1" * 40


class _Module:
    """Un paquet quelconque, vu par la résolution."""

    def __init__(self, fichier=None, version=None):
        if fichier is not None:
            self.__file__ = fichier
        if version is not None:
            self.__version__ = version


def test_les_quatre_champs_sont_toujours_la():
    p = provenance()
    assert set(p) == {"card_version", "card_commit",
                      "stase_version", "stase_commit"}


def test_aucun_commit_inventé():
    """Un commit publié est un sha1, ou rien. Jamais « main », jamais
    « dev », jamais une valeur abrégée : on citerait un état inexistant.
    """
    for cle in ("card_commit", "stase_commit"):
        valeur = provenance()[cle]
        assert valeur is None or _SHA1.match(valeur), valeur


def test_les_versions_sont_celles_des_paquets():
    """Lues dans la source, donc justes même en installation éditable, où
    `importlib.metadata` rend la valeur du dernier `pip install -e`.
    """
    import stase

    p = provenance()
    assert p["card_version"] == card.__version__
    assert p["stase_version"] == stase.__version__


def test_environnement_prioritaire(monkeypatch):
    """Le cas de l'image construite depuis une archive : personne d'autre
    que son constructeur ne connaît le commit, il le dit par là.
    """
    monkeypatch.setenv("CARD_COMMIT", FAUX)
    assert _commit("card", ("card-stase",), _Module()) == FAUX


def test_environnement_mal_formé_refusé(monkeypatch):
    """`CARD_COMMIT=main` ne doit pas faire publier « main »."""
    monkeypatch.setenv("CARD_COMMIT", "main")
    assert _commit("card", ("inexistant-xyz",), _Module()) is None


def test_pep_610_installation_depuis_git(monkeypatch, tmp_path):
    """Le cas mesuré le 2026-08-05 sur une vraie installation GitHub."""
    monkeypatch.setattr(
        MODULE, "_direct_url",
        lambda noms: {"url": "https://github.com/lou-heraut/card.git",
                      "vcs_info": {"vcs": "git", "commit_id": AUTRE,
                                   "requested_revision": "v0.3.1"}})
    assert _commit("card", ("card-stase",), _Module()) == AUTRE


def test_copie_de_travail_propre(tmp_path):
    depot = _depot_git(tmp_path)
    commit = _commit_du_depot(depot)
    assert commit and _SHA1.match(commit)


def test_copie_modifiée_ne_publie_pas_de_commit(tmp_path):
    """Le code qui tourne est alors le commit PLUS des modifications :
    annoncer le commit seul serait faux.
    """
    depot = _depot_git(tmp_path)
    (depot / "suivi.txt").write_text("modifié après le commit\n")
    assert _commit_du_depot(depot) is None


def test_un_brouillon_non_suivi_ne_compte_pas(tmp_path):
    """Ce qui n'est pas suivi par git ne change pas le code exécuté, et
    ne regarde personne.
    """
    depot = _depot_git(tmp_path)
    (depot / "note.txt").write_text("brouillon\n")
    assert _commit_du_depot(depot) is not None


def test_hors_de_tout_depot(tmp_path):
    assert _commit_du_depot(tmp_path / "nulle-part") is None


def test_swhid():
    assert swhid(FAUX) == f"swh:1:rev:{FAUX}"
    assert swhid(None) is None


def test_les_colonnes_voyagent_avec_le_resultat():
    """Le but du chantier : un `meta` exporté seul dit avec quel logiciel
    il a été produit.
    """
    meta = card.extract(None, cards=["QA"], metadata_only=True)["meta"]
    for colonne, attendu in provenance().items():
        assert colonne in meta.columns
        assert set(meta[colonne]) == {attendu}


def _depot_git(racine):
    """Un petit dépôt git réel : la résolution parle à git, pas à un
    simulacre, sinon le test ne dirait rien de ce qui se passe en vrai.
    """
    import subprocess

    depot = racine / "depot"
    depot.mkdir()
    lancer = lambda *a: subprocess.run(  # noqa: E731
        ("git", "-C", str(depot)) + a, capture_output=True, check=True)
    try:
        lancer("init", "-q")
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("git indisponible")
    lancer("config", "user.email", "test@example.org")
    lancer("config", "user.name", "test")
    (depot / "suivi.txt").write_text("premier état\n")
    lancer("add", "suivi.txt")
    lancer("commit", "-q", "-m", "premier")
    return depot


def test_direct_url_illisible_ne_casse_rien(monkeypatch, tmp_path):
    """Un `direct_url.json` corrompu ne doit pas faire échouer une
    extraction : la provenance est une information, pas une condition.
    """
    monkeypatch.setattr(MODULE, "_direct_url", lambda noms: json.loads("{}"))
    assert _commit("card", ("card-stase",), _Module()) is None
