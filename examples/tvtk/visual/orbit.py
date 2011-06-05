#!/usr/bin/env python
"""A simple example demonstrating the creation of actors and animating
the in a scene using visual modeule."""
# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

from math import sqrt

from tvtk.tools.visual import sphere, iterate, show, vector, curve

#Creating the actors for the scene
giant = sphere(pos=(-1.0e11, 0, 0),
               radius=2e10,
               color=(1, 0, 0),
               mass=2e30)

dwarf = sphere(pos=(1.5e11, 0, 0),
               radius=1e10,
               color=(1, 1, 0),
               mass=1e30)

giant.p = vector(0, 0, -1e4) * giant.mass
dwarf.p = -1*giant.p

# creating the curve which will trace the paths of actors
for a in [giant, dwarf]:
    a.orbit = curve(radius=2e9, color=a.color)

dt = 86400

def anim():
    #Creating the animation function which will be called at
    #uniform timeperiod through the iterate function
    dist = dwarf.pos - giant.pos
    force = 6.7e-11 * giant.mass * dwarf.mass * \
        dist/(sqrt(dist[0]**2 + dist[1]**2 + dist[2]**2))**3
    giant.p = giant.p + force*dt
    dwarf.p = dwarf.p - force*dt

    for a in [giant, dwarf]:
        a.pos = a.pos + (a.p/a.mass)*dt
        a.orbit.append(a.pos)
        p = a.orbit.points
        if len(p) > 1000:
            a.orbit.points = p[200:]

a = iterate(50, anim)
a.edit_traits()
show()
