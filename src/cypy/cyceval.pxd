# cyceval.pxd
# Eval / GIL init helpers. cimport-only (process-wide).

cdef extern from "Python.h":
    void PyEval_InitThreads() noexcept
    int PyEval_ThreadsInitialized() noexcept


cdef inline void eval_init_threads() noexcept:
    # No-op on modern CPython once runtime started; kept for Completeness.
    PyEval_InitThreads()


cdef inline bint eval_threads_initialized() noexcept:
    return PyEval_ThreadsInitialized() != 0
