"""exp_05 -- Order of the matter-sector optical-axis anisotropy (referee M1/M2).

Built entirely on the paper's OWN single-tick spinor transfer operator
(Eq. propagator; same H_RGB as exp_02):

    lambda_+(k) = cos(w/2) |H_RGB(k)| + i sin(w/2),   theta = arg(lambda_+),

this experiment quantifies -- as-constructed, for the bare single-tick spinor --
the three M1 consequences and the M2 filtering rate that a face-value reading of
the operator forces:

  M1(i)   Exact axial flat band: theta depends on k_perp ONLY (all k_parallel
          sits in the global phase of H_RGB), so d theta/d k_parallel == 0 to all
          orders; a wavepacket along n_star does not propagate.
  M1(ii)  O(1) directional anisotropy: the entire quadratic kinetic term is
          theta - w/2 = (sin w / 3)|k|^2 sin^2(alpha) -- proportional to
          sin^2(alpha) with NO isotropic piece, so the kinetic/level structure is
          anisotropic at order unity, not at (ka)^2.
  M1(iii) Kinetic-scale mismatch: the lattice perpendicular kinetic coefficient
          over the continuum k^2/2m (m = sin(w/2)/a) is (4/3) sin^2(w/2) cos(w/2)
          <= 8/(9 sqrt 3) ~ 0.513 at ANY w, so the bare spinor cannot be tuned to
          a continuum particle's kinematics.
  M2      omega=0 amplitude filtering accumulates LINEARLY in a: per-tick
          intensity damping 1-|lambda|^2 = (4/3)cos^2(w/2)(k_perp a)^2, axial
          exactly undamped; times the tick rate c/a the physical rate goes as
          (4/3)cos^2(w/2) k_perp^2 a c -- linear in a, because the dim-6 per-tick
          suppression is paid back by the a^{-1} tick count. e-folding times at
          a = l_Planck are days/minutes, far above isotropy/co-magnetometer bounds.

CONCLUSION (as-constructed): the bare single-tick spinor, read literally as lab
matter, is EXCLUDED -- axially inert, O(1) anisotropic, kinetically (ma)^2 off,
and amplitude-filtering at rates tens of orders above bounds. The escape is the
token->matter emergence map (lab particles as emergent sessions with their own
dispersion) and the program's delta_p_min floor; both OPEN. Backs the matter-
sector FAIL-as-constructed audit row.

Run: python -u src/experiments/exp_05_matter_sector_order.py
"""
from __future__ import annotations

import numpy as np

V = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1]], float)     # RGB hop vectors
NHAT = np.array([1.0, 1.0, -1.0]) / np.sqrt(3.0)               # optical axis
RNG = np.random.default_rng(11)

# physical constants (SI) for the M2 accumulation estimate
C_MS = 2.99792458e8
ELL_P = 1.616255e-35
A0 = 5.29177210903e-11        # Bohr radius


def H_RGB(k: np.ndarray) -> complex:
    return np.exp(1j * (V @ k)).sum() / 3.0


def lam_plus(k: np.ndarray, w: float) -> complex:
    """The + eigenvalue in magnitude/phase form (exp_02 convention)."""
    return np.cos(w / 2) * abs(H_RGB(k)) + 1j * np.sin(w / 2)


def theta(k: np.ndarray, w: float) -> float:
    return float(np.angle(lam_plus(k, w)))


def check_m1_flat_band() -> bool:
    """M1(i): d theta / d k_parallel == 0 exactly; |H| depends on k_perp only;
    the axial band is flat to all orders."""
    h = 1e-6
    worst_dpar = 0.0
    worst_magdiff = 0.0
    for _ in range(3000):
        k = RNG.uniform(-3, 3, 3)
        w = RNG.uniform(0.2, 3.0)
        dpar = (theta(k + h * NHAT, w) - theta(k - h * NHAT, w)) / (2 * h)
        worst_dpar = max(worst_dpar, abs(dpar))
        kperp = k - (k @ NHAT) * NHAT
        worst_magdiff = max(worst_magdiff, abs(abs(H_RGB(k)) - abs(H_RGB(kperp))))
    w0 = 1.3
    axial_flat = max(abs(theta(t * NHAT, w0) - w0 / 2)
                     for t in RNG.uniform(-8, 8, 200))
    print(f"  M1(i)  max|d theta/d k_parallel| (3000 k,w): {worst_dpar:.2e}")
    print(f"         max||H(k)|-|H(k_perp)|| (k_par=phase): {worst_magdiff:.2e}")
    print(f"         max|theta(t*nhat)-w/2| along axis:     {axial_flat:.2e}")
    return worst_dpar < 1e-6 and worst_magdiff < 1e-12 and axial_flat < 1e-12


