#!/usr/bin/env python
"""exp_02 -- analytic verification of the closed-form optical-axis split.

Backs the kinematic audit row's closed-form ordinary/extraordinary speed
split (notes/closed_form_speed_split.md). This is a *derivation check*,
not an engine simulation: it verifies the closed-form structure factor,
the M_eff = (4/3) P_perp projector identity, the exact eigenphase
dispersion tan(theta) = tan(w/2)/|H_RGB|, and the group-velocity speed
split v_g = (2/3) sin(w) k_perp -- each against an independent direct
computation. No dcl_core dependency: the propagator algebra is the object
under test, and exp_01 already validated it against both engines.

Run:  python src/experiments/exp_02_closed_form_split_check.py
"""
from __future__ import annotations

import numpy as np

# RGB basis vectors (Paper I, octahedral_substrate.tex eq:rgb_vectors)
V = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1]], float)
NHAT = np.array([1.0, 1.0, -1.0]) / np.sqrt(3.0)          # optical axis
PPERP = np.eye(3) - np.outer(NHAT, NHAT)                  # perp projector
M_EFF = np.array([[8, -4, 4], [-4, 8, 4], [4, 4, 8]], float) / 9.0


def H_RGB(k: np.ndarray) -> complex:
    """Structure factor (1/3) sum_V exp(i k.V)."""
    return np.exp(1j * (V @ k)).sum() / 3.0


def H2_closed(k: np.ndarray) -> float:
    """Closed form, eq. (2): (1/9)[3 + 2cos2(ky+kz)+2cos2(kx+kz)+2cos2(kx-ky)]."""
    kx, ky, kz = k
    return (3 + 2 * np.cos(2 * (ky + kz))
            + 2 * np.cos(2 * (kx + kz))
            + 2 * np.cos(2 * (kx - ky))) / 9.0


def theta(k: np.ndarray, w: float) -> float:
    """Mode energy = arg(lambda_+), eq. (1)."""
    s, c = np.sin(w / 2), np.cos(w / 2)
    return np.angle(1j * s + c * abs(H_RGB(k)))


def vg_formula(k: np.ndarray, w: float, h: float = 1e-7) -> np.ndarray:
    """Group velocity, eq. (6): -(1/2)sin(w) grad|H| / (c^2|H|^2 + s^2)."""
    s, c = np.sin(w / 2), np.cos(w / 2)
    u = abs(H_RGB(k))
    grad = np.array([(abs(H_RGB(k + e)) - abs(H_RGB(k - e))) / (2 * h)
                     for e in (h * np.eye(3))])
    return -0.5 * np.sin(w) * grad / (c * c * u * u + s * s)


def vg_fd(k: np.ndarray, w: float, h: float = 1e-7) -> np.ndarray:
    """Direct finite-difference of arg(lambda_+) (independent of vg_formula)."""
    return np.array([(theta(k + e, w) - theta(k - e, w)) / (2 * h)
                     for e in (h * np.eye(3))])


def main() -> int:
    rng = np.random.default_rng(0)
    checks: list[tuple[str, float, float]] = []   # (name, measured, tol)

    # 1. closed-form structure factor vs direct triple sum
    ks = 0.4 * rng.normal(size=(2000, 3))
    err = max(abs(H2_closed(k) - abs(H_RGB(k)) ** 2) for k in ks)
    checks.append(("|H_RGB|^2 closed form vs direct sum", err, 1e-12))

    # 2. |H_RGB|^2 == 1 exactly along the optical axis (all orders)
    err = max(abs(H2_closed(t * np.array([1, 1, -1.0])) - 1.0)
              for t in (0.1, 0.7, 1.5, 3.0))
    checks.append(("|H_RGB|^2 = 1 along (1,1,-1)", err, 1e-12))

    # 3. M_eff = (4/3) P_perp ; eigenvalues {4/3,4/3,0}; zero-vec = axis
    checks.append(("M_eff = (4/3) P_perp", float(np.abs(M_EFF - (4/3)*PPERP).max()), 1e-12))
    evals = np.sort(np.linalg.eigvalsh(M_EFF))
    checks.append(("M_eff eigenvalues {0,4/3,4/3}",
                   float(np.abs(evals - [0, 4/3, 4/3]).max()), 1e-12))

    # 4. exact eigenphase dispersion  tan(theta) = tan(w/2)/|H_RGB|
    for w in (0.1019, 0.5, 1.2):
        err = max(abs(np.tan(theta(k, w)) - np.tan(w / 2) / abs(H_RGB(k)))
                  for k in 0.3 * rng.normal(size=(500, 3)))
        checks.append((f"dispersion tan(th)=tan(w/2)/|H|  (w={w})", err, 1e-12))

    # 5. group-velocity formula vs finite-diff arg(lambda_+)
    w = 0.5
    err = max(float(np.abs(vg_formula(k, w) - vg_fd(k, w)).max())
              for k in 0.2 * rng.normal(size=(200, 3)))
    checks.append(("group velocity (6) vs finite-diff", err, 1e-6))

    # 6. principal speeds: perp coeff (2/3)sin w, axial coeff 0
    w = 0.5
    kperp = PPERP @ np.array([1.0, 0, 0]); kperp /= np.linalg.norm(kperp)
    c_perp = np.linalg.norm(vg_fd(1e-4 * kperp, w)) / 1e-4
    c_axial = np.linalg.norm(vg_fd(1e-4 * NHAT, w)) / 1e-4
    checks.append(("ordinary speed coeff = (2/3) sin w",
                   abs(c_perp - (2/3) * np.sin(w)), 1e-5))
    checks.append(("extraordinary (axial) speed coeff = 0", abs(c_axial), 1e-5))

    width = max(len(n) for n, _, _ in checks)
    ok = True
    for name, measured, tol in checks:
        passed = measured <= tol
        ok &= passed
        print(f"[{'PASS' if passed else 'FAIL'}] {name:<{width}}  "
              f"err={measured:.2e}  (tol {tol:.0e})")
    print("\nexp_02:", "ALL PASS" if ok else "FAILURES PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
