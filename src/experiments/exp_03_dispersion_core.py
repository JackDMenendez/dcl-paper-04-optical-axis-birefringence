"""exp_03 dispersion core -- validated building blocks for the gauge-sector
photon-dispersion verdict (the null polarization split + the common-mode
vacuum-speed anisotropy).

This module holds the two foundations that are engine-INDEPENDENT and already
validated, so the k-resolved dynamical extractor (gated on VIII's vacuum/mode-
filling prescription -- see notes/exp_03_dynamical_confirmation_plan.md) can be
built on top of them:

  1. `transverse_speeds` / `birefringence_sweep` -- the Fresnel photon-dispersion
     solver. Given the effective-medium blocks `epsilon` (permittivity) and
     `mu_inv` (inverse permeability), it returns the two transverse polarization
     phase speeds for a propagation direction, hence the birefringence split and
     the common-mode speed. This is what turns engine-extracted blocks into the
     observable verdict.

  2. `T_bloch` -- the Bloch transfer operator of the core3d bipartite Dirac hop
     (one even+odd period). Validated to match the real engine to 6e-16; it is
     the substrate for the perturbed-Bloch vacuum-polarization extractor.

Run as a script to execute the self-tests (all engine-independent):
    python -u src/experiments/exp_03_dispersion_core.py

Dependency: dcl_core >= 0.3.0 (core3d hop geometry). Pure lattice units; no
physical calibration constants appear here (per the v0.3.0 discipline the
(ka)->physical mapping is analysis-only). NumPy + SciPy.
"""
from __future__ import annotations

import sys

import numpy as np
from scipy.linalg import eigh

from dcl_core.core3d.lattice import RGB_VECTORS, CMY_VECTORS

# The optical axis IS the cube body-diagonal absent from the hop set (Paper VIII
# geometry): the sum V1+V2+V3 of the RGB hop vectors, = (1,1,-1).
OPTICAL_AXIS = np.array([1.0, 1.0, -1.0]) / np.sqrt(3.0)

# Paper VIII blocks in the lattice basis (electric_block.tex), for cross-checks:
#   epsilon = P = sum_a V_a V_a^T                 eigenvalues {1,4,4}, axis suppressed
#   mu_inv  = Q_B = adj(P)                         eigenvalues {4,4,16}, axis enhanced
EPS_PAPER8 = np.array([[3.0, -1.0, 1.0], [-1.0, 3.0, 1.0], [1.0, 1.0, 3.0]])
MU_INV_PAPER8 = np.array([[8.0, 4.0, -4.0], [4.0, 8.0, -4.0], [-4.0, -4.0, 8.0]])


# =====================================================================
# 1. Fresnel photon-dispersion solver
# =====================================================================
def _skew(n: np.ndarray) -> np.ndarray:
    """The matrix ``[n]_x`` with ``[n]_x a = n x a`` (the curl operator for a
    plane wave of unit direction ``n``)."""
    x, y, z = n
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def transverse_speeds(k_hat: np.ndarray, epsilon: np.ndarray,
                      mu_inv: np.ndarray) -> tuple[float, float]:
    """Return the two transverse phase speeds ``(v_minus, v_plus)`` for a photon
    propagating along ``k_hat`` in the anisotropic medium ``(epsilon, mu_inv)``.

    The plane-wave Maxwell equations ``k x (mu_inv (k x E)) = -omega^2 epsilon E``
    become, with ``K = [k_hat]_x`` and phase speed ``v = omega/|k|``, the
    generalized symmetric eigenproblem ``A E = v^2 epsilon E`` with
    ``A = -K mu_inv K``. Of the three eigenvalues one is the longitudinal null
    (``k_hat`` direction); the two transverse ones are ``v_-^2 <= v_+^2``.
    Birefringence is ``v_+ != v_-``.
    """
    k_hat = np.asarray(k_hat, float)
    k_hat = k_hat / np.linalg.norm(k_hat)
    K = _skew(k_hat)
    A = -K @ mu_inv @ K
    A = 0.5 * (A + A.T)                       # symmetric by construction
    w = eigh(A, epsilon, eigvals_only=True)   # ascending; w[0] ~ 0 longitudinal
    v2 = np.clip(w[1:], 0.0, None)
    return float(np.sqrt(v2[0])), float(np.sqrt(v2[1]))


def _fibonacci_hemisphere(n: int) -> np.ndarray:
    """``n`` roughly-uniform directions on the upper hemisphere (enough for a
    birefringence/anisotropy sweep given the antipodal symmetry of the tensors)."""
    i = np.arange(n) + 0.5
    phi = np.arccos(1.0 - i / n)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(theta),
                            np.sin(phi) * np.sin(theta),
                            np.cos(phi)])


