"""Python usage for cypy cytype.

Run: python examples/pytype.py
"""
from cypy import type_check, type_check_exact, type_is_subtype

def main() -> None:
    assert type_check(int) and type_check_exact(int)
    assert type_is_subtype(bool, int)
    print("ok", type_is_subtype(bool, int))

if __name__ == "__main__":
    main()
