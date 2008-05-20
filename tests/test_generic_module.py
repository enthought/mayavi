"""Simple test for the GenericModule.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from StringIO import StringIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestGenericModule(TestCase):

    def test(self):
        ############################################################
        # Imports.
        script = self.script
        from enthought.mayavi.filters.optional import Optional
        from enthought.mayavi.components.implicit_plane import ImplicitPlane
        from enthought.mayavi.components.cutter import Cutter
        from enthought.mayavi.filters.warp_scalar import WarpScalar
        from enthought.mayavi.components.poly_data_normals import PolyDataNormals
        from enthought.mayavi.components.contour import Contour
        from enthought.mayavi.components.actor import Actor
        from enthought.mayavi.modules.generic_module import GenericModule
        from enthought.mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
        from enthought.mayavi.components.contour import Contour
        from enthought.mayavi.filters.optional import Optional
        from enthought.mayavi.filters.collection import Collection 
        from enthought.mayavi.filters.api import PolyDataNormals
        from enthought.mayavi.modules.api import Surface

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # We now create the complete equivalent of a ScalarCutPlane in
        # the next block!
        ip = ImplicitPlane()
        cut = Cutter(cut_function=ip.plane)
        w = WarpScalar()
        warper = Optional(filter=w, label_text='Enable warping', enabled=False)
        c = Contour()
        ctr = Optional(filter=c, label_text='Enable contours', enabled=False)
        p = PolyDataNormals(name='Normals') 
        normals = Optional(filter=p, label_text='Compute normals', enabled=False)
        a = Actor()
        components = [ip, cut, warper, ctr, normals, a]
        m = GenericModule(name='ScalarCutPlane',
                          components=components,
                          contour=c, actor=a)

        mayavi.add_module(m)
        s.scene.isometric_view()

        ########################################
        # do the testing.
        def check():
            """Check if test status is OK."""
            # The intermediate ones are disabled.
            assert normals.outputs[0] is cut.outputs[0]
            # Enable the contours.
            ctr.enabled = True
            assert ctr.outputs[0] is c.outputs[0]
            assert ctr.outputs[0] is normals.outputs[0]
            rng = normals.outputs[0].point_data.scalars.range
            assert (rng[1] - rng[0]) < 1e-4
            # Turn on auto-contours
            c.auto_contours = True
            assert len(normals.outputs[0].points) == 0
            # Increase number of contours and the range should change.
            c.number_of_contours = 10
            assert len(normals.outputs[0].points) != 0
            rng = normals.outputs[0].point_data.scalars.range
            assert rng[0] < rng[1]
            # Check if pipeline_changed is correctly propagated.
            old = normals.outputs[0]
            assert a.mapper.scalar_mode == 'default'
            c.filled_contours = True
            assert normals.outputs[0] != old
            assert normals.outputs[0] is c.outputs[0]
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

        check()

        # FIXME: Add persistence support and test for it. 

if __name__ == "__main__":
    t = TestGenericModule()
    t.main()

