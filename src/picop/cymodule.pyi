"""Public :mod:`cypy.cymodule` stubs (signatures + docstrings for IDE / typecheckers)."""

def mod_check(p: object) -> bool:
    """Return True if ``p`` is a module or subtype (``PyModule_Check``)."""
    ...

def mod_check_exact(p: object) -> bool:
    """Return True if ``type(p) is types.ModuleType`` (``PyModule_CheckExact``)."""
    ...

def mod_eq(a: object, b: object) -> bool:
    """Return True if ``a is b`` (module-object identity; CPython ``object.__eq__``)."""
    ...

def mod_new(name: bytes) -> object:
    """Return a new module named ``name`` via ``PyModule_New``."""
    ...

def mod_new_object(name: object) -> object:
    """Return a new module named ``name`` via ``PyModule_NewObject``."""
    ...

def mod_get_name(module: object) -> object:
    """Return ``module.__name__`` via ``PyModule_GetNameObject``."""
    ...

def mod_get_filename(module: object) -> object:
    """Return ``module.__file__`` via ``PyModule_GetFilenameObject``."""
    ...

def mod_add_object_ref(module: object, name: bytes, value: object) -> int:
    """Add ``value`` as ``name`` without stealing the reference (``PyModule_AddObjectRef``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def mod_add_int(module: object, name: bytes, value: int) -> int:
    """Add integer constant ``name`` via ``PyModule_AddIntConstant``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def mod_import(name: bytes) -> object:
    """Import module ``name`` via ``PyImport_ImportModule``."""
    ...

def mod_import_object(name: object) -> object:
    """Import module ``name`` via ``PyImport_Import``."""
    ...

def mod_reload(m: object) -> object:
    """Reload module ``m`` via ``PyImport_ReloadModule``."""
    ...

def mod_magic_number() -> int:
    """Return the ``.pyc`` magic number via ``PyImport_GetMagicNumber``."""
    ...

# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def mod_add_cstr(module: object, name: bytes, value: bytes) -> int:
    """Add string constant ``name`` via ``PyModule_AddStringConstant``. Returns 0 on success; errors raise — do not use as bool. Alias of ``mod_add_string`` (prefer ``*_cstr`` naming)."""
    ...

