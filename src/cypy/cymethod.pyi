"""Public :mod:`cypy.cymethod` stubs (signatures + docstrings for IDE / typecheckers)."""

def method_check(o: object) -> bool:
    """Return True if ``o`` is a bound method (``PyMethod_Check``)."""
    ...

def method_new(func: object, self: object) -> object:
    """Return a bound method via ``PyMethod_New(func, self)``."""
    ...

def method_get_function(meth: object) -> object:
    """Preferred spelling of ``method_function`` (checked ``PyMethod_Function``)."""
    ...

def method_get_self(meth: object) -> object | None:
    """Preferred spelling of ``method_self`` (checked ``PyMethod_Self``)."""
    ...
