# cyslice

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.slice` |
| Sources | `src/cypy/cyslice.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Slice construction and index resolution without Python `slice.indices` attribute/method overhead.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| slcheck / slnew | public | |
| sleq / slice_eq | public | identity + richcompare; soft `sleq` |
| slindices_ex / slunpack | public | tuple-returning wrappers |
| slget_indices / slget_indices_ex / slunpack_c / sladjust_indices | cimport | out-params |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| slindices_ex (primary) | APPROVED | **0.29x** |
| slcheck / slnew / slunpack | APPROVED | **0.27–0.51x** |
| sleq / slice_eq | APPROVED | identity + richcompare (issue #30); on `buffers`, not `hot` |
| out-param cdef aliases | APPROVED (cimport) | for Cython callers |
| GetIndices (old) | APPROVED (cimport) | prefer Ex; keep alias |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 1 |
| Last pass | 2026-07-22 — `slice_eq` (#30) |
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| slindices_ex | **0.29x** vs `indices`+math | APPROVED | 1 |
| slnew | **0.48–0.51x** | APPROVED | 1 |
| sleq / slice_eq | identity + richcompare; Python `slice.__eq__` parity | APPROVED | 1 |

## Bench notes

- Harness: [`bench/cyslice_bench.py`](../../bench/cyslice_bench.py) · N=80000 · CPython 3.14.6

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| slcheck | slice / int | 0.50x / 0.39x | pass |
| slnew | 1:10:2 / :: | 0.48x / 0.51x | pass |
| slindices_ex | clipped shapes | 0.29x | pass |
| slunpack | 1:10:2 | 0.27x | pass |

Summary: 7/7 · mean **0.39x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cyslice.py`](../../bench/tier_b/cyslice.py) · `cyslice_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| slcheck | hit | 3.02±0.20ms | 3.28ms | 3.11±0.10ms | **0.97x** | 1.01x | cypy faster |

**Tier B takeaway:** primary `slcheck` **0.97x** vs typed Cython baseline (hit).


## Experiment conclusions

**Tier B:** `slcheck` **1.03x** vs isinstance — ~parity.

| Topic | Finding |
|-------|---------|
| Why `slindices_ex` wins | Single C call vs `slice.indices` + Python slicelen arithmetic |
| GetIndices vs Ex | Old API errors on OOB; Ex clips — public uses Ex |
| AdjustIndices | Pure C clip helper — cdef |
| Unpack | Maps None/large to ssize_t sentinels — not identical to attr access |
| Why win | `PySlice_GetIndicesEx` avoids Python attribute unpack of start/stop/step |
| Scale | Empty `::` and stepped `1:10:2` both ~0.28–0.29x vs pure Python indices |
| Safety | Length argument must match sequence length used later — wrong len → IndexError paths |
| Subtype | Check allows slice subtypes; Exact rejects them |
| `slice_eq` | Same semantics as `==` (identity then richcompare on start/stop/step); `None` bounds not normalized; on `cypy.buffers`, leave off `hot` |


## Done when

- [x] Try-all + depth + benches + `.pyi`
