from functools import cache
from pathlib import Path


@cache
def get_root() -> "Path":
    """Get the root directory of `Bull-Terrier`."""
    return Path(__file__).parent.parent.parent.parent
