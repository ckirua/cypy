"""Public :mod:`cypy.cytime` stubs.

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""
def time_monotonic() -> float:
    """Return monotonic seconds via ``PyTime_Monotonic``."""
    ...
def time_perf_counter() -> float:
    """Return perf-counter seconds via ``PyTime_PerfCounter``."""
    ...

