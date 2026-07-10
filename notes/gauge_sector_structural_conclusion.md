# Gauge-sector birefringence: operator-level Q-tensor EXACT/DONE; only the E+B photon-dispersion order is OPEN

**Status:** operator-level structure **CONFIRMED-AND-DONE**; observable
birefringence **OPEN** (2026-07-07 correction). The induced-gauge
$\mathbf{Q}$-tensor (the magnetic-sector Wilson-loop coefficient) is
reproduced **exactly by running code** -- dcl-core `exp_04` gives
`Q = [[8,4,-4],[4,8,-4],[-4,-4,8]]` with `max|Q - Paper_I_Q| = 0`,
eigenvalues `{4,4,16}`, optical axis `(1,1,-1)`. This is exact in the
lattice interior for a uniform field: **no large $N$, no GPU**. The one
genuinely open, GPU/large-$N$ question is **solely** the full
**electric + magnetic** photon-*dispersion* birefringence *order* (§2.3,
`exp_03` / dcl-core acceptance test #5): $O(1)$ dim-4 vs $(ka)^2$-suppressed
vs null. The gauge-sector audit row is `PART` **because of that open
observable**, not because the operator structure is unfinished.

> **Correction (2026-07-07).** An earlier version of this note carried a
> "test #4 is $N$-limited / GPU-bound" framing on the $\mathbf{Q}$-tensor
> verdict. That was **factually wrong** and is retracted here, not softened.
> The magnetic $\mathbf{Q}$ cross-check was never scale-limited -- it is an
> exact operator identity. The "$N$-limited" belief came from conflating two
> *different* observables (§1.1): the induced **action** (Wilson-loop
> holonomy, 4:1 = `{4,4,16}`, exact) vs the wavepacket **density** response
> (2:1 axis:planar, also robust but a different quantity). Source:
> dcl-core `exp_04`, `data/exp_04_induced_gauge_Q_tensor.log` (in the
> released `dcl_core` v0.3.0). Only §2.3 remains open and GPU-bound.

## 0. The question and what is / is not settled

The natural objection to a "birefringent lattice": *if the substrate is
birefringent, we should see vacuum birefringence; none is seen; therefore
the framework is falsified.* An earlier version of this note claimed the
framework defuses the objection because the photon kinetic term is a vacuum
quantity, hence $O_h$-symmetric, hence isotropic. **That argument fails**
(§2.1). The honest state:

- The induced photon action is **genuinely uniaxially anisotropic** about
  $(1,1,-1)$ at the operator level -- the $\mathbf{Q}$-tensor (§1). This is
  now **confirmed by running code and done** (dcl-core `exp_04`, exact),
  not deferred.
- Whether the **observable** photon dispersion is the excluded $O(1)$
  dimension-4 birefringence, or whether it cancels/suppresses in the
  **full electric + magnetic** lattice dispersion (Paper I computed the
  magnetic sector only), is **open** (§2.3).
- `exp_03` (the full E+B Peierls dynamics) is therefore **decisive, not
  confirmatory**, on that *observable* question **only**: it could confirm
  unobservability *or* surface a real tension/near-falsification.

---

## 1. What is derived AND reproduced by running code -- solid, exact

The induced photon action has an anisotropic coefficient tensor
`Q = [[8,4,-4],[4,8,-4],[-4,-4,8]]` on the magnetic field-strength
components `F = (F12,F13,F23)`, eigenvalues `{4,4,16}`. Its special
direction `F_* = (-1,-1,1)` Hodge-duals to `B_* = (1,1,-1) = V1+V2+V3` --
the same optical axis as the kinematic sector. The residual `Q_aniso`
(eigenvalues `{-4,-4,8}`) carries the anisotropy. Paper II uses the **same
`Q`** for the gauge **coupling ratio** `g_3^2/g_2^2 = 3/2` (spectator
counting) -- that quantitative role is verified and independent of the
birefringence question.

**This is now confirmed by the engine, not just derived on paper.** dcl-core
`exp_04` extracts `Q` from the Peierls plaquette holonomy
(`1 - Re W_ab = F^T Q F`) and cross-checks
`dcl/src/utilities/induced_gauge_action.py`: it reproduces Paper I App. B's
tensor **exactly** (`max|Q - Paper_I_Q| = 0`, eigenvalues `{4,4,16}`, axis
`(1,1,-1)`). The formerly-xfailed
`test_magnetic_response_reproduces_Q_eigenvalues_4_4_16` now passes. This is
an operator identity that holds in the lattice interior for a uniform field
-- **there is no large-$N$ or GPU dependence in it**.

### 1.1 Two observables, not a scale limit (why "$N$-limited" was wrong)

The retracted "$N$-limited" framing conflated two genuinely different
measurements of the magnetic response:

- **Induced action (Wilson-loop holonomy).** The bipartite plaquette
  holonomy `1 - Re W_ab = F^T Q F` gives the `{4,4,16}` tensor, i.e. a
  **4:1** axis:planar eigenvalue ratio. This is **exact** in the lattice
  interior for a uniform field -- no $N$-dependence.
- **Wavepacket density response.** The quantity
  `|psi(+B)|^2 + |psi(-B)|^2 - 2|psi(0)|^2` robustly gives a **2:1**
  axis:planar ratio (NOT 4:1), stable across $N$, packet width, momentum,
  and parity.

These are two different observables of the same anisotropy; the "$N$-limited"
worry arose from reading the density-response ratio as if it were failing to
converge to the action-tensor ratio. It is not a convergence problem -- they
are simply different quantities. **The operator-level $\mathbf{Q}$ is exact
and settled; neither observable is scale-limited.** The only quantity that is
genuinely GPU/large-$N$-bound is the *photon dispersion order* of §2.3.

## 2. Why the *observable birefringence* is open

### 2.1 The $O_h$-symmetry escape FAILS (the correction)

A clean "photon is isotropic by symmetry" argument would need the vacuum to
be $O_h$-symmetric. It is not. The bipartite RGB/CMY structure breaks $O_h$
to the uniaxial subgroup fixing `(1,1,-1)` (verified, reproducible from the
tensor):

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
polarimetry. That would be a tension, not a clean prediction. (Note the
matter-sector density observable of `exp_01` is a different quantity from the
gauge density response of §1.1; the shared lesson is only that operator-level
anisotropy can survive into observables.)

### 2.3 The one place a cancellation could hide -- THE open question

Paper I derived only the **magnetic** sector (`F_ij`, the `Q`-tensor). The
photon dispersion needs the **electric** sector (`F_0i`) too. It is
possible -- but **not shown** -- that the electric-sector anisotropy
compensates the magnetic at leading order, so the net leading birefringence
cancels and only a suppressed (higher-`(ka)`) residual survives, the way
the matter dispersion's anisotropy is `(ka)^2`-suppressed. No framework
argument for this compensation is in hand; it is exactly what `exp_03` (the
full E+B Peierls dynamics, dcl-core acceptance **test #5**) must test. **This
is the sole load-bearing open item in the gauge sector** -- and it is
genuinely GPU/large-$N$-bound (the birefringence-order precision is
$N$-bound).

## 3. Conclusion (the honest one)

The gauge-sector anisotropy `Q` is a **derived, uniaxial structural fact**
(axis `(1,1,-1)`; coupling ratio `3/2`), now **reproduced exactly by running
code** (dcl-core `exp_04`, `max|Q - Paper_I_Q| = 0`) -- confirmatory-and-done,
not deferred. Its **observability is undetermined**: there is no symmetry
proof of isotropy, the matter analogy points toward an observable (and
therefore excluded) $O(1)$ dimension-4 effect, and the only plausible escape
-- electric/magnetic cancellation in the full dispersion -- is uncomputed.
**`exp_03` decides whether the *observable* gauge sector is (a) unobservable
[framework consistent], (b) suppressed-but-present [a new dim-6-like
prediction], or (c) an $O(1)$ dimension-4 effect [a real
tension/falsification].** All three are live. The operator-level `Q` is not
in question -- only its projection into the full E+B photon dispersion.

## 4. Consequences for the rest of Paper IV

- **Gauge-sector audit row:** `PART` -- because the **observable** E+B
  dispersion order is open (`exp_03`), *not* because the operator structure
  is unfinished. The $\mathbf{Q}$-tensor magnetic cross-check is exact and
  done. Not `PASS` (the observable is what a `PASS` would need).
- **P9 multi-channel concordance:** still `PART`, but now with a sharper
  caveat -- the gauge "witness" is structural-and-exact at the operator
  level; what is open is whether it registers as an *observable* channel.
  P9's strength as a multi-*observable* claim is hostage to the `exp_03`
  outcome.
- **Falsifiability bet (Paper III deferral):** the kinematic dim-6
  dispersion remains the one *clean* frontier-testable channel. The gauge
  sector is no longer a "non-observability theorem" we can bank; its operator
  structure is settled but its observable status is an open question that
  could go either way. This makes `exp_03` load-bearing for the gauge
  *observable* story. See `notes/falsifiability_and_sme_mapping.md`.

## 5. Note for Paper I / II

Paper II flags the gauge birefringence as structural-only (good). Paper I's
`induced_gauge_action.tex` §B.5 presents the `O_h`-average as if it
delivers physical isotropic Maxwell; per §2.1 that average is not justified
by the (uniaxial) dynamics -- the same gap as the matter sector, where
`exp_01` showed the anisotropy survives. Worth a clarifying note in a future
Paper I revision: the `O_h`-averaged Maxwell density is the
*orientation-averaged* form, not what a fixed lattice's observables see.
(The operator-level $\mathbf{Q}$ itself is confirmed exact by dcl-core
`exp_04`, so Paper I App. B's tensor stands unchanged -- only its §B.5
isotropy *interpretation* is the open point.)

## 6. Cross-doc coordination

The same stale "test #4 $N$-limited" wording also lives in dcl-core
`docs/design/04_gauge_field_and_vacuum_response.md`. That is **not** this
repo's file to edit; the PM relays a design-doc-04 fix to a dcl-core session
separately (per handoff `2026-07-07-paper04-gauge-Q-tensor-framing-correction`).
