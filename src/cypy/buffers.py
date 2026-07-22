"""Category facade: bytes / bytearray / array / memoryview / buffer / slice.

Typed buffer-adjacent Core helpers. Prefer ``bytes_len`` / ``bytes_contains`` /
``bytes_eq`` from ``cypy.hot`` for the common bytes hot path.
"""

from __future__ import annotations

from .cyarray import array_check, array_check_exact, array_clone, array_len, array_zero
from .cybuffer import buf_check
from .cybytearray import (
    bytearray_check,
    bytearray_check_exact,
    bytearray_len,
    bytearray_size,
)
from .cybytes import (
    bytes_check,
    bytes_check_exact,
    bytes_contains,
    bytes_eq,
    bytes_len,
    bytes_size,
)
from .cymemoryview import memoryview_check, memoryview_from_object
from .cyslice import slice_check, slice_new

__all__: tuple[str, ...] = (
    "bytes_check",
    "bytes_check_exact",
    "bytes_len",
    "bytes_size",
    "bytes_contains",
    "bytes_eq",
    "bytearray_check",
    "bytearray_check_exact",
    "bytearray_len",
    "bytearray_size",
    "array_check",
    "array_check_exact",
    "array_len",
    "array_clone",
    "array_zero",
    "memoryview_check",
    "memoryview_from_object",
    "buf_check",
    "slice_check",
    "slice_new",
)
