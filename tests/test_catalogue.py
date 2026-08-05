"""Le catalogue et le décompte du corpus sont générés : ils doivent être
à jour dans le dépôt.

`docs/CARDS.md` et le décompte du README (entre les balises
`<!-- cards:count -->`) sortent tous deux de `scripts/generate_catalog.py`.
Rien ne les surveillait : leur fraîcheur reposait sur une consigne écrite
dans le CLAUDE.md et dans le README, donc sur la mémoire de qui touche
une fiche. Une consigne ne rougit pas.

Le catalogue est régénéré ICI, en mémoire, puis confronté aux fichiers
versionnés. Ajouter une fiche sans relancer le script fait donc échouer
la suite, en local comme en CI, et le message dit la commande qui répare.
"""

import generate_catalog as gc

RELANCE = "relance `python scripts/generate_catalog.py`"


def test_catalogue_et_decompte_a_jour():
    texte, n_cards, n_vars, _ = gc.render()

    assert gc.OUT.exists(), f"{gc.OUT} manque : {RELANCE}"
    assert gc.OUT.read_text(encoding="utf-8") == texte, (
        f"{gc.OUT.name} ne correspond plus aux fiches du dépôt : {RELANCE}"
    )

    m = gc.README_COUNT.search(gc.README.read_text(encoding="utf-8"))
    assert m, (
        "les balises <!-- cards:count --> ont disparu du README : elles sont "
        "le seul endroit où le décompte du corpus est écrit"
    )
    attendu = gc.count_label(n_cards, n_vars)
    assert m.group(2) == attendu, (
        f"le README annonce « {m.group(2)} » pour un corpus qui en compte "
        f"« {attendu} » : {RELANCE}"
    )
