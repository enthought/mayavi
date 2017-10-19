"""Simple test for the grid plane and outline module.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestGridPlane(TestCase):
    def check(self):
        script = self.script
        s = script.engine.current_scene
        mm = s.children[0].children[0]
        gp1, gp2, gp3 = mm.children[1:]
        assert gp1.grid_plane.axis == 'x'
        assert gp1.grid_plane.position == 0
        assert gp1.actor.property.ambient == 1.0

        assert gp2.grid_plane.axis == 'y'
        assert gp2.grid_plane.position == 16
        assert gp2.actor.property.ambient == 1.0

        assert gp3.grid_plane.axis == 'z'
        assert gp3.grid_plane.position == 6
        assert gp3.actor.property.ambient == 1.0

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.modules.outline import Outline
        from mayavi.modules.grid_plane import GridPlane

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(get_example_data('heart.vtk'))
        script.add_source(r)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Create three simple grid plane modules.
        # First normal to 'x' axis.
        gp1 = GridPlane()
        script.add_module(gp1)
        # Second normal to 'y' axis.
        gp2 = GridPlane()
        # We'll test how robust things are by setting attributes
        # *before* we add it to the scene.
        gp2.grid_plane.axis = 'y'
        gp2.grid_plane.position = 16
        script.add_module(gp2)
        # Third normal to 'z' axis.
        gp3 = GridPlane()
        script.add_module(gp3)
        gp3.grid_plane.axis = 'z'
        gp3.grid_plane.position = 6

        for gp in (gp1, gp2, gp3):
            gp.actor.property.trait_set(ambient=1.0)

        # Set the scene to an isometric view.
        s.scene.isometric_view()

        self.check()

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

        self.check()

        ############################################################
        # Test if the MayaVi2 visualization can be deepcopied.

        # Pop the source object.
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

        # If we have come this far, we are golden!


if __name__ == "__main__":
    t = TestGridPlane()
    t.test()
