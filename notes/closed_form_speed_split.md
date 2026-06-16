# Closed-form ordinary/extraordinary speed split along (1,1,-1)

**Status:** DERIVED + numerically verified (2026-06-16). Backs the
kinematic audit row's remaining gap ("closed-form ordinary/extraordinary
speed split not yet derived analytically"). Companion check:
`src/experiments/exp_02_closed_form_split_check.py`. Builds directly on
Paper~I §6.4 (`emergent_kinematics.tex`), the propagator `T(k)` and
`M_eff`.

---

## 1. Inputs from Paper I

RGB basis vectors (Paper I, `octahedral_substrate.tex` eq. `rgb_vectors`):

    V1 = (1, 1, 1),  V2 = (1, -1, -1),  V3 = (-1, 1, -1),
    V1 + V2 + V3 = (1, 1, -1)  ==  optical axis  n* = (1,1,-1)/sqrt(3).

Single-tick spinor propagator (Paper I eq. after `eq:hop_expand`):

    T(k) = [[ i sin(w/2),            cos(w/2) H_RGB(k) ],
            [ cos(w/2) H_CMY(k),     i sin(w/2)        ]],
    H_CMY = conj(H_RGB),

with eigenvalues

    lambda_pm(k) = i sin(w/2) +/- cos(w/2) |H_RGB(k)|.            (1)

Here `w` (= omega) is the per-tick Zitterbewegung / mass rate; the rest
mass is `m = sin(w/2)/a`. The photon is `w -> 0`.

## 2. Exact closed-form structure factor

    H_RGB(k) = (1/3) sum_{V in RGB} exp(i k.V).

Using |sum|^2 = 3 + 2 sum_{i<j} cos(k.(Vi - Vj)) with difference vectors
V1-V2 = (0,2,2), V1-V3 = (2,0,2), V2-V3 = (2,-2,0):

    |H_RGB(k)|^2 = (1/9) [ 3
                           + 2 cos(2(k_y + k_z))
                           + 2 cos(2(k_x + k_z))
                           + 2 cos(2(k_x - k_y)) ].               (2)

Exact, all orders in k. Verified vs the direct triple sum to 5.6e-16 over
2000 random k (exp_02).

**On-axis flatness (all orders).** For k = t (1,1,-1) every argument in
(2) vanishes, so |H_RGB|^2 = 1 *exactly* for all t. No dispersion along
the optical axis -- the extraordinary direction is frozen.

## 3. The anisotropy is a pure perpendicular projector

Second-order expansion of (2):

    |H_RGB(k)|^2 = 1 - k^T M_eff k + O(k^4),
    M_eff = (1/9) [[8,-4,4],[-4,8,4],[4,4,8]].

The clean closed form (verified, machine precision):

    M_eff = (4/3) ( I - n* n*^T ) = (4/3) P_perp,                 (3)

i.e. **4/3 times the projector onto the plane perpendicular to the
optical axis**. Eigenvalues {4/3, 4/3, 0}, the 0 along n*. Hence the
dispersion depends only on the perpendicular wavevector component:

    |H_RGB(k)|^2 = 1 - (4/3) |k_perp|^2 + O(k^4),
    k_perp = P_perp k = k - (k.n*) n*.                           (4)

This is the structural heart of the uniaxial birefringence: **only
k_perp disperses; k_parallel is inert.**

## 4. Exact eigenphase dispersion

The mode energy (phase advance per tick) is theta(k) = arg(lambda_+).
From (1), Re lambda_+ = cos(w/2)|H_RGB|, Im lambda_+ = sin(w/2):

    tan theta(k) = tan(w/2) / |H_RGB(k)|.                        (5)

Exact, all orders. Verified to 1e-16 (exp_02). At k=0, |H_RGB|=1 gives
theta = w/2 (the rest-mass Zitterbewegung phase). Off-axis |H_RGB| < 1
raises theta -- the perpendicular modes carry more phase per tick.

