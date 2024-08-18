import sys

from eth_pydantic_types import HashStr20


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


SHA1: TypeAlias = HashStr20
