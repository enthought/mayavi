"""`MlabSceneModel` makes it easy to plug `mayavi.mlab` in traits UI views.
"""
# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

import functools

from enthought.traits.api import Instance
from enthought.tvtk.pyface.scene_model import SceneModel
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.core.scene import Scene
from enthought.mayavi import mlab as m2_mlab

######################################################################
# `MlabProxy` class
######################################################################
class MlabProxy(object):
    """ A descriptor to implement getters for mlab functions setting the 
        figure.
    """
    def __init__(self, parent):
        self._mlab_proxy_parent = parent


    def __getattr__(self, attr):
        if attr == '_mlab_proxy_parent':
            return object.__getattr__(self, attr)
        # XXX: This is not thread-safe
        f = getattr(m2_mlab, attr)
        if not callable(f):
            return f

        @functools.wraps(f)
        def my_f(*args, **kwargs):
            current_figure = m2_mlab.gcf()
            m2_mlab.figure(self._mlab_proxy_parent.mayavi_scene)
            output = f(*args, **kwargs)
            m2_mlab.figure(current_figure)
            return output

        return my_f


    def __setattr__(self, attr, value):
        if attr == '_mlab_proxy_parent':
            return object.__setattr__(self, attr, value)
        return setattr(m2_mlab, attr, value)


    def __delattr__(self, attr):
        if attr == '_mlab_proxy_parent':
            return object.__delattr__(self, attr)
        return delattr(m2_mlab, attr)


######################################################################
# `MlabSceneModel` class
######################################################################
class MlabSceneModel(SceneModel):

    # The mayavi engine.
    engine = Instance(Engine)

    # The mlab instance.
    mlab = Instance(MlabProxy)

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

    def _mlab_default(self):
        return MlabProxy(self)


