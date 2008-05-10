"""`MlabSceneModel` makes it easy to plug `mayavi.mlab` in traits UI views.
"""
# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from enthought.traits.api import Instance, Property
from enthought.pyface.tvtk.scene_model import SceneModel
from enthought.mayavi.core.engine import Engine
from enthought.mayavi import mlab as m2_mlab

######################################################################
# `MlabSceneModel` class
######################################################################
class MlabSceneModel(SceneModel):

    # The mayavi engine.
    engine = Instance(Engine)

    # The mlab instance.
    mlab = Property

    def __init__(self, parent=None, **traits):
        super(MlabSceneModel, self).__init__(parent, **traits)
        # register ourselves with the engine.
        self.engine.new_scene(self)

    ###################################################################
    # Private API.
    ###################################################################
    def _engine_default(self):
        return m2_mlab.get_engine()

    def _get_mlab(self):
        return m2_mlab

