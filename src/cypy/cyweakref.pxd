# cyweakref.pxd
# Weakref helpers. Public docs in ``cyweakref.pyi``.
# GET_OBJECT macro: cdef.

from cpython.object cimport PyObject
from cpython.ref cimport Py_INCREF


cdef extern from "Python.h":
    bint PyWeakref_Check(object ob) noexcept
    bint PyWeakref_CheckRef(object ob) noexcept
    bint PyWeakref_CheckProxy(object ob) noexcept
    object PyWeakref_NewRef(object ob, object callback)
    object PyWeakref_NewProxy(object ob, object callback)
    PyObject *PyWeakref_GetObject(object ref) except? NULL
    PyObject *PyWeakref_GET_OBJECT(object ref) noexcept


cpdef inline bint weakref_check(object ob) noexcept:
    return PyWeakref_Check(ob)


cpdef inline bint weakref_check_ref(object ob) noexcept:
    return PyWeakref_CheckRef(ob)


cpdef inline bint weakref_check_proxy(object ob) noexcept:
    return PyWeakref_CheckProxy(ob)


cpdef inline object weakref_new_ref(object ob, object callback=None):
    return PyWeakref_NewRef(ob, callback)


cpdef inline object weakref_new_proxy(object ob, object callback=None):
    return PyWeakref_NewProxy(ob, callback)


cpdef inline object weakref_get_object(object ref):
    cdef PyObject *p = PyWeakref_GetObject(ref)
    if p is NULL:
        return None
    cdef object obj = <object>p
    Py_INCREF(obj)
    return obj


cdef inline object weakref_get_object_unchecked(object ref):
    cdef PyObject *p = PyWeakref_GET_OBJECT(ref)
    if p is NULL:
        return None
    cdef object obj = <object>p
    Py_INCREF(obj)
    return obj
