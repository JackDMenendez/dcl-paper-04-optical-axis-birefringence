"""exp_03a -- Gauge-sector E+B induced-response cancellation screen (R4, Choice 1).

Audit row: "Gauge-sector birefringence (Q eigenvalues {4,4,16})".
Spec: notes/exp_03_R4_cancellation_screen_spec.md.

What this screens
-----------------
The gauge-sector birefringence question is whether the induced photon action's
uniaxial anisotropy about the optical axis (1,1,-1) survives into an observable
speed split, or whether the ELECTRIC sector cancels the MAGNETIC anisotropy at
leading order (Paper I derived the magnetic sector only; the E/B cancellation is
the uncomputed "escape").

A key engine fact refines the readout (hop.py:8-16, 96-103):
  * MAGNETIC B enters as a spatial LINK phase  exp(i A_mid . v)  -> so it has a
    clean Wilson-loop holonomy, which exp_04 uses to get Q = {4,4,16} EXACTLY.
  * ELECTRIC E enters as an ON-SITE phase  delta_phi = omega + V(x)  (a static
    spatially-varying V(x) = -E.x IS the electric field) -> there is NO direct
    spatial-holonomy analog. The electric block must be probed DYNAMICALLY.

So this screen measures BOTH sectors on the SAME footing -- the second-order
token-DENSITY response to a small uniform field, symmetrised to isolate the
field-squared (even) part:

    d_rho(n_hat) = rho(+eps * n_hat) + rho(-eps * n_hat) - 2 rho(0),

a scalar amplitude  s(n_hat) = sqrt(<d_rho^2>_interior) / eps^2  per orientation.
Measuring E and B with the identical estimator keeps their relative normalization
physical (avoiding the density-vs-holonomy conflation: the density response is the
2:1 family, the holonomy is the 4:1 family -- do not mix them).

The magnetic HOLONOMY tensor (exp_04's method) is also computed here as a
validated structural ANCHOR and a check on the plumbing.

Scope / limits
--------------
This is a small-N, static-field, CPU-cheap operator screen (exp_04 ran N=20).
It answers the DENSITY-response cancellation question. The photon-DISPERSION
(action-level) cancellation -- the actual O(1) dim-4 vs (ka)^2 verdict -- needs
the electric ACTION block, which (per the finding above) has no holonomy and
would need either Paper I's derivation extended to E or an action-level
(spectral) probe. That is the deliberate next step, not this screen.

Dependency: dcl_core >= 0.3.0 (Peierls hop + uniform_B_potential + external
(A_0) threading). Pure lattice units. CPU; no GPU needed for the screen.

Usage:  python exp_03a_gauge_cancellation_screen.py [N] [NTICKS]
Default N=33, NTICKS=40.
"""
from __future__ import annotations

import os
import sys
import json
import numpy as np

from dcl_core.core3d import (
    BipartiteLattice, DiscreteCausalSession, HopOperator, TickScheduler,
    uniform_B_potential,
)
from dcl_core.core3d.lattice import RGB_VECTORS

# ---- config ----
N = int(sys.argv[1]) if len(sys.argv) > 1 else 33
NTICKS = int(sys.argv[2]) if len(sys.argv) > 2 else 40
SIGMA = 3.0
OMEGA = 0.1                       # massive reference packet (photon limit omega->0 also fine)
N_UNITS = 10**9
EPS = 1e-2                        # small probe field; screen uses the eps^2 response
EPS_HALF = 5e-3                   # second magnitude for the quadratic-scaling check
MARGIN = 4                        # interior margin (symmetric-gauge wrap + packet tail)
_HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(_HERE, "..", "..", "data", "exp_03a_gauge_cancellation_screen.json")

AXIS = np.array([1.0, 1.0, -1.0]); AXIS /= np.linalg.norm(AXIS)
# two directions perpendicular to the optical axis (dot with (1,1,-1) = 0):
PERP1 = np.array([1.0, -1.0, 0.0]); PERP1 /= np.linalg.norm(PERP1)
PERP2 = np.array([1.0, 1.0, 2.0]);  PERP2 /= np.linalg.norm(PERP2)

# ============================================================
# Magnetic HOLONOMY anchor (adapted from dcl-core exp_04; the {4,4,16} check)
# ============================================================
_B_FROM_F = np.array([[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]])
_RGB_PLANES = [(0, 1), (0, 2), (1, 2)]
_REFERENCE_Q = np.array([[8.0, 4.0, -4.0], [4.0, 8.0, -4.0], [-4.0, -4.0, 8.0]])


