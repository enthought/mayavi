# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import unittest

# Local imports.
from mayavi.tests.common import get_example_data

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
from mayavi.modules.api import ContourGridPlane
from mayavi.filters.image_data_probe import ImageDataProbe

class TestImageDataProbe(unittest.TestCase):

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
        idp = ImageDataProbe()
        idp.rescale_scalars = True
        e.add_filter(idp)
        cgp = ContourGridPlane(enable_contours=False)
        e.add_module(cgp)
        cgp.grid_plane.axis = 'z'
        cgp.grid_plane.position = 1
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing"""
        scene = self.scene
        src = scene.children[0]
        idp = src.children[0]
        mm = idp.children[0]

        self.assertEqual(src.get_output_dataset().is_a('vtkUnstructuredGrid'),True)
        self.assertEqual(idp.get_output_dataset().is_a('vtkImageData'),True)
        sc = idp.get_output_dataset().point_data.scalars
        vc = idp.get_output_dataset().point_data.vectors
        self.assertEqual(sc.name,idp.rescaled_scalar_name)
        self.assertEqual(vc.name,'velocity')
        self.assertEqual(mm.scalar_lut_manager.data_name,
                                                idp.rescaled_scalar_name)
        self.assertEqual((abs(sc.range[0]) < 1e-2),True)
        self.assertEqual( abs(sc.range[1] - 65535.0) < 1.e-2,True)
        self.assertEqual((idp.get_output_dataset().dimensions == (3, 3, 2)).all(),True)



    def test_image_data_probe(self):
        "Test if the test fixture works"
        #Now test.
        self.check()

        #from mayavi.tools.show import show
        #show()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene
        self.check()

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

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        source1 = copy.deepcopy(source)
        s.children[0] = source1
        self.check()
        #from mayavi.tools.show import show
        #show()


if __name__ == '__main__':
    unittest.main()
