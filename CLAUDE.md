<!-- markdownlint-disable MD022 MD025 MD033 MD060 -->
# CLAUDE.md -- Working Brief for Claude Code

> Project: Paper VIII -- The Electric Induced-Action Block

This file is the project memory for Claude Code. Keep it updated so a
new conversation can continue work without the full chat history.

---

## CURRENT STATUS (2026-07-16) -- v0.1-DRAFT (derivation done, analytic; PART)

**Headline result (analytic; referee-reviewed 2026-07-16).** Method (a) succeeded. The
electric block is `epsilon = P = sum_a V_a V_a^T`, eigenvalues `{1,4,4}`, optical axis
`(1,1,-1)` **suppressed** -- the exact mirror of the magnetic `{4,4,16}` (axis enhanced),
sign-consistent with Paper IV `exp_03a`. The covariant completion is the theorem
`mu^{-1} = Q_B = adj(epsilon)` (proven for general hop vectors). Given `(eps,mu^{-1}) =
(P,Q_B)`, the photon dispersion is a **double transverse root** `w^2 = k^T eps k`, so the
polarization split `~ |eps_a mu_a - eps_p mu_p| = |1*16-4*4| = 0`: **gauge-sector vacuum
birefringence CANCELS** -- prefactor-independent and geometry-general. Verifier:
`src/utilities/electric_induced_action.py` (all conditional checks PASS) + numeric sweep
(2e4 random `k`, split `< 1e-14`).

**Two honest gaps keep this at PART, not PASS** (referee findings, do NOT overclaim):
1. `eps = P` is analytic-only -- derived from the standard temporal-plaquette holonomy but
   with **no engine-level extraction** (the mirror of dcl-core `exp_04`). The temporal
   holonomy is `(V_a . E) * a_t`, not unit weight; `a_t = 1` is set only to display the
   structure. Closing this (a dcl-core experiment reading `P` off the engine's on-site
   `V(x)` + Peierls hop) is the path to the unconditional verdict.
2. The shared dispersion `w^2 = k^T eps k` gives a **factor-~2 directional anisotropy of
   the vacuum `c`** (common to both polarizations -- NOT birefringence, but not small). Its
   `O_h`-isotropy restoration is a separate open question; do not sell the null as a clean
   polarimetry result.

**Headline claim (to be earned):** the A=1 lattice has a well-defined *electric*
induced-action block -- a permittivity `epsilon` and the covariant completion of the
gauge response -- derivable from the tick rule, matching the already-exact *magnetic*
block. **Now derived analytically (PART); engine confirmation outstanding.**

**Why this paper exists.** Paper IV's gauge-sector photon-dispersion birefringence
*verdict* cannot be rendered without it. The engine couples E and B **asymmetrically**:
magnetic `B` is a spatial link phase -> clean Wilson-loop holonomy -> the exact
magnetic `Q`-tensor (eigenvalues `{4,4,16}`, optical axis `(1,1,-1)`; Paper I App. B,
reproduced by dcl-core `exp_04`). Electric `E` enters as an **on-site, mass-like**
`delta_phi = omega + V(x)` -> there is **no electric Wilson-loop analog**. The covariant
electric action block (the `epsilon`) exists in **neither Paper I nor Paper II**, and
there is **no symmetry shortcut** (the framework establishes only spatial `O_h`, not the
Lorentz boosts `K_a`, which are not in the discrete centralizer -- Paper II audit table).
So the electric block is genuinely new theory. Discovered via Paper IV `exp_03a`
(the static E+B cancellation screen, paper-04 commit `a238896`): magnetic response is
**axis-enhanced**, electric **axis-suppressed** about `(1,1,-1)` -- opposite senses,
suggestive of a cancellation, but density response is NOT the photon action, so it is
not a verdict.

**Derivation method -- TBD (two candidates):**
- **(a)** Paper I App. B's magnetic plaquette approach extended to the
  electric/temporal-plaquette sector.
- **(b)** an action-level spectral (`Tr ln T`) probe.

**Audit rows:** the magnetic anchor is `PASS` (inherited/verified, now also derived from
first principles here); the electric block, the covariant `(epsilon, mu^{-1})` completion,
and the birefringence verdict are all `PART` (analytic + symbolic + numeric, gaps
documented) -- upgraded from `STUB` on 2026-07-16.

**Next concrete action:** the analytic derivation is done. The path to PASS is the
**engine cross-check (mirror of dcl-core `exp_04`)**: extract `epsilon = P` numerically from
core3d's on-site `V(x)` coupling combined with the Peierls hop, confirming the tick rule
realizes the temporal plaquette with holonomy `~ V_a . E`. This is a dcl-core experiment --
likely a handoff to a dcl-core session. Secondary: the paper body is still scaffold
placeholders; the derivation section presenting the above is unwritten.

**Scope gate:** this paper is HELD-upstream of Paper IV v1.0 (PM ruling 2026-07-09):
Paper IV v1.0 waits on this verdict. Board issue #23 (project 6); blocks #13/#17/#18/#19.

---

## What This Project Is

A symbolic-derivation paper (Paper VIII of the A=1 Discrete Causal Lattice series). It
derives the electric sector of the lattice's induced gauge action -- the permittivity and
the covariant `F_{mu nu} F^{mu nu}` completion -- so that the gauge-sector photon
dispersion (and hence the birefringence verdict of Paper IV) becomes computable. Every
claim is backed by a runnable sympy script under `src/utilities/` whose printed output the
audit table cites; the magnetic `{4,4,16}` result is the built-in consistency anchor.

