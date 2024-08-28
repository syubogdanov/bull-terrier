import sys

from abc import abstractmethod
from typing import Protocol


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class SupportsStr(Protocol):
    """An ABC with one abstract method `__str__`."""

    @abstractmethod
    def __str__(self: Self) -> str:
        """Return `str(self)`."""
