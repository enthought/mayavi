# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import numpy
import unittest

# Enthought library imports.
from mayavi.core.null_engine import NullEngine
from mayavi.sources.builtin_surface import BuiltinSurface
from mayavi.modules.surface import Surface
from mayavi.modules.outline import Outline


class TestBuiltinSurfaceSource(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by
        TestCase before any other test method is invoked"""

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()

        poly_data = BuiltinSurface()
        e.add_source(poly_data)

        outline = Outline()
        e.add_module(outline)

        surface = Surface()
        e.add_module(surface)

        poly_data.data_source.shaft_radius = 0.05
        poly_data.data_source.shaft_resolution = 7
        poly_data.data_source.tip_radius = 0.1

        self.e=e
        self.scene = e.current_scene

        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase
        after the test methods have been invoked"""
        self.e.stop()
        return

    def test_poly_data_source(self):
        """Do the basic testing"""
        s = self.scene
        src = s.children[0]

        #Check the properties of the default source
        self.assertEqual(src.source,'arrow')
        self.assertEqual(src.data_source.shaft_radius,0.05)
        self.assertEqual(src.data_source.shaft_resolution,7)
        self.assertEqual(src.data_source.tip_radius,0.1)

    def check(self):
        """Do the actual testing."""
        s = self.scene
        src = s.children[0]
        ot = src.children[0].children[0]
        ot.render() # Flush the pipeline.

        # Check the outline bounds
        self.assertEqual(numpy.allclose(ot.outline_filter.output.bounds,
                                        (-0.5, 0.5, -0.5, 0.5, -0.475, 0.475),
                                        atol=1.01e-03), True)

        self.assertEqual(numpy.allclose(src.data_source.angle, 26.565,
                                        atol=1.01e-03),True)
        self.assertEqual(numpy.allclose(src.data_source.direction,(1., 0., 0.)),True)
        self.assertEqual(src.data_source.radius,0.5)
        self.assertEqual(src.data_source.height,1.0)
        self.assertEqual(numpy.allclose(src.data_source.center,(0., 0., 0.)),True)
        self.assertEqual(src.data_source.resolution, 10)

        #Modify Properties and check again
        src.data_source.height = 1.5
        src.data_source.angle = 30
        src.data_source.modified()
        self.assertEqual(numpy.allclose(src.data_source.radius,0.866,atol=1.01e-03),True)

    def test_change(self):
        """Test if it works fine on changing the source"""
        s = self.scene
        src = s.children[0]
        ot = src.children[0].children[0]
        src.source = 'cone'
        src.data_source.resolution = 10

        # Check with the default properties of cone to verify that the
        # source has actually changed
        self.assertEqual(src.source,'cone')
        self.check()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene
        src = scene.children[0]
        src.source = 'cone'
        src.data_source.resolution = 10

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
