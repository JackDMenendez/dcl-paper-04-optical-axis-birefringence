# dcl-paper-04-optical-axis-birefringence

*Optical-Axis Birefringence on the A=1 Discrete Causal Lattice:
kinematic and gauge-sector anisotropy along $(1,1,-1)$.*

**Paper IV** of the A=1 Discrete Causal Lattice (DCL) series. Develops
the lattice's intrinsic optical-axis birefringence — the direction-
dependent propagation of light along the optical axis
$\mathbf{V}_1+\mathbf{V}_2+\mathbf{V}_3 = (1,1,-1)$ — into a paper-shaped
treatment. Takes up follow-on item **#14** (*Balanced Equations and
Birefringent Channels*) from Paper I's
`notes/follow_on_implications.md` catalogue.

> **Status:** v0.1-DRAFT, freshly provisioned 2026-06-13 from
> `dcl-paper-template`. Working title; scaffold in place, body to be
> written.

## Scope

The birefringence emerges from the frame-invariance step of Paper I's
Dirac derivation: the lattice's response depends on the *direction* of
the wavevector, not just its magnitude. Two channels are in view —

- **Kinematic birefringence** along $(1,1,-1)$ (the ordinary /
  extraordinary split), and
- **Gauge-sector birefringence** ($\mathbf{Q}$ eigenvalues $\{4,4,16\}$),

together with their predicted **multi-channel concordance (P9)**. The
$(1,1,-1)$ optical-axis birefringence is one of the series' *standing
falsifiable predictions* (see the program
[claim map](https://geometryinducedphysics.org/papers/claim-map.html));
this paper works it to closed form. Distinct from *vacuum*
birefringence (follow-on #11), which is a separate photon–photon
effect.

This is a **paper-only** subproject (no companion experiment code at
provisioning time).

## Series context

| | |
|---|---|
| **Paper I** | *Geometry First* — [DOI:10.5281/zenodo.20078529](https://doi.org/10.5281/zenodo.20078529) |
| **Paper II** | *Geometry Forces Physics* — [DOI:10.5281/zenodo.20292158](https://doi.org/10.5281/zenodo.20292158) |
| **Paper IV** | *Optical-Axis Birefringence* — **this repo** |

Program site: [geometryinducedphysics.org](https://geometryinducedphysics.org/).

## Build

```sh
./build.sh paper        # POSIX / MSYS2 UCRT64 on Windows
build.cmd paper         # Windows cmd / PowerShell
```

Output: `build/Paper.pdf`. Requires GNU Make >= 4.3 (on Windows use
MSYS2 UCRT64), plus `pdflatex` + `bibtex` (TeX Live or MiKTeX).

## Layout

```
paper/        LaTeX source (main.tex wires the sections)
  sections/   abstract, introduction, audit_table, conclusion, ...
  macros/     packages.tex, commands.tex
  figures/    figure fragments + binaries
  paper-bib/  references.bib
notes/        working theoretical notes
release_notes/ per-version changelog + Release body
.claude/      claim-auditor agent + project config
CLAUDE.md     project memory for Claude Code
CITATION.cff  machine-readable citation
```

## Audit table

`paper/sections/audit_table.tex` is the source of truth for which
claims are `PASS` / `PART` / `STUB` / `FAIL`; the claim-auditor agent
in `.claude/agents/` flags prose that contradicts it.

## Release flow

See `release_notes/README.md`. Short version: deposit on Zenodo first
to get the DOI, *then* commit the version bump (the DOI lands in the
title-page `\thanks{}` block and `CITATION.cff`).

## License

Paper text and figures: **CC BY 4.0**. Source / scaffolding: **MIT**
(see `LICENSE`).
