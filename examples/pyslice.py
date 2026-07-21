"""Python usage for cypy cyslice.

Run: python examples/pyslice.py
"""
from cypy import slice_check, slice_new, slice_unpack

def main() -> None:
    s = slice_new(1, 10, 2)
    assert slice_check(s)
    start, stop, step = slice_unpack(s)
    assert (start, stop, step) == (1, 10, 2)
    print("ok", start, stop, step)

if __name__ == "__main__":
    main()
