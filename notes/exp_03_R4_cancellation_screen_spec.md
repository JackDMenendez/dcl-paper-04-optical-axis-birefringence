# exp_03 R4 readout — DECIDED: the static E+B induced-action cancellation screen (Choice 1)

**Status:** R4 definition SETTLED (2026-07-09). This closes the owner-gated
"R4 readout definition" item for `exp_03`. The chosen readout is the **static
electric-plus-magnetic induced-action cancellation screen** — the extension of
`exp_04`'s magnetic Wilson-loop extraction to the electric sector, testing
whether the electric and magnetic anisotropies cancel the *leading* photon
birefringence.

This note specifies what to compute, the decision criterion, the sweep, the
validation tests, and the (small) cost. It is written to drop into an `exp_03`
driver once implementation is green-lit.

---

## 1. Why this readout

The load-bearing gauge question is whether the induced photon action's known
uniaxial anisotropy about the optical axis `(1,1,-1)` produces an **observable**
birefringence, or whether it is unobservable / suppressed. Paper I derived the
**magnetic** sector only — the coefficient tensor `Q` with eigenvalues
`{4,4,16}` — and `exp_04` reproduced it exactly from the lattice's spatial
plaquette holonomies. The one uncomputed escape named throughout the notes is
that the **electric** sector could cancel the magnetic anisotropy at leading
order, pushing any real effect to higher order in the wavevector.

Choice 1 tests exactly that escape, and nothing more — it is a **screen**, and
it is decisive in the good case:

- **If the electric and magnetic anisotropies cancel** the leading photon
  speed split, the gauge birefringence is **not** a dimension-4 effect; the
  operator anisotropy is unobservable at leading order and the framework is
  consistent at the level astrophysical polarimetry constrains. Question
  effectively closed, cheaply.
- **If they do not cancel**, there is a genuine `O(1)`, dimension-4 birefringence
  at the operator level — a strong tension signal (that regime is excluded by
  ~30–37 orders if it survives into observables), and the motivation to pin the
  exact observable order under the full A=1 dynamics (a later, heavier
  measurement) becomes concrete.

The screen is chosen over the k-resolved dispersion measurement because it
returns a publishable verdict at a fraction of the cost and can outright close
the question in the cancellation case. Its limit is stated in §7.

## 2. The physical target, in words

The induced photon action is a quadratic form in the electromagnetic field
strength. Split into the magnetic part (the three components of the magnetic
field `B`) and the electric part (the three components of the electric field
`E`). Integrating the matter tokens out of the A=1 dynamics gives an effective
Maxwell-like energy density

    energy density  =  ½ ( E · epsilon · E  +  B · (mu-inverse) · B )

where `epsilon` (the permittivity tensor) and `mu-inverse` (the inverse
permeability tensor) are **anisotropic**, both uniaxial about `(1,1,-1)`. The
magnetic tensor `mu-inverse` is what `Q = {4,4,16}` encodes. The permittivity
tensor `epsilon` is the electric-sector analog and is **uncomputed**.

Birefringence — a polarization-dependent phase speed — arises when, for a wave
of given direction, the two transverse polarizations see different combinations
of `epsilon` and `mu-inverse`. The leading (dimension-4) birefringence can be
read directly from these two tensors. It **vanishes** if and only if `epsilon`
and `mu-inverse` are anisotropic in a way that conspires so that both transverse
polarizations propagate at the same speed for every direction — the cancellation.

So the screen reduces to: **measure `epsilon`, combine with the known
`mu-inverse`, and evaluate the leading transverse-mode speed split.**

## 3. What is already in hand — the magnetic block

`exp_04`'s `extract_Q` (dcl-core `experiments/exp_04_induced_gauge_Q_tensor.py`)
builds the magnetic coefficient from **spatial** plaquette holonomies: for each
RGB plane it measures the Wilson-loop phase of a uniform `B` (via
`uniform_B_potential`), which by Stokes is linear in `B`; squaring and summing
over planes gives the quadratic form `B · (mu-inverse) · B`, i.e. `Q`. Result:
eigenvalues `{4,4,16}`, special axis `(1,1,-1)`, reproduced with
`max|Q − Q_PaperI| = 0`. **Reuse this verbatim as the magnetic block.**

