# cydatetime.pxd
# datetime.h helpers. Public docs in ``cydatetime.pyi``.
# Call ``import_datetime()`` once (done in ``cydatetime.pyx``) before use.

from cpython.datetime cimport (
    PyDate_Check,
    PyDate_CheckExact,
    PyDateTime_Check,
    PyDateTime_CheckExact,
    PyDelta_Check,
    PyDelta_CheckExact,
    PyTime_Check,
    PyTime_CheckExact,
    date_day,
    date_month,
    date_new,
    date_year,
    datetime_day,
    datetime_hour,
    datetime_microsecond,
    datetime_minute,
    datetime_month,
    datetime_new,
    datetime_second,
    datetime_year,
    import_datetime,
    time_hour,
    time_microsecond,
    time_minute,
    time_new,
    time_second,
    timedelta_days,
    timedelta_microseconds,
    timedelta_new,
    timedelta_seconds,
)


cpdef inline bint dt_date_check(object o) noexcept:
    return PyDate_Check(o)


cpdef inline bint dt_date_check_exact(object o) noexcept:
    return PyDate_CheckExact(o)


cpdef inline bint dt_datetime_check(object o) noexcept:
    return PyDateTime_Check(o)


cpdef inline bint dt_datetime_check_exact(object o) noexcept:
    return PyDateTime_CheckExact(o)


cpdef inline bint dt_time_check(object o) noexcept:
    return PyTime_Check(o)


cpdef inline bint dt_time_check_exact(object o) noexcept:
    return PyTime_CheckExact(o)


cdef inline bint dt_delta_check(object o) noexcept:
    return PyDelta_Check(o)


cdef inline bint dt_delta_check_exact(object o) noexcept:
    return PyDelta_CheckExact(o)


cpdef inline object dt_date_new(int year, int month, int day):
    return date_new(year, month, day)


cpdef inline object dt_time_new(int hour, int minute, int second, int microsecond, object tz=None, int fold=0):
    return time_new(hour, minute, second, microsecond, tz, fold)


cpdef inline object dt_datetime_new(
    int year, int month, int day, int hour, int minute, int second, int microsecond, object tz=None, int fold=0
):
    return datetime_new(year, month, day, hour, minute, second, microsecond, tz, fold)


cpdef inline object dt_timedelta_new(int days, int seconds, int useconds):
    return timedelta_new(days, seconds, useconds)


cpdef inline int dt_date_year(object o) noexcept:
    return date_year(o)


cpdef inline int dt_date_month(object o) noexcept:
    return date_month(o)


cpdef inline int dt_date_day(object o) noexcept:
    return date_day(o)


cpdef inline int dt_datetime_year(object o) noexcept:
    return datetime_year(o)


cpdef inline int dt_datetime_month(object o) noexcept:
    return datetime_month(o)


cpdef inline int dt_datetime_day(object o) noexcept:
    return datetime_day(o)


cpdef inline int dt_datetime_hour(object o) noexcept:
    return datetime_hour(o)


cpdef inline int dt_datetime_minute(object o) noexcept:
    return datetime_minute(o)


cpdef inline int dt_datetime_second(object o) noexcept:
    return datetime_second(o)


cpdef inline int dt_datetime_microsecond(object o) noexcept:
    return datetime_microsecond(o)


cpdef inline int dt_time_hour(object o) noexcept:
    return time_hour(o)


cpdef inline int dt_time_minute(object o) noexcept:
    return time_minute(o)


cpdef inline int dt_time_second(object o) noexcept:
    return time_second(o)


cpdef inline int dt_time_microsecond(object o) noexcept:
    return time_microsecond(o)


cdef inline int dt_delta_days(object o) noexcept:
    return timedelta_days(o)


cdef inline int dt_delta_seconds(object o) noexcept:
    return timedelta_seconds(o)


cdef inline int dt_delta_microseconds(object o) noexcept:
    return timedelta_microseconds(o)

# N6 spelling: preferred dt_timedelta_* (0.3: dt_delta_* cdef-only)
cpdef inline bint dt_timedelta_check(object o) noexcept:
    return dt_delta_check(o)

cpdef inline bint dt_timedelta_check_exact(object o) noexcept:
    return dt_delta_check_exact(o)

cpdef inline int dt_timedelta_days(object o) noexcept:
    return dt_delta_days(o)

cpdef inline int dt_timedelta_seconds(object o) noexcept:
    return dt_delta_seconds(o)

cpdef inline int dt_timedelta_microseconds(object o) noexcept:
    return dt_delta_microseconds(o)

