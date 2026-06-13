# Optical-Axis Renormalization / Isotropy Test

**Status:** STABLE (result landed 2026-06-12; dcl_core v0.2.2).
**Purpose:** Record the numerical confirmation that the kinematic
birefringence anisotropy along $(1,1,-1)$ survives the per-tick A=1
renormalization in *observable* amplitudes -- and that the optical axis
is, in observables, exactly $(1,1,-1)$.
**Backs:** audit row "Kinematic birefringence along $(1,1,-1)$"
(`paper/sections/audit_table.tex`).
**Experiment:** `src/experiments/exp_01_optical_axis_isotropy.py`,
data `data/exp_01_optical_axis_isotropy_results.npz`.

---

## The question this settles

The lattice's single-tick spinor propagator has a structure factor
$|H_\text{RGB}(\mathbf{k})|^2 = 1 - \mathbf{k}^T M_\text{eff}\mathbf{k}
+ O(k^4)$ with $M_\text{eff}$ eigenvalues $\{4/3, 4/3, 0\}$, the zero
eigenvalue along $(1,1,-1)$.  That anisotropy is manifest in the
**bare** propagator.  The open question for an *observable* prediction
was whether the A=1 renormalization that every engine applies each tick
(`enforce_unity_spinor` in `core`; exact integer rebalance in `core3d`)
restores isotropy in the observed amplitudes.  If it did, the kinematic
birefringence channel would be unobservable.  It does not.

## Method (why spreading, not group velocity)

Along the optical axis the dispersion is **flat** ($M_\text{eff}$
eigenvalue 0 $\Rightarrow$ infinite effective mass), so a
momentum-launched packet gives no clean transport contrast there.  The
unambiguous, momentum-free dual is **anisotropic spreading**: an
initially isotropic pulse must flatten iff the dispersion is
anisotropic.  We launch a spherical Gaussian (momentum $=0$), evolve
under A=1 enforcement, and track the density covariance tensor:
`var_par` $= \hat u^T C \hat u$ along $\hat u=(1,1,-1)/\sqrt3$,
`var_perp` the perpendicular average, and the alignment of the
smallest-variance eigenvector with $\hat u$.

## Result

Full run $129^3$, 1000 ticks (perpendicular spread stayed well inside
the box throughout):

- The pulse flattens into a **pancake perpendicular to $(1,1,-1)$**.
  `var_par` stays frozen at its initial value for all 1000 ticks (no
  spreading along the flat axis); `var_perp` grows ~100$\times$.
  Ratio $v_\parallel/v_\perp$: $1.0 \to 0.010$ (core3d) / $0.0054$
  (core).
- The smallest-variance eigenvector locks onto $(1,1,-1)$ at
  **align $= 1.0000$** from $t \gtrsim 100$ (the $t=0$ degenerate value
  is just the undefined eigenvector of a perfectly spherical start).
- **Both engines agree** -- integer `core3d` (exact A=1) and float
  `core` (`enforce_unity_spinor`) -- so the survival is not an artefact
  of one renormalization scheme. `core` shows a slightly stronger
  anisotropy.
- **$\omega$-independent** (photon $\omega=0$ and free particle
  $\omega=0.1019$ agree).

## Interpretation

1. The kinematic anisotropy is **real in observable amplitudes**, not a
   gauge/bare-propagator artefact removed by A=1 normalization.
2. The observed optical axis is **$(1,1,-1)$**, matching the geometric
   prediction $\mathbf{V}_1+\mathbf{V}_2+\mathbf{V}_3$.
3. This is the lattice-scale ($a=1$) anisotropy and is $O(1)$.  The
   physical photon-scale signal is this $O(1)$ anisotropy suppressed by
   $(a/\lambda)^2$ (quadratic / CPT-even), which sets the detectability
   regime -- a separate question from this test.

## What remains (for PASS, not PART)

This test confirms the axis and the renormalization-robustness of the
split; it does **not** supply the closed-form ordinary/extraordinary
**speed split** along the optical axis.  That analytical derivation
(from $|H_\text{RGB}|$ and the propagator eigenphases) is the remaining
step that flips the audit row from PART to PASS.
