# -*- coding: utf-8 -*-
#
# Mayavi documentation build configuration file, created by
# sphinx-quickstart on Sat Apr 12 23:25:24 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.


# Adding the current directory to the path, so that sphinx finds the
# extensions.
import faulthandler
import os
import re

# autodoc imports mayavi, so VTK can take the build down with it; without this
# a crash is a bare signal number.  The variable carries it into any child.
faulthandler.enable()
os.environ['PYTHONFAULTHANDLER'] = '1'

try:
    # When translating the docs to another language, this variable is set 
    # elsewhere, so if it is not set, set it to a suitable default.
    basedir
except NameError:
    basedir = os.path.dirname(os.path.abspath(__file__))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'traits.util.trait_documenter']

# mayavi.tools.server (autodoc'd by tips.rst) imports wx and twisted and calls
# wxreactor.install() at import time; neither belongs in a docs build
autodoc_mock_imports = ['wx', 'twisted']

# Base classes that trait_documenter emits but that nothing here documents:
# ETS packages we do not build docs for, and -- because the build runs with
# ETS_TOOLKIT=null -- the null toolkit's placeholder class.
nitpick_ignore = [
    ('py:class', 'mayavi.core.base.Base'),
    ('py:class', 'pyface.base_toolkit.Toolkit.__call__.<locals>.Unimplemented'),
    ('py:class', 'traits.has_traits.HasStrictTraits'),
    ('py:class', 'traits.has_traits.HasTraits'),
    ('py:class', 'tvtk.pyface.scene_model.SceneModel'),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = 'mayavi'
copyright = u'2008-2018, Enthought Inc.'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
d = {}
fname = os.path.join(basedir, '..', '..', '..', 'mayavi', '__init__.py')
exec(compile(open(fname).read(), fname, 'exec'), d)
# "4.8.4.dev", not "4.8.4.dev14+g8665ab72c.d20260729": the commit and date show
# up in the title of every page, so they would churn the whole site each build.
# A pre-release segment such as rc1 is kept.
version = release = re.sub(r'\.dev\d+', '.dev', d['__version__'].split('+')[0])

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# Files that are ``include``d into another document.  Sphinx would otherwise
# also read each of them as a document in its own right, which duplicates every
# label they define and evaluates their ``:func:`` roles without the
# ``currentmodule`` their host sets.
exclude_patterns = [
    'auto/changes.rst',         # -> changes.rst
    'examples.rst',             # -> application.rst
    'mlab_3d_plotting_functions.rst',
    'mlab_animating.rst',
    'mlab_case_studies.rst',
    'mlab_changing_object_looks.rst',
    'mlab_demo.rst',
    'mlab_figures_decorations.rst',
    'mlab_pipeline.rst',
    'mlab_running_scripts.rst',  # ^ all -> mlab.rst
    # Superseded by the hand-maintained mlab_pipeline_reference.rst, which is
    # what auto/mlab_reference.rst's toctree actually points at.
    'auto/mlab_pipeline_reference.rst',
]

# Each of those was published as a page of its own for years, so leave a
# meta-refresh stub at the old URL aimed at the document that now holds it.
moved_pages = {
    'auto/changes': 'changes',
    'auto/mlab_pipeline_reference': 'mlab_pipeline_reference',
    'examples': 'application',
    'mlab_3d_plotting_functions': 'mlab',
    'mlab_animating': 'mlab',
    'mlab_case_studies': 'mlab',
    'mlab_changing_object_looks': 'mlab',
    'mlab_demo': 'mlab',
    'mlab_figures_decorations': 'mlab',
    'mlab_pipeline': 'mlab',
    'mlab_running_scripts': 'mlab',
}

_STUB = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url=%(url)s" />
    <link rel="canonical" href="%(url)s" />
    <title>Page moved</title>
  </head>
  <body>
    <p>This page has moved to <a href="%(url)s">%(url)s</a>.</p>
  </body>
</html>
"""


def _write_moved_page_stubs(app, exception):
    import re
    from pathlib import Path, PurePosixPath

    if exception is not None or app.builder.name != 'html':
        return
    for old, new in moved_pages.items():
        old = PurePosixPath(old)
        # land on the section itself: docutils turns label underscores into
        # hyphens when it makes the id
        source = (Path(basedir) / old).with_suffix('.rst')
        # nothing after the colon, else it is a hyperlink target, not a label
        label = re.search(r'^\.\.\s+_([\w-]+):\s*$', source.read_text(), re.M)
        anchor = '#' + label.group(1).replace('_', '-') if label else ''
        url = '../' * (len(old.parts) - 1) + new + '.html' + anchor
        target = (Path(app.outdir) / old).with_suffix('.html')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(_STUB % {'url': url})


def setup(app):
    app.connect('build-finished', _write_moved_page_stubs)
    # build-finished runs once in the main process, so -j is fine
    return {'parallel_read_safe': True, 'parallel_write_safe': True}

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# shared with docs/site/index.html, which links it alongside classic.css
html_css_files = ['mayavi.css']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# off: with a build on every push this would restamp all ~115 pages daily.
# The site landing page carries the build date instead (see docs/Makefile).
html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Content template for the index page.
#html_index = ''

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'Mayavidoc'

# A logo displayed in the html sidebar.
html_logo = 'mayavi-logo.png'

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [('index', 'mayavi_user_guide.tex', 'Mayavi User Guide',
                        'Prabhu Ramachandran, Gael Varoquaux', 'manual')]

# Additional stuff for the LaTeX preamble.
latex_preamble = r"""
\definecolor{VerbatimColor}{rgb}{0.95,1,0.833}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
"""

# A logo displayed on the cover page.
latex_logo = 'm2_about.jpg'


# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# To specify names to enable gettext extracting and translation applying for i18n additionally. You can specify below names:
gettext_additional_targets = ['raw'] 

################################################################################
# A hack:
import shutil
shutil.copyfile(os.path.join(basedir, '../../CHANGES.txt'), os.path.join(basedir, './auto/changes.rst'))
