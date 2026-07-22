"""Public :mod:`cypy.cyunicode` stubs (signatures + docstrings for IDE / typecheckers)."""

def uutf8_bytes(s: str) -> bytes:
    """Return owning UTF-8 ``bytes`` for ``s`` via ``PyUnicode_AsUTF8String``."""
    ...

def uintern(s: str) -> str:
    """Intern ``s`` via ``PyUnicode_InternInPlace`` and return the canonical instance."""
    ...

def unicode_eq(a: str, b: str) -> bool:
    """Return True if ``a == b`` — thin alias of ``str_eq`` (same semantics)."""
    ...

