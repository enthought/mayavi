#!/usr/bin/env python
"""
This script demonstrates how one can use the Mayavi application framework
without displaying Mayavi's UI.

Note: look at the end of this file to see how the non gui plugin is
chosen instead of the default gui mayavi plugin.

This should be run as::

  $ python nongui.py

Or::

  $ mayavi2 script.py

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join, abspath

# Enthought library imports
from mayavi.scripts.util import get_data_dir
from mayavi.plugins.app import Mayavi, get_non_gui_plugins

class MyApp(Mayavi):
    def run(self):
        """This is executed once the application GUI has started.
        *Make sure all other MayaVi specific imports are made here!*
        """

        # Various imports to do different things.
        from mayavi.sources.vtk_file_reader import VTKFileReader
        from mayavi.modules.outline import Outline
        from mayavi.modules.axes import Axes
        from mayavi.modules.grid_plane import GridPlane
        from mayavi.modules.image_plane_widget import ImagePlaneWidget
        from mayavi.modules.text import Text
        from mayavi.modules.contour_grid_plane import ContourGridPlane
        from mayavi.modules.iso_surface import IsoSurface

        script = self.script

        # Create a new scene.
        script.new_scene()

        # Read a VTK (old style) data file.
        r = VTKFileReader()
        r.initialize(join(get_data_dir(abspath(__file__)),
                          'heart.vtk'))
        script.add_source(r)

        # Put up some text.
        t = Text(text='MayaVi rules!', x_position=0.2, y_position=0.9, width=0.8)
        t.property.color = 1, 1, 0  # Bright yellow, yeah!
        script.add_module(t)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)

        # Create an axes for the data.
        a = Axes()
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

        # Create one ContourGridPlane normal to the 'x' axis.
        cgp = ContourGridPlane()
        script.add_module(cgp)
        # Set the position to the middle of the data.
        cgp.grid_plane.axis = 'y'
        cgp.grid_plane.position = 15

        # An isosurface module.
        iso = IsoSurface(compute_normals=True)
        script.add_module(iso)
        iso.contour.contours = [200.0]

        # Set the view.
        s = script.engine.current_scene
        cam = s.scene.camera
        cam.azimuth(45)
        cam.elevation(15)
        s.render()


if __name__ == '__main__':
    m = MyApp()
    # Get the default non GUI plugins.
    plugins = get_non_gui_plugins()
    # Start the app with these plugins.
    m.main(plugins=plugins)
