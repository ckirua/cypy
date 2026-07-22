"""Python usage for cypy cyunicode.

Run: python examples/pyunicode.py

Cimport-only ``unicode_from_string``: see ``bench/tier_b/cyunicode_tb.pyx`` smoke.
"""
from cypy import uutf8_bytes, uintern

def main() -> None:
    b = uutf8_bytes("hi")
    assert b == b"hi"
    s = uintern("phase6")
    assert s is uintern("phase6")
    print("ok", b, s)

if __name__ == "__main__":
    main()
