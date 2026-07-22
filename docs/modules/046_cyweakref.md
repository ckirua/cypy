# cyweakref

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.weakref` |
| Sources | `src/cypy/cyweakref.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided |
| Format | v2 |
| Indexed | full |

## Why

Weakref checks and NewRef/GetObject for Cython.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| check* / new_ref / new_proxy / get_object | public | |
| weakref_eq / weakrefeq | public | referent eq (`weakref_richcompare`); soft `weakrefeq`; not `hot` |
| GET_OBJECT | cimport | unchecked |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| check / new_ref / get_object | APPROVED | see benches |
| weakref_eq / weakrefeq | APPROVED | referent equality (issue #39); not `hot` |
| GET_OBJECT | APPROVED (cimport) | unchecked |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 1 |
| Last pass | 2026-07-22 — `weakref_eq` (#39) |
| Next action | — |

## Decision log

| Function | Decision | Iteration |
|----------|----------|-----------|
| public | APPROVED | 1 |
| weakref_eq / weakrefeq | APPROVED | 1 |
| GET_OBJECT | APPROVED (cimport) | 1 |

## Bench notes

- Harness: [`bench/cyweakref_bench.py`](../../bench/cyweakref_bench.py)

## Bench results

Harness: [`bench/cyweakref_bench.py`](../../bench/cyweakref_bench.py) · tier A · CPython 3.14 · N=80_000

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| weakref_check | ref | **0.49x** | APPROVED |
| weakref_new_ref | object | **0.89x** | APPROVED |
| weakref_get_object | live | **0.60x** | APPROVED |

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cyweakref.py`](../../bench/tier_b/cyweakref.py) · `cyweakref_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| weakref_check | ref | 3.07±0.19ms | 3.25ms | 7.91±0.04ms | **0.39x** | 0.41x | cypy faster |

**Tier B takeaway:** primary `weakref_check` **0.39x** vs typed Cython baseline (ref).


## Experiment conclusions

**Tier B:** `weakref_check` **0.44x** vs isinstance(ref).

| Topic | Finding |
|-------|---------|
| Why win | C type checks and `PyWeakref_GetObject` beat Python `weakref` attribute paths |
| Borrowed / ownership | C `GetObject` returns borrowed; public wrapper INCREFs for safety |
| Dead ref | Cleared refs yield None — treat carefully vs historical `Py_None` quirks |
| ABI / safety | Unchecked `GET_OBJECT` macro is cimport-only; wrong type → crash |
| Scale | Ref ops are O(1); callback registration dominates real workloads, not check/get |
| `weakref_eq` | Referent equality (not identity): alive refs compare referents via `==`; dead → identity only (CPython `weakref_richcompare`). Soft `weakrefeq`. Unlike `capsule_eq` (identity). Leave off `hot` until measured win |

## Done when

- [x] Try-all + depth + benches + `.pyi`
