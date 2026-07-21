"""Python usage for cypy cylong.

Run: python examples/pylong.py
"""
from cypy import long_check, long_from_long, long_from_ssize

def main() -> None:
    n = long_from_long(99)
    assert long_check(n) and n == 99
    assert long_from_ssize(7) == 7
    print("ok", n)

if __name__ == "__main__":
    main()
