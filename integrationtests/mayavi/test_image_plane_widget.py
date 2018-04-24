"""Tests for the ImagePlaneWidget module.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy

# Enthought library imports.
from traits.api import TraitError
from pyface.api import GUI

# Local imports.
from common import TestCase


class TestImagePlaneWidget(TestCase):
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

    def set_view(self, s):
        """Sets the view correctly."""
        #s.scene.reset_zoom()
        s.scene.z_plus_view()
        c = s.scene.camera
        c.azimuth(30)
        c.elevation(30)
        s.render()
        GUI.process_events()

    def check(self):
        script = self.script
        src = script.engine.current_scene.children[0]
        i1, i2, i3 = src.children[0].children[1:]
        assert i1.ipw.plane_orientation == 'x_axes'
        assert numpy.allclose(i1.ipw.center, (0, 31.5, 31.5))
        rng = i1.ipw.reslice_output.point_data.scalars.range
        assert numpy.allclose(rng, (-0.2, 1.0), atol=0.1)
        assert i2.ipw.plane_orientation == 'y_axes'
        assert numpy.allclose(i2.ipw.center, (31.5, 0, 31.5))
        rng = i2.ipw.reslice_output.point_data.scalars.range
        assert numpy.allclose(rng, (-0.2, 1.0), atol=0.1)
        assert i3.ipw.plane_orientation == 'z_axes'
        assert numpy.allclose(i3.ipw.center, (31.5, 31.5, 0))
        rng = i3.ipw.reslice_output.point_data.scalars.range
        assert numpy.allclose(rng, (-0.2, 1.0), atol=0.1)

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.array_source import ArraySource
        from mayavi.modules.outline import Outline
        from mayavi.modules.image_plane_widget import ImagePlaneWidget

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        d = ArraySource()
        sc = self.make_data()
        d.scalar_data = sc

        script.add_source(d)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)
        # ImagePlaneWidgets for the scalars
        ipw = ImagePlaneWidget()
        script.add_module(ipw)

        ipw_y = ImagePlaneWidget()
        script.add_module(ipw_y)
        ipw_y.ipw.plane_orientation = 'y_axes'

        ipw_z = ImagePlaneWidget()
        script.add_module(ipw_z)
        ipw_z.ipw.plane_orientation = 'z_axes'

        # Set the scene to a suitable view.
        self.set_view(s)

        self.check()

        ############################################################
        # Test if saving a visualization and restoring it works.

        # Save visualization.
        f = BytesIO()
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

        GUI.process_events()
        self.check()

        ############################################################
        # Test if the MayaVi2 visualization can be deepcopied.

        # Pop the source object.
        sources = s.children
        s.children = []
        # Add it back to see if that works without error.
        s.children.extend(sources)

        self.set_view(s)

        GUI.process_events()
        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        sources1 = copy.deepcopy(sources)
        s.children[:] = sources

        self.set_view(s)

        GUI.process_events()
        self.check()

        # If we have come this far, we are golden!


if __name__ == "__main__":
    t = TestImagePlaneWidget()
    t.test()
