"""Public :mod:`cypy.cydict` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def dict_check(p: object) -> bool:
    """Return True if ``p`` is a :class:`dict` or subtype (``PyDict_Check``)."""
    ...

def dict_check_exact(p: object) -> bool:
    """Return True if ``type(p) is dict`` (``PyDict_CheckExact``)."""
    ...

def dict_clear(d: dict) -> None:
    """Clear ``d`` via ``PyDict_Clear``."""
    ...

def dict_contains(d: dict, key: str) -> bool:
    """Return whether ``key`` is in ``d`` (``PyDict_Contains``)."""
    ...

def dict_copy(d: dict) -> dict:
    """Return a shallow copy of ``d`` via ``PyDict_Copy``."""
    ...

def dict_del(d: dict, key: str) -> int:
    """Delete ``d[key]`` via ``PyDict_DelItem`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def dict_get(d: dict, key: str) -> object:
    """Return ``d[key]`` via borrowed ``PyDict_GetItem`` (missing and stored ``None`` both yield ``None``)."""
    ...

def dict_get_ref(d: dict, key: object) -> object:
    """Return a strong ref to ``d[key]`` via ``PyDict_GetItemRef`` (missing → ``None``; stored ``None`` is distinct)."""
    ...

def dict_get_with_error(d: dict, key: object) -> object:
    """Return ``d[key]`` via ``PyDict_GetItemWithError`` (hash/eq errors propagate; missing → ``None``)."""
    ...

def dict_len(d: dict) -> int:
    """Return ``len(d)`` via ``PyDict_GET_SIZE``."""
    ...

def dict_eq(a: dict, b: dict) -> bool:
    """Return True if typed dicts are equal (identity/size short-circuit + richcompare)."""
    ...

def dict_merge(d: dict, other: object, override: bool = True) -> int:
    """Merge ``other`` into ``d`` via ``PyDict_Merge`` (``override`` controls overwrite). Returns 0 on success; errors raise — do not use as bool."""
    ...

def dict_merge_from_seq2(d: dict, seq2: object, override: bool = True) -> int:
    """Merge key/value pairs from ``seq2`` via ``PyDict_MergeFromSeq2``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def dict_new() -> dict:
    """Return a new empty :class:`dict` (``PyDict_New``)."""
    ...

def dict_pop(d: dict, key: str) -> object:
    """Remove ``key`` and return its value via ``PyDict_Pop`` (missing → ``None``)."""
    ...

def dict_proxy(d: dict) -> object:
    """Return a read-only ``mappingproxy`` over ``d`` (``PyDictProxy_New``)."""
    ...

def dict_set(d: dict, key: str, value: object) -> int:
    """Set ``d[key] = value`` via ``PyDict_SetItem`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def dict_setdefault(d: dict, key: str, default: object = None) -> object:
    """Return ``d.setdefault(key, default)`` via borrowed ``PyDict_SetDefault``."""
    ...

def dict_setdefault_ref(d: dict, key: object, default: object = None) -> object:
    """Return ``setdefault`` via strong-ref ``PyDict_SetDefaultRef``."""
    ...

def dict_size(d: object) -> int:
    """Return ``len(d)`` via checked ``PyDict_Size`` (prefer ``dlen`` on typed ``dict``)."""
    ...

def dict_update(d: dict, other: dict) -> int:
    """Update ``d`` from ``other`` via ``PyDict_Update`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

