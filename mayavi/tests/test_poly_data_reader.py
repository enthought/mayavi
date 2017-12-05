# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Local imports.
from mayavi.tests.common import get_example_data

# Enthought library imports
from mayavi.sources.poly_data_reader import PolyDataReader
from mayavi.tests.data_reader_test_base import DataReaderTestBase

# External library imports
import vtk

vtk_major_version = vtk.vtkVersion.GetVTKMajorVersion()
vtk_minor_version = vtk.vtkVersion.GetVTKMinorVersion()


class TestPDBReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a PDB data file.
        r = PolyDataReader()
        r.initialize(get_example_data('caffeine.pdb'))
        self.e.add_source(r)
        self.bounds = (3.10, 10.78, -2.39, 4.03, -10.60, -6.31)

    def test_pdb_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestBYUReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a BYU data file.
        r = PolyDataReader()
        r.initialize(get_example_data('cow.g'))
        self.e.add_source(r)
        self.bounds = (-4.445, 5.998, -3.608, 2.760, -1.690, 1.690)

    def test_byu_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestOBJReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a OBJ data file.
        r = PolyDataReader()
        r.initialize(get_example_data('shuttle.obj'))
        self.e.add_source(r)
        self.bounds = (-7.65, 7.04, -4.68, 4.68, -1.35, 4.16)

    def test_obj_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestParticleReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a Particle data file.
        r = PolyDataReader()
        r.initialize(get_example_data('Particles.raw'))
        self.e.add_source(r)
        r.reader.trait_set(data_byte_order='big_endian', data_type='float',
                     file_type='binary')
        self.bounds = (817.33, 826.09, 545.02, 571.02, 1443.48, 1511.18)

    def test_particle_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestPLYReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a PLY data file.
        r = PolyDataReader()
        r.initialize(get_example_data('pyramid.ply'))
        self.e.add_source(r)
        self.bounds = (0.0, 1.0, 0.0, 1.0, 0.0, 1.60)

    def test_ply_data_reader(self):
        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        self.check_deepcopying(self.scene, self.bounds)


class TestPointsReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a Points data file.
        r = PolyDataReader()
        r.initialize(get_example_data('points.txt'))
        self.e.add_source(r)
        self.bounds = (0.0, 1.0, 0.0, 1.0, 0.0, 1.0)

    def test_points_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestSTLReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a STL data file.
        r = PolyDataReader()
        r.initialize(get_example_data('humanoid_tri.stla'))
        self.e.add_source(r)
        self.bounds = (0.60, 3.47, -3.96, 3.95, 3.05, 17.39)

    def test_stl_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestFacetReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a Facet data file.
        r = PolyDataReader()
        r.initialize(get_example_data('clown.facet'))
        self.e.add_source(r)
        self.bounds = (-0.5, 0.69, -0.49, 0.49, -1.09, 0.5)

    def test_facet_data_reader(self):
        "Test if the test fixture works"

        self.check(self.scene, self.bounds)

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""

        self.check_saving(self.e, self.scene, self.bounds)

    def test_deepcopied(self):
        """Test if the MayaVi2 visualization can be deep-copied."""
        ############################################################
        # Test if the MayaVi2 visualization can be deep-copied.

        self.check_deepcopying(self.scene, self.bounds)


class TestSLCReader(DataReaderTestBase):

    def setup_reader(self):

        """"Setup the reader in here.  This is called after the engine
        has been created and started.  The engine is available as
        self.e.  This method is called by setUp().
        """
        # Read a SLC data file.
        r = PolyDataReader()
        r.initialize(get_example_data('nut.slc'))
        self.e.add_source(r)
        self.bounds = (0.0, 67.0, 0.0, 40.0, 0.0, 58.0)

    def test_slc_data_reader(self):
        "Test if the test fixture works"

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
