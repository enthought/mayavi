"""
Sample Mayavi customization file.

This code is not to be executed as `mayavi2 -x user_mayavi.py` or
`python user_mayavi.py`.

Put this file in ~/.mayavi2/user_mayavi.py and rerun mayavi2 to see what
it does -- the worker view may not show up by default so you will have
to go to View->Other and in the Show View dialog, activate the "Custom
Mayavi2 View".

The added modules should show up in the menus (Look for UserOutline in
the Modules)

____

This module demonstrates how to extend Mayavi.  It extends the  modules
provided by mayavi by adding these to the Mayavi registry.  Note that
the registry imports customize which in turn imports this file.

It also defines an Envisage plugin that is added to the default list of
plugins to extend the running mayavi application.  This plugin is
returned by the `get_plugins()` function.

This file must be placed inside the `~/.mayavi2` directory and called
`user_mayavi.py`.  Please note that `~/.mayavi2` is placed in `sys.path`
(if the directory exists) so make sure that you choose your module names
carefully (so as not to override any common module names).

The file may also be placed anywhere on sys.path and called
`site_mayavi.py` for global system level customizations.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006-2020, Enthought, Inc.
# License: BSD Style.

from mayavi.core.registry import registry
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.metadata import ModuleMetadata

# Metadata for the new module we want to add -- notice that we use a
# factory function here for convenience, we could also use a class but
# the reasons for doing this are documented below.
user_outline = ModuleMetadata(
    id            = "UserOutlineModule",
    menu_name          = "&UserOutline",
    factory = 'user_mayavi.user_outline',
    desc   = "Draw a cornered outline for given input",
    tooltip       = "Draw a cornered outline for given input",
    help       = "Draw a cornered outline for given input",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

# Register the module with the mayavi registry.
registry.modules.append(user_outline)

#######
# The all important function that returns the plugin we wish to add to
# the default mayavi application.
def get_plugins():
    # We simply return a list containing the WorkerPlugin defined below.
    return [WorkerPlugin()]

######################################################################
# Thats it, basically.  The rest of the code should really be in another
# module but is in the same module for convenience here.  There are
# problems with doing any significant non-core module imports in this
# module as documented below.
######################################################################


######################################################################
# THE CODE BELOW SHOULD REALLY BE IN SEPARATE MODULES.
#
# The following can very well be in a separate module but I've kept it
# here to make this a compact demo of how to customize things.
######################################################################


######################################################################
# A new module to expose to mayavi.
#
# WARNING: Do not do other mayavi imports right here like for example:
# 'from mayavi.modules.outline import Outline' etc.  This is
# because the user_mayavi is imported at a time when many of the imports
# are not complete and this will cause hard-to-debug circular import
# problems.  The registry is given only metadata mostly in the form of
# strings and this will cause no problem.  Therefore to define new
# modules, we strongly recommend that the modules be defined in another
# module or be defined in a factory function as done below.

def user_outline():
    """A Factory function that creates a new module to add to the
    pipeline.  Note that the method safely does any mayavi imports
    inside avoiding any circular imports.
    """
    print("User Outline")
    from mayavi.modules.outline import Outline
    o = Outline(outline_mode='cornered', name='UserOutline')
    return o


######################################################################
# This code simulates something the user would like to do.  In this case
# we just want to create some data, view it with mayavi and modify the
# data.  We want to add this as a view to the standard mayavi.  The code
# below is simply traits code with a few extra things to be able to grab
# the running mayavi instance and script it.  The object we create we
# offer as an envisage service offer -- this instantiates the worker.
# The WorkerPlugin exposes the service offer and shows the view of this
# worker.

import numpy as np

from traits.api import HasTraits, Range, Button, Instance, List
from traitsui.api import Item, View

######################################################################
# `Worker` class
######################################################################
class Worker(HasTraits):
    """This class basically allows you to create a data set, view it
    and modify the dataset.  This is a rather crude example but
    demonstrates how things can be done.
    """

    # Set by envisage when this is contributed as a ServiceOffer.
    window = Instance('pyface.workbench.api.WorkbenchWindow')

    create_data = Button('Create data')
    reset_data = Button('Reset data')
    view_data = Button('View data')
    scale = Range(0.0, 1.0)
    source = Instance('mayavi.core.source.Source')

    # Our UI view.
    view = View(Item('create_data', show_label=False),
                Item('view_data', show_label=False),
                Item('reset_data', show_label=False),
                Item('scale'),
                resizable=True
                )

    def get_mayavi(self):
        from mayavi.plugins.script import Script
        return self.window.get_service(Script)

    def _make_data(self):
        dims = [64, 64, 64]
        np = dims[0]*dims[1]*dims[2]
        x, y, z = np.ogrid[-5:5:dims[0]*1j,-5:5:dims[1]*1j,-5:5:dims[2]*1j]
        x = x.astype('f')
        y = y.astype('f')
        z = z.astype('f')
        s = (np.sin(x*y*z)/(x*y*z))
        s = s.transpose().copy() # This makes the data contiguous.
        return s

    def _create_data_fired(self):
        mayavi = self.get_mayavi()
        from mayavi.sources.array_source import ArraySource
        s = self._make_data()
        src = ArraySource(transpose_input_array=False, scalar_data=s)
        self.source = src
        mayavi.add_source(src)

    def _reset_data_fired(self):
        self.source.scalar_data = self._make_data()

    def _view_data_fired(self):
        mayavi = self.get_mayavi()
        from mayavi.modules.outline import Outline
        from mayavi.modules.image_plane_widget import ImagePlaneWidget
        # Visualize the data.
        o = Outline()
        mayavi.add_module(o)
        ipw = ImagePlaneWidget()
        mayavi.add_module(ipw)
        ipw.module_manager.scalar_lut_manager.show_scalar_bar = True

        ipw_y = ImagePlaneWidget()
        mayavi.add_module(ipw_y)
        ipw_y.ipw.plane_orientation = 'y_axes'

    def _scale_changed(self, value):
        src = self.source
        data = src.scalar_data
        data += value*0.01
        np.mod(data, 1.0, data)
        src.update()

######################################################################
# The following code is the small amount of envisage code that brings
# the users code (above) and Envisage/Mayavi UI together.
from envisage.api import Plugin, ServiceOffer

######################################################################
# `WorkerPlugin` class
######################################################################
class WorkerPlugin(Plugin):

    # Extension point Ids.
    SERVICE_OFFERS = 'envisage.ui.workbench.service_offers'
    VIEWS          = 'envisage.ui.workbench.views'

    # Services we contribute.
    service_offers = List(contributes_to=SERVICE_OFFERS)
    # Views.
    views = List(contributes_to=VIEWS)

    ######################################################################
    # Private methods.
    def _service_offers_default(self):
        """ Trait initializer. """
        worker_service_offer = ServiceOffer(
            protocol = 'user_mayavi.Worker',
            factory  = 'user_mayavi.Worker'
        )
        return [worker_service_offer]

    def _views_default(self):
        """ Trait initializer. """
        return [self._worker_view_factory]

    def _worker_view_factory(self, window, **traits):
        """ Factory method for the current selection of the engine. """

        from pyface.workbench.traits_ui_view import \
                TraitsUIView

        worker = window.get_service(Worker)
        tui_worker_view = TraitsUIView(obj=worker,
                                       view='view',
                                       id='user_mayavi.Worker.view',
                                       name='Custom Mayavi2 View',
                                       window=window,
                                       position='left',
                                       **traits
                                       )
        return tui_worker_view

# END OF CODE THAT SHOULD REALLY BE IN SEPARATE MODULES.
######################################################################

if __name__ == '__main__':
    import sys
    print("*"*80)
    print("ERROR: This script isn't supposed to be executed.")
    print(__doc__)
    print("*"*80)

    from traits.util.home_directory import get_home_directory
    print("Your .mayavi2 directory should be in %s"%get_home_directory())
    print("*"*80)
    sys.exit(1)
