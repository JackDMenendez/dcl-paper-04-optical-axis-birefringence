# exp_01 -- Optical-Axis Isotropy Test

**Status:** PASS (run 2026-06-12, dcl_core v0.2.2).
**Audit row:** "Kinematic birefringence along $(1,1,-1)$"
(`paper/sections/audit_table.tex`).
**Tests:** whether the lattice's bare dispersion anisotropy survives the
per-tick A=1 renormalization in *observable* amplitudes -- the
load-bearing question for an observable birefringence prediction.

---

## What it measures

An initially **isotropic** Gaussian pulse (momentum $=0$) is evolved
under per-tick A=1 enforcement, and the density covariance tensor is
tracked over time.  If the dispersion anisotropy survives
renormalization the pulse flattens into a pancake **perpendicular to
$(1,1,-1)$**: the variance along the optical axis stays flat while the
perpendicular variance grows, and the smallest-variance eigenvector of
the covariance aligns with $(1,1,-1)$.

This real-space spreading observable is used in place of a
group-velocity / transport measurement because the dispersion is *flat*
along the optical axis (infinite effective mass), so a momentum-launched
packet gives no clean transport contrast along $(1,1,-1)$.  The
spreading anisotropy is the unambiguous, momentum-free dual.

## Engines (run both)

- **core3d** (integer-token): its `_hop_average` kernel realises the
  $\tfrac13\sum_\text{RGB}e^{i\mathbf{k}\cdot\mathbf{V}}$ structure
  factor the prediction is built on. A=1 is an exact integer identity.
  *Primary engine.*
- **core** (float amplitude): a different (directed) kernel with
  `enforce_unity_spinor`. Independent cross-check that the result is not
  an artefact of one A=1 scheme.

## Inputs

- Lattice $129^3$ (quick check: $41^3$); $\sigma = 2.5$; $\omega \in
  \{0\ (\text{photon}),\ 0.1019\ (\text{free particle})\}$;
  $N_\text{units}=10^9$ (core3d resolution); 1000 ticks.

## Outputs

- `data/exp_01_optical_axis_isotropy_results.npz` -- one structured
  array per `engine_omega` config; columns
  `tick, var_par, var_perp, eval0..2, align_flataxis_to_(1,1,-1),
  norm_or_tokens`.

## Result (full run, $129^3$, 1000 ticks)

| Engine | $\omega$ | ratio $v_\parallel/v_\perp$ ($t{=}100\to1000$) | flat-axis align to $(1,1,-1)$ | A=1 |
|---|---|---|---|---|
| core3d | 0 | $0.087 \to 0.010$ | 1.0000 | tokens exact |
| core | 0 | $0.046 \to 0.0054$ | 1.0000 | norm $=1$ |
| core3d | 0.1019 | $0.088 \to 0.010$ | 1.0000 | exact |
| core | 0.1019 | $0.056 \to 0.0061$ | 1.0000 | norm $=1$ |

The optical-axis variance stays frozen at its initial value for the full
1000 ticks (no spreading along the flat-dispersion axis) while the
perpendicular variance grows ~100$\times$; the smallest-variance axis
locks onto $(1,1,-1)$ to align $=1.0000$; the result is
$\omega$-independent and agrees across both engines.

## Success criteria

- **PASS** if the pulse flattens perpendicular to $(1,1,-1)$ (ratio
  $\ll 1$) with flat-axis alignment $\to 1$ on both engines: the
  anisotropy survives A=1 renormalization in observables, and the
  optical axis is confirmed to be $(1,1,-1)$.  *(Met.)*
- **FAIL** if the pulse stays isotropic (ratio $\approx 1$):
  renormalization restores isotropy and the kinematic prediction is
  unobservable.

## What this does and does not establish

Establishes, numerically: the kinematic anisotropy is real in
observable amplitudes (not a bare-propagator artefact), and its optical
axis is $(1,1,-1)$.  Does **not** by itself supply the closed-form
ordinary/extraordinary speed split -- that analytical step is what flips
the audit row from PART to PASS.  See
`notes/optical_axis_renormalization_test.md`.

## Reproduction

`python src/experiments/exp_01_optical_axis_isotropy.py` (needs
`dcl_core >= 0.2.2`). Quick check: append `41 80`.
