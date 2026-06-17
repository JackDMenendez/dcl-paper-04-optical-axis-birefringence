# Falsifiability of the optical-axis birefringence: magnitude, SME mapping, and the tactical question

**Status:** ANALYSIS (2026-06-16). Assesses whether the closed-form
kinematic split (`notes/closed_form_speed_split.md`) yields a *practically*
falsifiable result. **Blocking a tactical decision:** Paper III
(tidal ionization) was deferred in favour of Paper IV on the expectation
that the birefringence is falsifiable; this note is the evidence base for
keeping or reversing that ordering. Builds on Paper I P7
(`predictions.tex` §12.8, `subsec:p7_photon_dispersion`) and P9
(`subsec:p9_concordance`).

---

## 1. The magnitude is set by a free calibration, not by the Planck scale

Critically, the lattice spacing `a` is **not** fixed to the Planck length.
Paper I treats `a` as a calibration to be set by experiment, with the
surviving window. **NB:** Paper I P7 quotes this window as
`a <~ 7.6e-19 m`, but that is wrong by ~9 orders (see §3.3 and the
correction note): a lattice spacing `a ~ 1e-19 m` is a cutoff energy
`E_a = hbar c/a ~ 260 GeV`, which is excluded outright by directly observed
~PeV astrophysical photons (LHAASO). The "7.6" almost certainly traces to
Vasileiou 2013's *linear* result `E_QG1 > 7.6 E_Pl` mis-transcribed into a
length; the lattice effect is *quadratic*, so the linear bound is the wrong
one anyway. Anchored to the correct isotropic quadratic time-of-flight
bound (LHAASO GRB 221009A, `E_QG2 > 7e11 GeV`), the surviving window is

    l_P ~ 1.6e-35 m   <=   a   <~   3e-28 m     (§3.3).

The dispersion signal scales as `(a/lambda)^n` with `n = 2` here (the
anisotropy is a `k^2`, mass-dimension-6 effect -- §3). The effect is
**frontier-level only near the top of this corrected window** (`a ~
1e-28 m`, `E_a ~ E_QG2 ~ 1e12 GeV`), where the next tightening of the
quadratic-LIV bound detects or excludes it; for `a` from there down to
Planck it is up to ~14 orders (in the SME coefficient) below current reach.
So falsifiability does not require `(E/E_Pl)^2`, but it is more contingent
than the discarded `1e-19 m` figure suggested.

The price: `a` is a free parameter. A non-detection tightens the bound on
`a` rather than killing the framework outright -- unless the *angular
pattern* (which is parameter-free, §2-3) is itself contradicted.

## 2. The closed form makes the angular pattern parameter-free

From `closed_form_speed_split.md`, the operator-level structure factor is

    |H_RGB(k)|^2 = 1 - (4/3)|k_perp|^2 + O(k^4),   M_eff = (4/3) P_perp,

`k_perp` the component of `k` perpendicular to n* = (1,1,-1)/sqrt(3). The
fractional dispersion anisotropy between a wave at angle `alpha` to the
axis and one along it is, in physical units,

    delta(E, alpha) = (4/3) (a E / hbar c)^2 sin^2(alpha)
                    = (4/3) (a/lambda_bar)^2 sin^2(alpha).        (1)

Everything in the *shape* of (1) is fixed with **zero free parameters**:

- uniaxial (one axis), axis exactly n* in lattice coordinates;
- coefficient exactly 4/3, perpendicular;
- exact `sin^2(alpha)` angular law;
- **exactly flat along n* to all orders** (|H_RGB|^2 = 1, not just to
  O(k^2)) -- a sharp null direction.

Only the embedding (how n* maps to sky coordinates: 3 orientation numbers)
and the scalar `a` are free. A measured anisotropy that is biaxial, has a
different coefficient ratio, or shows dispersion along the null axis
falsifies the kinematic channel regardless of `a`.

