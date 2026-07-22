# cytype.pxd
# Type-object helpers. Public docs in ``cytype.pyi``.
# GenericAlloc/New/Ready/Modified/HasFeature/IS_GC: cdef (type-mutation / flags).

cdef extern from "Python.h":
    bint PyType_Check(object o) noexcept
    bint PyType_CheckExact(object o) noexcept
    void PyType_Modified(object type) noexcept
    bint PyType_HasFeature(object o, int feature) noexcept
    bint PyType_IS_GC(object o) noexcept
    bint PyType_IsSubtype(object a, object b) noexcept
    object PyType_GenericAlloc(object type, Py_ssize_t nitems)
    object PyType_GenericNew(object type, object args, object kwds)
    int PyType_Ready(object type) except -1


cpdef inline bint type_check(object o) noexcept:
    return PyType_Check(o)


cpdef inline bint type_check_exact(object o) noexcept:
    return PyType_CheckExact(o)


cpdef inline bint type_is_subtype(object a, object b) noexcept:
    return PyType_IsSubtype(a, b)


cdef inline bint typeeq(object a, object b) noexcept:
    # Type-object equality is identity (CPython ``type_richcompare`` default).
    # Not Python ``==`` when a metaclass overrides ``__eq__``. Soft ``typeeq``.
    # Callers should pass type objects. Not on ``hot`` — validate win first.
    return a is b


cpdef inline bint type_eq(object a, object b) noexcept:
    return typeeq(a, b)


cdef inline void type_modified(object typ) noexcept:
    # Invalidate type lookup cache after manual type mutation.
    PyType_Modified(typ)


cdef inline bint type_has_feature(object o, int feature) noexcept:
    return PyType_HasFeature(o, feature)


cdef inline bint type_is_gc(object o) noexcept:
    return PyType_IS_GC(o)


cdef inline object type_generic_alloc(object typ, Py_ssize_t nitems):
    return PyType_GenericAlloc(typ, nitems)


cdef inline object type_generic_new(object typ, object args, object kwds):
    return PyType_GenericNew(typ, args, kwds)


cdef inline int type_ready(object typ) except -1:
    return PyType_Ready(typ)
