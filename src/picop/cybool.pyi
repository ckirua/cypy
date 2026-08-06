"""Public :mod:`cypy.cybool` stubs (signatures + docstrings for IDE / typecheckers)."""

def bool_check(o: object) -> bool:
    """Return True if ``o`` is a :class:`bool` (``PyBool_Check``)."""
    ...

def bool_eq(a: object, b: object) -> bool:
    """Return True if values are equal (identity short-circuit + richcompare)."""
    ...

def bool_from_long(v: int) -> object:
    """Return ``True`` or ``False`` via ``PyBool_FromLong`` (nonzero → True)."""
    ...

def bool_true() -> object:
    """Return ``True`` via ``PyBool_FromLong(1)``."""
    ...

def bool_false() -> object:
    """Return ``False`` via ``PyBool_FromLong(0)``."""
    ...
