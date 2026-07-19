# The $O_h$ average is a shared Paper I–II assumption, not a Paper IV device

**Status:** STABLE (cross-paper structural observation, 2026-07-18).
**Backs:** the `rem:paper2_inheritance` remark in
`paper/sections/gauge_sector.tex` and the inheritance sentence in
`paper/sections/conclusion.tex`.
**Origin:** author directive "Absolutely Paper IV needs to call this out,"
after tracing the gauge tension to the $V_4$ exclusion and checking Paper II.

---

## The observation

The four-domain average that would isotropize Paper IV's gauge sector
(`oh_domain_average` in `src/utilities/electric_induced_action.py`,
$\langle\varepsilon\rangle = 3I$, $\langle\mu^{-1}\rangle = 8I$) is
**arithmetically identical** to the $O_h$ average Paper II applies to the same
$\{4,4,16\}$ tensor:

- Paper II, `notes/induced_gauge_action_nonabelian.md` lines 45–48:
  $\langle F^\top Q\,F\rangle_{O_h} = (\operatorname{Tr}Q/3)\,F_{ij}F^{ij}/2
  = 8\cdot F_{ij}F^{ij}/2$ — "recovering the Maxwell density."
- $\operatorname{Tr}(Q)/3 = 24/3 = 8 \Rightarrow \langle\mu^{-1}\rangle = 8I$,
  the same as Paper IV's four-domain $\langle Q_B\rangle$.

Democratizing over "which of the four cube body-diagonals is omitted" **is** the
$O_h$ average. So Paper II already "uses all four vectors" — not in the plaquette
loop (which is the same three-vector construction, plaquettes $(1,2),(1,3),(2,3)$),
but in the averaging step it applies immediately after, and needs, to recover
isotropic Maxwell.

## Why this matters (the depth)

Paper II uses that same $O_h$ average for more than Maxwell: it is the averaging
by which the program obtains **emergent Lorentz invariance itself** ($SO(3,1)$
from the $O_h$-averaged Dirac operator — Paper II `CLAUDE.md` "SO(3,1) (dim 6):
emergent Lorentz from $O_h$-averaged Dirac"; `notes/no_spacetime_torsion.md`,
`notes/aut_centralizer_enumeration.md`). So whether the $O_h$ average is
*physically realized* (vs a symmetry of an ensemble the single fixed vacuum does
not sample) is a **foundational question for the whole construction**, not a local
gauge-sector difficulty. Paper IV's induced photon is simply the first place its
cost is quantitative and observable.

### The $48$-vs-$12$ subtlety
The order-$48$ "$O_h$" automorphism of the hop set (`automorphism_discrete.py` in
Paper II) is the **signed-permutation group of the three basis vectors**
$\{\pm V_1,\pm V_2,\pm V_3\}$; only **12** of its 48 elements are orthogonal in
Euclidean $\mathbb{R}^3$. The isotropizing average uses the full combinatorial 48;
a single physical domain realizes only the trigonal $D_{3d}$ (the 12 orthogonal
elements about the omitted diagonal). That gap is where the tension lives.

## Both sectors are excluded as constructed (CORRECTED 2026-07-18 by referee M1/M2)

The earlier framing here — "matter survives via dim-6, only the photon fails" — is
**overturned** by the referee report (majors M1/M2, verified in
`src/experiments/exp_05_matter_sector_order.py`). The honest reconciliation:

- The matter **energy dispersion relative to the rest phase** IS dim-6
  (Planck-suppressed) — true, and it is the sidereal massive-dispersion channel.
- BUT the bare single-tick spinor's **kinetic and level structure** (the quantity
  an isotropy experiment actually compares) is **$O(1)$ anisotropic**, its axial
  band is **exactly flat** (axial transport zero), and its $\omega=0$ amplitude
  filter **accumulates linearly in $a$** (e-folds of days–minutes at $a=\ell_P$).
  So the bare matter sector is **excluded as constructed**, just like the photon.
- **Induced gauge block:** dimension-four tensor, $O(1)$, no suppression — also
  excluded as constructed.

So the two sectors ride the **same** footing: both are $O(1)$-excluded as a single
domain, both share the root (omission of $V_4=(1,1,-1)$), and both need a more
complete construction to escape — an $O_h$-restoring (four-orientation) vacuum for
the gauge loop, the **token→matter emergence map** (+ $\delta p_\text{min}$) for the
spinor, plausibly two faces of one extension. Paper IV now states this as a **no-go**
(title: "Universal Birefringence Cancellation and a Single-Domain No-Go"). The
emergent-Lorentz result of Papers I–II is thus safe only through the emergence map,
not because bare matter is harmless.

## Framing discipline (do NOT overstate)

- This is a **shared foundational assumption being stress-tested**, NOT a claim
  that Paper II erred. Paper II's $O_h$-average is a legitimate, explicitly stated
  construction; Paper IV is the first sector where its single-domain cost is
  dimension-four and therefore observable.
- Attribute the emergent-Lorentz / isotropic-Maxwell-from-$O_h$-average results to
  Paper II (`\cite{menendez2026smderivation}`), not as new Paper IV results.
- Does not change any Paper IV audit status: null split PASS, blocks-as-effective-
  action PART, common-mode FAIL/tension, kinematic PASS.

## Cross-repo action

Return handoff filed to the Paper II session: its $O_h$-average =
four-domain assumption is the shared root; Paper II may want to state (in its own
emergent-Lorentz / induced-Maxwell rows) that the averaging is an ensemble
assumption whose single-domain cost is dimension-six for matter (safe) but
dimension-four for the induced gauge field (Paper IV's tension).
