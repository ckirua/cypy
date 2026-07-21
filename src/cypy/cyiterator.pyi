"""Public :mod:`cypy.cyiterator` stubs (signatures + docstrings for IDE / typecheckers)."""

def iter_check(o: object) -> bool:
    """Return True if ``o`` supports the iterator protocol (``PyIter_Check``)."""
    ...

def iter_next(o: object) -> object:
    """Return the next item from iterator ``o``, or ``None`` at end (no ``StopIteration``)."""
    ...
