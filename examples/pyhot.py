"""Smoke for :mod:`cypy.hot` (DX-01 curated starters).

Run: python examples/pyhot.py
"""

from cypy.hot import (
    array_eq,
    bytearray_eq,
    bytes_contains,
    bytes_eq,
    bytes_len,
    bytes_ne,
    dict_get,
    dict_len,
    list_append,
    list_len,
    memoryview_eq,
    set_add,
    set_contains,
    str_len,
    tuple_pack2,
)

def main() -> None:
    d = {"a": 1}
    assert dict_get(d, "a") == 1 and dict_len(d) == 1
    xs: list[object] = []
    assert list_append(xs, 7) == 0 and list_len(xs) == 1
    s: set[object] = set()
    set_add(s, "x")
    assert set_contains(s, "x")
    assert tuple_pack2(1, 2) == (1, 2)
    assert bytes_len(b"ok") == 2 and bytes_contains(b"ab", b"a")
    assert bytes_eq(b"ok", b"ok") and not bytes_eq(b"ok", b"no")
    assert bytes_ne(b"ok", b"no") and not bytes_ne(b"ok", b"ok")
    assert bytearray_eq(bytearray(b"ok"), bytearray(b"ok"))
    from array import array as Array
    assert array_eq(Array("i", [1, 2]), Array("i", [1, 2]))
    assert memoryview_eq(memoryview(b"ok"), memoryview(b"ok"))
    assert str_len("hi") == 2
    print("ok", dict_len(d), list_len(xs), bytes_len(b"ok"))

if __name__ == "__main__":
    main()