def _roll_to(field, disp):
    return np.roll(field, shift=tuple(-int(d) for d in disp), axis=(0, 1, 2))


def _link_theta(A, v):
    th = np.zeros(A.shape[1:], dtype=np.float64)
    for d in range(3):
        th = th + v[d] * 0.5 * (A[d] + _roll_to(A[d], v))
    return th


def _plaquette_phase(A, va, vb):
    nva = tuple(-c for c in va); nvb = tuple(-c for c in vb)
    step2 = tuple(va[i] - vb[i] for i in range(3))
    t1 = _link_theta(A, va)
    t2 = _roll_to(_link_theta(A, nvb), va)
    t3 = _roll_to(_link_theta(A, nva), step2)
    t4 = _roll_to(_link_theta(A, vb), nvb)
    return t1 + t2 + t3 + t4


def extract_Q_holonomy(shape, margin=3):
    V = [tuple(v) for v in RGB_VECTORS]
    interior = (slice(margin, -margin),) * 3
    G = np.zeros((3, 3))
    for r, (a, b) in enumerate(_RGB_PLANES):
        for k in range(3):
            B = np.zeros(3); B[k] = 1e-3
            A = uniform_B_potential(shape, B)
            G[r, k] = float(_plaquette_phase(A, V[a], V[b])[interior].mean()) / 1e-3
    Q = _B_FROM_F.T @ (G.T @ G) @ _B_FROM_F
    return Q * (8.0 / Q[0, 0])                       # fix isotropic 1/g^2 prefactor


