# cybytearray

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.bytearray` (`Cython/Includes/cpython/bytearray.pxd`) |
| Sources | `src/cypy/cybytearray.pxd`, `cybytearray.pyx`, `cybytearray.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Hot-path len/check/from_object/concat/resize for typed exact `bytearray`, plus full include try-all. Depth covered uninit `banew`, borrowed `AS_STRING`, and resize vs Python extend/del.

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| bacheck | cypy | cpdef | public | `PyByteArray_Check` |
| bacheck_exact | cypy | cpdef | public | `PyByteArray_CheckExact` |
| balen | cypy | cpdef | public | `PyByteArray_GET_SIZE` |
| basize | cypy | cpdef | public | `PyByteArray_Size` |
| bafrom_object | cypy | cpdef | public | `PyByteArray_FromObject` |
| baconcat | cypy | cpdef | public | `PyByteArray_Concat` |
| baresize | cypy | cpdef | public | `PyByteArray_Resize` |
| baas_string | cypy | cdef | cimport | `PyByteArray_AS_STRING` |
| baas_string_checked | cypy | cdef | cimport | `PyByteArray_AsString` |
| baeq | cypy | cpdef | public | identity/len/`memcmp` (soft); preferred `bytearray_eq` |
| bane | cypy | cpdef | public | `not baeq` (soft); preferred `bytearray_ne` |
| bacontains | cypy | cpdef | public | memchr/memmem (soft); preferred `bytearray_contains` |
| bafrom_string_and_size | cypy | cdef | cimport | `PyByteArray_FromStringAndSize` |
| banew | cypy | cdef | cimport | uninit — `FromStringAndSize(NULL, n)` |
| PyByteArray_* | C-API | used-by | — | all 10 include symbols mapped |
| ConcatAndDel sibling | C-API | tried | — | **absent** from include / ABI |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| balen / basize | APPROVED | primary **0.60x** / **0.62x** |
| bacheck / exact | APPROVED | **0.49x** / **0.54x** |
| bafrom_object | APPROVED | **0.76–0.81x** |
| baconcat | APPROVED | **0.77–0.79x** |
| baresize | APPROVED | **0.61–0.71x** vs extend/del |
| baeq / bytearray_eq | APPROVED | mirrors `bytes_eq` / `str_eq` |
| bane / bytearray_ne | APPROVED | `not baeq` — API sibling of `bytes_ne` |
| bacontains / bytearray_contains | APPROVED | mirrors `bytes_contains` |
| baas_string* / from_string_and_size | APPROVED (cimport) | C pointers / builders |
| banew | APPROVED (cimport) | uninit ≠ `bytearray(n)` |
| ConcatAndDel | REJECTED | no C-API sibling on 3.14 include |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B (Cython baseline) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench / probe | Result | Decision | Iteration |
|----------|------------|---------------|--------|----------|-----------|
| balen / basize | Beat `len` | harness small+n=64 | **0.60–0.88x** | APPROVED | 1 |
| bacheck* | Beat isinstance | harness hit/miss | **0.45–0.54x** | APPROVED | 1 |
| bafrom_object | Beat `bytearray(buf)` | mv + bytes | **0.76–0.81x** | APPROVED | 1 |
| baconcat | Beat `+` | 5+5, 64+6 | **0.77–0.79x** | APPROVED | 1 |
| baresize | Beat extend/del | shrink + grow | **0.61–0.71x** | APPROVED | 1 |
| banew | Beat `bytearray(n)` | semantics | faster but **uninit** | APPROVED (cimport) | 1 |
| baas_string* | Buffer access | smoke | borrowed mutable | APPROVED (cimport) | 1 |
| ConcatAndDel | Cheap alias | `nm` / include | missing | REJECTED | 1 |

## Bench notes

- Harness: [`bench/cybytearray_bench.py`](../../bench/cybytearray_bench.py)
- Primary: `balen` on small bytearray
- Env: CPython 3.14.6 · Linux x86_64 · GIL on (venv bench) · N=80000 RUNS=5

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| balen | small | 0.99±0.07ms | 1.10ms | 0.60x | 0.63x | pass |
| balen | n=64 | 1.47±0.80ms | 2.78ms | 0.88x | 1.57x | pass |
| basize | small | 1.00±0.03ms | 1.05ms | 0.62x | 0.64x | pass |
| bacheck | bytearray | 0.89±0.02ms | 0.92ms | 0.49x | 0.48x | pass |
| bacheck | bytes | 0.98±0.06ms | 1.07ms | 0.45x | 0.49x | pass |
| bacheck_exact | bytearray | 0.91±0.03ms | 0.95ms | 0.54x | 0.54x | pass |
| bafrom_object | memoryview | 3.25±0.06ms | 3.33ms | 0.81x | 0.82x | pass |
| bafrom_object | bytes | 2.53±0.02ms | 2.55ms | 0.76x | 0.73x | pass |
| baconcat | 5+5 | 2.04±0.05ms | 2.09ms | 0.77x | 0.78x | pass |
| baconcat | 64+6 | 2.04±0.04ms | 2.09ms | 0.79x | 0.79x | pass |
| baresize | shrink 8→4 | 4.83±0.07ms | 4.91ms | 0.71x | 0.72x | pass |
| baresize | grow 4→16 | 5.18±0.10ms | 5.31ms | 0.61x | 0.62x | pass |

Summary: 12/12 faster · 12/12 ≥5% gate · mean ratio **0.67x** · median **0.67x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cybytearray.py`](../../bench/tier_b/cybytearray.py) · `cybytearray_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| balen | small | 2.90±0.21ms | 3.25ms | 2.82±0.05ms | **1.03x** | 1.12x | baseline faster |
| bacheck | bytearray | 2.97±0.08ms | 3.07ms | 2.98±0.08ms | **1.00x** | 1.01x | ~tie |
| bacheck_exact | bytearray | 3.00±0.15ms | 3.24ms | 2.89±0.16ms | **1.04x** | 1.04x | baseline faster |

**Tier B takeaway:** primary `balen` **1.03x** vs typed `len` — ~parity.

## Experiment conclusions

**Tier B:** primary `balen` **1.03x** vs typed `len` — ~parity.

| Topic | Finding |
|-------|---------|
| Why len/check win | Avoids Python `len`/`isinstance` call path; macros on typed `bytearray` |
| `baconcat` | Always allocates a **new** bytearray (unlike unique-ref `PyBytes_Concat`); safe as public |
| `banew` | `FromStringAndSize(NULL,n)` leaves **previous heap contents**; `bytearray(n)` zeros — **cdef only** |
| `baas_string` | Borrowed **mutable** buffer; must not outlive `ba`; `AsString` rejects non-bytearray |
| `baresize` | In-place realloc via C-API; Python baseline (del/extend zeros) does more work — grow especially |
| Cheap aliases | No `ConcatAndDel` in `bytearray.pxd` / 3.14 exports — nothing to alias |
| ABI | All 10 include symbols present (Check*/AS_*/GET_* are macros; others in `nm`) |

## Done when

- [x] Full inventory vs mapped include
- [x] Try-all + **depth** (uninit, borrowed buffer, resize shapes, ABI)
- [x] Bench results + experiment conclusions
- [x] Before merge: `.pyi` one-liners; lean `.pxd`; `banew` not public
