# Changelog

All notable changes to `cypy` are documented here. Version from
[`src/cypy/__about__.py`](src/cypy/__about__.py).

## [1.42.0] — 2026-07-22 — `context_eq` + Runtime eq stretch

### Added

- **`context_eq`** (`cycontextvars`): ``Context`` value equality — identity +
  richcompare (same as ``Context.__eq__``). Soft ``ctxeq``. On ``cypy``
  (not ``hot``). ``ContextVar`` / ``Token`` stay identity → use ``obj_eq``.
- **`docs/EQ_RUNTIME.md``**: Runtime/embedding ``*_eq`` checklist (#44) —
  skip/done; no mass identity wrappers.

## [1.41.0] — 2026-07-22 — `bytes_bytearray_eq`

### Added

- **`bytes_bytearray_eq`** (`cybytes`): cross-type ``bytes`` ↔ ``bytearray``
  content equality — identity / len + ``memcmp`` on ``AS_STRING`` (either
  order; same-type also works). Soft ``bba_eq``. On ``cypy`` /
  ``cypy.buffers`` (not ``hot``; prefer typed ``bytes_eq`` / ``bytearray_eq``
  there). Cross-link: ``buf_eq`` is buffer-protocol / views, not this.

## [1.40.0] — 2026-07-22 — `range_eq`

### Added

- **`range_eq`** (`cyrange`): ``range`` equality — identity +
  richcompare (same as ``range.__eq__``; empty / equivalent spans).
  Soft ``rqeq``. On ``cypy`` / ``cypy.containers`` (not ``hot``).

## [1.39.0] — 2026-07-22 — `deque_eq`

### Added

- **`deque_eq`** (`cydeque`): `collections.deque` equality — identity +
  richcompare (same as ``deque.__eq__``). Soft ``dqeq``. On ``cypy`` /
  ``cypy.containers`` (not ``hot``).

## [1.38.0] — 2026-07-22 — `func_eq` / `method_eq` / `mod_eq` / `gen_eq` / `iter_eq`

### Added

- **`func_eq`** (`cyfunction`): function equality via identity (``a is b``) —
  CPython ``object.__eq__``. Soft ``funceq``. On ``cypy`` (not ``hot``).
- **`method_eq`** (`cymethod`): bound-method equality via identity short-circuit
  + ``PyObject_RichCompareBool`` (``Py_EQ``) — CPython ``method_richcompare``
  (same function + ``__self__``; not identity). Soft ``methodeq``. On ``cypy``
  (not ``hot``).
- **`mod_eq`** (`cymodule`): module equality via identity (``a is b``) —
  CPython ``object.__eq__``. Soft ``modeq``. On ``cypy`` (not ``hot``).
- **`gen_eq`** (`cygenobject`): generator equality via identity (``a is b``) —
  CPython ``object.__eq__``. Soft ``geneq``. On ``cypy`` (not ``hot``).
- **`iter_eq`** (`cyiterator`): iterator equality via identity (``a is b``) —
  typical CPython ``object.__eq__``. Soft ``itereq``. On ``cypy`` (not ``hot``).

### Notes

- **`code_eq` skipped:** no ``cycode`` module (``cycodecs`` is codecs); structural
  code equality would need a dedicated module — out of scope for this batch.

## [1.37.0] — 2026-07-22 — `weakref_eq`

### Added

- **`weakref_eq`** (`cyweakref`): weakref/proxy equality via identity
  short-circuit + ``PyObject_RichCompareBool`` (``Py_EQ``) — CPython
  ``weakref_richcompare`` (referent ``==`` when both alive; identity when
  either is dead). Soft ``weakrefeq``. On ``cypy`` (not ``hot`` — Runtime;
  validate win before promoting).

## [1.36.0] — 2026-07-22 — `capsule_eq`

### Added

- **`capsule_eq`** (`cypycapsule`): capsule equality via identity (``a is b``) —
  CPython uses ``object.__eq__``; same pointer/name does not make distinct
  capsules equal. Soft ``capsuleeq``. On ``cypy`` (not ``hot`` — Runtime;
  validate win before promoting).

## [1.35.0] — 2026-07-22 — `cell_eq`

### Added

- **`cell_eq`** (`cycellobject`): cell equality via identity short-circuit +
  ``PyObject_RichCompareBool`` (``Py_EQ``) — content equality (CPython
  ``cell_richcompare``; empty↔empty True; not identity). Soft ``celleq``. On
  ``cypy`` (not ``hot`` — Runtime; validate win before promoting).

## [1.34.0] — 2026-07-22 — `type_eq`

### Added

- **`type_eq`** (`cytype`): type-object equality via identity (``a is b``) —
  CPython ``type_richcompare`` default; not Python ``==`` when a metaclass
  overrides ``__eq__``. Soft ``typeeq`` (``teq`` remains ``tuple_eq``). On
  ``cypy`` (not ``hot`` — Runtime; validate win before promoting).

## [1.33.0] — 2026-07-22 — `obj_eq`

### Added

- **`obj_eq`** (`cyobject`): generic object equality via ``PyObject_RichCompareBool``
  (``Py_EQ``) — identity short-circuit (incl. ``nan is nan`` → True; same as the
  C-API, not always Python ``==`` for floats). Prefer typed ``*_eq`` when known.
  Soft ``oeq``. On ``cypy`` / ``cypy.protocols`` (not ``hot`` — validate win
  before promoting).

## [1.32.0] — 2026-07-22 — `dt_timedelta_eq`

### Added

- **`dt_timedelta_eq`** (`cydatetime`): timedelta equality — identity short-circuit;
  exact ``timedelta`` pairs compare days/seconds/microseconds; else richcompare
  (subtypes — Python ``==`` parity). Soft ``dteq_delta``. On ``cypy`` (not
  ``hot`` — Runtime; validate win before promoting).

## [1.31.0] — 2026-07-22 — `dt_datetime_eq`

### Added

- **`dt_datetime_eq`** (`cydatetime`): datetime equality — identity short-circuit;
  exact naive ``datetime`` pairs compare year/month/day/hour/minute/second/
  microsecond; else richcompare (subtypes / aware/naive / offset / date↔datetime
  Python ``==`` parity; fold ignored). Soft ``dteq_dt``. On ``cypy`` (not
  ``hot`` — Runtime; validate win before promoting).

## [1.30.0] — 2026-07-22 — `dt_time_eq`

### Added

- **`dt_time_eq`** (`cydatetime`): time equality — identity short-circuit; exact
  naive ``time`` pairs compare hour/minute/second/microsecond; else richcompare
  (subtypes / aware/naive / offset Python ``==`` parity; fold ignored). Soft
  ``dteq_time``. On ``cypy`` (not ``hot`` — Runtime; validate win before
  promoting).

## [1.29.0] — 2026-07-22 — `dt_date_eq`

### Added

- **`dt_date_eq`** (`cydatetime`): date equality — identity short-circuit; exact
  ``date`` pairs compare year/month/day; else richcompare (subtypes /
  ``date`` vs ``datetime`` Python ``==`` parity). Soft ``dteq_date``. On
  ``cypy`` (not ``hot`` — Runtime; validate win before promoting).

## [1.28.0] — 2026-07-22 — `slice_eq`

### Added

- **`slice_eq`** (`cyslice`): slice equality — identity short-circuit +
  richcompare (same semantics as ``slice.__eq__``; compares start/stop/step
  objects, so ``None`` bounds are not normalized to ``0``/``1``). Soft ``sleq``.
  On ``cypy`` / ``cypy.buffers`` (not ``hot`` — completeness / buffer-adjacent).

## [1.27.0] — 2026-07-22 — `num_eq`

### Added

- **`num_eq`** (`cynumber`): abstract number equality via
  ``PyObject_RichCompare`` (Python ``==`` parity, including NaN != NaN even for
  the same object — not ``RichCompareBool``, which identity-shortcuts). Prefer
  typed ``long_eq`` / ``float_eq`` / ``complex_eq`` / ``bool_eq`` when known.
  Soft ``neq_num``. On ``cypy`` / ``cypy.protocols`` (not ``hot``).

## [1.26.0] — 2026-07-22 — `complex_eq`

### Added

- **`complex_eq`** (`cycomplex`): complex/value equality with Python parity
  (NaN on either real or imag => unequal even for the same object;
  ``+0.0 == -0.0`` on each part). Complex/complex uses C ``double ==`` on
  real/imag; mixed types use ``PyObject_RichCompare`` (not ``RichCompareBool``,
  which identity-shortcuts same-object NaN parts). Soft ``ceq``. On ``cypy``
  (not ``hot`` — clarity / scalar completeness).

## [1.25.0] — 2026-07-22 — `float_eq`

### Added

- **`float_eq`** (`cyfloat`): float/value equality with Python parity (NaN != NaN
  even for the same object, ``+0.0 == -0.0``). Float/float uses C ``double ==``;
  mixed types use ``PyObject_RichCompare`` (not ``RichCompareBool``, which
  identity-shortcuts NaN). Soft ``feq``. On ``cypy`` (not ``hot`` — clarity /
  scalar completeness).

## [1.24.0] — 2026-07-22 — `bool_eq`

### Added

- **`bool_eq`** (`cybool`): boolean/value equality — identity short-circuit +
  richcompare (same semantics as ``==``; True/False singletons hit identity).
  Soft ``booleq``. On ``cypy`` (not ``hot`` — clarity / scalar completeness).

## [1.23.0] — 2026-07-22 — `long_eq` / `int_eq`

### Added

- **`long_eq`** / **`int_eq`** (`cylong`): integer equality — identity short-circuit +
  richcompare (same semantics as ``==``). Preferred ``long_eq``; ``int_eq`` is a
  discoverability alias. Soft ``loeq`` / ``ieq``. On ``cypy`` (not ``hot`` —
  small-int ``==`` already specializes).

## [1.22.0] — 2026-07-22 — `map_eq`

### Added

- **`map_eq`** (`cymapping`): abstract mapping equality — identity/size
  short-circuit + richcompare (same semantics as ``==``). Soft ``mapeq``. Prefer
  typed ``dict_eq`` when known. On ``cypy`` / ``cypy.protocols``.

## [1.21.0] — 2026-07-22 — `seq_eq`

### Added

- **`seq_eq`** (`cysequence`): abstract sequence equality — identity/size
  short-circuit + richcompare (same semantics as ``==``). Soft ``sqeq``. Prefer
  typed ``list_eq`` / ``tuple_eq`` when known. On ``cypy`` / ``cypy.protocols``.

## [1.20.0] — 2026-07-22 — `frozenset_eq`

### Added

- **`frozenset_eq`** (`cyset`): typed ``frozenset`` equality — identity/size
  short-circuit + richcompare (same semantics as ``==``). Soft ``fseteq``. On
  ``cypy`` / ``cypy.containers``.

## [1.19.0] — 2026-07-22 — `set_eq`

### Added

- **`set_eq`** (`cyset`): typed ``set`` equality — identity/size short-circuit +
  richcompare (same semantics as ``==``). Soft ``seteq`` (not ``seq`` — avoids
  ``seq_*`` / ``sq*`` confusion). On ``cypy`` / ``cypy.containers``.

## [1.18.0] — 2026-07-22 — `dict_eq`

### Added

- **`dict_eq`** (`cydict`): typed ``dict`` equality — identity/size short-circuit +
  richcompare (same semantics as ``==``). Soft ``deq``. On ``cypy`` /
  ``cypy.containers``.

## [1.17.0] — 2026-07-22 — `tuple_eq`

### Added

- **`tuple_eq`** (`cytuple`): typed ``tuple`` equality — identity/len + richcompare.
  Soft ``teq``. On ``cypy`` / ``cypy.containers``.

## [1.16.0] — 2026-07-22 — `list_eq`

### Added

- **`list_eq`** (`cylist`): typed ``list`` equality — identity/len short-circuit +
  richcompare (same semantics as ``==``). Soft ``leq``. On ``cypy`` /
  ``cypy.containers``.

## [1.15.0] — 2026-07-22 — `uutf8_eq`

### Added

- **`uutf8_eq`** (`cyunicode`, **cimport-only**): compare UTF-8 byte views of two
  ``str`` via ``uutf8_and_size`` + ``memcmp`` (embedded NUL OK). Borrowed
  pointers must not outlive the arguments.

## [1.14.0] — 2026-07-22 — `str_lt` / `str_le` / `str_gt` / `str_ge`

### Added

- **`str_lt` / `str_le` / `str_gt` / `str_ge`** (`cystr`): typed ordering
  predicates via ``str_cmp``. Soft ``slt``/``sle``/``sgt``/``sge``. On ``cypy``
  (not ``hot``).

## [1.13.0] — 2026-07-22 — `str_cmp`

### Added

- **`str_cmp`** (`cystr`): three-way typed ``str`` compare → ``-1`` / ``0`` / ``1``
  via ``PyUnicode_Compare`` (identity short-circuit). Soft aliases ``str_compare`` /
  ``scmp`` (COMPAT only). On ``cypy`` (not ``hot``).

## [1.12.0] — 2026-07-22 — `unicode_eq`

### Added

- **`unicode_eq`** (`cyunicode`): discoverability alias of ``str_eq`` (same
  semantics; no divergent UCS path). Soft ``ueq``. On ``cypy``.

## [1.11.0] — 2026-07-22 — `bytes_endswith`

### Added

- **`bytes_endswith`** (`cybytes`): typed suffix test — empty suffix True,
  longer-than-`s` False, else tail `memcmp`. Soft `bendswith`. On `cypy` /
  `cypy.hot` / `cypy.buffers` (mirrors `str_endswith`).

## [1.10.0] — 2026-07-22 — `bytes_startswith`

### Added

- **`bytes_startswith`** (`cybytes`): typed prefix test — empty prefix True,
  longer-than-`s` False, else `memcmp` on `PyBytes_AS_STRING`. Soft
  `bstartswith`. On `cypy` / `cypy.hot` / `cypy.buffers` (mirrors
  `str_startswith`).

## [1.9.0] — 2026-07-22 — `bytearray_contains`

### Added

- **`bytearray_contains`** (`cybytearray`): typed `bytearray` membership for a
  `bytes` needle — same small-buffer `memchr`/`memmem` / large-buffer `in`
  hybrid as `bytes_contains`. Soft `bacontains`. On `cypy` / `cypy.hot` /
  `cypy.buffers`.

## [1.8.0] — 2026-07-22 — `buf_eq`

### Added

- **`buf_eq`** (`cybuffer`): abstract buffer-protocol equality — acquire
  `PyBUF_FULL_RO` views, format/size/shape gates, C-contiguous `memcmp` fast
  path, non-contiguous → `memoryview` richcompare. Soft alias `buffer_eq`
  (COMPAT only). On `cypy` / `cypy.buffers` (not `hot` — heavier than typed
  `bytes_eq`).

## [1.7.0] — 2026-07-22 — `bytearray_ne` / `array_ne` / `memoryview_ne`

### Added

- **`bytearray_ne`**, **`array_ne`**, **`memoryview_ne`**: typed inequality siblings of
  the corresponding `*_eq` helpers (`not *_eq` / soft `bane` / `ayne` / `mvne`).
  Same contig/format rules as `*_eq`. On `cypy` / `cypy.hot` / `cypy.buffers`
  (mirrors `bytes_ne` / `str_ne`).

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
