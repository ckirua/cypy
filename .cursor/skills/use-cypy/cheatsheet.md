# cypy consumer cheatsheet

Read only when the high-value table in `SKILL.md` is not enough. Prefer examples under `examples/py*.py`.

## Core containers / strings (public)

| Module | Example script | Typical symbols |
|--------|----------------|-----------------|
| cytuple | `examples/pytuple.py` | `tuple_check`, `tuple_len`, `tuple_get`, `tuple_pack2`… |
| cybytes | `examples/pybytes.py` | `bytes_len`, `bytes_contains`, `bytes_eq`, `bytes_check` |
| cydict | `examples/pydict.py` | `dict_get`, `dict_set`, `dict_pop`, `dict_len`, `dict_contains` |
| cylist | `examples/pylist.py` | `list_len`, `list_get`, `list_append`, … |
| cyset | `examples/pyset.py` | `set_contains`, `set_add`, `set_len`, … |
| cystr | `examples/pystr.py` | `str_len`, `str_eq`, `str_contains`, `str_startswith` |
| cyunicode | `examples/pyunicode.py` | `uutf8_bytes`, `uintern` |
| cyansi | `examples/wrap_ansi.py` | `ansi_wrap`, `ansi_fg8`, `ansi_strip` |
| cygc | `examples/pygc.py` | `gc_collect`, `gc_is_enabled` |

## Overlap playbooks (choice, not new APIs)

| Decision | Example |
|----------|---------|
| mapping vs dict | `examples/py_overlap_mapping_vs_dict.py` |
| sequence vs list/tuple | `examples/py_overlap_sequence_vs_list.py` |
| str value ops vs unicode encode/intern | `examples/py_overlap_str_vs_unicode.py` |

Facades: `cypy.containers`, `cypy.buffers`, `cypy.protocols` (discovery); prefer `cypy.hot` for micro-opts.

## Other public modules

See `examples/README.md` Orders 14–21, 23–27, 29–36, 39–46, 51, 53 (`pybytearray`, `pyarray`, `pymemoryview`, `pybuffer`, `pysequence`, `pyslice`, `pybool`, `pylong`, `pyfloat`, `pycomplex`, `pynumber`, `pyobject`, `pytype`, `pyfunction`, `pymethod`, `pymodule`, `pyiterator`, `pyiterobject`, `pygenobject`, `pycellobject`, `pydescr`, `pycodecs`, `pydatetime`, `pycontextvars`, `pymapping`, `pymarshal`, `pyfileobject`, `pypycapsule`, `pyweakref`, `pyconversion`, `pytime`).

## Cimport-only (Cython recipes, not Python)

Orders 10–13, 22, 28, 38, 47–50, 52: `cyerr`, `cymem`, `cythread`, `cyatomic`, `cylongintrepr`, `cyref`, `cygetargs`, `cyceval`, `cypystate`, `cypylifecycle`, `cypyport`, `cyversion`.

Use `cimport` from `.pyx` only — see `examples/cython/README.md`.

## n/a

- `cyinstance` — classic-class ABI gone on 3.14; no helpers.
