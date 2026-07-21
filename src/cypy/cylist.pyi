"""Public :mod:`cypy.cylist` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def list_append(l: list, value: object) -> int:
    """Append ``value`` via ``PyList_Append`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_as_tuple(l: list) -> tuple:
    """Return ``tuple(l)`` via ``PyList_AsTuple``."""
    ...

def list_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`list` or subtype (``PyList_Check``)."""
    ...

def list_check_exact(p: object) -> bool:
    """Return True if ``type(p) is list`` (``PyList_CheckExact``)."""
    ...

def list_clear(l: list) -> int:
    """Clear ``l`` via ``PyList_Clear`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_copy(l: list) -> list:
    """Return a shallow copy of ``l`` via ``PyList_GetSlice``."""
    ...

def list_empty() -> list:
    """Return a new empty list via ``PyList_New(0)``."""
    ...

def list_extend(l: list, iterable: object) -> int:
    """Extend ``l`` from ``iterable`` via ``PyList_Extend`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_get(l: list, i: int) -> object:
    """Return ``l[i]`` via ``PyList_GET_ITEM`` (**unchecked** — OOB is undefined; prefer ``lget_checked`` when unsure)."""
    ...

def list_get_checked(l: list, i: int) -> object:
    """Return ``l[i]`` via bounds-checked ``PyList_GetItem`` (raises ``IndexError``)."""
    ...

def list_get_ref(l: list, i: int) -> object:
    """Return a strong ref to ``l[i]`` via ``PyList_GetItemRef`` (raises ``IndexError``)."""
    ...

def list_insert(l: list, i: int, value: object) -> int:
    """Insert ``value`` at ``i`` via ``PyList_Insert`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_len(l: list) -> int:
    """Return ``len(l)`` via ``PyList_GET_SIZE``."""
    ...

def list_reverse(l: list) -> int:
    """Reverse ``l`` in place via ``PyList_Reverse`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_set_item(l: list, i: int, value: object) -> int:
    """Set ``l[i] = value`` via ``PyList_SetItem`` (INCREF then steal; ``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_set_slice(l: list, low: int, high: int, itemlist: object = None) -> int:
    """Assign ``l[low:high] = itemlist`` via ``PyList_SetSlice`` (``None`` deletes the slice). Returns 0 on success; errors raise — do not use as bool."""
    ...

def list_size(l: object) -> int:
    """Return ``len(l)`` via checked ``PyList_Size`` (prefer ``llen`` on typed ``list``)."""
    ...

def list_slice(l: list, low: int, high: int) -> list:
    """Return ``l[low:high]`` via ``PyList_GetSlice``."""
    ...

def list_sort(l: list) -> int:
    """Sort ``l`` in place via ``PyList_Sort`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

