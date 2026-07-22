"""Python usage for cypy cymemoryview.

Run: python examples/pymemoryview.py
"""
from cypy import memoryview_check, memoryview_eq, memoryview_from_object

def main() -> None:
    mv = memoryview_from_object(b"abc")
    assert memoryview_check(mv)
    assert bytes(mv) == b"abc"
    assert memoryview_eq(mv, memoryview(b"abc"))
    assert not memoryview_eq(mv, memoryview(b"abd"))
    assert memoryview_eq(memoryview(b""), memoryview(b""))
    print("ok", bytes(mv))

if __name__ == "__main__":
    main()
