#!/usr/bin/env python

"""A simple example demonstrating how one can use numpy arrays
transparently with TVTK.

"""

# Author: Prabhu Ramachandran and Eric Jones
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

from tvtk.api import tvtk
from tvtk.common import configure_input_data
from numpy import array

### DATA
data = array([[0,0,0,10],
              [1,0,0,20],
              [0,1,0,20],
              [0,0,1,30]], 'f')

triangles = array([[0,1,3],
                   [0,3,2],
                   [1,2,3],
                   [0,2,1]])

points = data[:,:3]
temperature = data[:,-1]

### TVTK PIPELINE
# create a renderer
renderer = tvtk.Renderer()

# create a render window and hand it the renderer
render_window = tvtk.RenderWindow(size=(400,400))
render_window.add_renderer(renderer)

# create interactor and hand it the render window
# This handles mouse interaction with window.
interactor = tvtk.RenderWindowInteractor(render_window=render_window)

# Create a mesh from the data created above.
mesh = tvtk.PolyData(points=points, polys=triangles)
mesh.point_data.scalars = temperature

# Set the mapper to scale temperature range
# across the entire range of colors
mapper = tvtk.PolyDataMapper()
configure_input_data(mapper, mesh)
mapper.scalar_range = min(temperature), max(temperature)

# Create mesh actor for display
actor = tvtk.Actor(mapper=mapper)

# Create a scalar bar
scalar_bar = tvtk.ScalarBarActor(title="Temperature",
                                 orientation='horizontal',
                                 width=0.8, height=0.17,
                                 lookup_table = mapper.lookup_table)
scalar_bar.position_coordinate.coordinate_system = 'normalized_viewport'
scalar_bar.position_coordinate.value = 0.1, 0.01, 0.0

# Use the ScalarBarWidget so we can drag the scalar bar around.
sc_bar_widget = tvtk.ScalarBarWidget(interactor=interactor,
                                     scalar_bar_actor=scalar_bar)

# Now add the actors to the renderer and start the interaction.
renderer.add_actor(actor)
interactor.initialize()
# Enable the widget so the scalar bar can be seen.  Press 'i' to
# disable the widget.
sc_bar_widget.enabled = True
interactor.start()