## 3. SME mapping (done -- with literature-grounded bounds)

Background literature established by a verified multi-source search
(2026-06-16); citations in §3.4.

### 3.1 Which SME sector

The kinematic channel is anisotropic *dispersion* (speed depends on
propagation direction), with **no** polarisation dependence at this order
-- it is **nonbirefringent**. In Kostelecky--Mewes it therefore lives in
the CPT-even, nonbirefringent, mass-dimension-6 photon sector: the
coefficients **`c^(6)_(I)jm`** (25 real coefficients, `j = 0,2,4`,
`|m|<=j`). [**SUPERSEDED guess, now resolved:** an earlier version of this
note speculated the gauge-sector birefringence would map to the *birefringent*
`k^(6)` coefficients and be "a much sharper handle." That was wrong. The
gauge-sector anisotropy `Q` rides on the leading `F^2` term, so it is a
*dimension-4* (`k_F`) effect, O(1), excluded by ~30-37 orders if observable
-- which is why it is **not** an observable at all (it is `O_h`-averaged to
isotropic Maxwell). It is a structural consequence the framework predicts
you *cannot* see, not a sharper falsifier. See
`notes/gauge_sector_structural_conclusion.md`.]

- **Dimension 6, not 4.** The leading anisotropy is `O(k^2)` beyond the
  dim-4 kinetic term; the dim-4 directional term `(i/3)(1,1,-1).k` averages
  to zero under O_h (Paper I). So there is no unsuppressed (dim-4)
  anisotropy, and lab/clock/cavity dim-4 bounds do not apply. The relevant
  constraints are the dim-6 astrophysical ones, and the dispersion is `~E^2`
  (the `omega^(d-4) = E^2` factor at d=6).

### 3.2 The prediction in SME form

The SME nonbirefringent dispersion is `E = |p|(1 - s0)` with
`s0 = Sum_{jm} omega^2 (-1)^j Y_jm(p-hat) c^(6)_(I)jm` (d=6). Our photon
dispersion, from `|H_RGB|^2 = 1 - (4/3)|k_perp|^2` with `k = a k_phys`,
`k_phys = E/hbar c`, and `|k_perp| = (aE/hbar c) sin(alpha)`:

    s0(E, alpha) = (4/3) (a/hbar c)^2 E^2 sin^2(alpha).             (2)

Using `sin^2(alpha) = (2/3)[1 - P_2(cos alpha)]`, this is a **fixed
combination of exactly a monopole (j=0) and a quadrupole (j=2)**, the
quadrupole oriented along n* = (1,1,-1), with **no j=4 part**:

    s0 = (8/9)(a/hbar c)^2 E^2 [1 - P_2(cos alpha)].                (3)

The predicted coefficient scale is

    c^(6)_(I) ~ (a/hbar c)^2   [GeV^-2],                            (4)

and -- the key falsifiable structural point -- **the monopole:quadrupole
ratio (1 : 1 in the `[1 - P_2]` basis) and the quadrupole orientation (n*)
are parameter-free**, fixed by `M_eff = (4/3) P_perp`. The overall scale
floats with `a`, but the *pattern* does not: a measured dim-6 dispersion
that is not a pure (monopole + axis-aligned quadrupole, no j=4) along a
single sky axis falsifies the channel regardless of `a`.

### 3.3 Numbers: where the prediction sits vs current bounds

The prediction's **unavoidable isotropic (monopole) part** is bounded by
the strongest isotropic dim-6 time-of-flight limit. Matching the monopole
of (3) to `v/c = 1 - (E/E_QG2)^2` gives `E_QG2 = (hbar c/a) sqrt(9/8) ~ hbar
c/a = E_a` (the lattice cutoff). So the LHAASO quadratic bound binds `a`:

| Quantity | Value |
|---|---|
| Binding bound (isotropic, quadratic TOF) | `E_QG2 > 7e11 GeV` (LHAASO GRB 221009A, PRL 133, 071501, 2024) |
| => lattice cutoff | `E_a = hbar c/a > ~7e11 GeV` |
| => **surviving window** | `l_P (1.6e-35 m) <= a <~ 3e-28 m` (~7 orders) |
| Predicted `c^(6)` at top of window (`a~3e-28 m`) | `~2e-24 GeV^-2` (at the bound, by construction) |
| Predicted `c^(6)` at Planck calibration (`a=l_P`) | `~7e-39 GeV^-2` |

Gap of the **Planck-calibration** prediction below current sensitivity:
~23 orders below the LHAASO-driven isotropic limit (~1e-15 GeV^-2,
arXiv:2508.02883), ~19 below the Fermi GeV credible-interval limit
(~8e-20 GeV^-2, arXiv:2602.01243), and ~8 below the Data-Tables *projected
maximal* sensitivity (~1e-30 GeV^-2, arXiv:0801.0287). So:

- **Detectable now only if `a` sits near the top of the surviving window**
  (`a ~ 1e-28 m`, `E_a ~ E_QG2 ~ 1e12 GeV`), where the next tightening of
  the quadratic TOF bound detects or excludes it.
- For `a` from there down to Planck, the effect is up to ~14 orders (in the
  coefficient) below reach.

**Anisotropic sector.** The distinctive direction-resolved fingerprint
(the j=2, axis-aligned part) is currently bounded ~5-6 orders *more weakly*
than the isotropic: the best simultaneous anisotropic dim-6 limits are
~1e-14 GeV^-2 (Kislat & Krawczynski, PRD 92, 045016, 2015; arXiv:1505.02669
-- first bounds on all 25 `c^(6)_(I)jm` from 25 AGN), because the joint
25-coefficient fit is dominated by its weakest direction. So the *directional*
test is the parameter-free fingerprint but the *isotropic* time-of-flight is
the tighter constraint on `a`.

**Opportunity (from the search's open questions):** a *targeted* single-axis
analysis -- binning gamma-ray TOF by angle to the specific candidate axis
n* rather than fitting all 25 coefficients -- could beat the ~1e-14 joint-fit
bound and approach isotropic (~1e-15 ... 1e-20) sensitivity. That is a
concrete, publishable observational proposal specific to this prediction.

### 3.4 Sources

- Kostelecky & Mewes, *Phys. Rev. D* 80, 015020 (2009), arXiv:0905.0031 --
  convention: `c^(6)_(I)jm` (nonbirefringent, dispersive), dispersion
  `p^0 ~ (1 - s0 +/- sqrt(...)) p`.
- LHAASO Collab., *Phys. Rev. Lett.* 133, 071501 (2024), arXiv:2402.06009 --
  `E_QG2 > 6e-8 E_Pl ~ 7e11 GeV` (isotropic quadratic, GRB 221009A).
- Guerrero et al. (2025), arXiv:2508.02883 -- SME<->E_QG mapping
  `s_pm/(2 E_QG2^2) = Sum Y_jm c^(6)_(I)jm`; isotropic `c^(6)_(I)00 ~ 1e-15`.
- Xiao, Song & Ma (2026), arXiv:2602.01243 -- Fermi GeV credible interval
  `|c^(6)_(I)00| <= 7.75e-20 GeV^-2`.
- Kislat & Krawczynski, *Phys. Rev. D* 92, 045016 (2015), arXiv:1505.02669
  -- anisotropic dim-6: all 25 `c^(6)_(I)jm` at ~1e-14 GeV^-2.
- Kostelecky & Russell, Data Tables, arXiv:0801.0287 (living ed.).

*Caveat:* literature `c^(6)_(I)00` figures use different metrics (projected
max sensitivity 1e-30 vs measured credible interval ~8e-20 vs combined-data
expectation ~1e-15) and are not directly comparable; the `a`-bound above is
anchored to the unambiguous `E_QG2` limit, not to a `c`-value conversion
(the Myers-Pospelov `c^(6) = -sqrt(4pi) chi^2 l_P^2/5` dictionary was
checked and *refuted* in the search, so it is not used). O(1) factors in
(4) are dropped; the order-of-magnitude gaps are robust to them.

## 4. A correction to Paper I's stated P7 photon signature

Paper I P7's "direction-resolved refinement" asserts (predictions.tex
~l.622-630):

