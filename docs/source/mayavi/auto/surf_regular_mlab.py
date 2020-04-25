#!/usr/bin/env python
"""Shows how to view data created by `tvtk.tools.mlab` with
mayavi2.
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006-2020, Enthought Inc.
# License: BSD Style.

import numpy

from mayavi.scripts import mayavi2
from tvtk.tools import mlab
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.filters.warp_scalar import WarpScalar
from mayavi.modules.outline import Outline
from mayavi.modules.surface import Surface


def make_data():
    """Make some test numpy data and create a TVTK data object from it
    that we will visualize.
    """
    def f(x, y):
        """Some test function.
        """
        return numpy.sin(x*y)/(x*y)

    x = numpy.arange(-7., 7.05, 0.1)
    y = numpy.arange(-5., 5.05, 0.05)
    s = mlab.SurfRegular(x, y, f)
    return s.data

def add_data(tvtk_data):
    """Add a TVTK data object `tvtk_data` to the mayavi pipleine.
    """
    d = VTKDataSource()
    d.data = tvtk_data
    mayavi.add_source(d)

def surf_regular():
    """Now visualize the data as done in mlab.
    """
    w = WarpScalar()
    mayavi.add_filter(w)
    o = Outline()
    s = Surface()
    mayavi.add_module(o)
    mayavi.add_module(s)

@mayavi2.standalone
def main():
    mayavi.new_scene()
    d = make_data()
    add_data(d)
    surf_regular()

if __name__ == '__main__':
    main()
