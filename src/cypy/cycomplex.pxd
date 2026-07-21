# cycomplex.pxd
# ``complex`` helpers. Public docs in ``cycomplex.pyi``.
# FromCComplex / AsCComplex: cdef (``Py_complex``).

cdef extern from "Python.h":
    ctypedef struct Py_complex:
        double real
        double imag

    bint PyComplex_Check(object p) noexcept
    bint PyComplex_CheckExact(object p) noexcept
    object PyComplex_FromCComplex(Py_complex v)
    object PyComplex_FromDoubles(double real, double imag)
    double PyComplex_RealAsDouble(object op) except? -1
    double PyComplex_ImagAsDouble(object op) except? -1
    Py_complex PyComplex_AsCComplex(object op) noexcept


cpdef inline bint complex_check(object p) noexcept:
    return PyComplex_Check(p)


cpdef inline bint complex_check_exact(object p) noexcept:
    return PyComplex_CheckExact(p)


cpdef inline object complex_from_doubles(double real, double imag):
    return PyComplex_FromDoubles(real, imag)


cpdef inline double complex_real_as_double(object op) except? -1:
    return PyComplex_RealAsDouble(op)


cpdef inline double complex_imag_as_double(object op) except? -1:
    return PyComplex_ImagAsDouble(op)


cdef inline object complex_from_ccomplex(Py_complex v):
    return PyComplex_FromCComplex(v)


cdef inline Py_complex complex_as_ccomplex(object op) noexcept:
    # On error returns (-1+0i); caller must check PyErr_Occurred.
    return PyComplex_AsCComplex(op)
