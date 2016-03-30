# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest
import numpy

# Local imports.
from mayavi.tests.common import get_example_data

# Enthought library imports
from mayavi.sources.image_reader import ImageReader
from mayavi.tests.data_reader_test_base import DataReaderTestBase

class TestDEMImageReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
         # Read a DEM Image file.
        r = ImageReader()
        r.initialize(get_example_data('example.dem'))
        self.e.add_source(r)
        self.bounds =(557945.0, 567725.0, 5107991.5, 5121971.5, 682.0, 682.0)

    def check(self, scene, bounds, error = 1.01e-02):
        """Do the actual testing."""

        src = scene.children[0]
        ot = src.children[0].children[0]
        ot.render() # Flush the pipeline.

        # Check the outline bounds
        self.assertEqual(numpy.allclose(ot.outline_filter.output.bounds,bounds,
                                    atol=error), True)
        self.assertEqual(src.reader.spatial_resolution, (30.0, 30.0, 1.0))
        self.assertEqual(src.reader.elevation_bounds, (682.0, 2543.0))

    def test_dem_image_data_reader(self):
        "Test if the test fixture works"
        #Now test.

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)

class TestMHAImageReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
         # Read a Meta Image file.
        r = ImageReader()
        r.initialize(get_example_data('foot.mha'))
        self.e.add_source(r)
        self.bounds =(0.0, 255.0, 0.0, 255.0, 0.0, 0.0)

    def check(self, scene, bounds, error = 1.01e-02):
        """Do the actual testing."""

        src = scene.children[0]
        ot = src.children[0].children[0]
        ot.render() # Flush the pipeline.

        # Check the outline bounds
        self.assertEqual(numpy.allclose(ot.outline_filter.output.bounds,bounds,
                                    atol=error), True)
        self.assertEqual(numpy.allclose(src.reader.data_spacing,(1., 1., 1.)),True)

    def test_mha_image_data_reader(self):
        "Test if the test fixture works"
        #Now test.

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)

if __name__ == '__main__':
    unittest.main()
