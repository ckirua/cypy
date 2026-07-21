"""Python usage for cypy cybuffer.

Run: python examples/pybuffer.py
"""
from cypy import buf_check, buf_copy_data

def main() -> None:
    src = bytearray(b"abc")
    dest = bytearray(3)
    assert buf_check(src) is True
    assert buf_check(object()) is False
    assert buf_copy_data(dest, src) == 0
    assert bytes(dest) == b"abc"
    print("ok", bytes(dest))

if __name__ == "__main__":
    main()
