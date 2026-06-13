<!-- markdownlint-disable MD022 MD025 MD033 MD060 -->
# CLAUDE.md -- Working Brief for Claude Code

> Project: Paper~IV of the A=1 Discrete Causal Lattice series --
> Optical-Axis Birefringence on the A=1 Discrete Causal Lattice

This file is the project memory for Claude Code. Keep it updated so a
new conversation can continue work without the full chat history.

---

## CURRENT STATUS (2026-06-13) -- v0.1-DRAFT

Repository freshly provisioned on 2026-06-13 from `dcl-paper-template`
(paper-only template; no companion experiment code). Takes up
follow-on item~\#14 ("Balanced Equations and Birefringent Channels")
of Paper~I's `notes/follow_on_implications.md` catalogue. The physics
originates in Paper~I: the frame-invariance step of the Dirac
derivation makes the lattice's response wavevector-direction
dependent, i.e. birefringent along the optical axis $(1,1,-1)$.

What is in place (v0.1-DRAFT):

- Scaffold copied + metadata customized (title, author, CITATION.cff,
  packages.tex PDF metadata, LICENSE, README).
- Title page and abstract/section stubs from the template; body not
  yet written.
- **Audit table seeded** with the three real claim rows (kinematic;
  gauge-sector; concordance), replacing the template examples.
- **First companion experiment landed** (the template started
  paper-only): `src/experiments/exp_01_optical_axis_isotropy.py` +
  `.md`, data in `data/`, run 2026-06-12 on `dcl_core` v0.2.2. It
  answers the load-bearing observability question for the kinematic
  channel -- *does the per-tick A=1 renormalization wash the
  $(1,1,-1)$ anisotropy out of observable amplitudes?* **No.** An
  isotropic pulse flattens perpendicular to $(1,1,-1)$ (spread ratio
  $v_\parallel/v_\perp \to 0.01$), flat-axis alignment $=1.0000$,
  $\omega$-independent, on **both** engines (integer `core3d` exact
  A=1, and float `core` with `enforce_unity_spinor`) -- so the
  survival is not a single-scheme artefact, and the optical axis is
  confirmed $(1,1,-1)$ in observables.  Kinematic audit row flipped
  `STUB`$\to$`PART`.  See
  `notes/optical_axis_renormalization_test.md`.

**Next concrete action:** derive the **closed-form
ordinary/extraordinary speed split** along $(1,1,-1)$ (from
$|H_\text{RGB}|$ and the propagator eigenphases) -- the remaining step
that flips the kinematic row `PART`$\to$`PASS`; then draft the abstract
and introduction stating the two channels and the multi-channel
concordance (P9).

> **Working title** -- "Optical-Axis Birefringence on the A=1
> Discrete Causal Lattice"; confirm/refine before first deposit.

---

## What This Project Is

Paper~IV develops the A=1 lattice's intrinsic **optical-axis
birefringence**: light propagating along the optical axis
$\mathbf{V}_1+\mathbf{V}_2+\mathbf{V}_3 = (1,1,-1)$ splits into
ordinary/extraordinary modes whose speeds differ in a calculable,
closed-form way. The effect is a *consequence* of Paper~I's geometry,
not a new postulate. The $(1,1,-1)$ birefringence is one of the
series' **standing falsifiable predictions** (it appears in the
program claim map); this paper works it to closed form. It is
**distinct from** follow-on #11 (*vacuum* birefringence as a
photon-photon session interaction).

---

## Paper Title and Theme

**Title (working):** Optical-Axis Birefringence on the A=1 Discrete
Causal Lattice: Kinematic and Gauge-Sector Anisotropy along
$(1,1,-1)$.

**Core theme / framing:** the lattice is a *birefringent medium* whose
optical axis is fixed by its geometry; predicting *where* and *how
much* the ordinary/extraordinary split occurs turns a structural fact
about the substrate into an observable signature. Per the program's
falsifiability stance, claim only what is derived; route falsifiability
claims through the audit table / claim map, not the prose.

---

## Audit Table Status

| Row | Status | What it claims |
|---|---|---|
| Kinematic birefringence along $(1,1,-1)$ | PART | Closed-form ordinary/extraordinary split along the optical axis. `exp_01` numerically confirms the axis $(1,1,-1)$ and that the anisotropy survives A=1 renormalization (both engines); closed-form split pending. |
| Gauge-sector birefringence ($\mathbf{Q}$ eigenvalues $\{4,4,16\}$) | STUB | Anisotropy in the gauge sector. |
| Multi-channel concordance (P9) | STUB | The kinematic and gauge-sector channels predict a shared optical axis. |

Mirror of `paper/sections/audit_table.tex` -- update this table when
the audit table changes. The claim-auditor agent
(`.claude/agents/claim-auditor.md`) treats `audit_table.tex` as the
authority; this section is for quick orientation only.

---

## Conventions

- **Status legend.** `PASS` / `PART` / `STUB` / `FAIL` (defined in the
  front-matter of `paper/main.tex`).
- **File naming.** Sections: `paper/sections/<topic>.tex`. Figures:
  `paper/figures/<name>.{tex,pdf,png}`. Notes: `notes/<topic>.md`.
- **Cross-references.** Always `\label{}` + `\ref{}` / `\autoref{}`,
  never hard-coded numbers (`sec:`, `eq:`, `fig:`, `tab:`, `thm:`).
- **Bibliography.** All cites flow through
  `paper/paper-bib/references.bib`; `\bibliographystyle{unsrt}`.

---

## Release flow

See `release_notes/README.md`. Summary: CI green -> update
`CITATION.cff` -> draft `release_notes/vX.Y.md` -> **deposit on Zenodo
first** (DOI lands in title-page `\thanks{}` + `CITATION.cff`) ->
commit version bump -> tag `vX.Y` -> push tag -> GitHub Release.

---

## What NOT to Change

- The MIT (`LICENSE`) / CC BY 4.0 (prose) split.
- The series identifiers in the title-page `\thanks{}` (Paper~IV,
  follow-on #14, links to Papers I & II).

---

## Notes Index

`notes/README.md` -- conventions for notes/.

- `notes/optical_axis_renormalization_test.md` -- numerical
  confirmation (STABLE) that the kinematic $(1,1,-1)$ anisotropy
  survives A=1 renormalization in observables and that the optical axis
  is $(1,1,-1)$; backs the kinematic audit row. Experiment:
  `src/experiments/exp_01_optical_axis_isotropy.py`.
