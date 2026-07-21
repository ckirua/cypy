"""Public :mod:`cypy.cydatetime` stubs."""

def dt_date_check(o: object) -> bool:
    """Return True if ``o`` is a ``date`` or subtype (``PyDate_Check``)."""
    ...

def dt_date_check_exact(o: object) -> bool:
    """Return True if ``type(o) is date`` (``PyDate_CheckExact``)."""
    ...

def dt_datetime_check(o: object) -> bool:
    """Return True if ``o`` is a ``datetime`` or subtype (``PyDateTime_Check``)."""
    ...

def dt_datetime_check_exact(o: object) -> bool:
    """Return True if ``type(o) is datetime`` (``PyDateTime_CheckExact``)."""
    ...

def dt_time_check(o: object) -> bool:
    """Return True if ``o`` is a ``time`` or subtype (``PyTime_Check``)."""
    ...

def dt_time_check_exact(o: object) -> bool:
    """Return True if ``type(o) is time`` (``PyTime_CheckExact``)."""
    ...

def dt_date_new(year: int, month: int, day: int) -> object:
    """Return a ``date`` via DateTime C-API (unchecked ranges)."""
    ...

def dt_time_new(hour: int, minute: int, second: int, microsecond: int, tz: object = None, fold: int = 0) -> object:
    """Return a ``time`` via DateTime C-API (unchecked ranges)."""
    ...

def dt_datetime_new(year: int, month: int, day: int, hour: int, minute: int, second: int, microsecond: int, tz: object = None, fold: int = 0) -> object:
    """Return a ``datetime`` via DateTime C-API (unchecked ranges)."""
    ...

def dt_timedelta_new(days: int, seconds: int, useconds: int) -> object:
    """Return a ``timedelta`` via DateTime C-API."""
    ...

def dt_date_year(o: object) -> int:
    """Datetime field/helper ``dt_date_year``."""
    ...

def dt_date_month(o: object) -> int:
    """Datetime field/helper ``dt_date_month``."""
    ...

def dt_date_day(o: object) -> int:
    """Datetime field/helper ``dt_date_day``."""
    ...

def dt_datetime_year(o: object) -> int:
    """Datetime field/helper ``dt_datetime_year``."""
    ...

def dt_datetime_month(o: object) -> int:
    """Datetime field/helper ``dt_datetime_month``."""
    ...

def dt_datetime_day(o: object) -> int:
    """Datetime field/helper ``dt_datetime_day``."""
    ...

def dt_datetime_hour(o: object) -> int:
    """Datetime field/helper ``dt_datetime_hour``."""
    ...

def dt_datetime_minute(o: object) -> int:
    """Datetime field/helper ``dt_datetime_minute``."""
    ...

def dt_datetime_second(o: object) -> int:
    """Datetime field/helper ``dt_datetime_second``."""
    ...

def dt_datetime_microsecond(o: object) -> int:
    """Datetime field/helper ``dt_datetime_microsecond``."""
    ...

def dt_time_hour(o: object) -> int:
    """Datetime field/helper ``dt_time_hour``."""
    ...

def dt_time_minute(o: object) -> int:
    """Datetime field/helper ``dt_time_minute``."""
    ...

def dt_time_second(o: object) -> int:
    """Datetime field/helper ``dt_time_second``."""
    ...

def dt_time_microsecond(o: object) -> int:
    """Datetime field/helper ``dt_time_microsecond``."""
    ...

# N6: prefer dt_timedelta_*; dt_delta_* kept
def dt_timedelta_check(o: object) -> bool:
    """Alias of ``dt_delta_check`` (preferred ``timedelta`` spelling)."""
    ...

def dt_timedelta_check_exact(o: object) -> bool:
    """Alias of ``dt_delta_check_exact`` (preferred ``timedelta`` spelling)."""
    ...

def dt_timedelta_days(o: object) -> int:
    """Alias of ``dt_delta_days`` (preferred ``timedelta`` spelling)."""
    ...

def dt_timedelta_seconds(o: object) -> int:
    """Alias of ``dt_delta_seconds`` (preferred ``timedelta`` spelling)."""
    ...

def dt_timedelta_microseconds(o: object) -> int:
    """Alias of ``dt_delta_microseconds`` (preferred ``timedelta`` spelling)."""
    ...
