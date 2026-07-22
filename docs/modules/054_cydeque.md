# cydeque

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `collections.deque` (custom; no public C-API) |
| Sources | `src/cypy/cydeque.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided |
| Format | v2 |
| Indexed | full (declared surface) |

## Why

Typed equality for `collections.deque` queue/window call sites without a full deque C-API wrap. Richcompare matches Python `deque.__eq__` (len + elementwise).

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| dqeq / deque_eq | cypy | cpdef | public | identity + richcompare; soft `dqeq` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| dqeq / deque_eq | APPROVED | Tier A gate on small/empty/nested; n=64 ~tie (issue #41); not `hot` |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 2 |
| Last pass | 2026-07-22 — Tier A depth (issue #41 follow-up) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| deque_eq | Beat Python `==` call overhead | Tier A scale | small/empty/nested **0.57–0.91x**; n=64 **~0.98–0.99x** | APPROVED (not hot) | 2 |

## Bench notes

- Harness: [`bench/cydeque_bench.py`](../../bench/cydeque_bench.py)

## Bench results

Harness: [`bench/cydeque_bench.py`](../../bench/cydeque_bench.py) · tier A · CPython 3.14 · N=80_000 × runs=11

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| deque_eq | eq small | 5.06±0.08ms | 5.20ms | **0.90x** | 0.91x | APPROVED |
| deque_eq | ne small | 4.78±0.05ms | 4.87ms | **0.91x** | 0.92x | APPROVED |
| deque_eq | identity | 0.95±0.03ms | 1.00ms | **0.57x** | 0.56x | APPROVED |
| deque_eq | eq empty | 3.27±0.04ms | 3.35ms | **0.84x** | 0.84x | APPROVED |
| deque_eq | eq n=64 | 29.42±0.37ms | 30.29ms | **0.99x** | 1.01x | ~tie (keep API) |
| deque_eq | ne n=64 | 28.81±0.06ms | 28.93ms | **0.98x** | 0.98x | ~tie (keep API) |
| deque_eq | eq nested | 4.26±0.04ms | 4.32ms | **0.87x** | 0.86x | APPROVED |

Summary: 7/7 faster · 5/7 ≥5% gate · mean **0.87x** · median **0.90x**.

## Experiment conclusions

| Topic | Finding |
|-------|---------|
| Why win (small) | Avoids Python `==` method lookup / call overhead; identity short-circuit is **0.57x** |
| Why n=64 ~tie | Elementwise richcompare dominates; same CPython deque compare work after the call |
| Scale | Wins shrink as element count grows — leave off `hot`; prefer for small windows / identity-heavy sites |
| Semantics | Same as `deque.__eq__` (len + elementwise, nested OK). Soft `dqeq` COMPAT-only |
| Ownership | No borrowed pointers — safe |

## Done when

- [x] Declared surface inventory
- [x] Workflow + decision log
- [x] Tier A harness + tracker tables (no smoke placeholders)
- [x] Smoke example + exports + CHANGELOG
