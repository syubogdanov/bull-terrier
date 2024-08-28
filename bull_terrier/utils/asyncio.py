from __future__ import annotations

import sys

from asyncio import Lock, get_running_loop
from contextvars import copy_context
from dataclasses import dataclass
from functools import partial
from typing import TYPE_CHECKING, Any, ClassVar
from weakref import WeakValueDictionary


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from collections.abc import Callable, Hashable


@dataclass
class LockSingletonFactory:
    """A singleton version of `asyncio.Lock`.

    Notes
    -----
    * By specifying the key, you get a new singletone.
    * By default, the key is `None`.

    Examples
    --------
    >>> lhs = LockSingletonFactory.new(key="python")
    >>> rhs = LockSingletonFactory.new(key="python")
    >>> id(lhs) == id(rhs)
    True

    >>> lhs = LockSingletonFactory.new(key="hello")
    >>> rhs = LockSingletonFactory.new(key="world")
    >>> id(lhs) == id(rhs)
    False
    """

    _locks: ClassVar = WeakValueDictionary()

    @classmethod
    def new(cls: type[Self], *, key: Hashable | None = None) -> Lock:
        """Create an `asyncio.Lock` object."""
        if key not in cls._locks:
            lock = Lock()
            cls._locks[key] = lock
        return cls._locks[key]


async def to_thread(func: Callable[..., Any], /, *args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
    """Asynchronously run function `func` in a separate thread.

    Parameters
    ----------
    func : Callable[..., Any]
        Function.
    *args : Any
        Positional arguments to `func`.
    *kwargs : Any
        Keyword arguments to `func`.

    Returns
    -------
    Any
        Eventual result of `func`.

    Notes
    -----
    * Used to ensure compatibility with `Python` below `3.9`;
    * This is literally a complete copy of `asyncio.to_thread`.

    See Also
    --------
    * `asyncio.to_thread`.
    """
    loop = get_running_loop()
    ctx = copy_context()
    func_call = partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)
