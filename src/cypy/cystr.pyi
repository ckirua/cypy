"""Public :mod:`cypy.cystr` stubs (signatures + docstrings for IDE / typecheckers)."""

def str_or_none(obj: object) -> str | None:
    """Return ``obj`` if exact ``str``, else ``None``."""
    ...

def str_or_empty(obj: object) -> str:
    """Return ``obj`` if truthy exact ``str``, else ``""``."""
    ...

# Preferred public names (0.3 hard trim)

def str_all_alnum_ascii(s: str) -> bool:
    """Return True if ``s`` is non-empty and every code unit is ASCII alnum."""
    ...

def str_all_alpha_ascii(s: str) -> bool:
    """Return True if ``s`` is non-empty and every code unit is ASCII ``A-Za-z``."""
    ...

def str_all_digits(s: str) -> bool:
    """Return True if ``s`` is non-empty and every code unit is ASCII ``0-9``."""
    ...

def str_as_or_empty(obj: object) -> str:
    """Return ``obj`` if it is an exact ``str``, else ``""``."""
    ...

def str_char_at(s: str, i: int) -> int:
    """Return the code point at ``i`` via ``PyUnicode_READ`` (**unchecked** — OOB is undefined)."""
    ...

def str_concat(a: str, b: str) -> str:
    """Return ``a + b`` via ``PyUnicode_Concat``."""
    ...

def str_concat3(a: str, b: str, c: str) -> str:
    """Return ``a + b + c`` via two ``PyUnicode_Concat`` calls."""
    ...

def str_concat4(a: str, b: str, c: str, d: str) -> str:
    """Return ``a + b + c + d`` via three ``PyUnicode_Concat`` calls."""
    ...

def str_contains(haystack: str, needle: str) -> bool:
    """Return whether ``needle`` is in ``haystack`` (1BYTE ``memchr``/``memmem`` / Find)."""
    ...

def str_endswith(s: str, suffix: str) -> bool:
    """Return whether ``s`` ends with ``suffix`` (1BYTE ``memcmp`` / Tailmatch)."""
    ...

def str_first_char(s: str) -> int:
    """Return the first code point via ``PyUnicode_READ`` (**unchecked** — empty string is undefined)."""
    ...

def str_is_blank(s: str) -> bool:
    """Return True if every code unit is ASCII whitespace (space/tab/LF/VT/FF/CR)."""
    ...

def str_is_empty(s: str) -> bool:
    """Return True if ``s`` has length 0."""
    ...

def str_is_not(obj: object) -> bool:
    """Return True if ``type(obj) is not str``."""
    ...

def str_is(obj: object) -> bool:
    """Return True if ``type(obj) is str``. Same gate as ``str_check_exact`` (N3); alias of ``is_str``."""
    ...

def str_last_char(s: str) -> int:
    """Return the last code point via ``PyUnicode_READ`` (**unchecked** — empty string is undefined)."""
    ...

def str_none_to_empty(obj: object) -> str:
    """Return ``obj`` if exact ``str``, else ``""`` (including when ``obj is None``)."""
    ...

def str_not_empty(s: str) -> bool:
    """Return True if ``s`` has non-zero length."""
    ...

def str_startswith(s: str, prefix: str) -> bool:
    """Return whether ``s`` starts with ``prefix`` (1BYTE ``memcmp`` / Tailmatch)."""
    ...

def str_eq(a: str, b: str) -> bool:
    """Return whether ``a == b`` (1BYTE ``memcmp`` / ``PyUnicode_Compare``)."""
    ...

def str_len(s: str) -> int:
    """Return ``len(s)`` via ``PyUnicode_GET_LENGTH``."""
    ...

def str_ne(a: str, b: str) -> bool:
    """Return whether ``a != b`` (negated ``streq``)."""
    ...

def str_check(obj: object) -> bool:
    """Return True if ``obj`` is a :class:`str` or subtype (``PyUnicode_Check``)."""
    ...

def str_check_exact(obj: object) -> bool:
    """Return True if ``type(obj) is str`` (``PyUnicode_CheckExact``). Prefer over ``str_is`` / ``is_str`` / ``ucheck_exact`` in check-pair tables (N3)."""
    ...

