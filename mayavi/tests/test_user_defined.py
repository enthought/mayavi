# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.filters.optional import Optional
from mayavi.filters.user_defined import UserDefined
from mayavi.filters.api import (CellToPointData, ExtractVectorNorm, ExtractVectorComponents)
from mayavi.modules.api import ScalarCutPlane
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from tvtk.api import tvtk

# Local imports.
from mayavi.tests.common import get_example_data

class TestUserDefined(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        e.new_scene()
        self.e=e

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('pyramid_ug.vtu'))
        e.add_source(r)

        # Create the filters.
        # CellDerivatives
        cd = tvtk.CellDerivatives()
        ud = UserDefined(filter=cd)
        e.add_filter(ud)
        ctp = CellToPointData()
        ctp.filter.pass_cell_data = False
        e.add_filter(ctp)
        evn = ExtractVectorNorm()
        e.add_filter(evn)
        evc = ExtractVectorComponents(component='y-component')
        o = Optional(filter=evc)
        e.add_filter(o)
        e.add_module(ScalarCutPlane())
        self.scene = e.current_scene
        s = self.scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing."""
        scene = self.scene
        src = scene.children[0]
        ud = src.children[0]
        o = ud.children[0].children[0].children[0]
        mm = o.children[0]

        assert src.get_output_dataset().point_data.scalars.name == 'temperature'
        assert src.get_output_dataset().point_data.vectors.name == 'velocity'
        expect = ['ScalarGradient', 'Vorticity']
        expect1 = [x +'-y' for x in expect]
        expect2 = [x + ' magnitude' for x in expect]

        o.enabled = True
        assert o.get_output_dataset().point_data.scalars.name in expect1
        assert o.get_output_dataset().point_data.vectors.name in expect
        assert mm.scalar_lut_manager.data_name in expect1
        # Turn of extraction.
        o.enabled = False
        assert o.get_output_dataset().point_data.scalars.name in expect2
        assert o.get_output_dataset().point_data.vectors.name in expect
        assert mm.scalar_lut_manager.data_name in expect2

        # Compute the vorticity
        ud.filter.vector_mode = 'compute_vorticity'
        assert o.get_output_dataset().point_data.scalars.name == 'Vorticity magnitude'
        assert o.get_output_dataset().point_data.vectors.name == 'Vorticity'
        assert mm.scalar_lut_manager.data_name == 'Vorticity magnitude'
        # Turn on extraction.
        o.enabled = True
        assert o.get_output_dataset().point_data.scalars.name == 'Vorticity-y'
        assert o.get_output_dataset().point_data.vectors.name == 'Vorticity'
        assert mm.scalar_lut_manager.data_name == 'Vorticity-y'
        # Turn off extraction.
        o.enabled = False

    def test_user_defined(self):
        "Test if the test fixture works"
        #Now test.
        s = self.scene
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
        s = self.scene
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
        s = self.scene

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        s = self.scene
        self.check()
        #from mayavi.tools.show import show
        #show()


if __name__ == '__main__':
    unittest.main()