## 4. The new piece — the electric block

**IMPLEMENTATION FINDING (2026-07-09, corrects the original plan below).**
The electric sector does **not** have a clean Wilson-loop holonomy analogous to
the magnetic one. The engine couples the two fields *asymmetrically*
(`core3d/hop.py:8-16, 96-103`):

- **Magnetic `B`** enters as a spatial **link phase** `exp(i A_mid · v)` — a true
  U(1) link variable — so a closed spatial loop gives the exact holonomy `exp_04`
  uses.
- **Electric `E`** enters as an **on-site phase** `delta_phi = omega + V(x)`, where
  a static spatially-varying `V(x) = −E·x` is the electric field. But `delta_phi`
  drives the Dirac-like R↔L mixing rotation `cos(delta_phi/2)`, `sin(delta_phi/2)`
  — it is **mass-like, not a U(1) link phase**. (Confirmed independently: a
  *constant* `V` shifts `delta_phi` uniformly, i.e. it shifts the effective mass —
  it is NOT a pure gauge and does change densities.) There is therefore **no
  temporal Wilson loop** of the exp_04 form; the electric-block holonomy idea in
  the original plan is withdrawn.

So the electric block must be measured **dynamically**, and — to keep the
electric and magnetic blocks on the *same normalization footing* (avoiding the
density-vs-holonomy 2:1/4:1 conflation) — **both** sectors are measured with the
**same** second-order token-density response estimator:

    d_rho(n_hat) = rho(+eps·n_hat) + rho(−eps·n_hat) − 2·rho(0),
    s(n_hat)     = sqrt( <d_rho^2>_interior ) / eps^2,

the symmetrised (field-squared) response of a centred reference packet, swept
over orientations `n_hat`. `E` via an `external_potential` ramp, `B` via
`uniform_B_potential`. The magnetic **holonomy** `{4,4,16}` is retained as a
validated structural **anchor** (and plumbing check), not as the block that is
combined with the electric response.

**Implemented and run:** `src/experiments/exp_03a_gauge_cancellation_screen.py`
(N=33, CPU, minutes). Results in §4a.

### 4a. Results (exp_03a, 2026-07-09)

- **Anchor:** magnetic holonomy `Q = {4,4,16}` reproduced EXACTLY
  (`max|Q − Q_ref| = 1.8e-15`) — plumbing + method validated against `exp_04`.
- **Both sectors are cleanly uniaxial** about `(1,1,-1)` (the two independent
  perpendicular probe directions agree to `<0.2%`).
- **Density response, axis : perpendicular ratio:**
  - Magnetic: **9.14 — axis-ENHANCED** (response strongest for `B` along the axis).
  - Electric: **0.68 — axis-SUPPRESSED** (response *weakest* for `E` along the axis).
  - ⇒ **The electric and magnetic anisotropies have OPPOSITE sense along the
    optical axis.** This is the qualitative signature one would want for a
    cancellation, and it is a genuine, previously-uncomputed result.
- Electric response confirmed quadratic in `|E|` (the leading `F^2` response).
- **Caveat on the absolute ratios:** this density-response estimator is the
  2:1-*family* observable, not the `{4,4,16}` action tensor; its absolute
  magnitudes (9.14, 0.68) are estimator-specific and should not be read as action
  coefficients. The robust, interpretation-independent content is: **both uniaxial,
  opposite sense.**

**What this does NOT yet settle:** the opposite-sense density result is
*suggestive* of cancellation but is not the photon-dispersion verdict, because the
density response is not the effective action that governs the photon speed. The
action-level electric block (the true `epsilon`) still needs either Paper I's
App. B derivation extended to the electric sector, or an action-level (spectral /
`Tr ln T`) probe — see §7. That is the next step.

## 5. The decision criterion

From `epsilon` (measured, §4) and `mu-inverse` (`Q`, §3), form the effective
photon dispersion and, for each probe direction `k̂`, the two transverse
polarization speeds `v_plus(k̂)` and `v_minus(k̂)`. Define the leading speed
split `Δv(k̂) = v_plus(k̂) − v_minus(k̂)`. Evaluate along the optical axis
`(1,1,-1)`, in the perpendicular plane, and at oblique angles.

