# A Thin Wrapper for the Makefiles for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  qthelp    to make HTML files and a qthelp project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  doctest   to run all doctests embedded in the documentation (if enabled)"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	make -f MakefileMayavi html
	@echo
	make -f MakefileTVTK html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/."

dirhtml:
	make -f MakefileMayavi dirhtml
	@echo
	make -f MakefileTVTK dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

pickle:
	make -f MakefileMayavi pickle
	@echo
	make -f MakefileTVTK pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	make -f MakefileMayavi json
	@echo
	make -f MakefileTVTK json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	make -f MakefileMayavi htmlhelp
	@echo
	make -f MakefileTVTK htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	make -f MakefileMayavi qthelp
	@echo
	make -f MakefileTVTK qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/mayavi/qthelp/mayavi.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/mayavi/qthelp/mayavi.qhc"

latex:
	make -f MakefileMayavi latex
	@echo
	make -f MakefileTVTK latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	make -f MakefileMayavi changes
	@echo
	make -f MakefileTVTK changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	make -f MakefileMayavi linkcheck
	@echo
	make -f MakefileTVTK linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	make -f MakefileMayavi doctest
	@echo
	make -f MakefileTVTK doctest
	@echo
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."
