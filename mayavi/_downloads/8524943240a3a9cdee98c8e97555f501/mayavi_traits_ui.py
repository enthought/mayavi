#!/usr/bin/env python
"""
An example of how to create a UI similar to the complete Mayavi application
inside a Traits UI view.

This does not use Envisage and provides a similar UI as seen in the full
Mayavi application.

This example uses `traitsUI <http://docs.enthought.com/traitsui/>`_
to create a dialog mimicking the mayavi2 application: a scene on the
right, and on the left a pipeline tree view, and below it a panel to
edit the currently-selected object.
"""

# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard imports.
from numpy import sqrt, sin, mgrid

# Enthought imports.
from traits.api import HasTraits, Instance, Property, Enum
from traitsui.api import View, Item, HSplit, VSplit, InstanceEditor
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.core.ui.engine_view import EngineView
from mayavi.tools.mlab_scene_model import MlabSceneModel


######################################################################
class Mayavi(HasTraits):

    # The scene model.
    scene = Instance(MlabSceneModel, ())

    # The mayavi engine view.
    engine_view = Instance(EngineView)

    # The current selection in the engine tree view.
    current_selection = Property


    ######################
    view = View(HSplit(VSplit(Item(name='engine_view',
                                   style='custom',
                                   resizable=True,
                                   show_label=False
                                   ),
                              Item(name='current_selection',
                                   editor=InstanceEditor(),
                                   enabled_when='current_selection is not None',
                                   style='custom',
                                   springy=True,
                                   show_label=False),
                                   ),
                               Item(name='scene',
                                    editor=SceneEditor(),
                                    show_label=False,
                                    resizable=True,
                                    height=500,
                                    width=500),
                        ),
                resizable=True,
                scrollable=True
                )

    def __init__(self, **traits):
        HasTraits.__init__(self, **traits)
        self.engine_view = EngineView(engine=self.scene.engine)

        # Hook up the current_selection to change when the one in the engine
        # changes.  This is probably unnecessary in Traits3 since you can show
        # the UI of a sub-object in T3.
        self.scene.engine.on_trait_change(self._selection_change,
                                          'current_selection')

        self.generate_data_mayavi()

    def generate_data_mayavi(self):
        """Shows how you can generate data using mayavi instead of mlab."""
        from mayavi.sources.api import ParametricSurface
        from mayavi.modules.api import Outline, Surface
        e = self.scene.engine
        s = ParametricSurface()
        e.add_source(s)
        e.add_module(Outline())
        e.add_module(Surface())

    def _selection_change(self, old, new):
        self.trait_property_changed('current_selection', old, new)

    def _get_current_selection(self):
        return self.scene.engine.current_selection


if __name__ == '__main__':
    m = Mayavi()
    m.configure_traits()
