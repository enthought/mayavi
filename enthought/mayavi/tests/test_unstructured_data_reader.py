# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Local imports.
from common import get_example_data

# Enthought library imports
from enthought.mayavi.sources.unstructured_grid_reader import UnstructuredGridReader
from enthought.mayavi.tests.data_reader_test_base import DataReaderTestBase

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
        
class TestExodusReader(DataReaderTestBase):
    
    def setup_reader(self):
        
        """"Setup the reader in here.  This is called after the engine 
        has been created and started.  The engine is available as 
        self.e.  This method is called by setUp().
        """
        # Read a Exodus data file.
        r = UnstructuredGridReader()
        r.initialize(get_example_data('edgeFaceElem.exii'))
        self.e.add_source(r)
        self.bounds =(-3.0, 3.0, -3.0, 3.0, -3.0, 3.0)
    
    def test_exodus_data_reader(self): 
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
