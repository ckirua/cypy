"""Public :mod:`cypy.cylong` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def long_check(p: object) -> bool:
    """Return True if ``p`` is an :class:`int` or subtype (``PyLong_Check``)."""
    ...

def long_check_exact(p: object) -> bool:
    """Return True if ``type(p) is int`` (``PyLong_CheckExact``); False for :class:`bool`."""
    ...

def long_eq(a: object, b: object) -> bool:
    """Return True if integers are equal (identity short-circuit + richcompare)."""
    ...

def int_eq(a: object, b: object) -> bool:
    """Return True if ``a == b`` — thin alias of ``long_eq`` (same semantics)."""
    ...

def long_from_ulong(v: int) -> object:
    """Return an :class:`int` from an unsigned long via ``PyLong_FromUnsignedLong``."""
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

def long_as_long_overflow(pylong: object) -> tuple[int, int]:
    """Return ``(value, overflow)`` via ``PyLong_AsLongAndOverflow``."""
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

