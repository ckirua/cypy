# cyiterator.pxd
# Iterator protocol helpers. Public docs in ``cyiterator.pyi``.

cdef extern from "Python.h":
    bint PyIter_Check(object o) noexcept
    object PyIter_Next(object o)


cpdef inline bint iter_check(object o) noexcept:
    return PyIter_Check(o)


cpdef inline object iter_next(object o):
    # Returns None at end without raising StopIteration (C-API convention).
    return PyIter_Next(o)
