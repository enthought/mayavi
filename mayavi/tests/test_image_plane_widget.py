# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2015,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy
import unittest
from mock import patch


# Enthought library imports
from mayavi.core.engine import Engine
from mayavi.core.null_engine import NullEngine
from mayavi.sources.array_source import ArraySource
from mayavi.modules.outline import Outline
from mayavi.modules.image_plane_widget import ImagePlaneWidget
from mayavi.tests.common import get_example_data
from mayavi import mlab


class TestImagePlaneWidget(unittest.TestCase):


    def make_data(self):
        """Creates suitable data for the test."""
        dims = numpy.array((64, 64, 64), 'i')

        # Create some scalars to render.
        dx, dy, dz = 10.0/(dims - 1)
        x = numpy.reshape(numpy.arange(-5.0, 5.0+dx*0.5, dx, 'f'),
                          (dims[0], 1, 1))
        y = numpy.reshape(numpy.arange(-5.0, 5.0+dy*0.5, dy, 'f'),
                          (1, dims[1], 1))
        z = numpy.reshape(numpy.arange(-5.0, 5.0+dz*0.5, dz, 'f'),
                          (1, 1, dims[0]))
        scalars = numpy.sin(x*y*z)/(x*y*z)
        return scalars

    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s=e.new_scene()
        self.e=e
        self.s=s

        ############################################################
        # Create a new scene and set up the visualization.

        d = ArraySource()

        sc = self.make_data()
        d.scalar_data = sc

        e.add_source(d)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)
        # ImagePlaneWidgets for the scalars
        ipw = ImagePlaneWidget()
        e.add_module(ipw)

        ipw_y = ImagePlaneWidget()
        e.add_module(ipw_y)
        ipw_y.ipw.plane_orientation = 'y_axes'

        ipw_z = ImagePlaneWidget()
        e.add_module(ipw_z)
        ipw_z.ipw.plane_orientation = 'z_axes'
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self):
        """Do the actual testing."""

        s=self.scene
        src = s.children[0]
        i1, i2, i3 = src.children[0].children[1:]
        self.assertEqual(i1.ipw.plane_orientation,'x_axes')
        self.assertEqual(numpy.allclose(i1.ipw.center, (0, 31.5, 31.5)),True)
        self.assertEqual( i2.ipw.plane_orientation,'y_axes')
        self.assertEqual(numpy.allclose(i2.ipw.center, (31.5, 0, 31.5)),True)
        self.assertEqual(i3.ipw.plane_orientation,'z_axes')
        self.assertEqual( numpy.allclose(i3.ipw.center, (31.5, 31.5, 0)),True)


    def test_image_plane_widget(self):
        "Test if the test fixture works"
        self.check()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene
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
        sources = s.children
        s.children = []
        # Add it back to see if that works without error.
        s.children.extend(sources)

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        sources1 = copy.deepcopy(sources)
        s.children[:] = sources1
        self.check()


class TestImagePlaneWidgetNewPipeline(unittest.TestCase):

    def setUp(self):
        self._orig_backend = mlab.options.backend
        mlab.options.backend = "test"

    def tearDown(self):
        mlab.options.backend = self._orig_backend

    def test_ipw_works_with_image_data_probe(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        idp = mlab.pipeline.image_data_probe(src)
        with patch('pyface.api.error') as m:
            ipw = mlab.pipeline.image_plane_widget(idp)
        self.assertEqual(m.call_count, 0)
        self.assertEqual(numpy.allclose(ipw.ipw.center, (0.0, 3.0, 1.5)),True)

if __name__ == '__main__':
    unittest.main()
