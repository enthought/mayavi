"""Tests for the Text3D module

"""
import os
import shutil
import sys
import unittest
import tempfile

import numpy
from PIL import Image

from mayavi import mlab

from common import TestCase


class TestText3DUnitTest(unittest.TestCase):

    def setUp(self):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, "saved_figure.png")

        # this ensures that the temporary directory is removed
        self.addCleanup(self.remove_tempdir)

    def remove_tempdir(self):
        shutil.rmtree(self.temp_dir)

    def mlab_close_all(self):
        mlab.close(all=True)

    def test_text3d(self):
        """Test if Text3D shows"""
        # the points3d is there to provide data for
        # attaching the text3d module.  Opacity is set to
        # zero so that the image should only show
        # the text3d and we look for the pixels
        mlab.points3d(0., 0., 0., opacity=0.)

        self.addCleanup(self.mlab_close_all)

        mlab.text3d(0., 0., 0., "X")
        mlab.savefig(self.filename)

        self.check()

    def check(self):
        image = numpy.array(Image.open(self.filename))[:, :, :3]

        # Check that the image has pixel different from the background
        # Supposedly the first pixel is the background color
        if not (numpy.sum(image != image[0, 0], axis=2) == 3).any():
            message = "Looks like the Text3D is not shown"
            self.fail(message)


class TestText3D(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(
            TestText3DUnitTest)

        result = unittest.TextTestRunner().run(suite)

        if result.errors or result.failures:
            sys.exit(1)


if __name__ == "__main__":
    t = TestText3D()
    t.test()
