"""Python usage for cypy cymemoryview.

Run: python examples/pymemoryview.py
"""
from cypy import memoryview_check, memoryview_from_object

def main() -> None:
    mv = memoryview_from_object(b"abc")
    assert memoryview_check(mv)
    assert bytes(mv) == b"abc"
    print("ok", bytes(mv))

if __name__ == "__main__":
    main()
