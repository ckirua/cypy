"""Python usage for cypy cyiterator.

Run: python examples/pyiterator.py
"""
from cypy import iter_check, iter_next

def main() -> None:
    it = iter([10, 20])
    assert iter_check(it)
    assert iter_next(it) == 10
    assert iter_next(it) == 20
    print("ok", iter_check(it))

if __name__ == "__main__":
    main()
