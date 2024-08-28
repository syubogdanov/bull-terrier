from __future__ import annotations

import sys

from asyncio import Lock
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar
from weakref import WeakValueDictionary


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from collections.abc import Hashable


@dataclass
class LockSingleton:
    """A singleton version of `asyncio.Lock`.

    Notes
    -----
    * By specifying the key, you get a new singletone.
    * By default, the key is `None`.

    Examples
    --------
    >>> lhs = LockSingleton("python")
    >>> rhs = LockSingleton("python")
    >>> id(lhs) == id(rhs)
    True

    >>> lhs = LockSingleton("hello")
    >>> rhs = LockSingleton("world")
    >>> id(lhs) == id(rhs)
    False
    """

    _locks: ClassVar = WeakValueDictionary()

    def __new__(cls: type[Self], key: Hashable | None = None) -> Lock:
        """Create an `asyncio.Lock` object."""
        if key not in cls._locks:
            lock = Lock()
            cls._locks[key] = lock
        return cls._locks[key]
