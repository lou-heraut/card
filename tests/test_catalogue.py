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
    # Les deux langues sont générées du même corpus : en oublier une
    # laisserait un catalogue périmé sans que rien ne le dise, ce qui est
    # exactement ce que ce test existe pour empêcher.
    for lang, chemin in gc.OUT.items():
        texte, n_cards, n_vars, _ = gc.render(lang)
        assert chemin.exists(), f"{chemin} manque : {RELANCE}"
        assert chemin.read_text(encoding="utf-8") == texte, (
            f"{chemin.name} ne correspond plus aux fiches du dépôt : {RELANCE}"
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


def test_page_catalogue_du_site_a_jour():
    """La page du site est le TROISIÈME rendu du même corpus.

    Les deux markdown servent GitHub, celle-ci sert le site, `card.ttl`
    sert les machines. Trois artefacts générés dont deux périmeraient en
    silence si la garde n'en couvrait qu'un : c'est exactement ce qui
    était arrivé au `.ttl` avant que `test_skos.py` n'existe.
    """
    page, n_lignes = gc.render_site()
    assert gc.SITE.exists(), f"{gc.SITE} manque : {RELANCE}"
    assert gc.SITE.read_text(encoding="utf-8") == page, (
        f"{gc.SITE.name} ne correspond plus aux fiches du dépôt : {RELANCE}"
    )
    assert n_lignes > 400, "une ligne par variable produite, pas par fiche"


def test_la_page_reste_lisible_sans_javascript():
    """Le tableau ENTIER est écrit à la construction.

    C'est la contrainte qui distingue cette page d'une application : le
    JavaScript ne fait que masquer des lignes déjà présentes. Sans elle,
    la page serait vide pour un moteur de recherche, pour un lecteur
    d'écran mal servi et pour qui coupe JS, alors que le catalogue
    markdown qu'elle remplace est indexable. On ne régresse pas là-dessus.
    """
    page, n_lignes = gc.render_site()
    assert page.count("<tr data-domain=") == n_lignes, (
        "le tableau doit porter toutes ses lignes en HTML, pas les "
        "fabriquer côté navigateur"
    )
    # chaque ligne porte ses DEUX libellés : la bascule de langue masque
    # une colonne au lieu de recharger une autre page
    assert page.count('<td lang="en">') == n_lignes
    assert page.count('<td lang="fr">') == n_lignes
