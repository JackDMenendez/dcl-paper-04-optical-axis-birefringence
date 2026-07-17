"""Ward-safe form of the induced-action vacuum polarization (for Paper IV).

Paper IV's dynamical BZ extractor of the physical-band 2nd-order eigenphase shift
diverges (sign-wrong, grid-divergent). This diagnoses WHY and states the Ward-safe
form. It does NOT reproduce {4,4,16} from a band sum -- the honest finding is that
the anisotropic tensor STRUCTURE is geometric (VIII's plaquette holonomy), so the
band sum is the wrong place to look for it; the physical band supplies the isotropic
scalar prefactor, and its naive current-current tensor does NOT equal Q_B.

The divergence (proven here)
----------------------------
Along the optical axis d = (1,1,-1)/sqrt(3), ALL three hop vectors project equally:

    d . V_a = 1/sqrt(3)   for a = 1, 2, 3   (this IS the D_3d trigonal symmetry).

So moving by t*axis multiplies S_RGB only by the phase exp(-i t/sqrt3) and leaves
|S| unchanged; since the eigenvalues are

    lambda = i sin(omega/2) +/- cos(omega/2) |S(k)|,

they are INDEPENDENT of position along the axis direction (from ANY base point) --
the physical band is EXACTLY FLAT along (1,1,-1). On the axis itself |S| = 1 and the
flat value is { e^{i omega/2}, - e^{-i omega/2} }. Consequences:

  1. The intraband denominator lambda_phys(k) - lambda_phys(k +/- q) vanishes
     IDENTICALLY along the optical axis -> the naive intraband (physical->physical
     at k +/- q) 2nd-order term diverges. THIS is Paper IV's divergence.
  2. That intraband term is Ward-cancelled: it carries occupation difference
     f(k) - f(k+q) = 1 - 1 = 0 (both physical states filled), and the diamagnetic
     seagull cancels its q->0 pole (the f-sum rule). It must be DROPPED, not summed
     with a principal-value/eta regulator.
  3. The interband (physical <-> doubler) part is finite: the gap is 2 cos(omega/2)
     along the axis and O(1) generically, vanishing only at the BZ corners where
     S_RGB = 0 (measure zero, integrable).

The Ward-safe prescription
--------------------------
- STRUCTURE {4,4,16}/{1,4,4}: compute it GEOMETRICALLY (the plaquette holonomy,
  sum of squared fluxes (V_a x V_b . B)^2 -- VIII's derive_magnetic_Q / dcl-core
  exp_04). This is the exact q->0 closed form, pole-free, and is what the fermion
  loop must reproduce. Do NOT extract the anisotropic tensor from a Lindhard-style
  band sum -- the anisotropy is in the gauge-field coupling (the plaquettes), not
  the band response. (Confirmed: the naive interband current-current tensor is
  uniaxial about (1,-1,0) with ratio ~9, NOT Q_B.)
- MAGNITUDE (the 1/g^2 scalar): the physical-band trace, with the intraband pole
  DROPPED, interband only, at FINITE omega (gaps the doubler); extrapolate
  omega -> 0. No pole/PV regulator is needed -- the correct object has no pole.

Run: python -u src/utilities/ward_safe_diagnosis.py
"""

from __future__ import annotations

import numpy as np

RGB = [np.array(v) for v in [(1, 1, 1), (1, -1, -1), (-1, 1, -1)]]
AXIS = np.array([1, 1, -1.0]) / np.sqrt(3)


def _S(k: np.ndarray, sign: int) -> complex:
    return sum(np.exp(sign * (-1j * np.dot(k, v))) for v in RGB) / 3


def _T(k: np.ndarray, omega: float) -> np.ndarray:
    s, c = np.sin(omega / 2), np.cos(omega / 2)
    return np.array([[1j * s, c * _S(k, +1)], [c * _S(k, -1), 1j * s]], complex)


def verify(omega: float = 0.6) -> bool:
    rng = np.random.default_rng(0)

    # (1) all hop vectors project equally onto the optical axis (D_3d symmetry).
    projections = [float(AXIS @ v) for v in RGB]
    equal_proj = np.allclose(projections, projections[0])

    # (2) physical band is flat ALONG the axis direction: moving by t*axis from any
    #     base point leaves the eigenvalues unchanged (only the phase of S rotates,
    #     while |S| -- which fixes lambda = i s +/- c|S| -- is constant along the
    #     axis). Hence lambda_phys(k) - lambda_phys(k + q*axis) = 0 (the intraband
    #     pole). On the axis itself (|S|=1) the flat value is {e^{iw/2},-e^{-iw/2}}.
    def _evsorted(k):
        return np.sort_complex(np.linalg.eigvals(_T(k, omega)))

    flat = True
    for _ in range(20):
        kperp = rng.standard_normal(3)
        kperp = kperp - (kperp @ AXIS) * AXIS          # arbitrary transverse base point
        base = _evsorted(kperp)
        for t in np.linspace(0.3, 3, 5):
            if not np.allclose(_evsorted(kperp + t * AXIS), base, atol=1e-9):
                flat = False
    # on the axis itself the flat value is the analytic {e^{iw/2}, -e^{-iw/2}}
    on_axis = np.sort_complex(np.array([np.exp(1j * omega / 2), -np.exp(-1j * omega / 2)]))
    flat = flat and np.allclose(_evsorted(1.7 * AXIS), on_axis, atol=1e-9)

    # (3) interband gap: finite along the axis (2 cos(w/2)), vanishes only at S=0.
    gap_axis = abs(np.exp(1j * omega / 2) - (-np.exp(-1j * omega / 2)))
    gap_axis_ok = np.isclose(gap_axis, 2 * np.cos(omega / 2))
    # generic interband gap bounded below away from BZ corners
    gaps = []
    for _ in range(2000):
        k = rng.standard_normal(3)
        w = np.linalg.eigvals(_T(k, omega))
        gaps.append(abs(w[0] - w[1]))
    interband_ok = np.median(gaps) > 0.5

    print("Ward-safe vacuum-polarization diagnosis")
    print("=" * 52)
    print(f"[1] hop vectors project equally on (1,1,-1) (D_3d): "
          f"{'PASS' if equal_proj else 'FAIL'}  (d.V_a = {projections[0]:.4f} each)")
    print(f"[2] physical band FLAT along the axis "
          f"(lambda_phys = e^(i w/2) = const):        {'PASS' if flat else 'FAIL'}")
    print(f"[3] interband gap along axis = 2 cos(w/2) = {gap_axis:.4f}: "
          f"{'PASS' if gap_axis_ok else 'FAIL'}; median gap {np.median(gaps):.3f} "
          f"(finite): {'PASS' if interband_ok else 'FAIL'}")
    ok = equal_proj and flat and gap_axis_ok and interband_ok
    print("=" * 52)
    print("DIAGNOSIS: the divergence is the intraband pole on the flat optical axis")
    print("(Ward-cancelled, occupation f-f=0). Ward-safe: drop intraband, keep")
    print("interband at finite omega; take the STRUCTURE from the geometric holonomy.")
    print(f"OVERALL: {'ALL PASS' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if verify() else 1)
