"""Public :mod:`cypy.cygc` stubs (signatures + docstrings for IDE / typecheckers)."""

def gc_collect() -> int:
    """Run a full GC collection via ``PyGC_Collect``; return unreachable count."""
    ...

def gc_is_enabled() -> bool:
    """Return whether automatic GC is enabled via ``PyGC_IsEnabled``."""
    ...

def gc_enable() -> int:
    """Enable automatic GC via ``PyGC_Enable``; return the prior enabled flag."""
    ...

def gc_disable() -> int:
    """Disable automatic GC via ``PyGC_Disable``; return the prior enabled flag."""
    ...
