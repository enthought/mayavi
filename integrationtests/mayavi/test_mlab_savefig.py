import os
import shutil
import sys
import unittest
import tempfile

import numpy

from mayavi import mlab
from mayavi.core.engine import Engine
from mayavi.core.off_screen_engine import OffScreenEngine
from mayavi.tools.figure import savefig, screenshot

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

    @unittest.skipIf(os.environ.get("TRAVIS", False),
                     ("Offscreen rendering is not tested on Travis "
                      "due to lack of GLX support"))
    def test_many_savefig_offscreen(self):
        """Test if savefig works with off_screen_rendering and Engine"""
        engine = Engine()
        for _ in range(5):
            self.setup_engine_and_figure(engine)

            # Use off-screen rendering
            self.figure.scene.off_screen_rendering = True

            # Set up the scene
            create_quiver3d()

            # save the figure
            savefig(self.filename, size=(131, 217),
                    figure=self.figure)

    def _get_pixel_ratio(self, fig):
        return getattr(fig.scene._vtk_control, '_pixel_ratio', 1.0)

    def test_mlab_screenshot(self):
        # Given
        engine = Engine()
        self.setup_engine_and_figure(engine)
        create_quiver3d()
        sz = self.figure.scene.get_size()
        pixel_ratio = self._get_pixel_ratio(self.figure)
        sz = (sz[0]*pixel_ratio, sz[1]*pixel_ratio)

        for aa in (False, True):
            # When
            data = screenshot(mode='rgb', antialiased=aa)
            # Then
            self.assertEqual(data.shape, (sz[1], sz[0], 3))

            # When
            data = screenshot(mode='rgba', antialiased=aa)
            # Then
            self.assertEqual(data.shape, (sz[1], sz[0], 4))


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
