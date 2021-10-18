# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Enthought library imports
from mayavi.sources.unstructured_grid_reader import UnstructuredGridReader
from mayavi.tests.data_reader_test_base import DataReaderTestBase

# Local imports.
from mayavi.tests.common import get_example_data


class TestAVSUCDReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a AVSUCD data file.
        r = UnstructuredGridReader()
        r.initialize(get_example_data('cellsnd.ascii.inp'))
        self.e.add_source(r)
        self.bounds =(-2.0, 2.0, -2.0, 2.0, 0.0, 0.0)

    def test_avsucd_data_reader(self):
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


#TODO: Update the ExodusIIReader test for scenarios as for the other readers
#in this module.
@unittest.skip("ExodusIIReader support is disabled for now.")
class TestExodusIIReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a Exodus data file.
        r = UnstructuredGridReader()
        r.initialize(get_example_data('disk_out_ref.ex2'))
        self.e.add_source(r)

    def test_point_cell_data(self):
        """ Test if the point and cell data is parsed correctly."""
        u_grid = self.scene.children[0].outputs[0]
        self.assertEqual(u_grid.point_data.number_of_arrays, 7)
        self.assertEqual(u_grid.cell_data.number_of_arrays, 1)
        self.assertEqual(u_grid.point_data.number_of_tuples, 8499)
        self.assertEqual(u_grid.cell_data.number_of_tuples, 7472)

class TestGambitReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a Gambit data file.
        r = UnstructuredGridReader()
        r.initialize(get_example_data('prism.neu'))
        self.e.add_source(r)
        self.bounds = (-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

    def test_gambit_data_reader(self):
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
