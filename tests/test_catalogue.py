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
        texte, n_cards, n_colonnes, _ = gc.render(lang)
        assert chemin.exists(), f"{chemin} manque : {RELANCE}"
        assert chemin.read_text(encoding="utf-8") == texte, (
            f"{chemin.name} ne correspond plus aux fiches du dépôt : {RELANCE}"
        )

    # Le décompte du README compte les variables DISTINCTES, pas les
    # lignes de ces deux catalogues, qui listent par fiche et comptent
    # donc deux fois les vingt-huit variables produites par deux fiches.
    _, n_vars = gc.render_site()
    assert n_vars < n_colonnes, (
        "si les deux comptes coïncident, plus rien ne distingue une "
        "variable d'une colonne, et ce test ne garde plus rien"
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
    page, n_entrees = gc.render_site()
    assert gc.SITE.exists(), f"{gc.SITE} manque : {RELANCE}"
    assert gc.SITE.read_text(encoding="utf-8") == page, (
        f"{gc.SITE.name} ne correspond plus aux fiches du dépôt : {RELANCE}"
    )
    assert n_entrees > 400, "une entrée par variable, pas par fiche"


def test_une_entree_par_variable_et_une_seule():
    """Une variable produite par DEUX fiches reste une seule entrée.

    Vingt-huit le sont, et c'est voulu (`centerLF` vient de sa fiche et
    de la fiche groupée `allLF`). En faire deux entrées donnerait deux
    lignes pour un même concept et, surtout, deux fois la même ancre :
    `#centerLF` ne désignerait plus rien de précis.
    """
    from card.management import list_cards

    page, n_entrees = gc.render_site()
    assert n_entrees == list_cards()["variable_en"].nunique()
    assert page.count('<details class="cat-row"') == n_entrees


def test_la_page_reste_lisible_sans_javascript():
    """Les entrées ENTIÈRES sont écrites à la construction.

    C'est la contrainte qui distingue cette page d'une application : le
    JavaScript ne fait que masquer des entrées déjà présentes, et le
    dépliage est celui du navigateur (`<details>`), donc il lui échappe.
    Sans elle, la page serait vide pour un moteur de recherche, pour un
    lecteur d'écran mal servi et pour qui coupe JS, alors que le
    catalogue markdown qu'elle remplace est indexable. On ne régresse pas
    là-dessus.
    """
    page, n_entrees = gc.render_site()
    # Chaque entrée porte ses DEUX langues, appariées : la bascule masque
    # l'une, elle ne va rien rechercher ailleurs. Un texte identique dans
    # les deux langues n'est écrit qu'une fois, d'où l'égalité entre les
    # deux comptes plutôt qu'un compte par entrée.
    assert page.count('lang="en"') == page.count('lang="fr"') > n_entrees
    # Le détail est dans la page, pas dans une requête : c'est ce qui
    # permet de le trouver par la recherche du navigateur.
    assert page.count('<div class="cat-detail">') == n_entrees


def test_pages_de_fiche_a_jour():
    """Une page par fiche, et rien qu'elles.

    Le dossier est entièrement engendré : une fiche renommée doit
    emporter sa page, sans quoi le site sert indéfiniment une définition
    qui n'existe plus. C'est ce que `clean: false` avait fait à card4r.
    """
    pages = gc.render_cards()
    for chemin, texte in pages.items():
        assert chemin.exists(), f"{chemin.name} manque : {RELANCE}"
        assert chemin.read_text(encoding="utf-8") == texte, (
            f"{chemin.name} ne correspond plus à sa fiche : {RELANCE}"
        )
    restantes = set(gc.CARTES.glob("*.md")) - set(pages)
    assert not restantes, (
        f"{len(restantes)} page(s) de fiche sans fiche : {RELANCE}"
    )


def test_le_site_ne_redessine_pas_les_fiches():
    """La page d'une fiche porte la figure de `card.figure()`, verbatim.

    C'est la règle qui empêche l'écosystème de raconter la même fiche de
    quatre façons : le terminal (`card.info`), R, l'API et le site
    montrent le MÊME dessin. Si un jour le site le reformate, il devient
    un cinquième rendu à tenir d'accord avec les autres.
    """
    from card.render import figure

    pages = gc.render_cards()
    texte = pages[gc.CARTES / "VCN10.md"]
    for lang in ("en", "fr"):
        dessin = figure("VCN10", lang=lang)
        # le dessin n'a rien à échapper, mais le générateur échappe
        # quand même : on compare donc sur une ligne qui le prouve
        assert "rollmean_center(Q)" in dessin
        assert dessin.splitlines()[-1] in texte
