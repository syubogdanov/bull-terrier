import sys

from pydantic import AfterValidator


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


_MIN_LENGTH: int = 1
_MAX_LENGTH: int = 39


def _validate(value: str) -> str:
    if not (_MIN_LENGTH <= len(value) <= _MAX_LENGTH):
        detail = (
            f"The GitHub username must be at least {_MIN_LENGTH}"
            f" and at most {_MAX_LENGTH} characters"
        )
        raise ValueError(detail)

    if not all(char.isalnum() or char == "-" for char in value):
        detail = "The GitHub username can only consist of alphanumeric characters or hyphens '-'"
        raise ValueError(detail)

    if value.startswith("-") or value.endswith("-") or "--" in value:
        detail = (
            "The GitHub username cannot begin or end with a "
            "hyphen or contain multiple consecutive hyphens"
        )
        raise ValueError(detail)

    return value


Username = Annotated[str, AfterValidator(_validate)]
