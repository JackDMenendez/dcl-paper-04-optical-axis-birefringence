# exp_03 -- dynamical, large-N confirmation of the gauge-sector verdict (PLAN)

**Status:** PLAN + validated foundations (2026-07-16). Supersedes the R4
*static screen* framing of `exp_03_R4_cancellation_screen_spec.md` for the
**companion-paper deliverable**: Paper VIII has since delivered the analytic
verdict and the *static* engine read-off, so IV's job is now the **dynamical,
large-N** confirmation, not another static screen. Consumes handoff
`2026-07-16-paper08-paper04-companion-publication`.

---

## 1. Why this exists / what changed

Paper VIII (`dcl-paper-08-electric-induced-action`) delivered, 2026-07-16:

- **Electric block** `eps = P = sum_a V_a V_a^T`, eigenvalues `{1,4,4}`, optical
  axis `(1,1,-1)` **suppressed** -- read off `HopOperator.step` (temporal-plaquette
  holonomy on the engine-recovered `delta_phi = omega + V`) in
  `exp_01_electric_permittivity_extraction.py`.
- **Magnetic block** `mu^-1 = Q_B = adj(P)`, eigenvalues `{4,4,16}`, axis
  **enhanced** -- Paper I App. B / dcl-core `exp_04`.
- **Adjugate theorem** `Q_B = adj(P)` for *any* hop vectors -> the photon
  dispersion `det(K mu^-1 K + w^2 eps) = det(eps) w^2 (w^2 - k^T eps k)^2` is a
  **double transverse root**: gauge-sector vacuum **birefringence cancels**,
  prefactor-independently. VIII also ran a numeric Fresnel sweep (2e4 k, max
  split ~1e-14).

**So the static/holonomy route and the analytic null verdict are DONE (VIII).**
A tensor-level IV redo would *duplicate* VIII. VIII's own honest caveats
(`electric_induced_action.py:69-84`) name what is *not* earned and is IV's to
supply:

1. The **conditional identification** -- that the geometric holonomy tensors
   `(P, Q_B)` are the *observable* `(eps, mu^-1)` governing real propagation --
   is assumed, not shown to survive the **A=1 token renormalization** (the
   `exp_01` lesson: operator-level anisotropy *can* be distorted in observables;
   for the matter sector `exp_01` found it survives cleanly -- the gauge sector
   is untested).
2. The **common-mode vacuum-speed anisotropy**: the shared root gives
   `v^2(k) = k^T eps k in [1,4]` -- an **order-unity (factor ~2) direction-
   dependent vacuum speed**. Whether it is physical (single trigonal domain) or
   `O_h`-restored (isotropic) is undecided. The lattice has **one fixed hop-set**
   (optical axis = the omitted 4th cube body-diagonal), so structurally it is a
   *single domain* and the `O_h` 4-domain average is a fictitious ensemble the
   physical lattice does not realize -> the anisotropy is expected **physical**.
   IV must show this dynamically.

## 2. IV's deliverable (decided 2026-07-16, PM/author)

A **dynamical, large-N** confirmation on the *actual* A=1-renormalized engine:

- **(a) Null polarization split**, confirmed independently by feeding
  **engine-extracted** blocks to IV's own validated dispersion solver (not VIII's
  hand-typed matrices).
- **(b) Common-mode speed anisotropy**: measure it dynamically; confirm the
  single-domain factor-~2 (`v^2 in [1,4]`), **not** `O_h`-restored. This sets
  VIII's separate "vacuum speed isotropy / `O_h` restoration" audit row.
- **(c) A=1 survival**: show the geometric induced-action anisotropy survives the
  engine's multi-tick quantize+renormalize dynamics (the gauge analog of
  `exp_01`).

**Scope honesty (engine limitation).** `core3d` has **no dynamical gauge field**
-- `external_potential`/`vector_potential` are *static* backgrounds, so there is
no literal propagating photon to clock. IV's "dynamical" content is therefore the
**A=1-survival of the induced-action anisotropy in a dynamical *matter* observable
under the static background**, combined with the dispersion-solver verdict from
the engine-extracted blocks. A literal dynamical-photon dispersion would require
adding gauge dynamics to dcl-core (a MAJOR engine extension -- out of scope, flag
to PM if ever wanted).

## 3. Validated foundations (2026-07-16, in scratchpad; to promote into `exp_03`)

- **Fresnel/dispersion solver** (`transverse_speeds`, `sweep`): given `(eps,
  mu^-1)`, returns the two transverse phase speeds `v_+/-(k_hat)` from the
  generalized eigenproblem `-K mu^-1 K E = v^2 eps E`. **Validated:** vacuum ->
  `v=1`; VIII blocks -> max split **1.8e-15** over 2000 directions (null
  confirmed independently); a **detuned control** (break `adj`) -> split **0.5**
  (so a null is not a false pass); `O_h` 4-domain average -> isotropic
  (`<eps>=3I, <mu^-1>=8I`). Single-domain common-mode: `v` from **1.0 on axis to
  2.0 in the perp plane** (the factor-2 anisotropy).
- **Bloch transfer operator `T(k)`** for the bipartite Dirac hop (one even+odd
  period): **matches the real engine to 6e-16** over random `k`; reproduces the
  optical-axis dispersion flatness (`(1,1,-1)` dispersion == `k=0`).
