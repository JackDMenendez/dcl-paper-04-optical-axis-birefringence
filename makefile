# Paper-only template -- root build
# ----------------------------------------------------------------------------
# Requirements
#   GNU Make >= 4.3
#   pdflatex, bibtex  (MiKTeX or TeX Live)
#
#   On Windows, run from an MSYS2 UCRT64 shell. The stock Windows GNU Make
#   port (3.81) is too old. Confirm with: `make --version` -> >= 4.3.
# ----------------------------------------------------------------------------
# Targets
#   all      paper -> promote                 (default)
#   paper    build PDF (3-pass pdflatex + bibtex)
#   promote  copy final PDF into stage/
#   clean    remove build/ and stage/
#   help     print this list
# ----------------------------------------------------------------------------

RELATIVE_PATH :=
include common.mak

# --- Paper ------------------------------------------------------------------
DOC_TITLE := Paper
DOC_PDF   := $(build_dir)/$(DOC_TITLE).pdf

PAPER_DIR    := paper
PAPER_INPUTS := $(PAPER_DIR)/main.tex \
                $(wildcard $(PAPER_DIR)/sections/*.tex) \
                $(wildcard $(PAPER_DIR)/macros/*.tex) \
                $(wildcard $(PAPER_DIR)/paper-bib/*.bib)

# pdflatex/bibtex run from inside paper/ so relative \input{} paths resolve.
# Output goes to ../build/.
PDFLATEX_PAPER := cd $(PAPER_DIR) && $(PDFLATEX) -output-directory=../$(build_dir)
BIBTEX_PAPER   := cd $(PAPER_DIR) && $(BIBTEX) ../$(build_dir)

# --- Promote ----------------------------------------------------------------
PROMOTE_FIGS :=
PROMOTE_PDF_TARGETS := $(stage_dir)/$(DOC_TITLE).pdf
PROMOTE_FIG_TARGETS := $(addprefix $(stage_dir)/,$(PROMOTE_FIGS))

.PHONY: all help paper promote clean

all: paper promote
	@echo "================ Build Complete ================"

help:
	@sed -n '1,30p' makefile

# --- Paper ------------------------------------------------------------------
paper: $(DOC_PDF)

$(build_dir) $(stage_dir):
	mkdir -p $@

$(DOC_PDF): $(PAPER_INPUTS) | $(build_dir)
	$(PDFLATEX_PAPER) -jobname=$(DOC_TITLE) main.tex
	$(BIBTEX_PAPER)/$(DOC_TITLE)
	$(PDFLATEX_PAPER) -jobname=$(DOC_TITLE) main.tex
	$(PDFLATEX_PAPER) -jobname=$(DOC_TITLE) main.tex

# --- Promote ----------------------------------------------------------------
promote: $(PROMOTE_PDF_TARGETS) $(PROMOTE_FIG_TARGETS)

$(stage_dir)/$(DOC_TITLE).pdf: $(DOC_PDF) | $(stage_dir)
	cp -v $< $@

$(stage_dir)/%: $(figures_dir)/% | $(stage_dir)
	cp -v $< $@

# --- Clean ------------------------------------------------------------------
clean:
	-rm -rf $(build_dir) $(stage_dir)
	@echo "================ Clean Complete ================"
