import sys

from pydantic import AfterValidator

from bull_terrier.domain.exceptions import BitbucketError


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


_MIN_LENGTH: int = 1
_MAX_LENGTH: int = 255


def _validate(value: str) -> str:
    if not (_MIN_LENGTH <= len(value) <= _MAX_LENGTH):
        detail = (
            f"The Bitbucket repository name must be at least {_MIN_LENGTH}"
            f" and at most {_MAX_LENGTH} characters"
        )
        raise BitbucketError(detail)

    if not all(char.isalnum() or char in {"-", "_"} for char in value):
        detail = (
            "The Bitbucket repository name can only contain ASCII"
            " letters, digits, hyphens '-', and underscores '_'"
        )
        raise BitbucketError(detail)

    return value


Repository = Annotated[str, AfterValidator(_validate)]
