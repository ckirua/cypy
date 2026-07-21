## Short

<!-- 1–2 sentences: what this PR does -->

## Brief

- **Queue:** Order `NN` · module `cy{name}` · presence: present / absent
- **Change:** index only / helpers / benches (pick)
- **Tallies:** APPROVED _ · APPROVED (cimport) _ · TODO _ · REJECTED _ · ONGOING _
- **Lifecycle:** stub / indexed / measuring / decided
- **Branch:** `mod/NN-cy{name}`

## Detailed

### Inventory / decisions

<!-- Highlights: what was APPROVED, APPROVED (cimport), or REJECTED and why; link docs/modules/NNN_cy{name}.md -->

### Benchmarks

<!-- Required when helpers exist or changed. Else write: n/a (absent index) or n/a (docs-only). -->

| Case | Tier | Ratio (cypy/baseline) | Verdict | Notes |
|------|------|-------------------------|---------|-------|
| primary … | A / B | 0.xx | pass / fail / n/a | N=… RUNS=… |

- **Harness:** `bench/cy{name}_bench.py`
- **Tracker evidence:** `docs/modules/NNN_cy{name}.md` (results table + conclusions)
- **Env:** CPython … · platform … · git …

### Follow-ups

<!-- Tier B / follow-ups — do not start next module in this PR -->

### Before merge (checklist)

- [ ] Try-all **+ depth** done
- [ ] **`docs/modules/NNN_cy{name}.md` updated** with Bench results + Experiment conclusions (**no skip**)
- [ ] Public `cpdef` PEP 257 one-liners in `cy{name}.pyi` (no Args/Returns); `.pxd` lean
- [ ] Exports match APPROVED vs APPROVED (cimport)
- [ ] Update `docs/modules/NNN_*.md` if surface / decisions changed

---

**Merge:** maintainers may merge when the Before-merge checklist is green; external PRs need review.
