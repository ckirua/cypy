# cylongintrepr.pxd
# Internals of CPython ``int`` (digit layout). cimport-only — no public surface.
# Unsafe: ``_PyLong_New`` leaves digits uninitialized; fill before expose.

from cpython.longintrepr cimport (
    PyLong_BASE,
    PyLong_MASK,
    PyLong_SHIFT,
    _PyLong_New,
    digit,
    py_long,
    sdigit,
)


cdef inline py_long longrepr_new(Py_ssize_t size):
    # Size in digits; uninitialized ob_digit — fill before Python exposure.
    return _PyLong_New(size)


cdef inline digit *longrepr_digits(py_long o) noexcept:
    return o.ob_digit
