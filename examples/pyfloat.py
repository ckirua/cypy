"""Python usage for cypy cyfloat.

Run: python examples/pyfloat.py
"""
from cypy import float_check, float_from_double, float_as_double

def main() -> None:
    x = float_from_double(2.5)
    assert float_check(x) and float_as_double(x) == 2.5
    print("ok", x)

if __name__ == "__main__":
    main()
