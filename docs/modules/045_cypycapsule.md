# cypycapsule

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.pycapsule` |
| Sources | `src/cypy/cypycapsule.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided |
| Format | v2 |
| Indexed | full |

## Why

Capsule type checks public; pointer get/set cimport (void*).

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| capsule_check_exact / is_valid | public | |
| new / get_pointer / set_* / import | cimport | void* |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| check_exact / is_valid | APPROVED | see benches |
| pointer APIs | APPROVED (cimport) | void* |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B |
| Next action | — |

## Bench notes

- Harness: [`bench/cypycapsule_bench.py`](../../bench/cypycapsule_bench.py)

## Bench results

Harness: [`bench/cypycapsule_bench.py`](../../bench/cypycapsule_bench.py) · tier A · CPython 3.14 · N=80_000

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| capsule_check_exact | capsule | **0.31x** | APPROVED |
| capsule_is_valid | name match | **0.31x** | APPROVED |

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cypycapsule.py`](../../bench/tier_b/cypycapsule.py) · `cypycapsule_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| capsule_check_exact | capsule | 2.89±0.24ms | 3.17ms | 28.42±0.26ms | **0.10x** | 0.11x | cypy faster |

**Tier B takeaway:** primary `capsule_check_exact` **0.10x** vs typed Cython baseline (capsule).


## Experiment conclusions

**Tier B:** `capsule_check_exact` **0.10x** vs type-name baseline.

| Topic | Finding |
|-------|---------|
| Why checks win | Exact type + name validation in C beats Python capsule introspection |
| Ownership / safety | `GetPointer` returns `void*` — never public; destructor is C fn or NULL |
| ABI | Pointer get/set/import stay cimport; wrong name → NULL / exception |
| Scale | Check is O(1); no payload size — capsule holds an opaque pointer |
| Prefer | Public checks for gates; all pointer mutation in cdef under GIL |

## Done when

- [x] Try-all + depth + benches + `.pyi`
