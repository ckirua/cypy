"""Public :mod:`cypy.cylong` stubs (signatures + docstrings for IDE / typecheckers)."""

def long_check(p: object) -> bool:
    """Return True if ``p`` is an :class:`int` or subtype (``PyLong_Check``)."""
    ...

def long_check_exact(p: object) -> bool:
    """Return True if ``type(p) is int`` (``PyLong_CheckExact``); False for :class:`bool`."""
    ...

def long_from_long(v: int) -> object:
    """Return ``int(v)`` via ``PyLong_FromLong``."""
    ...

def long_from_ulong(v: int) -> object:
    """Return an :class:`int` from an unsigned long via ``PyLong_FromUnsignedLong``."""
    ...

def long_from_ssize(v: int) -> object:
    """Return an :class:`int` from ``Py_ssize_t`` via ``PyLong_FromSsize_t``."""
    ...

def long_from_size(v: int) -> object:
    """Return an :class:`int` from ``size_t`` via ``PyLong_FromSize_t``."""
    ...

def long_from_longlong(v: int) -> object:
    """Return an :class:`int` from ``long long`` via ``PyLong_FromLongLong``."""
    ...

def long_from_ulonglong(v: int) -> object:
    """Return an :class:`int` from ``unsigned long long`` via ``PyLong_FromUnsignedLongLong``."""
    ...

def long_from_double(v: float) -> object:
    """Return ``int(v)`` via ``PyLong_FromDouble`` (truncates toward zero)."""
    ...

def long_as_long(pylong: object) -> int:
    """Return a C ``long`` via ``PyLong_AsLong`` (raises on overflow)."""
    ...

def long_as_long_overflow(pylong: object) -> tuple[int, int]:
    """Return ``(value, overflow)`` via ``PyLong_AsLongAndOverflow``."""
    ...

def long_as_ssize(pylong: object) -> int:
    """Return a ``Py_ssize_t`` via ``PyLong_AsSsize_t``."""
    ...

def long_as_ulong(pylong: object) -> int:
    """Return an unsigned long via ``PyLong_AsUnsignedLong``."""
    ...

def long_as_longlong(pylong: object) -> int:
    """Return a ``long long`` via ``PyLong_AsLongLong``."""
    ...

def long_as_ulonglong(pylong: object) -> int:
    """Return an ``unsigned long long`` via ``PyLong_AsUnsignedLongLong``."""
    ...

def long_as_ulong_mask(io: object) -> int:
    """Return ``PyLong_AsUnsignedLongMask`` (wrap on overflow; no exception)."""
    ...

def long_as_ulonglong_mask(io: object) -> int:
    """Return ``PyLong_AsUnsignedLongLongMask`` (wrap on overflow; no exception)."""
    ...

def long_as_double(pylong: object) -> float:
    """Return a C ``double`` via ``PyLong_AsDouble``."""
    ...
