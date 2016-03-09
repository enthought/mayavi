"""Simple test for the UsedDefined filter.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Enthought library imports.
from tvtk.api import tvtk

# Local imports.
from common import TestCase, get_example_data


class TestUserDefined(TestCase):

    def check(self, saved=False):
        """Does the checking, if saved is True it does not change the
        properties at first to see how those behave and only tests the
        final unpickled state."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        src = scene.children[0]
        ud = src.children[0]
        o = ud.children[0].children[0].children[0]
        mm = o.children[0]
        if not saved:
            assert ud.filter.vector_mode == 'compute_gradient'
            assert src.get_output_dataset().point_data.scalars.name == 't'
            assert src.get_output_dataset().point_data.vectors.name == 'uvw'
            expect = ['ScalarGradient', 'Vorticity']
            expect1 = [x +'-y' for x in expect]
            expect2 = [x + ' magnitude' for x in expect]
            # FIXME: This is really a bug in VTK, the name of the scalar
            # should really be ScalarGradient-y.  This is fixed in
            # 5.2 but earlier versions fail.
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


    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from mayavi.filters.optional import Optional
        from mayavi.filters.user_defined import UserDefined
        from mayavi.filters.api import (CellToPointData,
                ExtractVectorNorm, ExtractVectorComponents)
        from mayavi.modules.api import ScalarCutPlane
        from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()
        script = mayavi = self.script

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # Create the filters.
        # CellDerivatives
        cd = tvtk.CellDerivatives()
        ud = UserDefined(filter=cd)
        script.add_filter(ud)
        ctp = CellToPointData()
        ctp.filter.pass_cell_data = False
        script.add_filter(ctp)
        evn = ExtractVectorNorm()
        script.add_filter(evn)
        evc = ExtractVectorComponents(component='y-component')
        o = Optional(filter=evc)
        script.add_filter(o)

        script.add_module(ScalarCutPlane())
        s.scene.isometric_view()

        # Check.
        self.check(saved=False)
        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene
        s.scene.isometric_view()

        # Now do the check.
        self.check(saved=True)

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        # Now do the check.
        s.scene.isometric_view()
        self.check(saved=True)

        # If we have come this far, we are golden!

if __name__ == "__main__":
    t = TestUserDefined()
    t.test()
