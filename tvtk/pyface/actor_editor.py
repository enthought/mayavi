""" A mostly-general Traits UI editor for viewing things in TVTK scenes.
"""

# Authors: Robert Kern <robert.kern [at] gmail.com>
#          Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Import the toolkit specific version.
from tvtk.pyface.toolkit import toolkit_object
ActorEditor = toolkit_object('actor_editor:ActorEditor')