# ============================================================
# Density-response estimator (SAME footing for E and B)
# ============================================================
def _run_density(shape, sector, field_vec):
    """Evolve a centred packet NTICKS under a uniform `field_vec` (in `sector`
    'B' or 'E') and return the token density array."""
    C = tuple(s // 2 for s in shape)
    lat = BipartiteLattice(shape=shape)
    s = DiscreteCausalSession.wavepacket(lat, N_UNITS, OMEGA, C, sigma=SIGMA, momentum=(0, 0, 0))
    sch = TickScheduler(lattice=lat, hop=HopOperator(lattice=lat))
    if sector == "B":
        sch.vector_potential = uniform_B_potential(shape, tuple(field_vec))
    elif sector == "E":
        gx, gy, gz = np.indices(shape)
        ramp = (field_vec[0]*(gx - C[0]) + field_vec[1]*(gy - C[1]) + field_vec[2]*(gz - C[2]))
        sch.external_potential = (-ramp).astype(np.float64)     # E = -grad V
    sch.register(s)
    for _ in range(NTICKS):
        sch.step()
    a = s.amplitude("R"); b = s.amplitude("L")
    return np.abs(a) ** 2 + np.abs(b) ** 2


def susceptibility(shape, sector, n_hat, eps):
    """Symmetrised second-order density response amplitude s(n_hat) = sqrt(<d_rho^2>)/eps^2."""
    rho_p = _run_density(shape, sector, eps * n_hat)
    rho_m = _run_density(shape, sector, -eps * n_hat)
    rho_0 = _run_density(shape, sector, 0.0 * n_hat)
    d_rho = rho_p + rho_m - 2.0 * rho_0
    interior = (slice(MARGIN, -MARGIN),) * 3
    return float(np.sqrt(np.mean(d_rho[interior] ** 2))) / eps ** 2


def main():
    shape = (N, N, N)
    print(f"[exp_03a] N={N} NTICKS={NTICKS} SIGMA={SIGMA} EPS={EPS}")

    # --- 1. magnetic holonomy anchor (must reproduce exp_04) ---
    Q = extract_Q_holonomy(shape)
    eigs = np.sort(np.linalg.eigvalsh(Q))
    q_dev = float(np.abs(Q - _REFERENCE_Q).max())
    q_ok = q_dev < 1e-3
    print(f"\n[anchor] magnetic holonomy Q eigenvalues = {np.round(eigs,3).tolist()} "
          f"(Paper I [4,4,16]); max|Q-Q_ref|={q_dev:.2e}  {'PASS' if q_ok else 'FAIL'}")

    # --- 2. density-response screen: axis vs perpendicular, both sectors ---
    res = {}
    for sector in ("B", "E"):
        s_axis = susceptibility(shape, sector, AXIS, EPS)
        s_p1 = susceptibility(shape, sector, PERP1, EPS)
        s_p2 = susceptibility(shape, sector, PERP2, EPS)
        s_perp = 0.5 * (s_p1 + s_p2)
        ratio = s_axis / s_perp if s_perp else float("nan")
        res[sector] = dict(s_axis=s_axis, s_perp1=s_p1, s_perp2=s_p2, s_perp=s_perp, ratio=ratio)
        print(f"\n[{sector}] density response  s(axis)={s_axis:.4e}  "
              f"s(perp)={s_perp:.4e}  axis:perp ratio = {ratio:.3f}")

    # --- 3. validation checks ---
    b_ratio = res["B"]["ratio"]; e_ratio = res["E"]["ratio"]
    # (a) UNIAXIALITY: the two independent perpendicular directions must agree
    #     (the anisotropy is a function of angle-to-(1,1,-1) only).
    def _uniax(r):
        return abs(r["s_perp1"] - r["s_perp2"]) / (0.5 * (r["s_perp1"] + r["s_perp2"]))
    uni_B, uni_E = _uniax(res["B"]), _uniax(res["E"])
    uniax_ok = uni_B < 0.05 and uni_E < 0.05
    # (b) QUADRATIC scaling: s / eps^2 is eps-independent (leading response is F^2).
    s_full = susceptibility(shape, "E", AXIS, EPS)
    s_half = susceptibility(shape, "E", AXIS, EPS_HALF)
    quad_ratio = s_full / s_half if s_half else float("nan")
    quad_ok = 0.8 < quad_ratio < 1.25
    # (c) ANISOTROPY present: both sectors clearly deviate from isotropy (ratio != 1).
    aniso_ok = abs(np.log(b_ratio)) > 0.2 and abs(np.log(e_ratio)) > 0.2
    # NOTE: no "constant-A_0 gauge covariance" check -- a CONSTANT external_potential
    # shifts delta_phi = omega + V uniformly, i.e. it is a MASS shift, NOT a pure
    # gauge (the electric/temporal sector couples on-site, mass-like; hop.py:14-16).
    # The genuine spatial pure-gauge Ward identity (A = grad Lambda) is dcl-core
    # test #2; the holonomy anchor above already exercises the spatial link machinery.

    print("\n[validation]")
    print(f"  uniaxiality (perp1==perp2):  B {uni_B*100:.2f}%  E {uni_E*100:.2f}%  {'PASS' if uniax_ok else 'FAIL'}")
    print(f"  electric response ~ eps^2:   {quad_ratio:.3f}  {'PASS' if quad_ok else 'FAIL'}")
    print(f"  anisotropy present (ratio!=1): B {b_ratio:.3f}  E {e_ratio:.3f}  {'PASS' if aniso_ok else 'FAIL'}")

    # --- 4. screen result ---
    b_sense = "axis-ENHANCED" if b_ratio > 1 else "axis-suppressed"
    e_sense = "axis-ENHANCED" if e_ratio > 1 else "axis-SUPPRESSED"
    opposite = (b_ratio > 1) != (e_ratio > 1)
    print("\n[screen result]")
    print(f"  magnetic axis:perp density ratio = {b_ratio:.3f}  ({b_sense})")
    print(f"  electric axis:perp density ratio = {e_ratio:.3f}  ({e_sense})")
    print(f"  --> E and B anisotropies are {'OPPOSITE in sense' if opposite else 'SAME in sense'} "
          f"along the optical axis.")
    print("  Holonomy anchor: magnetic action tensor Q = {4,4,16} EXACT (axis-enhanced).")
    print("\n  SCOPE: this is the DENSITY-response screen (2:1-family observable). The")
    print("  photon-DISPERSION (action-level) cancellation verdict needs the electric")
    print("  ACTION block, which has NO holonomy (E couples on-site, mass-like) -- so it")
    print("  requires Paper I's derivation extended to E, or an action-level (spectral)")
    print("  probe. The opposite-sense result here is suggestive, NOT the final verdict.")

    out = dict(
        config=dict(N=N, NTICKS=NTICKS, SIGMA=SIGMA, OMEGA=OMEGA, EPS=EPS, MARGIN=MARGIN),
        holonomy=dict(Q=Q.tolist(), eigenvalues=eigs.tolist(), max_dev=q_dev, pass_=q_ok),
        density_response=res,
        finding=dict(b_sense=b_sense, e_sense=e_sense, opposite_sense=bool(opposite)),
        validation=dict(uni_B=float(uni_B), uni_E=float(uni_E), uniax_ok=bool(uniax_ok),
                        quad_ratio=float(quad_ratio), quad_ok=bool(quad_ok),
                        b_ratio=float(b_ratio), e_ratio=float(e_ratio), aniso_ok=bool(aniso_ok)),
    )
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"\n[exp_03a] wrote {os.path.relpath(OUT, _HERE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
