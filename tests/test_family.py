# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""La famille : les variantes d'un même concept.

Deux variables sont de la même famille quand elles ont les mêmes
composants sémantiques et ne diffèrent que par un PARAMÈTRE. C'est ce que
`skos:broader` exprimera dans l'export, et c'est calculé, jamais déclaré :
tout vient de facettes que la fiche affirme déjà, donc déclarer la famille
aurait ajouté une chose à tenir sans ajouter d'information.

Ce qui est mesuré ici est que la colonne reste ce qu'elle prétend être :
stable sous une reformulation de libellé, insensible aux paramètres de
période, et distincte d'une recherche par sous-chaîne.
"""

import pytest

import card


def test_the_family_gathers_the_variants_of_one_concept():
    """`VCN10` a trois frères, dont un que le nom ne montre pas.

    `QNA` est le minimum annuel du débit journalier, donc le cas d'une
    moyenne mobile d'UN jour : il appartient au même concept que `VCN3`,
    `VCN10` et `VCN30`. Une recherche par sous-chaîne ne le trouverait
    jamais, et c'est la raison d'être de cette colonne.
    """
    famille = set(card.list_cards(family_of="VCN10")["variable_en"])
    assert famille == {"QNA", "VCN3", "VCN10", "VCN30"}


def test_the_family_is_not_a_substring_search():
    """Les deux répondent à des questions différentes, et on les confond.

    `variable="VCN"` est une recherche de texte : elle rend `delta-VCN10`
    et `alpha-VCN10`, qui sont d'AUTRES concepts, et manque `QNA`.
    """
    par_nom = set(card.list_cards(variable="VCN")["variable_en"])
    par_famille = set(card.list_cards(family_of="VCN10")["variable_en"])
    assert "delta-VCN10" in par_nom and "delta-VCN10" not in par_famille
    assert "QNA" in par_famille and "QNA" not in par_nom


def test_the_period_parameters_do_not_split_a_family():
    """Une borne fournie par l'appelant n'est pas une grandeur mesurée.

    Les fiches à horizon déclarent `ref_start`, `horizon_end`… dans leurs
    `input_vars`. Les compter dans l'identité séparerait `delta-VCN10` de
    ses frères pour une raison qui n'a rien de sémantique, d'où le filtre
    sur `type: date` du registre `inputs.yaml`.
    """
    d = card.list_cards()
    famille = d.loc[d["variable_en"] == "delta-VCN10", "family"].iloc[0]
    assert "horizon" not in famille and "ref_" not in famille


def test_the_family_is_built_from_slugs_not_labels():
    """Un libellé reformulé ne doit pas changer l'identité d'une famille.

    C'est la raison d'être des slugs de `topics.yaml`, et la colonne s'en
    sert plutôt que des étiquettes affichées.
    """
    d = card.list_cards()
    famille = d.loc[d["variable_en"] == "VCN10", "family"].iloc[0]
    assert famille == "flow.low-flows.magnitude.minimum.annual.series.q"


def test_every_variable_has_a_family():
    """Une variable sans famille serait invisible à `skos:broader`."""
    d = card.list_cards()
    vides = d[d["family"].astype(str).str.strip() == ""]
    assert vides.empty, f"variables sans famille : {list(vides['variable_en'])}"


def test_family_of_refuses_an_unknown_name():
    """Un nom inconnu doit le dire, pas rendre un tableau vide.

    Une famille vide et une variable inexistante se ressemblent trop.
    """
    with pytest.raises(ValueError, match="aucune variable"):
        card.list_cards(family_of="CETTE_VARIABLE_N_EXISTE_PAS")