- **Dynamical feasibility** (`dyn_probe.py`, real `TickScheduler`, multi-tick,
  A=1): the field-induced second-order **phase** response is uniaxial about
  `(1,1,-1)`, **B axis-enhanced / E axis-suppressed** (opposite senses, matching
  `{4,4,16}`/`{1,4,4}`), and the anisotropy **grows/persists under multi-tick
  renormalized dynamics** -> the geometric prediction survives A=1. Ratios are
  still `nticks`-dependent -> a **convergent phase-rate estimator** is needed to
  lock the clean tensor (Step 4a below).

## 4. Build steps

- **4a. Convergent dynamical estimator.** *(FINDING 2026-07-16 -- the hard part.)*
  Three real-space readouts were prototyped and **none converges** to the clean
  tensor: (i) wavepacket local-phase 2nd-order response, (ii) return-overlap
  `arg<psi_0|psi_N>` per tick, (iii) uniform-state interior RMS phase. All show
  the correct **qualitative** structure (uniaxial about `(1,1,-1)`; B
  axis-enhanced, E axis-suppressed; opposite senses -> the anisotropy survives
  A=1) but the axis:perp **ratio drifts with `nticks`** (e.g. B: 4.1->7.8->11.9).
  **Root cause:** along the optical axis the free dispersion is FLAT
  (`|H_RGB|=1`), so axis-aligned phases accumulate coherently (secular growth)
  while perpendicular modes spread/dephase -- the real-space phase response
  **conflates the induced action with the free dispersion + gauge/boundary
  structure**. VIII's static read-off sidesteps this (single step, no
  propagation); the *dynamical* clean tensor needs the **k-resolved route**:
  build the perturbed Bloch transfer operator `T(k; A)` (the validated `T(k)` +
  the field as a `k -> k+/-q` coupling), extract the **per-mode second-order
  eigenphase shift**, and **subtract the free part** mode-by-mode before the BZ
  average -> the vacuum-polarization tensor `Pi_00(q->0) -> eps`,
  `Pi_ij -> mu^-1`. Anchor: this route must reproduce `{4,4,16}` magnetically
  before the electric `{1,4,4}` is trusted.
  - **EMBEDDED PHYSICS DECISION (owner):** the BZ mode sum needs a **vacuum /
    mode-filling prescription** (which band(s) of the 2-band non-unitary `T(k)`
    constitute the "sea" whose phase is summed). Paper I's induced action came
    out *geometric* (holonomy, no explicit sea sum), so the prescription must be
    chosen to reproduce that -- this is a theory choice, not a numerics knob, and
    should be settled (possibly with the VIII session) before the extractor is
    trusted. See open question in the checkpoint.
- **4b. Engine-extracted blocks.** From the converged estimator, build
  `(eps, mu^-1)` in the principal basis; confirm eigenvalues `{1,4,4}`/`{4,4,16}`,
  axis `(1,1,-1)`, and the **adjugate relation `mu^-1 = adj(eps)`** from the two
  *independently engine-measured* blocks (a mismatch vs VIII is a RED FLAG to
  reconcile before publishing -- per handoff).
- **4c. Verdict.** Feed engine-extracted blocks -> dispersion solver -> null split
  + common-mode anisotropy profile `v(k_hat)`; classify single-domain vs
  `O_h`-restored.
- **4d. Large-N / GPU.** Convergence study in `N`; run the largest `N` on the GPU
  backend (`BipartiteLattice(backend="gpu")`, fused `hop_average`). Report the
  `N`-scaling; the holonomy blocks are exact at any `N`, so this demonstrates
  **stability/N-independence** of the dynamical readout (not convergence of a
  noisy loop) -- state that honestly.
- **4e. Acceptance tests.** (1) magnetic regression to `{4,4,16}`; (2) quadratic
  vanishing in field; (3) spatial pure-gauge Ward identity -> null; (4)
  uniaxiality about `(1,1,-1)`; (5) detuned control -> split detected; (6)
  adjugate relation from engine blocks; (7) A=1 exactness each tick.
- **4f. Calibration.** Any physical-unit conversion routes through
  `dcl_core.calibration` (per the v0.3.0 discipline); the lattice-unit verdict
  carries none.

## 5. Reconciliation with VIII (companion release)

- IV cites VIII for the derivation + blocks; VIII cites IV for the dynamical
  large-N confirmation (lifts VIII's birefringence row PART->PASS).
- IV's engine-extracted `(eps, mu^-1)` must match VIII's `(P, Q_B)`; a mismatch
  is reconciled before either deposits.
- On landing: file a return handoff to `dcl-paper-08-electric-induced-action`
  with the large-N null result + the common-mode (vacuum-speed) readout so VIII
  writes its held intro/conclusion/abstract and sets its "vacuum speed isotropy"
  row.

## 6. Files

- Solver + Bloch + dynamical estimator -> `src/experiments/exp_03_*.py` (this
  repo), consuming `dcl_core` v0.3.0 (`core3d`, `uniform_B_potential`,
  `external_potential`/`vector_potential` threading, GPU backend).
- Prior static screen `exp_03a_gauge_cancellation_screen.py` stays as the
  density-proxy screen (its opposite-sense finding corroborates the block signs).
