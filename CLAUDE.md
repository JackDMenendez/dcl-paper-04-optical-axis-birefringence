<!-- markdownlint-disable MD022 MD025 MD033 MD060 -->
# CLAUDE.md -- Working Brief for Claude Code

> Project: Paper~IV of the A=1 Discrete Causal Lattice series --
> Optical-Axis Birefringence on the A=1 Discrete Causal Lattice

This file is the project memory for Claude Code. Keep it updated so a
new conversation can continue work without the full chat history.

---

## CURRENT STATUS (2026-07-18) -- v1.0 RELEASED

> **UPDATE 2026-07-18 (d) -- v1.0 RELEASED (DOI 10.5281/zenodo.21435952).** Author
> decision: publish this paper first (v1.0, final) so Papers I & II can cite its DOI,
> then publish new versions of those two. Release done: title-page `\thanks{}` +
> `CITATION.cff` + release notes carry DOI `10.5281/zenodo.21435952` (reserved on Zenodo);
> tag `v1.0` pushed; GitHub Release created with the PDF asset
> (`.../releases/tag/v1.0`). Build clean (36 pp). CITATION.cff Paper I DOI reconciled to
> `10.5281/zenodo.20613677` (was stale `20078529`). **STILL PENDING (user, on Zenodo):**
> upload the final `build/Paper.pdf` (now carries the DOI on the title page) to the
> reserved deposit and **click Publish** -- until then the DOI is reserved but not live.
> Then grab the Zenodo **concept DOI** for the Papers I/II cross-citations. **NEXT
> (after Zenodo publish):** new versions of Papers I & II citing Paper IV; and the parked
> Paper II handoff on the shared O_h-average root. Remaining follow-on scope (documented
> in `release_notes/v1.0.md`): emergence map, dynamical Tr ln T tensor, O_h-restoring
> vacuum, nonlinear-QM analysis, editorial trims. See memory `paper04-v1.0-released.md`.

> **UPDATE 2026-07-18 (c) -- NO-GO REVISION (referee report M1/M2 verified; matter also
> excluded as-constructed; title changed).** A full external referee report
> (`notes/referee-report-paper4-v0.1.md` + verifier `src/utilities/verify.py`, both
> committed) recommended MAJOR REVISION: all algebra correct, but the paper UNDER-claimed
> consequences. Author decisions: **verify M1/M2 first, then FAIL-as-constructed for matter
> + adopt a NO-GO framing.** M1/M2 INDEPENDENTLY VERIFIED from the paper's own transfer
> operator (`src/experiments/exp_05_matter_sector_order.py`, ALL PASS): the bare single-tick
> spinor has (M1i) an **exact axial flat band** (axial transport identically zero), (M1ii)
> an **O(1) directional kinetic anisotropy** ($\theta-\omega/2=\tfrac13\sin\omega|k|^2\sin^2\alpha$,
> no isotropic piece -> Hughes-Drever excludes at zeroth order), (M1iii) kinetic/continuum
> ratio $\le 8/(9\sqrt3)\approx0.513$; and (M2) an $\omega=0$ amplitude filter that
> **accumulates LINEARLY in $a$** (e-folds electron ~5 d, N$_2$ ~49 min, neutron ~7 d at
> $a=\ell_P$). **KEY CORRECTION:** the old "matter is safe because dim-6" claim is
> OVERTURNED -- dim-6 is only the energy-vs-rest anisotropy; the observable kinetic/level
> structure is O(1), so **bare matter is excluded as-constructed just like the photon**.
> Both escape only via a fuller construction ($O_h$-restoring four-orientation vacuum for the
> gauge loop; **token->matter emergence map + $\delta p_\text{min}$** for the spinor). Applied
> (build 33 pp, clean): title -> *"Birefringence Cancellation and a Single-Domain
> No-Go"*; abstract/intro/conclusion = survive-vs-excluded; new `kinematic_channel.tex`
> `subsec:as_constructed` (Props `flat_band` + `filtering`); audit table = kinematic PASS
> *(substrate)* + NEW **matter FAIL-as-constructed** row; falsifiability matter channels
> corrected (each sector INDEPENDENTLY O(1)-excluded; observability no longer rests on
> "matter is dim-6"); Collins et al. 2004 (`collins2004`) cited. **Referee majors STILL
> OPEN (v1.0 queue):** M4 (Cauchy-Binet / impedance-matching antecedent citations + "sits on
> the impedance-matched point automatically" slogan), M5 (Ward-safe band-sum -> appendix;
> fill Appendix A/B stubs), M6 (A=1 nonlinear-QM / signaling: Weinberg/Gisin/Polchinski),
> and minors (Eq 14 $K=[k]_\times$ not $[\hat k]_\times$; Table 1/1.1; define status
> semantics; exp_04 name collision; abstract length; repetition trim). See memory
> `paper04-nogo-m1m2-matter-excluded.md`.

