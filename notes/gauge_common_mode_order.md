# 2.a: the order of the gauge-sector common-mode speed anisotropy

**Status:** RESULT (2026-07-18). Answers the "anisotropy ORDER" question for the
gauge-sector photon channel (board #27 / paper `subsec:gauge_channel`). Decision rule
(user): if the anisotropy is too small to measure -> the sector is consistent (PASS);
otherwise the O_h / single-domain question must be settled.

## The question
The gauge-sector common-mode speed anisotropy is `v^2(k_hat) = k_hat^T eps k_hat` with
`eps = {1,4,4}` -> `v in [1,2]`, a factor-~2 direction-dependent vacuum speed. Is this
an O(1), dimension-4 effect (present at leading order, continuum-surviving) or is it
suppressed to dimension-6 (`~(ka)^2`, unobservably small)? Only "suppressed" would let
the sector pass on smallness.

## The computation
Two independent routes, both -> O(1), dimension-4 (NOT suppressed):

1. **Geometric blocks (established derivation).** `eps` is a *constant* (k-independent)
   induced tensor, so `v(k_hat)` is |k|-INDEPENDENT: the factor-~2 anisotropy is present
   at all wavelengths including the long-wavelength / continuum limit. That is the
   definition of a leading-order (dim-4) effect. (`exp_03_dispersion_core`: v in [1,2].)

2. **Dynamical Ward-safe band-sum (fresh check).** The physical-band second-order
   response (intraband dropped per VIII's Ward-safe prescription), swept over the photon
   wavevector |q|, gives an axis-vs-perp anisotropy RATIO that CONVERGES to a constant
   ~0.32 (not to 1) as |q| -> 0:

   | \|q\| | 0.30 | 0.20 | 0.12 | 0.07 |
   |---|---|---|---|---|
   | max:min ratio | 0.60 | 0.37 | 0.33 | 0.32 |

   A constant, non-unity ratio in the q->0 limit = O(1) dim-4 anisotropy. (If it were
   dim-6-suppressed the ratio would -> 1 as q->0.) **Caveat:** this is the interband-only
   "wrong-axis" object (uniaxial about (1,-1,0), not the optical axis) VIII flagged as not
   the correct induced tensor; it is used here only to gauge the ORDER/magnitude of the
   anisotropy, not its exact structure. For the correct object to be suppressed, the
   Berry-curvature + quantum-metric terms would have to CANCEL this O(1) anisotropy -- a
   non-generic cancellation, and the naive evidence is against it.

## Conclusion
The anisotropy is **O(1), dimension-4, not suppressed.** The "small / viable suppressed
prediction" outcome is **ruled out.** 2.a therefore collapses to a **binary**:

- **NULL** -- if the physical vacuum is `O_h`-restored (`<eps> = 3I`), the O(1) anisotropy
  averages away: consistent, but no falsifiable gauge signal.
- **EXCLUDED** -- if the vacuum is a single fixed trigonal domain, the induced
  electromagnetism has a **factor-~2 direction-dependent speed of light**, excluded by
  cavity / Michelson-Morley isotropy bounds (~10^-18) by ~15-18 orders -> **the gauge
  sector is FALSIFIED.** (The birefringence null is unaffected -- this is the common-mode
  speed, not a polarization split.)

Structurally the A=1 lattice IS a single fixed hop-set (one orientation, no ensemble of
four domains), which points toward the EXCLUDED branch unless a coarse-graining mechanism
restores `O_h`.

## Decision + next step
Per the decision rule (not small -> settle the fork). **We attack the
O_h / single-domain question** (board #27): is the physical A=1 vacuum a single trigonal
domain (-> tension/exclusion) or does the continuum limit / coarse-graining restore `O_h`
(-> null)? Escapes to keep in view: (a) an `O_h`-restoration mechanism; (b) the full
`Gamma^(2)` (orbital-susceptibility) suppressing the anisotropy against the naive O(1)
evidence. Computation: `scratchpad/order_scan.py` (Ward-safe q-scan on the validated
Bloch `T(k)`); the geometric route is `exp_03_dispersion_core` + `electric_induced_action`.
