"""Python usage for cypy cydatetime.

Run: python examples/pydatetime.py
"""
from datetime import timedelta

from cypy import (
    dt_date_check,
    dt_date_new,
    dt_date_year,
    dt_timedelta_check,
    dt_timedelta_days,
    dt_timedelta_new,
)

def main() -> None:
    d = dt_date_new(2026, 7, 21)
    assert dt_date_check(d)
    assert dt_date_year(d) == 2026

    td = dt_timedelta_new(1, 2, 3)
    assert dt_timedelta_check(td)
    assert dt_timedelta_days(td) == 1
    assert isinstance(td, timedelta)
    print("ok", d, td)

if __name__ == "__main__":
    main()
