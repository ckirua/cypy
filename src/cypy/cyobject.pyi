"""Public :mod:`cypy.cyobject` stubs (signatures + docstrings for IDE / typecheckers)."""

def obj_hasattr(o: object, name: object) -> bool:
    """Return True if ``o`` has attribute ``name`` (``PyObject_HasAttr``)."""
    ...

def obj_getattr(o: object, name: object) -> object:
    """Return ``getattr(o, name)`` via ``PyObject_GetAttr``."""
    ...

def obj_setattr(o: object, name: object, v: object) -> int:
    """Set attribute ``name`` on ``o`` via ``PyObject_SetAttr``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_delattr(o: object, name: object) -> int:
    """Delete attribute ``name`` on ``o`` via ``PyObject_DelAttr``. Returns 0 on success; errors raise — do not use as bool."""
    ...

def obj_richcompare(o1: object, o2: object, opid: int) -> object:
    """Return rich comparison of ``o1`` and ``o2`` for ``opid`` (``Py_EQ`` …)."""
    ...

def obj_richcompare_bool(o1: object, o2: object, opid: int) -> bool:
    """Return rich comparison as bool for ``opid`` (``PyObject_RichCompareBool``)."""
    ...

def obj_repr(o: object) -> object:
    """Return ``repr(o)`` via ``PyObject_Repr``."""
    ...

def obj_str(o: object) -> object:
    """Return ``str(o)`` via ``PyObject_Str``."""
    ...

def obj_bytes(o: object) -> object:
    """Return ``bytes(o)`` via ``PyObject_Bytes``."""
    ...

def obj_isinstance(inst: object, cls: object) -> bool:
    """Return ``isinstance(inst, cls)`` via ``PyObject_IsInstance``."""
    ...

def obj_issubclass(derived: object, cls: object) -> bool:
    """Return ``issubclass(derived, cls)`` via ``PyObject_IsSubclass``."""
    ...

def obj_callable(o: object) -> bool:
    """Return True if ``o`` is callable (``PyCallable_Check``)."""
    ...

def obj_call(callable_object: object, args: object, kw: object = None) -> object:
    """Call ``callable_object(*args, **kw)`` via ``PyObject_Call`` (``args`` is a tuple)."""
    ...

def obj_call_object(callable_object: object, args: object) -> object:
    """Call ``callable_object(*args)`` via ``PyObject_CallObject``."""
    ...

def obj_hash(o: object) -> int:
    """Return ``hash(o)`` via ``PyObject_Hash``."""
    ...

def obj_istrue(o: object) -> bool:
    """Return ``bool(o)`` via ``PyObject_IsTrue``."""
    ...

def obj_not(o: object) -> bool:
    """Return ``not o`` via ``PyObject_Not``."""
    ...

def obj_type(o: object) -> object:
    """Return ``type(o)`` via ``PyObject_Type``."""
    ...

def obj_len(o: object) -> int:
    """Return ``len(o)`` via ``PyObject_Length``."""
    ...

def obj_size(o: object) -> int:
    """Return ``len(o)`` via ``PyObject_Size`` (Length alias)."""
    ...

def obj_length_hint(o: object, default_value: int) -> int:
    """Return ``operator.length_hint(o, default_value)`` via ``PyObject_LengthHint``."""
    ...

def obj_getitem(o: object, key: object) -> object:
    """Return ``o[key]`` via ``PyObject_GetItem``."""
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

# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def obj_hasattr_cstr(o: object, name: bytes) -> bool:
    """Return True if ``o`` has C-string attribute ``name`` (``PyObject_HasAttrString``). Alias of ``obj_hasattr_string`` (prefer ``*_cstr`` naming)."""
    ...

def obj_getattr_cstr(o: object, name: bytes) -> object:
    """Return attribute ``name`` via ``PyObject_GetAttrString``. Alias of ``obj_getattr_string`` (prefer ``*_cstr`` naming)."""
    ...

def obj_setattr_cstr(o: object, name: bytes, v: object) -> int:
    """Set C-string attribute ``name`` on ``o`` via ``PyObject_SetAttrString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``obj_setattr_string`` (prefer ``*_cstr`` naming)."""
    ...

def obj_delattr_cstr(o: object, name: bytes) -> int:
    """Delete C-string attribute ``name`` via ``PyObject_DelAttrString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``obj_delattr_string`` (prefer ``*_cstr`` naming)."""
    ...