> **UPDATE 2026-07-18 (b) -- GAUGE-SECTOR TENSION, published honestly (author decision).**
> The 2.a computation (board #27) is done: the induced photon common-mode speed anisotropy
> `v^2=k^T eps k`, `eps={1,4,4}`, is **O(1) and dimension-4 (NOT suppressed)** -- three
> independent routes (geometric holonomy; Ward-safe physical-band vacuum polarization,
> traceless/iso ~0.5 and q-independent; density response `exp_03a`). So for the physical
> vacuum as the single fixed trigonal domain, it is a marginal CPT-even `k_F` Lorentz
> violation **EXCLUDED** by cavity/Michelson-Morley isotropy bounds (~1e-18) -- observable
> because MATTER does not share it (matter anisotropy is dim-6, so the sectors ride
> different light cones). **ROOT (author insight):** the anisotropy is the single tensor
> `sum_a V_a V_a^T = {1,4,4}`, O(1) only because the hop set is THREE of the four cube
> body-diagonals (omitting `V_4=(1,1,-1)`); the FOUR-diagonal set = `4*I` (isotropic). The
> optical axis and the gauge tension share this one origin -- the arbitrary V_4 exclusion /
> single-domain choice. **Why matter survives:** its leading term is a SCALAR (dim-6
> anisotropy, viable); the induced photon block is a TENSOR (dim-4, O(1)) -- emergent
> Lorentz invariance does not descend to the induced gauge sector. **RESOLUTION (open,
> foundational):** the formalism admits four-axis / higher-dim / polygonal hop topologies;
> a four-orientation VACUUM would restore O_h for the induced gauge loop while matter keeps
> its dim-6 axis (decoupling). Whether it preserves A=1/Dirac is a Paper-I-level open
> question. **DECISION (author, 2026-07-18): publish Paper IV with the tension honestly
> stated** (abstract + falsifiability section + conclusion + audit reworked; gauge
> common-mode audit row = `FAIL` as-single-domain / open otherwise). **SCOPE: does NOT
> touch** the birefringence null (passed), the adjugate theorem, the kinematic dispersion,
> or Bell/other program results. Builds clean (make paper, 25 pp). See
> `notes/gauge_anisotropy_root_and_resolution.md`, `notes/gauge_common_mode_order.md`,
> memory `paper04-gauge-tension-v4-exclusion.md`.

> **UPDATE 2026-07-18 -- FALSIFIABILITY SECTION ADDED (multi-channel map); the
> birefringence null is now framed as a PASSED falsifiable prediction.** Executes the
> author's "do both" decision (handoffs `2026-07-18-paper04-falsifiability-do-both-decision`
> + `-birefringence-null-is-a-passed-falsifier`, consumed). New
> `paper/sections/falsifiability.tex` (wired into `main.tex`): (1) **the birefringence
> null is a PASSED falsifiable prediction** -- the framework FORBIDS optical-axis vacuum
> birefringence (`thm:doubled_root`), it is tightly bounded + unobserved, and the same
> datum EXCLUDES the CPT-odd (dim-5) birefringent LV rivals while corroborating the
> CPT-even non-birefringent class. Do NOT call it "not a falsifier" / "consistency null"
> (that was the earlier draft's error, corrected). Two guardrails: prospectively
> non-discriminating; corroborated-AND-conditional on the blocks. (2) Multi-channel
> falsifiability map (table): birefringence (passed) / kinematic massive dispersion
> (PART, dim-6, Planck-suppressed, distinctive SIDEREAL signature + neutrinos) / omega=0
> magnitude-filtering anisotropy (PART, real observable) / gauge-sector photon
> common-mode dispersion (**OPEN, contingent** on the Tr ln T effective-action derivation
> + O_h restoration, which may null it -- do NOT assert as a bound). (3) SME placement
> (odd-dim CPT-odd birefringent / even-dim non-birefringent dispersive) verified vs
> Kostelecky-Mewes; bib adds K-M 2009, LHAASO 2024, K-Russell tables. Intro + conclusion
> + audit falsifiability row reframed to match; `notes/falsifiability_and_sme_mapping.md`
> reconciled (the dim-6 PHOTON c^(6) mapping re-filed under the GAUGE channel, since the
> omega=0 massless spinor limit does NOT disperse; kinematic = massive). **2.a (gauge
> photon dispersion) is tracked FOLLOW-ON** (same effective-action + O_h program as the
> VIII revision; board #17/#18/#19). Builds clean (make paper, 23 pp). See memory
> `paper04-falsifiability-multichannel-map.md`.

> **UPDATE 2026-07-17 (b) -- PAPER VIII MERGED IN; RETITLED; EXTERNAL REVIEW
> RESOLVED.** Per user + PM (handoff `2026-07-17-execute-iv-viii-merge-into-paper04`,
> consumed), Paper~VIII (electric induced-action block) is **merged into this paper**
> and this repo is the home (slug unchanged). VIII folded in via `git subtree`
> (history preserved, merge commit `bdc7bf3`); its SymPy derivation scripts +
> generated fragments now live in `src/utilities/` + `paper/sections/generated/`
> (`exp_04_electric_permittivity_extraction.py` is VIII's engine eps read-off);
> VIII's derivation absorbed into the unified `paper/sections/gauge_sector.tex`;
> `paper08/` scaffolding removed; `dcl-paper-08` archived read-only (tombstone).
> Board: #23 closed as merged-into-#13; #13 retitled.
> **Retitle:** *Optical-Axis Anisotropy on the A=1 Discrete Causal Lattice: Kinematic
> Dispersion and the Gauge-Sector Birefringence Cancellation.*
> **External review (2026-07-17, `2026-07-17-paper04-paper08-external-review`)
> corrections applied:** (1) "birefringence" is now RESERVED FOR THE GAUGE SECTOR --
> the kinematic channel is **directional dispersion anisotropy** (Prop.\ renamed
> "axial--transverse group-velocity contrast"); the non-unitary transfer operator
> means the eigenphase$\to$group-velocity reading needs the A=1 normalization
> argument, at $\omega=0$ the surviving curvature is of the eigenvalue MAGNITUDE
> (attenuation, not proven photon dispersion), and the massless-spinor$\to$photon
> identification is NOT claimed. (2) Gauge blocks are **geometric candidates**
> (vertex verified via `HopOperator.step`, NOT the quadratic effective action
> $\Gamma^{(2)}$; a $D_{3d}$ form has TWO free coefficients so the 1:4 ratio is not
> symmetry-forced); dispersion prefactor is $\det\varepsilon$ (not 16); proportional
> closure $\mu^{-1}=\gamma\,\mathrm{adj}(\varepsilon)$; the EXACT adjugate fails
> $O_h$ averaging ($\mathrm{adj}(3I)=9I\neq8I$); "constitutive closure" not
> "covariant completion"; a common $1/g^2$ does NOT set the photon speed (relative
> normalization does). (3) Audit table is now a **three-way split**: null
> polarization split (conditional on the blocks) = PASS; blocks as the dynamical
> effective action = PART; common-mode/$O_h$ isotropy = PART. (4) "independent
> confirmation" softened to "independent code-path verification" (same
> framework/engine). **Affirmed anchor kept:** $Q_B=\mathrm{adj}(P)$, $P=MM^T$,
> doubled transverse root (reviewer independently recomputed). Builds clean
> (pdflatex+bibtex, 17 pp); claim-auditor faithful. **Reviewer verdict was
> working-draft; the paper is revised per review but NOT yet submission-ready**
> (external literature + the deeper physics items -- the group-velocity/photon
> derivation and the dynamical $\mathrm{Tr}\ln T$ tensor -- remain). See memory
> `paper-viii-merged-into-paper-iv.md`.

> **UPDATE 2026-07-17 -- GAUGE BIREFRINGENCE VERDICT = PASS (null split);
> tensor = geometry x scalar; dynamical Tr ln T tensor is a stated OPEN item.**
> After the exp_03 build + two VIII exchanges (handoffs
> `2026-07-17-paper08-to-paper04-ward-safe-answer` / `-ward-open-decision`,
> consumed): IV extracts BOTH induced-action blocks from the engine GEOMETRY
> (`src/experiments/exp_03_geometric_blocks.py`, ALL PASS) --
> $\mu^{-1}=Q_B=\{4,4,16\}$ (spatial plaquette holonomy), $\varepsilon=P=\{1,4,4\}$
> (temporal plaquette holonomy off `HopOperator.step`, fidelity 4e-19), adjugate
> $\mu^{-1}=\mathrm{adj}(\varepsilon)$ confirmed (5e-15). The Fresnel solver on the
> engine blocks gives the **null polarization split** ($\max|v_+-v_-|=1.6\times10^{-15}$;
> detuned control 0.5) -> **gauge birefringence CANCELS (audit row PASS)**, and the
> anisotropy **survives A=1** (dynamical, correct senses). Separate row: the
> **common-mode vacuum speed** is direction-dependent ($v^2\in[1,4]$, single-domain
> factor ~2; $O_h$ average is a fictitious ensemble) -> **PART** (isotropy-restoration
> open). **Framing (author-endorsed): STRUCTURE (geometry, from-engine) x SCALAR
> ($1/g^2$, deferred).** **STATED OPEN ITEM (do NOT claim; possible follow-on):** the
> single-object DYNAMICAL ($\mathrm{Tr}\ln T$ / orbital-susceptibility) tensor
> extraction -- a naive band sum is Ward-divergent (intraband pole on the flat
> optical axis) and yields the WRONG object (uniaxial about $(1,-1,0)$); IV and VIII
> independently confirmed. Do NOT present the naive band-sum tensor. Next: draft the
> gauge section on this framing; on write-up landing file the return handoff so VIII
> flips its verdict row PART->PASS for the joint release. See memory
> `gauge-verdict-resolved-structure-times-scalar.md`,
> `notes/exp_03_dynamical_confirmation_plan.md`.

> **UPDATE 2026-07-16 -- electric-block GATE RESOLVED; VIII+IV are now
> COMPANION papers.** Paper VIII (`dcl-paper-08-electric-induced-action`)
> has DELIVERED the electric induced-action derivation that the gauge verdict
> was gated on (handoff `2026-07-16-paper08-paper04-companion-publication`,
> consumed this session). Results: electric block
> $\varepsilon = P$ (eigenvalues $\{1,4,4\}$, axis $(1,1,-1)$ suppressed;
> matrix $[[3,-1,1],[-1,3,1],[1,1,3]]$), magnetic block
> $\mu^{-1}=\operatorname{adj}(\varepsilon)$ (eigenvalues $\{4,4,16\}$;
> matrix $[[8,4,-4],[4,8,-4],[-4,-4,8]]$), and the gauge-sector vacuum
> **birefringence CANCELS analytically** (doubled transverse root,
> prefactor-independent, every trigonal domain + $O_h$ average). The
> cancellation is **proven decoupled** from the vacuum *speed* anisotropy --
> keep the two in SEPARATE audit rows. **Plan (PM/author 2026-07-16):**
> publish VIII+IV as companion papers, cross-cited; **IV's remaining job is
> the large-$N$ NUMERICAL confirmation** (`exp_03`) of the null polarization
> split, which lifts VIII's verdict row PART$\to$PASS. IV must confirm its own
> $(\varepsilon,\mu^{-1})$ MATCH VIII's blocks -- a mismatch is a red flag to
> reconcile before publishing. This **supersedes** the 2026-07-09 "Paper IV
> v1.0 HELD until the gauge verdict exists" ruling (now a joint release).
> Gauge/P9 audit rows stay `PART` until `exp_03` lands. See memory
> `paper08-electric-block-delivered.md`.

**Resuming? Read the ⏳ WAITING ON block below.** Kinematic channel is
`PASS` (done). **Gauge sector is `PART`:** its **operator-level structure is
now EXACT and DONE** -- the induced $\mathbf{Q}$-tensor (eigenvalues
$\{4,4,16\}$, axis $(1,1,-1)$) is reproduced *exactly by running code*
(dcl-core `exp_04`, $\max|\mathbf{Q}-\mathbf{Q}_{\text{PaperI}}|=0$; an
earlier "test #4 is N-limited" framing was retracted 2026-07-07 -- it
conflated the induced *action* [Wilson-loop, 4:1] with the wavepacket
*density* response [2:1]). What stays `PART`/OPEN is **only the observable
E+B photon-dispersion order** (`exp_03`): the bipartite structure breaks
$O_h$ to a uniaxial subgroup, so there is no symmetry proof of photon
isotropy, and whether the anisotropy is unobservable / $(ka)^2$-suppressed /
excluded $O(1)$ dim-4 is decided by the full electric+magnetic dispersion,
which is uncomputed and GPU/large-$N$-bound. **`dcl_core` v0.3.0 has SHIPPED**
(2026-07-08; Peierls gauge coupling + `dcl_core.calibration`), so the engine
upgrade `exp_03` waited on is no longer a blocker; the remaining gate is the
R4 readout + GPU provisioning + writing `exp_03` itself (see WAITING ON).
Unblocked next action: draft the abstract/introduction.

Repository freshly provisioned on 2026-06-13 from `dcl-paper-template`
(paper-only template; no companion experiment code). Takes up
follow-on item~\#14 ("Balanced Equations and Birefringent Channels")
of Paper~I's `notes/follow_on_implications.md` catalogue. The physics
originates in Paper~I: the frame-invariance step of the Dirac
derivation makes the lattice's response wavevector-direction
dependent, i.e. birefringent along the optical axis $(1,1,-1)$.

What is in place (v0.1-DRAFT):

- Scaffold copied + metadata customized (title, author, CITATION.cff,
  packages.tex PDF metadata, LICENSE, README).
- Title page and abstract/section stubs from the template; body not
  yet written.
- **Audit table seeded** with the three real claim rows (kinematic;
  gauge-sector; concordance), replacing the template examples.
- **First companion experiment landed** (the template started
  paper-only): `src/experiments/exp_01_optical_axis_isotropy.py` +
  `.md`, data in `data/`, run 2026-06-12 on `dcl_core` v0.2.2. It
  answers the load-bearing observability question for the kinematic
  channel -- *does the per-tick A=1 renormalization wash the
  $(1,1,-1)$ anisotropy out of observable amplitudes?* **No.** An
  isotropic pulse flattens perpendicular to $(1,1,-1)$ (spread ratio
  $v_\parallel/v_\perp \to 0.01$), flat-axis alignment $=1.0000$,
  $\omega$-independent, on **both** engines (integer `core3d` exact
  A=1, and float `core` with `enforce_unity_spinor`) -- so the
  survival is not a single-scheme artefact, and the optical axis is
  confirmed $(1,1,-1)$ in observables.  Kinematic audit row flipped
  `STUB`$\to$`PART`.  See
  `notes/optical_axis_renormalization_test.md`.

- **Closed-form kinematic split DERIVED** (2026-06-16): kinematic row
  `PART`$\to$`PASS`. Key result $M_\text{eff} = \tfrac43(I-\hat n_*\hat
  n_*^T) = \tfrac43 P_\perp$, so the dispersion depends only on
  $\mathbf{k}_\perp$ and $|H_\text{RGB}|^2 = 1-\tfrac43|\mathbf{k}_\perp|^2$.
  Exact eigenphase dispersion $\tan\theta = \tan(\omega/2)/|H_\text{RGB}|$;
  closed-form group velocity giving split $\Delta v = \tfrac23\sin\omega\,
  |\mathbf{k}|$ (massive sector, angular law $\sin\alpha$) plus the
  $\omega$-independent dispersion-curvature split $4/3$ vs $0$ (photon +
  massive). Per the framing decision, the claim names **both** observables.
  Verified by `src/experiments/exp_02_closed_form_split_check.py` (10/10
  checks: identities $<10^{-12}$, speed coeffs $<10^{-5}$). Derivation in
  `notes/closed_form_speed_split.md`. Section
  `paper/sections/kinematic_channel.tex` (wired into `main.tex`, builds
  clean). Paper~I now cited via `menendez2026geometryfirst` (DOI
  10.5281/zenodo.20613677, corrected on title page).

- **Gauge-sector channel: operator EXACT, observable OPEN** (updated
  2026-07-07). Row `PART`, P9 `PART`. $\mathbf{Q}$-tensor structure
  (eigenvalues $\{4,4,16\}$, axis $(1,1,-1)$; coupling ratio
  $g_3^2/g_2^2=3/2$, Paper~II) is now **reproduced exactly by running code**
  -- dcl-core `exp_04` extracts $\mathbf{Q}$ from the Peierls plaquette
  holonomy and matches Paper~I App.~B with $\max|\mathbf{Q}-\mathbf{Q}_{\text{PaperI}}|=0$;
  the de-xfailed `test_magnetic_response_reproduces_Q_eigenvalues_4_4_16`
  passes. This is **confirmatory-and-done, not deferred** (no large $N$, no
  GPU). *Correction (2026-07-07):* the earlier "test #4 is N-limited/GPU-bound"
  framing was **retracted** -- it conflated two observables, the induced
  *action* (Wilson-loop, 4:1 $=\{4,4,16\}$, exact) vs the wavepacket
  *density* response (2:1 axis:planar, robust but a different quantity).
  **Observability still OPEN.** The bipartite RGB/CMY structure breaks $O_h$
  to a uniaxial subgroup about $(1,1,-1)$ ($\mathbf{Q}$ fixed by $12/48$, RGB
  by $6/48$), so the induced photon action is genuinely uniaxially
  anisotropic; the $O_h$-average to isotropic Maxwell is unjustified, and by
  the `exp_01` analogy the anisotropy may survive in observables (where read
  literally it is the excluded dim-4 $O(1)$ effect). **The sole open item is
  the full electric+magnetic photon-dispersion order** (`exp_03` / dcl-core
  acceptance test #5) -- Paper~I did the magnetic sector only; the E/B
  cancellation escape is uncomputed and genuinely GPU/large-$N$-bound.
  **`exp_03` is decisive, not confirmatory.** See
  `notes/gauge_sector_structural_conclusion.md`.

- **GATING FACTOR -- electric-sector induced-action derivation** (2026-07-09).
  The gauge-sector *verdict* is gated on deriving the **electric block** -- the
  permittivity tensor $\varepsilon$, the temporal/$F_{0i}$ analog of Paper~I
  App.~B's magnetic $\mathbf{Q}$-tensor $\{4,4,16\}$. **It exists in neither
  Paper~I nor Paper~II** (Paper~II reuses only the magnetic $\mathbf{Q}$ for the
  coupling ratio; confirmed 2026-07-09), and **no symmetry supplies it**: the
  framework establishes only the spatial cubic group $O_h$, *not* the Lorentz
  boosts that would fix $\varepsilon$ from $\mu^{-1}$. Without it the sign and
  magnitude of the leading photon birefringence $\Delta v$ cannot be computed, so
  the gauge audit row **cannot move past `PART`**. Screen `exp_03a` (2026-07-09)
  measured the *density*-response proxy and found the electric and magnetic
  anisotropies **opposite in sense** about $(1,1,-1)$ (suggestive of cancellation,
  but density is not the action). This gating factor **does NOT gate a v1.0
  deposit** (the kinematic channel is the falsifiable result, `PASS`), but it
  **does gate**: (a) any gauge-sector prediction/tension claim, (b) P9 as a
  multi-*observable* concordance, and (c) the tactical case that Paper~IV adds a
  second falsifiable channel. **Delivery (decided 2026-07-09): a SEPARATE
  companion paper** in the series -- not a Paper~I appendix -- carrying the
  electric-block derivation (method TBD: Paper~I App.~B's approach extended to the
  electric/temporal sector, or an action-level spectral $\mathrm{Tr}\ln T$ probe).
  Paper~IV's gauge verdict gates on that new paper. See
  `notes/exp_03_R4_cancellation_screen_spec.md` §4a, §7.

- **`dcl_core` pin bumped to v0.3.0** (2026-07-09): committed pin now lives
  in `virtual-env-requirements.txt` (was: no pin file; docstring said
  "0.2.2"). v0.3.0 (Zenodo doi:10.5281/zenodo.21272238) is additive over
  v0.2.x -- `exp_01`/`exp_02` results unchanged -- and adds the
  `dcl_core.calibration` unit boundary + `core3d` U(1) Peierls gauge surface.
  **Calibration discipline:** physical-unit conversions go through
  `dcl_core.calibration`, not ad-hoc constants; `exp_01`/`exp_02` are pure
  lattice-unit and carry none (the $(ka)\to$physical mapping is analysis-only
  in `notes/falsifiability_and_sme_mapping.md`), so `exp_03` is the first
  place calibration constants will appear.

- **Post-v1 "Experiment 5" folded into the kinematic section** (2026-07-09,
  per PM directive): vacuum birefringence = the same optical-axis split this
  paper already derives (Prop.~\ref{prop:speed_split}); anisotropic packet
  spreading = the real-space dual of the group-velocity dispersion `exp_01`
  already measures. Neither is a new/5th falsifier (program = 4 falsifiers +
  1 demonstrator; Exp 5 is the demonstrator). The isotropic spread-*rate*
  belongs to the post-v1 LIV-dispersion program, NOT Paper IV; only its
  $(1,1,-1)$-aligned anisotropy is this paper's result, stated as the
  $a\to0$-surviving residual (an isotropic excess would be numerical
  dispersion, not physics). Added as `rem:spreading_same_channel` in
  `paper/sections/kinematic_channel.tex`. Do NOT stand Exp 5 up as its own
  repo.

**Next concrete action (unblocked):** draft the **abstract and
introduction** stating the kinematic channel (= falsifiable dim-6
dispersion) and the structural concordance. Frame the gauge sector as
**operator-exact but observationally open**: the $\mathbf{Q}$-tensor is
derived-and-code-confirmed, but whether it registers as an *observable*
birefringence is undecided (`exp_03`-pending) -- do not assert it as either
a prediction or a non-observable. See WAITING ON for `exp_03`'s remaining
gate (R4 readout + GPU provisioning; the v0.3.0 engine upgrade has shipped).

### TODO / Open Items

### ⏳ WAITING ON (read this first if resuming)

- **`exp_03` (gauge-sector E+B photon-dispersion order) -- engine SHIPPED,
  experiment not yet written.** The `dcl_core` core3d v0.3.0 upgrade this
  waited on **has landed** (released 2026-07-08; Peierls gauge coupling,
  `uniform_B_potential`, vector-potential threading, fused CuPy `hop_average`).
  The magnetic $\mathbf{Q}$ cross-check (acceptance test #4) is **done and
  exact** via `exp_04` -- that part is no longer open. *Still open (DECISIVE,
  not confirmatory):* the gauge anisotropy is uniaxial about $(1,1,-1)$ with
  no symmetry proof of isotropy, so `exp_03` must measure the
  **order/magnitude** of the induced photon birefringence with the **full
  electric + magnetic** Peierls dynamics (dcl-core acceptance **test #5**) to
  decide: $O(1)$ dim-4 (excluded $\Rightarrow$ tension), $(ka)^2$-suppressed
  (a viable dim-6-like prediction), or null. **NB the earlier "token
  vacuum-average $\to$ isotropic vs single-probe anisotropic" framing is
  retracted** -- the lattice has one fixed bipartite orientation, so the token
  ensemble is uniaxial too; $O_h$ is not restored by averaging. *Why core3d
  not core:* core3d is the canonical engine with exact integer-token A=1
  accounting; `core` is legacy-only.
  - **Requirements spec** (dcl-core, revised 2026-06-16):
    `dcl-core/docs/design/04_gauge_field_and_vacuum_response.md` (R1 gauge
    param, R2 Peierls hop, R3 `uniform_B_potential`, R4 induced-response
    readout, R5 GPU/parallel sweep). The spec was revised to the
    order/magnitude + E+B premise (isotropy premise dropped) and v0.3.0
    Phases 1--2 were implemented against the corrected version. *(Cross-doc:
    the design doc may still carry stale "test #4 N-limited" wording; that is
    a dcl-core-session fix, not this repo's -- flagged to PM.)*
  - **Remaining owner-gated items (user):** (2) settle the **R4 readout**;
    (3) **GPU / parallelism provisioning** (the birefringence-order precision
    is $N$-bound $\Rightarrow$ GPU-bound); (4) green light to write `exp_03`.
    *(Item (1) "review + revise the spec" is DONE -- spec revised 2026-06-16.)*
  - **Then (Claude):** write `exp_03` on the four-cell / token-ensemble grid
    against v0.3.0, using the GPU path once provisioned, routing any physical
    units through `dcl_core.calibration`.
  - Cross-repo note: the engine work lives in **`dcl-core`** (separate
    repo), not here; this repo's `exp_03` consumes it. Pin is now
    `dcl_core @ v0.3.0` (`virtual-env-requirements.txt`).

- **[BLOCKING -- TACTICAL] Falsifiability magnitude + SME dim-6 mapping.**
  Paper~III (tidal ionization) was deferred in favour of Paper~IV *on the
  expectation that the optical-axis birefringence is falsifiable*; this
  item gates whether that ordering holds. Full analysis (literature-grounded
  via a verified multi-source search) in
  `notes/falsifiability_and_sme_mapping.md`. **SME mapping DONE:** the
  kinematic channel is the CPT-even, nonbirefringent, mass-dim-6 photon
  sector ($c^{(6)}_{(I)jm}$); the predicted pattern is parameter-free
  (axis $(1,1,-1)$; monopole + axis-aligned quadrupole, fixed ratio, no
  $j{=}4$; on-axis flat to all orders) even though the scale floats with
  $a$. **Key numbers:** binding bound is LHAASO GRB 221009A
  ($E_{\rm QG2}>7\times10^{11}$ GeV), giving surviving window $\ell_P
  \lesssim a \lesssim 3\times10^{-28}$ m. Frontier-detectable only near the
  top of that window; Planck calibration is ~14-23 orders below current
  reach. **Correction found:** Paper~I P7's $a\lesssim7.6\times10^{-19}$ m
  is wrong by ~9 orders (implies an absurd $260$ GeV cutoff, excluded by
  observed PeV photons) -- feed back to Paper~I errata. **Remaining to
  settle the tactical call:** (a) reconcile P7's "two arrival peaks" photon
  claim (corrected in `rem:photon_limit`); (b) frame-fixing (is the lattice
  frame the CMB frame?). **Gauge sector -- the earlier "sharper falsifier"
  hope was wrong, but its fate is now OPEN, not closed:** it is dim-4 $k_F$
  (not birefringent $k^{(6)}$), and its observability is undecided pending
  `exp_03` (could be unobservable, suppressed, or an excluded $O(1)$ effect
  -- see the gauge-sector-OPEN bullet above /
  `notes/gauge_sector_structural_conclusion.md`). So for now the one *clean*
  frontier-testable falsifiable channel is the **kinematic dim-6
  dispersion**; the gauge story is load-bearing but unresolved. Net: the
  falsifiable content is currently the single kinematic channel, which
  **weakens** (does not kill) the empirical case for prioritising Paper~IV
  over Paper~III -- and the gauge `exp_03` could swing it either way. A fact
  for the tactical ledger; user's call.

> **Working title** -- "Optical-Axis Birefringence on the A=1
> Discrete Causal Lattice"; confirm/refine before first deposit.

---

## What This Project Is

Paper~IV develops the A=1 lattice's intrinsic **optical-axis
birefringence**: light propagating along the optical axis
$\mathbf{V}_1+\mathbf{V}_2+\mathbf{V}_3 = (1,1,-1)$ splits into
ordinary/extraordinary modes whose speeds differ in a calculable,
closed-form way. The effect is a *consequence* of Paper~I's geometry,
not a new postulate. The $(1,1,-1)$ birefringence is one of the
series' **standing falsifiable predictions** (it appears in the
program claim map); this paper works it to closed form. It is
**distinct from** follow-on #11 (*vacuum* birefringence as a
photon-photon session interaction).

---

## Paper Title and Theme

**Title (working):** Optical-Axis Birefringence on the A=1 Discrete
Causal Lattice: Kinematic and Gauge-Sector Anisotropy along
$(1,1,-1)$.

**Core theme / framing:** the lattice is a *birefringent medium* whose
optical axis is fixed by its geometry; predicting *where* and *how
much* the ordinary/extraordinary split occurs turns a structural fact
about the substrate into an observable signature. Per the program's
falsifiability stance, claim only what is derived; route falsifiability
claims through the audit table / claim map, not the prose.

---

## Audit Table Status

| Row | Status | What it claims |
|---|---|---|
| Kinematic directional dispersion anisotropy along $(1,1,-1)$ | PASS *(substrate)* | Closed-form axial--transverse anisotropy: $M_\text{eff}=\tfrac43 P_\perp$, $\|H_\text{RGB}\|^2=1-\tfrac43\|k_\perp\|^2$ flat along axis; massive group speed $\tfrac23\sin\omega\|k\|\sin\alpha$. PASS covers the **substrate math** (`exp_02` identities $<10^{-12}$); the **observable reading on a lab particle is the as-constructed FAIL below.** `notes/closed_form_speed_split.md`. |
| Bare single-tick spinor as literal lab matter (as-constructed) | **FAIL** *(as-constructed; open via emergence map)* | M1/M2 (verified `exp_05_matter_sector_order`): exact axial flat band (axial transport zero); O(1) directional kinetic anisotropy ($\theta-\omega/2=\tfrac13\sin\omega\|k\|^2\sin^2\alpha$, no isotropic piece); kinetic/continuum ratio $\le 8/(9\sqrt3)\approx0.513$; $\omega=0$ filter accumulates **linearly in $a$** (e-folds days--min at $\ell_P$). Excluded as constructed; escape = token->matter emergence map + $\delta p_\text{min}$ (OPEN). |
| Gauge-sector null polarization split (birefringence cancels), *conditional on the blocks* | PASS | $\mu^{-1}=\gamma\,\text{adj}(\varepsilon)$ (theorem, any hop vectors) forces a doubled transverse root -> split $=0$. `electric_induced_action.py` (symbolic) + `exp_03_geometric_blocks`/`exp_03_dispersion_core` ($\max\|v_+-v_-\|=1.6\times10^{-15}$). **Universal:** no three-hop lattice can be birefringent. |
| Gauge blocks as the actual *dynamical* induced action | PART | Vertex verified (`exp_04...`, $4\times10^{-19}$) but not the full $\Gamma^{(2)}$ Hessian; $\text{Tr}\ln T$ route Ward-divergent on the flat axis (naive band sum -> wrong $(1,-1,0)$ object). Stated open follow-on. |
| Gauge-sector common-mode speed anisotropy (factor $\sim2$) -- a stated *tension* | **FAIL** *(as-constructed; geometric decisive / dynamical strong-provisional; open under $O_h$)* | $v^2\in[\gamma,4\gamma]$, ratio 4 ($\gamma$-independent), $O(1)$ dim-4 (3 routes) -> excluded by isotropy bounds as a single domain. Escape = $O_h$-restoring four-orientation vacuum (OPEN). Each sector independently O(1)-excluded (no matter/photon-contrast needed). |
| Multi-channel concordance (P9) | PART | Kinematic, gauge, and matter sectors inherit the same axis $(1,1,-1)$ (structural identity). Both single-domain sectors excluded as constructed; the birefringence null is the one clean surviving result. |
| Falsifiability along the optical axis (no-go map) | PART | **Survives:** universal birefringence null (passed postdiction, excludes CPT-odd dim-5 rivals). **Excluded as constructed:** induced photon speed (O(1) dim-4) AND bare matter (flat band + O(1) kinetic + linear filter). Substrate massive dispersion (sidereal) awaits the emergence map. |

Mirror of `paper/sections/audit_table.tex` -- update this table when
the audit table changes. The claim-auditor agent
(`.claude/agents/claim-auditor.md`) treats `audit_table.tex` as the
authority; this section is for quick orientation only.

---

## Conventions

- **Status legend.** `PASS` / `PART` / `STUB` / `FAIL` (defined in the
  front-matter of `paper/main.tex`).
- **File naming.** Sections: `paper/sections/<topic>.tex`. Figures:
  `paper/figures/<name>.{tex,pdf,png}`. Notes: `notes/<topic>.md`.
- **Cross-references.** Always `\label{}` + `\ref{}` / `\autoref{}`,
  never hard-coded numbers (`sec:`, `eq:`, `fig:`, `tab:`, `thm:`).
- **Bibliography.** All cites flow through
  `paper/paper-bib/references.bib`; `\bibliographystyle{unsrt}`.

---

## Release flow

See `release_notes/README.md`. Summary: CI green -> update
`CITATION.cff` -> draft `release_notes/vX.Y.md` -> **deposit on Zenodo
first** (DOI lands in title-page `\thanks{}` + `CITATION.cff`) ->
commit version bump -> tag `vX.Y` -> push tag -> GitHub Release.

---

## What NOT to Change

- The MIT (`LICENSE`) / CC BY 4.0 (prose) split.
- The series identifiers in the title-page `\thanks{}` (Paper~IV,
  follow-on #14, links to Papers I & II).

---

## Notes Index

`notes/README.md` -- conventions for notes/.

- `notes/optical_axis_renormalization_test.md` -- numerical
  confirmation (STABLE) that the kinematic $(1,1,-1)$ anisotropy
  survives A=1 renormalization in observables and that the optical axis
  is $(1,1,-1)$; backs the kinematic audit row. Experiment:
  `src/experiments/exp_01_optical_axis_isotropy.py`.
- `notes/closed_form_speed_split.md` -- the closed-form
  ordinary/extraordinary speed split derivation (DERIVED + verified):
  $M_\text{eff}=\tfrac43 P_\perp$, eigenphase dispersion, group-velocity
  and dispersion-curvature splits. Flips the kinematic audit row to
  `PASS`. Verification: `src/experiments/exp_02_closed_form_split_check.py`;
  section: `paper/sections/kinematic_channel.tex`.
- `notes/falsifiability_and_sme_mapping.md` -- ANALYSIS (blocks a tactical
  decision): is the birefringence practically falsifiable? SME mapping DONE
  (nonbirefringent dim-6 $c^{(6)}_{(I)jm}$; parameter-free pattern; window
  $a\lesssim3\times10^{-28}$ m from LHAASO, correcting Paper~I's
  $10^{-19}$ m by ~9 orders). **Superseded re: gauge sector** -- the
  earlier "gauge maps to birefringent $k^{(6)}$, a sharper falsifier" claim
  was wrong (it is dim-4 $k_F$), and the follow-on "unobservable" claim was
  *also* retracted (see next entry -- now OPEN). The one *clean*
  frontier-testable falsifiable channel is the kinematic dim-6 dispersion.
  See the BLOCKING TODO above.
- `notes/gauge_sector_structural_conclusion.md` -- operator structure
  **EXACT/done**, observable **OPEN** (corrected 2026-07-07). The
  $\mathbf{Q}$-structure (axis $(1,1,-1)$; coupling ratio $g_3^2/g_2^2=3/2$,
  Paper~II) is reproduced *exactly by running code* (dcl-core `exp_04`,
  $\max|\mathbf{Q}-\mathbf{Q}_{\text{PaperI}}|=0$) -- the earlier "test #4
  N-limited/GPU-bound" wording is retracted (it conflated the induced
  *action* [Wilson-loop, 4:1] with the *density* response [2:1]).
  **Observability still undecided:** the $O_h$-isotropy mechanism fails
  (bipartite structure breaks $O_h$ to a uniaxial subgroup, $\mathbf{Q}$
  fixed $12/48$), so the induced action is genuinely uniaxial; read as an
  observable it is the excluded dim-4 $O(1)$ effect. The sole open item is
  the full **E+B photon-dispersion order** (E/B cancellation uncomputed;
  `exp_03` / dcl-core test #5, GPU-bound). Gauge audit row PART, P9 PART.
