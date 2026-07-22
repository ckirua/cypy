# cysequence

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.sequence` |
| Sources | `src/cypy/cysequence.pxd`, `.pyx`, `.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Abstract sequence protocol for unknown concrete types. Prefer typed modules (`cylist`/`cytuple`) when the type is known — `sqsize`/`sqlen` lose to `len` from Python.

## Inventory

| Symbol | Export | Notes |
|--------|--------|-------|
| sqcheck / sqsize / sqlen | public | Length is Size alias (cheap sibling) |
| sqeq | public | identity/size + richcompare; preferred `seq_eq` |
| sqconcat / sqrepeat / inplace_* | public | |
| sqget / sqslice / sqset / sqdel / slice mutators | public | |
| sqcount / sqcontains / sqindex | public | |
| sqlist / sqtuple | public | |
| sqfast / sqfast_get / sqfast_items / sqfast_size / sqitem | cimport | Fast macros / pointer |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| sqget (primary) | APPROVED | list **0.93x** / tuple **0.72x** |
| sqcheck / contains / concat / repeat / slice / list / index | APPROVED | 0.37–0.91x |
| sqeq / seq_eq | APPROVED | identity/size + richcompare (issue #23) |
| sqsize / sqlen | APPROVED (API) | **1.09–1.10x** vs `len` — keep for abstract protocol |
| sqcount / sqtuple | APPROVED (API) | **1.05–1.09x** — protocol completeness |
| sqfast* / sqitem | APPROVED (cimport) | borrowed / unchecked |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **Provisional (Protocols)** after 1.0 — not Core; may evolve under minors |
| Iteration | 1 |
P26-07-22 — `*_eq` inventory Tier A (`cyeq_inventory_bench`)|
| Next action | — |

## Decision log

| Function | Hypothesis | Result | Decision | Iteration |
|----------|------------|--------|----------|-----------|
| sqget | Beat `o[i]` | 0.72–0.93x | APPROVED | 1 |
| sqsize | Beat `len` | **1.09x** lose | APPROVED (API) | 1 |
| sqfast* | Hot Cython | macros | APPROVED (cimport) | 1 |
| sqeq | Abstract `==` | identity/size + richcompare | APPROVED | 1 |

## Bench notes

- Harness: [`bench/cysequence_bench.py`](../../bench/cysequence_bench.py) · N=80000 · CPython 3.14.6
- Primary: `sqget` list[0]

## Bench results

| operation | case | ratio | verdict |
|-----------|------|-------|---------|
| sqcheck | list / int | 0.37x / 0.44x | pass |
| sqsize / sqlen | list | 1.09x / 1.10x | API keep |
| sqget | list[0] / tuple[2] | 0.93x / 0.72x | pass |
| sqcontains | hit / miss | 0.71x / 0.76x | pass |
| sqindex / sqcount | | 0.91x / 1.05x | pass / API |
| sqslice / concat / repeat | | 0.74–0.90x | pass |
| sqlist / sqtuple | | 0.88x / 1.09x | pass / API |

Summary: 11/15 ≥5% gate · mean **0.83x**.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cysequence.py`](../../bench/tier_b/cysequence.py) · `cysequence_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| sqget | list[0] | 2.84±0.09ms | 3.00ms | 2.61±0.02ms | **1.09x** | 1.14x | baseline faster |
| sqlen | n=4 | 2.63±0.07ms | 2.74ms | 2.93±0.11ms | **0.90x** | 0.90x | cypy faster |

**Tier B takeaway:** primary `sqget` **1.09x** vs typed Cython baseline (list[0]).



### `*_eq` inventory (Tier A depth)

Harness: [`bench/cyeq_inventory_bench.py`](../../bench/cyeq_inventory_bench.py) · N=80_000 × runs=11 · CPython 3.14

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| seq_eq | list eq | 1.43±0.12ms | 1.76ms | **0.76x** | 0.80x | APPROVED |
| seq_eq | tuple↔list eq | 1.39±0.12ms | 1.69ms | **0.76x** | 0.81x | APPROVED |
| seq_eq | list ne | 1.57±0.06ms | 1.72ms | **0.73x** | 0.75x | APPROVED |
## Experiment conclusions

**Tier B:** primary `sqget` **1.10x** vs typed index; `sqlen` **0.90x**.

| Topic | Finding |
|-------|---------|
| Why `sqsize` loses | Abstract `PySequence_Size` → tp_as_sequence indirection; `len` specializes |
| Prefer typed | Use `llen`/`tlen` when type known; prefer `list_eq`/`tuple_eq` over `seq_eq` |
| `seq_eq` | Same semantics as `==` (list≠tuple; identity/size short-circuit then richcompare) |
| `sqfast` | Returns list/tuple as-is; GET_ITEM borrowed — cdef |
| InPlace* | May return new object if type refuses in-place — same as Python `+=` |
| Cheap alias | `sqlen` ≡ `sqsize` (Length/Size) |

## Done when

- [x] Full try-all + depth + benches + `.pyi`
