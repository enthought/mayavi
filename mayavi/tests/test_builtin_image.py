# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import numpy
import unittest
from numpy import array

# Enthought library imports.
from tvtk.common import is_old_pipeline, vtk_major_version
from mayavi.core.null_engine import NullEngine
from mayavi.sources.builtin_image import BuiltinImage
from mayavi.modules.surface import Surface
from mayavi.modules.outline import Outline


class TestBuiltinImageSource(unittest.TestCase):

    def setUp(self):

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        # e = Engine()
        e.start()
        s = e.new_scene()

        image_data = BuiltinImage()
        e.add_source(image_data)

        outline = Outline()
        e.add_module(outline)

        surface = Surface()
        e.add_module(surface)

        image_data.data_source.radius = array([80.,  80.,  80.])
        image_data.data_source.center = array([150.,  150.,    0.])
        image_data.data_source.whole_extent = array([10, 245, 10, 245, 0, 0])
        if is_old_pipeline():
            image_data.data_source.update_whole_extent()
        elif vtk_major_version < 8:
            image_data.data_source.set_update_extent_to_whole_extent()

        self.e = e
        self.scene = e.current_scene

        return

    def tearDown(self):
        self.e.stop()
        return

    def test_data_source(self):
        s = self.scene
        src = s.children[0]
        self.assertEqual(src.source,'ellipsoid')
        self.assertEqual(numpy.allclose(src.data_source.center,(150., 150., 0.)),True)
        self.assertEqual(numpy.allclose(src.data_source.radius,(80., 80., 80.)),True)
        self.assertEqual(numpy.allclose(src.data_source.whole_extent,(10, 245,  10, 245,   0,   0)),True)

    def check(self):
        s = self.scene
        src = s.children[0]
        ot = src.children[0].children[0]
        ot.render()

        # Check with the default properties of gaussian image to verify
        # that the source has actually changed
        self.assertEqual(src.source,'gaussian')
        self.assertEqual(numpy.allclose(src.data_source.center,(0., 0., 0.)),True)
        self.assertEqual(src.data_source.maximum,2.0)
        self.assertEqual(src.data_source.standard_deviation,15)

        # Check the scalar ranges
        sc = src.outputs[0].output.point_data.scalars
        self.assertEqual(numpy.allclose(sc.range, (0, 2.0), atol=1.01e-03), True)

    def test_change(self):
        s = self.scene
        src = s.children[0]
        ot = src.children[0].children[0]
        src.source = 'gaussian'

        # Check with the default properties of gaussian image to verify
        # that the source has actually changed
        self.assertEqual(src.source,'gaussian')
        self.assertEqual(numpy.allclose(src.data_source.center,(0., 0., 0.)),True)
        self.assertEqual(src.data_source.maximum,1.0)
        self.assertEqual(src.data_source.standard_deviation,100)

        # Check the scalar ranges
        self.assertEqual(numpy.allclose(src.outputs[0].output.point_data.scalars.range,
                                        (0.00149, 1.0), atol=1.01e-03),True)

        src.data_source.maximum = 2.0
        src.data_source.standard_deviation = 15
        if not is_old_pipeline():
            src.data_source.update()
        self.check()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene
        src = scene.children[0]
        src.source = 'gaussian'
        src.data_source.maximum = 2.0
        src.data_source.standard_deviation = 15

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        engine.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine.close_scene(scene)

        # Load visualization
        engine.load_visualization(f)
        self.scene = engine.current_scene

        self.check()


if __name__ == '__main__':
    unittest.main()
