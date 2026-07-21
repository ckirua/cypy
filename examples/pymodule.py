"""Python usage for cypy cymodule.

Run: python examples/pymodule.py
"""
import sys
from cypy import mod_check, mod_get_name

def main() -> None:
    m = sys.modules["sys"]
    assert mod_check(m)
    assert mod_get_name(m) == "sys"
    print("ok", mod_get_name(m))

if __name__ == "__main__":
    main()
