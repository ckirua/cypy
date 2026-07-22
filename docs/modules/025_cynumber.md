# cynumber

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.number` |
| Sources | `src/cypy/cynumber.pxd`, `.pyx`, `.pyi` |
| Surface | public |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Abstract number protocol for unknown concrete types. Prefer typed modules (`cylong`/`cyfloat`) when known — binary ops lose to `operator.*` from Python.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| num_check / num_index_check | public | |
| num_eq | public | RichCompare; soft `neq_num`; prefer typed `*_eq` |
| binary / unary / inplace / convert | public | full protocol minus ABI-missing |
| PyNumber_Divide / InPlaceDivide / Coerce | — | REJECTED (ABI missing 3.14) |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| num_check / index_check | APPROVED | **0.30–0.45x** |
| num_inplace_add | APPROVED | **0.78x** |
| num_eq / neq_num | APPROVED | RichCompare (issue #29); not on `hot` |
| binary / unary / convert | APPROVED (API) | **1.07–1.34x** — protocol completeness |
| Divide / InPlaceDivide / Coerce | REJECTED | missing from libpython3.14 |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **Provisional (Protocols)** after 1.0 — not Core; may evolve under minors |
| Iteration | 1 |
| Last pass | 2026-07-22 — `num_eq` (#29) |
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| checks | 0.30–0.45x | APPROVED | 1 |
| ops | 1.07–1.34x | APPROVED (API) | 1 |
| inplace_add | 0.78x | APPROVED | 1 |
| Divide/Coerce | ctypes missing | REJECTED | 1 |
| neq_num / num_eq | RichCompare; NaN parity; protocol bridge | APPROVED | 1 |

## Bench notes

- Harness: [`bench/cynumber_bench.py`](../../bench/cynumber_bench.py) · N=80000

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| num_check | int / str | 0.30x / 0.33x | pass |
| num_index_check | int / float | 0.31x / 0.45x | pass |
| num_add / mul / … | ints | 1.07–1.17x | API |
| num_inplace_add | 10+=3 | 0.78x | pass |
| num_as_ssize | 99 | 1.34x | API |

Summary: 5/17 gate · mean **0.94x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cynumber.py`](../../bench/tier_b/cynumber.py) · `cynumber_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| num_check | hit | 3.22±0.16ms | 3.36ms | 2.60±0.13ms | **1.24x** | 1.21x | baseline faster |

**Tier B takeaway:** primary `num_check` **1.24x** vs typed Cython baseline (hit).


## Experiment conclusions

**Tier B:** `num_check` **1.29x** vs isinstance tuple — Cython emit tighter for multi-type check.

| Topic | Finding |
|-------|---------|
| Check win | Slot probe vs hasattr/`__index__` |
| Why ops lose | `operator.add` etc. specialize; `PyNumber_*` is abstract nb_* dispatch |
| Prefer typed | Use `long_*` / `float_*` when type known |
| InPlace | Wins when avoiding Python `+=` bytecode for immutable ints (returns new) |
| ABI | `PyNumber_Divide` / `InPlaceDivide` / `Coerce` removed — ctypes AttributeError |
| Cheap aliases | All InPlace* siblings wrapped |
| `num_eq` | Abstract `==` via `PyObject_RichCompare` (not `RichCompareBool` — identity-shortcuts same-object NaN → True). Prefer `long_eq`/`float_eq`/`complex_eq`/`bool_eq` when typed. Soft `neq_num`. Leave off `hot` (protocol bridge / clarity). Errors from `__eq__` propagate; `NotImplemented` on both sides → False for EQ (CPython `do_richcompare`) |

## Done when

- [x] Try-all + depth + benches + `.pyi`
