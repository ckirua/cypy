"""Python usage for cypy cyobject.

Run: python examples/pyobject.py
"""
from cypy import obj_eq, obj_hasattr, obj_getattr_cstr, obj_len, obj_type
from cypy import protocols


def main() -> None:
    xs = [1, 2]
    assert obj_hasattr(xs, "append")
    meth = obj_getattr_cstr(xs, b"append")
    assert callable(meth)
    meth(3)
    assert xs == [1, 2, 3]
    assert obj_len(xs) == 3
    assert obj_type(xs) is list
    assert obj_eq(xs, [1, 2, 3]) and not obj_eq(xs, [1, 2])
    assert obj_eq(xs, xs)
    assert protocols.obj_eq("a", "a") and not protocols.obj_eq("a", "b")
    print("ok", obj_len(xs))


if __name__ == "__main__":
    main()
