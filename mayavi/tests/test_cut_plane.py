# Author: Deepak Surti <dsurti@enthought.com>
# Copyright (c) 2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

# Local imports.
from . import datasets
from .common import get_example_data

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.modules.scalar_cut_plane import ScalarCutPlane
from mayavi.sources.unstructured_grid_reader import UnstructuredGridReader


class TestCutter(unittest.TestCase):

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase
           before any other test method is invoked"""

        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #from mayavi.core.engine import Engine
        #e = Engine()
        e.start()
        e.new_scene()
        self.e = e

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the
           test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """ Configures the scalar cut plane and checks the cutter output
            changes when the plane is changed.
        """
        e = self.e

        # An interactive scalar cut plane.
        cp = ScalarCutPlane()
        e.add_module(cp)
        self.cp = cp

        ip = cp.implicit_plane
        ip.origin = -1.5, -1.5, -1.5
        poly_data = cp.cutter.outputs[0].output
        initial_cells = poly_data.number_of_cells

        # Change the plane normal
        ip.normal = 1, 1, 1
        updated_cells =  poly_data.number_of_cells
        self.assertNotEqual(initial_cells, updated_cells)

        # Change the plane origin
        ip.normal = 1, 1, 1
        updated_cells =  poly_data.number_of_cells
        self.assertNotEqual(initial_cells, updated_cells)

    def test_with_structured_data(self):
        e = self.e

        sgrid=datasets.generateStructuredGrid()
        src = VTKDataSource(data = sgrid)
        e.add_source(src)

        self.check()

    def test_with_unstructured_data(self):
        e = self.e

        # Read a AVSUCD data file.
        r = UnstructuredGridReader()
        r.initialize(get_example_data('cellsnd.ascii.inp'))
        e.add_source(r)

        self.check()

if __name__ == '__main__':
    unittest.main()
