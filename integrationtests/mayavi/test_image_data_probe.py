"""Simple test for the ImageDataProbe filter.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy

# Local imports.
from common import TestCase, get_example_data


class TestImageDataProbe(TestCase):

    def check(self, saved=False):
        """Does the checking, if saved is True it does not change the
        properties at first to see how those behave and only tests the
        final unpickled state."""
        script = self.script
        e = script.engine
        scene = e.current_scene
        src = scene.children[0]
        idp = src.children[0]
        mm = idp.children[0]
        if not saved:
            assert src.get_output_dataset().is_a('vtkUnstructuredGrid')
            assert idp.get_output_dataset().is_a('vtkImageData')
            sc = idp.get_output_dataset().point_data.scalars
            assert sc.name == 't'
            assert mm.scalar_lut_manager.data_name == 't'
            assert abs(sc.range[0]) < 1.0
            assert abs(sc.range[1] - 626.0) < 1.0

            idp.rescale_scalars = True
            idp.dimensions = (41, 19, 19)

        sc = idp.get_output_dataset().point_data.scalars
        assert sc.name == idp.rescaled_scalar_name
        assert mm.scalar_lut_manager.data_name == idp.rescaled_scalar_name
        assert abs(sc.range[0]) < 1e-2
        assert abs(sc.range[1] - 65535.0) < 1.e-2
        assert (idp.get_output_dataset().dimensions == (41, 19, 19)).all()

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from mayavi.filters.image_data_probe import ImageDataProbe
        from mayavi.modules.api import ContourGridPlane
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
        idp = ImageDataProbe()
        script.add_filter(idp)
        cgp = ContourGridPlane(enable_contours=False)
        script.add_module(cgp)
        cgp.grid_plane.axis = 'z'
        cgp.grid_plane.position = 2
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
    t = TestImageDataProbe()
    t.test()
