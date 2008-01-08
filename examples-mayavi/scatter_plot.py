# This script creates a bunch of random points with random scalar data
# and then shows these as a "scatter" plot of points.  The script
# illustrates (a) how to create a dataset easily using tvtk and numpy,
# (b) use a created dataset in mayavi2 and visualize it.
# Run this script like so::
#   $ mayavi2 -x scatter_plot.py
#
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007 Prabhu Ramachandran.
# License: BSD Style.

# Create some random points to view.
from enthought.tvtk.api import tvtk
import numpy

# The following *optional* two lines allow a user to call this script
# as either `python script.py` or `mayavi2 script.py`.  These two
# lines must be placed before any other mayavi imports.
from enthought.mayavi.scripts import mayavi2
mayavi2.standalone(globals())

pd = tvtk.PolyData()
pd.points = numpy.random.random((1000, 3))
verts = numpy.arange(0, 1000, 1)
verts.shape = (1000, 1)
pd.verts = verts
pd.point_data.scalars = numpy.random.random(1000)
pd.point_data.scalars.name = 'scalars'

# Now visualize it using mayavi2.
from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.modules.surface import Surface

mayavi.new_scene()
d = VTKDataSource()
d.data = pd
mayavi.add_source(d)
mayavi.add_module(Outline())
s = Surface()
mayavi.add_module(s)
s.actor.property.set(representation = 'p', point_size = 2)
# You could also use glyphs to render the points via the Glyph module.
