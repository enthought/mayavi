"""
This example displays the trajectories for the Lorenz system of
equations using mlab along with the z-nullcline.  It provides a simple
UI where a user can change the parameters and the system of equations on
the fly.  This primarily demonstrates how one can build powerful tools
with a UI using Traits and Mayavi.

For explanations and more examples of interactive application building
with Mayavi, please refer to section :ref:`builing_applications`.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Enthought, Inc.
# License: BSD Style.

import numpy as np
import scipy

from traits.api import HasTraits, Range, Instance, \
        on_trait_change, Array, Tuple, Str
from traitsui.api import View, Item, HSplit, Group

from mayavi import mlab
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, \
    SceneEditor

################################################################################
# `Lorenz` class.
################################################################################
class Lorenz(HasTraits):

    # The parameters for the Lorenz system, defaults to the standard ones.
    s = Range(0.0, 20.0, 10.0, desc='the parameter s', enter_set=True,
              auto_set=False)
    r = Range(0.0, 50.0, 28.0, desc='the parameter r', enter_set=True,
              auto_set=False)
    b = Range(0.0, 10.0, 8./3., desc='the parameter b', enter_set=True,
              auto_set=False)

    # These expressions are evaluated to compute the right hand sides of
    # the ODE.  Defaults to the Lorenz system.
    u = Str('s*(y-x)', desc='the x component of the velocity',
            auto_set=False, enter_set=True)
    v = Str('r*x - y - x*z', desc='the y component of the velocity',
            auto_set=False, enter_set=True)
    w = Str('x*y - b*z', desc='the z component of the velocity',
            auto_set=False, enter_set=True)

    # Tuple of x, y, z arrays where the field is sampled.
    points = Tuple(Array, Array, Array)

    # The mayavi(mlab) scene.
    scene = Instance(MlabSceneModel, args=())

    # The "flow" which is a Mayavi streamline module.
    flow = Instance(HasTraits)

    ########################################
    # The UI view to show the user.
    view = View(HSplit(
                    Group(
                        Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                             height=500, width=500, show_label=False)),
                    Group(
                        Item('s'),
                        Item('r'),
                        Item('b'),
                        Item('u'), Item('v'), Item('w')),
                    ),
                resizable=True
                )

    ######################################################################
    # Trait handlers.
    ######################################################################

    # Note that in the `on_trait_change` call below we listen for the
    # `scene.activated` trait.  This conveniently ensures that the flow
    # is generated as soon as the mlab `scene` is activated (which
    # happens when the configure/edit_traits method is called).  This
    # eliminates the need to manually call the `update_flow` method etc.
    @on_trait_change('s, r, b, scene.activated')
    def update_flow(self):
        x, y, z = self.points
        u, v, w = self.get_uvw()
        self.flow.mlab_source.trait_set(u=u, v=v, w=w)

    @on_trait_change('u')
    def update_u(self):
        self.flow.mlab_source.trait_set(u=self.get_vel('u'))

    @on_trait_change('v')
    def update_v(self):
        self.flow.mlab_source.trait_set(v=self.get_vel('v'))

    @on_trait_change('w')
    def update_w(self):
        self.flow.mlab_source.trait_set(w=self.get_vel('w'))

    def get_uvw(self):
        return self.get_vel('u'), self.get_vel('v'), self.get_vel('w')

    def get_vel(self, comp):
        """This function basically evaluates the user specified system
        of equations using scipy.
        """
        func_str = getattr(self, comp)
        try:
            g = scipy.__dict__
            x, y, z = self.points
            s, r, b = self.s, self.r, self.b
            val = eval(func_str, g,
                        {'x': x, 'y': y, 'z': z,
                         's':s, 'r':r, 'b': b})
        except:
            # Mistake, so return the original value.
            val = getattr(self.flow.mlab_source, comp)
        return val

    ######################################################################
    # Private interface.
    ######################################################################
    def _points_default(self):
        x, y, z = np.mgrid[-50:50:100j,-50:50:100j,-10:60:70j]
        return x, y, z

    def _flow_default(self):
        x, y, z = self.points
        u, v, w = self.get_uvw()
        f = self.scene.mlab.flow(x, y, z, u, v, w)
        f.stream_tracer.integration_direction = 'both'
        f.stream_tracer.maximum_propagation = 200
        src = f.mlab_source.m_data
        o = mlab.outline()
        mlab.view(120, 60, 150)
        return f


if __name__ == '__main__':
    # Instantiate the class and configure its traits.
    lor = Lorenz()
    lor.configure_traits()

