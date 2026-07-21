"""Public :mod:`cypy.cyfileobject` stubs."""
def file_from_fd(fd: int, name: bytes, mode: bytes, buffering: int = -1, encoding: bytes | None = None, errors: bytes | None = None, newline: bytes | None = None, closefd: int = 1) -> object:
    """Wrap OS ``fd`` as a Python file via ``PyFile_FromFd``."""
    ...
def file_getline(p: object, n: int = -1) -> object:
    """Read a line from file ``p`` via ``PyFile_GetLine``."""
    ...
def file_write_object(obj: object, p: object, flags: int = 0) -> int:
    """Write ``obj`` to file ``p`` via ``PyFile_WriteObject``. Returns 0 on success; errors raise — do not use as bool."""
    ...
# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def file_write_cstr(s: bytes, p: object) -> int:
    """Write C string ``s`` to file ``p`` via ``PyFile_WriteString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``file_write_string`` (prefer ``*_cstr`` naming)."""
    ...

