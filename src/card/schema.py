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
  qui aurait détecté la perte de borne de fin sur 29 fiches) ;
- classification (docs/dev/TOPICS.md) : présence des facettes requises,
  valeurs au vocabulaire (topics.yaml), appariement en/fr, aspect
  interdit quand purpose est présent.
"""

import datetime as _dt
import re
from pathlib import Path

import yaml

from . import suffix as _sfx
from .extraction import _DEFAULT_CARD_DIR, resolve
from .loader import load_card

_VOCAB_PATH = Path(__file__).parent / "topics.yaml"
_VOCAB = None
_INPUTS_PATH = Path(__file__).parent / "inputs.yaml"
_INPUTS = None


def _vocab():
    global _VOCAB
    if _VOCAB is None:
        _VOCAB = yaml.safe_load(_VOCAB_PATH.read_text(encoding="utf-8"))
    return _VOCAB


def input_registry():
    """Registre {variable d'entrée: {unit, en, fr}} (inputs.yaml)."""
    global _INPUTS
    if _INPUTS is None:
        _INPUTS = yaml.safe_load(_INPUTS_PATH.read_text(encoding="utf-8"))
    return _INPUTS


def _check_inputs(card, issues):
    raw = card["meta"]["global"].get("input_vars", "X")
    for var in str(raw).split(","):
        var = var.strip()
        if var and var != "X" and var not in input_registry():
            issues.append(
                f"input_vars: '{var}' absent du registre des entrées "
                "(src/card/inputs.yaml)"
            )

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


# Noms d'agrégation à sémantique NaN ambiguë (numpy strict, pandas
# skipna, builtins dépendants de l'ordre...) : les fiches doivent dire
# ce qu'elles font, la variante nan* porte la sémantique dans son nom.
_AMBIGUOUS_FN_NAMES = {"mean", "median", "std", "var", "sum", "max",
                       "min", "amax", "amin", "argmax", "argmin"}


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
        if entry["fn_name"] in _AMBIGUOUS_FN_NAMES:
            issues.append(
                f"{name}.func.{entry['name']}: '{entry['fn_name']}' a une "
                "sémantique NaN ambiguë ; utiliser la variante "
                f"'nan{entry['fn_name'].lstrip('a')}' (skipna explicite) "
                "ou une fonction card.functions"
            )
    if isinstance(sp, dict):
        try:
            resolve(sp["func"]["fn_name"])
        except KeyError:
            issues.append(
                f"{name}.sampling_period: fonction inconnue "
                f"'{sp['funct']['fn_name']}'"
            )


# Convention des fenêtres adaptatives : le sens de l'adaptatif (couper
# l'année là où le phénomène est absent) et la fenêtre fixe de repli
# (preferred_sampling_period, prise par sampling_period="preferred" à
# l'extraction) sont fixés par le PHÉNOMÈNE, pas fiche par fiche.
_ADAPTIVE_BY_PHENOMENON = {
    "low flows":  ("nanmax", "01-01"),
    "high flows": ("nanmin", "09-01"),
}


def _check_adaptive_convention(card, issues):
    adaptive_fns = {proc["sampling_period"]["func"]["fn_name"]
                    for proc in card["processes"]
                    if isinstance(proc["sampling_period"], dict)}
    if not adaptive_fns:
        return
    preferred = card["meta"]["global"].get("preferred_sampling_period")
    if not preferred:
        issues.append(
            "sampling_period adaptatif sans "
            "meta.global.preferred_sampling_period : la fenêtre fixe de "
            "repli est requise (cf. sampling_period='preferred')"
        )
    phen = card["meta"]["en"].get("classification", {}).get("phenomenon")
    for p in (phen if isinstance(phen, list) else [phen] if phen else []):
        conv = _ADAPTIVE_BY_PHENOMENON.get(p)
        if conv is None:
            continue
        fn_expected, pref_expected = conv
        if adaptive_fns != {fn_expected}:
            issues.append(
                f"adaptatif {sorted(adaptive_fns)} incompatible avec "
                f"phenomenon '{p}' (convention : {fn_expected})"
            )
        if preferred and preferred != pref_expected:
            issues.append(
                f"preferred_sampling_period {preferred!r} incompatible "
                f"avec phenomenon '{p}' (convention : '{pref_expected}')"
            )


_CL_KEYS = ("domain", "phenomenon", "aspect", "season", "output", "purpose")
_CL_REQUIRED = ("domain", "season", "output")


def _check_classification(card, issues):
    vocab = _vocab()
    cl_en = card["meta"]["en"].get("classification")
    cl_fr = card["meta"]["fr"].get("classification")
    if not isinstance(cl_en, dict) or not isinstance(cl_fr, dict):
        issues.append("classification manquante (bloc requis en meta.en ET meta.fr)")
        return
    for lang, cl in (("en", cl_en), ("fr", cl_fr)):
        for k in cl:
            if k not in _CL_KEYS:
                issues.append(f"classification.{lang}: clé inconnue '{k}'")
        for k in _CL_REQUIRED:
            if k not in cl:
                issues.append(f"classification.{lang}: facette requise '{k}' absente")
    if set(cl_en) != set(cl_fr):
        issues.append("classification: clés différentes entre en et fr")
        return
    if "purpose" in cl_en and "aspect" in cl_en:
        issues.append("classification: aspect interdit quand purpose est présent")
    if "purpose" not in cl_en and "aspect" not in cl_en:
        issues.append("classification: aspect requis (sauf purpose présent)")

    for key in cl_en:
        ven, vfr = cl_en[key], cl_fr.get(key)
        len_ = isinstance(ven, list)
        if len_ != isinstance(vfr, list) or (len_ and len(ven) != len(vfr)):
            issues.append(f"classification.{key}: formes en/fr différentes")
            continue
        pairs = zip(ven, vfr) if len_ else [(ven, vfr)]
        for e, f in pairs:
            entry = vocab.get(key, {}).get(e)
            if entry is None:
                issues.append(f"classification.{key}: '{e}' hors vocabulaire")
            elif entry["fr"] != f:
                issues.append(
                    f"classification.{key}: '{e}' apparié à '{f}' "
                    f"(attendu '{entry['fr']}')"
                )


def _check_suffix(card, issues):
    """Placeholders {suffix.X} et vocabulaire de suffixes.

    Garantit qu'aucune accolade ne peut sortir non résolue : une fiche
    qui utilise un placeholder déclare son défaut, dans chaque langue.
    Une fiche reste ainsi lisible seule, et metadata_only, l'extraction
    sans suffixe et le catalogue produisent la même phrase.
    """
    used_any = False
    for lang in ("en", "fr"):
        meta_lang = card["meta"][lang]
        used = _sfx.card_fields_used(meta_lang)
        declared = meta_lang.get("suffix_default")
        used_any = used_any or bool(used)

        if used and not declared:
            issues.append(
                f"meta.{lang}: placeholder {{suffix}} utilisé sans "
                f"'suffix_default' (champs requis : {sorted(used)})"
            )
        elif used:
            manquants = sorted(f for f in used if f not in declared)
            if manquants:
                issues.append(
                    f"meta.{lang}.suffix_default: champs manquants "
                    f"{manquants} (utilisés par un placeholder)"
                )
        if declared and not isinstance(declared, dict):
            issues.append(f"meta.{lang}.suffix_default: dict attendu")

        suffixes = meta_lang.get("suffixes")
        if suffixes is not None:
            if not isinstance(suffixes, dict):
                issues.append(f"meta.{lang}.suffixes: dict attendu")
            else:
                for key, rec in suffixes.items():
                    if not isinstance(rec, dict):
                        issues.append(
                            f"meta.{lang}.suffixes.{key}: dict de champs attendu"
                        )

    if not used_any:
        for lang in ("en", "fr"):
            for field in ("suffix_default", "suffixes"):
                if card["meta"][lang].get(field) is not None:
                    issues.append(
                        f"meta.{lang}.{field}: déclaré mais aucun placeholder "
                        "{suffix} ne l'utilise (champ mort)"
                    )

    keys_en = set((card["meta"]["en"].get("suffixes") or {}))
    keys_fr = set((card["meta"]["fr"].get("suffixes") or {}))
    if keys_en != keys_fr:
        issues.append(
            f"meta.suffixes: clés en/fr différentes "
            f"({sorted(keys_en ^ keys_fr)})"
        )


_VERSION_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


def _check_version(card, issues):
    """La version d'une fiche est `majeur.mineur`, plus un `.patch`
    optionnel. Majeur = les SORTIES ont changé, mineur = method ou
    description, patch = le reste. Le champ doit être une chaîne : sans
    guillemets, YAML lit 1.10 comme le nombre 1.1, et deux versions
    distinctes deviennent la même."""
    v = card.get("version")
    if v is None:
        issues.append("champ 'version' manquant")
        return
    if not isinstance(v, str):
        issues.append(
            f"version {v!r} non citée : mettre des guillemets, sinon YAML la "
            "lit comme un nombre et 1.10 devient 1.1"
        )
        return
    if not _VERSION_RE.match(v):
        issues.append(
            f"version '{v}' mal formée : attendu majeur.mineur[.patch], "
            "chiffres uniquement"
        )
    elif v.endswith(".0") and v.count(".") == 2:
        issues.append(
            f"version '{v}' : un patch nul ne s'écrit pas, "
            f"utiliser '{v[:-2]}'"
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
    _check_version(card, issues)

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
    _check_adaptive_convention(card, issues)
    _check_classification(card, issues)
    _check_path_coherence(card, Path(path), issues)
    _check_inputs(card, issues)
    _check_suffix(card, issues)
    return issues


def _check_path_coherence(card, path, issues):
    """L'arborescence cards/<domain>/<output>/ doit refléter la
    classification (domaine premier si liste). Ignoré hors d'un dossier
    'cards' (fiches de test, copies utilisateur)."""
    parts = path.resolve().parts
    if "cards" not in parts or parts.index("cards") != len(parts) - 4:
        return
    cl = card["meta"]["en"].get("classification")
    if not isinstance(cl, dict):
        return                            # déjà signalé par ailleurs
    dom = cl.get("domain")
    dom = dom[0] if isinstance(dom, list) else dom
    expected = (dom, cl.get("output"))
    actual = (parts[-3], parts[-2])
    if expected != actual and None not in expected:
        issues.append(
            f"chemin cards/{actual[0]}/{actual[1]}/ ≠ classification "
            f"(attendu cards/{expected[0]}/{expected[1]}/)"
        )


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
