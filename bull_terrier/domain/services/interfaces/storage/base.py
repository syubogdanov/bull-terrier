from __future__ import annotations

import sys

from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from bull_terrier.utils.typing import SupportsStr


T = TypeVar("T")


class BaseStorage(Generic[T]):
    """The storage protocol."""

    @abstractmethod
    async def get(self: Self, key: SupportsStr) -> T | None:
        """
        Return the value for key if key is in the cache storage.

        Parameters
        ----------
        key : SupportsStr
            Key.

        Returns
        -------
        T
            Value for key.
        None
            Key is not present.
        """

    @abstractmethod
    async def update(self: Self, key: SupportsStr, value: T) -> None:
        """
        Update the cache storage with the key/value pair.

        Parameters
        ----------
        key : SupportsStr
            Key.
        value : T
            Value.
        """

    @abstractmethod
    async def delete(self: Self, key: SupportsStr) -> None:
        """
        Delete the key from the cache storage.

        Parameters
        ----------
        key : SupportsStr
            Key.
        """
