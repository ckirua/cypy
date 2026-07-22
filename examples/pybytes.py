"""Python usage of :func:`cypy.bytes_len`, :func:`cypy.bytes_contains`, :func:`cypy.bytes_eq`, :func:`cypy.bytes_ne`.

Run: python examples/pybytes.py
"""

from cypy import bytes_contains, bytes_eq, bytes_len, bytes_ne
PAYLOAD: bytes = b"BTCUSDT"
HAYSTACK: bytes = b"abcabc"

BCONTAINS_CASES: tuple[tuple[bytes, bytes, bool], ...] = (
    (HAYSTACK, b"b", True),   # single-byte hit  (memchr)
    (HAYSTACK, b"z", False),  # single-byte miss
    (HAYSTACK, b"ab", True),  # multi-byte hit   (memmem)
    (HAYSTACK, b"xy", False), # multi-byte miss
    (HAYSTACK, b"", True),    # empty needle
    (b"", b"a", False),       # empty haystack
)

BEQ_CASES: tuple[tuple[bytes, bytes, bool], ...] = (
    (PAYLOAD, PAYLOAD, True),       # identity
    (PAYLOAD, b"BTCUSDT", True),    # equal content
    (PAYLOAD, b"ETHUSDT", False),   # same len, different
    (PAYLOAD, b"BTC", False),       # different len
    (b"", b"", True),               # empty
)

def main() -> None:
    print(f"bytes_len(payload) -> {bytes_len(PAYLOAD)!r}")
    assert bytes_len(PAYLOAD) == len(PAYLOAD)
    assert bytes_len(b"") == 0

    print()
    for haystack, needle, expected in BCONTAINS_CASES:
        result = bytes_contains(haystack, needle)
        py_result = needle in haystack
        status = "ok" if result == expected == py_result else "FAIL"
        print(
            f"{status:4}  {needle!r:>6} in {haystack!r:>10}  "
            f"-> {result!r}  (python {py_result!r})"
        )
        assert result == expected
        assert result == py_result

    print()
    for a, b, expected in BEQ_CASES:
        result = bytes_eq(a, b)
        py_result = a == b
        status = "ok" if result == expected == py_result else "FAIL"
        print(
            f"{status:4}  bytes_eq({a!r}, {b!r})  "
            f"-> {result!r}  (python {py_result!r})"
        )
        assert result == expected
        assert result == py_result
        assert bytes_ne(a, b) == (not expected) == (a != b)

    print()
    print("assertions passed")

if __name__ == "__main__":
    main()
