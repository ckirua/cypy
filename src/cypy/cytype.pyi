"""Public :mod:`cypy.cytype` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def type_check(o: object) -> bool:
    """Return True if ``o`` is a type object or subtype (``PyType_Check``)."""
    ...

def type_check_exact(o: object) -> bool:
    """Return True if ``type(o) is type`` (``PyType_CheckExact``)."""
    ...

def type_eq(a: object, b: object) -> bool:
    """Return True if ``a is b`` (type-object identity; not metaclass ``__eq__``)."""
    ...
