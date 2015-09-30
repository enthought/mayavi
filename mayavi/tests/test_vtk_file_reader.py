# Copyright (c) 2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Local imports.
from common import get_example_data

# Enthought library imports
from mayavi.sources.vtk_file_reader import VTKFileReader

# External library imports
import vtk

vtk_major_version = vtk.vtkVersion.GetVTKMajorVersion()
vtk_minor_version = vtk.vtkVersion.GetVTKMinorVersion()

class TestVTKFileReader(unittest.TestCase):
    def setUp(self):
        # Read a VTK data file.
        self.src = VTKFileReader()

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase 
           after the test methods have been invoked"""
        self.src = None
        return

    def check(self, n_points, n_cells):
        """Do the actual testing."""
        output = self.src.outputs[0]
        self.assertEqual(output.number_of_points, n_points)
        self.assertEqual(output.number_of_cells, n_cells)
    
    def test_structured_points_file(self):
        self.src.initialize(get_example_data('texThres2.vtk'))
        self.check(128, 127)
    
    def test_rectiliner_grid_file(self):
        self.src.initialize(get_example_data('RectGrid2.vtk'))
        self.check(17061, 14720)
    
    def test_polydata_file(self):
        self.src.initialize(get_example_data('polyEx.vtk'))
        self.check(8, 6)
    
    def test_structured_grid_file(self):
        self.src.initialize(get_example_data('SampleStructGrid.vtk'))
        self.check(24000, 21489)
    
    @unittest.skipIf(vtk_major_version == 5 and vtk_minor_version < 10,
                    "This test is probably broken in VTK < 5.10")
    def test_unstructured_grid_file(self):
        self.src.initialize(get_example_data('uGridEx.vtk'))
        self.check(27, 12)
    
    def test_field_file(self):
        self.src.initialize(get_example_data('fieldfile.vtk'))
        self.check(18, 3)

if __name__ == '__main__':
    unittest.main()
