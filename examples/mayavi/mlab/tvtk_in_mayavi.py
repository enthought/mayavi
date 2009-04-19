"""
An example of pure TVTK programming to build TVTK objects, which are then
added to a Mayavi scene.

This example show how pure TVTK objects can be added to a Mayavi scene.

This programming style does not allow to benefit from the data-management
facilities of Mayavi (the pipeline, the data-oriented mlab functions),
but it allows to easily reuse VTK code together with Mayavi or mlab code.
"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from enthought.tvtk.api import tvtk
from enthought.mayavi import mlab

v = mlab.figure()

# Create a first sphere
sphere = tvtk.SphereSource(center=(0, 0, 0), radius=0.5)
sphereMapper = tvtk.PolyDataMapper(input=sphere.output)
p = tvtk.Property(opacity=0.2, color=(1, 0, 0))
sphereActor = tvtk.Actor(mapper=sphereMapper, property=p)
v.scene.add_actor(sphereActor)

# Create a second sphere
sphere2 = tvtk.SphereSource(center=(7, 0, 1), radius=0.2)
sphereMapper2 = tvtk.PolyDataMapper(input=sphere2.output)
p = tvtk.Property(opacity=0.3, color=(1, 0, 0))
sphereActor2 = tvtk.Actor(mapper=sphereMapper2, property=p)
v.scene.add_actor(sphereActor2)

# Create a line between the two spheres
line = tvtk.LineSource(point1=(0, 0, 0), point2=(7, 0, 1))
lineMapper = tvtk.PolyDataMapper(input=line.output)
lineActor = tvtk.Actor(mapper=lineMapper)
v.scene.add_actor(lineActor)

# And display text
vtext = tvtk.VectorText()
vtext.text = 'Mayavi'
textMapper = tvtk.PolyDataMapper(input=vtext.get_output())
p2 = tvtk.Property(color=(0, 0.3, 0.3))
textActor = tvtk.Follower(mapper=textMapper, property=p2)
textActor.position = (0, 0, 0)
v.scene.add_actor(textActor)

# Choose a view angle, and display the figure
mlab.view(85, -17, 15, [ 3.5, -0.3, -0.8])
mlab.show()

