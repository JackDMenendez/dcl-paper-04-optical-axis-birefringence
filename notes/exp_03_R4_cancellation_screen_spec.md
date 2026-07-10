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

The electric field is the temporal/tick-direction gauge sector: the hop's
`external_potential` is "the temporal (`A_0`) gauge phase" (dcl-core
`core3d/gauge.py:11-12`), and a uniform electric field along a direction `n̂`
is a spatial ramp of that potential, `A_0(r) = − E · r`. There is **no
`uniform_E_potential` helper yet** — it is a one-line ramp constructor,
recommended to live experiment-side first (promote to `gauge.py` only if reused).

The electric analog of `exp_04`'s spatial plaquette is a **temporal plaquette**:
a loop that steps along an RGB link vector `V_a` in space, advances one tick,
returns along `−V_a`, and steps back one tick. Its holonomy encodes the electric
field projected on `V_a` (the object `F_{0i}` in continuum language). Summing the
squared temporal-plaquette phases over the RGB link vectors, in exact analogy to
`extract_Q`, gives the electric quadratic form `E · epsilon · E` and hence the
permittivity tensor `epsilon`.

**This temporal-plaquette construction is the one genuinely new estimator to
build and validate** — everything else is reuse. Two implementation notes:

- Unlike the magnetic plaquette (pure geometry of the spatial `A`), the temporal
  plaquette involves the tick direction, so it is evaluated with the engine's
  one-tick evolution under `external_potential` present, kept **A=1 token-exact**
  (the integer-residual machinery must stay conserving with the temporal phase).
- **Cross-check hypothesis (do not assume):** by the same RGB geometry the
  electric block is expected to be uniaxial about `(1,1,-1)` as well, but with a
  *different* eigenvalue pattern than the magnetic `{4,4,16}`. Whether the two
  patterns cancel the leading birefringence is precisely the open question — it
  is **not** obvious by inspection, which is why the screen is worth running.

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
