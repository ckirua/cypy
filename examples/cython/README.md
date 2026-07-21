# Cython recipes (cimport-only modules)

Public Python examples cannot wrap these APIs honestly. Use the corresponding `src/cypy/cy*.pxd` from a `.pyx`:

```cython
from cypy.cyerr cimport *          # example pattern — see each .pxd
# cyerr / cymem / cythread / cyatomic / cylongintrepr / cyref
# cygetargs / cyceval / cypystate / cypylifecycle / cypyport / cyversion
```

Full inventory and safety notes: `docs/modules/NNN_cy{name}.md`.

## Ownership (public + cimport)

See [`borrow_vs_owned.md`](borrow_vs_owned.md) (DX-05) for `dict_get`/`dict_get_ref`, `list_get`/`list_get_checked`, and borrowed `char*` notes.
