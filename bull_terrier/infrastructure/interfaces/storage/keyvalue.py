from __future__ import annotations

import sys

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from bull_terrier.utils.typing import SupportsStr


class KeyValueStorage(Protocol):
    """The key-value storage protocol."""

    @abstractmethod
    async def get(self: Self, key: SupportsStr) -> str | None:
        """
        Return the value for key if key is in the storage.

        Parameters
        ----------
        key : SupportsStr
            Key.

        Returns
        -------
        str
            Value for key.
        None
            Key is not present.
        """

    @abstractmethod
    async def insert(self: Self, key: SupportsStr, value: SupportsStr) -> bool:
        """
        Insert the value.

        Parameters
        ----------
        key : SupportsStr
            Key.
        value : SupportsStr
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
