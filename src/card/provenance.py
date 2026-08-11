# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Quel LOGICIEL a calculé ce résultat.

Trois niveaux de traçabilité voyagent avec une extraction : la
définition (le `swhid` de la fiche et sa `version`, posés par le
loader), le corpus et le moteur (ici), et pour un appel au service son
propre numéro (posé par card-api). Seul le premier existait quand card
était employé seul : un résultat calculé dans un carnet ne disait pas
avec quel code il l'avait été, alors que la même requête passée au
service était parfaitement tracée.

**Le numéro ne suffit pas, le commit fait foi.** Un numéro de version
ne désigne un état unique que le jour où il est coupé : `card` a
compté quatre-vingt-treize commits sous le même 0.2.0. Pire, dans une
installation ÉDITABLE il est figé au moment du `pip install -e` :
mesuré le 2026-08-05, cet environnement annonçait 0.1.0 pour des dépôts
en 0.3.1 et 0.6.0. Le commit, lui, désigne toujours un état et un seul,
et `swh:1:rev:<commit>` en est l'identifiant Software Heritage citable,
calculable sans appeler quoi que ce soit.

**Comment card connaît un commit**, dans cet ordre, chaque étape étant
la réponse à un mode d'installation réel (les quatre ont été mesurés le
2026-08-05) :

1. `CARD_COMMIT` / `STASE_COMMIT` dans l'environnement. C'est le seul
   cas que card ne peut pas observer : une image construite depuis une
   ARCHIVE (`.../archive/main.tar.gz`, ce que fait le Dockerfile de
   card-api) ne porte aucune trace de son commit. Celui qui a fabriqué
   l'image est le seul à le savoir, il le dit par là.
2. `direct_url.json` de la distribution installée, champ `vcs_info`
   (PEP 610) : une installation `pip install git+…@ref` y enregistre le
   `commit_id` résolu. Rien à fabriquer, la norme le fournit.
3. Même fichier, champ `dir_info.editable` : l'URL donne le chemin de la
   copie de travail, et git y répond. C'est le cas du développement.
4. Sinon, exécution depuis une copie du dépôt sans installation
   (`PYTHONPATH`), git est interrogé à côté du module lui-même.

Et si rien ne répond, **la valeur est vide**. Jamais de commit deviné.

**Une copie modifiée ne publie pas de commit.** Aux étapes 3 et 4, le
code qui tourne est le commit PLUS les modifications en cours : annoncer
le commit seul serait faux. On ne publie donc un commit que s'il est
exactement vrai, et une colonne vide dit alors quelque chose d'utile,
« ce résultat vient d'un code en cours d'édition, ne le cite pas ». Les
fichiers NON SUIVIS par git ne comptent pas : ce sont les brouillons de
qui travaille, ils ne changent pas le code exécuté.

`stase` n'a rien à implémenter pour ça, et c'est voulu : savoir comment
on a été installé n'est pas le métier d'un moteur d'agrégation. Ce qu'on
lit ici est un fait d'ENVIRONNEMENT, que celui qui assemble le résultat
observe pour le signer. C'est déjà ce que card-api faisait pour card et
stase, et il n'a plus qu'à consommer cette fonction.
"""

import json
import os
import re
import subprocess
from functools import lru_cache
from importlib import metadata
from pathlib import Path

# Un commit git est un sha1 : quarante caractères hexadécimaux. Tout ce
# qui n'a pas cette forme est refusé, y compris venant de
# l'environnement, sinon `CARD_COMMIT=main` publierait « main ».
_SHA1 = re.compile(r"\A[0-9a-f]{40}\Z")

# `card` est distribué sous le nom `card-stase` tant que la demande
# PEP 541 n'a pas abouti ; l'import reste `card`. Les deux noms sont
# donc à essayer, le définitif d'abord.
_PAQUETS = {"card": ("card", "card-stase"), "stase": ("stase",)}


def _version(noms, module):
    """Le numéro annoncé par le paquet.

    `module.__version__` d'abord : il est lu dans la SOURCE, donc juste
    même en installation éditable, là où `importlib.metadata` rend la
    valeur enregistrée au dernier `pip install -e` (mesuré : 0.1.0 pour
    des dépôts en 0.3.1 et 0.6.1). Les deux paquets le tiennent accordé
    au `pyproject.toml` par leur `set_version.py`, et leur
    `test_citation.py` refuse le désaccord.
    """
    depuis_source = getattr(module, "__version__", None)
    if depuis_source:
        return depuis_source
    for nom in noms:
        try:
            return metadata.version(nom)
        except metadata.PackageNotFoundError:
            continue
    return None


def _direct_url(noms):
    """Le `direct_url.json` de la PEP 610, s'il existe."""
    for nom in noms:
        try:
            texte = metadata.distribution(nom).read_text("direct_url.json")
        except metadata.PackageNotFoundError:
            continue
        if texte:
            try:
                return json.loads(texte)
            except ValueError:
                return None
    return None


def _git(dossier, *args):
    try:
        out = subprocess.run(("git", "-C", str(dossier)) + args,
                             capture_output=True, text=True, check=True,
                             timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip()


def _commit_du_depot(dossier):
    """Commit d'une copie de travail, et seulement si elle est propre.

    `--untracked-files=no` : un brouillon posé à côté ne change pas le
    code exécuté, et ce qui n'est pas suivi ne regarde personne.
    """
    if dossier is None or not Path(dossier).exists():
        return None
    if _git(dossier, "status", "--porcelain", "--untracked-files=no"):
        return None
    commit = _git(dossier, "rev-parse", "HEAD")
    return commit if commit and _SHA1.match(commit) else None


def _commit(cle, noms, module):
    env = os.environ.get(f"{cle.upper()}_COMMIT", "").strip()
    if _SHA1.match(env):
        return env

    infos = _direct_url(noms) or {}
    vcs = infos.get("vcs_info") or {}
    depuis_git = vcs.get("commit_id", "")
    if _SHA1.match(depuis_git):
        return depuis_git

    if (infos.get("dir_info") or {}).get("editable"):
        url = infos.get("url", "")
        if url.startswith("file://"):
            return _commit_du_depot(url[len("file://"):])

    fichier = getattr(module, "__file__", None)
    return _commit_du_depot(Path(fichier).parent if fichier else None)


@lru_cache(maxsize=1)
def provenance():
    """The software that computed, as it travels with the result.

    Returns
    -------
    dict
        ``card_version``, ``card_commit``, ``stase_version`` and
        ``stase_commit``. A commit is empty when the code comes from a
        modified working copy: a commit is published only when it
        designates exactly the code that ran.

    Notes
    -----
    Resolved once per process, since the answer cannot change without
    reinstalling or restarting, and :func:`card.extract` asks for it at
    every call.

    The keys carry the same names as the fields card-api publishes, so
    that a local result and a result from the service read the same way.
    """
    import card

    try:
        import stase
    except ImportError:                                  # jamais en usage réel
        stase = None

    modules = {"card": card, "stase": stase}
    out = {}
    for cle, noms in _PAQUETS.items():
        out[f"{cle}_version"] = _version(noms, modules[cle])
        out[f"{cle}_commit"] = _commit(cle, noms, modules[cle])
    return out


def swhid(commit):
    """Identifiant Software Heritage d'une révision, ou None.

    `swh:1:rev:` suivi du hash EST l'identifiant SWH d'un commit git, ils
    se calculent de la même façon. Aucun appel réseau, et il résout dès
    lors que le dépôt a été archivé une fois, ce qui est fait pour les
    trois depuis le 2026-07-22.
    """
    return f"swh:1:rev:{commit}" if commit else None
