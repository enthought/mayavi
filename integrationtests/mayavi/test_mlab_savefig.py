import os
import shutil
import unittest
import tempfile

import numpy
from PIL import Image

from mayavi import mlab
from mayavi.core.engine import Engine
from mayavi.core.off_screen_engine import OffScreenEngine
from mayavi.tools.figure import savefig

from common import TestCase


def create_quiver3d(figure):
    x, y, z = numpy.mgrid[1:10, 1:10, 1:10]
    u, v, w = numpy.mgrid[1:10, 1:10, 1:10]
    s = numpy.sqrt(u**2 + v**2)
    mlab.quiver3d(x, y, z, u, v, w, scalars=s, figure=figure)


# Note: the figure(window) size is delibrately set to be smaller than
# the required size in `savefig`, this forces the re-rendering to
# occur and catch any potential ill rendering

class TestMlabSavefigUnitTest(unittest.TestCase):

    def setUp(self):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, "saved_figure.png")

        # this ensures that the temporary directory is removed
        self.addCleanup(self.remove_tempdir)

    def remove_tempdir(self):
        shutil.rmtree(self.temp_dir)

    def setup_engine_and_figure(self, engine):
        # Set up a Engine/OffScreenEngine/... for the test case
        self.engine = engine

        if not engine.running:
            engine.start()

        # figure size is set to be small to force re-rendering
        engine.new_scene(size=(90, 100))
        self.figure = engine.current_scene

        # the clean up function will close all figures and stop the engine
        self.addCleanup(self.cleanup_engine, self.engine)

    def cleanup_engine(self, engine):
        """ Close all scenes in the engine and stop it """
        scenes = [scene for scene in engine.scenes]
        for scene in scenes:
            engine.close_scene(scene)
        engine.stop()

    def test_savefig(self):
        """Test if savefig works with auto size, mag and a normal Engine"""
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure (magnification is default "auto")
        savefig(self.filename, figure=self.figure)

        # check
        self.check_image()

    def test_savefig_with_size(self):
        """Test if savefig works with given size and a normal Engine"""
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure (magnification is default "auto")
        savefig(self.filename, size=(131, 217), figure=self.figure)

        # check
        self.check_image((217, 131))

    def test_savefig_with_magnification(self):
        """Test savefig with given magnification and a normal Engine"""
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure with a magnification
        savefig(self.filename, magnification=2, figure=self.figure)

        # check
        self.check_image()

    @unittest.skipIf(os.environ.get("TRAVIS", False),
                     ("Offscreen rendering is not tested on Travis "
                      "due to lack of GLX support"))
    def test_savefig_with_size_offscreen(self):
        """Test if savefig works with given size on an OffScreenEngine"""
        self.setup_engine_and_figure(OffScreenEngine())

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), figure=self.figure)

        # check
        self.check_image((217, 131))

    def test_savefig_with_size_and_magnification(self):
        """Test if savefig works with given size and magnification"""
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    @unittest.skipIf(os.environ.get("TRAVIS", False),
                     ("Offscreen rendering is not tested on Travis "
                      "due to lack of GLX support"))
    def test_savefig_with_size_and_magnification_offscreen(self):
        """Test savefig with off_screen_rendering and OffScreenEngine"""
        self.setup_engine_and_figure(OffScreenEngine())

        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    @unittest.skipIf(os.environ.get("TRAVIS", False),
                     ("Offscreen rendering is not tested on Travis "
                      "due to lack of GLX support"))
    def test_savefig_with_size_and_magnification_offscreen_with_engine(self):
        """Test if savefig works with off_screen_rendering and Engine"""
        self.setup_engine_and_figure(Engine())

        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        create_quiver3d(figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    @unittest.skipIf(os.environ.get("TRAVIS", False),
                     ("Offscreen rendering is not tested on Travis "
                      "due to lack of GLX support"))
    def test_many_savefig_offscreen(self):
        """Test saving many figures offscreen"""
        engine = Engine()
        for _ in xrange(5):
            self.setup_engine_and_figure(engine)

            # Use off-screen rendering
            self.figure.scene.off_screen_rendering = True

            # Set up the scene
            create_quiver3d(figure=self.figure)

            # save the figure
            savefig(self.filename, size=(131, 217),
                    figure=self.figure)

    def check_image(self, size=None):
        image = numpy.array(Image.open(self.filename))[:, :, :3]

        # check the size is correct
        if size:
            self.assertEqual(image.shape[:2], size)

        # check if the image has black spots
        if (numpy.sum(image == [0, 0, 0], axis=2) == 3).any():
            message = "The image has black spots"
            self.fail(message)


class TestMlabSavefig(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(
            TestMlabSavefigUnitTest)
        unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    t = TestMlabSavefig()
    t.test()
