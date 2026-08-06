"""Public :mod:`cypy.cybytearray` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def bytearray_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`bytearray` or subtype (``PyByteArray_Check``)."""
    ...

def bytearray_check_exact(p: object) -> bool:
    """Return True if ``type(p) is bytearray`` (``PyByteArray_CheckExact``)."""
    ...

def bytearray_concat(a: object, b: object) -> bytearray:
    """Return a new bytearray concatenating ``a`` and ``b`` via ``PyByteArray_Concat``."""
    ...

def bytearray_from_object(o: object) -> bytearray:
    """Return ``bytearray(o)`` via ``PyByteArray_FromObject`` (buffer protocol)."""
    ...

def bytearray_len(ba: bytearray) -> int:
    """Return ``len(ba)`` via ``PyByteArray_GET_SIZE``."""
    ...

def bytearray_eq(a: bytearray, b: bytearray) -> bool:
    """Return True if typed ``bytearray`` values are equal (identity/len/`memcmp`)."""
    ...

def bytearray_ne(a: bytearray, b: bytearray) -> bool:
    """Return True if typed ``bytearray`` values differ (``not bytearray_eq``)."""
    ...

def bytearray_contains(haystack: bytearray, needle: bytes) -> bool:
    """Return True if ``needle`` is found in typed ``haystack`` (mirror ``bytes_contains``)."""
    ...

def bytearray_resize(ba: bytearray, n: int) -> int:
    """Resize ``ba`` in place via ``PyByteArray_Resize`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def bytearray_size(ba: object) -> int:
    """Return ``len(ba)`` via checked ``PyByteArray_Size`` (prefer ``balen`` on typed ``bytearray``)."""
    ...

