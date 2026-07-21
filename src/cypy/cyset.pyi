"""Public :mod:`cypy.cyset` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def set_add(s: set, value: object) -> int:
    """Add ``value`` via ``PySet_Add`` (``0`` / raises). Returns 0 on success; errors raise — do not use as bool."""
    ...

def set_any_check(p: object) -> bool:
    """Return True if ``p`` is a set or frozenset (or subtype)."""
    ...

def set_any_check_exact(p: object) -> bool:
    """Return True if ``type(p) is set`` or ``frozenset`` (no subtype)."""
    ...

def set_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`set` or subtype (``PySet_Check``)."""
    ...

def set_check_exact(p: object) -> bool:
    """Return True if ``type(p) is set`` (``PySet_CheckExact``)."""
    ...

def set_clear(s: set) -> int:
    """Clear ``s`` via ``PySet_Clear`` (``0`` / raises). Returns 0 on success; errors raise — do not use as bool."""
    ...

def set_contains(anyset: object, value: object) -> bool:
    """Return whether ``value`` is in ``anyset`` via ``PySet_Contains``."""
    ...

def set_copy(s: set) -> set:
    """Shallow-copy ``s`` via ``PySet_New(s)``."""
    ...

def set_discard(s: set, value: object) -> int:
    """Discard ``value`` via ``PySet_Discard`` (``1`` removed / ``0`` absent; no ``KeyError``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def set_empty() -> set:
    """Return a new empty set via ``PySet_New(NULL)``."""
    ...

def frozenset_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`frozenset` or subtype."""
    ...

def frozenset_check_exact(p: object) -> bool:
    """Return True if ``type(p) is frozenset``."""
    ...

def frozenset_empty() -> frozenset:
    """Return a new empty frozenset via ``PyFrozenSet_New(NULL)``."""
    ...

def frozenset_new(iterable: object) -> frozenset:
    """Return a new frozenset from ``iterable`` via ``PyFrozenSet_New``."""
    ...

def set_len(s: set) -> int:
    """Return ``len(s)`` via ``PySet_GET_SIZE`` (exact ``set``)."""
    ...

def set_new(iterable: object) -> set:
    """Return a new set from ``iterable`` via ``PySet_New``."""
    ...

def set_pop(s: set) -> object:
    """Remove and return an arbitrary element via ``PySet_Pop`` (raises ``KeyError`` if empty)."""
    ...

def set_size(anyset: object) -> int:
    """Return ``len(anyset)`` via checked ``PySet_Size`` (set/frozenset/subtypes)."""
    ...

def set_update(s: set, iterable: object) -> int:
    """Update ``s`` from ``iterable`` via ``_PySet_Update`` (``0`` / raises). Returns 0 on success; errors raise — do not use as bool."""
    ...

