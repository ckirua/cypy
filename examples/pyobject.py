"""Python usage for cypy cyobject.

Run: python examples/pyobject.py
"""
from cypy import obj_hasattr, obj_getattr_cstr, obj_len, obj_type

def main() -> None:
    xs = [1, 2]
    assert obj_hasattr(xs, "append")
    meth = obj_getattr_cstr(xs, b"append")
    assert callable(meth)
    meth(3)
    assert xs == [1, 2, 3]
    assert obj_len(xs) == 3
    assert obj_type(xs) is list
    print("ok", obj_len(xs))

if __name__ == "__main__":
    main()
