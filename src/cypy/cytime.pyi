"""Public :mod:`cypy.cytime` stubs."""
def time_monotonic() -> float:
    """Return monotonic seconds via ``PyTime_Monotonic``."""
    ...
def time_perf_counter() -> float:
    """Return perf-counter seconds via ``PyTime_PerfCounter``."""
    ...

def time_wall() -> float:
    """Alias of ``time_time`` (wall clock; preferred non-stutter name)."""
    ...
