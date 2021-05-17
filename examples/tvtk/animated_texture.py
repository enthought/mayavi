#!/usr/bin/env python

""" Illustrates texturing on a glyph and also illustrates how easy it
is to change that texture when you treat it as a numpy array.  You can
change the numpy array in-place and have TVTK re-render the scene.
TVTK sees a view of this array without doing any data transfers.

"""
# Authors: Prabhu Ramachandran, Eric Jones
# Copyright (c) 2006-2020, Enthought, Inc.
# License: BSD Style.

from numpy import arange, zeros, uint8, exp, sqrt, pi

from tvtk.api import tvtk
from tvtk.common import configure_input_data, configure_source_data, \
                        is_old_pipeline

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

def image_from_array(ary):
    """ Create a VTK image object that references the data in ary.
        The array is either 2D or 3D with.  The last dimension
        is always the number of channels.  It is only tested
        with 3 (RGB) or 4 (RGBA) channel images.

        Note: This works no matter what the ary type is (accept
        probably complex...).  uint8 gives results that make since
        to me.  Int32 and Float types give colors that I am not
        so sure about.  Need to look into this...
    """

    sz = ary.shape
    dims = len(sz)
    # create the vtk image data
    img = tvtk.ImageData()

    if dims == 2:
        # 1D array of pixels.
        img.whole_extent = (0, sz[0]-1, 0, 0, 0, 0)
        img.dimensions = sz[0], 1, 1
        img.point_data.scalars = ary

    elif dims == 3:
        # 2D array of pixels.
        if is_old_pipeline():
            img.whole_extent = (0, sz[0]-1, 0, sz[1]-1, 0, 0)
        else:
            img.extent = (0, sz[0]-1, 0, sz[1]-1, 0, 0)
        img.dimensions = sz[0], sz[1], 1

        # create a 2d view of the array
        ary_2d = ary[:]
        ary_2d.shape = sz[0]*sz[1],sz[2]
        img.point_data.scalars = ary_2d

    else:
        raise ValueError("ary must be 3 dimensional.")

    return img

sz = (256, 256, 3)
array_3d = zeros(sz, uint8)
img = image_from_array(array_3d)

t = tvtk.Texture(interpolate = 1)
configure_input_data(t, img)
a.texture = t

# Renderwindow stuff and add actor.
rw = tvtk.RenderWindow(size=(600, 600))
ren = tvtk.Renderer(background=(0.1, 0.2, 0.4))
rw.add_renderer(ren)
rwi = tvtk.RenderWindowInteractor(render_window=rw)
ren.add_actor(a)
rwi.initialize()

# create a little wave to slide across the image.
wave = 1/sqrt(2*pi)*exp(-arange(-2, 2, .05)**2/2)*255
# have to use += here because = doesn't respect broadcasting correctly.
array_3d[:len(wave)] += wave.astype(uint8)[:,None,None]

import time
t1 = time.time()
N = 256
for i in range(N):
    array_3d[1:] = array_3d[:-1]
    img.modified()
    rwi.render()
    #print i
t2 = time.time()
print('texture size:', array_3d.shape)
print('fps:', N/(t2-t1))

rwi.start()
