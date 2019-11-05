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
import os
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
version = release = d['__version__']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

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

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

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
latex_preamble = """
\definecolor{VerbatimColor}{rgb}{0.95,1,0.833}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
"""

# A logo displayed on the cover page.
latex_logo = '_static/m2_about.jpg'


# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

################################################################################
# A hack:
import shutil
shutil.copyfile(os.path.join(basedir, '../../CHANGES.txt'), os.path.join(basedir, './auto/changes.rst'))
