# cypylifecycle.pxd
# Interpreter lifecycle. cimport-only; public REJECTED (process-wide).

cdef extern from "Python.h":
    void Py_Initialize() noexcept
    void Py_InitializeEx(int initsigs) noexcept
    int Py_IsInitialized() noexcept
    void Py_Finalize() noexcept
    int Py_FinalizeEx() noexcept
    wchar_t *Py_GetProgramName() noexcept
    void Py_SetProgramName(wchar_t *name) noexcept
    char *Py_GetVersion() noexcept
    char *Py_GetPlatform() noexcept
    char *Py_GetCopyright() noexcept
    char *Py_GetCompiler() noexcept
    char *Py_GetBuildInfo() noexcept


cdef inline void life_initialize() noexcept:
    Py_Initialize()


cdef inline void life_initialize_ex(int initsigs) noexcept:
    Py_InitializeEx(initsigs)


cdef inline bint life_is_initialized() noexcept:
    return Py_IsInitialized() != 0


cdef inline void life_finalize() noexcept:
    Py_Finalize()


cdef inline int life_finalize_ex() noexcept:
    return Py_FinalizeEx()


cdef inline bytes life_get_version():
    return Py_GetVersion()
