"""Python usage for cypy cybytearray.

Run: python examples/pybytearray.py
"""
from cypy import bytearray_check, bytearray_from_object, bytearray_len

def main() -> None:
    ba = bytearray(b"hi")
    assert bytearray_check(ba) and bytearray_len(ba) == 2
    again = bytearray_from_object(b"xy")
    assert isinstance(again, bytearray) and bytes(again) == b"xy"
    print("ok", bytearray_len(ba))

if __name__ == "__main__":
    main()
