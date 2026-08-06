"""Public :mod:`cypy.cyiterator` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def iter_check(o: object) -> bool:
    """Return True if ``o`` supports the iterator protocol (``PyIter_Check``)."""
    ...

def iter_eq(a: object, b: object) -> bool:
    """Return True if ``a is b`` (iterator identity; typical CPython ``object.__eq__``)."""
    ...

