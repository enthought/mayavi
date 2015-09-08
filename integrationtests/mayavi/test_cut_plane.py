"""Simple test for the scalar cut plane
"""
# Author: Deepak Surti
# Copyright (c) 2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.

# Local imports.
from common import TestCase, get_example_data

class TestCutPlane(TestCase):
    def check(self):
        """Do the actual testing."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        src = scene.children[0]
        mm = src.children[0]
        cp = mm.children[0]
        ip = cp.implicit_plane
        poly_data = cp.cutter.outputs[0]
        initial_cells = poly_data.number_of_cells

        # Change the plane normal
        ip.normal = 1, 1, 1
        updated_cells =  poly_data.number_of_cells
        assert initial_cells != updated_cells

        # Change the plane origin
        ip.normal = 1, 1, 1
        updated_cells =  poly_data.number_of_cells
        assert initial_cells != updated_cells

    def test(self):
        self.main()

    def add_cut_plane(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.modules.scalar_cut_plane import ScalarCutPlane

        ############################################################
        # An interactive scalar cut plane.
        cp = ScalarCutPlane()
        script.add_module(cp)
        ip = cp.implicit_plane
        ip.normal = 0,0,1
        ip.origin = 0,0,5
        ip.widget.enabled = False

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

        ############################################################
        # Create a new scene and set up the visualization for structured data.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(get_example_data('heart.vtk'))
        script.add_source(r)

        # Add the scalar cut plane
        self.add_cut_plane()

        # Set the scene to an isometric view.
        s.scene.isometric_view()

        # Now test.
        self.check()

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Create a new scene and set up the visualization for unstructured data.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('fire_ug.vtu'))
        script.add_source(r)

        # Add the scalar cut plane
        self.add_cut_plane()

        # Set the scene to an isometric view.
        s.scene.isometric_view()

        # Now test.
        self.check()

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

if __name__ == "__main__":
    t = TestCutPlane()
    t.test()
