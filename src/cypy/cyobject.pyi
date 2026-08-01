"""Public :mod:`cypy.cyobject` stubs (signatures + docstrings for IDE / typecheckers).

Tier A losers (ratio > 1.02 vs builtins) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work. Prefer builtins or typed
container helpers from Python; use equality helpers below when needed.
"""

def obj_richcompare(o1: object, o2: object, opid: int) -> object:
    """Return rich comparison of ``o1`` and ``o2`` for ``opid`` (``Py_EQ`` …)."""
    ...

def obj_richcompare_bool(o1: object, o2: object, opid: int) -> bool:
    """Return rich comparison as bool for ``opid`` (``PyObject_RichCompareBool``)."""
    ...

def obj_eq(a: object, b: object) -> bool:
    """Return True if ``a == b`` via ``PyObject_RichCompareBool`` (identity short-circuit; prefer typed ``*_eq``)."""
    ...

def obj_setattr(o: object, name: object, v: object) -> int:
    """Set attribute ``name`` on ``o`` via ``PyObject_SetAttr``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_delattr(o: object, name: object) -> int:
    """Delete attribute ``name`` on ``o`` via ``PyObject_DelAttr``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_repr(o: object) -> object:
    """Return ``repr(o)`` via ``PyObject_Repr``."""
    ...

def obj_bytes(o: object) -> object:
    """Return ``bytes(o)`` via ``PyObject_Bytes``."""
    ...

def obj_issubclass(derived: object, cls: object) -> bool:
    """Return ``issubclass(derived, cls)`` via ``PyObject_IsSubclass``."""
    ...

def obj_call(callable_object: object, args: object, kw: object = None) -> object:
    """Call ``callable_object(*args, **kw)`` via ``PyObject_Call`` (``args`` is a tuple)."""
    ...

def obj_call_object(callable_object: object, args: object) -> object:
    """Call ``callable_object(*args)`` via ``PyObject_CallObject``."""
    ...

def obj_not(o: object) -> bool:
    """Return ``not o`` via ``PyObject_Not``."""
    ...

def obj_length_hint(o: object, default_value: int) -> int:
    """Return ``operator.length_hint(o, default_value)`` via ``PyObject_LengthHint``."""
    ...

def obj_setitem(o: object, key: object, v: object) -> int:
    """Set ``o[key] = v`` via ``PyObject_SetItem``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_delitem(o: object, key: object) -> int:
    """Delete ``o[key]`` via ``PyObject_DelItem``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_as_fd(o: object) -> int:
    """Return a file descriptor via ``PyObject_AsFileDescriptor``. Returns a file descriptor; on error raises — do not use as a boolean."""
    ...

def obj_dir(o: object) -> object:
    """Return ``dir(o)`` via ``PyObject_Dir``."""
    ...

def obj_iter(o: object) -> object:
    """Return ``iter(o)`` via ``PyObject_GetIter``."""
    ...

def obj_format(obj: object, format_spec: object) -> object:
    """Return ``format(obj, format_spec)`` via ``PyObject_Format``."""
    ...

def obj_setattr_cstr(o: object, name: bytes, v: object) -> int:
    """Set C-string attribute ``name`` on ``o`` via ``PyObject_SetAttrString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``obj_setattr_string`` (prefer ``*_cstr`` naming)."""
    ...

def obj_delattr_cstr(o: object, name: bytes) -> int:
    """Delete C-string attribute ``name`` via ``PyObject_DelAttrString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``obj_delattr_string`` (prefer ``*_cstr`` naming)."""
    ...