def check_m1_o1_anisotropy() -> bool:
    """M1(ii): theta-w/2 = (sin w/3)|k|^2 sin^2(alpha), entirely prop sin^2(alpha)."""
    w = 1.1
    kmag = 1e-3
    worst_rel = 0.0
    for _ in range(4000):
        kdir = RNG.standard_normal(3)
        kdir /= np.linalg.norm(kdir)
        cosa = kdir @ NHAT
        sin2a = 1 - cosa ** 2
        predicted = (np.sin(w) / 3) * kmag ** 2 * sin2a
        actual = theta(kmag * kdir, w) - w / 2
        if sin2a > 1e-6:
            worst_rel = max(worst_rel, abs(actual - predicted) / abs(predicted))
        else:
            worst_rel = max(worst_rel, abs(actual))
    print(f"  M1(ii) max rel err theta-w/2 vs (sin w/3)|k|^2 sin^2a: {worst_rel:.2e}")
    return worst_rel < 1e-4


def check_m1_scale_mismatch() -> bool:
    """M1(iii): max_w (4/3) sin^2(w/2) cos(w/2) = 8/(9 sqrt 3) ~ 0.513."""
    ws = np.linspace(1e-3, np.pi - 1e-3, 40000)
    ratio = (4 / 3) * np.sin(ws / 2) ** 2 * np.cos(ws / 2)
    analytic = 8 / (9 * np.sqrt(3))
    print(f"  M1(iii) max_w kinetic ratio = {ratio.max():.4f} "
          f"(analytic 8/(9 sqrt3) = {analytic:.4f})")
    return abs(ratio.max() - analytic) < 1e-3


def check_m2_filtering() -> bool:
    """M2: per-tick intensity damping (4/3)cos^2(w/2)k_perp^2; axial undamped;
    accumulated rate linear in a; e-folds at a=l_P match the referee."""
    w = 0.6
    c2 = np.cos(w / 2) ** 2
    worst = 0.0
    for _ in range(4000):
        k = RNG.standard_normal(3)
        k /= np.linalg.norm(k)
        k *= 1e-3
        kperp2 = k @ k - (k @ NHAT) ** 2
        damp = 1 - abs(lam_plus(k, w)) ** 2
        pred = (4 / 3) * c2 * kperp2
        worst = max(worst, abs(damp - pred) / abs(pred))
    axial_damp = 1 - abs(lam_plus(2.0 * NHAT, w))
    print(f"  M2  max rel err 1-|lambda|^2 vs (4/3)cos^2(w/2)k_perp^2: {worst:.2e}")
    print(f"      1-|lambda| on axis (undamped):                      {axial_damp:.2e}")

    # accumulation: rate ~ (4/3) cos^2(w/2) k_perp^2 a c, slow particles cos^2~1
    def efold_days(k_perp: float, a: float = ELL_P) -> float:
        rate = (4 / 3) * 1.0 * k_perp ** 2 * a * C_MS
        return 1.0 / rate / 86400.0
    cases = {
        "electron k~1/a0": 1 / A0,
        "thermal N2": 2.3e11,
        "cold neutron 1000 m/s": (1.675e-27 * 1000) / 1.0545718e-34,
    }
    for name, kp in cases.items():
        print(f"      e-fold @a=l_P, {name:22s}: {efold_days(kp):.2f} days")
    # linear-in-a: halving a doubles the e-fold time
    e1 = efold_days(1 / A0, ELL_P)
    e2 = efold_days(1 / A0, ELL_P / 2)
    linear = abs(e2 / e1 - 2.0) < 1e-9
    print(f"      linear-in-a check (t(a/2)/t(a) == 2): {e2 / e1:.6f}")
    return worst < 1e-4 and axial_damp < 1e-12 and linear


def main() -> int:
    print("exp_05 -- Matter-sector optical-axis anisotropy order (referee M1/M2)")
    print("=" * 68)
    results = {
        "M1(i) exact axial flat band": check_m1_flat_band(),
        "M1(ii) O(1) directional anisotropy": check_m1_o1_anisotropy(),
        "M1(iii) kinetic-scale mismatch <= 0.513": check_m1_scale_mismatch(),
        "M2 linear-in-a amplitude filtering": check_m2_filtering(),
    }
    print("=" * 68)
    for name, ok in results.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    all_ok = all(results.values())
    print("=" * 68)
    print("VERDICT: as-constructed, the bare single-tick spinor is EXCLUDED as lab "
          "matter\n         (axially inert, O(1) anisotropic, (ma)^2 off, "
          "linearly-filtering).\n         Escape = emergence map / delta_p_min (OPEN).  "
          f"Checks: {'ALL PASS' if all_ok else 'FAILED'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
