import os
import shutil
import sys
import unittest
import tempfile

import numpy
from PIL import Image

from tvtk.api import tvtk
from mayavi import mlab

from common import TestCase

# path to mayavi source
MAYAVI_DIR = os.path.split(mlab.__file__)[0]


class TestTextureUnitTest(unittest.TestCase):

    def setUp(self):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()

        # We save the same image twice to calibrate the difference in pixels
        # simply from rendering it again
        self.original_image_file = os.path.join(self.temp_dir,
                                                "saved_figure.png")
        self.same_image_file = os.path.join(self.temp_dir,
                                            "same_saved_figure.png")

        # This is an image with the texture inverted
        # The differences in pixels between original image and this one
        # should be greater than the difference between the two saved images
        # above
        self.inverted_image_file = os.path.join(self.temp_dir, "inverted.png")

        # this ensures that the temporary directory is removed
        self.addCleanup(self.remove_tempdir)

        # texture image
        # the image is a black-white checker box pattern
        image_path = os.path.join(
            MAYAVI_DIR, "../integrationtests/mayavi/images/checker.jpg")
        img = tvtk.JPEGReader(file_name=image_path)
        self.texture = tvtk.Texture(input_connection=img.output_port,
                                    interpolate=1)

        # inverted version of the same image
        image_path = os.path.join(
            MAYAVI_DIR,
            "../integrationtests/mayavi/images/checker_inverted.jpg")
        img = tvtk.JPEGReader(file_name=image_path)
        self.texture_inverted = tvtk.Texture(
            input_connection=img.output_port,
            interpolate=1)

    def remove_tempdir(self):
        shutil.rmtree(self.temp_dir)

    def mlab_close_all(self):
        mlab.close(all=True)

    def add_texture(self, source, mode):
        # Add texture
        source.actor.actor.mapper.scalar_visibility = False
        source.actor.enable_texture = True
        source.actor.tcoord_generator_mode = mode
        source.actor.actor.texture = self.texture

    def test_texture_curve(self):
        """ Test texture on mlab.surf """
        mlab.figure()
        X, Y = numpy.mgrid[-1:1:20j, -1:1:20j]
        Z = -numpy.cos(Y*X)+.5
        source = mlab.surf(X, Y, Z, color=(1., 1., 1.))

        # ensure the figure is closed at the end of the test
        self.addCleanup(self.mlab_close_all)

        # Apply the texture
        self.add_texture(source, "plane")

        # Zoom in closer for analysis
        mlab.view(67.2, 47, 2.1, [0.22, 0.13, -0.6])

        mlab.savefig(self.original_image_file)
        mlab.savefig(self.same_image_file)

        # Change the texture to the inverted one
        source.actor.actor.texture = self.texture_inverted
        mlab.savefig(self.inverted_image_file)

        self.check_images_differ(self.original_image_file,
                                 self.same_image_file,
                                 self.inverted_image_file)

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

        mlab.savefig(self.original_image_file)
        mlab.savefig(self.same_image_file)

        # Change the texture to the inverted one
        source.actor.actor.texture = self.texture_inverted
        mlab.savefig(self.inverted_image_file)

        self.check_images_differ(self.original_image_file,
                                 self.same_image_file,
                                 self.inverted_image_file)

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

        mlab.savefig(self.original_image_file)
        mlab.savefig(self.same_image_file)

        # Change the texture to the inverted one
        source.actor.actor.texture = self.texture_inverted
        mlab.savefig(self.inverted_image_file)

        self.check_images_differ(self.original_image_file,
                                 self.same_image_file,
                                 self.inverted_image_file)

    def check_images_differ(self, original_image_file, same_image_file,
                            inverted_image_file):
        ''' Check if the difference between inverted_image_file and
        original_image_file is greater than the difference between
        the same_image_file and original_image_file '''
        # These two images have the same textures
        # But when they are saved, re-rendering may lead to some differences
        # in their pixels
        original_image = numpy.array(
            Image.open(original_image_file))[:, :, :3].sum(axis=2)
        same_image = numpy.array(
            Image.open(same_image_file))[:, :, :3].sum(axis=2)

        # Inverted texture
        inverted_image = numpy.array(
            Image.open(inverted_image_file))[:, :, :3].sum(axis=2)

        ref_diff = numpy.abs(
            original_image.ravel() - same_image.ravel())

        sample_diff = numpy.abs(
            inverted_image.ravel() - original_image.ravel())

        self.assertGreater(sum(sample_diff > 0), 2*sum(ref_diff > 0),
                           "Applying an image and its inverse as textures. "
                           "However the images do not differ greatly.")


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
