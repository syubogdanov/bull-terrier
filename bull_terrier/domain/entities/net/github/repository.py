import sys

from pydantic import AfterValidator


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


_MIN_LENGTH: int = 1
_MAX_LENGTH: int = 100


def _validate(value: str) -> str:
    if not (_MIN_LENGTH <= len(value) <= _MAX_LENGTH):
        detail = (
            f"The GitHub repository name must be at least {_MIN_LENGTH}"
            f" and at most {_MAX_LENGTH} characters"
        )
        raise ValueError(detail)

    if not all(char.isalnum() or char in {".", "-", "_"} for char in value):
        detail = (
            "The GitHub repository name can only contain ASCII letters,"
            " digits, hyphens '-', dots '.' and underscores '_'"
        )
        raise ValueError(detail)

    if value in {".", ".."}:
        detail = "The GitHub repository name cannot be '.' or '..'"
        raise ValueError(detail)

    return value


Repository = Annotated[str, AfterValidator(_validate)]
