import numpy as np, sympy as sp

rng = np.random.default_rng(7)
V1, V2, V3 = np.array([1,1,1]), np.array([1,-1,-1]), np.array([-1,1,-1])
Vs = [V1, V2, V3]
n_star = np.array([1,1,-1])/np.sqrt(3)

print("== 1. Structure factor closed form (Eq 2) ==")
def H2_direct(k):
    s = sum(np.exp(1j*k@V) for V in Vs)/3
    return abs(s)**2
def H2_closed(k):
    kx,ky,kz = k
    return (3 + 2*np.cos(2*(ky+kz)) + 2*np.cos(2*(kx+kz)) + 2*np.cos(2*(kx-ky)))/9
errs = [abs(H2_direct(k)-H2_closed(k)) for k in rng.uniform(-3,3,(2000,3))]
print("max |direct-closed| over 2000 random k:", max(errs))
ts = rng.uniform(-10,10,50)
print("max |H2-1| along axis k=t(1,1,-1):", max(abs(H2_closed(t*np.array([1,1,-1]))-1) for t in ts))

print("\n== 2. M_eff = (4/3) P_perp (Eq 3) ==")
kx,ky,kz = sp.symbols('kx ky kz', real=True)
H2s = sp.Rational(1,9)*(3 + 2*sp.cos(2*(ky+kz)) + 2*sp.cos(2*(kx+kz)) + 2*sp.cos(2*(kx-ky)))
quad = sp.expand(sp.series(H2s.subs({kx:sp.Symbol('t')*kx, ky:sp.Symbol('t')*ky, kz:sp.Symbol('t')*kz}), sp.Symbol('t'), 0, 3).removeO().coeff(sp.Symbol('t'),2))
M = sp.Matrix(3,3, lambda i,j: 0)
vars_ = [kx,ky,kz]
for i in range(3):
    for j in range(3):
        M[i,j] = -sp.Rational(1,2)*sp.diff(quad, vars_[i], vars_[j]) * (-1)  # quad = -k^T M k
Meff = -sp.Matrix(3,3, lambda i,j: sp.Rational(1,2)*sp.diff(quad, vars_[i], vars_[j]))
Pperp = sp.eye(3) - sp.Matrix([1,1,-1])*sp.Matrix([[1,1,-1]])/3
print("M_eff =", Meff.tolist())
print("M_eff == (4/3)P_perp:", sp.simplify(Meff - sp.Rational(4,3)*Pperp) == sp.zeros(3,3))

print("\n== 3. Group-velocity formula (Eq 6) ==")
w, Hs = sp.symbols('omega H', positive=True)
theta = sp.atan(sp.tan(w/2)/Hs)
dtheta = sp.simplify(sp.diff(theta, Hs))
claimed = -sp.Rational(1,2)*sp.sin(w)/(sp.cos(w/2)**2*Hs**2 + sp.sin(w/2)**2)
print("d(theta)/dH matches Eq(6) kernel:", sp.simplify(dtheta - claimed) == 0)

print("\n== 4. Gauge blocks (Eqs 10,12), eigenvalues, adjugate ==")
QB = sum(np.outer(np.cross(a,b), np.cross(a,b)) for a,b in [(V1,V2),(V1,V3),(V2,V3)])
eps = sum(np.outer(V,V) for V in Vs)
print("Q_B =\n", QB)
print("eps =\n", eps)
print("eig(Q_B):", np.sort(np.linalg.eigvalsh(QB)), " eig(eps):", np.sort(np.linalg.eigvalsh(eps)))
print("Q_B n* :", QB@np.array([1,1,-1]), " eps n* :", eps@np.array([1,1,-1]))
adj_eps = np.linalg.det(eps)*np.linalg.inv(eps)
print("max|adj(eps)-Q_B| =", np.abs(adj_eps-QB).max(), "; det(eps) =", np.linalg.det(eps))

print("\n== 5. Adjugate theorem symbolically for GENERAL hop vectors (Thm 3.2) ==")
a = sp.symbols('a1:4'); b = sp.symbols('b1:4'); c = sp.symbols('c1:4')
A, B, C = sp.Matrix(a), sp.Matrix(b), sp.Matrix(c)
Msym = sp.Matrix.hstack(A,B,C)
eps_sym = A*A.T + B*B.T + C*C.T
QB_sym = sp.zeros(3,3)
for X,Y in [(A,B),(A,C),(B,C)]:
    cr = X.cross(Y)
    QB_sym += cr*cr.T
