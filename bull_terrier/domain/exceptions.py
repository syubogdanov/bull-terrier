class BullTerrierError(Exception):
    """The base class for all `Bull-Terrier` exceptions."""


class BitbucketError(BullTerrierError):
    """The base class for all `Bitbucket` exceptions."""


class GitError(BullTerrierError):
    """The base class for all `git` exceptions."""


class GitHubError(BullTerrierError):
    """The base class for all `GitHub` exceptions."""


class GitLabError(BullTerrierError):
    """The base class for all `GitLab` exceptions."""
