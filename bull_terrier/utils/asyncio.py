import sys

from asyncio import Lock
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from weakref import WeakValueDictionary


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from collections.abc import Callable, Hashable


@dataclass
class LockSingletonFactory:
    """An `asyncio.Lock` singleton factory."""

    _locks: WeakValueDictionary["Hashable", Lock] = field(default_factory=WeakValueDictionary)

    def new(self: Self, *, key: "Hashable" = None) -> Lock:
        """Create an `asyncio.Lock` singleton.

        Notes
        -----
        * By specifying the key, you get a new singleton.
        * By default, the key is `None`.

        Examples
        --------
        >>> factory = LockSingletonFactory()
        >>> lhs = factory.new(key="python")
        >>> rhs = factory.new(key="python")
        >>> id(lhs) == id(rhs)
        True

        >>> factory = LockSingletonFactory()
        >>> lhs = factory.new(key="hello")
        >>> rhs = factory.new(key="world")
        >>> id(lhs) == id(rhs)
        False
        """
        if key not in self._locks:
            lock = Lock()
            self._locks[key] = lock
        return self._locks[key]


if not (sys.version_info >= (3, 9)):
    """The backwards compatibility block."""

    from asyncio import get_running_loop
    from contextvars import copy_context
    from functools import partial
    from typing import Any


    async def to_thread(func: "Callable[..., Any]", /, *args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
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
