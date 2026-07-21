# cyfloat.pxd
# ``float`` helpers. Public docs in ``cyfloat.pyi``.
# ``AS_DOUBLE`` unchecked: also exposed as cdef alias.

cdef extern from "Python.h":
    bint PyFloat_Check(object p) noexcept
    bint PyFloat_CheckExact(object p) noexcept
    object PyFloat_FromString(object str)
    object PyFloat_FromDouble(double v)
    double PyFloat_AsDouble(object pyfloat) except? -1
    double PyFloat_AS_DOUBLE(object pyfloat) noexcept


cpdef inline bint float_check(object p) noexcept:
    return PyFloat_Check(p)


cpdef inline bint float_check_exact(object p) noexcept:
    return PyFloat_CheckExact(p)


cpdef inline object float_from_double(double v):
    return PyFloat_FromDouble(v)


cdef inline object float_from_string(object s):
    return PyFloat_FromString(s)


cpdef inline double float_as_double(object pyfloat) except? -1:
    return PyFloat_AsDouble(pyfloat)


cdef inline double float_as_double_unchecked(object pyfloat) noexcept:
    # No type check — UB if not a float.
    return PyFloat_AS_DOUBLE(pyfloat)
# N2 preferred *_cstr (0.3: *_string cdef-only where soft)

cpdef inline object float_from_cstr(object s):
    return float_from_string(s)
