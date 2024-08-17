import sys

from pydantic import AfterValidator


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


_RESERVED_NAMES = {
    "badges",
    "blame",
    "blob",
    "builds",
    "commits",
    "create",
    "create_dir",
    "edit",
    "files",
    "find_file",
    "new",
    "preview",
    "raw",
    "refs",
    "tree",
    "update",
    "wikis",
}


_MIN_LENGTH: int = 2
_MAX_LENGTH: int = 255


def _validate(value: str) -> str:
    """
    Ensure that a project name is well formed.

    Notes
    -----
    * Rules: https://docs.gitlab.com/ee/user/reserved_names.html.
    """
    if not (_MIN_LENGTH <= len(value) <= _MAX_LENGTH):
        detail = (
            f"The GitLab project name must be at least {_MIN_LENGTH}"
            f" and at most {_MAX_LENGTH} characters"
        )
        raise ValueError(detail)

    if not all(char.isalnum() or char in {".", "-", "_"} for char in value):
        detail = (
            "The GitLab project name can only contain ASCII letters,"
            " digits, hyphens '-', dots '.' and underscores '_'"
        )
        raise ValueError(detail)

    if value.startswith(("_", "-", ".")) or value.endswith(("_", "-", ".")):
        detail = (
            "The GitLab project name cannot start or end"
            " with underscore '_', hyphen '-' or dot '.'"
        )
        raise ValueError(detail)

    if not value[0].isalnum():
        detail = "The GitLab project name must start with a letter ('a-zA-Z') or digit ('0-9')"
        raise ValueError(detail)

    if any(f"{char}{char}" in value for char in ("_", "-", ".")):
        detail = "The GitLab project name must not contain consecutive special characters"
        raise ValueError(detail)

    if value.endswith((".git", ".atom")):
        detail = "The GitLab project name cannot end in '.git' or '.atom'"
        raise ValueError(detail)

    if value in _RESERVED_NAMES:
        detail = (
            "The specified GitLab project name is reserved by the"
            " platform, which means that this name cannot be used"
        )
        raise ValueError(detail)

    return value


Project = Annotated[str, AfterValidator(_validate)]
