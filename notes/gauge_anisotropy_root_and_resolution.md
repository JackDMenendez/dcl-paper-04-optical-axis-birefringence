# The gauge-sector anisotropy: its root (the V4 exclusion) and the resolution direction

**Status:** FOUNDATIONAL ANALYSIS (2026-07-18). Diagnoses the root of the gauge-sector
common-mode speed anisotropy tension (`notes/gauge_common_mode_order.md`, board #27) and
lays out the structural resolution direction. Author decision (2026-07-18): publish
Paper IV with this tension honestly stated; the resolution is a foundational research
direction, not an edit.

## The tension (recap)
The induced photon common-mode speed anisotropy `v^2(k) = k^T eps k`, `eps = {1,4,4}`, is
`O(1)` and dimension-4 (NOT suppressed) -- three independent routes agree (geometric
holonomy; Ward-safe physical-band vacuum polarization, traceless/iso ~0.5 and
q-independent; density response exp_03a). For the physical vacuum taken as the single
fixed trigonal domain, an `O(1)` direction-dependent speed of light is a marginal
(CPT-even, non-birefringent `k_F`) Lorentz violation excluded by cavity / Michelson-Morley
isotropy bounds (~1e-18). It is observable because the matter sector does NOT share it
(matter anisotropy is dim-6), so the two sectors ride different light cones and the
measurable is their `O(1)` relative tilt. As constructed: excluded.

## The root: one tensor, one arbitrary choice
The entire effect is the single tensor `eps = sum_a V_a V_a^T` over the hop axes:
- **Three** cube body-diagonals {(1,1,1),(1,-1,-1),(-1,1,-1)}: `sum V_a V_a^T = {1,4,4}`
  (anisotropic, D_3d about the omitted (1,1,-1)).
- **Four** body-diagonals: `sum V_a V_a^T = 4 I` (exactly isotropic, O_h restored).
So the anisotropy is precisely the omission of the 4th diagonal `V_4 = (1,1,-1)` --
equivalently, the selection of one of the four diamond orientations. That choice was
somewhat arbitrary (author, 2026-07-18). The optical axis (Paper IV's whole subject) and
the gauge tension are the SAME fact seen twice.

## Why matter survives the choice but the induced photon does not
Structural, clean, and the crux:
- **Matter** leading term is a SCALAR: `|sum_a e^{i k.V_a}|^2 = |3|^2` at k=0, isotropic;
  the D_3d breaking is pushed to the `O(k^2)`, dimension-6 correction
  (`|H|^2 = 1 - (4/3)|k_perp|^2`). Irrelevant operator -> viable, Planck-suppressed
  (the kinematic falsifiable channel).
- **Induced photon** block is a TENSOR from the outset: `eps = sum_a V_a V_a^T`, so its
  anisotropy sits at `O(1)`, dimension-4. Marginal operator -> not suppressed -> excluded.
The emergent leading-order Lorentz invariance of the matter sector does NOT descend to the
induced gauge sector -- a recognized naturalness difficulty of emergent-spacetime
constructions (you can tune matter onto one light cone; the induced photon generically
lands on a different, anisotropic one unless a symmetry forces coincidence, and D_3d does
not).

## The resolution direction (structural; foundational; open)
Because the anisotropy is fixed by the choice of hop set, the formalism already admits the
fix. The current dcl-math permits including `V_4` and `-V_4`, and more generally
higher-dimensional and polygonal axis topologies (author, 2026-07-18) -- i.e. the
three-axis single-domain lattice is one choice in a family, not the framework.
- **Four-axis / O_h hop set:** `sum V_a V_a^T = 4I` isotropic -> gauge tension removed. But
  the matter structure factor `sum_4 e^{ik.V}` is then also isotropic at `O(k^2)` -> the
  optical axis vanishes in BOTH sectors (no kinematic channel, no Paper IV subject). Fixes
  the gauge sector by deleting the phenomenon.
- **Four-orientation VACUUM (the promising decoupling):** if the vacuum superposes the four
  diamond orientations, the induced gauge action -- a loop over the whole vacuum -- sees the
  `O_h` average (`<eps> propto I`, isotropic; gauge Lorentz-invariant), while a matter
  EXCITATION propagating in a single orientation retains its dimension-6 optical axis. The
  two sectors DECOUPLE: gauge isotropic, matter axis-bearing and viable. This is exactly the
  O_h-restoration mechanism that is absent for a single fixed lattice but present the moment
  the construction is four-orientation.

## Open foundational questions (the "research project")
1. Does the four-orientation-vacuum decoupling hold consistently -- why does the loop
   average over orientations while the excitation does not? (Vacuum superposition vs a
   spontaneously chosen ground state; if matter states also average, the matter axis washes
   out too.)
2. Does an `O_h`-restoring / four-axis / polygonal construction preserve A=1 conservation and
   the Dirac/chiral structure that the three-axis choice was made to secure (3 spatial
   directions -> 3 gamma-matrices, the RGB/CMY bipartite split)?
3. Is the optical axis physical (spontaneously chosen D_3d) or an artifact of a
   single-domain description of an O_h-symmetric vacuum? The answer decides whether Paper IV's
   subject and the gauge tension are both real, or both dissolve.

This is a Paper-I-level structural question ("which sector inherits which symmetry"), which
is why the author notes the structural/foundational derivation (Paper-02 material) arguably
belongs UNDER the phenomenology rather than downstream of it.

## Scope (do not overstate)
The tension is specific to the gauge-sector common-mode speed. It does NOT touch: the
birefringence null (passed; adjugate theorem holds for any hop set), the kinematic
directional dispersion, the Bell-test / quantum results, or the broader program. Paper IV
publishes with the tension honestly stated; the resolution is tracked follow-on (board #27 /
a foundational note that may seed a dedicated paper).
