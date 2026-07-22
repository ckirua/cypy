# cybytes

| Field | Value |
|-------|--------|
| Status | present |
| Maps to | `cpython.bytes` (`Cython/Includes/cpython/bytes.pxd`) |
| Sources | `src/cypy/cybytes.pxd`, `cybytes.pyx`, `cybytes.pyi` |
| Surface | public + cimport |
| Tracker lifecycle | decided (tier A + depth) |
| Format | v2 |
| Indexed | full |

## Why

Scanner hot paths plus full include try-all. Depth showed pure `memmem` **loses** to CPython `stringlib` on large haystacks; hybrid threshold + uninit/`_PyBytes_Resize` semantics documented below.

## Inventory

| Symbol | Layer | Kind | Export | Notes |
|--------|-------|------|--------|-------|
| bcheck | cypy | cpdef | public | `PyBytes_Check` |
| bcheck_exact | cypy | cpdef | public | `PyBytes_CheckExact` |
| blen | cypy | cpdef | public | `PyBytes_GET_SIZE` |
| bsize | cypy | cpdef | public | `PyBytes_Size` |
| bcontains | cypy | cpdef | public | `memchr`/`memmem` if `hlen≤256` else `in` |
| beq | cypy | cpdef | public | identity/len/`memcmp` (soft); preferred `bytes_eq` |
| bne | cypy | cpdef | public | `not beq` (soft); preferred `bytes_ne` |
| bstartswith | cypy | cpdef | public | prefix len + `memcmp` (soft); preferred `bytes_startswith` |
| bfrom_object | cypy | cpdef | public | `PyBytes_FromObject` |
| bas_string | cypy | cdef | cimport | `PyBytes_AS_STRING` |
| bas_string_checked | cypy | cdef | cimport | `PyBytes_AsString` (rejects non-bytes) |
| bfrom_string | cypy | cdef | cimport | `PyBytes_FromString` |
| bfrom_string_and_size | cypy | cdef | cimport | `PyBytes_FromStringAndSize` |
| bnew | cypy | cdef | cimport | uninit buffer — **not public** |
| bconcat | cypy | cdef | cimport | `PyBytes_Concat` |
| bconcat_and_del | cypy | cdef | cimport | `PyBytes_ConcatAndDel` |
| bresize | cypy | cdef | cimport | `_PyBytes_Resize` |
| PyBytes_Check / Exact | C-API | used-by | — | → checks |
| PyBytes_GET_SIZE / Size | C-API | used-by | — | → `blen` / `bsize` |
| PyBytes_AS_STRING / AsString | C-API | used-by | — | → `bas_string*` |
| PyBytes_AsStringAndSize | C-API | tried | — | covered by pointer + `blen` |
| PyBytes_FromObject / FromString* | C-API | used-by | — | → from_* / bnew |
| PyBytes_FromFormat / V | C-API | tried | — | varargs; no public wrap |
| PyBytes_Concat* | C-API | used-by | — | → `bconcat` / `bconcat_and_del` |
| _PyBytes_Resize | C-API | used-by | — | → `bresize` |
| PyBytes_Format / Intern* / Decode* / Encode* | C-API | tried | — | **not exported** on 3.14 `.so` |

## Workflow status

| Function | Status | Why |
|----------|--------|-----|
| bcontains | APPROVED | primary small **0.20x**; hybrid fixes large regression |
| beq | APPROVED | mirror `streq`; identity/len + `memcmp`; see Bench |
| bne / bytes_ne | APPROVED | `not beq` — API sibling of `str_ne` |
| bstartswith / bytes_startswith | APPROVED | prefix len + `memcmp` (mirror `str_startswith`) |
| blen / bsize | APPROVED | **0.59x**; prefer `blen` typed |
| bcheck / exact | APPROVED | **0.56x** / **0.55x** |
| bfrom_object | APPROVED | **0.60x** |
| bas_string* / from_string* | APPROVED (cimport) | C pointers / builders |
| bnew | APPROVED (cimport) | uninit ≠ `bytes(n)`; unsafe as public |
| bconcat / bconcat_and_del / bresize | APPROVED (cimport) | ownership/`*pv` semantics — cdef |
| Format / Intern / codecs | REJECTED | missing 3.14 ABI |
| FromFormat | REJECTED | varargs |
| AsStringAndSize helper | REJECTED | redundant with pointer + len |

