"""Simple test for the VTKDataSource source.  This is basically a copy
of test_contour.py with the data source alone modified.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from common import get_example_data
from test_contour import TestContour


class TestVTKDataSource(TestContour):
    def make_data(self):
        script = self.script
        from mayavi.sources.vtk_data_source import VTKDataSource
        from tvtk.api import tvtk

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = tvtk.StructuredPointsReader()
        r.file_name = get_example_data('heart.vtk')
        r.update()
        d = VTKDataSource(data=r.output)
        script.add_source(d)

    def test(self):
        self.main()

    def do(self):
        # Setup the source.
        self.make_data()

        from mayavi.modules.outline import Outline
        from mayavi.modules.iso_surface import IsoSurface
        from mayavi.modules.contour_grid_plane \
             import ContourGridPlane
        from mayavi.modules.scalar_cut_plane import ScalarCutPlane
        script = self.script
        s = script.engine.current_scene
        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp = ContourGridPlane()
        script.add_module(cgp)
        # Set the position to the middle of the data.
        cgp.grid_plane.position = 15

        # Another with filled contours normal to 'y' axis.
        cgp = ContourGridPlane()
        cgp.contour.filled_contours = True
        # Set the axis and position to the middle of the data.
        cgp.grid_plane.axis = 'y'
        cgp.grid_plane.position = 15
        script.add_module(cgp)

        # An isosurface module.
        iso = IsoSurface(compute_normals=True)
        script.add_module(iso)
        iso.contour.contours = [200.0]

        # An interactive scalar cut plane.
        cp = ScalarCutPlane()
        script.add_module(cp)
        ip = cp.implicit_plane
        ip.normal = 0,0,1
        ip.origin = 0,0,5
        ip.widget.enabled = False

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
        # Test if the MayaVi2 visualization can be deep-copied.

        # Pop the source object.
        source = s.children.pop()
        # Add it back to see if that works without error.
        s.children.append(source)
        # Now set the enabled status of the widget, this is impossible
        # to get correctly.
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

        # If we have come this far, we are golden!


if __name__ == "__main__":
    t = TestVTKDataSource()
    t.test()
