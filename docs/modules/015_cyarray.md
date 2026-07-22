# cyarray

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.array` (`Cython/Includes/cpython/array.pxd`) — Cython helpers over `array.array` |
| Sources | `src/cypy/cyarray.pxd`, `cyarray.pyx`, `cyarray.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Stable `cypy` names over Cython’s `array.pxd` inline helpers (`clone`/`copy`/`resize*`/`extend`/`zero`) for stdlib `array.array` buffer hot paths.

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| aycheck / aycheck_exact | cypy | cpdef | public | `isinstance` / `type is` |
| aylen | cypy | cpdef | public | `Py_SIZE` |
| ayeq | cypy | cpdef | public | typecode/len/`memcmp` (soft); preferred `array_eq` |
| aycopy / ayclone | cypy | cpdef | public | Cython `copy` / `clone` |
| ayextend / ayzero | cypy | cpdef | public | `extend` / `memset` zero |
| ayresize / ayresize_smart | cypy | cpdef | public | Cython resize helpers |
| ayextend_buffer | cypy | cdef | cimport | raw `char*` append |
| array.array / newarrayobject | C-API | used-by | — | via Cython include |
| resize / resize_smart / clone / copy / extend / zero | C-API | used-by | — | wrapped above |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| aylen / checks | APPROVED | **0.51–0.61x** |
| ayeq / array_eq | APPROVED | mirrors `bytes_eq` (typecode + memcmp) |
| aycopy / ayclone | APPROVED | **0.19–0.46x** |
| ayextend / ayzero | APPROVED | **0.08–0.82x** (`memset` demolishes Python loop) |
| ayresize / smart | APPROVED | **0.25–0.81x** |
| ayextend_buffer | APPROVED (cimport) | raw pointer |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B (Cython baseline) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| aylen | Beat `len` | harness | **0.60x** | APPROVED | 1 |
| aycopy / ayclone | Beat ctor | harness | **0.19–0.46x** | APPROVED | 1 |
| ayzero | Beat Python loop | n=64 | **0.08x** | APPROVED | 1 |
| ayextend_buffer | C pointer | smoke | cdef only | APPROVED (cimport) | 1 |

## Bench notes

- Harness: [`bench/cyarray_bench.py`](../../bench/cyarray_bench.py)
- Primary: `aylen` small · Env: CPython 3.14.6 · N=80000 RUNS=5

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| aylen | small | 0.95±0.02ms | 0.98ms | 0.60x | 0.61x | pass |
| aylen | n=64 | 0.97±0.03ms | 1.00ms | 0.61x | 0.61x | pass |
| aycheck | array | 0.88±0.03ms | 0.94ms | 0.51x | 0.52x | pass |
| aycheck | list | 0.95±0.03ms | 1.00ms | 0.43x | 0.43x | pass |
| aycheck_exact | array | 0.92±0.05ms | 1.00ms | 0.55x | 0.57x | pass |
| aycopy | small | 2.08±0.02ms | 2.10ms | 0.44x | 0.43x | pass |
| aycopy | n=64 | 2.23±0.07ms | 2.30ms | 0.46x | 0.46x | pass |
| ayclone | clone zero n=8 | 2.23±0.09ms | 2.37ms | 0.19x | 0.20x | pass |
| ayextend | extend +2 | 7.55±0.04ms | 7.60ms | 0.82x | 0.72x | pass |
| ayzero | zero n=64 | 6.78±0.07ms | 6.87ms | 0.08x | 0.08x | pass |
| ayresize | shrink 8→4 | 7.51±0.03ms | 7.55ms | 0.81x | 0.81x | pass |
| ayresize_smart | grow 4→16 | 7.59±0.04ms | 7.63ms | 0.25x | 0.25x | pass |

Summary: 12/12 faster · 12/12 ≥5% gate · mean **0.48x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cyarray.py`](../../bench/tier_b/cyarray.py) · `cyarray_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| aylen | small i | 3.00±0.17ms | 3.20ms | 2.87±0.08ms | **1.04x** | 1.07x | baseline faster |
| aycheck | array | 2.53±0.01ms | 2.54ms | 2.54±0.02ms | **1.00x** | 0.99x | ~tie |

**Tier B takeaway:** primary `aylen` **1.04x** vs typed `len` — ~parity.

## Experiment conclusions

**Tier B:** primary `aylen` **1.04x** vs typed `len` — ~parity.

| Topic | Finding |
|-------|---------|
| Why win | Direct `Py_SIZE` / Cython `newarrayobject`+`memcpy`/`memset` vs Python ctor/loops |
| `ayzero` | `memset` vs per-element Python assign — largest win (**0.08x**) |
| `ayclone(zero=False)` | Leaves uninit buffer like `banew`; public default `zero=True` is safe |
| `ayextend_buffer` | Requires matching typecode + valid `char*` — cimport only |
| Not classic `PyArray_*` | Stdlib `array.array` via Cython include (CPython-private layout) |

## Done when

- [x] Full inventory + try-all + depth
- [x] Bench results + experiment conclusions
- [x] `.pyi` one-liners; lean `.pxd`
