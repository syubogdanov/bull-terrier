from __future__ import annotations

import sys

from contextlib import suppress
from dataclasses import dataclass
from datetime import timedelta
from hashlib import sha256
from typing import TYPE_CHECKING

import aiofiles
import aiofiles.os
import aiofiles.ospath

from pydantic import ValidationError

from bull_terrier.domain.services.interfaces.storage.keyvalue import KeyValueStorage
from bull_terrier.infrastructure.schemas.storage.keyvalue import CellSchema
from bull_terrier.utils.asyncio import LockSingletonFactory
from bull_terrier.utils.datetime import utcnow


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import DirectoryPath, NonNegativeFloat

    from bull_terrier.utils.typing import SupportsStr


@dataclass
class KeyValueStorageAdapter(KeyValueStorage):
    """The key-value storage adapter."""

    _storage_dir: DirectoryPath
    _time_to_live: NonNegativeFloat

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
        as_str = str(key)
        path = self._to_path(as_str)

        async with LockSingletonFactory.new(key=as_str):
            if not await aiofiles.ospath.exists(path):
                return None

            async with aiofiles.open(path) as file:
                json_data = await file.read()

            try:
                cell = CellSchema.model_validate_json(json_data)

            except ValidationError:
                await aiofiles.os.remove(path)
                return None

            if utcnow() >= cell.expire_dttm:
                await aiofiles.os.remove(path)
                return None

            return cell.value

    async def update(self: Self, key: SupportsStr, value: SupportsStr) -> None:
        """
        Update the storage with the key/value pair.

        Parameters
        ----------
        key : SupportsStr
            Key.
        value : SupportsStr
            Value.
        """
        as_str = str(key)
        path = self._to_path(as_str)

        expire_dttm = utcnow() + timedelta(seconds=self._time_to_live)
        cell = CellSchema(key=as_str, value=str(value), expire_dttm=expire_dttm)

        async with LockSingletonFactory.new(key=as_str), aiofiles.open(path, mode="w") as file:
            await file.write(cell.model_dump_json())

    async def delete(self: Self, key: SupportsStr) -> None:
        """
        Delete the key.

        Parameters
        ----------
        key : SupportsStr
            Key.
        """
        as_str = str(key)
        path = self._to_path(as_str)

        async with LockSingletonFactory.new(key=as_str):
            with suppress(FileNotFoundError, OSError, PermissionError):
                await aiofiles.os.remove(path)

    @staticmethod
    def _encode(key: SupportsStr) -> str:
        return sha256(str(key).encode(errors="ignore")).hexdigest()

    def _to_path(self: Self, key: SupportsStr) -> Path:
        return self._storage_dir / self._encode(key)
