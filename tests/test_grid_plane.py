"""Simple test for the grid plane and outline module.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import os
from os.path import join, abspath
from StringIO import StringIO
import copy

# Local imports.
from common import TestCase, fixpath


class TestGridPlane(TestCase):
    def test(self):        
        ############################################################
        # Imports.
        script = self.script
        from enthought.mayavi.sources.vtk_file_reader import VTKFileReader
        from enthought.mayavi.modules.outline import Outline
        from enthought.mayavi.modules.grid_plane import GridPlane
        
        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(abspath(fixpath(join(os.pardir, 'examples', 'data',
                                          'heart.vtk'))))
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
            gp.actor.property.set(ambient=1.0)

        # Set the scene to an isometric view.
        s.scene.isometric_view()

        # Now compare the image.
        self.compare_image(s, 'images/test_grid_plane.png')

        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = StringIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene
        # Make the scene's size the default so we can test the image.
        #self.set_active_scene_size()

        # Now compare the image.
        self.compare_image(s, 'images/test_grid_plane.png')

        ############################################################
        # Test if the MayaVi2 visualization can be deepcopied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now compare the image.
        self.compare_image(s, 'images/test_grid_plane.png')

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        self.compare_image(s, 'images/test_grid_plane.png')
        
        # If we have come this far, we are golden!
        

if __name__ == "__main__":
    t = TestGridPlane()
    t.run()