> "a single light pulse propagating oblique to the optical axis separates
> into two arrival peaks ... because the two propagator eigenmodes
> lambda_pm have equal magnitude but different phases (hence different
> group velocities)."

The closed-form derivation does **not** support this mechanism *for
photons*:

- The eigenphases are `theta_pm = arg(i sin(w/2) +/- cos(w/2)|H_RGB|)`,
  with `theta_- = pi - theta_+`, so `v_g(-) = -v_g(+)`: the two branches
  are the particle/antiparticle (forward/backward) pair, with **equal and
  opposite** group velocity, not two co-propagating peaks at different
  speeds.
- The genuine group-velocity split is `Delta v = (2/3) sin(w)|k|`, which
  **vanishes as w -> 0** (the photon). So a massless pulse does **not**
  split into two same-direction arrival peaks via `lambda_pm`.

What *does* survive for the photon is the **direction-dependent dispersion
curvature** (1): bursts near n* disperse *less* than perpendicular bursts.
That axial-vs-perpendicular contrast -- already stated correctly elsewhere
in P7 -- is the defensible photon signature; the "two arrival peaks"
sentence should be reconciled (it may hold only in the massive sector, or
should be reframed as the dispersion contrast). **This is exactly the kind
of load-bearing detail that must be right before betting paper order on
it**, and Paper IV's `rem:photon_limit` already records the corrected
version.

## 5. Where the real falsifying power is: P9 concordance

A single anisotropic channel with a free `a` yields, on non-detection, only
a tighter bound on `a`. The framework's **strongest** falsifiable claim is
P9 (`subsec:p9_concordance`): the kinematic, gauge, gravitational, and
inertial anisotropies **share one sky axis**. In principle, multiple
independent witnesses on one direction is harder to fake than any one
channel.

**Caveat (updated 2026-06-16):** the witnesses are *not* all independent
observational channels, and the **gauge sector's status is itself OPEN**
(not "provably unobservable" -- that earlier claim was retracted; the
bipartite structure breaks `O_h` to a uniaxial subgroup, so there is no
symmetry proof of isotropy -- see
`notes/gauge_sector_structural_conclusion.md`). It shares the `(1,1,-1)`
axis by a *structural identity* (same `M`/`Q` geometry), not by an
independent measurement; whether it is *also* an observable (and whether
that observable is the excluded dim-4 `O(1)` effect) awaits `exp_03`. So P9
is "one axis, shared structurally, with the **kinematic** dispersion as the
one *clean* frontier-testable observational channel" -- not "N independent
observational witnesses." The concordance is real and parameter-free as a
*consistency* statement, but it does not
multiply the empirical falsifiability the way independent witnesses would.

## 6. Frame-fixing: the remaining physics gate

The axis n* is fixed in the *lattice* frame. To point telescopes it must be
tied to a physical frame; the natural candidate is the CMB rest frame, but
the program has not (as far as this repo shows) established that the lattice
frame is locatable on the sky. Until it is, the direction-resolved test
(binning GRBs/polarisation by angle to a *candidate* axis) can be run as a
search over orientations, but a clean prediction of *which* sky direction
requires the frame identification. **Open.**

## 7. Verdict for the tactical decision

