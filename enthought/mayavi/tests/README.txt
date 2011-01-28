=======================
Notes on testing Mayavi
=======================


This directory contains unit tests for mayavi.

Running the tests
=================

The best way to run the tests in this directory is to do::

 $ ./runtests.py .

Try ``runtests.py --help`` to see all help options.

You may also run each test individually.  For example::

 $ python test_contour.py

You can also use nosetests but nosetests runs everything in the same
process often tripping up on valid tests.


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


