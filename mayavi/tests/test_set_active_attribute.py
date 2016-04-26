# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.core.common import get_output
from mayavi.sources.api import VTKXMLFileReader
from mayavi.filters.contour import Contour
from mayavi.filters.api import PolyDataNormals
from mayavi.filters.set_active_attribute import SetActiveAttribute
from mayavi.modules.api import Surface, Outline

# Local imports.
from mayavi.tests.common import get_example_data


class TestSetActiveAttribute(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e

        r = VTKXMLFileReader()
        r.initialize(get_example_data('pyramid_ug.vtu'))
        e.add_source(r)
        r.point_scalars_name = 'temperature'
        o = Outline()
        e.add_module(o)
        c = Contour()
        e.add_filter(c)
        n = PolyDataNormals()
        e.add_filter(n)
        aa = SetActiveAttribute()
        e.add_filter(aa)
        aa.point_scalars_name = 'pressure'
        s = Surface()
        e.add_module(s)
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing"""
        scene = self.scene
        src = scene.children[0]
        self.assertEqual(src.point_scalars_name,'temperature')
        c = src.children[1]
        sc = get_output(c.outputs[0]).point_data.scalars
        self.assertEqual(sc.name,'temperature')
        # It is an iso-contour!
        self.assertEqual(sc.range[0],sc.range[1])
        aa = c.children[0].children[0]
        self.assertEqual(aa.point_scalars_name,'pressure')
        sc = get_output(aa.outputs[0]).point_data.scalars
        self.assertEqual(sc.name, 'pressure')
        self.assertEqual((abs(sc.range[0] - 70) < 1.0),True)
        self.assertEqual((abs(sc.range[1] - 70) < 1.0),True)
        s = aa.children[0].children[0]

    def test_set_active_attribute(self):
        "Test if the test fixture works"
        #Now test.
        self.check()

        #from mayavi.tools.show import show
        #show()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene

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

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        # Pop the source object.
        s =  self.scene
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        self.check()
        #from mayavi.tools.show import show
        #show()



if __name__ == '__main__':
    unittest.main()
