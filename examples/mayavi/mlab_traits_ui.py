#!/usr/bin/env python
"""An example of how to use mayavi.mlab inside a traits UI view.
"""

# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
#          Gael Varoquaux 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard imports.
from numpy import sqrt, sin, mgrid

# Enthought imports.
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.tvtk.pyface.scene_editor import SceneEditor 

from enthought.mayavi import mlab
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel
from enthought.mayavi.core.ui.mayavi_scene import MayaviScene

# Set mlab to use the simple backend instead of envisage.
mlab.options.backend = 'simple'

######################################################################
class ActorViewer(HasTraits):

    # The scene model.
    scene = Instance(MlabSceneModel, ())

    ######################
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
