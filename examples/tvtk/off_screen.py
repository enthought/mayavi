#!/usr/bin/env python
""" A simple example demonstrating TVTK for rendering to an off screen
    buffer.  This is useful when you are rendering images to files
    and do not wish to display a graphics window at all.

    Note: Tested to work on win32, Mac OS X and Linux.  Mac OS X and
    Linux require a VTK version released after Oct. 2005 (and ideally
    after March 2006).
"""
# Author: Eric Jones, Prabhu Ramachandran
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

# Create the actor and set its mapper.
a = tvtk.Actor(mapper=m)
cs.update()

# Create a Renderer, add the actor and set its background color.
ren = tvtk.Renderer(background=(0.1, 0.2, 0.4))
ren.add_actor(a)
ren.reset_camera()

# Create a RenderWindow, add the renderer and set its size.
rw = tvtk.RenderWindow(size=(300,300))
rw.off_screen_rendering=1
rw.add_renderer(ren)

w2if = tvtk.WindowToImageFilter()
w2if.magnification = 2
w2if.input = rw
ex = tvtk.PNGWriter()
ex.file_name = "example.png"
configure_input_data(ex, w2if.output)
w2if.update()
ex.write()
