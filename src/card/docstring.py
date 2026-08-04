# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Lecture des docstrings bilingues des fonctions hydro.

Une docstring de fonction hydro se lit comme une FICHE : `en:` puis `fr:`
portent la description, à égalité et dans cet ordre, et ce qui n'a pas de
langue reste hors bloc. C'est le découpage de `meta.en` / `meta.fr` /
`meta.global`, appliqué au code, et les codes sont ceux des fiches, ISO
639-1 en minuscules.

Pourquoi dans la docstring plutôt qu'ailleurs. Aucun standard Python ne
traduit un `__doc__` à l'exécution : `gettext` ne peut pas l'envelopper
dans `_()`, qui l'empêcherait d'être un littéral, et `sphinx-intl`
traduit à la construction de la doc, quand notre lecteur est un rendu
fait à la volée. Restait à choisir, et une traduction rangée loin de son
original dérive sans que personne ne le voie.

**Qui lit ces blocs.** Plus la figure d'une fiche : elle affichait la
première phrase de la docstring sous chaque étape, et une docstring est
attachée à une FONCTION, donc elle ne peut dire que du général.
`apply_threshold` mesurait ici une durée de crue et datait ailleurs un
début d'étiage, sous la même phrase. La figure lit désormais le `method`
de la fiche, écrit par étape.

Leurs lecteurs restent `help(card.functions.apply_threshold)` et la
personne qui ouvre le fichier, et c'est assez. Un rendu web de ces blocs
a été conçu puis abandonné le 2026-08-03 : un rendu texte d'une
docstring est du code recopié en moins bien, et qui veut l'algorithme
veut le code (docs/dev/archive/PLAN_METHOD.md, « Pourquoi le lot E a été
abandonné »). Le format bilingue reste tenu par des tests, il n'a pas
besoin d'une page pour exister.
"""

import inspect
import re

LANGUES = ("en", "fr")
_MARQUEUR = re.compile(r"^(" + "|".join(LANGUES) + r"):[ \t]*(.*)$")


def blocs(doc):
    """Découpe une docstring en {langue: texte}, notes hors langue exclues.

    Un marqueur en marge ouvre un bloc ; les lignes INDENTÉES sous lui le
    continuent, paragraphes compris. Une ligne revenue en marge sans
    marqueur clôt le bloc : c'est une note, qui n'a pas de langue (parité
    R, dates, renvois vers docs/dev/), et qu'on ne traduit donc pas, sous
    peine d'entretenir deux versions d'un même fait daté.

    Le `\"\"\"` seul sur sa ligne n'est pas une coquetterie : il donne à
    TOUS les blocs la même indentation, donc une seule règle sans
    exception. Une exception dans une règle de lecture est ce qui produit
    les bugs que ce module a coûté une semaine à corriger.
    """
    lignes = inspect.cleandoc(doc or "").split("\n")
    sortie, notes, courant = {}, [], None
    for ligne in lignes:
        m = _MARQUEUR.match(ligne)
        if m:
            courant = m.group(1)
            sortie.setdefault(courant, []).append(m.group(2))
            continue
        if ligne.strip() and not ligne[:1].isspace():
            courant = None                    # retour en marge : note
        (sortie[courant] if courant else notes).append(ligne.strip())
    return {k: "\n".join(v).strip() for k, v in sortie.items()}


def paragraphe(doc, lang):
    """Le premier paragraphe de la langue demandée, replié sur une ligne.

    Sans bloc de langue (fonction écrite par un tiers), on rend le début
    de la docstring telle quelle : une phrase non traduite renseigne
    encore, une ligne absente n'apprend rien. Un test exige les deux
    blocs pour toute fonction du corpus, donc ce repli ne joue que
    dehors.
    """
    b = blocs(doc)
    if b:
        texte = b.get(lang) or next(iter(b.values()))
    else:
        texte = inspect.cleandoc(doc or "")
    return re.sub(r"\s+", " ", texte.split("\n\n")[0]).strip()
