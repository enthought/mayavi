#!/usr/bin/env python

""" Illustrates the Glyph3D class and some basic texturing of the
glyph.  Notice how easy it is to create a simple PolyData object as
the input of the Glyph using Python lists.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

from tvtk.api import tvtk
from tvtk.common import is_old_pipeline, configure_input_data, configure_source_data

# Source for glyph.  Note that you need to pick a source that has
# texture co-ords already set.  If not you'll have to generate them.
# This is easily done -- its just a 2d array of (u,v) coords each
# between [0, 1] that you can set via something like
# point_data.t_coords = <array>.
#
# In this case CubeSource already defines texture coords for us (as of
# VTK-4.4).
cs = tvtk.CubeSource(x_length=2, y_length=1.0, z_length=0.5)

# Create input for the glyph -- the sources are placed at these input
# points.
pts = [[1,1,1],[0,0,0], [-1,-1,-1]]
pd = tvtk.PolyData(points=pts, polys=[[0],[1],[2]])
# Orientation/scaling is as per the vector attribute.
vecs = [[1,0,0], [0,1,0], [0,0,1]]
pd.point_data.vectors = vecs

# Create the glyph3d and set up the pipeline.
g = tvtk.Glyph3D(scale_mode='data_scaling_off', vector_mode = 'use_vector')
configure_input_data(g, pd)

# Note that VTK's vtkGlyph.SetSource is special because it has two
# call signatures: SetSource(src) and SetSource(int N, src) (which
# sets the N'th source).  In tvtk it is represented as both a property
# and as a method.  Using the `source` property will work fine if all
# you want is the first `source`.  OTOH if you want the N'th `source`
# use get_source(N).
# g.source = cs.output
configure_source_data(g, cs.output)
cs.update()
g.update()

m = tvtk.PolyDataMapper()
configure_input_data(m, g.output)
a = tvtk.Actor(mapper=m)

# Read the texture from image and set the texture on the actor.  If
# you don't like this image, replace with your favorite -- any image
# will do (you must use a suitable reader though).
img = tvtk.JPEGReader(file_name='images/masonry.jpg')
t = tvtk.Texture(interpolate = 1)
if is_old_pipeline():
    t.input = img.output
else:
    t.input_connection = img.output_port
a.texture = t

# Renderwindow stuff and add actor.
rw = tvtk.RenderWindow(size=(600, 600))
ren = tvtk.Renderer(background=(0.5, 0.5, 0.5))
rw.add_renderer(ren)
rwi = tvtk.RenderWindowInteractor(render_window=rw)
ren.add_actor(a)
rwi.initialize()
rwi.start()