---

## Paper Title and Theme

**Title:** The Electric Induced-Action Block: Permittivity and the Covariant Completion
of the Lattice Gauge Response.

**Core theme / framing:** the lattice gives magnetism a clean Wilson-loop but hands
electricity an on-site mass-like coupling; completing the gauge response to a covariant
`(epsilon, mu^{-1})` pair is the missing derivation that decides whether the lattice's
vacuum birefringence cancels (framework consistent) or persists (a real tension). One
derivation, a binary physical consequence.

---

## Audit Table Status

| Row | Status | What it claims |
|---|---|---|
| Magnetic induced-action `Q`-tensor `{4,4,16}` (anchor) | PASS | Paper I App. B / dcl-core `exp_04`; `max\|Q - Paper_I_Q\| = 0`; re-derived here |
| Electric induced-action block `epsilon = P = {1,4,4}`, axis suppressed | PART | temporal-plaquette holonomy; analytic + symbolic, matches `exp_03a` sign. Gap: no engine extraction (mirror of `exp_04`) |
| Covariant completion `mu^{-1} = Q_B = adj(epsilon)` | PART | adjugate identity proven for general vectors. Gap: relative `eps`:`mu^{-1}` normalization (`a_t`, `1/g^2`) |
| Gauge-sector birefringence verdict: **cancels** (conditional) | PART | double-root theorem + 2e4-`k` numeric; gates Paper IV #18/#17/#19. Gaps: unconditional needs `eps=P` engine-verified; residual speed anisotropy |

Mirror of `paper/sections/audit_table.tex` -- update both together. The claim-auditor
agent treats `audit_table.tex` as the authority.

---

## Conventions

- **Status legend.** `PASS` / `PART` / `STUB` / `FAIL` (front-matter of `paper/main.tex`).
- **File naming.** Sections: `paper/sections/<topic>.tex`. Notes: `notes/<topic>.md`.
  Derivation/verification scripts: `src/utilities/<topic>.py`. Experiments (if any):
  `src/experiments/exp_NN_<name>.{py,md}`.
- **Cross-references.** `\label{}` + `\ref{}`/`\autoref{}`, never hard-coded numbers.
- **Bibliography.** `paper/paper-bib/references.bib`; `\bibliographystyle{unsrt}`.
- **Verification-script discipline.** Every audit row that claims a derived result names a
  `src/utilities/*.py` (or `exp_NN`) whose printed output backs it. `python audit_universe.py`
  is the roll-up. A claim without a runnable verifier cannot be `PASS`.
- **SymPy-generated equations (use when it makes sense).** When a paper equation is a
  *derived* symbolic result -- not definitional prose -- generate its LaTeX from the verifying
  SymPy expression via `sympy.latex()` rather than hand-transcribing it. Emit the fragments to
  auto-generated `paper/sections/generated/*.tex` files that the section `.tex` files
  `\input`, so the paper's equations are provably identical to what the verification script
  computed and cannot drift from it. (Same pattern the generator-zoo uses to emit its
  catalogue table.) Apply judgment: this is for the load-bearing derived equations (the
  magnetic `Q`, the electric block, the covariant `(epsilon, mu^{-1})` form), not every inline
  symbol. `src/utilities/electric_induced_action.py::write_latex_fragments` is the working
  exemplar (it emits the magnetic `Q`); the electric block follows the same route once derived.

## Documentation convention for code

Every non-trivial line of physics code says what it **is** in the theory, not just what it
does in the program: name the mathematical object, cite the section/equation, use "IS" for
exact correspondences and "approximates" for continuum limits.

---

## Release flow

See `release_notes/README.md`. Summary: CI green -> update `CITATION.cff` -> draft
`release_notes/vX.Y*.md` -> **Zenodo deposit first (DOI into `\thanks{}` + `CITATION.cff`)**
-> commit -> tag -> GitHub Release.

---

## What NOT to Change

- The magnetic `{4,4,16}` anchor values -- they are inherited from Paper I App. B and are
  the consistency check; if a derivation step breaks them, the step is wrong, not the anchor.
- The audit table's role as canonical PASS/STUB authority.

---

## Cross-references (series)

- **Paper I** (`dcl`, doi:10.5281/zenodo.20078529) -- App. B magnetic `Q`-tensor (anchor).
- **Paper II** (`dcl-paper-02-sm-derivation`, doi:10.5281/zenodo.20292158) -- gauge structure;
  `notes/induced_gauge_action_nonabelian.py` is the closest existing derivation to extend.
- **Paper IV** (`dcl-paper-04-optical-axis-birefringence`) -- the downstream consumer; its
  gauge verdict gates on this paper. See its `notes/exp_03_R4_cancellation_screen_spec.md`.
- **dcl-core** (v0.3.0) -- `exp_04` (magnetic Q holonomy) is the numerical cross-check.

---

## Notes Index

`notes/README.md` -- conventions for notes/.

- `notes/electric_block_derivation.md` -- the derivation plan: the E/B asymmetry, why no
  electric holonomy, the two method candidates, and the consistency anchor. Start here.
