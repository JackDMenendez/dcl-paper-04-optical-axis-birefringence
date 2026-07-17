"""exp_03 -- gauge-sector induced-action blocks from the engine geometry, and the
photon-dispersion verdict (null birefringence + common-mode speed anisotropy).

Framing (endorsed by Paper VIII, handoffs 2026-07-17-paper08-to-paper04-*):
the induced Maxwell action factors as

    ANISOTROPIC STRUCTURE (geometry, exact, pole-free)  x  ISOTROPIC SCALAR (1/g^2).

The anisotropic tensors eps, mu^-1 are read from the engine's hop GEOMETRY -- the
plaquette / temporal-plaquette holonomies (this file) -- NOT from a dynamical
momentum-space fermion-loop sum. The single-object dynamical (Tr ln T /
orbital-susceptibility) tensor extraction is a STATED OPEN ITEM (a naive band sum
is Ward-divergent on the flat optical axis and, once regularized, yields the wrong
object -- uniaxial about (1,-1,0), not the optical axis; confirmed independently by
IV and VIII, see notes/exp_03_dynamical_confirmation_plan.md). The overall scalar
1/g^2 is the deferred coupling (Paper I / VIII); this file exposes STRUCTURE.

What this computes, all from the engine:
  * MAGNETIC  mu^-1 = Q_B : the spatial plaquette holonomy of `uniform_B_potential`
    (the dcl-core exp_04 route). Eigenvalues {4,4,16}, optical axis (1,1,-1)
    ENHANCED.
  * ELECTRIC  eps  = P    : the temporal plaquette holonomy read off the engine's
    on-site coupling delta_phi = omega + V(x) (the Paper VIII exp_01 route, which
    exercises HopOperator.step). Eigenvalues {1,4,4}, optical axis SUPPRESSED.
  * The adjugate relation mu^-1 = adj(eps) from the two engine-extracted blocks.
  * The VERDICT: feed (eps, mu^-1) to the dispersion solver -> null polarization
    split (birefringence CANCELS) + the common-mode vacuum-speed anisotropy
    (single trigonal domain, factor ~2; the O_h 4-domain average, a fictitious
    ensemble the fixed lattice does not realize, is isotropic).

The blocks are normalized to a common scale (magnetic diag -> 8, as exp_04 does)
so only STRUCTURE is compared -- the 1/g^2 magnitude is out of scope.

Dependency: dcl_core >= 0.3.0. Pure lattice units. CPU; the holonomy is exact in
the interior at any N (no large-N/GPU needed for STRUCTURE). NumPy.

Run:  python -u src/experiments/exp_03_geometric_blocks.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

from dcl_core.core3d import (
    BipartiteLattice, DiscreteCausalSession, HopOperator, uniform_B_potential,
)
from dcl_core.core3d.lattice import RGB_VECTORS

# Reuse the validated dispersion solver (Fresnel) from the core module.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp_03_dispersion_core import (  # noqa: E402
    birefringence_sweep, oh_domain_average, OPTICAL_AXIS,
)

SHAPE = (16, 16, 16)
MARGIN = 3          # interior margin excluding the symmetric-gauge wrap layer
EPS = 1e-3          # small probe field; extraction is linear -> value-independent

# F=(F12,F13,F23) <-> B map (matches exp_04): B_k = 1/2 eps_kij F_ij.
_B_FROM_F = np.array([[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]])
_RGB_PLANES = [(0, 1), (0, 2), (1, 2)]


# ============================================================
# shared Peierls holonomy helpers (identical convention to the engine hop)
# ============================================================
def _roll_to(field, disp):
    """field(x + disp) indexed at x (periodic)."""
    return np.roll(field, shift=tuple(-int(d) for d in disp), axis=(0, 1, 2))


def _link_theta(A, v):
    """Peierls link phase A_mid . v for the x-v -> x hop, A_mid = 1/2(A(x)+A(x-v))."""
    th = np.zeros(A.shape[1:], dtype=np.float64)
    for d in range(3):
        th = th + v[d] * 0.5 * (A[d] + _roll_to(A[d], v))
    return th


# ============================================================
# MAGNETIC block mu^-1 = Q_B : spatial plaquette holonomy (exp_04 route)
# ============================================================
def _plaquette_phase(A, va, vb):
    """Bipartite spatial-plaquette holonomy x -> x+va -> x+va-vb -> x-vb -> x."""
    nva = tuple(-c for c in va); nvb = tuple(-c for c in vb)
    step2 = tuple(va[i] - vb[i] for i in range(3))
    return (_link_theta(A, va)
            + _roll_to(_link_theta(A, nvb), va)
            + _roll_to(_link_theta(A, nva), step2)
            + _roll_to(_link_theta(A, vb), nvb))


def extract_mu_inv(shape=SHAPE, margin=MARGIN):
    """mu^-1 = Q_B off the engine's `uniform_B_potential` Peierls links."""
    V = [tuple(v) for v in RGB_VECTORS]
    interior = (slice(margin, -margin),) * 3
    G = np.zeros((3, 3))
    for r, (a, b) in enumerate(_RGB_PLANES):
        for k in range(3):
            B = np.zeros(3); B[k] = EPS
            A = uniform_B_potential(shape, B)
            G[r, k] = float(_plaquette_phase(A, V[a], V[b])[interior].mean()) / EPS
    Q = _B_FROM_F.T @ (G.T @ G) @ _B_FROM_F
    return Q * (8.0 / Q[0, 0])          # normalize the shared 1/g^2 (diag -> 8)


