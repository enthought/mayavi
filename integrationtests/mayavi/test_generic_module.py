"""Simple test for the GenericModule.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from mayavi.core.common import get_output
from common import TestCase, get_example_data


class TestGenericModule(TestCase):

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.filters.optional import Optional
        from mayavi.filters.warp_scalar import WarpScalar
        from mayavi.filters.cut_plane import CutPlane
        from mayavi.components.poly_data_normals import PolyDataNormals
        from mayavi.components.contour import Contour
        from mayavi.components.actor import Actor
        from mayavi.modules.generic_module import GenericModule
        from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # We now create the complete equivalent of a ScalarCutPlane in
        # the next block!
        cp = CutPlane()
        w = WarpScalar()
        warper = Optional(filter=w, label_text='Enable warping', enabled=False)
        c = Contour()
        ctr = Optional(filter=c, label_text='Enable contours', enabled=False)
        p = PolyDataNormals(name='Normals')
        normals = Optional(filter=p, label_text='Compute normals', enabled=False)
        a = Actor()
        components = [cp, warper, ctr, normals, a]
        m = GenericModule(name='ScalarCutPlane',
                          components=components,
                          contour=c, actor=a)

        script.add_module(m)
        s.scene.isometric_view()

        ########################################
        # do the testing.
        def check(mod):
            """Check if test status is OK for the given module."""
            cut, warper, ctr, normals, a = mod.components
            c = ctr.filter
            # The intermediate ones are disabled.
            assert normals.outputs[0] is cut.outputs[0]
            # Enable the contours.
            ctr.enabled = True
            assert ctr.outputs[0] is c.outputs[0]
            assert ctr.outputs[0] is normals.outputs[0]
            n_output = get_output(normals.outputs[0])
            rng = n_output.point_data.scalars.range
            assert (rng[1] - rng[0]) < 1e-4
            # Turn on auto-contours
            c.auto_contours = True
            # Increase number of contours and the range should change.
            c.number_of_contours = 10
            n_output = get_output(normals.outputs[0])
            assert len(n_output.points) != 0
            rng = n_output.point_data.scalars.range
            assert rng[0] < rng[1]
            # Check if pipeline_changed is correctly propagated.
            old = get_output(normals.outputs[0])
            assert a.mapper.scalar_mode == 'default'
            c.filled_contours = True
            n_output = get_output(normals.outputs[0])
            c_output = get_output(c.outputs[0])
            assert n_output != old
            assert n_output is c_output
            # Check if the actor responds correctly to the
            # filled_contour change.
            assert a.mapper.scalar_mode == 'use_cell_data'

            # Set back everything to original state.
            c.filled_contours = False
            assert a.mapper.scalar_mode == 'default'
            c.number_of_contours = 1
            c.auto_contours = False
            ctr.enabled = False
            assert normals.outputs[0] is cut.outputs[0]

        check(m)

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
        m = s.children[0].children[0].children[0]
        check(m)

        ############################################################
        # Test if the Mayavi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now do the check.
        m = s.children[0].children[0].children[0]
        s.scene.isometric_view()
        check(m)

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        # Now do the check.
        m = s.children[0].children[0].children[0]
        s.scene.isometric_view()
        check(m)

        # If we have come this far, we are golden!

if __name__ == "__main__":
    t = TestGenericModule()
    t.test()
