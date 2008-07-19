=======================
Notes on testing Mayavi
=======================

Introduction
============

MayaVi tests use the same approach that VTK uses.  A visualization is
created and the rendered scene is saved to a PNG image.  The test code
will check to see if a rendered scene is similar to the image saved.
If the pictures are nearly-identical then the test passes.  If not one
gets a failure with an error message and a bunch of images that
indicate the difference between the saved and rendered images.  In
addition no error or warning messages should be shown if a test
passes.

The tests here do not use `unittest` or `py.test`.  The problem with
these is that `PyFace.GUI` (and wxPython underneath) is running a
mainloop.  `Unittest` and friends want to run the test code for you.
Therefore, it is a pain to use them.  Therefore we use a much simpler
approach and merely run the tests in this directory as normal Python
programs.  It is the tests responsibility to print suitable error
messages when there is a failure.

VTK and the `mayavi` tests support the notion of multiple valid test
images.  For example between VTK-4.4 and 5.0 there were changes made
to the way the camera was reset.  Thus, an image produced with 4.4 is
different from that with 5.0.  In order to be able to test for these
VTK tests allow the user to save a number of test images.  These are
all tested in sequence to check for a valid image.  If a default test
image is called `test_outline_image.png` then its various alternatives
can be called `test_outline_image_%d.png` (for example,
`test_outline_image_1.png`).

To run all the tests simply execute the `run.py` script like so::
    $ python run.py


Command line arguments
======================

By default, when a test is executed, it will pop up a window, do some
things and close.  Each test provides some command line options.  Here
is an example::

  $ python test_foo.py -h
  [ usage and help message ]
  
  $ python test_foo.py -v # print verbose output.
  $ python test_foo.py -i # don't close window when done.


Writing Tests
=============

The best way to write a test is to look at an existing test like
`test_grid_plane.py` and adapt it to suit your needs.  All the
commonly used functionality is available in `common.py`.