# ============================================================
# ELECTRIC block eps = P : temporal plaquette holonomy off HopOperator.step
# ============================================================
def _uniform_E_potential(shape, E_vec):
    """A_0(x) = -E . (x - center); the engine's on-site external_potential."""
    origin = np.array([(s - 1) / 2.0 for s in shape])
    coords = np.indices(shape, dtype=np.float64) - origin.reshape(3, 1, 1, 1)
    return -(E_vec[0] * coords[0] + E_vec[1] * coords[1] + E_vec[2] * coords[2])


def _engine_delta_phi(hop, session, psi_R, V):
    """Recover delta_phi = omega + V(x) from a real HopOperator.step:
    Im(psi_R_new)/psi_R = sin(delta_phi/2). Exercises the tick operator's coupling."""
    psi_R_new, _ = hop.step(session, "even", external_potential=V, vector_potential=None)
    ratio = np.asarray(psi_R_new).imag / psi_R.real
    return 2.0 * np.arcsin(np.clip(ratio, -1.0, 1.0))


def extract_eps(shape=SHAPE, margin=MARGIN, omega=0.0):
    """eps = P off the engine's on-site delta_phi coupling. Returns (eps, fidelity)."""
    lattice = BipartiteLattice(shape=shape)
    n = 2 * int(np.prod(shape))
    session = DiscreteCausalSession(lattice=lattice, n_units=n, omega=omega)
    session.N_RGB[...] = 1; session.N_CMY[...] = 1
    session.phi_RGB[...] = 0.0; session.phi_CMY[...] = 0.0
    hop = HopOperator(lattice=lattice)
    psi_R = np.asarray(session.amplitude("R"))
    V_hops = [tuple(v) for v in RGB_VECTORS]
    interior = (slice(margin, -margin),) * 3
    G = np.zeros((3, 3)); fidelity = 0.0
    for a in range(3):
        for k in range(3):
            E = np.zeros(3); E[k] = EPS
            Vpot = _uniform_E_potential(shape, E)
            dphi = _engine_delta_phi(hop, session, psi_R, Vpot)
            fidelity = max(fidelity, float(np.abs(dphi - (omega + Vpot))[interior].max()))
            theta = dphi - _roll_to(dphi, V_hops[a])          # temporal holonomy = V_a . E
            G[a, k] = float(theta[interior].mean()) / EPS
    P = G.T @ G
    return P * (2.0 / P[0, 0]), fidelity   # normalize so P matches {1,4,4} scale (diag->2)


# ============================================================
# driver
# ============================================================
def _eigs(M):
    return np.sort(np.linalg.eigvalsh(M))


def _axis_eigenvector(M, want_min):
    vals, vecs = np.linalg.eigh(M)
    idx = int(np.argmin(vals) if want_min else np.argmax(vals))
    v = vecs[:, idx]
    return v / np.abs(v).max()


