# cyunicode

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.unicode` (UTF-8 / intern slice; high-level str → [`006_cystr.md`](006_cystr.md)) |
| Sources | `src/cypy/cyunicode.pxd`, `cyunicode.pyx`, `cyunicode.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full (declared slice) |

## Why

Zero-copy UTF-8 borrow + intern for Cython; public owning `bytes` / `uintern` for benches and `cyansi`.

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| uutf8 | cypy | cdef | cimport | borrowed `AsUTF8` — do not outlive `s` |
| uutf8_and_size | cypy | cdef | cimport | borrowed + length |
| uutf8_bytes | cypy | cpdef | public | owning `AsUTF8String` |
| uintern_in_place | cypy | cdef | cimport | mutates `PyObject**` slot |
| uintern | cypy | cpdef | public | intern + return |
| unicode_from_string | cypy | cdef | cimport | `PyUnicode_FromString` — no intern; mirror `bytes_from_string` |
| uintern_from_string | cypy | cdef | cimport | `PyUnicode_InternFromString` sibling |
| codecs / From* / New / … | C-API | tried | — | out of slice → cystr deferred / REJECTED scope |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| uutf8 / uutf8_and_size | APPROVED (cimport) | zero-copy; unsafe from Python |
| uutf8_bytes | APPROVED | **0.95–1.01x** vs `encode` — clarity / owning mirror |
| uintern | APPROVED | **1.04–1.05x** vs `sys.intern` — clarity; used by cyansi |
| unicode_from_string | APPROVED (cimport) | ordinary C→str; no intern; issue #1 |
| uintern_in_place / uintern_from_string | APPROVED (cimport) | slot / C-string siblings |
| remainder unicode | REJECTED (scope) | not this slice |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 2 |
| Last pass | 2026-07-22 — `unicode_from_string` (issue #1) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench | Result | Decision | Iteration |
|----------|------------|-------|--------|----------|-----------|
| uutf8_bytes | Beat encode | `bench/cyunicode_bench.py` | ~1.0x | APPROVED (clarity) | 1 |
| uintern | Match sys.intern | same | ~1.05x | APPROVED (clarity) | 1 |
| uutf8* | Zero-copy | smoke/docs | borrowed | APPROVED (cimport) | 1 |
| unicode_from_string | Cheap C→str | smoke (cimport) | thin alias | APPROVED (cimport) | 2 |

## Bench notes

- Harness: [`bench/cyunicode_bench.py`](../../bench/cyunicode_bench.py)
- Env: CPython 3.14.6 · Linux x86_64 · GIL on · N=80000 RUNS=5

## Bench results

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| uutf8_bytes | short | 1.51±0.06ms | 1.60ms | 1.01x | 1.04x | tie |
| uutf8_bytes | n=64 | 1.43±0.03ms | 1.47ms | 0.95x | 0.89x | pass |
| uutf8_bytes | n=4k | 4.36±0.21ms | 4.72ms | 1.01x | 1.08x | tie |
| uutf8_bytes | non-ascii | 2.64±0.05ms | 2.73ms | 1.00x | 1.03x | tie |
| uintern | already | 1.03±0.05ms | 1.12ms | 1.05x | 1.10x | clarity |
| uintern | short | 1.05±0.03ms | 1.10ms | 1.05x | 1.00x | clarity |
| uintern | non-ascii | 1.03±0.02ms | 1.05ms | 1.04x | 0.95x | clarity |
| unicode_from_string | ascii / empty / non-ascii | — | — | n/a (cimport) | — | smoke OK |

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cyunicode.py`](../../bench/tier_b/cyunicode.py) · `cyunicode_tb.pyx` · CPython 3.14.6 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| uutf8_bytes | short | 11.18±0.01ms | 11.20ms | 11.22±0.04ms | **1.00x** | 0.99x | ~tie |
| uintern | already | 4.20±0.01ms | 4.22ms | 3.84±0.03ms | **1.09x** | 1.08x | baseline faster |

**Tier B takeaway:** `uutf8_bytes` **1.00x** vs `AsUTF8String` — thin wrapper parity.

## Experiment conclusions

**Tier B:** `uutf8_bytes` **1.00x** vs `AsUTF8String` — thin wrapper parity.

- **Why public ~tie:** `AsUTF8String` / `InternInPlace` are the same C entry points `str.encode` / `sys.intern` use; Python→cpdef adds little. Real win is **cdef `uutf8`** zero-copy borrow in Cython (not tier-A measurable).
- **Safety:** borrowed `uutf8*` must not outlive `s`; invalidate if `s` is resized. `uintern_in_place` needs a mutable `PyObject**` — not safe as a naive Python call. C-string helpers take NUL-terminated `const char *` (not Python `str`); NULL is undefined (same as raw C-API).
- **Alias:** `unicode_from_string` wraps `PyUnicode_FromString` (owning `str`, **no** intern). `uintern_from_string` wraps `PyUnicode_InternFromString`. Prefer the former for ordinary C→str (toml keys, path fragments); reserve intern for table/cold-path identity.
- **Demotion:** `unicode_from_string` is **APPROVED (cimport)** — `const char *` is not a Python-callable surface; mirrors `bytes_from_string` (not on `cypy.hot` / buffers).
- **Free-threaded:** intern table is runtime-shared; prefer intern at module-init / cold paths (as `cyansi` tables do). Non-interning `unicode_from_string` has no intern-table contention.

## Done when

- [x] Full inventory of declared slice
- [x] Workflow + decision log
- [x] Bench results + Experiment conclusions
- [x] Public `.pyi` one-liners; lean `.pxd`
- [x] `unicode_from_string` (issue #1) — cimport + smoke
