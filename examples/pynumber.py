"""Python usage for cypy cynumber.

Run: python examples/pynumber.py
"""
from cypy import num_check, num_add, num_mul, num_eq
from cypy import protocols


def main() -> None:
    assert num_check(3)
    assert num_add(2, 3) == 5
    assert num_mul(4, 5) == 20
    assert num_eq(1, 1) and not num_eq(1, 2) and num_eq(0, 0)
    assert num_eq(1.5, 1.5) and num_eq(0.0, -0.0) and num_eq(1, 1.0)
    assert num_eq(1 + 0j, 1) and not num_eq(1j, 2j)
    nan = float("nan")
    assert not num_eq(nan, nan) and not (nan == nan)
    assert protocols.num_eq(10, 10) and not protocols.num_eq(10, 11)
    print("ok", num_add(1, 1))


if __name__ == "__main__":
    main()
