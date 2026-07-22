# cydatetime

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.datetime` |
| Sources | `src/cypy/cydatetime.pxd`, `.pyx`, `.pyi` |
| Surface | public |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

`datetime.h` checks/constructors/getters via Cython Includes + `PyDateTime_IMPORT` on load.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| dt_*_check* / *_new / field getters | public | wraps cpython.datetime helpers |
| dteq_date / dt_date_eq | public | identity + exact y/m/d / richcompare; soft `dteq_date` |
| dteq_time / dt_time_eq | public | identity + exact naive h/m/s/us / richcompare; soft `dteq_time` |
| dteq_dt / dt_datetime_eq | public | identity + exact naive y/m/d/h/m/s/us / richcompare; soft `dteq_dt` |
| dteq_delta / dt_timedelta_eq | public | identity + exact days/s/us / richcompare; soft `dteq_delta` |
| dt_timedelta_check* / days / seconds / microseconds | public | preferred spelling |
| dt_delta_* (check/days/seconds/microseconds) | cimport impl | 0.3: soft names cdef-only; prefer `dt_timedelta_*` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| checks / year / date_new / timedelta_new | APPROVED | **0.20–0.65x** |
| dteq_date / dt_date_eq | APPROVED | identity + exact field compare / richcompare (issue #31); not `hot` |
| dteq_time / dt_time_eq | APPROVED | identity + exact naive field compare / richcompare (issue #32); not `hot` |
| dteq_dt / dt_datetime_eq | APPROVED | identity + exact naive field compare / richcompare (issue #33); not `hot` |
| dteq_delta / dt_timedelta_eq | APPROVED | identity + exact field compare / richcompare (issue #34); not `hot` |
| remaining getters/ctors | APPROVED (API) | completeness |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **Provisional (Runtime)** after 1.0 — not Core; may evolve under minors |
| Iteration | 1 |
P26-07-22 — `*_eq` inventory Tier A (`cyeq_inventory_bench`)|
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| checks/getters/ctors | 0.20–0.65x | APPROVED | 1 |
| dteq_date / dt_date_eq | identity + exact y/m/d; richcompare for subtypes / date↔datetime | APPROVED | 1 |
| dteq_time / dt_time_eq | identity + exact naive h/m/s/us; richcompare for subtypes / aware | APPROVED | 1 |
| dteq_dt / dt_datetime_eq | identity + exact naive y/m/d/h/m/s/us; richcompare for subtypes / aware | APPROVED | 1 |
| dteq_delta / dt_timedelta_eq | identity + exact days/s/us; richcompare for subtypes | APPROVED | 1 |

## Bench notes

- Harness: [`bench/cydatetime_bench.py`](../../bench/cydatetime_bench.py)

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| dt_date_check | date / int | 0.52x / 0.43x | pass |
| dt_datetime_check | | 0.51x | pass |
| dt_date_year | | 0.58x | pass |
| dt_date_new | | 0.65x | pass |
| dt_delta_check | | 0.52x | pass |
| dt_timedelta_new | | 0.20x | pass |

Summary: 7/7 gate · mean **0.49x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cydatetime.py`](../../bench/tier_b/cydatetime.py) · `cydatetime_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| dt_date_check | date | 2.56±0.02ms | 2.58ms | 2.52±0.01ms | **1.01x** | 1.01x | ~tie |

**Tier B takeaway:** primary `dt_date_check` **1.01x** vs typed Cython baseline (date).



### `*_eq` inventory (Tier A depth)

Harness: [`bench/cyeq_inventory_bench.py`](../../bench/cyeq_inventory_bench.py) · N=80_000 × runs=11 · CPython 3.14

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| dt_date_eq | eq | 1.04±0.06ms | 1.17ms | **0.60x** | 0.64x | APPROVED |
| dt_date_eq | ne | 1.01±0.02ms | 1.05ms | **0.57x** | 0.53x | APPROVED |
| dt_time_eq | eq | 1.08±0.04ms | 1.13ms | **0.62x** | 0.62x | APPROVED |
| dt_datetime_eq | eq | 1.14±0.04ms | 1.22ms | **0.65x** | 0.67x | APPROVED |
| dt_timedelta_eq | eq | 1.02±0.03ms | 1.09ms | **0.61x** | 0.62x | APPROVED |
## Experiment conclusions

**Tier B:** `dt_date_check` **1.01x** vs isinstance(date) — ~parity.

| Topic | Finding |
|-------|---------|
| IMPORT | `import_datetime()` in `.pyx` required before macros |
| Why win | Direct C-API vs isinstance / attr / Python ctor |
| timedelta_new | Avoids Python timedelta argument parsing |
| Unchecked ranges | C-API ctors skip range checks — documented |
| Why win | Capsule/type checks + C getters avoid Python attribute descriptors |
| Scale | DateFromDate / Delta constructors win; timezone edges left to datetime module |
| Safety | Must call `PyDateTime_IMPORT` once before macros — wrappers ensure import |
| ABI | datetime C-API via capsule; missing import → segfault risk if bypassed |
| `dt_date_eq` | Exact `date` pairs: C y/m/d compare; subtypes / date↔datetime via richcompare (Python `==`; date≠datetime); leave off `hot` until measured win |
| `dt_time_eq` | Exact naive `time` pairs: C h/m/s/us (fold ignored); aware/subtypes via richcompare (Python `==` offset rules); leave off `hot` until measured win |
| `dt_datetime_eq` | Exact naive `datetime` pairs: C y/m/d/h/m/s/us (fold ignored); aware/subtypes / date↔datetime via richcompare (Python `==`); leave off `hot` until measured win |
| `dt_timedelta_eq` | Exact `timedelta` pairs: C days/seconds/microseconds; subtypes via richcompare (Python `==`); leave off `hot` until measured win |


## Done when

- [x] Try-all + depth + benches + `.pyi`
