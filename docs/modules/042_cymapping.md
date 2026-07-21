# cymapping

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.mapping` |
| Sources | `src/cypy/cymapping.pxd`, `.pyx`, `.pyi` |
| Surface | public |
| Tracker lifecycle | decided |
| Format | v2 |
| Indexed | full |

## Why

Abstract mapping protocol. Prefer ``cydict`` when type known.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| map_check / len / has_key* / del* / keys / values / items / getitem_string / setitem_string | public | |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| map_check / has_key / getitem_string | APPROVED | see benches |
| map_len / keys | APPROVED (API) | often lose to builtins |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **Provisional (Protocols)** after 1.0 — not Core; may evolve under minors |
| Iteration | 1 |
| Last pass | 2026-07-21 — Phase 4 Tier B |
| Next action | — |

## Bench notes

- Harness: [`bench/cymapping_bench.py`](../../bench/cymapping_bench.py)

## Bench results

Harness: [`bench/cymapping_bench.py`](../../bench/cymapping_bench.py) · tier A · CPython 3.14 · N=80_000

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| map_check | dict | **0.16x** | APPROVED |
| map_check | list (miss) | **0.18x** | APPROVED |
| map_len | dict | **1.03x** | APPROVED (API) |
| map_has_key | hit | **0.71x** | APPROVED |
| map_getitem_string | key | **0.67x** | APPROVED |
| map_keys | dict | **0.51x** | APPROVED |

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cymapping.py`](../../bench/tier_b/cymapping.py) · `cymapping_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| map_check | hit | 2.92±0.01ms | 2.93ms | 2.49±0.02ms | **1.17x** | 1.16x | baseline faster |

**Tier B takeaway:** primary `map_check` **1.17x** vs typed Cython baseline (hit).


## Experiment conclusions

**Tier B:** `map_check` **1.16x** vs isinstance(dict) — Mapping check is broader.

| Topic | Finding |
|-------|---------|
| Why checks win | Mapping flag / abstract check beats `isinstance(Mapping)` |
| Why prefer typed | When dict known, `cydict` (`dget`/`dcontains`) avoids abstract protocol dispatch |
| Scale | Abstract ops stay O(1) wrapper cost; large maps dominated by hash lookup either way |
| Safety | `HasKey` never raises on miss (unlike `o[k]`); string helpers are cheap aliases |
| Subtype | Works for any mapping subtype implementing the protocol — not dict-only |

## Done when

- [x] Try-all + depth + benches + `.pyi`
