# cymemoryview

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.memoryview` |
| Sources | `src/cypy/cymemoryview.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Thin wrappers for memoryview construction / check / contiguous views used in buffer pipelines.

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| mvcheck | cypy | cpdef | public | `PyMemoryView_Check` |
| mveq | cypy | cpdef | public | contig `memcmp` / richcompare fallback; preferred `memoryview_eq` |
| mvfrom_object | cypy | cpdef | public | `PyMemoryView_FromObject` |
| mvget_contiguous | cypy | cpdef | public | `PyMemoryView_GetContiguous` |
| mvfrom_memory | cypy | cdef | cimport | caller-owned `char*` |
| mvfrom_buffer | cypy | cdef | cimport | `Py_buffer*` |
| mvget_buffer / mvget_base | cypy | cdef | cimport | macros; unchecked type |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| mvcheck | APPROVED | primary **0.49x** |
| mveq / memoryview_eq | APPROVED | contig memcmp + richcompare fallback |
| mvfrom_object | APPROVED | **0.74–0.76x** |
| mvget_contiguous | APPROVED | **0.62–0.63x** |
| mvfrom_memory / buffer / get_* | APPROVED (cimport) | pointers / lifetime |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| mvcheck | Beat isinstance | harness | **0.41–0.49x** | APPROVED | 1 |
| mvfrom_object | Beat memoryview() | ba/bytes | **0.74–0.76x** | APPROVED | 1 |
| mvget_contiguous | Beat Python path | C order | **0.62–0.63x** | APPROVED | 1 |
| FromMemory/FromBuffer/GET_* | Pointer APIs | ABI present | cdef | APPROVED (cimport) | 1 |

## Bench notes

- Harness: [`bench/cymemoryview_bench.py`](../../bench/cymemoryview_bench.py) · N=80000 RUNS=5 · CPython 3.14.6

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| mvcheck | memoryview | 0.88±0.02ms | 0.90ms | 0.49x | 0.48x | pass |
| mvcheck | bytearray | 0.88±0.02ms | 0.90ms | 0.41x | 0.41x | pass |
| mvfrom_object | bytearray | 3.36±0.08ms | 3.45ms | 0.76x | 0.76x | pass |
| mvfrom_object | bytes | 3.23±0.11ms | 3.40ms | 0.74x | 0.77x | pass |
| mvget_contiguous | bytearray C | 3.45±0.13ms | 3.63ms | 0.62x | 0.64x | pass |
| mvget_contiguous | bytes C | 3.41±0.08ms | 3.51ms | 0.63x | 0.63x | pass |

Summary: 6/6 faster · mean **0.61x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cymemoryview.py`](../../bench/tier_b/cymemoryview.py) · `cymemoryview_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| mvcheck | hit | 2.93±0.10ms | 3.02ms | 3.07±0.15ms | **0.95x** | 0.93x | cypy faster |

**Tier B takeaway:** primary `mvcheck` **0.95x** vs typed Cython baseline (hit).


## Experiment conclusions

**Tier B:** `mvcheck` **0.97x** vs isinstance — ~parity.

| Topic | Finding |
|-------|---------|
| Why win | Avoid Python `memoryview` type lookup / constructor overhead |
| `mvfrom_memory` | Caller must keep `mem` alive for view lifetime — cdef |
| `GET_BUFFER` / `GET_BASE` | Unchecked macros — crash if not memoryview |
| Contiguous | Already-contiguous exporters return a view of original memory (no copy) |
| Why win | Type-slot / C buffer path vs Python memoryview constructor overhead |
| Scale | Contiguous bytearray vs bytes shapes both ~0.63x; non-contiguous left to CPython |
| Safety | `mvget_*` borrows buffer — must not outlive the memoryview; release rules apply |
| ABI | Check/FromMemory macros vs exported FromObject/GetContiguous — all probed |


## Done when

- [x] Inventory + try-all + depth + benches + `.pyi`
