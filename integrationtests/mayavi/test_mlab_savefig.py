import os
import shutil
import sys
import unittest
import tempfile

import numpy
from PIL import Image

from mayavi import mlab
from mayavi.core.engine import Engine
from mayavi.core.off_screen_engine import OffScreenEngine
from mayavi.tools.figure import savefig

from common import TestCase


def create_quiver3d():
    x, y, z = numpy.mgrid[1:10, 1:10, 1:10]
    u, v, w = numpy.mgrid[1:10, 1:10, 1:10]
    s = numpy.sqrt(u**2 + v**2)
    mlab.quiver3d(x, y, z, u, v, w, scalars=s)


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

    def test_many_savefig_offscreen(self):
        """Test if savefig works with off_screen_rendering and Engine"""
        engine = Engine()
        for _ in xrange(5):
            self.setup_engine_and_figure(engine)

            # Use off-screen rendering
            self.figure.scene.off_screen_rendering = True

            # Set up the scene
            create_quiver3d()

            # save the figure
            savefig(self.filename, size=(131, 217), figure=self.figure)
            self.assertImageSavedWithContent(self.filename)

    def assertImageSavedWithContent(self, filename):
        """ Load the image and check that there is some content in it.
        """
        image = numpy.array(Image.open(filename))
        # default is expected to be a totally white image

        self.assertEqual(image.shape[:2], (215, 130))
        if image.shape[2] == 3:
            check = numpy.sum(image == [255, 0, 0], axis=2) == 3
        elif image.shape[2] == 4:
            check = numpy.sum(image == [255, 0, 0, 255], axis=2) == 4
        else:
            self.fail(
                'Pixel size is not 3 or 4, but {0}'.format(image.shape[2]))
        if check.any():
            return
        self.fail('The image looks empty, content was drawn')

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


class TestMlabSavefig(TestCase):

    def test(self):
        self.main()

    def do(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(
            TestMlabSavefigUnitTest)

        result = unittest.TextTestRunner().run(suite)

        if result.errors or result.failures:
            sys.exit(1)


if __name__ == "__main__":
    t = TestMlabSavefig()
    t.test()
