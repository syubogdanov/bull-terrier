import re
import sys

from pydantic import AfterValidator

from bull_terrier.domain.exceptions import GitError


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


def _validate(value: str) -> str:  # noqa: C901
    """
    Ensure that a reference name is well formed.

    Notes
    -----
    * Algorithm: https://git-scm.com/docs/git-check-ref-format;
    * The `--allow-onelevel` option is enabled.
    """
    if not value:
        detail = "The reference name cannot be empty"
        raise GitError(detail)

    if "/." in value or any(component.endswith(".lock") for component in value.split("/")):
        detail = (
            "The reference name can include slash '/' for hierarchical "
            "(directory) grouping, but no slash-separated component can"
            "begin with a dot '.' or end with the sequence '.lock'"
        )
        raise GitError(detail)

    if ".." in value:
        detail = "The reference name cannot have two consecutive dots '..' anywhere"
        raise GitError(detail)

    if re.search("[\000-\037\177 ~^:]", value):
        detail = (
            "The reference name cannot have ASCII control characters (i.e. "
            "bytes whose values are lower than '\\040', or '\\177'), space,"
            " tilde '~', caret '^', or colon ':' anywhere"
        )
        raise GitError(detail)

    if any(char in value for char in ["?", "*", "["]):
        detail = (
            "The reference name cannot have question-mark '?',"
            " asterisk '*', or open bracket '[' anywhere"
        )
        raise GitError(detail)

    if value.startswith("/") or value.endswith("/") or "//" in value:
        detail = (
            "The reference name cannot begin or end with a slash"
            " '/' or contain multiple consecutive slashes"
        )
        raise GitError(detail)

    if value.endswith("."):
        detail = "The reference name cannot end with a dot '.'"
        raise GitError(detail)

    if "@{" in value:
        detail = "The reference name cannot contain a sequence '@{'"
        raise GitError(detail)

    if value == "@":
        detail = "The reference name cannot be a single character '@'"
        raise GitError(detail)

    if "\\" in value:
        detail = "The reference name cannot contain a '\\'"
        raise GitError(detail)

    return value


ShortRef = Annotated[str, AfterValidator(_validate)]
