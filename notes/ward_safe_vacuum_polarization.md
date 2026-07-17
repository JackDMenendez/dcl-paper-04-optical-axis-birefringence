# Ward-safe form of the induced-action vacuum polarization

**Status:** diagnosis complete (2026-07-17); full band-sum reproduction of `{4,4,16}`
NOT achieved (honest -- see below). **DECISION (author, 2026-07-17): this is a formally
OPEN item, deliberately left open -- candidate for a follow-on paper.** VIII does NOT claim
a single-object dynamical (momentum-space fermion-loop) extraction of the induced-action
tensor; VIII's tensor is the geometric holonomy (method (a), engine-verified via `exp_01`).
**Verifier:** `src/utilities/ward_safe_diagnosis.py` (all checks PASS). **Triggered by:**
handoff `2026-07-16-paper04-to-paper08-ward-safe-vacuum-polarization`.
**Related:** [[trlnT_prescription]], [[speed_anisotropy_and_isotropy_restoration]].

## Decision (2026-07-17) -- leave open, be honest

The single-object momentum-space extraction of the induced-action TENSOR is left **open on
purpose**. Rationale: it is a *methodological completeness* question, not a correctness one
-- methods (a) geometric-holonomy and (b) fermion-loop are the same induced action and must
agree, and (a) already gives `{4,4,16}` (engine-verified). So finishing (b) would confirm a
known answer, not decide anything. It is not on the companion critical path (the null split
`1.8e-15` and A=1-survival stand independently). A follow-on paper may address the correct
orbital-susceptibility (Berry-curvature + quantum-metric) assembly. Until then, both VIII
and IV frame the tensor as **geometric structure x scalar magnitude**, never as a from-
scratch single-object dynamical extraction (see the honesty checklist in the reply handoff
`2026-07-17-paper08-to-paper04-ward-open-decision`).

---

## The question (Paper IV)

IV adopted the physical-band prescription and built a dynamical BZ extractor of the
second-order eigenphase shift. A naive sum does not converge to `{4,4,16}`: it is
sign-wrong, magnitude-wrong (`~1e3`), and grid-divergent. IV asks for the exact
Ward-safe form and the regularization knob.

## Diagnosis (proven, verified)

**Where the divergence is.** Along the optical axis `d = (1,1,-1)/sqrt3`, all three hop
vectors project equally (`d.V_a = 1/sqrt3` -- this IS the `D_3d` trigonal symmetry), so
moving by `t*d` only rotates the phase of `S_RGB` and leaves `|S|` fixed. The transfer
eigenvalues `lambda = i sin(w/2) +/- cos(w/2)|S(k)|` are therefore **independent of
position along the axis** -- the physical band is **exactly flat along `(1,1,-1)`**.
Hence the intraband denominator `lambda_phys(k) - lambda_phys(k +/- q)` **vanishes
identically along the optical axis**: that is IV's divergence.

**Why it is spurious.** The intraband (physical -> physical at `k +/- q`) term carries
occupation difference `f(k) - f(k+q) = 1 - 1 = 0` (both physical states filled) and its
`q -> 0` pole is cancelled by the diamagnetic seagull (the f-sum rule). It must be
**dropped**, not regularized with a principal value / `eta`. The interband
(physical <-> doubler) part is finite -- the gap is `2 cos(w/2)` along the axis and
`O(1)` generically, vanishing only at BZ corners (`S_RGB = 0`, measure zero, integrable).

## The Ward-safe prescription

- **Regularization knob:** finite `omega` gaps the doubler (keeps the interband
  denominator open); **drop the intraband pole** (Ward-cancelled); extrapolate
  `omega -> 0`. No pole/PV regulator -- the correct object has no pole.
- **Structure `{4,4,16}`/`{1,4,4}`: take it from the geometry, not the band sum.** In
  the A=1 construction the induced action is `c * sum_plaq (1 - Re W)`, so the
  anisotropic tensor is the plaquette holonomy (VIII's `derive_magnetic_Q` / dcl-core
  `exp_04`, exact and pole-free -- the `q -> 0` closed form), and the fermion loop
  supplies the (isotropic) scalar `c = 1/g^2`. The anisotropy lives in the gauge-field
  coupling to the hop pairs, not the band response.

## Honest status (what is NOT settled)

I did **not** reproduce `{4,4,16}` from a physical-band Lindhard-style sum. The naive
symmetric interband current-current tensor comes out uniaxial about `(1,-1,0)` with
ratio `~9` -- **not** `Q_B`. So the correct magnetic (orbital-susceptibility) assembly is
more subtle than a current-current sum, and the geometric route above is the reliable
one for the structure. Two honest options for IV:

1. **Recommended:** compute the structure geometrically from the engine's hop vectors
   (an engine computation, `exp_04`-style, pole-free) and the scalar `c` from the
   physical-band trace (interband, finite `omega`). This is a genuine from-engine
   extraction; it just factors structure (geometry) x magnitude (band sum) rather than
   forcing both through one Lindhard sum.
2. If a single-object dynamical tensor is wanted, it must be the full orbital-
   susceptibility (Berry-curvature + quantum-metric) combination, not the current-current
   proxy -- open, and not needed for the companion verdict (the null split `1.8e-15`
   already stands).
