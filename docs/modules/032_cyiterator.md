# cyiterator

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.iterator` |
| Sources | `src/cypy/cyiterator.pxd`, `.pyx`, `.pyi` |
| Surface | public |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Iterator protocol check and C-style next (None at end).

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| iter_check / iter_next | public | next returns None at end |
| iter_eq / itereq | public | identity eq (`object.__eq__`); soft `itereq`; not `hot` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| iter_check | APPROVED | **0.31–0.46x** |
| iter_eq / itereq | APPROVED | identity equality (issue #40); not `hot` |
| iter_next | APPROVED (API) | **1.05x** — different end semantics vs `next` |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 1 |
| Last pass | 2026-07-22 — `iter_eq` (#40) |
| Next action | — |

## Decision log

| Function | Result | Decision | Iteration |
|----------|--------|----------|-----------|
| iter_check | 0.31–0.46x | APPROVED | 1 |
| iter_eq / itereq | identity | APPROVED | 1 |
| iter_next | 1.05x | APPROVED (API) | 1 |

## Bench notes

- Harness: [`bench/cyiterator_bench.py`](../../bench/cyiterator_bench.py) · N=80000

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| iter_check | iter / list | 0.31x / 0.46x | pass |
| iter_next | range-iter | 1.05x | API |

Summary: 2/3 gate · mean **0.61x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cyiterator.py`](../../bench/tier_b/cyiterator.py) · `cyiterator_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| iter_check | list_iter | 2.99±0.04ms | 3.05ms | 27.45±0.44ms | **0.11x** | 0.11x | cypy faster |

**Tier B takeaway:** primary `iter_check` **0.11x** vs typed Cython baseline (list_iter).


## Experiment conclusions

**Tier B:** `iter_check` **0.11x** vs hasattr `__next__`.

| Topic | Finding |
|-------|---------|
| Check win | Slot vs hasattr(`__next__`) |
| Next semantics | C-API returns NULL/None at end without StopIteration — not a drop-in for Python `next` |
| Why ~tie | Same underlying tp_iternext when items remain |
| Why win | Iter Check is a type flag test vs collections.abc heuristics |
| Scale | `iter(range)` constructor ~1.09x lose — prefer builtin `iter` for construction |
| Safety | Next/Send/Throw match generator protocol; StopIteration must propagate |
| ABI | Iterator API stable on 3.14 |
| `iter_eq` | Identity (`a is b`) — typical CPython `object.__eq__`; soft `itereq`; leave off `hot` until measured win |


## Done when

- [x] Try-all + depth + benches + `.pyi`
