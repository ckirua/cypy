"""Public :mod:`cypy.cybytes` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def bytes_check(p: object) -> bool:
    """Return True if ``p`` is :class:`bytes` or a subtype (``PyBytes_Check``)."""
    ...

def bytes_check_exact(p: object) -> bool:
    """Return True if ``type(p) is bytes`` (``PyBytes_CheckExact``)."""
    ...

def bytes_contains(haystack: bytes, needle: bytes) -> bool:
    """Return True if ``needle`` is in ``haystack`` (``memchr``/``memmem`` under 256B, else ``in``)."""
    ...

def bytes_eq(a: bytes, b: bytes) -> bool:
    """Return True if ``a == b`` (identity/len check + ``memcmp`` on typed ``bytes``)."""
    ...

def bytes_from_object(o: object) -> bytes:
    """Return ``bytes`` from a buffer-protocol object (``PyBytes_FromObject``)."""
    ...

def bytes_len(b: bytes) -> int:
    """Return ``len(b)`` via ``PyBytes_GET_SIZE``."""
    ...

def bytes_size(b: object) -> int:
    """Return ``len(b)`` via checked ``PyBytes_Size`` (prefer ``bytes_len`` on typed ``bytes``)."""
    ...