print("Q_B == adj(eps) for general vectors:", sp.simplify(QB_sym - eps_sym.adjugate()) == sp.zeros(3,3))

print("\n== 6. Fresnel factorization (Thm 3.4 / Eq 14) numeric, random eps,k,gamma ==")
def kcross(k):
    return np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
ok = True
for trial in range(200):
    R = rng.normal(size=(3,3)); E = R@R.T + 0.5*np.eye(3)   # random SPD eps
    g = rng.uniform(0.2, 3.0)
    k = rng.normal(size=3)
    adjE = np.linalg.det(E)*np.linalg.inv(E)
    K = kcross(k)                      # FULL k, not k-hat
    # det(K mu^-1 K + w^2 eps) as poly in x=w^2: compute at sample points and compare
    target = lambda x: np.linalg.det(K@(g*adjE)@K + x*E)
    claimed = lambda x: np.linalg.det(E)*x*(x - g*(k@E@k))**2
    xs = rng.uniform(0, 50, 6)
    if max(abs(target(x)-claimed(x))/(1+abs(claimed(x))) for x in xs) > 1e-8:
        ok = False; print("FAIL trial", trial); break
print("det(K gamma*adj(eps) K + w^2 eps) == det(eps) w^2 (w^2 - gamma k^T eps k)^2 (200 random trials):", ok)
# with unit k-hat in K but full k in root -- show it breaks (the Eq-14 notation issue)
k = rng.normal(size=3); khat = k/np.linalg.norm(k)
R = rng.normal(size=(3,3)); E = R@R.T + 0.5*np.eye(3); g = 1.3
adjE = np.linalg.det(E)*np.linalg.inv(E); K = kcross(khat)
x = 7.0
lhs = np.linalg.det(K@(g*adjE)@K + x*E); rhs = np.linalg.det(E)*x*(x - g*(k@E@k))**2
print("with K=[khat]x but root gamma k^T eps k (paper's literal Eq 14 notation): mismatch ->", abs(lhs-rhs)>1e-6)

print("\n== 7. Impedance-matched reading: mu ∝ eps ==")
mu_inv = adj_eps  # gamma=1, lattice blocks
mu = np.linalg.inv(mu_inv)
print("mu * det(eps) == eps ? max diff:", np.abs(mu*np.linalg.det(eps) - eps).max())

print("\n== 8. O_h averaging (Eq 17) ==")
diags = [np.array(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(1,1,-1)]]
import itertools
eps_list, qb_list = [], []
for subset in itertools.combinations(range(4),3):
    Vsub = [diags[i] for i in subset]
    eps_list.append(sum(np.outer(v,v) for v in Vsub))
    qb_list.append(sum(np.outer(np.cross(x,y),np.cross(x,y)) for x,y in itertools.combinations(Vsub,2)))
print("<eps> =\n", sum(eps_list)/4)
print("<Q_B> =\n", sum(qb_list)/4)
print("gamma for proportional closure: <QB> = g*adj(<eps>):", (sum(qb_list)/4)[0,0]/ (np.linalg.det(sum(eps_list)/4)*np.linalg.inv(sum(eps_list)/4))[0,0])
print("Sum over ALL four diagonals V V^T =\n", sum(np.outer(v,v) for v in diags))

print("\n== 9. Photon speed range check (Sec 3.5) ==")
vals = np.linalg.eigvalsh(eps)
print("v^2/gamma range =", vals.min(), "to", vals.max(), "; vmax/vmin =", np.sqrt(vals.max()/vals.min()))

print("\n== 10. Back-of-envelope: omega=0 filtering accumulation rate ==")
lP = 1.616e-35; c = 3e8
def rate(k_perp, a=lP):   # per-second relative damping between k_perp and axis-aligned components
    return (4/3)*k_perp**2 * a * c    # (4/3)(k a)^2 per tick * (c/a) ticks/s, cos^2~1
cases = {
 "electron in H (k~1/a0=1.9e10 /m)": 1.89e10,
 "thermal N2 molecule (k~2.3e11 /m)": 2.3e11,
 "cold neutron 1000 m/s (k~1.6e10 /m)": 1.67e-27*1000/1.055e-34,
}
for name,k in cases.items():
    r = rate(k)
    print(f"  {name}: rate={r:.2e}/s, e-fold={1/r:.2e} s = {1/r/86400:.2f} days")
age = 4.35e17
k_mol = 2.3e11
a_needed = 1/((4/3)*k_mol**2*c*age)
print(f"  lattice spacing needed so N2 e-fold > age of universe: a < {a_needed:.2e} m = {a_needed/lP:.2e} l_P")