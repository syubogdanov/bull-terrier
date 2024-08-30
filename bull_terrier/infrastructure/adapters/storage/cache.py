from __future__ import annotations

import sys

from dataclasses import dataclass, field
from hashlib import sha256
from typing import TYPE_CHECKING

from bull_terrier.domain.services.interfaces.storage.cache import CacheStorage
from bull_terrier.utils.asyncio import LockSingletonFactory


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import DirectoryPath, NonNegativeFloat

    from bull_terrier.utils.typing import SupportsStr


@dataclass
class CacheStorageAdapter(CacheStorage):
    """The cache storage protocol."""

    _cache_directory: DirectoryPath
    _time_to_live: NonNegativeFloat

    _lock_singleton_factory: LockSingletonFactory = field(default_factory=LockSingletonFactory)

    async def get(self: Self, key: SupportsStr) -> str | None:
        """
        Return the value for key if key is in the cache storage.

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

    async def update(self: Self, key: SupportsStr, value: SupportsStr) -> None:
        """
        Update the cache storage with the key/value pair.

        Parameters
        ----------
        key : SupportsStr
            Key.
        value : SupportsStr
            Value.
        """

    async def delete(self: Self, key: SupportsStr) -> None:
        """
        Delete the key from the cache storage.

        Parameters
        ----------
        key : SupportsStr
            Key.
        """

    def _to_cache_path(self: Self, key: SupportsStr) -> Path:
        """Get the path associated with the key."""
        return self._cache_directory / self._hash(key)

    @staticmethod
    def _hash(key: SupportsStr) -> str:
        """Get the hash associated with the key."""
        return sha256(str(key).encode(errors="ignore")).hexdigest()
