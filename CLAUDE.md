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

- **Closed-form kinematic split DERIVED** (2026-06-16): kinematic row
  `PART`$\to$`PASS`. Key result $M_\text{eff} = \tfrac43(I-\hat n_*\hat
  n_*^T) = \tfrac43 P_\perp$, so the dispersion depends only on
  $\mathbf{k}_\perp$ and $|H_\text{RGB}|^2 = 1-\tfrac43|\mathbf{k}_\perp|^2$.
  Exact eigenphase dispersion $\tan\theta = \tan(\omega/2)/|H_\text{RGB}|$;
  closed-form group velocity giving split $\Delta v = \tfrac23\sin\omega\,
  |\mathbf{k}|$ (massive sector, angular law $\sin\alpha$) plus the
  $\omega$-independent dispersion-curvature split $4/3$ vs $0$ (photon +
  massive). Per the framing decision, the claim names **both** observables.
  Verified by `src/experiments/exp_02_closed_form_split_check.py` (10/10
  checks: identities $<10^{-12}$, speed coeffs $<10^{-5}$). Derivation in
  `notes/closed_form_speed_split.md`. Section
  `paper/sections/kinematic_channel.tex` (wired into `main.tex`, builds
  clean). Paper~I now cited via `menendez2026geometryfirst` (DOI
  10.5281/zenodo.20613677, corrected on title page).

**Next concrete action:** draft the **abstract and introduction** stating
the two channels and the multi-channel concordance (P9); then attack the
**gauge-sector channel** ($\mathbf{Q}$ eigenvalues $\{4,4,16\}$, currently
`STUB`).

### TODO / Open Items

- **[BLOCKING -- TACTICAL] Falsifiability magnitude + SME dim-6 mapping.**
  Paper~III (tidal ionization) was deferred in favour of Paper~IV *on the
  expectation that the optical-axis birefringence is falsifiable*; this
  item gates whether that ordering holds. Full analysis (literature-grounded
  via a verified multi-source search) in
  `notes/falsifiability_and_sme_mapping.md`. **SME mapping DONE:** the
  kinematic channel is the CPT-even, nonbirefringent, mass-dim-6 photon
  sector ($c^{(6)}_{(I)jm}$); the predicted pattern is parameter-free
  (axis $(1,1,-1)$; monopole + axis-aligned quadrupole, fixed ratio, no
  $j{=}4$; on-axis flat to all orders) even though the scale floats with
  $a$. **Key numbers:** binding bound is LHAASO GRB 221009A
  ($E_{\rm QG2}>7\times10^{11}$ GeV), giving surviving window $\ell_P
  \lesssim a \lesssim 3\times10^{-28}$ m. Frontier-detectable only near the
  top of that window; Planck calibration is ~14-23 orders below current
  reach. **Correction found:** Paper~I P7's $a\lesssim7.6\times10^{-19}$ m
  is wrong by ~9 orders (implies an absurd $260$ GeV cutoff, excluded by
  observed PeV photons) -- feed back to Paper~I errata. **Remaining to
  settle the tactical call:** (a) the decisive falsifier is **P9
  concordance** -> do the **gauge-sector channel** ($\mathbf{Q}$ {4,4,16},
  `STUB`); note it maps to the *birefringent* $k^{(6)}$ coefficients, which
  polarimetry bounds ~25+ orders tighter than dispersion -- **potentially a
  far sharper falsifier than the kinematic channel**; (b) reconcile P7's
  "two arrival peaks" photon claim (corrected in `rem:photon_limit`); (c)
  frame-fixing (is the lattice frame the CMB frame?). Until (a)-(c)
  resolve, the Paper~III deferral is a bet, not a settled decision -- though
  the gauge-sector birefringent handle now looks like the strongest reason
  to expect it pays off.

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
| Kinematic birefringence along $(1,1,-1)$ | PASS | Closed-form ordinary/extraordinary split. $M_\text{eff}=\tfrac43(I-\hat n_*\hat n_*^T)$; group-velocity split $\Delta v=\tfrac23\sin\omega\,\|k\|$ (massive) + $\omega$-independent curvature split $4/3$ vs $0$ (photon+massive). `exp_01` (axis + A=1 survival) and `exp_02` (analytic identities $<10^{-12}$, speed coeffs $<10^{-5}$). Derivation: `notes/closed_form_speed_split.md`. |
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
- `notes/closed_form_speed_split.md` -- the closed-form
  ordinary/extraordinary speed split derivation (DERIVED + verified):
  $M_\text{eff}=\tfrac43 P_\perp$, eigenphase dispersion, group-velocity
  and dispersion-curvature splits. Flips the kinematic audit row to
  `PASS`. Verification: `src/experiments/exp_02_closed_form_split_check.py`;
  section: `paper/sections/kinematic_channel.tex`.
- `notes/falsifiability_and_sme_mapping.md` -- ANALYSIS (blocks a tactical
  decision): is the birefringence practically falsifiable? SME mapping DONE
  (nonbirefringent dim-6 $c^{(6)}_{(I)jm}$; parameter-free pattern; window
  $a\lesssim3\times10^{-28}$ m from LHAASO, correcting Paper~I's
  $10^{-19}$ m by ~9 orders). Decisive falsifier is P9 concordance via the
  gauge sector (maps to *birefringent* $k^{(6)}$, polarimetry-tight). See
  the BLOCKING TODO above.
