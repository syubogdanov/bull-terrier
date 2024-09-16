import doctest
import sys

from importlib import import_module
from typing import TYPE_CHECKING, Final

from tests.utils.core.root import get_root


if TYPE_CHECKING:
    from pathlib import Path


EXIT_FAILURE: Final[int] = 1


def get_module_name(python_module: "Path") -> str:
    """Convert the `Python` path to a module name."""
    return python_module.with_suffix("").as_posix().replace("/", ".")


def main() -> None:
    """Run the docstring tests."""
    root = get_root()

    failed_tests: int = 0

    for path in root.glob("bull_terrier/**/*.py"):
        relpath = path.relative_to(root)

        module_name = get_module_name(relpath)
        module = import_module(module_name)

        failed, _ = doctest.testmod(module)
        failed_tests += failed

    if failed_tests > 0:
        sys.exit(EXIT_FAILURE)


if __name__ == "__main__":
    main()
