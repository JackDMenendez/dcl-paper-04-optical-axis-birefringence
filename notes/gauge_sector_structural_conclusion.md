# Gauge-sector birefringence: uniaxial operator-level anisotropy; observability OPEN (exp_03-decisive)

**Status:** OPEN (2026-06-16). **Supersedes an earlier "provably
unobservable" framing in this same file, which was wrong** -- it rested on
an $O_h$-symmetry of the vacuum that the bipartite structure does not have
(§2.1). The gauge-sector audit row is therefore `PART`, not a clean `PASS`:
the structure is derived, but the load-bearing question (is the
birefringence an observable?) is unresolved and is decided by `exp_03`.

## 0. The question and why it is not yet answered

The natural objection to a "birefringent lattice": *if the substrate is
birefringent, we should see vacuum birefringence; none is seen; therefore
the framework is falsified.* An earlier version of this note claimed the
framework defuses the objection because the photon kinetic term is a vacuum
quantity, hence $O_h$-symmetric, hence isotropic. **That argument fails**
(§2.1). The honest state:

- The induced photon action is **genuinely uniaxially anisotropic** about
  $(1,1,-1)$ at the operator level (the $\mathbf{Q}$-tensor, §1).
- Whether the **observable** photon dispersion is the excluded $O(1)$
  dimension-4 birefringence, or whether it cancels/suppresses in the
  **full electric + magnetic** lattice dispersion (Paper I computed the
  magnetic sector only), is **open**.
- `exp_03` is therefore **decisive, not confirmatory**: it could confirm
  unobservability *or* surface a real tension/near-falsification.

---

## 1. What is derived (Paper I App. B; Paper II) -- solid

The induced photon action has an anisotropic coefficient tensor
`Q = [[8,4,-4],[4,8,-4],[-4,-4,8]]` on the magnetic field-strength
components `F = (F12,F13,F23)`, eigenvalues `{4,4,16}`. Its special
direction `F_* = (-1,-1,1)` Hodge-duals to `B_* = (1,1,-1) = V1+V2+V3` --
the same optical axis as the kinematic sector. The residual `Q_aniso`
(eigenvalues `{-4,-4,8}`) carries the anisotropy. Paper II uses the **same
`Q`** for the gauge **coupling ratio** `g_3^2/g_2^2 = 3/2` (spectator
counting) -- that quantitative role is verified and independent of the
birefringence question.

## 2. Why observability is open

### 2.1 The $O_h$-symmetry escape FAILS (the correction)

A clean "photon is isotropic by symmetry" argument would need the vacuum to
be $O_h$-symmetric. It is not. The bipartite RGB/CMY structure breaks $O_h$
to the uniaxial subgroup fixing `(1,1,-1)` (verified, `/tmp` check
reproducible from the tensor):

- `Q` is fixed by **12 of 48** $O_h$ elements (a `D_3d`-type uniaxial
  subgroup about `(1,1,-1)`), not all 48.
- The RGB triple `{V1,V2,V3}` is preserved by **6 of 48** (`C_3v` about
  `(1,1,-1)`).

So the induced photon action is invariant only under the uniaxial subgroup
-> it **is** uniaxially anisotropic. Paper I's §B.5 `O_h`-average to
isotropic Maxwell (`<Q>_Oh = 8 I`) mixes `Q` over all **4 body-diagonal
orientations**, but the fixed bipartite lattice samples exactly **one**
(`(1,1,-1)`) and never the other three. The `O_h`-average is thus an
*external imposition on observables*, not a symmetry of the dynamics. There
is no symmetry that forces the photon isotropic.

### 2.2 `exp_01`'s lesson cuts toward observability

For the **matter** sector, `exp_01` showed the operator-level anisotropy is
**not** washed out in observables -- an isotropic pulse really flattens
along `(1,1,-1)`. By the same logic the gauge anisotropy should survive in
observables too. If it does, it is the $O(1)$, dimension-4 vacuum
birefringence (`Δn/n ~ 0.7`, no `a`-suppression -- it rides on the leading
`F^2` Maxwell term), **excluded by ~30-37 orders** by astrophysical
polarimetry. That would be a tension, not a clean prediction.

### 2.3 The one place a cancellation could hide

Paper I derived only the **magnetic** sector (`F_ij`, the `Q`-tensor). The
photon dispersion needs the **electric** sector (`F_0i`) too. It is
possible -- but **not shown** -- that the electric-sector anisotropy
compensates the magnetic at leading order, so the net leading birefringence
cancels and only a suppressed (higher-`(ka)`) residual survives, the way
the matter dispersion's anisotropy is `(ka)^2`-suppressed. No framework
argument for this compensation is in hand; it is exactly what `exp_03` (the
full E+B Peierls dynamics) must test.

## 3. Conclusion (the honest one)

The gauge-sector anisotropy `Q` is a **derived, uniaxial structural fact**
(axis `(1,1,-1)`; coupling ratio `3/2`). Its **observability is
undetermined**: there is no symmetry proof of isotropy, the matter analogy
points toward an observable (and therefore excluded) $O(1)$ dimension-4
effect, and the only plausible escape -- electric/magnetic cancellation in
the full dispersion -- is uncomputed. **`exp_03` decides whether the gauge
sector is (a) unobservable [framework consistent], (b) suppressed-but-present
[a new dim-6-like prediction], or (c) an $O(1)$ dimension-4 effect [a real
tension/falsification].** All three are live.

## 4. Consequences for the rest of Paper IV

- **Gauge-sector audit row:** `PART` (structure derived; observability open
  pending `exp_03`). Not `PASS`.
- **P9 multi-channel concordance:** still `PART`, but now with a sharper
  caveat -- the gauge "witness" is not merely structural-vs-observational;
  its very status (observable? excluded?) is open. P9's strength is hostage
  to the `exp_03` outcome.
- **Falsifiability bet (Paper III deferral):** the kinematic dim-6
  dispersion remains the one *clean* frontier-testable channel. The gauge
  sector is no longer a "non-observability theorem" we can bank; it is an
  open question that could go either way. This neither strengthens nor
  cleanly weakens the bet -- it makes `exp_03` load-bearing for the whole
  gauge story. See `notes/falsifiability_and_sme_mapping.md`.

## 5. Note for Paper I / II

Paper II flags the gauge birefringence as structural-only (good). Paper I's
`induced_gauge_action.tex` §B.5 presents the `O_h`-average as if it
delivers physical isotropic Maxwell; per §2.1 that average is not justified
by the (uniaxial) dynamics -- the same gap as the matter sector, where
`exp_01` showed the anisotropy survives. Worth a clarifying note in a future
Paper I revision: the `O_h`-averaged Maxwell density is the
*orientation-averaged* form, not what a fixed lattice's observables see.
