"""Python usage for cypy cybool.

Run: python examples/pybool.py
"""
from cypy import bool_check, bool_from_long, bool_true, bool_false

def main() -> None:
    assert bool_check(True) and bool_check(False)
    assert not bool_check(1)
    assert bool_from_long(1) is True
    assert bool_from_long(0) is False
    assert bool_true() is True and bool_false() is False
    print("ok", bool_check(True), bool_from_long(2))

if __name__ == "__main__":
    main()
