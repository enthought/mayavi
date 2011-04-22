""" A simple model to use for viewing TVTK actors/widgets.
"""

# Authors: Robert Kern <robert.kern [at] gmail.com>
#          Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Dict, Event, HasTraits, Bool

#####################################################################
# `ITVTKActorModel` class
#####################################################################
class ITVTKActorModel(HasTraits):
    """ An interface for view models that can control a TVTK scene's contents.
    """

    # This maintains a dictionary mapping objects (by identity) to lists (or
    # single items) of TVTK Actors or 3D Widgets that represent them in the
    # scene. Adding and removing objects from this dictionary adds and removes
    # them from the scene. This is the trait that will be edited by a
    # ActorEditor.
    actor_map = Dict()

    # Turn off rendering such that multiple adds/removes can be refreshed at
    # once.
    disable_render = Bool(False)

    # Send this event in order to force a rendering of the scene.
    do_render = Event()


