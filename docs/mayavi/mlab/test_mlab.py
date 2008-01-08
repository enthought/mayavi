"""
Script to be called either in "ipython -wthread" or with "mayavi -x" to
test mlab.

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


import enthought.mayavi.tools.mlab as M
import sys
import datetime

from inspect import getmembers, getsource

def is_test(value):
    name, function = member
    if name[:4] == 'test_':
        return True
    else:
        return False

def indent(lines):
    if lines is None:
        return ''
    return '\n'.join('    '+line for line in lines.split('\n'))

tests = [(func, name[5:]) for name, func in getmembers(M) 
                                        if name[:5] == 'test_']

function_tests = ((func, name) for func, name in tests
                                        if hasattr(M, name) )

function_fmt = lambda name, testfunc: """
%s
--------------------------

Documentation::

%s

.. image:: %s.jpg

Example::

%s

""" % (name, indent(getattr(M, name).__doc__), name,
                    indent(getsource(testfunc)))

example_tests = ((func, name) for func, name in tests
                                        if not hasattr(M, name) )

example_fmt = lambda name, testfunc: """
%s
--------------------------

%s

.. image:: %s.jpg

Example::

%s

""" % (name, indent(testfunc.__doc__),  
                        name, indent(getsource(testfunc)) )


def do_test(testfunc, name, print_fmt):
    print "************ testing %s **************" % name
    sys.stdout.flush()
    report.write( print_fmt(name, testfunc) )
    testfunc()
    M.savefig('%s.jpg' % name , size=(400, 400) )
    M.clf()


report = file('mlab.rst', 'w')

now = datetime.datetime.now()

report.write("""
==============
Mayavi - MLab
==============

This is not a documentation as the API is not fixed. This should be
considered as a window to the progress on mlab. Function calls and
behavior are likely to change at any moments.

Report generated on %s

Helper functions
=================

""" % now.ctime() )


for testfunc, name in function_tests:
    do_test(testfunc, name, function_fmt)


report.write("""

Examples
=================

""")

for testfunc, name in example_tests:
    do_test(testfunc, name, example_fmt)

report.close()

mayavi2.close()
