"""Public :mod:`cypy.cycellobject` stubs."""

def cell_check(ob: object) -> bool:
    """Return True if ``ob`` is a cell object (``PyCell_Check``)."""
    ...

def cell_new(ob: object) -> object:
    """Return a new cell containing ``ob`` (``PyCell_New``; ``ob`` may be ``None``)."""
    ...

def cell_get(cell: object) -> object:
    """Return the contents of ``cell`` via ``PyCell_Get``."""
    ...

def cell_set(cell: object, value: object) -> int:
    """Set the contents of ``cell`` via ``PyCell_Set``; returns 0. Returns 0 on success; errors raise — do not use as bool."""
    ...
