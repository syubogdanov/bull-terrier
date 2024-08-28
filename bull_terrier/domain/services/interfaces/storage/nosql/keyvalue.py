from __future__ import annotations

import sys

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol, overload


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from bull_terrier.utils.typing import SupportsStr


class KeyValueNoSQL(Protocol):
    """The key-value database protocol."""

    @overload
    async def get(self: Self, key: SupportsStr) -> str | None: ...

    @overload
    async def get(self: Self, key: SupportsStr, default: str) -> str: ...

    @abstractmethod
    async def get(self: Self, key: SupportsStr, default: str | None = None) -> str | None:
        """
        Return the value for key if key is in the storage, else default.

        Parameters
        ----------
        key : SupportsStr
            Key.
        default : str | None
            Default value.

        Returns
        -------
        str
            Value (or default).
        None
            Key is not present.

        Notes
        -----
        * Default values are not inserted.
        """

    @abstractmethod
    async def insert(self: Self, key: SupportsStr, value: str) -> bool:
        """
        Insert the value.

        Parameters
        ----------
        key : SupportsStr
            Key.
        value : str
            Value.

        Returns
        -------
        True
            Value was inserted.
        False
            Value was **NOT** inserted.
        """

    @abstractmethod
    async def delete(self: Self, key: SupportsStr) -> None:
        """
        Delete the key.

        Parameters
        ----------
        key : SupportsStr
            Key.
        """
