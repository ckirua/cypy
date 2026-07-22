"""Public :mod:`cypy.cyiterator` stubs (signatures + docstrings for IDE / typecheckers)."""

def iter_check(o: object) -> bool:
    """Return True if ``o`` supports the iterator protocol (``PyIter_Check``)."""
    ...

def iter_eq(a: object, b: object) -> bool:
    """Return True if ``a is b`` (iterator identity; typical CPython ``object.__eq__``)."""
    ...

def iter_next(o: object) -> object:
    """Return the next item from iterator ``o``, or ``None`` at end (no ``StopIteration``)."""
    ...
