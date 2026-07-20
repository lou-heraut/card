"""Suffixes de scénario et métadonnées évolutives.

Une même fiche peut être appliquée à plusieurs variantes d'une entrée :
plusieurs seuils réglementaires (DOE, DCR), une observation et une
simulation (obs, sim), plusieurs horizons. stase éclate les VALEURS au
niveau colonne (cf. son paramètre suffix) ; ce module s'occupe des
MÉTADONNÉES, et de rien d'autre. Aucun placeholder ne peut changer un
calcul : le pire défaut possible ici est une phrase bancale, jamais un
chiffre faux.

Un suffixe est un enregistrement, pas une simple étiquette : un nom
court (H1, DOE), un nom long (« horizon proche »), et autant de champs
complémentaires que la fiche en demande (une période, par exemple).
La fiche les déclare, l'appelant peut les compléter ou les remplacer.

  meta.<lang>.suffixes        {clé: {champ: valeur}}  ensemble fermé
  meta.<lang>.suffix_default  {champ: valeur}         cas sans suffixe

En prose, `{suffix}` vaut `{suffix.short}`, et `{suffix.<champ>}`
désigne n'importe quel champ. Le jeu de champs n'est pas fermé par le
code : un besoin nouveau s'exprime dans les fiches, pas ici.

Trois règles (cf. docs/dev/CHANTIERS.md §9) :
  1. aucune accolade ne sort jamais non résolue d'un champ de meta ;
  2. une fiche qui utilise {suffix.X} déclare X dans son suffix_default,
     dans chaque langue (vérifié par le linter, sans données) ;
  3. si un suffixe fourni ne porte pas un champ, `short` et `name`
     retombent sur LA CLÉ, jamais sur le défaut de la fiche : retomber
     sur le défaut donnerait le même nom à deux variantes, soit
     exactement l'ambiguïté qu'on veut lever. Les autres champs n'ont
     pas de repli sensible et lèvent une erreur explicite.
"""

import re

LANGS = ("en", "fr")

# Champs de meta.<lang> soumis à la substitution.
TEXT_FIELDS = ("unit", "name", "description", "method", "sampling_period")

_PLACEHOLDER = re.compile(r"\{suffix(?:\.([A-Za-z_][A-Za-z0-9_]*))?\}")


def fields_used(value) -> set:
    """Champs de suffixe référencés par un texte (récursif sur listes)."""
    if isinstance(value, str):
        return {m.group(1) or "short" for m in _PLACEHOLDER.finditer(value)}
    if isinstance(value, (list, tuple)):
        used = set()
        for v in value:
            used |= fields_used(v)
        return used
    return set()


def card_fields_used(meta_lang) -> set:
    """Champs référencés par l'ensemble des champs texte d'une langue."""
    used = set()
    for field in TEXT_FIELDS:
        used |= fields_used(meta_lang.get(field))
    return used


def _record_by_lang(value):
    """Normalise la valeur d'un suffixe fourni à l'appel.

    "simulation"                        -> même nom long dans toutes les langues
    {"en": {...}, "fr": {...}}          -> enregistrement par langue
    {"name": ..., "period": ...}        -> même enregistrement dans toutes
    """
    if value is None:
        return {lang: {} for lang in LANGS}
    if isinstance(value, str):
        return {lang: {"name": value} for lang in LANGS}
    if not isinstance(value, dict):
        raise TypeError(
            f"suffix : valeur invalide {value!r}. Attendu une chaîne (nom "
            "long) ou un dict de champs, éventuellement par langue."
        )
    if value and set(value) <= set(LANGS):
        return {lang: dict(value.get(lang) or {}) for lang in LANGS}
    return {lang: dict(value) for lang in LANGS}


def normalize(suffix):
    """suffix= de card.extract -> (clés, enregistrements par clé et langue).

    Accepte une liste de clés (les noms longs valent alors la clé) ou un
    dict {clé: valeur} dont les valeurs suivent _record_by_lang.
    """
    if suffix is None:
        return [], {}
    if isinstance(suffix, str):
        suffix = [suffix]
    if isinstance(suffix, (list, tuple, set)):
        keys = [str(k) for k in suffix]
        return keys, {k: _record_by_lang(None) for k in keys}
    if isinstance(suffix, dict):
        keys = [str(k) for k in suffix]
        return keys, {str(k): _record_by_lang(v) for k, v in suffix.items()}
    raise TypeError(
        f"suffix : type invalide {type(suffix).__name__}. Attendu une liste "
        "de clés ou un dict {clé: champs}."
    )


def record(key, lang, meta_lang, records):
    """Enregistrement effectif d'un suffixe : clé, puis fiche, puis appel.

    L'appelant gagne champ par champ : la fiche fournit le sens par
    défaut, l'appelant l'adapte à son étude sans la forker.
    """
    rec = {"short": key, "name": key}
    declared = (meta_lang.get("suffixes") or {}).get(key)
    if declared:
        rec.update(declared)
    rec.update((records.get(key) or {}).get(lang) or {})
    return rec


def default_record(meta_lang):
    """Enregistrement du cas sans suffixe, déclaré par la fiche."""
    return dict(meta_lang.get("suffix_default") or {})


def substitute(value, rec, *, card_id, lang, field, key=None):
    """Remplace les placeholders d'un texte (récursif sur les listes)."""
    if isinstance(value, (list, tuple)):
        return [substitute(v, rec, card_id=card_id, lang=lang, field=field,
                           key=key) for v in value]
    if not isinstance(value, str):
        return value

    def _one(m):
        name = m.group(1) or "short"
        if name in rec and rec[name] is not None:
            return str(rec[name])
        if key is None:
            raise ValueError(
                f"{card_id} : meta.{lang}.{field} utilise "
                f"{{suffix.{name}}} mais meta.{lang}.suffix_default ne "
                f"déclare pas '{name}'. Une fiche doit rester lisible sans "
                "suffixe (cf. CHANTIERS §9, règle 2)."
            )
        raise ValueError(
            f"{card_id} : meta.{lang}.{field} utilise {{suffix.{name}}} "
            f"mais le suffixe '{key}' ne fournit pas '{name}'. Passez-le à "
            f"l'appel, ex. suffix={{'{key}': {{'{lang}': "
            f"{{'{name}': ...}}}}}}."
        )

    return _PLACEHOLDER.sub(_one, value)


def apply(meta_lang, rec, *, card_id, lang, key=None):
    """Champs texte d'une langue, placeholders résolus.

    Une fiche SANS placeholder qui reçoit un suffixe voit son `name`
    complété en fin de chaîne : c'est le cas obs/sim, applicable à
    n'importe quelle fiche du corpus, dont aucune n'a de placeholder.
    Sur `name` seul, puisque c'est lui qui sert de titre de graphique.
    """
    out = {}
    for field in TEXT_FIELDS:
        if field not in meta_lang:
            continue
        out[field] = substitute(meta_lang[field], rec, card_id=card_id,
                                lang=lang, field=field, key=key)

    if key is not None and not card_fields_used(meta_lang):
        name = out.get("name")
        label = rec.get("name") or key
        if isinstance(name, str) and name:
            out["name"] = f"{name} ({label})"
        elif isinstance(name, list):
            out["name"] = [f"{n} ({label})" if isinstance(n, str) and n else n
                           for n in name]
    return out
