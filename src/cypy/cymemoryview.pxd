# cymemoryview.pxd
# ``memoryview`` helpers. Public docs in ``cymemoryview.pyi``.
# FromMemory / FromBuffer / GET_* macros: cdef (pointers / lifetime).

from cpython.buffer cimport Py_buffer, PyBUF_READ, PyBUF_WRITE


cdef extern from "Python.h":
    memoryview PyMemoryView_FromObject(object obj)
    memoryview PyMemoryView_FromMemory(char *mem, Py_ssize_t size, int flags)
    memoryview PyMemoryView_FromBuffer(Py_buffer *view)
    memoryview PyMemoryView_GetContiguous(object obj, int buffertype, char order)
    bint PyMemoryView_Check(object obj) noexcept
    Py_buffer *PyMemoryView_GET_BUFFER(object mview) noexcept
    object PyMemoryView_GET_BASE(object mview) noexcept


cdef inline bint mvcheck(object p) noexcept:
    return PyMemoryView_Check(p)


cdef inline memoryview mvfrom_object(object obj):
    return PyMemoryView_FromObject(obj)


cdef inline memoryview mvget_contiguous(object obj, int buffertype=PyBUF_READ, str order="C"):
    # order must be a single char 'C' / 'F' / 'A'.
    cdef bytes ob = order.encode("ascii")
    cdef char *op = ob
    return PyMemoryView_GetContiguous(obj, buffertype, op[0])


cdef inline memoryview mvfrom_memory(char *mem, Py_ssize_t size, int flags=PyBUF_READ):
    # Caller owns ``mem`` for the lifetime of the view.
    return PyMemoryView_FromMemory(mem, size, flags)


cdef inline memoryview mvfrom_buffer(Py_buffer *view):
    return PyMemoryView_FromBuffer(view)


cdef inline Py_buffer *mvget_buffer(memoryview mview) noexcept:
    # Private exporter buffer; mview must be a memoryview.
    return PyMemoryView_GET_BUFFER(mview)


cdef inline object mvget_base(memoryview mview) noexcept:
    # Exporting object, or None if FromMemory/FromBuffer.
    return PyMemoryView_GET_BASE(mview)

# Wave 4 N1/N5 preferred names (0.3: soft letter/bare are cdef-only)

cpdef inline bint memoryview_check(object p) noexcept:
    return mvcheck(p)

cdef inline memoryview memoryview_from_buffer(Py_buffer *view):
    return mvfrom_buffer(view)

cdef inline memoryview memoryview_from_memory(char *mem, Py_ssize_t size, int flags=PyBUF_READ):
    return mvfrom_memory(mem, size, flags)

cpdef inline memoryview memoryview_from_object(object obj):
    return mvfrom_object(obj)

cdef inline object memoryview_get_base(memoryview mview) noexcept:
    return mvget_base(mview)

cpdef inline memoryview memoryview_get_contiguous(object obj, int buffertype=PyBUF_READ, str order="C"):
    return mvget_contiguous(obj, buffertype, order)

