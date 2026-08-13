# Bloc-notes des commandes de développement. `make` seul liste les cibles.
#
# Rien ici n'est indispensable : chaque cible est une commande qu'on
# pourrait taper à la main, rangée pour ne pas avoir à s'en souvenir. Ce
# fichier ne décide donc rien. Ce qui décide vit ailleurs, et il ne faut
# pas le recopier ici : le CI dans `.github/workflows/`, la doctrine de
# version dans `CHANGELOG.md`, les règles de travail dans `CLAUDE.md`.
#
# Prérequis : le venv `.python_env/` (`make deps` le remplit).

VENV := .python_env/bin
PY   := $(VENV)/python

.DEFAULT_GOAL := help
.PHONY: help deps check test schema lint catalogue skos serve site \
        etat alignements classification

help:            ## liste des cibles
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | \
	  awk -F':.*## ' '{printf "  make %-14s %s\n", $$1, $$2}'

deps:            ## installe card et de quoi développer (tests, RDF, site)
	$(PY) -m pip install -e ".[dev,docs]"


# ── vérifier ─────────────────────────────────────────────────────────
# `check` est EXACTEMENT ce que lance le CI, dans le même ordre. Oublier
# ruff casse le CI en silence et envoie un mail d'échec à chaque push,
# ce qui est arrivé du 2026-07-21 au 2026-07-22.

check: test schema lint   ## les trois vérifs du CI, dans l'ordre

test:            ## la suite pytest
	$(PY) -m pytest

schema:          ## le linter des fiches YAML
	$(PY) -m card.schema

lint:            ## ruff sur les sources, les tests et les scripts
	$(VENV)/ruff check src tests scripts


# ── régénérer ce qui est GÉNÉRÉ ──────────────────────────────────────
# Aucune de ces sorties ne s'édite à la main, et un test refuse l'écart :
# il nomme la commande à relancer, donc rien n'est à retenir.

catalogue:       ## docs/CARDS*.md, la page catalogue et le décompte du README
	$(PY) scripts/generate_catalog.py

# Le .ttl porte la version du PAQUET : il se régénère APRÈS
# `set_version.py`, jamais avant, sans quoi il annonce l'ancienne.
skos:            ## docs/card.ttl : le corpus en SKOS + I-ADOPT
	$(PY) scripts/generate_skos.py


# ── le site ──────────────────────────────────────────────────────────
# `serve` recharge sur tout changement de `docs/`, mais ne régénère PAS
# le catalogue : cette page sort de `make catalogue`.

serve:           ## le site en local, http://127.0.0.1:8000/card/
	$(VENV)/mkdocs serve

site:            ## construit le site comme le CI (--strict)
	$(VENV)/mkdocs build --strict


# ── enquêter ─────────────────────────────────────────────────────────

etat:            ## dernier tag, commits depuis, entrées non publiées
	$(PY) scripts/set_version.py --etat

alignements:     ## résout les URIs externes du .ttl (réseau, hors pytest)
	$(PY) scripts/verifie_alignements.py

classification:  ## santé des facettes, à lancer avant d'en toucher une
	$(PY) scripts/analyse_classification.py
