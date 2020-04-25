"""Simple test for the contour related modules.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy

# Local imports.
from common import TestCase, get_example_data


class TestContour(TestCase):
    def check(self):
        """Do the actual testing."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        src = scene.children[0]
        mm = src.children[0]
        cgp1 = mm.children[1]
        assert cgp1.grid_plane.position == 15

        cgp2 = mm.children[2]
        assert cgp2.contour.filled_contours == True
        assert cgp2.grid_plane.axis == 'y'
        assert cgp2.grid_plane.position == 15

        iso = mm.children[3]
        ctr = iso.contour.contours
        assert iso.compute_normals == True
        assert ctr == [200.0]
        rng = iso.actor.mapper.input.point_data.scalars.range
        assert rng[0] == 200.0
        assert rng[1] == 200.0

        cp = mm.children[4]
        ip = cp.implicit_plane
        assert abs(numpy.sum(ip.normal - (0,0,1))) < 1e-16
        assert abs(numpy.sum(ip.origin - (0,0,5))) < 1e-16
        assert ip.widget.enabled == False

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.modules.outline import Outline
        from mayavi.modules.iso_surface import IsoSurface
        from mayavi.modules.contour_grid_plane \
             import ContourGridPlane
        from mayavi.modules.scalar_cut_plane import ScalarCutPlane

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

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp1 = ContourGridPlane()
        script.add_module(cgp1)
        # Set the position to the middle of the data.
        cgp1.grid_plane.position = 15

        # Another with filled contours normal to 'y' axis.
        cgp2 = ContourGridPlane()
        cgp2.contour.filled_contours = True
        # Set the axis and position to the middle of the data.
        cgp2.grid_plane.axis = 'y'
        cgp2.grid_plane.position = 15
        script.add_module(cgp2)

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

        # Now test.
        self.check()

        ############################################################
        # Test if the modules respond correctly when the components
        # are changed.
        ctr = cgp2.contour
        cgp2.contour = ctr.__class__()
        cgp2.contour = ctr
        cgp2.actor = cgp2.actor.__class__()

        iso.contour = iso.contour.__class__()
        iso.contour.contours = [200.0]
        iso.actor = iso.actor.__class__()
        iso.normals = iso.normals.__class__()

        ip = cp.implicit_plane
        cp.implicit_plane = cp.implicit_plane.__class__()
        cp.implicit_plane = ip
        ip.widget.enabled = False
        cp.contour = cp.contour.__class__()
        cp.cutter = cp.cutter.__class__()
        cp.actor = cp.actor.__class__()

        s.render()

        # Now check.
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

    def do_profile(self):
        ############################################################
        # Imports.
        ############################################################
        script = self.script
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.modules.outline import Outline
        from mayavi.modules.iso_surface import IsoSurface
        from mayavi.modules.contour_grid_plane \
             import ContourGridPlane
        from mayavi.modules.scalar_cut_plane import ScalarCutPlane

        ############################################################
        # Create a new scene and set up the visualization.
        ############################################################
        s = self.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(get_example_data('heart.vtk'))

        script.add_source(r)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp1 = ContourGridPlane()
        script.add_module(cgp1)
        # Set the position to the middle of the data.
        cgp1.grid_plane.position = 15

        # Another with filled contours normal to 'y' axis.
        cgp2 = ContourGridPlane()
        cgp2.contour.filled_contours = True
        # Set the axis and position to the middle of the data.
        cgp2.grid_plane.axis = 'y'
        cgp2.grid_plane.position = 15
        script.add_module(cgp2)

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

        s.render()

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

if __name__ == "__main__":
    t = TestContour()
    t.test()
