"""Public :mod:`cypy.cyfloat` stubs (signatures + docstrings for IDE / typecheckers)."""

def float_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`float` or subtype (``PyFloat_Check``)."""
    ...

def float_check_exact(p: object) -> bool:
    """Return True if ``type(p) is float`` (``PyFloat_CheckExact``)."""
    ...

def float_from_double(v: float) -> object:
    """Return ``float(v)`` via ``PyFloat_FromDouble``."""
    ...

def float_as_double(pyfloat: object) -> float:
    """Return a C ``double`` via ``PyFloat_AsDouble`` (accepts float-like)."""
    ...

# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def float_from_cstr(s: object) -> object:
    """Return ``float(s)`` via ``PyFloat_FromString``. Alias of ``float_from_string`` (prefer ``*_cstr`` naming)."""
    ...

