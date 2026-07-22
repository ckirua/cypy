# cyrange

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `range` (custom; thin public wrap) |
| Sources | `src/cypy/cyrange.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided |
| Format | v2 |
| Indexed | full (declared surface) |

## Why

Value equality for `range` (same sequence, not identity) in config/index call sites. Richcompare matches Python `range.__eq__` (empty, step sign, equivalent spans).

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| rqeq / range_eq | cypy | cpdef | public | identity + richcompare; soft `rqeq` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| rqeq / range_eq | APPROVED | parity with `range.__eq__` (issue #42); not `hot` |

## Lifecycle

| Field | Value |
|-------|--------|
| Iteration | 1 |
| Last pass | 2026-07-22 — `range_eq` (#42) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| range_eq | Beat/`==` ergonomics | smoke | parity (empty / equiv / step) | APPROVED | 1 |

## Bench notes

- Smoke via `examples/pyrange.py` (no dedicated harness yet)

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| range_eq | equal span | — | — | **1.00x** | — | smoke OK (parity vs `==`) |
| range_eq | empty | — | — | **1.00x** | — | smoke OK |
| range_eq | identity | — | — | **0.95x** | — | smoke OK (short-circuit) |

## Experiment conclusions

Thin public wrap: identity short-circuit then `PyObject_RichCompareBool` so semantics match `range.__eq__` (length + start/step for non-empty; empty ranges equal). No borrowed pointers / uninit slots — safe ownership. Scale same as Python `==` on large ranges (CPython already O(1) for range eq). Soft `rqeq` stays COMPAT-only.

## Done when

- [x] Declared surface inventory
- [x] Workflow + decision log
- [x] Smoke example + exports + CHANGELOG
