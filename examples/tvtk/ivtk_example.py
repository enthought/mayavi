#!/usr/bin/env python

"""A simple demonstration of how one can use the ivtk module with
PyFace to create a standalone VTK window with an embedded TVTK
pipeline browser and a Python shell!

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# We use this just for the demo.
import random

# The GUI class lets us start a PyFace GUI.
from pyface.api import GUI
from traits.api import HasTraits, Tuple

# The IVTK module.
from tvtk.tools import ivtk

# The actors module has a few helper functions that allow one to
# create simple shapes easily.  These functions return TVTK Actor
# instances.  We use it here for convenience.
from tvtk.pyface import actors

# Create a GUI instance.
gui = GUI()

# Create and open an IVTK application window that has an embedded TVTK
# pipeline browser and an interactive Python interpreter shell via
# PyCrust.  If you don't want all these you can choose between the
# following classes in ivtk -- IVTK, IVTKWithCrust, IVTKWithBrowser
# and IVTKWithCrustAndBrowser.
window = ivtk.IVTKWithCrustAndBrowser(size=(800,600))  # Size is optional.

# Open the window.
window.open()

class EarthActor(HasTraits):
    position = Tuple
    def __init__(self):
        earth = actors.earth_actor()
        earth.property.color = actors.colors.green
        sphere = actors.sphere_actor(color=actors.colors.blue, opacity=0.65)
        self.earth, self.sphere = earth, sphere

    def _position_changed(self, val):
        for actor in (self.earth, self.sphere):
            actor.position = val


# Now create your TVTK actors.  Here we simply use the actors module
# and generate actors randomly.

# Get all the functions in the actors module that end with '_actors'.
ACTORS = [getattr(actors, x) for x in dir(actors)
        if x.endswith('_actor') and not x.startswith('earth')]
ACTORS.append(EarthActor)

# Now create the actors with these functions.
for i in range(len(ACTORS)):
    # Create the actor.
    func = random.choice(ACTORS)
    actor = func()

    # Set its position randomly.
    x = random.uniform(-3, 3)
    y = random.uniform(-3, 3)
    z = random.uniform(-3, 3)
    actor.position = x, y, z

    # Add the actor to the scene.
    if isinstance(actor, EarthActor):
        window.scene.add_actors((actor.earth, actor.sphere))
    else:
        window.scene.add_actor(actor)

# Now reset the view so all the actors.
window.scene.reset_zoom()

# Start the GUI event loop!
gui.start_event_loop()
