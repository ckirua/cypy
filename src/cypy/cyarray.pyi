"""Public :mod:`cypy.cyarray` stubs (signatures + docstrings for IDE / typecheckers)."""

from array import array

# Preferred public names (0.3 hard trim)

def array_check(p: object) -> bool:
    """Return True if ``p`` is an :class:`array.array` (``isinstance``)."""
    ...

def array_check_exact(p: object) -> bool:
    """Return True if ``type(p) is array.array``."""
    ...

def array_clone(template: array, length: int, zero: bool = True) -> array:
    """Return a new array like ``template`` with ``length`` items (optionally zeroed)."""
    ...

def array_copy(a: array) -> array:
    """Return a shallow copy of ``a`` via Cython ``array.copy``."""
    ...

def array_extend(self: array, other: array) -> int:
    """Extend ``self`` from ``other`` (same typecode) via Cython ``array.extend`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def array_len(a: array) -> int:
    """Return ``len(a)`` via ``Py_SIZE``."""
    ...

def array_resize(a: array, n: int) -> int:
    """Resize ``a`` to ``n`` elements via Cython ``array.resize`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def array_resize_smart(a: array, n: int) -> int:
    """Resize ``a`` to ``n`` via Cython ``array.resize_smart`` (small-grow friendly; ``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def array_zero(a: array) -> int:
    """Zero all elements of ``a`` via ``memset`` (``0``). Returns 0 on success; errors raise — do not use as bool."""
    ...

