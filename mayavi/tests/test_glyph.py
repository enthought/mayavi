# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import platform
import copy
import numpy
import unittest

# Local imports.
from mayavi.core.null_engine import NullEngine

# Enthought library imports
from mayavi.sources.array_source import ArraySource
from mayavi.modules.outline import Outline
from mayavi.modules.glyph import Glyph
from mayavi.modules.vector_cut_plane import VectorCutPlane


class TestGlyph(unittest.TestCase):

    def make_data(self):
        """Trivial data -- creates an elementatry scalar field and a
        constant vector field along the 'x' axis."""
        s = numpy.arange(0.0, 10.0, 0.01)
        s = numpy.reshape(s, (10, 10, 10))
        s = numpy.transpose(s)

        v = numpy.zeros(3000, 'd')
        v[1::3] = 1.0
        v = numpy.reshape(v, (10, 10, 10, 3))
        return s, v

    def setUp(self):
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        # e = Engine()
        e.start()
        s = e.new_scene()
        self.e = e
        self.s = s

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
        # Glyphs for the scalars
        g = Glyph()
        e.add_module(g)
        g.glyph.glyph_source.glyph_position = 'center'
        g.glyph.glyph.vector_mode = 'use_normal'
        g.glyph.glyph.scale_factor = 0.5
        g.glyph.mask_points.on_ratio = 20
        g.actor.property.line_width = 1.0

        v = VectorCutPlane()
        glyph = v.glyph
        gs = glyph.glyph_source
        gs.glyph_position = 'tail'
        gs.glyph_source = gs.glyph_list[1]
        e.add_module(v)
        v.implicit_plane.trait_set(normal=(0, 1, 0), origin=(0, 3, 0))

        v = VectorCutPlane()
        glyph = v.glyph
        gs = glyph.glyph_source
        gs.glyph_source = gs.glyph_list[2]
        gs.glyph_position = 'head'
        e.add_module(v)
        v.implicit_plane.trait_set(normal=(0, 1, 0), origin=(0, -2, 0))
        self.g=g
        self.v=v
        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        self.e.stop()
        return

    def check(self, mask=False, mask_random_mode=False):
        """Do the actual testing with and without masking. For masking,
           both the presence and absence of random mode is also tested.
        """
        s = self.scene
        src = s.children[0]
        g = src.children[0].children[1]
        self.assertEqual(g.glyph.glyph_source.glyph_position, 'center')
        self.assertEqual(g.glyph.glyph.vector_mode, 'use_normal')
        self.assertEqual(g.glyph.glyph.scale_factor, 0.5)
        self.assertEqual(g.actor.property.line_width, 1.0)
        # Test masking
        n_output_points = src.outputs[0].output.number_of_points
        n_glyph_input_points = g.glyph.glyph.input.number_of_points
        if mask:
            self.assertNotEqual(n_glyph_input_points, 0)
            if mask_random_mode:
                self.assertLessEqual(n_glyph_input_points, n_output_points)
            else:
                on_ratio = g.glyph.mask_points.on_ratio
                self.assertEqual(n_glyph_input_points,
                                 n_output_points / on_ratio)
        else:
            self.assertEqual(n_glyph_input_points, n_output_points)

        v = src.children[0].children[2]
        glyph = v.glyph
        gs = glyph.glyph_source
        self.assertEqual(gs.glyph_position, 'tail')
        self.assertEqual(gs.glyph_source, gs.glyph_list[1])
        self.assertEqual(numpy.allclose(v.implicit_plane.normal,
                                        (0., 1., 0.)), True)

        v = src.children[0].children[3]
        glyph = v.glyph
        gs = glyph.glyph_source
        self.assertEqual(gs.glyph_source, gs.glyph_list[2])
        self.assertEqual(gs.glyph_position, 'head')
        self.assertEqual(numpy.allclose(v.implicit_plane.normal,
                                        (0., 1., 0.)), True)

    def test_glyph(self):
        "Test if the test fixture works"
        self.check()

    @unittest.skipIf(platform.system() == "Darwin", "Test crashes on OSX. See issue #373")
    def test_mask_input_points_with_random_mode(self):
        """Test if masking input points works with random mode.
           Tests Issue #165"""
        s = self.scene
        src = s.children[0]
        g = src.children[0].children[1]
        g.glyph.mask_input_points = True
        self.check(mask=True, mask_random_mode=True)

    def test_mask_input_points_without_random_mode(self):
        """Test if masking input points works without random mode.
           Tests Issue #165"""
        s = self.scene
        src = s.children[0]
        g = src.children[0].children[1]
        g.glyph.mask_points.random_mode = 0
        g.glyph.mask_input_points = True
        self.check(mask=True)

    def test_components_changed(self):
        """"Test if the modules respond correctly when the components
            are changed."""

        g = self.g
        v = self.v
        g.actor = g.actor.__class__()
        glyph = g.glyph
        g.glyph = glyph.__class__()
        g.glyph = glyph

        glyph = v.glyph
        v.glyph = glyph.__class__()
        v.glyph = glyph
        v.actor = v.actor.__class__()
        v.cutter = v.cutter.__class__()
        ip = v.implicit_plane
        v.implicit_plane = ip.__class__()
        v.implicit_plane = ip
        self.check()

    def test_save_and_restore(self):
        """Test if saving a visualization and restoring it works."""
        engine = self.e
        scene = self.scene
        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2')  # We simulate a file.
        engine.save_visualization(f)
        f.seek(0)  # So we can read this saved data.

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
