> **Statut : plan en cours, le contact est pris.** Réclamer le nom `card`
> sur PyPI, occupé depuis 2019 par une réservation vide. Le courriel et
> l'issue sont partis le 2026-08-06 ; la demande PEP 541 peut suivre à
> partir du 2026-09-06. Contient les preuves mesurées et les textes. Les
> dates vivent ici, et nulle part ailleurs.
> À supprimer une fois le nom obtenu ou la demande refusée.

# Réclamer `card` sur PyPI (PEP 541)

## Pourquoi le dossier est solide

Mesuré le 2026-08-05, en téléchargeant le paquet publié.

| fait | valeur |
|---|---|
| release unique | 0.0.1, 2019-08-23, 1 425 octets |
| modules Python dans l'archive | **0** |
| `top_level.txt` | **vide** |
| contenu réel | `setup.py`, `README.rst`, `setup.cfg`, `card.egg-info/` |
| README | gabarit cookiecutter non rempli, titre « SDK », badges vers PyPI |
| résumé du projet | « card » |
| propriétaire | Longniao, `longniao@gmail.com` |
| dépôt annoncé | `github.com/pipname/card`, dernier push le 2019-08-23 |

**`pip install card` n'installe rien.** Ce n'est pas un projet abandonné,
c'est une réservation de nom sans contenu, ce que la politique PyPI
appelle un projet *invalide*. C'est le motif le plus solide de PEP 541,
et il est vérifiable en trente secondes par n'importe quel administrateur.

Reproduire la mesure :

```bash
curl -sL https://pypi.org/pypi/card/json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['releases']['0.0.1'][0]['url'])"
# télécharger l'archive, puis :
tar tzf card-0.0.1.tar.gz          # aucun .py hors setup.py
cat card-0.0.1/card.egg-info/top_level.txt   # vide
```

## Les trois étapes

PyPI exige la preuve d'une tentative de contact avant d'arbitrer. On la
fait donc sérieusement, et publiquement pour qu'elle soit montrable.

| # | quoi | où | date d'envoi |
|---|---|---|---|
| 1 | courriel au propriétaire | `longniao@gmail.com` | **envoyé le 2026-08-06** |
| 2 | issue publique, trace horodatée | `github.com/pipname/card/issues` | **ouverte le 2026-08-06** |
| 3 | demande PEP 541 | `github.com/pypi/support/issues/new/choose`, modèle de demande de nom de projet | **à partir du 2026-09-06** |

Entre 2 et 3, **attendre un mois**. Ce délai n'est pas une politesse : il
rend la demande inattaquable, personne ne pouvant dire que le
propriétaire n'a pas eu sa chance.

**Le délai court depuis le 2026-08-06**, donc la demande PEP 541 peut
partir à partir du **2026-09-06**. Si une réponse arrive d'ici là, elle
change tout : ce plan s'arrête et le nom de repli reste.

Compter ensuite plusieurs mois de traitement. Rien ne presse : `card-stase`
fonctionne, et le nom d'import est déjà `card`.

## Texte 1 : courriel

> **Objet** : PyPI project name "card"
>
> Hi,
>
> I maintain a scientific Python package and I would like to use the name
> `card` on PyPI. You own that name, so I am asking you first.
>
> As published, the project has no content: the only release (0.0.1,
> August 2019) ships `setup.py`, a README template and metadata, no
> Python module, and `top_level.txt` is empty. `pip install card`
> therefore installs nothing. The repository it points to,
> github.com/pipname/card, has not been touched since the same day.
>
> If you still plan to use the name, say so and I will look elsewhere. If
> not, would you agree to transfer the project to me, or to delete it?
>
> What I would publish under it: a collection of over 200 hydroclimatic
> variable definitions (low flows, floods, seasonality, climate change)
> used in hydrology research at INRAE, France. It is GPL-3, archived on
> Software Heritage, and currently installed under the fallback name
> `card-stase` while its import name is already `card`.
> https://github.com/lou-heraut/card
>
> If I get no answer, I will open a PEP 541 request with the PyPI
> administrators in a month.
>
> Thanks,
> Louis Héraut, INRAE, UR RiverLy

## Texte 2 : issue publique sur `pipname/card`

> **Titre** : Are you still using the PyPI name `card`?
>
> Hi, I am asking here as well as by email, so that the question is on
> the record.
>
> I would like to use the name `card` on PyPI for a scientific Python
> package. The release published under that name (0.0.1, August 2019)
> contains no Python module: only `setup.py`, a README template and
> metadata, with an empty `top_level.txt`. So `pip install card`
> installs nothing, and this repository has not changed since the same
> day.
>
> If you still plan to use the name, tell me and I will look elsewhere.
> If not, would you transfer the PyPI project or delete it?
>
> What I would publish: over 200 hydroclimatic variable definitions used
> in hydrology research at INRAE, France, GPL-3, archived on Software
> Heritage. https://github.com/lou-heraut/card
>
> Without an answer, I will open a PEP 541 request with PyPI in a month.

## Texte 3 : demande PEP 541

Sur `github.com/pypi/support`, choisir le modèle de demande de nom de
projet. Il demande le nom, ton identifiant PyPI et le motif ; le corps
ci-dessous répond au reste.

> **Project to be claimed**: `card` (https://pypi.org/project/card/)
> **Reason**: the project is invalid, it has no content.
>
> The only release, 0.0.1 of 2019-08-23, contains no Python module. The
> sdist is 1425 bytes and ships `setup.py`, `README.rst`, `setup.cfg`
> and `card.egg-info/` only. `top_level.txt` is empty, so `pip install
> card` installs nothing importable. The description is an unmodified
> cookiecutter template titled "SDK", and the summary is the word
> "card". The linked repository, github.com/pipname/card, was last
> pushed on 2019-08-23, the same day, and has never been updated.
>
> **Contact attempts**: I emailed the owner at the address published in
> the project metadata on 2026-08-06, and opened an issue on the linked
> repository the same day: <LIEN DE L'ISSUE>. No answer as of
> <DATE DU JOUR>.
>
> **What I would publish**: `card`, a collection of over 200
> hydroclimatic variable definitions (low flows, floods, seasonality,
> climate change indicators) computed from daily time series, developed
> at INRAE (French National Research Institute for Agriculture, Food and
> the Environment) for hydrology research. GPL-3, archived on Software
> Heritage, with a public web service and an R front end. It is already
> released and installable under the fallback name `card-stase`, and its
> import name is `card`.
> https://github.com/lou-heraut/card

## Ce qui reste vrai quoi qu'il arrive

Ne rien publier sur PyPI tant que la demande n'est pas tranchée : publier
`card-stase` maintenant obligerait à maintenir deux noms ensuite.
`card-stase` reste le nom de repli du `pyproject.toml`, et l'import reste
`card` dans tous les cas.
