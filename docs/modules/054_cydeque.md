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
| dqeq / deque_eq | APPROVED | parity with `deque.__eq__` (issue #41); not `hot` |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 1 |
| Last pass | 2026-07-22 — `deque_eq` (#41) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| deque_eq | Beat/`==` ergonomics | smoke | parity + identity short-circuit | APPROVED | 1 |

## Bench notes

- Smoke via `examples/pydeque.py` (no dedicated harness yet)

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| deque_eq | equal small | — | — | **1.00x** | — | smoke OK (parity vs `==`) |
| deque_eq | unequal | — | — | **1.00x** | — | smoke OK |
| deque_eq | identity | — | — | **0.95x** | — | smoke OK (short-circuit) |

## Experiment conclusions

Thin public wrap: identity short-circuit then `PyObject_RichCompareBool` so semantics match `deque.__eq__` (len + elementwise, including nested). No borrowed pointers / uninit slots — safe ownership. Scale same as Python `==` on large deques (no memcmp path; deque is linked blocks). Soft `dqeq` stays COMPAT-only.

## Done when

- [x] Declared surface inventory
- [x] Workflow + decision log
- [x] Smoke example + exports + CHANGELOG
