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


class TestMlabSavefigUnitTest(unittest.TestCase):

    def setUp(self):
        # Make a temporary directory for saved figures
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, "saved_figure.png")

        # this ensures that the temporary directory is removed
        self.addCleanup(self.remove_tempdir)

    def setup_engine_and_figure(self, engine):
        self.engine = engine

        if not engine.running:
            engine.start()

        engine.new_scene()
        self.figure = engine.current_scene

        self.addCleanup(self.cleanup_engine, self.engine)

    def cleanup_engine(self, engine):
        scenes = [scene for scene in engine.scenes]
        for scene in scenes:
            engine.close_scene(scene)
        engine.stop()

    def remove_tempdir(self):
        shutil.rmtree(self.temp_dir)

    def test_savefig_with_size(self):
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z, figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), figure=self.figure)

        # check
        self.check_image((217, 131))

    def test_savefig_with_size_offscreen(self):
        self.setup_engine_and_figure(OffScreenEngine())

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z, figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), figure=self.figure)

        # check
        self.check_image((217, 131))

    def test_savefig_with_size_and_magnification(self):
        self.setup_engine_and_figure(Engine())

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z, figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    def test_savefig_with_size_and_magnification_offscreen(self):
        self.setup_engine_and_figure(OffScreenEngine())

        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z, figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    def test_savefig_with_size_and_magnification_offscreen_with_engine(self):
        self.setup_engine_and_figure(Engine())

        # Use off-screen rendering
        self.figure.scene.off_screen_rendering = True

        # Set up the scene
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z, figure=self.figure)

        # save the figure
        savefig(self.filename, size=(131, 217), magnification=2,
                figure=self.figure)

        # check if the image size is twice as big
        self.check_image((434, 262))

    def check_image(self, size):
        image = numpy.array(Image.open(self.filename))[:, :, :3]

        # check the size is correct
        self.assertEqual(image.shape[:2], size)


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
