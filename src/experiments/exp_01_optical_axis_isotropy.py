"""exp_01 -- Optical-axis isotropy test for the kinematic birefringence channel.

Audit row: "Kinematic birefringence along (1,1,-1)".

Question
--------
The bipartite octahedral lattice has an anisotropic single-tick spinor
propagator whose structure factor |H_RGB(k)|^2 = 1 - k^T M_eff k is flat
along the optical axis (1,1,-1) (M_eff eigenvalue 0) and curved in the
perpendicular plane (eigenvalue 4/3).  That anisotropy is present in the
*bare* propagator.  The load-bearing question for an observable
prediction is whether the per-tick A=1 renormalization (which both
engines apply) washes it out of the *observable* amplitudes, or whether
it survives.

Observable
----------
Group velocity along the optical axis is degenerate (flat dispersion),
so a momentum-launched packet gives no clean transport contrast.  The
real-space dual is unambiguous and momentum-free: an initially isotropic
pulse must spread anisotropically iff the dispersion is anisotropic.  We
launch a spherical Gaussian (momentum = 0), evolve under per-tick A=1
enforcement, and track the density covariance tensor.  If the anisotropy
survives renormalization the pulse flattens into a pancake perpendicular
to (1,1,-1): var_parallel stays flat while var_perp grows, and the
smallest-variance eigenvector of the covariance aligns with (1,1,-1).

Engines
-------
Run on BOTH dcl_core engines:
  * core3d (integer-token): its _hop_average kernel realises the
    (1/3) sum_RGB exp(i k.V) structure factor the prediction is built
    on -- this is the primary engine.  A=1 is an exact integer identity.
  * core (float amplitude): a different (directed) kernel with
    enforce_unity_spinor renormalization -- an independent cross-check
    that the result is not an artefact of one A=1 scheme.

Dependency: dcl_core >= 0.3.0 (committed pin: virtual-env-requirements.txt;
originally run 2026-06-12 against 0.2.2, results unchanged under the additive
v0.3.0 release).  The canonical Windows venv (C:\\Users\\jackd\\.venv-win)
carries dcl_core v0.3.0.  This experiment is pure lattice-unit (ticks, box
cells, omega) and holds no physical-unit constants; any physical calibration
belongs in dcl_core.calibration, not here.

Usage:  python exp_01_optical_axis_isotropy.py [BOX] [NTICKS]
Default BOX=129, NTICKS=1000 (~1-2 h wall-clock, float massive case the
long pole).  A quick check: python exp_01_optical_axis_isotropy.py 41 80.
"""
import os
import sys
import time
import json
import numpy as np

# ---- config ----
BOX = int(sys.argv[1]) if len(sys.argv) > 1 else 129
NTICKS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
MEAS_EVERY = 5
SIGMA = 2.5
N_UNITS = 10**9                       # core3d resolution (integer magnitude only -- free)
OMEGAS = [0.0, 0.1019]                # photon, free-particle
_HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(_HERE, "..", "..", "data", "exp_01_optical_axis_isotropy_results.npz")
C = BOX // 2
U = np.array([1.0, 1.0, -1.0]); U /= np.linalg.norm(U)   # optical axis (1,1,-1)


def covariance(dn):
    t = dn.sum()
    ax = [np.arange(s) for s in dn.shape]
    c = np.array([(ax[0][:, None, None] * dn).sum() / t,
                  (ax[1][None, :, None] * dn).sum() / t,
                  (ax[2][None, None, :] * dn).sum() / t])
    g = [ax[0][:, None, None] - c[0], ax[1][None, :, None] - c[1], ax[2][None, None, :] - c[2]]
    Cm = np.empty((3, 3))
    for i in range(3):
        for j in range(i, 3):
            Cm[i, j] = Cm[j, i] = (g[i] * g[j] * dn).sum() / t
    return Cm


def summarize(Cm):
    vpar = float(U @ Cm @ U)
    vperp = float((np.trace(Cm) - vpar) / 2.0)
    evals, evecs = np.linalg.eigh(Cm)               # ascending
    align = float(abs(evecs[:, 0] @ U))             # flat axis vs (1,1,-1); 1.0 == aligned
    return vpar, vperp, evals, align


def run_core3d(omega):
    from dcl_core.core3d import BipartiteLattice, DiscreteCausalSession, HopOperator, TickScheduler
    L = BipartiteLattice(shape=(BOX, BOX, BOX))
    s = DiscreteCausalSession.wavepacket(L, N_UNITS, omega, (C, C, C), sigma=SIGMA, momentum=(0, 0, 0))
    hop = HopOperator(L); sch = TickScheduler(lattice=L, hop=hop); sch.register(s)

    def dens():
        a = s.amplitude("R"); b = s.amplitude("L"); return np.abs(a) ** 2 + np.abs(b) ** 2
    rows = []
    for t in range(NTICKS + 1):
        if t % MEAS_EVERY == 0:
            vpar, vperp, evals, align = summarize(covariance(dens()))
            rows.append((t, vpar, vperp, evals[0], evals[1], evals[2], align, s.total_tokens() / N_UNITS))
        if t < NTICKS:
            sch.step()
    return np.array(rows)


def run_core(omega):
    from dcl_core.core import OctahedralLattice, CausalSession
    L = OctahedralLattice(BOX, BOX, BOX)
    s = CausalSession(L, (C, C, C), omega, momentum=(0, 0, 0), is_massless=(omega == 0.0))
    gx, gy, gz = np.indices((BOX, BOX, BOX))
    env = np.exp(-0.5 * ((gx - C) ** 2 + (gy - C) ** 2 + (gz - C) ** 2) / SIGMA ** 2)
    s.psi = env.astype(complex)                      # isotropic, momentum 0
    rows = []
    for t in range(NTICKS + 1):
        if t % MEAS_EVERY == 0:
            dn = s.probability_density()
            vpar, vperp, evals, align = summarize(covariance(dn))
            rows.append((t, vpar, vperp, evals[0], evals[1], evals[2], align, float(dn.sum())))
        if t < NTICKS:
            s.tick(); s.advance_tick_counter()
    return np.array(rows)


if __name__ == "__main__":
    print(f"exp_01 optical-axis isotropy  BOX={BOX} NTICKS={NTICKS} sigma={SIGMA} "
          f"n_units={N_UNITS} omegas={OMEGAS}", flush=True)
    cols = "tick,var_par,var_perp,eval0,eval1,eval2,align_flataxis_to_(1,1,-1),norm_or_tokens"
    out = {"_cols": cols, "_meta": json.dumps({"BOX": BOX, "NTICKS": NTICKS, "SIGMA": SIGMA,
                                               "N_UNITS": N_UNITS, "OMEGAS": OMEGAS})}
    for omega in OMEGAS:
        for engine, fn in [("core3d", run_core3d), ("core", run_core)]:
            key = f"{engine}_omega{omega}"
            t0 = time.time()
            try:
                arr = fn(omega); out[key] = arr; last = arr[-1]
                print(f"[{key}] {time.time()-t0:6.1f}s  final var_par={last[1]:.2f} "
                      f"var_perp={last[2]:.2f} ratio={last[1]/last[2]:.4f} align={last[6]:.4f}", flush=True)
            except Exception:
                import traceback; traceback.print_exc()
            np.savez(OUT, **out)            # incremental save -- partial results survive
    print("saved", os.path.normpath(OUT), flush=True)
