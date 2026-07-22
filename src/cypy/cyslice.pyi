"""Public :mod:`cypy.cyslice` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def slice_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`slice` (``PySlice_Check``)."""
    ...

def slice_eq(a: slice, b: slice) -> bool:
    """Return True if slices are equal (identity short-circuit + richcompare)."""
    ...

def slice_indices_ex(sl: object, length: int) -> tuple[int, int, int, int]:
    """Return ``(start, stop, step, slicelen)`` via ``PySlice_GetIndicesEx`` (clips like normal slices)."""
    ...

def slice_new(start: object = None, stop: object = None, step: object = None) -> slice:
    """Return ``slice(start, stop, step)`` via ``PySlice_New``."""
    ...

def slice_unpack(sl: object) -> tuple[int, int, int]:
    """Return ``(start, stop, step)`` as C integers via ``PySlice_Unpack``."""
    ...

