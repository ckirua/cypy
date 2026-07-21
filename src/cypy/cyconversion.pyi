"""Public :mod:`cypy.cyconversion` stubs."""
def conv_stricmp(s1: bytes, s2: bytes) -> int:
    """Case-insensitive C-string compare via ``PyOS_stricmp``."""
    ...
def conv_strnicmp(s1: bytes, s2: bytes, size: int) -> int:
    """Case-insensitive compare of at most ``size`` bytes via ``PyOS_strnicmp``."""
    ...

# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def conv_cstr_to_double(s: bytes) -> float:
    """Parse ``s`` as a C double via ``PyOS_string_to_double`` (no surrounding whitespace). Alias of ``conv_string_to_double`` (prefer ``*_cstr`` naming)."""
    ...

