#!/usr/bin/env python
"""A simple example demonstrating TVTK.  This example is basically a
translation of the VTK tutorial demo available in
VTK/Examples/Tutorial/Step6/Python/Cone6.py.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

from tvtk.api import tvtk
from tvtk.common import configure_input_data

# Create a cone source and configure it.
cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)

# Print the traits of the cone.
#cs.print_traits()

# Setup the rest of the pipeline.
m = tvtk.PolyDataMapper()

# Note that VTK's GetOutput method is special because it has two call
# signatures: GetOutput() and GetOutput(int N) (which gets the N'th
# output).  In tvtk it is represented as both a property and as a
# method.  Using the output property will work fine if all you want is
# the default output.  OTOH if you want the N'th output use
# get_output(N).
# m.input = cs.output # or m.input = cs.get_output()
configure_input_data(m, cs.output)
cs.update()

# Create the actor and set its mapper.
a = tvtk.Actor(mapper=m)

# Create a Renderer, add the actor and set its background color.
ren = tvtk.Renderer(background=(0.1, 0.2, 0.4))
ren.add_actor(a)

# Create a RenderWindow, add the renderer and set its size.
rw = tvtk.RenderWindow(size=(300,300))
rw.add_renderer(ren)

# Create the RenderWindowInteractor
rwi = tvtk.RenderWindowInteractor(render_window=rw)

# Setup a box widget.
bw = tvtk.BoxWidget(interactor=rwi, place_factor=1.25,
                    prop3d=a)
bw.place_widget()

def callback(widget, event):
    """This callback sets the transformation of the cone using that
    setup by the the box."""
    t = tvtk.Transform()
    bw.get_transform(t)
    bw.prop3d.user_transform = t

# Add an observer
bw.add_observer("InteractionEvent", callback)

# Turn on the box interaction.  The default is off and can be toggled
# by pressing 'i' on the RenderWindowInteractor.
bw.on()

# Start the VTK event loop.
rwi.initialize()
rwi.start()
