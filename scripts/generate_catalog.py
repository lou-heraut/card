# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Génère docs/CARDS.md — catalogue des fiches CARD, consultable sur GitHub.

Usage (depuis la racine du repo) :
    .python_env/bin/python scripts/generate_catalog.py

À relancer après tout ajout/modification de fiche YAML.
"""

import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT.parent.parent / "EXstat_project" / "stase" / "src"))

from card.extraction import _DEFAULT_CARD_DIR, _find_cards, _meta_frame  # noqa: E402
from card.loader import load_card  # noqa: E402
from card.schema import input_registry  # noqa: E402


def _inputs_with_units(raw):
    reg = input_registry()
    out = []
    for var in str(raw).split(","):
        var = var.strip()
        unit = reg.get(var, {}).get("unit") or reg.get(var, {}).get("type")
        out.append(f"{var} [{unit}]" if unit else var)
    return ", ".join(out)

OUT = ROOT / "docs" / "CARDS.md"


def main():
    cards = _find_cards(_DEFAULT_CARD_DIR, None)
    sections = defaultdict(list)   # chemin thématique -> [(nom, meta_df, path)]

    for name, path in sorted(cards.items()):
        rel = path.relative_to(_DEFAULT_CARD_DIR)
        section = " / ".join(p.replace("_", " ") for p in rel.parts[:-1])
        # _meta_frame (et non _meta_rows) : le catalogue doit montrer la
        # forme par défaut d'une fiche à placeholders, jamais l'accolade.
        meta = _meta_frame(load_card(path))
        sections[section].append((name, meta, rel))

    n_cards = len(cards)
    n_vars = sum(len(m) for grp in sections.values() for _, m, _ in grp)

    lines = [
        "# Catalogue des fiches CARD",
        "",
        f"{n_cards} fiches, {n_vars} variables. "
        "Généré par `scripts/generate_catalog.py`, ne pas éditer à la main.",
        "",
        "Chaque fiche s'exécute via "
        "`card.extract(data, cards=[...])` ; la colonne *entrées* "
        "indique les colonnes que `data` doit contenir "
        "(cf. `rename=` pour la correspondance). Détail d'une fiche : "
        "`card.info(\"nom\")`.",
        "",
    ]

    for section in sorted(sections):
        lines += [f"## {section}", ""]
        lines += ["| fiche | variable(s) | nom | phénomène | aspect | saison "
                  "| unité | entrées | exp. |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for name, meta, rel in sections[section]:
            variables = ", ".join(str(v) for v in meta["variable_en"])
            label = str(meta["name_fr"].iloc[0]) or str(meta["name_en"].iloc[0])
            unit = str(meta["unit_en"].iloc[0])
            inputs = _inputs_with_units(meta["input_vars"].iloc[0])
            exp = "⚠" if bool(meta["is_experimental"].iloc[0]) else ""

            def facet(col):
                vals = [str(v) for v in meta[col] if str(v)]
                uniq = sorted(set(vals), key=vals.index)
                return ", ".join(uniq)

            phen = facet("phenomenon_fr") or facet("purpose_fr")
            aspect = facet("aspect_fr")
            season = facet("season_fr")
            link = (f"[{name}](https://github.com/lou-heraut/card/"
                    f"blob/main/src/card/cards/{rel.as_posix()})")
            lines.append(
                f"| {link} | {variables} | {label} | {phen} | {aspect} "
                f"| {season} | {unit} | {inputs} | {exp} |"
            )
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{OUT} : {n_cards} fiches, {n_vars} variables, "
          f"{len(sections)} sections")


if __name__ == "__main__":
    main()
