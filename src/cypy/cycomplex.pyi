"""Public :mod:`cypy.cycomplex` stubs (signatures + docstrings for IDE / typecheckers)."""

def complex_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`complex` or subtype (``PyComplex_Check``)."""
    ...

def complex_check_exact(p: object) -> bool:
    """Return True if ``type(p) is complex`` (``PyComplex_CheckExact``)."""
    ...

def complex_from_doubles(real: float, imag: float) -> object:
    """Return ``complex(real, imag)`` via ``PyComplex_FromDoubles``."""
    ...

def complex_real_as_double(op: object) -> float:
    """Return the real part of ``op`` as a C ``double`` (``PyComplex_RealAsDouble``)."""
    ...

def complex_imag_as_double(op: object) -> float:
    """Return the imaginary part of ``op`` as a C ``double`` (``PyComplex_ImagAsDouble``)."""
    ...
