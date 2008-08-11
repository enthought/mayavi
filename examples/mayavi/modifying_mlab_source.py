#!/usr/bin/env python
"""
An example of how to modify the data source of an object created by mlab 
function. 

This example uses a traits object to wire up callbacks to modify a plot.
The scene is displayed in the traits view using an mlab_scene_model.
"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


from numpy import arange, pi, cos, sin
from enthought.mayavi.mlab import plot3d

from enthought.traits.api import HasTraits, Range, Instance, \
        on_trait_change
from enthought.traits.ui.api import View, Item, HGroup, spring
from enthought.tvtk.pyface.scene_editor import SceneEditor
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel
from enthought.mayavi.core.pipeline_base import PipelineBase
from enthought.mayavi.core.ui.mayavi_scene import MayaviScene


dphi = pi/1000.
phi = arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')

def curve(n_mer, n_long):
    mu = phi*n_mer
    x = cos(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    y = sin(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    z = 0.5 * sin(n_long*mu/n_mer)
    t = sin(mu)
    return x, y, z, t    


class MyModel(HasTraits):
    n_meridional    = Range(0, 30, 6, )#mode='spinner')
    n_longitudinal  = Range(0, 30, 11, )#mode='spinner')

    scene = Instance(MlabSceneModel, ())

    plot = Instance(PipelineBase)

    def _plot_default(self):
        x, y, z, t = curve(self.n_meridional, self.n_longitudinal)
        return self.scene.mlab.plot3d(x, y, z, t,
                            tube_radius=0.025, colormap='Spectral')


    @on_trait_change('n_meridional,n_longitudinal')
    def update_plot(self):
        x, y, z, t = curve(self.n_meridional, self.n_longitudinal)
        self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t)

    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene), 
                     height=500, width=500, show_label=False), 
                '_', 
                HGroup('n_meridional', spring, 'n_longitudinal'))

my_model = MyModel()
my_model.update_plot()
my_model.configure_traits()