def main():
    print(f"[exp_03] geometric induced-action blocks from the engine  SHAPE={SHAPE}\n")

    mu_inv = extract_mu_inv()
    eps, fidelity = extract_eps()
    eps_massive, _ = extract_eps(omega=0.3)

    mu_eig = _eigs(mu_inv); eps_eig = _eigs(eps)
    # normalize eps to {1,4,4} display scale using its own suppressed eigenvalue
    eps_disp = eps / eps_eig[0]
    mu_disp = mu_inv / (mu_inv[0, 0] / 8.0) / 4.0   # already diag->8; show {4,4,16}? keep as is

    print("MAGNETIC  mu^-1 = Q_B (spatial plaquette holonomy, uniform_B_potential):")
    print(f"  eigenvalues = {np.round(mu_eig, 3).tolist()}   (Paper I {{4,4,16}})")
    ax_mu = _axis_eigenvector(mu_inv, want_min=False)
    print(f"  enhanced axis = {np.round(ax_mu, 3).tolist()}   (optical axis (1,1,-1))")

    print("\nELECTRIC  eps = P (temporal plaquette holonomy off HopOperator.step):")
    print(f"  eigenvalues (norm) = {np.round(_eigs(eps_disp), 3).tolist()}   ({{1,4,4}})")
    ax_eps = _axis_eigenvector(eps, want_min=True)
    print(f"  suppressed axis = {np.round(ax_eps, 3).tolist()}   (optical axis (1,1,-1))")
    print(f"  engine coupling fidelity max|dphi-(omega+V)| = {fidelity:.2e}  (a_t=1)")
    print(f"  omega-cancellation max|P(0)-P(0.3)| = {np.abs(eps - eps_massive).max():.2e}")

    # adjugate relation from the two engine-extracted blocks
    adj = np.linalg.det(eps) * np.linalg.inv(eps)
    # bring adj to mu^-1's normalization (both diag->8 after /adj[0,0]*8)
    adj_n = adj * (8.0 / adj[0, 0])
    commute = np.abs(eps @ mu_inv - mu_inv @ eps).max()
    print("\nADJUGATE  mu^-1 = adj(eps)  (two engine blocks):")
    print(f"  [eps, mu^-1] = {commute:.2e}  (commute -> shared eigenbasis)")
    print(f"  max|adj(eps)_norm - mu^-1| = {np.abs(adj_n - mu_inv).max():.2e}")

    # VERDICT: feed engine blocks (on a common scale) to the dispersion solver.
    # put both on the physical scale eps={1,4,4}, mu^-1={4,4,16}:
    eps_v = eps / eps_eig[0]
    mu_v = mu_inv                                   # already diag 8 -> {4,4,16}
    res = birefringence_sweep(eps_v, mu_v, n=2000)
    print("\nVERDICT (dispersion solver on the engine-extracted blocks):")
    print(f"  null polarization split: max|v+ - v-| = {res['max_split']:.2e}  "
          f"-> birefringence CANCELS")
    print(f"  common-mode vacuum speed v in [{res['vbar_min']:.4f}, {res['vbar_max']:.4f}] "
          f"(single domain, factor {res['vbar_max']/res['vbar_min']:.2f})")
    avg = birefringence_sweep(oh_domain_average(eps_v), oh_domain_average(mu_v), n=400)
    print(f"  O_h 4-domain average (fictitious ensemble): common-mode aniso "
          f"= {avg['vbar_anisotropy']:.1e} -> isotropic")

    print("\nSCOPE: STRUCTURE only (geometry); the isotropic scalar 1/g^2 is the")
    print("deferred coupling. The single-object dynamical (Tr ln T) tensor extraction")
    print("is a STATED OPEN ITEM -- see notes/exp_03_dynamical_confirmation_plan.md.")

    ok = (np.allclose(mu_eig, [4, 4, 16], atol=1e-6)
          and np.allclose(_eigs(eps_disp), [1, 4, 4], atol=1e-6)
          and commute < 1e-6 and np.abs(adj_n - mu_inv).max() < 1e-6
          and res['max_split'] < 1e-9 and fidelity < 1e-9)
    print(f"\n{'ALL PASS' if ok else 'CHECK FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
