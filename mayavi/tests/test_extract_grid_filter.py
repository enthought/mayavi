# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran
# Copyright (c) 2009,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest
from numpy import random, allclose, arange

# Local imports.
from mayavi.core.null_engine import NullEngine

# Enthought library imports
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.modules.grid_plane import GridPlane
from mayavi.modules.axes import Axes
from mayavi.filters.extract_grid import ExtractGrid
from tvtk.api import tvtk
from tvtk.common import is_old_pipeline

class TestExtractGridFilter(unittest.TestCase):

    def make_scatter(self):
        pd = tvtk.PolyData()
        pd.points = 100 + 100*random.random((1000, 3))
        verts = arange(0, 1000, 1)
        verts.shape = (1000, 1)
        pd.verts = verts
        pd.point_data.scalars = random.random(1000)
        pd.point_data.scalars.name = 'scalars'
        return pd

    def make_grid4scatter(self):
        src = VTKDataSource()
        xmin, xmax, dx = 100, 200, 2
        nx = int((xmax-xmin)/dx)+1
        ymin, ymax, dy = 100, 200, 2
        ny = int((ymax-ymin)/dy)+1
        zmin, zmax, dz = 100, 200, 2
        nz  = int((zmax-zmin)/dz)+1
        image_data = tvtk.ImageData(origin=(xmin, ymin, zmin),
                                    spacing=(dx, dy, dz),
                                    extent=(0, nx-1, 0, ny-1, 0, nz-1))
        if is_old_pipeline():
            image_data.whole_extent = image_data.extent
        src.data = image_data
        return src

    def setUp(self):
        """Initial setting up of test fixture, automatically called by
        TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()
        self.e=e
        self.s=s

        ############################################################
        # Create a new scene and set up the visualization.

        #Make the grid
        grid = self.make_grid4scatter()
        e.add_source(grid)

        eg = ExtractGrid()
        e.add_filter(eg)

        nb_ticks = 6

        eg.x_ratio = eg.y_ratio = eg.z_ratio = 100/(nb_ticks-1)/2

        gpx = GridPlane()
        e.add_module(gpx)
        gpx.grid_plane.axis = 'x'

        gpy = GridPlane()
        e.add_module(gpy)
        gpy.grid_plane.axis = 'y'

        gpz = GridPlane()
        e.add_module(gpz)
        gpz.grid_plane.axis = 'z'

        #Add the scatter
        d = VTKDataSource()
        d.data = self.make_scatter()
        e.add_source(d)
        if is_old_pipeline():
            a = Axes()
            e.add_module(a)
            a.axes.number_of_labels = nb_ticks

        self.eg = eg
        self.gpx = gpx
        self.gpy = gpy
        self.gpz = gpz
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase
        after the test methods have been invoked"""
        self.e.stop()
        return

    def test_extract_grid_filter_sample(self):
        import sys
        if sys.platform != "darwin":
            raise unittest.SkipTest("actor.bounds returns incorrect values")
        "Test if the sample rate works."
        eg = self.eg
        gpx = self.gpx
        gpy = self.gpy
        gpz = self.gpz

        self.assertEqual(allclose(gpx.actor.actor.bounds,
                        (100.0, 100.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 200.0, 100.0, 100.0)), True)

        eg.x_ratio = eg.y_ratio = eg.z_ratio = 25

        self.assertEqual(allclose(gpx.actor.actor.bounds,
                         (100.0, 100.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 200.0, 100.0, 100.0)), True)

        eg.x_ratio = eg.y_ratio = eg.z_ratio = 5

        self.assertEqual(allclose(gpx.actor.actor.bounds,
                         (100.0, 100.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 200.0, 100.0, 100.0)), True)
        return

    def test_voi(self):
        import sys
        if sys.platform != "darwin":
            raise unittest.SkipTest("actor.bounds returns incorrect values")
        "Test if setting the VOI works correctly."
        eg = self.eg
        gpx = self.gpx
        gpy = self.gpy
        gpz = self.gpz

        self.assertEqual(allclose(gpx.actor.actor.bounds,
                        (100.0, 100.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 200.0, 100.0, 100.0)), True)

        eg.x_ratio = eg.y_ratio = eg.z_ratio = 10

        # Now changing the VOI and then setting the ratio used to
        # show a stupid bug in the grid plane so we test that here.
        eg.trait_set(x_min=10, x_max=40)
        eg.x_ratio = 5

        self.assertEqual(allclose(gpx.actor.actor.bounds,
                         (120.0, 120.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (120.0, 180.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (120.0, 180.0, 100.0, 200.0, 100.0, 100.0)), True)

        # Set some smaller VOI.
        eg.trait_set(y_min=20, y_max=40, z_min=10, z_max=30)
        eg.trait_set(x_ratio = 1, y_ratio=1, z_ratio=1)

        # Reset it and it should go right back.
        eg.trait_set(x_min=0, x_max=50, y_min=0, y_max=50, z_min=0, z_max=50)
        self.assertEqual(allclose(gpx.actor.actor.bounds,
                        (100.0, 100.0, 100.0, 200.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpy.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 100.0, 100.0, 200.0)), True)
        self.assertEqual(allclose(gpz.actor.actor.bounds,
                         (100.0, 200.0, 100.0, 200.0, 100.0, 100.0)), True)

        #from mayavi.tools.show import show
        #show()



if __name__ == '__main__':
    unittest.main()
