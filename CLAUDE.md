<!-- markdownlint-disable MD022 MD025 MD033 MD060 -->
# CLAUDE.md -- Working Brief for Claude Code

> Project: Paper~IV of the A=1 Discrete Causal Lattice series --
> Optical-Axis Birefringence on the A=1 Discrete Causal Lattice

This file is the project memory for Claude Code. Keep it updated so a
new conversation can continue work without the full chat history.

---

## CURRENT STATUS (2026-06-16) -- v0.1-DRAFT

**Resuming? Read the ⏳ WAITING ON block below** -- the gauge-sector
`exp_03` is blocked on a `dcl_core` core3d v0.3.0 engine upgrade
(owner-gated). Kinematic channel is `PASS` (done). **Gauge sector is
`PART` and OPEN** -- an earlier "provably unobservable" claim was
*retracted* (2026-06-16): the bipartite structure breaks $O_h$ to a
uniaxial subgroup, so there is no symmetry proof of photon isotropy; the
gauge anisotropy is genuinely uniaxial and its observability (unobservable
/ suppressed / excluded $O(1)$ dim-4) is decided by `exp_03`. Unblocked next
action: draft the abstract/introduction.

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

- **Gauge-sector channel OPEN** (2026-06-16): row `STUB`$\to$`PART`, P9
  `STUB`$\to$`PART`. $\mathbf{Q}$-tensor structure derived (eigenvalues
  $\{4,4,16\}$, axis $(1,1,-1)$; coupling ratio $g_3^2/g_2^2=3/2$,
  Paper~II) -- solid. **Observability OPEN.** An earlier "provably
  unobservable" claim was **retracted**: the proposed $O_h$-symmetry
  mechanism fails because the bipartite RGB/CMY structure breaks $O_h$ to a
  uniaxial subgroup about $(1,1,-1)$ ($\mathbf{Q}$ fixed by $12/48$, RGB by
  $6/48$). So the induced photon action is genuinely uniaxially anisotropic;
  the $O_h$-average to isotropic Maxwell is an external imposition the
  dynamics do not justify, and by the `exp_01` analogy the anisotropy may
  survive in observables -- where read literally it is the excluded dim-4
  $O(1)$ effect. The one escape (electric/magnetic cancellation in the full
  dispersion; Paper~I did magnetic only) is uncomputed. **`exp_03` is
  decisive, not confirmatory** -- it could surface a real tension. See
  `notes/gauge_sector_structural_conclusion.md`. `exp_03` is **blocked on a
  `dcl_core` core3d v0.3.0 upgrade** (see WAITING ON).

**Next concrete action (unblocked):** draft the **abstract and
introduction** stating the kinematic channel (= falsifiable dim-6
dispersion) and the structural concordance, but **keep the gauge sector
explicitly open** (observability undecided, `exp_03`-pending) -- do not
assert it as either a prediction or a non-observable. The gauge `exp_03`
is blocked (see WAITING ON).

### TODO / Open Items

### ⏳ WAITING ON (read this first if resuming)

