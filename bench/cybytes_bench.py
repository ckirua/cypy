"""Compare public :mod:`cypy` cybytes helpers vs plain Python (tier A).

Includes scale cases for depth (small win / large hybrid).
Run: python bench/cybytes_bench.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_BENCH_ROOT = Path(__file__).resolve().parent
if str(_BENCH_ROOT) not in sys.path:
    sys.path.insert(0, str(_BENCH_ROOT))

from cypy import (
    bytes_check,
    bytes_check_exact,
    bytes_contains,
    bytes_from_object,
    bytes_len,
    bytes_size,
)

from _bench_util import BenchSession

HAYSTACK = b"abcabc"
NEEDLE_HIT = b"ab"
NEEDLE_MISS = b"zz"
NEEDLE_ONE = b"a"
HAY_1K = (b"a" * 1022) + b"xy"
HAY_8K = (b"a" * 8190) + b"xy"


def py_blen(b: bytes) -> int:
    return len(b)


def py_bcontains(haystack: bytes, needle: bytes) -> bool:
    return needle in haystack


def py_bcheck(p: object) -> bool:
    return isinstance(p, bytes)


def py_bcheck_exact(p: object) -> bool:
    return type(p) is bytes


def py_bfrom_object(o: object) -> bytes:
    return bytes(o)


def main() -> None:
    session = BenchSession("cybytes — public helpers vs plain Python (tier A)")
    session.header()

    session.section("bytes_contains vs `in`  [primary: small multi-byte hit]")
    session.compare(
        "bytes_contains",
        bytes_contains,
        py_bcontains,
        HAYSTACK,
        NEEDLE_HIT,
        param="small multi hit",
    )
    session.compare(
        "bytes_contains",
        bytes_contains,
        py_bcontains,
        HAYSTACK,
        NEEDLE_ONE,
        param="small 1-byte hit",
    )
    session.compare(
        "bytes_contains",
        bytes_contains,
        py_bcontains,
        HAYSTACK,
        NEEDLE_MISS,
        param="small miss",
    )
    session.compare(
        "bytes_contains",
        bytes_contains,
        py_bcontains,
        HAY_1K,
        b"xy",
        param="1KiB late hit",
    )
    session.compare(
        "bytes_contains",
        bytes_contains,
        py_bcontains,
        HAY_8K,
        b"zz",
        param="8KiB miss",
    )

    session.section("bytes_len / bytes_size vs len")
    session.compare("bytes_len", bytes_len, py_blen, HAYSTACK, param="bytes_len")
    session.compare("bytes_size", bytes_size, py_blen, HAYSTACK, param="bytes_size")

    session.section("bytes_check / bytes_check_exact")
    session.compare("bytes_check", bytes_check, py_bcheck, HAYSTACK, param="bytes")
    session.compare("bytes_check", bytes_check, py_bcheck, "str", param="str")
    session.compare(
        "bytes_check_exact",
        bytes_check_exact,
        py_bcheck_exact,
        HAYSTACK,
        param="bytes",
    )

    session.section("bytes_from_object vs bytes()")
    session.compare(
        "bytes_from_object",
        bytes_from_object,
        py_bfrom_object,
        memoryview(HAYSTACK),
        param="memoryview",
    )

    session.summary()


if __name__ == "__main__":
    main()
