# External barrel `cimport` smoke

Regression check that **`from cypy cimport …`** (package barrel via `__init__.pxd`) and submodule paths both cythonize against an **installed** `cypy` (editable or wheel).

## Prerequisites

```bash
# from repo root
pip install -e . --no-build-isolation
# or: pip install dist/cypy-*.whl
```

## Build + assert

```bash
# from repo root
bash scripts/smoke_barrel_cimport.sh
```

Or manually:

```bash
cd examples/cimport_ext
python setup.py build_ext --inplace
python -c "import demo; assert demo.check_barrel(); assert demo.check_submodule() == 2"
```

`demo.pyx` uses barrel (`bytes_eq`, `list_len`, `str_eq`) and `from cypy.cybytes cimport bytes_len`.
