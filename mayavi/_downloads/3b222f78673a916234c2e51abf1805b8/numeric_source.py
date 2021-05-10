#!/usr/bin/env python

"""This script demonstrates how to create a numpy array data and
visualize it as image data using a few modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports
import numpy

# Enthought library imports
from mayavi.scripts import mayavi2
from mayavi.sources.array_source import ArraySource
from mayavi.modules.outline import Outline
from mayavi.modules.image_plane_widget import ImagePlaneWidget


def make_data(dims=(128, 128, 128)):
    """Creates some simple array data of the given dimensions to test
    with."""
    np = dims[0]*dims[1]*dims[2]

    # Create some scalars to render.
    x, y, z = numpy.ogrid[-5:5:dims[0]*1j,-5:5:dims[1]*1j,-5:5:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    scalars = (numpy.sin(x*y*z)/(x*y*z))
    # The copy makes the data contiguous and the transpose makes it
    # suitable for display via tvtk.  Please note that we assume here
    # that the ArraySource is configured to not transpose the data.
    s = numpy.transpose(scalars).copy()
    # Reshaping the array is needed since the transpose messes up the
    # dimensions of the data.  The scalars themselves are ravel'd and
    # used internally by VTK so the dimension does not matter for the
    # scalars.
    s.shape = s.shape[::-1]

    return s


@mayavi2.standalone
def view_numpy():
    """Example showing how to view a 3D numpy array in mayavi2.
    """
    # 'mayavi' is always defined on the interpreter.
    mayavi.new_scene()
    # Make the data and add it to the pipeline.
    data = make_data()
    src = ArraySource(transpose_input_array=False)
    src.scalar_data = data
    mayavi.add_source(src)
    # Visualize the data.
    o = Outline()
    mayavi.add_module(o)
    ipw = ImagePlaneWidget()
    mayavi.add_module(ipw)
    ipw.module_manager.scalar_lut_manager.show_scalar_bar = True

    ipw_y = ImagePlaneWidget()
    mayavi.add_module(ipw_y)
    ipw_y.ipw.plane_orientation = 'y_axes'


if __name__ == '__main__':
    view_numpy()