- **`exp_03` (gauge-sector A=1 dynamical test) is BLOCKED on
  `dcl_core` core3d v0.3.0.** *What:* a gauge-field + Peierls coupling +
  uniform-$B$ + induced-response capability that core3d does **not** yet
  have. *Why (DECISIVE, not confirmatory):* the gauge anisotropy is
  uniaxial about $(1,1,-1)$ and there is no symmetry proof of isotropy
  (the $O_h$-average is unjustified). `exp_03` must measure the
  **order/magnitude** of the induced photon birefringence on the fixed
  bipartite lattice, with the **full electric + magnetic** Peierls
  dynamics, to decide: $O(1)$ dim-4 (excluded $\Rightarrow$ tension),
  $(ka)^2$-suppressed (a viable dim-6-like prediction), or null. **NB the
  earlier "token vacuum-average $\to$ isotropic vs single-probe anisotropic"
  framing is retracted** -- the lattice has one fixed bipartite orientation,
  so the token ensemble is uniaxial too; $O_h$ is not restored by
  averaging. *Why core3d not core:* core3d is the canonical engine with
  exact integer-token A=1 accounting; `core` is legacy-only.
  - **Requirements spec written:**
    `dcl-core/docs/design/04_gauge_field_and_vacuum_response.md` (R1 gauge
    param, R2 Peierls hop, R3 `uniform_B_potential`, R4 induced-response
    readout, R5 GPU/parallel sweep). **NB: the spec still carries the old
    "vacuum-average $\to$ isotropy" premise (acceptance test #5, §1.1, R4)
    -- needs revising to the order/magnitude + E+B test above before
    implementation.**
  - **Owner-gated before implementation (user):** (1) review + revise the
    spec (drop the isotropy premise; require **both E and B** responses;
    target is the birefringence *order*); (2) settle the **R4 readout**;
    (3) **GPU / parallelism provisioning** (offered 2026-06-16; the
    birefringence-order precision is $N$-bound $\Rightarrow$ GPU-bound);
    (4) green light to implement.
  - **Then (Claude):** implement v0.3.0 R1--R3 + tests (CPU-first), GPU
    path (R2/R5) once provisioned, then write `exp_03` on the four-cell /
    token-ensemble grid.
  - Cross-repo note: the engine work lives in **`dcl-core`** (separate
    repo), not here; this repo's `exp_03` consumes it and will pin
    `dcl_core >= 0.3.0`.

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
  settle the tactical call:** (a) reconcile P7's "two arrival peaks" photon
  claim (corrected in `rem:photon_limit`); (b) frame-fixing (is the lattice
  frame the CMB frame?). **Gauge sector -- the earlier "sharper falsifier"
  hope was wrong, but its fate is now OPEN, not closed:** it is dim-4 $k_F$
  (not birefringent $k^{(6)}$), and its observability is undecided pending
  `exp_03` (could be unobservable, suppressed, or an excluded $O(1)$ effect
  -- see the gauge-sector-OPEN bullet above /
  `notes/gauge_sector_structural_conclusion.md`). So for now the one *clean*
  frontier-testable falsifiable channel is the **kinematic dim-6
  dispersion**; the gauge story is load-bearing but unresolved. Net: the
  falsifiable content is currently the single kinematic channel, which
  **weakens** (does not kill) the empirical case for prioritising Paper~IV
  over Paper~III -- and the gauge `exp_03` could swing it either way. A fact
  for the tactical ledger; user's call.

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
| Gauge-sector birefringence ($\mathbf{Q}$ eigenvalues $\{4,4,16\}$) | PART | Structure derived (axis $(1,1,-1)$; coupling ratio $g_3^2/g_2^2=3/2$, Paper~II). **Observability OPEN.** Bipartite structure breaks $O_h$ to a uniaxial subgroup ($\mathbf{Q}$ fixed $12/48$, RGB $6/48$) -> genuinely uniaxially anisotropic; no symmetry forces isotropy. Read as an observable it is the excluded dim-4 $O(1)$ effect; the only escape (E/B cancellation in the full dispersion, uncomputed) and the verdict await `exp_03`. See `notes/gauge_sector_structural_conclusion.md`. |
| Multi-channel concordance (P9) | PART | Axis-sharing is a *structural identity* ($M_\text{eff}$ and $\mathbf{Q}$ both inherit $(1,1,-1)$). Kinematic dispersion is the one frontier-testable observational channel; the gauge sector's observable status is itself *open* (`exp_03`), so P9's strength as a multi-witness claim is hostage to that outcome. |

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
  $10^{-19}$ m by ~9 orders). **Superseded re: gauge sector** -- the
  earlier "gauge maps to birefringent $k^{(6)}$, a sharper falsifier" claim
  was wrong (it is dim-4 $k_F$), and the follow-on "unobservable" claim was
  *also* retracted (see next entry -- now OPEN). The one *clean*
  frontier-testable falsifiable channel is the kinematic dim-6 dispersion.
  See the BLOCKING TODO above.
- `notes/gauge_sector_structural_conclusion.md` -- OPEN (was wrongly
  "CONCLUDED/unobservable"): $\mathbf{Q}$-structure derived (axis
  $(1,1,-1)$; coupling ratio $g_3^2/g_2^2=3/2$, Paper~II) but
  **observability undecided**. The $O_h$-isotropy mechanism fails -- the
  bipartite structure breaks $O_h$ to a uniaxial subgroup ($\mathbf{Q}$
  fixed $12/48$), so the induced action is genuinely uniaxial and the
  $O_h$-average is unjustified. Read as an observable it is the excluded
  dim-4 $O(1)$ effect; the escape (E/B cancellation, uncomputed) and the
  verdict await `exp_03`. Gauge audit row PART, P9 PART.
