"""Public :mod:`cypy.cyfloat` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def float_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`float` or subtype (``PyFloat_Check``)."""
    ...

def float_check_exact(p: object) -> bool:
    """Return True if ``type(p) is float`` (``PyFloat_CheckExact``)."""
    ...

def float_eq(a: object, b: object) -> bool:
    """Return True if values are equal with Python float parity (NaN != NaN, ``+0.0 == -0.0``)."""
    ...

