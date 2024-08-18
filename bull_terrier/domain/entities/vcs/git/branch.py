import sys

from bull_terrier.domain.entities.vcs.git.shortref import ShortRef


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


Branch: TypeAlias = ShortRef
