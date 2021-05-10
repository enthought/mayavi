"""
An example of plotting scatter points with Mayavi's core API.

This script creates a bunch of random points with random scalar data
and then shows these as a "scatter" plot of points.  The script
illustrates how to

 1. create a dataset easily using tvtk and numpy,

 2. use a created dataset in Mayavi and visualize it.

This example achieve the same functionnality as mlab's points3d
function ( :func:`mayavi.mlab.points3d`), but explicitly
creating the objects and adding them to the pipeline engine via the Mayavi
core API. Compared to using mlab, this method has the advantage of giving
more control on which objects are created, and there life cycle.

Run this script like so::

  $ mayavi2 -x scatter_plot.py

Alternatively it can be run as::

  $ python scatter_plot.py
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007 Prabhu Ramachandran.
# License: BSD Style.

import numpy as np
from tvtk.api import tvtk
from mayavi.scripts import mayavi2


@mayavi2.standalone
def main():
    # Create some random points to view.
    pd = tvtk.PolyData()
    pd.points = np.random.random((1000, 3))
    verts = np.arange(0, 1000, 1)
    verts.shape = (1000, 1)
    pd.verts = verts
    pd.point_data.scalars = np.random.random(1000)
    pd.point_data.scalars.name = 'scalars'

    # Now visualize it using mayavi2.
    from mayavi.sources.vtk_data_source import VTKDataSource
    from mayavi.modules.outline import Outline
    from mayavi.modules.surface import Surface

    mayavi.new_scene()
    d = VTKDataSource()
    d.data = pd
    mayavi.add_source(d)
    mayavi.add_module(Outline())
    s = Surface()
    mayavi.add_module(s)
    s.actor.property.trait_set(representation='p', point_size=2)
    # You could also use glyphs to render the points via the Glyph module.

if __name__ == '__main__':
    main()
