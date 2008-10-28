"""
This is an example of doing pure tvtk programming to build the objects,
and adding them to a mayavi scene.

This programming style does not allow to benefit from the data-management
facilities of Mayavi (the pipeline, the data-oriented mlab functions),
but it allows to easily reuse vtk code.
"""

from enthought.tvtk.api import tvtk
from enthought.mayavi import mlab

v = mlab.figure()

sphere = tvtk.SphereSource(center=(0,0,0), radius=0.5)
sphereMapper = tvtk.PolyDataMapper(input=sphere.output)
p = tvtk.Property(opacity=0.2, color=(1,0,0))
sphereActor = tvtk.Actor(mapper=sphereMapper, property=p)
v.scene.add_actor(sphereActor)

sphere2 = tvtk.SphereSource(center=(1,1,1), radius=0.2)
sphereMapper2 = tvtk.PolyDataMapper(input=sphere2.output)
p = tvtk.Property(opacity=0.3, color=(1,0,0))
sphereActor2 = tvtk.Actor(mapper=sphereMapper2, property=p)
v.scene.add_actor(sphereActor2)

line = tvtk.LineSource(point1=(0,0,0), point2=(1,1,1))
lineMapper = tvtk.PolyDataMapper(input=line.output)
lineActor = tvtk.Actor(mapper=lineMapper)
v.scene.add_actor(lineActor)

vtext = tvtk.VectorText()
vtext.text = 'Simone'
textMapper = tvtk.PolyDataMapper(input=vtext.get_output())
p2 = tvtk.Property(color=(1,1,1))
textActor = tvtk.Follower(mapper=textMapper, property=p2)
textActor.position = (0,0,0)
v.scene.add_actor(textActor)

mlab.show()
