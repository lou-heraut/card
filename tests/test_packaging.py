"""Les fichiers de données lus à l'exécution doivent être empaquetés.

En installation éditable tout est là, donc un oubli de package-data ne se
voit pas en dev : il ne casse qu'en installation depuis une archive
(l'image Docker de card-api). C'est ce qui est arrivé à inputs.yaml, dont
l'absence faisait remonter card.info() en FileNotFoundError.
"""

from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parent.parent
_PKG = _ROOT / "src" / "card"


def _declared_patterns():
    tomllib = pytest.importorskip("tomllib")          # 3.11+
    conf = tomllib.loads((_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return conf["tool"]["setuptools"]["package-data"]["card"]


def test_package_data_covers_root_yaml():
    patterns = _declared_patterns()
    orphans = [
        p.name for p in sorted(_PKG.glob("*.yaml"))
        if not any(Path(p.name).match(pat) for pat in patterns)
    ]
    assert not orphans, (
        f"fichiers non empaquetés : {orphans} ; compléter package-data "
        "dans pyproject.toml, sinon ils manqueront hors install éditable"
    )


def test_runtime_registries_are_present():
    assert (_PKG / "inputs.yaml").is_file()
    assert (_PKG / "topics.yaml").is_file()
