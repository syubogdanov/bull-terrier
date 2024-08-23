import sys

from pydantic import AfterValidator

from bull_terrier.domain.exceptions import GitLabError


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


_MIN_LENGTH: int = 2
_MAX_LENGTH: int = 255


def _validate(value: str) -> str:
    """
    Ensure that a username is well formed.

    Rules
    -----
    * https://docs.gitlab.com/ee/user/profile/#change-your-username;
    * https://docs.gitlab.com/ee/user/reserved_names.html.
    """
    if not (_MIN_LENGTH <= len(value) <= _MAX_LENGTH):
        detail = (
            f"The GitLab username must be at least {_MIN_LENGTH}"
            f" and at most {_MAX_LENGTH} characters"
        )
        raise GitLabError(detail)

    if not all(char.isalnum() or char in {".", "-", "_"} for char in value):
        detail = (
            "The GitLab username can only contain ASCII letters,"
            " digits, hyphens '-', dots '.' and underscores '_'"
        )
        raise GitLabError(detail)

    if value.startswith(("_", "-", ".")) or value.endswith(("_", "-", ".")):
        detail = (
            "The GitLab username cannot start or end with"
            " underscore '_', hyphen '-' or dot '.'"
        )
        raise GitLabError(detail)

    if not value[0].isalnum():
        detail = "The GitLab username must start with a letter ('a-zA-Z') or digit ('0-9')"
        raise GitLabError(detail)

    if any(f"{char}{char}" in value for char in ("_", "-", ".")):
        detail = "The GitLab username must not contain consecutive special characters"
        raise GitLabError(detail)

    if value.endswith((".git", ".atom")):
        detail = "The GitLab username cannot end in '.git' or '.atom'"
        raise GitLabError(detail)

    return value


Username = Annotated[str, AfterValidator(_validate)]
