from __future__ import annotations

import sys

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol, overload


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from pydantic import DirectoryPath

    from bull_terrier.domain.entities.vcs.git.branch import Branch
    from bull_terrier.domain.entities.vcs.git.commit import Commit
    from bull_terrier.domain.entities.vcs.git.tag import Tag
    from bull_terrier.domain.entities.web.com.gitlab.project import Project
    from bull_terrier.domain.entities.web.com.gitlab.username import Username


class GitHub(Protocol):
    """The `GitLab` protocol."""

    @overload
    async def download(self: Self, username: Username, project: Project) -> DirectoryPath: ...

    @overload
    async def download(
        self: Self,
        username: Username,
        project: Project,
        *,
        branch: Branch,
    ) -> DirectoryPath: ...

    @overload
    async def download(
        self: Self,
        username: Username,
        project: Project,
        *,
        commit: Commit,
    ) -> DirectoryPath: ...

    @overload
    async def download(
        self: Self,
        username: Username,
        project: Project,
        *,
        tag: Tag,
    ) -> DirectoryPath: ...

    @abstractmethod
    async def download(
        self: Self,
        username: Username,
        project: Project,
        *,
        branch: Branch | None = None,
        commit: Commit | None = None,
        tag: Tag | None = None,
    ) -> DirectoryPath:
        """
        Download the `GitLab` project.

        Parameters
        ----------
        username : Username
            Username.
        project : Project
            Project.
        branch : Branch
            Branch.
        commit : Commit
            Commit.
        tag : Tag
            Tag.

        Returns
        -------
        DirectoryPath
            Directory with the contents of the project.

        Notes
        -----
        * Only one of *branch*, *commit* or *tag* can be specified;
        * By default, the project's default branch is downloaded.
        """
