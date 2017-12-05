# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest
from mayavi.tests import datasets

# Local imports.
from mayavi.core.engine import Engine
from mayavi.core.null_engine import NullEngine

# Enthought library imports
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.modules.outline import Outline
from mayavi.modules.grid_plane import GridPlane


class TestGridPlane(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e

        sgrid = datasets.generateStructuredGrid()
        src = VTKDataSource(data = sgrid)
        e.add_source(src)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        # Create three simple grid plane modules.
        # First normal to 'x' axis.
        gp1 = GridPlane()
        e.add_module(gp1)
        # Second normal to 'y' axis.
        gp2 = GridPlane()
        # We'll test how robust things are by setting attributes
        gp2.grid_plane.axis = 'y'
        gp2.grid_plane.position = 16
        e.add_module(gp2)
        # Third normal to 'z' axis.
        gp3 = GridPlane()
        e.add_module(gp3)
        gp3.grid_plane.axis = 'z'
        gp3.grid_plane.position = 6

        for gp in (gp1, gp2, gp3):
            gp.actor.property.trait_set(ambient=1.0)

        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing."""
        s = self.scene

        mm = s.children[0].children[0]
        gp1, gp2, gp3 = mm.children[1:]
        self.assertEqual(gp1.grid_plane.axis,'x')
        self.assertEqual(gp1.grid_plane.position,0)
        self.assertEqual(gp1.actor.property.ambient,1.0)

        self.assertEqual(gp2.grid_plane.axis,'y')
        self.assertEqual(gp2.grid_plane.position,16)
        self.assertEqual(gp2.actor.property.ambient,1.0)

        self.assertEqual(gp3.grid_plane.axis,'z')
        self.assertEqual(gp3.grid_plane.position,6)
        self.assertEqual(gp3.actor.property.ambient,1.0)

    def test_grid_plane(self):
        "Test if the test fixture works"
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
