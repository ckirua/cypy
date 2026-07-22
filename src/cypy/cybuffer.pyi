"""Public :mod:`cypy.cybuffer` stubs (signatures + docstrings for IDE / typecheckers)."""

def buf_check(obj: object) -> bool:
    """Return True if ``obj`` supports the buffer protocol (``PyObject_CheckBuffer``)."""
    ...

def buf_copy_data(dest: object, src: object) -> int:
    """Copy buffer data from ``src`` into writable ``dest`` via ``PyObject_CopyData`` (``0`` / ``-1``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def buf_eq(a: object, b: object) -> bool:
    """Return True if buffer-protocol views are equal (C-contiguous ``memcmp``; else memoryview richcompare). Format/size mismatch → False."""
    ...
