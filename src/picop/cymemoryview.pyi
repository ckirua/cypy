"""Public :mod:`cypy.cymemoryview` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def memoryview_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`memoryview` (``PyMemoryView_Check``)."""
    ...

def memoryview_eq(a: memoryview, b: memoryview) -> bool:
    """Return True if views are equal (C-contiguous ``memcmp`` fast path; else richcompare)."""
    ...

def memoryview_ne(a: memoryview, b: memoryview) -> bool:
    """Return True if views differ (``not memoryview_eq``; same contig/richcompare rules)."""
    ...

def memoryview_from_object(obj: object) -> memoryview:
    """Return ``memoryview(obj)`` via ``PyMemoryView_FromObject``."""
    ...

def memoryview_get_contiguous(obj: object, buffertype: int = ..., order: str = "C") -> memoryview:
    """Return a contiguous memoryview of ``obj`` via ``PyMemoryView_GetContiguous`` (``order`` is ``C``/``F``/``A``)."""
    ...

