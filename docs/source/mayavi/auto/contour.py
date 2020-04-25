#!/usr/bin/env python
"""
This script demonstrates how one can script Mayavi and use its
contour related modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join, abspath, dirname

# Enthought library imports
from mayavi.scripts import mayavi2
from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.modules.outline import Outline
from mayavi.modules.grid_plane import GridPlane
from mayavi.modules.contour_grid_plane import ContourGridPlane
from mayavi.modules.iso_surface import IsoSurface
from mayavi.modules.scalar_cut_plane import ScalarCutPlane

@mayavi2.standalone
def contour():
    """The script itself.  We needn't have defined a function but
    having a function makes this more reusable.
    """
    # 'mayavi' is always defined on the interpreter.
    # Create a new scene.
    mayavi.new_scene()

    # Read a VTK (old style) data file.
    r = VTKFileReader()
    filename = join(mayavi2.get_data_dir(dirname(abspath(__file__))),
                    'heart.vtk')
    r.initialize(filename)
    mayavi.add_source(r)

    # Create an outline for the data.
    o = Outline()
    mayavi.add_module(o)

    # Create three simple grid plane modules.
    # First normal to 'x' axis.
    gp = GridPlane()
    mayavi.add_module(gp)
    # Second normal to 'y' axis.
    gp = GridPlane()
    mayavi.add_module(gp)
    gp.grid_plane.axis = 'y'
    # Third normal to 'z' axis.
    gp = GridPlane()
    mayavi.add_module(gp)
    gp.grid_plane.axis = 'z'

    # Create one ContourGridPlane normal to the 'x' axis.
    cgp = ContourGridPlane()
    mayavi.add_module(cgp)
    # Set the position to the middle of the data.
    cgp.grid_plane.position = 15

    # Another with filled contours normal to 'y' axis.
    cgp = ContourGridPlane()
    mayavi.add_module(cgp)
    # Set the axis and position to the middle of the data.
    cgp.grid_plane.axis = 'y'
    cgp.grid_plane.position = 15
    cgp.contour.filled_contours = True

    # An isosurface module.
    iso = IsoSurface(compute_normals=True)
    mayavi.add_module(iso)
    iso.contour.contours = [220.0]

    # An interactive scalar cut plane.
    cp = ScalarCutPlane()
    mayavi.add_module(cp)
    cp.implicit_plane.normal = 0,0,1


if __name__ == '__main__':
    contour()
