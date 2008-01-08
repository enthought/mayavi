#!/usr/bin/env python

"""This script demonstrates how one can script MayaVi, create a new
VTK scene and create a few simple modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# On systems with multiple wx installations installed, pick one that works
# with the libraries Mayavi depends on.
try:
    import wxversion
    wxversion.ensureMinimal('2.6')
except ImportError:
    pass

# Standard library imports
import sys
from os.path import join, dirname

# Enthought library imports
from enthought.mayavi.app import Mayavi


class MyApp(Mayavi):
    def run(self):
        """This is executed once the application GUI has started.
        *Make sure all other MayaVi specific imports are made here!*
        """
        # Various imports to do different things.
        from enthought.mayavi.sources.vtk_file_reader import VTKFileReader
        from enthought.mayavi.filters.threshold import Threshold
        from enthought.mayavi.modules.outline import Outline
        from enthought.mayavi.modules.axes import Axes
        from enthought.mayavi.modules.grid_plane import GridPlane
        from enthought.mayavi.modules.image_plane_widget import ImagePlaneWidget
        from enthought.mayavi.modules.text import Text

        script = self.script
        # Create a new scene.
        script.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(join(dirname(__file__), 'data', 'heart.vtk'))
        script.add_source(r)

        # Put up some text.
        t = Text(text='MayaVi rules!', x_position=0.2,
                 y_position=0.9, width=0.8)
        t.property.color = 1, 1, 0  # Bright yellow, yeah!
        script.add_module(t)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Create an axes for the data.
        a = Axes()
        script.add_module(a)

        # Create an orientation axes for the scene.  This only works with
        # VTK-4.5 and above which is why we have the try block.
        try:
            from enthought.mayavi.modules.orientation_axes import OrientationAxes
        except ImportError:
            pass
        else:
            a = OrientationAxes()
            a.marker.set_viewport(0.0, 0.8, 0.2, 1.0)
            script.add_module(a)

        # Create three simple grid plane modules.
        # First normal to 'x' axis.
        gp = GridPlane()
        script.add_module(gp)
        # Second normal to 'y' axis.
        gp = GridPlane()
        gp.grid_plane.axis = 'y'
        script.add_module(gp)
        # Third normal to 'z' axis.
        gp = GridPlane()
        script.add_module(gp)
        gp.grid_plane.axis = 'z'

        # Create one ImagePlaneWidget.
        ipw = ImagePlaneWidget()
        script.add_module(ipw)
        # Set the position to the middle of the data.
        ipw.ipw.slice_position = 16

    

if __name__ == '__main__':
    a = MyApp()
    a.main()