- **Δv ≡ 0 for all `k̂` (to the measured precision) → CANCELLATION (null).**
  Verdict: no dimension-4 gauge birefringence; the operator anisotropy is
  unobservable at leading order. Gauge observability question closed as
  "not dim-4 / consistent"; any residual is at most higher order.
- **Δv ≠ 0 somewhere → NON-NULL, `O(1)` dimension-4 at the operator level.**
  Verdict: a real leading-order anisotropy survives the E+B combination →
  tension flag; escalate to a k-resolved order measurement under full dynamics
  (out of scope for this readout — see §7) to decide whether A=1 renormalization
  suppresses it.

Report `epsilon`, its eigenvalues/axis, and the full `Δv(k̂)` profile, not just
the boolean — the profile is the physics.

## 6. Protocol and cost

- **Field magnitudes:** small `|E|`, `|B|` in the quadratic-response limit
  (mirror `exp_04`'s `EPS = 1e-3`), with two or three magnitudes to confirm the
  field-squared scaling and extract the small-field coefficient cleanly.
- **Orientation sweep:** enough directions to reconstruct the six independent
  components of `epsilon` (and re-confirm `mu-inverse`); exploit the expected
  uniaxial symmetry about `(1,1,-1)` — sweep from the axis through the
  perpendicular plane plus a couple of off-plane directions to verify
  uniaxiality rather than assume it.
- **Lattice size:** **small — this is a static operator measurement, not the
  large-N dispersion sweep.** `exp_04` ran at `N = 20`. The screen inherits that:
  it is **CPU-cheap and does not need the GPU path or large N at all.** This is
  an important consequence of choosing the screen — the first, potentially
  decisive, gauge answer is a minutes-scale CPU job, decoupled from the
  GPU-bound R5 sweep.
- **A=1 exactness:** token-exact throughout, magnetic and electric alike.

## 7. What this readout does and does not settle

- It **settles the leading-order (dimension-4) question** at the operator level:
  cancellation yes/no. In the cancellation case that is a full, clean closure.
- It does **not**, by itself, pin the observable order in the non-cancellation
  case. Establishing whether a surviving `O(1)` operator anisotropy is renormalized
  down to a suppressed `(ka)^2` effect by the full A=1 dynamics (the lesson of
  `exp_01`, where matter-sector operator anisotropy *did* survive into observables)
  would require the k-resolved dispersion measurement, which is deliberately not
  part of this single chosen readout. The screen tells you whether that heavier
  measurement is even needed.

## 8. Acceptance / validation tests

1. **Magnetic regression.** The magnetic block reproduces `exp_04`:
   eigenvalues `{4,4,16}`, axis `(1,1,-1)`, `max|Q − Q_PaperI| = 0`.
2. **Quadratic vanishing.** Both electric and magnetic induced responses go to
   zero quadratically as the field magnitude goes to zero.
3. **Gauge covariance.** A pure-gauge potential (lattice gradient of an arbitrary
   scalar, temporal or spatial) produces zero induced response — the U(1) Ward
   identity, the core correctness check.
4. **Uniaxiality.** `epsilon` is uniaxial about `(1,1,-1)` (or the note records
   the actual symmetry found, if different).
5. **Verdict output.** The driver emits `epsilon`, `mu-inverse`, and `Δv(k̂)`
   with a clear CANCELLATION / NON-NULL classification and the measured precision.

## 9. Scope and home

- **Where:** an `exp_03` driver in this repo (paper-04), consuming dcl-core
  v0.3.0 primitives (`uniform_B_potential`, `external_potential` threading, the
  A=1-exact Peierls hop). The only new code is the temporal-plaquette electric
  estimator (§4) and the trivial uniform-E ramp — both experiment-side.
- **No new dcl-core engine capability is required** for the screen. (Promote the
  uniform-E helper or a canonical in-engine temporal-plaquette readout into
  dcl-core only if it proves reusable.)
- **Green light to implement is still owner-gated**, but the R4 *definition* — the
  thing that was open — is now this note.