## Lifecycle

| Field | Value |
|-------|--------|
| Freeze | **1.0 Core** — public + documented cimport; see COVERAGE § 1.0 freeze |
| Iteration | 6 |
| Last pass | 2026-07-22 — `bytes_eq` / `beq` (issue #2) |
| Next action | — |

## Decision log

| Function | Hypothesis | Bench / probe | Result | Decision | Iteration |
|----------|------------|---------------|--------|----------|-----------|
| bcontains | Beat `in` always | scale 6…8KiB | win &lt;256B; **lose** ≥1KiB on pure memmem | hybrid ≤256 → APPROVED | 4 |
| beq | Beat `==` on typed bytes | short/1KiB eq+ne | wins short; ~tie/win 1KiB | APPROVED (public + hot) | 6 |
| blen / bsize | Beat `len` | harness | **0.59x** | APPROVED | 4 |
| bcheck* | Beat isinstance | harness | **0.40–0.56x** | APPROVED | 4 |
| bfrom_object | Beat `bytes(buf)` | harness | **0.60x** | APPROVED | 4 |
| bnew | Beat `bytes(n)` | semantics | faster but **uninit leak** | REJECTED public → **cdef** | 4 |
| bconcat / bconcat_and_del | Unique-only / +DECREF | source | unique in-place; else new object | APPROVED (cimport) | 5 |
| bresize | Like tuple SystemError | CPython source | non-unique **copies** (no BadInternalCall) | APPROVED (cimport) | 4 |
| Format/Intern/codecs | Wrap | `nm` 3.14 | missing symbols | REJECTED | 3 |

## Bench results

Harness: [`bench/cybytes_bench.py`](../../bench/cybytes_bench.py) · tier A · 3.14 · `N=80_000` × 5 · warmup 0  
**Primary:** small multi-byte hit → **~0.20x** · **`bytes_eq`** short/1KiB → **0.59–0.68x** vs Python `==`

| operation | case | cypy mean±σ | p99 | ratio | p99× | verdict |
|-----------|------|-------------|-----|-------|------|---------|
| bcontains | small multi hit | — | — | **~0.20x** | — | APPROVED |
| bcontains | small 1-byte hit | — | — | ~0.19x | — | APPROVED |
| bcontains | small miss | — | — | ~0.20x | — | APPROVED |
| bcontains | 1KiB late hit | — | — | ~1.00x | — | ~tie (hybrid) |
| bcontains | 8KiB miss | — | — | ~1.03x | — | ~tie (hybrid) |
| beq | eq same | 0.97±0.03ms | 1.00ms | **0.59x** | 0.58x | APPROVED |
| beq | ne same-len | 1.01±0.01ms | 1.02ms | **0.61x** | 0.59x | APPROVED |
| beq | ne short | 0.99±0.04ms | 1.05ms | **0.60x** | 0.60x | APPROVED |
| beq | eq 1KiB | 0.94±0.02ms | 0.97ms | **0.59x** | 0.59x | APPROVED |
| beq | ne 1KiB | 1.56±0.02ms | 1.59ms | **0.68x** | 0.67x | APPROVED |
| beq | eq empty | 0.93±0.02ms | 0.95ms | **0.59x** | 0.59x | APPROVED |
| blen | blen | — | — | **~0.60x** | — | APPROVED |
| bsize | bsize | — | — | ~0.61x | — | APPROVED |
| bcheck | bytes | — | — | ~0.50x | — | APPROVED |
| bcheck | str | — | — | ~0.40x | — | APPROVED |
| bcheck_exact | bytes | — | — | ~0.59x | — | APPROVED |
| bfrom_object | memoryview | — | — | ~0.61x | — | APPROVED |

### Pre-hybrid scale (evidence for threshold)

Pure `memmem` vs `in` (ad-hoc, before hybrid): hlen=6 → ~0.20x; 64 → ~0.40x; **256 → ~1.00x**; 1024 → ~1.9x; 8192 → ~2.7x. Threshold **256** chosen at crossover.

### Tier B (Cython baseline)

Harness: [`bench/tier_b/cybytes.py`](../../bench/tier_b/cybytes.py) · `cybytes_tb.pyx` · CPython 3.14 · Linux x86_64 · `CPY_TIERB_N=2_000_000` × `runs=5`  
Ratio = cypy `cdef` loop / typed Cython baseline loop (opaque + sink). **Informational** — does not reopen Tier A.

| operation | case | cypy mean±σ | p99 | cy-base mean±σ | ratio | p99× | note |
|-----------|------|-------------|-----|----------------|-------|------|------|
| bcontains | small multi hit | 3.91±0.06ms | 3.97ms | 103.07±0.59ms | **0.04x** | 0.04x | cypy faster |
| beq | equal | 2.52±0.01ms | 2.53ms | 2.53±0.01ms | **1.00x** | 0.99x | ~tie |
| blen | small | 2.97±0.20ms | 3.20ms | 2.84±0.10ms | **1.05x** | 1.11x | baseline faster |
| bcheck | bytes | 2.48±0.01ms | 2.49ms | 2.51±0.02ms | **0.99x** | 0.98x | ~tie |
| bcheck_exact | bytes | 2.96±0.19ms | 3.22ms | 2.83±0.14ms | **1.05x** | 1.08x | baseline faster |

**Tier B takeaway:** primary `bcontains` **0.04x** vs typed `in` (memmem path wins in cdef loop). `beq` **~tie** vs typed `==` (win is Tier A Python call overhead).

## Experiment conclusions

**Tier B:** primary `bcontains` **0.04x** vs typed `in` (memmem path wins in cdef loop).

| Topic | Finding |
|-------|---------|
| Why small win | Avoids Python `sq_contains` / `stringlib` call overhead; `memchr`/`memmem` on tiny buffers |
| Why large lose | CPython `bytes_contains` → `_Py_bytes_contains` / `stringlib_find` (not exported); glibc `memmem` slower here past ~256B |
| Fix | `hlen > 256` → fall back to `needle in haystack` |
| `beq` / `bytes_eq` | Identity + len short-circuit + `memcmp` on `PyBytes_AS_STRING` (mirror `streq`). Tier A **0.59–0.68x** vs Python `==`; Tier B ~tie vs typed Cython `==` — export to `cypy.hot` |
| `bne` / `bytes_ne` | `not beq` — API sibling of `str_ne`; public + hot |
| `bstartswith` / `bytes_startswith` | prefix len + `memcmp`; public + hot |
| `bnew` | `FromStringAndSize(NULL,n)` leaves **previous heap contents**; `bytes(n)` zeros — **cdef only** |
| `_PyBytes_Resize` | Unlike `_PyTuple_Resize`, non-unique path **allocates a copy** and DECREFs old `*pv` (expects owned ref). Mis-wrapping without owning the ref is UB |
| `PyBytes_Concat` / `ConcatAndDel` | Unique+exact → resize in place; else new object via `SETREF`. Both aliased (`bconcat`, `bconcat_and_del`) |
| `AsString` | `TypeError` on `bytearray`; `AS_STRING` is unchecked typed `bytes` |
| 3.14 ABI | No Format / Intern / Decode / Encode exports |

## Done when

- [x] Full inventory
- [x] Try-all + **depth** (scale, hybrid, uninit, resize≠tuple, ABI)
- [x] Bench results + experiment conclusions
- [x] Before merge: `.pyi` one-liners; lean `.pxd`; `bnew` not public
- [x] `bytes_eq` / `beq` (issue #2) — public + hot
- [x] `bytes_ne` / `bne` (issue #8) — public + hot
- [x] `bytes_startswith` / `bstartswith` (issue #12) — public + hot
