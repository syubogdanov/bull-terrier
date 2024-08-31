from __future__ import annotations

import sys

from dataclasses import dataclass, field
from http.client import HTTPMessage
from pathlib import Path
from tempfile import mkstemp
from typing import TYPE_CHECKING
from urllib.error import HTTPError

import aiofiles
import aiofiles.ospath

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectionError, ClientResponseError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

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

    _cache_storage: CacheStorage

    _lock_singleton_factory: LockSingletonFactory = field(default_factory=LockSingletonFactory)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(),
        retry=retry_if_exception_type(ConnectionError),
        reraise=True,
    )
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
            if cached_file := await self._get_from_cache(url):
                return cached_file

            async with ClientSession() as session:
                try:
                    async with session.get(str(url), raise_for_status=True) as response:
                        # `tempfile.mkstemp` is a blocking IO operation
                        file_descriptor, path = await to_thread(mkstemp)

                        async with aiofiles.open(file_descriptor, mode="wb") as file:
                            async for chunk, _ in response.content.iter_chunks():
                                await file.write(chunk)

                except ClientConnectionError as exception:
                    detail = str(exception)
                    raise ConnectionError(detail) from exception

                except ClientResponseError as exception:
                    raise HTTPError(
                        url=url.unicode_string(),
                        code=exception.status,
                        msg=exception.message,
                        hdrs=HTTPMessage(),
                        fp=None,
                    ) from exception

            await self._cache_storage.update(key=url, value=path)

            return Path(path)

    async def _get_from_cache(self: Self, url: HttpUrl) -> FilePath | None:
        """Get the cached file, if it exists."""
        value = await self._cache_storage.get(key=url)
        path = Path(value) if value else None

        if path is None:
            return None

        if not await aiofiles.ospath.exists(path):
            await self._cache_storage.delete(key=url)
            return None

        if not await aiofiles.ospath.isfile(path):
            await self._cache_storage.delete(key=url)
            return None

        return path
