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
| dt_timedelta_check* / days / seconds / microseconds | public | preferred spelling |
| dt_delta_* (check/days/seconds/microseconds) | cimport impl | 0.3: soft names cdef-only; prefer `dt_timedelta_*` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| checks / year / date_new / timedelta_new | APPROVED | **0.20–0.65x** |
| remaining getters/ctors | APPROVED (API) | completeness |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **Provisional (Runtime)** after 1.0 — not Core; may evolve under minors |
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B |
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| checks/getters/ctors | 0.20–0.65x | APPROVED | 1 |

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


## Done when

- [x] Try-all + depth + benches + `.pyi`
