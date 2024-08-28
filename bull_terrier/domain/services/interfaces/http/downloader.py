import sys

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from pydantic import FilePath, HttpUrl


class Downloader(Protocol):
    """The `HTTP` downloader protocol."""

    @abstractmethod
    async def download(self: Self, url: "HttpUrl") -> "FilePath":
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