Note |lambda_+|^2 = sin^2(w/2) + cos^2(w/2)|H_RGB|^2 <= 1, with equality
only where |H_RGB| = 1 (on axis or k=0). The sub-unit modulus off-axis is
exactly what the per-tick A=1 renormalization restores; the physical
content is carried by the phase theta, and exp_01 already confirmed the
anisotropy survives that renormalization in observables.

## 5. Closed-form group-velocity (speed) split

Differentiating (5):

    v_g(k) = grad_k theta
           = -(1/2) sin(w) grad|H_RGB|
             / ( cos^2(w/2)|H_RGB|^2 + sin^2(w/2) ).             (6)

Exact; matches finite-difference of arg(lambda_+) to machine precision
(exp_02). Since grad|H_RGB| = grad(|H_RGB|^2)/(2|H_RGB|) and, from (4),
grad(|H_RGB|^2) = -(8/3) k_perp + O(k^3), the small-k limit is

    v_g(k) = (2/3) sin(w) k_perp + O(k^3).                       (7)

**Principal speeds (ordinary / extraordinary).** Write k at angle alpha
to the optical axis, |k_perp| = |k| sin(alpha):

    ordinary (k perpendicular, alpha = 90deg):  |v_g| = (2/3) sin(w) |k|,
    extraordinary (k parallel, alpha = 0):      |v_g| = 0,
    general direction:                           |v_g| = (2/3) sin(w) |k| sin(alpha).   (8)

The closed-form speed split is therefore

    Delta v == v_ord - v_extra = (2/3) sin(w) |k|,               (9)

with optical axis n* = (1,1,-1)/sqrt(3) the degenerate (frozen,
extraordinary) direction. The sin(alpha) law (8) is the angular
signature. Verified: perpendicular coefficient (2/3) sin(w) and axial
coefficient 0 to machine precision (exp_02).

## 6. The photon limit (open modeling choice -- flagged)

The group-velocity split (9) scales as sin(w) and therefore **vanishes
for the massless photon (w -> 0)**. This is consistent with exp_01's
design note: along the optical axis the dispersion is flat (infinite
effective mass), so a momentum-launched photon packet gives no clean
transport contrast -- which is why exp_01 measured real-space *spreading*
(the (4/3)|k_perp|^2 dispersion curvature of (4)) rather than transport.

So there are two distinct, both closed-form, anisotropy measures:

  (a) **dispersion-curvature split** (universal, w-independent):
      coefficient 4/3 perpendicular vs 0 axial, eq. (4). Shared by the
      photon and the massive sector. This is what exp_01 confirmed
      observable.
  (b) **group-velocity speed split** (massive sector): eq. (8)-(9),
      proportional to sin(w), zero for the photon.

**Decision (2026-06-16): both, stated jointly.** The kinematic claim
names *both* observables -- the group-velocity split (b) and the universal
dispersion-curvature split (a) -- as the same uniaxial structure read off
two observables. The audit row is flipped to PASS on that basis: (a) is
what exp_01 observed (photon + massive, w-independent); (b) is the
massive-sector velocity (zero for the photon). The math for both is
closed-form and verified. See `paper/sections/kinematic_channel.tex`
(Remark rem:photon_limit).

## 7. Numerical verification summary (exp_02)

| Check | Result |
|---|---|
| closed form (2) vs direct triple sum, 2000 random k | max err 5.6e-16 |
| \|H_RGB\|^2 = 1 along (1,1,-1), t in {0.1..3.0} | = 1 to 1e-15 |
| M_eff = (4/3) P_perp; eigvals {4/3,4/3,0}; 0-vec = (1,1,-1) | exact |
| dispersion identity tan th = tan(w/2)/\|H\|, random k | max err 1e-16 |
| group velocity (6) vs finite-diff arg(lambda_+) | machine precision |
| perp speed coeff (2/3)sin w; axial coeff 0 | exact |
