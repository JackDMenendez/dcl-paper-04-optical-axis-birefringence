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

## Why matter survives but the induced photon does not

A difference of dimension, not of averaging:

- **Matter (spinor) sector:** residual anisotropy about $(1,1,-1)$ is the
  **dimension-six, Planck-suppressed scalar** correction (Paper IV's kinematic
  channel). Empirically viable on a single fixed domain *without* any averaging —
  which is the real reason Paper II's emergent-Lorentz result is safe, not the
  average being physical.
- **Induced gauge block:** a **dimension-four tensor** ($\varepsilon=\{1,4,4\}$,
  $\mu^{-1}=\{4,4,16\}$), $O(1)$, no suppression. Only a genuinely
  $O_h$-restoring vacuum (four-orientation / more symmetric hop set) removes it.

So the two sectors ride different footings. The average Papers I–II could invoke
harmlessly for matter cannot be invoked for the induced gauge field, and both
share the same root: the arbitrary omission of the fourth diagonal $V_4=(1,1,-1)$,
which is exactly the optical axis Paper IV studies.

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
