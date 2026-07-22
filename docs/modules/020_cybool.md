# cybool

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.bool` |
| Sources | `src/cypy/cybool.pxd`, `.pyx`, `.pyi` |
| Surface | public |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

`PyBool_Check` / `FromLong` for bool-typed hot paths; True/False singleton accessors.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| bool_check | public | `PyBool_Check` |
| bool_eq | public | identity + richcompare; soft `booleq` |
| bool_from_long | public | `PyBool_FromLong` |
| bool_true / bool_false | public | FromLong(1/0) cheap aliases |
| Py_True / Py_False macros | C-API | covered by true/false helpers |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| bool_check (primary) | APPROVED | **0.41–0.50x** |
| booleq / bool_eq | APPROVED | identity + richcompare (issue #26); not on `hot` |
| bool_true / bool_false | APPROVED | **0.63x** |
| bool_from_long | APPROVED (API) | **1.06–1.12x** vs `bool()` — keep for C `long` from Cython |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 1 |
| Last pass | 2026-07-22 — `bool_eq` (#26) |
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| bool_check | 0.41–0.50x | APPROVED | 1 |
| bool_from_long | 1.06–1.12x | APPROVED (API) | 1 |
| booleq / bool_eq | identity + richcompare; scalar completeness | APPROVED | 1 |

## Bench notes

- Harness: [`bench/cybool_bench.py`](../../bench/cybool_bench.py) · N=80000

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| bool_check | True / int | 0.50x / 0.41x | pass |
| bool_from_long | 1 / 0 | 1.12x / 1.06x | API keep |
| bool_true / false | | 0.63x | pass |

Summary: 4/6 gate · mean **0.72x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cybool.py`](../../bench/tier_b/cybool.py) · `cybool_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| bool_check | hit | 2.95±0.25ms | 3.32ms | 3.18±0.26ms | **0.93x** | 0.95x | cypy faster |

**Tier B takeaway:** primary `bool_check` **0.93x** vs typed Cython baseline (hit).


## Experiment conclusions

**Tier B:** `bool_check` **0.88x** vs isinstance.

| Topic | Finding |
|-------|---------|
| Check win | Avoids `isinstance` MRO for bool-vs-int |
| FromLong vs bool() | `bool(1)` is specialized bytecode; FromLong still useful from cdef `long` |
| Singletons | FromLong returns immortal True/False — no alloc |
| Why win | `bool_check` / `Py_True`/`Py_False` identity vs isinstance / constructing bools |
| Scale | FromLong loses slightly to cached `True`/`False` singletons (1.07–1.09x) — API keep |
| Safety | Always returns immortal True/False singletons — no new allocations on FromLong |
| ABI | Bool is long subclass; CheckExact false for int |
| `bool_eq` | Same semantics as `==` (identity then richcompare); True/False hit identity; leave off `hot` (clarity / completeness, not a measured hot-path win) |


## Done when

- [x] Try-all + depth + benches + `.pyi`
