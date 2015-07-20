=======================
Notes on testing Mayavi
=======================


This directory contains integration tests for mayavi.  The unit tests
are in `mayavi/tests` and are distributed with the package.  The
tvtk unit tests are in `enthought/tvtk/tests`.


Running the tests
=================

The best way to run the tests in this directory is to do::

 $ ./run.py

This will run all of the tests in the mayavi directory by running them
each in a separate Python interpreter.  You may also run each test
individually.  For example::

 $ python test_contour.py

To see the supported command line options you may do::

    $ python test_contour.py -h # or --help

    Usage: test_contour.py [options]

    Options:
    -h, --help          show this help message and exit
    -v, --verbose       Print verbose output
    -i, --interact      Allow interaction after test (default: False)
    -p, --profile       Profile for memory usage and leaks (default: False).
                        [Long Running]
    -s, --nostandalone  Run test using envisage without standalone (default:
                        False)
    -o, --offscreen     Always use offscreen rendering when generating images
                        (default: False)

You should be able to run the tests as::

 $ nosetests

However, nosetests changes the Python environment when it runs the tests
and this does not always work cleanly with Mayavi.  So if this does run,
fine if not use `run.py`.


Writing tests
=============

Mayavi tests are not typical tests.  The easiest way to get started
writing a test is to look at the existing ones and copy one of them then
modify it suitably for your test.

Image based tests
=================

Image based tests (like the ones VTK uses) are possible but a pain since
there are almost always complications.  The image tests may fail due to
hardware/driver issues and this becomes a red-herring for new users.
**Therefore, in general we do not recommend the use of image based
tests**.

There is one test that is image based for your reference --
`test_streamline.py`, the images for this test are in the `images`
directory.  The image based tests  use the same approach that VTK uses.
A visualization is created and the rendered scene is saved to a PNG
image.  The test code will check to see if a rendered scene is similar
to the image saved.  If the pictures are nearly-identical then the test
passes.  If not one gets a failure with an error message and a bunch of
images that indicate the difference between the saved and rendered
images.  In addition no error or warning messages should be shown if a
test passes.

VTK and the `mayavi` image based tests support the notion of multiple
valid test images.  For example between VTK-4.4 and 5.0 there were
changes made to the way the camera was reset.  Thus, an image produced
with 4.4 is different from that with 5.0.  In order to be able to test
for these VTK tests allow the user to save a number of test images. These
are all tested in sequence to check for a valid image.  If a default
test image is called `test_outline_image.png` then its various
alternatives can be called `test_outline_image_%d.png` (for example,
`test_outline_image_1.png`).

