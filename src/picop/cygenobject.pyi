"""Public :mod:`cypy.cygenobject` stubs."""

def gen_check(ob: object) -> bool:
    """Return True if ``ob`` is a generator (``PyGen_Check``)."""
    ...

def gen_check_exact(ob: object) -> bool:
    """Return True if ``type(ob) is types.GeneratorType`` (``PyGen_CheckExact``)."""
    ...

def gen_eq(a: object, b: object) -> bool:
    """Return True if ``a is b`` (generator identity; CPython ``object.__eq__``)."""
    ...
