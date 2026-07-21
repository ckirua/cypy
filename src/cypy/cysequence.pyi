"""Public :mod:`cypy.cysequence` stubs (signatures + docstrings for IDE / typecheckers)."""

# Preferred public names (0.3 hard trim)

def seq_check(o: object) -> bool:
    """Return True if ``o`` supports the sequence protocol (``PySequence_Check``)."""
    ...

def seq_concat(o1: object, o2: object) -> object:
    """Return ``o1 + o2`` via ``PySequence_Concat``."""
    ...

def seq_contains(o: object, value: object) -> bool:
    """Return ``value in o`` via ``PySequence_Contains``."""
    ...

def seq_count(o: object, value: object) -> int:
    """Return ``o.count(value)`` via ``PySequence_Count``. Returns a count; on error raises (except -1) — do not treat -1 as a normal count without checking."""
    ...

def seq_del(o: object, i: int) -> int:
    """Delete ``o[i]`` via ``PySequence_DelItem`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def seq_del_slice(o: object, i1: int, i2: int) -> int:
    """Delete ``o[i1:i2]`` via ``PySequence_DelSlice`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def seq_get(o: object, i: int) -> object:
    """Return ``o[i]`` via ``PySequence_GetItem``."""
    ...

def seq_index(o: object, value: object) -> int:
    """Return ``o.index(value)`` via ``PySequence_Index``."""
    ...

def seq_inplace_concat(o1: object, o2: object) -> object:
    """Return ``o1 += o2`` result via ``PySequence_InPlaceConcat``."""
    ...

def seq_inplace_repeat(o: object, count: int) -> object:
    """Return ``o *= count`` result via ``PySequence_InPlaceRepeat``."""
    ...

def seq_len(o: object) -> int:
    """Return ``len(o)`` via ``PySequence_Length`` (alias of ``sqsize``)."""
    ...

def seq_list(o: object) -> list:
    """Return ``list(o)`` via ``PySequence_List`` (always a new list)."""
    ...

def seq_repeat(o: object, count: int) -> object:
    """Return ``o * count`` via ``PySequence_Repeat``."""
    ...

def seq_set(o: object, i: int, v: object) -> int:
    """Assign ``o[i] = v`` via ``PySequence_SetItem`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def seq_set_slice(o: object, i1: int, i2: int, v: object) -> int:
    """Assign ``o[i1:i2] = v`` via ``PySequence_SetSlice`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def seq_size(o: object) -> int:
    """Return ``len(o)`` via ``PySequence_Size``."""
    ...

def seq_slice(o: object, i1: int, i2: int) -> object:
    """Return ``o[i1:i2]`` via ``PySequence_GetSlice``."""
    ...

def seq_tuple(o: object) -> tuple:
    """Return ``tuple(o)`` via ``PySequence_Tuple``."""
    ...

