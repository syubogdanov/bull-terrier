from __future__ import annotations

import sys

from dataclasses import dataclass, field
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

    from bull_terrier.domain.services.interfaces.storage.cache import CacheStorage


@dataclass
class DownloaderAdapter(Downloader):
    """The `HTTP` downloader adapter."""

    _cache: CacheStorage

    _lock_singleton_factory: LockSingletonFactory = field(default_factory=LockSingletonFactory)

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
        async with self._lock_singleton_factory.new(key=url):
            if (cached_file := await self._get_cached_file(url)):
                return cached_file

            async with ClientSession() as session, session.get(str(url)) as response:
                response.raise_for_status()

                # `tempfile.mkstemp` is a blocking IO operation
                file_descriptor, path = await to_thread(mkstemp)

                async with aiofiles.open(file_descriptor, mode="wb") as file:
                    async for chunk, _ in response.content.iter_chunks():
                        await file.write(chunk)

                await self._cache.update(key=url, value=path)

                return Path(path)

    async def _get_cached_file(self: Self, url: HttpUrl) -> FilePath | None:
        """Get the cached file, if it exists."""
        value = await self._cache.get(key=url)
        path = Path(value) if value else None

        if path is None:
            return None

        if not await aiofiles.ospath.exists(path):
            await self._cache.delete(key=url)
            return None

        if not await aiofiles.ospath.isfile(path):
            await self._cache.delete(key=url)
            return None

        return path
