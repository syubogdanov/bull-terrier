from __future__ import annotations

import sys

from dataclasses import dataclass
from pathlib import Path
from tempfile import mkstemp
from typing import TYPE_CHECKING

import aiofiles
import aiofiles.ospath

from aiohttp import ClientSession

from bull_terrier.domain.services.interfaces.http.downloader import Downloader
from bull_terrier.utils.asyncio import LockSingletonFactory


if sys.version_info >= (3, 9):
    from asyncio import to_thread
else:
    from bull_terrier.utils.asyncio import to_thread


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from pydantic import FilePath, HttpUrl

    from bull_terrier.infrastructure.interfaces.storage.keyvalue import KeyValueStorage


@dataclass
class DownloaderAdapter(Downloader):
    """The `HTTP` downloader adapter."""

    _storage: KeyValueStorage

    async def download(self: Self, url: HttpUrl) -> FilePath:
        """
        Download contents of the web page.

        Parameters
        ----------
        url : HttpUrl
            URL.

        Returns
        -------
        FilePath
            File with the contents of the web-page.
        """
        async with LockSingletonFactory.new(key=url):
            if (cached_file := await self._get_cached_file(url)) is not None:
                return cached_file

            async with ClientSession() as session, session.get(str(url)) as response:
                response.raise_for_status()

                # `tempfile.mkstemp` is a blocking IO operation
                file_descriptor, path = await to_thread(mkstemp)

                async with aiofiles.open(file_descriptor, mode="wb") as file:
                    async for chunk, _ in response.content.iter_chunks():
                        await file.write(chunk)

                await self._storage.update(key=url, value=path)

                return Path(path)

    async def _get_cached_file(self: Self, url: HttpUrl) -> FilePath | None:
        value = await self._storage.get(key=url)
        path = Path(value) if value else None

        if path is None:
            return None

        if not await aiofiles.ospath.exists(path):
            await self._storage.delete(key=url)
            return None

        if not await aiofiles.ospath.isfile(path):
            await self._storage.delete(key=url)
            return None

        return path
