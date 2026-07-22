# Changelog

All notable changes to `cypy` are documented here. Version from
[`src/cypy/__about__.py`](src/cypy/__about__.py).

## [1.6.0] — 2026-07-22 — `bytes_ne`

### Added

- **`bytes_ne`** (`cybytes`): typed `bytes` inequality (`not bytes_eq` / soft `bne`).
  On `cypy` / `cypy.hot` / `cypy.buffers` (mirrors `str_ne` API; pairs with `bytes_eq`).

## [1.5.0] — 2026-07-22 — `memoryview_eq`

### Added

- **`memoryview_eq`** (`cymemoryview`): typed `memoryview` equality — C-contiguous
  same layout/`memcmp` fast path; non-contiguous falls back to richcompare.
  Soft `mveq` cdef-only; on `cypy` / `cypy.hot` / `cypy.buffers`.

## [1.4.0] — 2026-07-22 — `array_eq`

### Added

- **`array_eq`** (`cyarray`): typed `array.array` equality — identity/typecode/len
  short-circuit + `memcmp` over `itemsize * len` (mirrors `bytes_eq`). Soft
  letter `ayeq` stays cdef-only; preferred name on `cypy` / `cypy.hot` /
  `cypy.buffers`. Different typecodes compare false (same as Python `==`).

## [1.3.0] — 2026-07-22 — `bytearray_eq`

### Added

- **`bytearray_eq`** (`cybytearray`): typed `bytearray` equality — identity/len
  short-circuit + `memcmp` on `PyByteArray_AS_STRING` (mirrors `bytes_eq`). Soft
  letter `baeq` stays cdef-only; preferred name on `cypy` / `cypy.hot` /
  `cypy.buffers`.

## [1.2.0] — 2026-07-22 — `unicode_from_string`

### Added

- **`unicode_from_string`** (`cyunicode`): cimport thin wrapper for
  `PyUnicode_FromString` (no intern). Sibling of `uintern_from_string`;
  mirrors `bytes_from_string`.

## [1.1.0] — 2026-07-22 — `bytes_eq`

### Added

- **`bytes_eq`** (`cybytes`): typed `bytes` equality — identity/len short-circuit +
  `memcmp` on `PyBytes_AS_STRING` (mirrors `str_eq`). Soft letter `beq` stays
  cdef-only; preferred name on `cypy` / `cypy.hot` / `cypy.buffers`.

## [1.0.0] — 2026-07-21 — Core freeze

### Frozen

- **Core** public set: [`cypy.__all__`](src/cypy/__init__.py) + [`cypy.hot`](src/cypy/hot.py)
  — additive minors OK; removals / semantic changes need a major (see
  [`docs/RELEASE.md`](docs/RELEASE.md)).
- **Cimport contracts** for Core + documented `cdef` helpers: see
  [`COVERAGE.md`](COVERAGE.md) § “1.0 freeze” and per-module Surface / inventory
  in [`docs/modules/`](docs/modules/).

### Post-1.0 policy (Protocols / Runtime)

These tiers are **not** part of the Core freeze. They may still evolve under
**minors** after 1.0 (additions preferred; removals need deprecation + major
when they were public):

| Tier | Examples | Guidance |
|------|----------|----------|
| **Protocols** | `map_*`, `seq_*`, `num_*`, most `obj_*` | Prefer typed Core when the concrete type is known; `cypy.protocols` is provisional |
| **Runtime** | `dt_*`, `codec_*`, `time_*`, marshal/file/weakref/capsule/contextvars | Not micro-opt defaults; embedding / higher-level bridges |
| **cimport-only** | `cyerr`, `cymem`, `cythread`, `cyatomic`, … | Cython SDK only — never pure-Python |

### DEMOTE_ROOT at 1.0

Soft-alias demotions completed in **0.3**. Protocol/Runtime families remain
importable but **outside** Core `__all__` / `cypy.hot` (no surprise barrel trim).

## [0.3.0] — hard trim (Strategy B)

### Breaking

Soft root aliases in [`cypy.compat.COMPAT_MAP`](src/cypy/compat.py) are **removed**
from the `cypy` barrel and from public `.pyi` stubs. Soft letter/bare/`*_string` /
`dt_delta_*` / `method_function` / `method_self` / `time_time` names are Cython
`cdef`-only where they remain as implementation. Prefer word-prefix / `str_*` /
`ansi_*` / `*_cstr` / `dt_timedelta_*` / `method_get_*` / `time_wall`.

`cypy.__getattr__` raises `AttributeError` with `soft_alias_removal_hint` for
removed soft names.

### Kept

**Semantic twins** (`dict_len`/`dict_size`, `list_len`/`list_size`, …) stay dual —
never identity-aliased.

## [0.2.0] — soft-alias window (Strategy B)

### Soft aliases (removed in 0.3)

Word-prefix / `str_*` / `ansi_*` / `*_cstr` / `dt_timedelta_*` / `method_get_*` /
`time_wall` preferred; letter/bare/`*_string`/… dual-exported for the soft window.

### Conventions & discovery (Wave 5)

- N3/N4 rules: [`docs/NAMING.md`](docs/NAMING.md)
- Overlap playbooks: `examples/py_overlap_*.py`
- Facades: `cypy.containers`, `cypy.buffers`, `cypy.protocols` (prefer `cypy.hot`)
- Export CI: `scripts/check_exports.py`

## [0.1.1] — prior

Phase 5/6 surface + skill + examples on git tags. See git history / GitHub releases.
