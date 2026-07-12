# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
# *2 INRAE, UMR G-Eau, Montpellier, France
# *3 IRSTEA, France
#
# This file is part of the card Python package (Python port of the
# CARD R package).
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.
#
# card is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.

"""Validation structurelle des fiches CARD YAML (linter, sans dépendance).

Usage :
    from card.schema import validate_card, lint_cards
    issues = validate_card("QA.yaml")          # liste de problèmes (vide = ok)
    report = lint_cards()                       # {fiche: [issues]} sur le corpus

    python -m card.schema                       # linter en ligne de commande

Contrôles :
- structure (id, meta en/fr/global, process P1..Pn consécutifs) ;
- tuples func bien formés et fonctions résolubles (card.functions/numpy) ;
- champs process valides (time_step, keep, max_na_pct, sampling_period) ;
- cohérence des longueurs des listes meta (variable/name/...) ;
- cohérence fenêtre meta ↔ process : une fenêtre partielle déclarée en
  meta doit se retrouver dans un sampling_period de process (le contrôle
  qui aurait détecté la perte de borne de fin sur 29 fiches).
"""

import datetime as _dt
import re
from pathlib import Path

from .extraction import _DEFAULT_CARD_DIR, resolve
from .loader import load_card

_VALID_TIME_STEPS = {"year", "year-month", "month", "year-season",
                     "season", "yearday", "none"}
_MMDD = re.compile(r"^\d{2}-\d{2}$")


def _parse_mmdd(s):
    if not isinstance(s, str) or not _MMDD.match(s):
        return None
    m, d = int(s[:2]), int(s[3:])
    try:
        return _dt.date(2001, m, d)      # année non bissextile de référence
    except ValueError:
        return None


def _is_full_year_window(start, end):
    """[start, end] couvre-t-il toute l'année (end = veille de start) ?"""
    ds, de = _parse_mmdd(start), _parse_mmdd(end)
    if ds is None or de is None:
        return None                       # non analysable (ex. 02-28(29))
    return de == ds - _dt.timedelta(days=1) or (ds, de) == (
        _dt.date(2001, 1, 1), _dt.date(2001, 12, 31))


def _check_meta_lists(meta_lang, prefix, issues):
    variable = meta_lang.get("variable")
    if variable is None:
        issues.append(f"{prefix}: champ 'variable' manquant")
        return
    if isinstance(variable, list):
        n = len(variable)
        for field in ("name", "description", "method", "sampling_period"):
            v = meta_lang.get(field)
            if isinstance(v, list) and not (
                    v and isinstance(v[0], str) and len(v) == 2
                    and field == "sampling_period"):
                if len(v) not in (n, 2):
                    issues.append(
                        f"{prefix}.{field}: liste de longueur {len(v)} "
                        f"pour {n} variables"
                    )


def _windows_in_processes(processes):
    """Fenêtres [début, fin] présentes dans les sampling_period process."""
    windows = set()
    for proc in processes:
        sp = proc["sampling_period"]
        if isinstance(sp, list) and len(sp) == 2 \
                and all(isinstance(x, str) for x in sp):
            windows.add(tuple(sp))
    return windows


def _check_window_coherence(card, issues):
    """Fenêtre partielle en meta.en.sampling_period → un process doit
    porter la même fenêtre (sauf time_steps saisonniers/mensuels, gérés
    par Seasons ou le découpage temporel)."""
    sp = card["meta"]["en"].get("sampling_period")
    if not (isinstance(sp, list) and len(sp) == 2
            and all(isinstance(x, str) for x in sp)):
        return                           # texte libre, liste de listes...
    full = _is_full_year_window(sp[0], sp[1])
    if full is None or full:
        return
    exempt_steps = {"year-month", "month", "year-season", "season", "yearday"}
    if all(p["time_step"] in exempt_steps for p in card["processes"]):
        return
    if tuple(sp) not in _windows_in_processes(card["processes"]):
        issues.append(
            f"meta.en.sampling_period {sp} est une fenêtre partielle mais "
            "aucun process ne porte cette fenêtre en sampling_period "
            "(borne de fin perdue ?)"
        )


def _check_process(proc, issues):
    name = proc["name"]
    if proc["time_step"] not in _VALID_TIME_STEPS:
        issues.append(f"{name}.time_step invalide : {proc['time_step']!r}")

    keep = proc["keep"]
    if keep is not None and keep != "all" and not isinstance(keep, list):
        issues.append(f"{name}.keep invalide : {keep!r}")

    napct = proc["max_na_pct"]
    if napct is not None and not (isinstance(napct, (int, float))
                                  and 0 <= napct <= 100):
        issues.append(f"{name}.max_na_pct invalide : {napct!r}")

    sp = proc["sampling_period"]
    if isinstance(sp, str) and _parse_mmdd(sp) is None:
        issues.append(f"{name}.sampling_period invalide : {sp!r}")
    elif isinstance(sp, list):
        if len(sp) != 2 or any(_parse_mmdd(x) is None for x in sp):
            issues.append(f"{name}.sampling_period invalide : {sp!r}")

    for entry in proc["func"]:
        try:
            resolve(entry["fn_name"])
        except KeyError:
            issues.append(
                f"{name}.func.{entry['name']}: fonction inconnue "
                f"'{entry['fn_name']}'"
            )
    if isinstance(sp, dict):
        try:
            resolve(sp["func"]["fn_name"])
        except KeyError:
            issues.append(
                f"{name}.sampling_period: fonction inconnue "
                f"'{sp['funct']['fn_name']}'"
            )


def validate_card(path) -> list[str]:
    """Retourne la liste des problèmes détectés (vide si la fiche est valide)."""
    issues: list[str] = []
    try:
        card = load_card(path)
    except Exception as e:
        return [f"chargement impossible : {type(e).__name__}: {e}"]

    if not card.get("id"):
        issues.append("champ 'id' manquant")
    if Path(path).stem != card.get("id"):
        issues.append(
            f"id '{card.get('id')}' ≠ nom de fichier '{Path(path).stem}'"
        )

    for lang in ("en", "fr"):
        _check_meta_lists(card["meta"][lang], f"meta.{lang}", issues)

    var_en = card["meta"]["en"].get("variable")
    var_fr = card["meta"]["fr"].get("variable")
    if isinstance(var_en, list) != isinstance(var_fr, list) or (
            isinstance(var_en, list) and len(var_en) != len(var_fr or [])):
        issues.append("meta: variable en/fr de formes différentes")

    for proc in card["processes"]:
        _check_process(proc, issues)

    _check_window_coherence(card, issues)
    return issues


def lint_cards(CARD_path=None) -> dict:
    """Valide toutes les fiches d'une arborescence.
    Retourne {nom_de_fiche: [issues]} pour les fiches en défaut."""
    root = Path(CARD_path) if CARD_path else _DEFAULT_CARD_DIR
    report = {}
    for p in sorted(root.rglob("*.yaml")):
        issues = validate_card(p)
        if issues:
            report[p.stem] = issues
    return report


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else None
    report = lint_cards(path)
    if not report:
        print("✓ toutes les fiches sont valides")
        return 0
    for name, issues in report.items():
        for issue in issues:
            print(f"✗ {name}: {issue}")
    print(f"\n{len(report)} fiche(s) en défaut")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
