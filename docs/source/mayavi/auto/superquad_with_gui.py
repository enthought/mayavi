"""
This example uses MayaVi to show the evolution of a superquadric
(http://en.wikipedia.org/wiki/Superquadrics), which are ellipsoidal surfaces parametrised
by two parameters,\alpha and \beta. The equations that are used to determine the superquadric are 
(in spherical-polar coordinates):

  \(x = A(\sin^{\alpha}(\phi)*\cos^{\beta}(\theta))\)
  \(y = B(\sin^{\alpha}(\phi)*\sin^{\beta}(\theta))\)
  \(z = C(\cos^{\alpha}(\phi))\)

Note that when we set A=B=C=r, and \alpha =  \beta = 1, we get the 
equation for a sphere in spherical polar coordinate.

Use the controls at the bottom of the plot to adjust \alpha and \beta,
and watch as the figure transforms accordingly!

"""

# Author: Pratik Mallya <pmallya@enthought.com>
# Copyright (c) 2008-2020, Enthought, Inc.
# License: BSD Style.

import numpy as np
from enthought.traits.api import HasTraits, Range, Instance, \
                    on_trait_change
from enthought.traits.ui.api import View, Item, HGroup
from enthought.tvtk.pyface.scene_editor import SceneEditor
from enthought.mayavi.tools.mlab_scene_model import \
                    MlabSceneModel
from enthought.mayavi.core.ui.mayavi_scene import MayaviScene


def fexp(x,p):
    """a different kind of exponentiation"""
    return (np.sign(x) * (np.abs(x)**p))

def tens_fld(A,B,C,P,Q):
    """this module plots superquadratic surfaces with the given parameters"""
    phi, theta = np.mgrid[0:np.pi:80j, 0:2*np.pi:80j]
    x = A * (fexp(np.sin(phi),P)) * (fexp(np.cos(theta),Q))
    y = B * (fexp(np.sin(phi),P)) * (fexp(np.sin(theta),Q))
    z = C * (fexp(np.cos(phi),P))
    return x , y , z 


class Visualization(HasTraits):
    alpha = Range(0.0, 4.0, 1.0/4)
    beta  = Range(0.0, 4.0, 1.0/4)
    scene = Instance(MlabSceneModel, ())

    def __init__(self):
        # Do not forget to call the parent's __init__
        HasTraits.__init__(self)
        x, y, z, = tens_fld(1, 1, 1, self.beta, self.alpha)
        self.plot = self.scene.mlab.mesh(x, y, z, colormap='copper', representation='surface')

    @on_trait_change('beta,alpha')
    def update_plot(self):
        x, y, z, = tens_fld(1, 1, 1, self.beta, self.alpha)
        self.plot.mlab_source.set(x = x, y = y, z = z)


    # the layout of the dialog created
    view = View(Item('scene', editor = SceneEditor(scene_class=MayaviScene),
                    height = 750, width=750, show_label=False),
                HGroup(
                        '_', 'beta', 'alpha',
                    ),
                )

visualization = Visualization()
visualization.configure_traits()


