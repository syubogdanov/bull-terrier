from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=None)
def get_root() -> "Path":
    """Get the root directory of `Bull-Terrier`."""
    return Path(__file__).parent.parent.parent.parent
