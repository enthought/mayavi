=======================
Notes on testing Mayavi
=======================


This directory contains unit tests for mayavi.

Running the tests
=================

Run them with pytest, from the root of a source checkout::

 $ pytest -v --timeout=10 mayavi

which is what CI does.  A single file, or a single test, is::

 $ pytest mayavi/tests/test_contour.py
 $ pytest mayavi/tests/test_contour.py::TestContour::test_contour


Debugging using on-screen rendering
===================================

Many of these unit tests run off screen and make use of TestEngine.

TestEngine can be replaced by Engine to allow for scene creation
which may be useful in debugging.

This can be easily done by uncommenting the following line from the
setUp() functions::

        e = Engine() # This is commented by default

It must be followed by the commenting of :

        e = TestEngine() # This is uncommented by default

Debugging using an IPython Shell
===================================

The IPython Shell can be embedded anywhere in the program.

You need to import the  `IPython` module and then add the following
lines wherver you want to embed the shell::

        embedshell = IPython.Shell.IPShellEmbed()
        embedshell()


