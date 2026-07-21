# Release checklist

Ship a tagged `cypy` release from `main`. Version is sourced from [`src/cypy/__about__.py`](../src/cypy/__about__.py) (`pyproject.toml` dynamic version).

## Compatibility (0.x → 1.0)

**Locked policy (API refactor): Strategy B — soft then hard.**

| Change | Before 1.0 (0.x) | After 1.0 |
|--------|------------------|-----------|
| Add public symbol | OK | OK (minor) |
| Rename with dual alias | Preferred (`0.2` soft window) | Required ≥1 minor |
| Remove / rename without alias | OK if noted in tag notes | Forbidden without major |
| Change semantics of existing name | Avoid; new name instead | Major only |
| Promote cimport → public | OK | Minor |
| Demote public → cimport / drop from root | Soft-deprecate then remove in `0.3` | Major + long deprecation |
| Identity alias (`old is new`) | OK | OK during window |
| Semantic twin (`dlen` vs `dsize`) | **Keep both** — never alias as identity | Same |

**Version sketch:** `0.2` soft aliases + curated Core messaging → `0.3` hard trim of deprecated root names → `1.0` freeze **Core** public + documented cimport contracts. Protocols/Runtime may still evolve under minors after 1.0.

**Current (`1.0.0`):** **Core** public (`cypy.__all__` + `cypy.hot`) and documented
cimport contracts are frozen. Soft root aliases were trimmed in `0.3`. Preferred
names only on `cypy`; ledger + `__getattr__` hints: [`cypy.compat`](../src/cypy/compat.py).
Export gate: [`scripts/check_exports.py`](../scripts/check_exports.py).
Protocols / Runtime remain **provisional** under post-1.0 minor policy (see
[`CHANGELOG.md`](../CHANGELOG.md) / [`COVERAGE.md`](../COVERAGE.md)).

**Alternative (not default):** Strategy A — single breaking `0.2` with **no** aliases (only if maintainers confirm near-zero external pins). Do not mix A and B halfway. **Chosen path was Strategy B** (soft then hard); do not reopen A for 1.x.

**Always:** update `use-cypy` skill, examples, and `__all__`/`.pyi` in the **same** rename wave; bare `cystr` names need extra care. Naming so far: **N2** `*_cstr`, **N6** spelling, **N1** word-prefix, **N5** `str_*`/`ansi_*`, **N3+N4** check/len conventions (docs + CI). Soft aliases **removed in 0.3**.

### 0.3 hard-trim checklist

1. [x] For each `COMPAT_MAP` soft name: drop root identity alias / dual import; update `.pxd` / `.pyi` duals.
2. [x] Short-lived `__getattr__` raises `AttributeError` with `soft_alias_removal_hint(name)`.
3. [x] Demote DEMOTE_ROOT soft-alias row (letter/bare/`*_string`/…); family demotions remain non-Core (not in `__all__`).
4. [x] Keep **semantic twins** (`*_len` / `*_size`).
5. [x] Bump to `0.3.0`; refresh skill pin + examples (preferred-only).
6. [x] Re-run `scripts/check_exports.py` + examples + grader (CI / local smoke).

### 1.0 Core freeze checklist

1. [x] Freeze Core public set (`cypy.__all__` + `cypy.hot`) and document cimport contracts in COVERAGE / module trackers.
2. [x] Changelog: close “Provisional (non-Core)” — Protocols/Runtime under post-1.0 minor policy.
3. [x] Tag `v1.0.0` (after merge to `main`).

## Before tagging

| Step | Check |
|------|-------|
| 1 | On latest `main`; working tree clean |
| 2 | If any `docs/modules/` Lifecycle lines changed: `python scripts/grade_trackers.py` → **53/53 A** |
| 3 | Local smoke: `pip install -e . --no-build-isolation` then `from cypy.hot import bytes_len, dict_get, str_len` |
| 4 | Examples: `for f in examples/py*.py examples/wrap_ansi.py; do python "$f"; done` |
| 5 | Export/compat: `python scripts/check_exports.py` |
| 6 | Confirm [`future/MONKEY.md`](future/MONKEY.md) is **not** wired into `src/cypy` |
| 7 | Bump `__about__.__version__` (PEP 440), e.g. `1.0.0` |
| 8 | Update [`CHANGELOG.md`](../CHANGELOG.md) / [`README.md`](README.md) status / [`COVERAGE.md`](../COVERAGE.md) if surface/policy changed |

## Tag and GitHub Release

```bash
git checkout main && git pull
# after version bump is on main:
git tag -a "vX.Y.Z" -m "cypy vX.Y.Z"
git push origin "vX.Y.Z"
gh release create "vX.Y.Z" --title "cypy vX.Y.Z" --notes-file - <<'EOF'
## Highlights
- …

## Requires
- Python ≥ 3.14

## Install
```bash
pip install "git+https://github.com/ckirua/cypy.git@vX.Y.Z"
```
EOF
```

## Artifacts / PyPI (optional)

```bash
pip install build twine
python -m build
twine check dist/*
# optional: twine upload --repository testpypi dist/*
# optional: twine upload dist/*
```

PyPI publish is **optional** for Phase 5 exit if git-tag install works. Mark deferred in QUEUE when secrets / name availability block upload.

## Post-release verify

```bash
pip install "cypy @ git+https://github.com/ckirua/cypy.git@vX.Y.Z"
python -c "from cypy.hot import bytes_len; assert bytes_len(b'ok') == 2"
```

Portable builds are the default (`-O3` only). Contributors may set `CPY_NATIVE=1` for local tuned benches — do **not** require it for release artifacts.
