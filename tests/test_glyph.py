"""Tests for the Glyph module.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import join, abspath
from StringIO import StringIO
import copy
import numpy

# Enthought library imports.
from enthought.traits.api import TraitError

# Local imports.
from common import TestCase


class TestGlyph(TestCase):
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

    def set_view(self, s):
        """Sets the view correctly."""
        #s.scene.reset_zoom()
        s.scene.z_plus_view()
        c = s.scene.camera
        c.azimuth(-30)
        c.elevation(20)
        s.render()

    def test(self):        
        ############################################################
        # Imports.
        script = self.script
        from enthought.mayavi.sources.array_source import ArraySource
        from enthought.mayavi.modules.outline import Outline
        from enthought.mayavi.modules.glyph import Glyph
        from enthought.mayavi.modules.vector_cut_plane import VectorCutPlane
        
        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        d = ArraySource()
        sc, vec = self.make_data()
        d.scalar_data = sc
        d.vector_data = vec
        d.image_data.origin = (-5, -5, -5)

        script.add_source(d)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)
        # Glyphs for the scalars
        g = Glyph()
        script.add_module(g)
        g.glyph.glyph_source.glyph_position = 'center'
        g.glyph.glyph.vector_mode = 'use_normal'
        g.glyph.glyph.scale_factor = 0.5
        g.actor.property.line_width = 1.0

        v = VectorCutPlane()
        glyph = v.glyph
        gs = glyph.glyph_source
        gs.glyph_position = 'tail'
        gs.glyph_source = gs.glyph_list[1]
        script.add_module(v)
        v.implicit_plane.set(normal=(0, 1, 0), origin=(0, 3, 0))
        
        v = VectorCutPlane()
        glyph = v.glyph
        gs = glyph.glyph_source
        gs.glyph_source = gs.glyph_list[2]
        gs.glyph_position = 'head'
        script.add_module(v)
        v.implicit_plane.set(normal=(0, 1, 0), origin=(0, -2, 0))
        
        # Set the scene to a suitable view.
        self.set_view(s)

        # Now compare the image.
        self.compare_image(s, 'images/test_glyph.png')

        ############################################################
        # Test if the modules respond correctly when the components
        # are changed.
        
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

        s.render()
        # Now compare the image.
        self.compare_image(s, 'images/test_glyph.png')
        s.render()
        

        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = StringIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene
        # Set the scene to a suitable view.
        self.set_view(s)
        # Now compare the image.
        self.compare_image(s, 'images/test_glyph.png')

        ############################################################
        # Test if the MayaVi2 visualization can be deepcopied.

        # Pop the source object.
        sources = s.children
        s.children = []
        # Add it back to see if that works without error.
        s.children.extend(sources)

        self.set_view(s)
        # Now compare the image.
        self.compare_image(s, 'images/test_glyph.png')

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        sources1 = copy.deepcopy(sources)
        s.children[:] = sources

        self.set_view(s)
        self.compare_image(s, 'images/test_glyph.png')
        
        # If we have come this far, we are golden!
        

if __name__ == "__main__":
    t = TestGlyph()
    t.run()
