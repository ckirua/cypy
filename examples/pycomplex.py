"""Python usage for cypy cycomplex.

Run: python examples/pycomplex.py
"""
from cypy import complex_check, complex_from_doubles, complex_real_as_double, complex_imag_as_double

def main() -> None:
    z = complex_from_doubles(1.5, -2.0)
    assert complex_check(z)
    assert complex_real_as_double(z) == 1.5
    assert complex_imag_as_double(z) == -2.0
    print("ok", z)

if __name__ == "__main__":
    main()
