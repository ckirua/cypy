"""Public :mod:`cypy.cymapping` stubs."""
def map_check(o: object) -> bool:
    """Return True if ``o`` provides the mapping protocol."""
    ...
def map_eq(a: object, b: object) -> bool:
    """Return True if mappings are equal (identity/size short-circuit + richcompare; prefer ``dict_eq`` when typed)."""
    ...
def map_len(o: object) -> int:
    """Return ``len(o)`` via ``PyMapping_Length``."""
    ...
def map_has_key(o: object, key: object) -> bool:
    """Return True if mapping ``o`` has ``key``."""
    ...
def map_del(o: object, key: object) -> int:
    """Delete ``o[key]`` via ``PyMapping_DelItem``. Returns 0 on success; errors raise — do not use as bool."""
    ...
def map_keys(o: object) -> object:
    """Return ``o.keys()`` via ``PyMapping_Keys``."""
    ...
def map_values(o: object) -> object:
    """Return ``o.values()`` via ``PyMapping_Values``."""
    ...
def map_items(o: object) -> object:
    """Return ``o.items()`` via ``PyMapping_Items``."""
    ...
# N2 preferred ``*_cstr`` (0.3: ``*_string`` removed from stubs)
def map_has_key_cstr(o: object, key: bytes) -> bool:
    """Return True if mapping ``o`` has C-string ``key``. Alias of ``map_has_key_string`` (prefer ``*_cstr`` naming)."""
    ...

def map_del_cstr(o: object, key: bytes) -> int:
    """Delete ``o[key]`` via ``PyMapping_DelItemString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``map_del_string`` (prefer ``*_cstr`` naming)."""
    ...

def map_getitem_cstr(o: object, key: bytes) -> object:
    """Return ``o[key]`` via ``PyMapping_GetItemString`` (``key`` must be ``bytes``, not ``str``). Alias of ``map_getitem_string`` (prefer ``*_cstr`` naming)."""
    ...

def map_setitem_cstr(o: object, key: bytes, v: object) -> int:
    """Set ``o[key] = v`` via ``PyMapping_SetItemString``. Returns 0 on success; errors raise — do not use as bool. Alias of ``map_setitem_string`` (prefer ``*_cstr`` naming)."""
    ...