- **Is the result falsifiable?** Yes: the angular *pattern* is
  parameter-free (axis n*, monopole+quadrupole with fixed ratio, no j=4),
  the SME sector is identified (nonbirefringent dim-6 `c^(6)_(I)jm`,
  §3), and the test reuses existing gamma-ray time-of-flight binned by sky
  angle. But the *magnitude* is more contingent than first thought: the
  corrected surviving window is `a <~ 3e-28 m` (not `1e-19 m`), so the
  effect is at current frontier sensitivity only near the top of that
  window; below it, down to Planck, it is up to ~14 orders (in the
  coefficient) out of reach.
- **Is it a clean falsification *now*?** Not from the kinematic channel
  alone: (i) `a` is free, so a null result bounds `a` (and only the
  *pattern* is unfalsifiable-by-tuning); (ii) the isotropic time-of-flight
  is the binding constraint while the distinctive *anisotropic* fingerprint
  is currently ~5-6 orders weaker (§3.3); (iii) frame-fixing is open; (iv)
  the photon signature needed the §4 correction.
- **Gauge sector is OPEN, not a rescue and not a clean null (2026-06-16):**
  the hoped-for "sharper gauge falsifier" (`k^(6)`) does not exist -- the
  gauge anisotropy is dim-4 `k_F`. But the follow-on "provably unobservable"
  claim was **retracted**: the bipartite structure breaks `O_h` to a
  uniaxial subgroup, so there is no symmetry proof of isotropy. The gauge
  anisotropy is genuinely uniaxial; whether it is unobservable, suppressed,
  or the excluded dim-4 `O(1)` effect is **decided by `exp_03`** (full E+B
  dynamics). So for now the **kinematic dim-6 dispersion is the one *clean*
  frontier-testable channel**.
- **Tactical read (for keeping Paper IV ahead of Paper III):** weaker than
  the earlier draft hoped. The *clean* falsifiable content reduces to the
  single kinematic channel (frontier-level, contingent on `a` near the top
  of its window). The gauge sector is unresolved -- `exp_03` could make it a
  second prediction, a non-observability result, *or* a tension. This
  **weakens** (does not settle) the empirical case for prioritising Paper IV
  over Paper III -- a fact for the tactical ledger; the kinematic channel
  plus the clean by-product (the Paper I bound erratum) are real
  deliverables regardless of the `exp_03` outcome.

## 8. Concrete next steps (in priority order)

1. ~~SME dim-6 dictionary translation of `M_eff = (4/3) P_perp` and numeric
   comparison to published bounds.~~ **DONE (§3).** Result: nonbirefringent
   dim-6 `c^(6)_(I)jm`, pattern parameter-free; surviving window
   `a <~ 3e-28 m`; Paper I's `1e-19 m` corrected.
2. **Correct Paper I P7's `a <~ 7.6e-19 m`** -> `a <~ 3e-28 m` (LHAASO
   GRB 221009A, `E_QG2 > 7e11 GeV`), and reconcile the P7 "two arrival
   peaks" sentence with §4 (coordinate with Paper I -- this is an error in
   the published Paper I and should feed back into its errata / next rev).
3. **Gauge-sector channel -- OPEN, `exp_03`-decisive.** Not the sharper
   `k^(6)` falsifier (it is dim-4 `k_F`); and *not* "provably unobservable"
   either (that claim was retracted -- the bipartite structure breaks `O_h`
   to a uniaxial subgroup, no symmetry proof of isotropy). The anisotropy is
   genuinely uniaxial; `exp_03` (full E+B Peierls dynamics on core3d) must
   decide whether it is unobservable, suppressed, or the excluded dim-4
   `O(1)` effect (a real tension). See
   `notes/gauge_sector_structural_conclusion.md`; audit row PART, P9 PART;
   engine requirements `dcl-core/docs/design/04`.
4. Targeted single-axis gamma-ray TOF analysis along a candidate n* (could
   beat the ~1e-14 GeV^-2 joint-fit anisotropic bound; §3.3) -- a concrete
   observational proposal for the paper.
5. Frame-fixing: is the lattice frame the CMB frame? (§6).
