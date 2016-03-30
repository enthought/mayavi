# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest

import numpy

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from mayavi.modules.outline import Outline
from mayavi.modules.contour_grid_plane import ContourGridPlane
from mayavi.modules.scalar_cut_plane import ScalarCutPlane

# Local imports.
from mayavi.tests.common import get_example_data

class TestVTKXMLReader(unittest.TestCase):

    def setUp(self):

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e

        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('cube.vti'))
        e.add_source(r)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp1 = ContourGridPlane()
        e.add_module(cgp1)
        # Set the position to the middle of the data.
        cgp1.grid_plane.position = 1

        # Another with filled contours normal to 'y' axis.
        cgp2 = ContourGridPlane()
        cgp2.contour.filled_contours = True
        # Set the axis and position to the middle of the data.
        cgp2.grid_plane.axis = 'y'
        cgp2.grid_plane.position = 1
        e.add_module(cgp2)

        # An interactive scalar cut plane.
        cp = ScalarCutPlane()
        e.add_module(cp)
        ip = cp.implicit_plane
        ip.normal = 0,0,1
        ip.origin = 0.5, 0.5, 1.0
        # Since this is running offscreen this seems necessary.
        ip.widget.origin = 0.5, 0.5, 1.0
        ip.widget.enabled = False
        self.scene = e.current_scene
        self.cgp2=cgp2
        self.cp=cp
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing."""
        scene = self.scene
        src = scene.children[0]
        mm = src.children[0]
        cgp1 = mm.children[1]
        self.assertEqual(cgp1.grid_plane.position,1)

        cgp2 = mm.children[2]
        self.assertEqual(cgp2.contour.filled_contours,True)
        self.assertEqual(cgp2.grid_plane.axis, 'y')
        self.assertEqual(cgp2.grid_plane.position,1)

        cp = mm.children[3]
        ip = cp.implicit_plane
        self.assertAlmostEqual(numpy.sum(ip.normal - (0,0,1)) , 1e-16)
        self.assertAlmostEqual(numpy.sum(ip.origin - (0.5, 0.5, 1.0)), 0.0)
        self.assertEqual(ip.widget.enabled,False)



    def test_vtk_xml_reader(self):
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
        cp = source.children[0].children[-1]
        cp.implicit_plane.widget.enabled = False

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        cp = source1.children[0].children[-1]
        cp.implicit_plane.widget.enabled = False
        self.check()
        #from mayavi.tools.show import show
        #show()

if __name__ == '__main__':
    unittest.main()
