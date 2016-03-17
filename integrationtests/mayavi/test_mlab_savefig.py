import os
import shutil
import unittest
import tempfile

import numpy
from PIL import Image

from mayavi import mlab
from mayavi.tools.figure import savefig

from common import TestCase


class TestMlabSavefigUnitTest(unittest.TestCase):

    def setUp(self, figure=None):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, "saved_figure.png")

        self.figure = mlab.figure()

        # this ensures that the temporary directory is removed
        # and all scene is closed
        self.addCleanup(self.cleanup)

    def cleanup(self):
        shutil.rmtree(self.temp_dir)
        mlab.close(all=True)

    def test_savefig_with_size(self):
        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z)

        # save the figure
        savefig(self.filename, size=(131, 217))

        # check
        self.check_image((217, 131))

    def test_savefig_with_size_offscreen(self):
        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z)

        # save the figure
        savefig(self.filename, size=(131, 217))

        # check
        self.check_image((217, 131))

    def test_savefig_with_size_and_magnification(self):
        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2)

        # check if the image size is twice as big
        self.check_image((434, 262))

    def test_savefig_with_size_and_magnification_offscreen(self):
        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2)

        # check if the image size is twice as big
        self.check_image((434, 262))

    def check_image(self, size):
        image = numpy.array(Image.open(self.filename))[:, :, :3]

        # check the size is correct
        self.assertEqual(image.shape[:2], size)

        # check that there is no black spot
        if (numpy.sum(image == [0, 0, 0], axis=2) == 3).any():
            self.fail("The saved image has black spots")


class TestMlabSavefig(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(
            TestMlabSavefigUnitTest)
        for test in suite:
            test.run()


if __name__ == "__main__":
    t = TestMlabSavefig()
    t.test()
