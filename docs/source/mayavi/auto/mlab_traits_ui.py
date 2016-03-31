#!/usr/bin/env python
"""A simple example of how to use mayavi.mlab inside a traits UI dialog.

This example uses traitsUI (
`traitsUI <http://docs.enthought.com/traitsui/>`_ ) to create a
the simplest possible dialog: a single Mayavi scene in a window.
"""

# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
#          Gael Varoquaux
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard imports.
from numpy import sqrt, sin, mgrid

# Enthought imports.
from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from tvtk.pyface.scene_editor import SceneEditor

from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene


######################################################################
class ActorViewer(HasTraits):

    # The scene model.
    scene = Instance(MlabSceneModel, ())

    ######################
    # Using 'scene_class=MayaviScene' adds a Mayavi icon to the toolbar,
    # to pop up a dialog editing the pipeline.
    view = View(Item(name='scene',
                     editor=SceneEditor(scene_class=MayaviScene),
                     show_label=False,
                     resizable=True,
                     height=500,
                     width=500),
                resizable=True
                )

    def __init__(self, **traits):
        HasTraits.__init__(self, **traits)
        self.generate_data()

    def generate_data(self):
        # Create some data
        X, Y = mgrid[-2:2:100j, -2:2:100j]
        R = 10*sqrt(X**2 + Y**2)
        Z = sin(R)/R

        self.scene.mlab.surf(X, Y, Z, colormap='gist_earth')


if __name__ == '__main__':
    a = ActorViewer()
    a.configure_traits()
