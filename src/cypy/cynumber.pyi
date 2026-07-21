"""Public :mod:`cypy.cynumber` stubs (signatures + docstrings for IDE / typecheckers)."""

def num_check(o: object) -> bool:
    """Return True if ``o`` provides the number protocol (``PyNumber_Check``)."""
    ...

def num_index_check(o: object) -> bool:
    """Return True if ``o`` is an index integer (``PyIndex_Check``)."""
    ...

def num_add(o1: object, o2: object) -> object:
    """Return ``o1 + o2`` via ``PyNumber_Add``."""
    ...

def num_sub(o1: object, o2: object) -> object:
    """Return ``o1 - o2`` via ``PyNumber_Subtract``."""
    ...

def num_mul(o1: object, o2: object) -> object:
    """Return ``o1 * o2`` via ``PyNumber_Multiply``."""
    ...

def num_matmul(o1: object, o2: object) -> object:
    """Return ``o1 @ o2`` via ``PyNumber_MatrixMultiply``."""
    ...

def num_floordiv(o1: object, o2: object) -> object:
    """Return ``o1 // o2`` via ``PyNumber_FloorDivide``."""
    ...

def num_truediv(o1: object, o2: object) -> object:
    """Return ``o1 / o2`` via ``PyNumber_TrueDivide``."""
    ...

def num_mod(o1: object, o2: object) -> object:
    """Return ``o1 % o2`` via ``PyNumber_Remainder``."""
    ...

def num_divmod(o1: object, o2: object) -> object:
    """Return ``divmod(o1, o2)`` via ``PyNumber_Divmod``."""
    ...

def num_pow(o1: object, o2: object, o3: object = None) -> object:
    """Return ``pow(o1, o2, o3)`` via ``PyNumber_Power`` (pass ``None`` for binary pow)."""
    ...

def num_neg(o: object) -> object:
    """Return ``-o`` via ``PyNumber_Negative``."""
    ...

def num_pos(o: object) -> object:
    """Return ``+o`` via ``PyNumber_Positive``."""
    ...

def num_abs(o: object) -> object:
    """Return ``abs(o)`` via ``PyNumber_Absolute``."""
    ...

def num_invert(o: object) -> object:
    """Return ``~o`` via ``PyNumber_Invert``."""
    ...

def num_lshift(o1: object, o2: object) -> object:
    """Return ``o1 << o2`` via ``PyNumber_Lshift``."""
    ...

def num_rshift(o1: object, o2: object) -> object:
    """Return ``o1 >> o2`` via ``PyNumber_Rshift``."""
    ...

def num_and(o1: object, o2: object) -> object:
    """Return ``o1 & o2`` via ``PyNumber_And``."""
    ...

def num_xor(o1: object, o2: object) -> object:
    """Return ``o1 ^ o2`` via ``PyNumber_Xor``."""
    ...

def num_or(o1: object, o2: object) -> object:
    """Return ``o1 | o2`` via ``PyNumber_Or``."""
    ...

def num_inplace_add(o1: object, o2: object) -> object:
    """Return in-place ``o1 += o2`` result via ``PyNumber_InPlaceAdd``."""
    ...

def num_inplace_sub(o1: object, o2: object) -> object:
    """Return in-place ``o1 -= o2`` result via ``PyNumber_InPlaceSubtract``."""
    ...

def num_inplace_mul(o1: object, o2: object) -> object:
    """Return in-place ``o1 *= o2`` result via ``PyNumber_InPlaceMultiply``."""
    ...

def num_inplace_matmul(o1: object, o2: object) -> object:
    """Return in-place ``o1 @= o2`` result via ``PyNumber_InPlaceMatrixMultiply``."""
    ...

def num_inplace_floordiv(o1: object, o2: object) -> object:
    """Return in-place ``o1 //= o2`` result via ``PyNumber_InPlaceFloorDivide``."""
    ...

def num_inplace_truediv(o1: object, o2: object) -> object:
    """Return in-place ``o1 /= o2`` result via ``PyNumber_InPlaceTrueDivide``."""
    ...

def num_inplace_mod(o1: object, o2: object) -> object:
    """Return in-place ``o1 %= o2`` result via ``PyNumber_InPlaceRemainder``."""
    ...

def num_inplace_pow(o1: object, o2: object, o3: object = None) -> object:
    """Return in-place power via ``PyNumber_InPlacePower``."""
    ...

def num_inplace_lshift(o1: object, o2: object) -> object:
    """Return in-place ``o1 <<= o2`` result via ``PyNumber_InPlaceLshift``."""
    ...

def num_inplace_rshift(o1: object, o2: object) -> object:
    """Return in-place ``o1 >>= o2`` result via ``PyNumber_InPlaceRshift``."""
    ...

def num_inplace_and(o1: object, o2: object) -> object:
    """Return in-place ``o1 &= o2`` result via ``PyNumber_InPlaceAnd``."""
    ...

def num_inplace_xor(o1: object, o2: object) -> object:
    """Return in-place ``o1 ^= o2`` result via ``PyNumber_InPlaceXor``."""
    ...

def num_inplace_or(o1: object, o2: object) -> object:
    """Return in-place ``o1 |= o2`` result via ``PyNumber_InPlaceOr``."""
    ...

def num_long(o: object) -> object:
    """Return ``int(o)`` via ``PyNumber_Long``."""
    ...

def num_float(o: object) -> object:
    """Return ``float(o)`` via ``PyNumber_Float``."""
    ...

def num_index(o: object) -> object:
    """Return ``operator.index(o)`` via ``PyNumber_Index``."""
    ...

def num_as_ssize(o: object, exc: object = None) -> int:
    """Return ``o`` as ``Py_ssize_t``; ``exc`` is raised on overflow (or clip if ``None``)."""
    ...
