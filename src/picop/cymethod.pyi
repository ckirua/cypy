"""Public :mod:`cypy.cymethod` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def method_check(o: object) -> bool:
    """Return True if ``o`` is a bound method (``PyMethod_Check``)."""
    ...

def method_eq(a: object, b: object) -> bool:
    """Return True if methods equal (same function + ``__self__``; not identity)."""
    ...

def method_get_function(meth: object) -> object:
    """Preferred spelling of ``method_function`` (checked ``PyMethod_Function``)."""
    ...

def method_get_self(meth: object) -> object | None:
    """Preferred spelling of ``method_self`` (checked ``PyMethod_Self``)."""
    ...
