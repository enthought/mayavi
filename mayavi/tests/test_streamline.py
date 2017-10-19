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

# Enthought library imports
from mayavi.core.null_engine import NullEngine
from mayavi.sources.array_source import ArraySource
from mayavi.modules.outline import Outline
from mayavi.modules.streamline import Streamline

class TestStreamline(unittest.TestCase):


    def make_data(self):
        """Trivial data -- creates an elementatry scalar field and a
        constant vector field along the 'x' axis."""
        s = numpy.arange(0.0, 10.0, 0.01)
        s = numpy.reshape(s, (10,10,10))
        s = numpy.transpose(s)

        v = numpy.zeros(3000, 'd')
        v[1::3] = 1.0
        v = numpy.reshape(v, (10,10,10,3))
        return s, v

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
        sc, vec = self.make_data()
        d.origin = (-5, -5, -5)
        d.scalar_data = sc
        d.vector_data = vec

        e.add_source(d)

        # Create an outline for the data.
        o = Outline()
        e.add_module(o)

        # View the data.
        st = Streamline()
        e.add_module(st)
        widget = st.seed.widget
        widget.trait_set(radius=1.0, center=(-4.0, -4.0, -4.0),
                   theta_resolution=4, phi_resolution=4)

        st = Streamline(streamline_type='ribbon')
        seed = st.seed
        seed.widget = seed.widget_list[1]
        e.add_module(st)
        seed.widget.trait_set(point1=(-5.0, -4.5, -4.0), point2=(-5.0, -4.5, 4.0))
        st.ribbon_filter.width = 0.25

        st = Streamline(streamline_type='tube')
        seed = st.seed
        seed.widget = seed.widget_list[2]
        e.add_module(st)
        seed.widget.trait_set(center=(-5.0, 1.5, -2.5))
        st.tube_filter.radius = 0.15

        st = Streamline(streamline_type='tube')
        seed = st.seed
        seed.widget = seed.widget_list[3]
        e.add_module(st)
        seed.widget.position=(-5.0, 3.75, 3.75)
        st.tube_filter.radius = 0.2
        self.st = st
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

        st = src.children[0].children[2]
        self.assertEqual(st.streamline_type,'ribbon')
        self.assertEqual(st.ribbon_filter.width,0.25)
        self.assertEqual(st.seed.widget,st.seed.widget_list[1])
        self.assertEqual(numpy.allclose(st.seed.widget.point1,
                            (-5.0, -4.5, -4.0)),True)
        self.assertEqual(numpy.allclose(st.seed.widget.point2,
                            (-5.0, -4.5, 4.0)),True)

        st = src.children[0].children[3]
        self.assertEqual(st.streamline_type,'tube')
        self.assertEqual(st.tube_filter.radius,0.15)
        self.assertEqual(st.seed.widget,st.seed.widget_list[2])
        self.assertEqual(numpy.allclose(st.seed.widget.center,
                            (-5.0, 1.5, -2.5)),True)

        st = src.children[0].children[4]
        self.assertEqual(st.streamline_type,'tube')
        self.assertEqual(st.tube_filter.radius,0.2)
        self.assertEqual(st.seed.widget,st.seed.widget_list[3])
        self.assertEqual(numpy.allclose(st.seed.widget.position,
                            (-5.0, 3.75, 3.75)),True)


    def test_streamline(self):
        "Test if the test fixture works"
        self.check()

    def test_components_changed(self):
        """Test if the modules respond correctly when the components
           are changed."""
        st = self.st
        tf = st.tube_filter
        st.tube_filter = tf.__class__()
        st.tube_filter = tf
        st.ribbon_filter = st.ribbon_filter.__class__()
        seed = st.seed
        st.seed = seed.__class__()
        st.seed = seed
        st.actor = st.actor.__class__()
        tracer = st.stream_tracer
        st.stream_tracer = tracer.__class__()
        st.stream_tracer = tracer
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


if __name__ == '__main__':
    unittest.main()
