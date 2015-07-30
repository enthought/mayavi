"""`MlabSceneModel` makes it easy to plug `mayavi.mlab` in traits UI views.
"""
# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from traits.api import Instance, Property
from tvtk.pyface.scene_model import SceneModel
from mayavi.core.engine import Engine
from mayavi.core.scene import Scene
from mayavi import mlab as m2_mlab


######################################################################
# `MlabSceneModel` class
######################################################################
class MlabSceneModel(SceneModel):
    """ An container for an mlab model, that can be exposed using a Mayavi
        scene in a TraitsUI view.
    """

    # The mayavi engine.
    engine = Instance(Engine)

    # The mlab instance.
    mlab = Property()

    # A reference to the mayavi scene object
    mayavi_scene = Instance(Scene)

    def __init__(self, parent=None, **traits):
        super(MlabSceneModel, self).__init__(parent, **traits)
        # Store the current mlab figure:
        current_figure = self.engine.current_scene
        # register ourselves with the engine.
        self.engine.new_scene(self)
        # XXX: This is not thread-safe
        self.mayavi_scene = self.engine.current_scene
        # Restore the current figure. We do this, because MlabSceneModel
        # can be created lazy by Traits, on access. Having side effects
        # thus renders the code quite unpredictable
        self.engine.current_scene = current_figure

    ###################################################################
    # Private API.
    ###################################################################
    def _engine_default(self):
        return m2_mlab.get_engine()

    def _get_mlab(self):
        return m2_mlab
