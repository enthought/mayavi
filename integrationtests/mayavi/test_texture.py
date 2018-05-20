import os
import shutil
import sys
import unittest
import tempfile

import numpy
from PIL import Image

from tvtk.api import tvtk
from mayavi import mlab
from mayavi.tools.figure import savefig

from common import TestCase

# path to this dir
MY_DIR = os.path.dirname(__file__)


class TestTextureUnitTest(unittest.TestCase):

    def setUp(self):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, "saved_figure.png")

        # this ensures that the temporary directory is removed
        self.addCleanup(self.remove_tempdir)

        # texture image
        # the image is a black-white checker box pattern
        image_path = os.path.join(
            MY_DIR, "images", "checker.jpg"
        )
        img=tvtk.JPEGReader(file_name=image_path)
        self.texture=tvtk.Texture(input_connection=img.output_port,
                                  interpolate=1)

    def remove_tempdir(self):
        shutil.rmtree(self.temp_dir)

    def mlab_close_all(self):
        mlab.close(all=True)

    def add_texture(self, source, mode):
        # Add texture
        source.actor.actor.mapper.scalar_visibility=False
        source.actor.enable_texture=True
        source.actor.tcoord_generator_mode=mode
        source.actor.actor.texture=self.texture

    def test_texture_curve(self):
        """ Test texture on mlab.surf """
        mlab.figure()
        X, Y = numpy.mgrid[-1:1:20j,-1:1:20j]
        Z = -numpy.cos(Y*X)+.5
        source = mlab.surf(X, Y, Z, color=(1., 1., 1.))

        # ensure the figure is closed at the end of the test
        self.addCleanup(self.mlab_close_all)

        # Apply the texture
        self.add_texture(source, "plane")

        # Zoom in closer for analysis
        mlab.view(67.2, 47, 2.1, [0.22, 0.13, -0.6])

        mlab.savefig(self.filename, size=(400, 300))

        # Check the saved image (if texture fails, std ~ 10)
        self.check_image_std(target_std=150.)

    def test_texture_sphere(self):
        """ Test texture on mlab.points3d (sphere) """
        mlab.figure()
        source = mlab.points3d(0, 0, 0)

        # ensure the figure is closed at the end of the test
        self.addCleanup(self.mlab_close_all)

        # Apply the texture
        self.add_texture(source, "sphere")

        # Zoom in closer for analysis
        mlab.view(-158., 10.4,  2., [0, 0, 0])

        mlab.savefig(self.filename, size=(400, 300))

        # Check the saved image (if texture fails, std ~ 90)
        self.check_image_std(target_std=150.)

    def test_texture_cylinder(self):
        """ Test texture on mlab.points3d (cylinder) """
        mlab.figure()
        source = mlab.points3d(0, 0, 0, mode="cylinder")

        # ensure the figure is closed at the end of the test
        self.addCleanup(self.mlab_close_all)

        # Apply the texture
        self.add_texture(source, "cylinder")

        # Zoom in closer for analysis
        mlab.view(52., 38., 1.4, [0., 0., 0.])

        mlab.savefig(self.filename, size=(400, 300))

        # Check the saved image (if texture fails, std ~ 90)
        self.check_image_std(target_std=150.)

    def check_image_std(self, target_std):
        # Check that the pixels in the image vary greatly as
        # the pattern is a checker box
        image = numpy.array(Image.open(self.filename))[:, :, :3].sum(axis=2)
        message = ("The Texture is a checker box but the image "
                   "pixels do not vary greatly enough. "
                   "It looks wrong. Target standard deviation: {0}, "
                   "got {1}")
        self.assertGreaterEqual(image.std(), target_std,
                                message.format(target_std, image.std()))


class TestTexture(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(
            TestTextureUnitTest)

        result = unittest.TextTestRunner().run(suite)

        if result.errors or result.failures:
            sys.exit(1)


if __name__ == "__main__":
    t = TestTexture()
    t.test()
