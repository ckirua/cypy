# Cython recipes (cimport-only modules)

Public Python examples cannot wrap these APIs honestly. Use the corresponding `src/cypy/cy*.pxd` from a `.pyx`:

```cython
from cypy cimport list_len, bytes_eq   # package barrel (__init__.pxd)
from cypy.cyerr cimport *              # submodule — see each .pxd
# cyerr / cymem / cythread / cyatomic / cylongintrepr / cyref
# cygetargs / cyceval / cypystate / cypylifecycle / cypyport / cyversion
```

Out-of-tree barrel smoke: [`../cimport_ext/`](../cimport_ext/).

Full inventory and safety notes: `docs/modules/NNN_cy{name}.md`.

## Ownership (public + cimport)

See [`borrow_vs_owned.md`](borrow_vs_owned.md) (DX-05) for `dict_get`/`dict_get_ref`, `list_get`/`list_get_checked`, and borrowed `char*` notes.
