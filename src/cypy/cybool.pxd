# cybool.pxd
# Boolean helpers. Public docs in ``cybool.pyi``.

cdef extern from "Python.h":
    bint PyBool_Check(object o) noexcept
    object PyBool_FromLong(long v)


cpdef inline bint bool_check(object o) noexcept:
    return PyBool_Check(o)


cpdef inline object bool_from_long(long v):
    return PyBool_FromLong(v)


cpdef inline object bool_true():
    return PyBool_FromLong(1)


cpdef inline object bool_false():
    return PyBool_FromLong(0)