def birefringence_sweep(epsilon: np.ndarray, mu_inv: np.ndarray,
                        n: int = 2000) -> dict:
    """Sweep directions; return the max polarization split, the common-mode speed
    range (the vacuum-speed anisotropy), and per-direction arrays.

    - ``max_split`` ~ 0  => birefringence CANCELS (null verdict).
    - ``vbar`` spread     => common-mode (direction-dependent) vacuum speed.
    """
    dirs = _fibonacci_hemisphere(n)
    vmi = np.empty(n); vpl = np.empty(n)
    for j, d in enumerate(dirs):
        vmi[j], vpl[j] = transverse_speeds(d, epsilon, mu_inv)
    dv = vpl - vmi
    vbar = 0.5 * (vpl + vmi)
    return dict(dirs=dirs, v_minus=vmi, v_plus=vpl, split=dv, vbar=vbar,
                max_split=float(np.abs(dv).max()),
                vbar_min=float(vbar.min()), vbar_max=float(vbar.max()),
                vbar_anisotropy=float((vbar.max() - vbar.min()) / vbar.mean()))


def oh_domain_average(block: np.ndarray) -> np.ndarray:
    """Average a uniaxial block over the four cube body-diagonal orientations (the
    four trigonal domains). Returns the ``O_h``-symmetrized (isotropic) block --
    the fictitious ensemble average whose isotropy the single fixed lattice does
    NOT realize (used to contrast single-domain vs restored)."""
    diags = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1]], float)
    diags /= np.linalg.norm(diags, axis=1, keepdims=True)
    w = np.linalg.eigvalsh(block)
    idx_axis = int(np.argmin([np.sum(np.isclose(w, wi)) for wi in w]))
    lam_a = w[idx_axis]
    lam_t = np.mean([w[j] for j in range(3) if j != idx_axis])
    acc = np.zeros((3, 3))
    for d in diags:
        proj = np.outer(d, d)
        acc += lam_a * proj + lam_t * (np.eye(3) - proj)
    return acc / len(diags)


# =====================================================================
# 2. Bloch transfer operator of the core3d bipartite Dirac hop
# =====================================================================
def _S_rgb(k: np.ndarray) -> complex:
    """RGB hop Fourier multiplier: ``(1/3) sum_{v in RGB} e^{-i k.v}`` (the
    ``shift(psi,v)(x)=psi(x-v)`` convention gives the ``e^{-i k.v}`` factor)."""
    return sum(np.exp(-1j * np.dot(k, v)) for v in RGB_VECTORS) / 3.0


def _S_cmy(k: np.ndarray) -> complex:
    return sum(np.exp(-1j * np.dot(k, v)) for v in CMY_VECTORS) / 3.0


def T_bloch(k: np.ndarray, omega: float) -> np.ndarray:
    """One-period (even then odd) Bloch transfer matrix on ``(psi_R, psi_L)`` for
    the free hop at wavevector ``k`` and on-site phase ``omega``.

    Even tick (RGB active): ``R' = i s R + c S_RGB L``, ``L' = L``.
    Odd  tick (CMY active): ``L' = c S_CMY R + i s L``, ``R' = R``.
    with ``c = cos(omega/2)``, ``s = sin(omega/2)``. The scheduler renormalizes
    (real, positive) each tick, so the *phases* of this operator's eigenvalues are
    the two-tick dispersion; magnitudes are A=1 bookkeeping. Matches the engine's
    analytic step to ~1e-15.
    """
    c = np.cos(omega / 2.0); s = np.sin(omega / 2.0)
    S = _S_rgb(k); Sc = _S_cmy(k)
    E_op = np.array([[1j * s, c * S], [0.0, 1.0]], dtype=complex)
    O_op = np.array([[1.0, 0.0], [c * Sc, 1j * s]], dtype=complex)
    return O_op @ E_op


