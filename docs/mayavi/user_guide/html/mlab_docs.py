"""
Script to be called either in "ipython -wthread" or with "mayavi -x" to
generate docs for mlab.

Runs all the functions starting by "test" in mlab, and generates some
documentation.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# The following *optional* two lines allow a user to call this script
# as either `python script.py` or `mayavi2 script.py`.  These two
# lines must be placed before any other mayavi imports.
from enthought.mayavi.scripts import mayavi2
mayavi2.standalone(globals())

OUT_DIR = 'html'

import enthought.mayavi.mlab as M
import sys
import datetime
import os

from inspect import getmembers, getsource, getfile
from enthought.mayavi.tools import auto_doc

def dedent(string):
    if string is not None:
        return auto_doc.dedent(string)
    else:
        return '\n'

def indent(lines):
    if lines is None:
        return ''
    return '\n'.join('    '+line for line in lines.split('\n'))

def make_doc(func, name):
    fmt = """
%s
%s

%s
    """
    file('%s/auto_mlab_%s.rst' % (OUT_DIR, name), 'w').write( fmt % (name, 
            "~"*len(name),
            dedent(getattr(M, name).__doc__) ))


def do_test(testfunc, name, print_fmt, report):
    print "************ testing %s **************" % name
    sys.stdout.flush()
    report.write("""

.. include:: auto_mlab_%s.rst

    """ % name)
    
    file('%s/auto_mlab_%s.rst' % (OUT_DIR, name), 'w').write( print_fmt(name, testfunc) )
    testfunc()
    image_name = '%s/images/mlab_%s.jpg' % (OUT_DIR, name)
    M.savefig(image_name , size=(400, 400) )
    os.system('convert %s -trim %s' % (image_name, image_name))
    M.clf()

def make_doc_plotting(func, name):
    function_fmt = lambda name, testfunc: """
%s
%s

%s

.. image:: images/mlab_%s.jpg

Example::

%s

    """ % ( name, '~'*len(name),
            dedent(getattr(M, name).__doc__), name,
            indent(getsource(testfunc)))
    do_test(func, name, function_fmt, mlab_reference)


def make_example(func, name):
    example_fmt = lambda name, testfunc: """
%s
%s

%s

.. image:: images/mlab_%s.jpg

Example::

    %s

    """ % (name, '~'*len(name), dedent(testfunc.__doc__),
                        name, indent(getsource(testfunc)) )
    do_test(func, name, example_fmt, mlab_examples)


def list_funcs(source_file):
    # FIXME: A global !!! This needs OOD
    global all_functions
    for func, name in all_functions:
        if os.path.splitext(os.path.basename(getfile(func)))[0] == source_file:
            mlab_reference.write("""

.. include:: auto_mlab_%s.rst

    """ % name)
            all_functions = [(a_func, a_name) 
                                for a_func, a_name in all_functions
                                if not a_name == name ]

#############################################################################
# Entry point

try:
    os.mkdir(OUT_DIR)
except:
    pass

tests = [(func, name[5:]) for name, func in getmembers(M) 
                                        if name[:5] == 'test_']

function_tests = ((func, name) for func, name in tests
                                        if hasattr(M, name) )

example_tests = ((func, name) for func, name in tests
                                        if not hasattr(M, name) )

try:
    os.mkdir('%s/images' % OUT_DIR)
except:
    pass

all_functions = [(func, name) for name, func in getmembers(M)
                    if not (name[:5] == 'test_' or name[0] == '_')
                        and callable(func)]

for func, name in all_functions:
    if not hasattr(M, 'test_' + name):
        print "Documenting ", name
        make_doc(func, name)

mlab_reference = file('%s/auto_mlab_reference.rst' % OUT_DIR, 'w')

now = datetime.datetime.now()

mlab_reference.write("""

MLab reference
=================

Reference list of all the main functions of ``enthought.mayavi.mlab``
with documentation and examples.

Generated on %s

""" % now.ctime() )

######################################################################
mlab_reference.write("""

Plotting functions
-------------------

""")

for testfunc, name in function_tests:
    make_doc_plotting(testfunc, name)
    all_functions = [(a_func, a_name) 
                                for a_func, a_name in all_functions
                                if not (name == a_name) ]

######################################################################
mlab_reference.write("""

Figure handling functions
---------------------------

""")
list_funcs('figure')

######################################################################
mlab_reference.write("""

Figure decorations functions
----------------------------

""")
list_funcs('decorations')
list_funcs('pipe_base')

######################################################################
mlab_reference.write("""

Camera handling functions
----------------------------

""")
list_funcs('camera')

######################################################################
mlab_reference.write("""

Misc
----------------------------

""")
for func, name in all_functions:
    # Only what hasn't been used in other section is left in
    # all_functions
    mlab_reference.write("""

.. include:: auto_mlab_%s.rst

""" % name)



mlab_reference.close()
######################################################################
mlab_examples = file('%s/auto_mlab_examples.rst' % OUT_DIR, 'w')

mlab_examples.write("""

Examples
~~~~~~~~~

""")

for testfunc, name in example_tests:
    make_example(testfunc, name)

mlab_examples.close()

mayavi2.close()
