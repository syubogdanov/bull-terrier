import sys

from typing import TYPE_CHECKING


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


if TYPE_CHECKING:
    HashStr20 = str
else:
    from eth_pydantic_types import HashStr20


SHA1: TypeAlias = HashStr20
