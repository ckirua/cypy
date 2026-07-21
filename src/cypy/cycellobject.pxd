# cycellobject.pxd
# Closure cell helpers. Public docs in ``cycellobject.pyi``.
# GET/SET macros: cdef unchecked.

from cpython.object cimport PyObject


cdef extern from "Python.h":
    bint PyCell_Check(object ob) noexcept
    object PyCell_New(object ob)
    object PyCell_Get(object cell)
    object PyCell_GET(object cell)
    int PyCell_Set(object cell, object value) except -1
    void PyCell_SET(object cell, object value) noexcept


cpdef inline bint cell_check(object ob) noexcept:
    return PyCell_Check(ob)


cpdef inline object cell_new(object ob):
    return PyCell_New(ob)


cpdef inline object cell_get(object cell):
    return PyCell_Get(cell)


cpdef inline int cell_set(object cell, object value) except -1:
    return PyCell_Set(cell, value)


cdef inline object cell_get_unchecked(object cell):
    # No type check — UB if not a cell.
    return PyCell_GET(cell)


cdef inline void cell_set_unchecked(object cell, object value) noexcept:
    # No refcount adjust / type check — UB if not a cell.
    PyCell_SET(cell, value)