# =====================================================================
# Self-tests (engine-independent; run as a script)
# =====================================================================
def _selftest() -> bool:
    ok = True
    np.set_printoptions(precision=6, suppress=True)

    # -- Fresnel: vacuum --
    vm, vp = transverse_speeds([0.3, 0.5, -0.2], np.eye(3), np.eye(3))
    t = abs(vm - 1) < 1e-12 and abs(vp - 1) < 1e-12
    ok &= t
    print(f"[fresnel/vacuum]   v=({vm:.6f},{vp:.6f})  expect (1,1)   {'OK' if t else 'FAIL'}")

    # -- Fresnel: VIII blocks -> null split; adjugate relation --
    adj = np.linalg.det(EPS_PAPER8) * np.linalg.inv(EPS_PAPER8)
    adj_dev = np.abs(adj - MU_INV_PAPER8).max()
    res = birefringence_sweep(EPS_PAPER8, MU_INV_PAPER8, n=2000)
    t = res["max_split"] < 1e-12 and adj_dev < 1e-10
    ok &= t
    print(f"[fresnel/VIII]     max split={res['max_split']:.2e}  adj dev={adj_dev:.2e}  "
          f"=> null birefringence   {'OK' if t else 'FAIL'}")
    print(f"                   common-mode v in [{res['vbar_min']:.4f},{res['vbar_max']:.4f}]  "
          f"anisotropy={res['vbar_anisotropy']:.3f}  (factor-~2, single domain)")

    # -- Fresnel: detuned control MUST detect a split --
    mu_bad = MU_INV_PAPER8.copy(); mu_bad[0, 0] += 3.0
    res_bad = birefringence_sweep(EPS_PAPER8, mu_bad, n=500)
    t = res_bad["max_split"] > 1e-2
    ok &= t
    print(f"[fresnel/control]  detuned max split={res_bad['max_split']:.3e}  "
          f"=> a null is not a false pass   {'OK' if t else 'FAIL'}")

    # -- Fresnel: O_h average -> isotropic --
    eps_avg = oh_domain_average(EPS_PAPER8); mu_avg = oh_domain_average(MU_INV_PAPER8)
    res_avg = birefringence_sweep(eps_avg, mu_avg, n=400)
    t = (abs(np.linalg.eigvalsh(eps_avg) - 3).max() < 1e-9
         and abs(np.linalg.eigvalsh(mu_avg) - 8).max() < 1e-9
         and res_avg["vbar_anisotropy"] < 1e-9)
    ok &= t
    print(f"[fresnel/O_h avg]  <eps>=3I <mu^-1>=8I isotropic, vbar aniso="
          f"{res_avg['vbar_anisotropy']:.1e}   {'OK' if t else 'FAIL'}")

    # -- Bloch T(k): matches the engine analytic step --
    dev = _bloch_vs_engine()
    t = dev < 1e-12
    ok &= t
    print(f"[bloch/engine]     max|T_bloch - T_engine|={dev:.2e} over random k   "
          f"{'OK' if t else 'FAIL'}")

    # -- Bloch T(k): optical-axis dispersion flatness --
    om = 0.3
    ph_gamma = np.sort(np.angle(np.linalg.eigvals(T_bloch(np.zeros(3), om))))
    ph_axis = np.sort(np.angle(np.linalg.eigvals(T_bloch(0.2 * np.sqrt(3) * OPTICAL_AXIS, om))))
    t = np.abs(ph_gamma - ph_axis).max() < 1e-9
    ok &= t
    print(f"[bloch/axis-flat]  |disp(axis) - disp(0)|={np.abs(ph_gamma-ph_axis).max():.2e}  "
          f"(optical-axis flatness)   {'OK' if t else 'FAIL'}")

    print(f"\n{'ALL PASS' if ok else 'A TEST FAILED'}")
    return ok


def _bloch_vs_engine() -> float:
    """Compare T_bloch to the engine's analytic two-tick operator on plane-wave
    R/L basis inputs (renorm is a real scale, so it does not affect the columns
    read at a central site up to a common factor -- here fields are off, so the
    linear operator is read directly)."""
    from dcl_core.core3d import BipartiteLattice, HopOperator

    class _FakeSession:
        def __init__(self, R, L, omega):
            self._R = R; self._L = L; self.omega = omega
        def amplitude(self, which):
            return self._R if which == "R" else self._L

    omega = 0.3
    N = 16
    shape = (N, N, N)
    lat = BipartiteLattice(shape=shape)
    hop = HopOperator(lattice=lat)
    gx, gy, gz = np.indices(shape)
    rng = np.random.default_rng(0)
    worst = 0.0
    for _ in range(6):
        k = rng.uniform(-1.0, 1.0, size=3)
        kx = np.exp(1j * (k[0] * gx + k[1] * gy + k[2] * gz))
        cols = []
        for (R0, L0) in [(kx.copy(), np.zeros_like(kx)), (np.zeros_like(kx), kx.copy())]:
            R, L = R0, L0
            R, L = hop.step(_FakeSession(R, L, omega), "even")
            R, L = hop.step(_FakeSession(R, L, omega), "odd")
            c = tuple(sh // 2 for sh in shape)
            cols.append((R[c] / kx[c], L[c] / kx[c]))
        T_engine = np.array([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]], dtype=complex)
        worst = max(worst, float(np.abs(T_bloch(k, omega) - T_engine).max()))
    return worst


if __name__ == "__main__":
    sys.exit(0 if _selftest() else 1)
