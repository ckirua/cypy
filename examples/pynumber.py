"""Python usage for cypy cynumber.

Run: python examples/pynumber.py
"""
from cypy import num_check, num_add, num_mul

def main() -> None:
    assert num_check(3)
    assert num_add(2, 3) == 5
    assert num_mul(4, 5) == 20
    print("ok", num_add(1, 1))

if __name__ == "__main__":
    main()
