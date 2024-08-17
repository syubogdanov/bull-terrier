import re
import sys

from pydantic import AfterValidator


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
        raise ValueError(detail)

    if "/." in value or any(component.endswith(".lock") for component in value.split("/")):
        detail = (
            "The reference name can include slash '/' for hierarchical "
            "(directory) grouping, but no slash-separated component can"
            "begin with a dot '.' or end with the sequence '.lock'"
        )
        raise ValueError(detail)

    if ".." in value:
        detail = "The reference name cannot have two consecutive dots '..' anywhere"
        raise ValueError(detail)

    if re.search("[\000-\037\177 ~^:]", value):
        detail = (
            "The reference name cannot have ASCII control characters (i.e. "
            "bytes whose values are lower than '\\040', or '\\177'), space,"
            " tilde '~', caret '^', or colon ':' anywhere"
        )
        raise ValueError(detail)

    if any(sign in value for sign in ["?", "*", "["]):
        detail = (
            "The reference name cannot have question-mark '?',"
            " asterisk '*', or open bracket '[' anywhere"
        )
        raise ValueError(detail)

    if value.startswith("/") or value.endswith("/") or "//" in value:
        detail = (
            "The reference name cannot begin or end with a slash"
            " '/' or contain multiple consecutive slashes"
        )
        raise ValueError(detail)

    if value.endswith("."):
        detail = "The reference name cannot end with a dot '.'"
        raise ValueError(detail)

    if "@{" in value:
        detail = "The reference name cannot contain a sequence '@{'"
        raise ValueError(detail)

    if value == "@":
        detail = "The reference name cannot be a single character '@'"
        raise ValueError(detail)

    if "\\" in value:
        detail = "The reference name cannot contain a '\\'"
        raise ValueError(detail)

    return value


ShortRef = Annotated[str, AfterValidator(_validate)]
