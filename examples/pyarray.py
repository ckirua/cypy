"""Python usage of :mod:`cypy` array helpers.

Run: python examples/pyarray.py
"""

from array import array

from cypy import array_check, array_clone, array_len, array_zero
PAYLOAD = array("i", [1, 2, 3, 4])

def main() -> None:
    print(f"array_check(payload) -> {array_check(PAYLOAD)!r}")
    print(f"array_len(payload) -> {array_len(PAYLOAD)!r}")
    assert array_check(PAYLOAD) is True
    assert array_len(PAYLOAD) == len(PAYLOAD)

    clone = array_clone(PAYLOAD, 4, zero=True)
    print(f"array_clone(..., zero=True) -> {list(clone)!r}")
    assert list(clone) == [0, 0, 0, 0]

    filled = array_clone(PAYLOAD, 3, zero=False)
    array_zero(filled)
    print(f"array_zero after clone -> {list(filled)!r}")
    assert list(filled) == [0, 0, 0]
    print("ok")

if __name__ == "__main__":
    main()
