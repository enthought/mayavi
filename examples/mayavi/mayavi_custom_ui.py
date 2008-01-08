"""This module allows us to extend the MayaVi2 UI.  It defines two
lists: `extensions` and `requires` as expected by the
`enthought.envisage.api.PluginDefinition` class.

`extensions` must be a list of plugin extension contributions that we
want to add.  `requires` specifies a list of plugins that we'd like to
have started.  The `requires` does not ensure that the plugin is
actually loaded but only ensures that the "required" plugins are
started (if loaded) before the mayavi2 ui plugin.  For most common
tasks it unlikely we will need to use a non-empty requires.

This file must be placed inside the `~/.mayavi2` directory.

Please note that `~/.mayavi2` is placed in `sys.path` so make sure
that you choose your module names carefully (so as not to override any
common module names).

"""
# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006-2007, Enthought, Inc.
# License: BSD Style.

######################################################################
# THE FOLLOWING BLOCK OF CODE COULD BE IN A SEPARATE MODULE.
#
# The following can very well be in a separate module but I've kept it
# here to make this a compact demo of how to customize things.
######################################################################

# This code simulates something the user would like to do.  The code
# below is simply traits code with a few extra things to be able to
# grab the running mayavi instance and script it.  The envisage
# specific code only gets the application and the IMAYAVI service.
import numpy
import scipy

from enthought.traits.api import HasTraits, Range, Button, Instance
from enthought.traits.ui.api import Item, View
from enthought.mayavi.services import IMAYAVI


######################################################################
# A test class.
class Worker(HasTraits):
    """This class basically allows you to create a data set, view it
    and modify the dataset.  This is a rather crude example but
    demonstrates how things can be done.
    """
    
    # Set by envisage when this is instantiated using the
    # ApplicationObject.
    application = Instance  

    create_data = Button('Create data')
    reset_data = Button('Reset data')
    view_data = Button('View data')
    scale = Range(0.0, 1.0)
    source = Instance

    # Our UI view.
    view = View(Item('create_data', show_label=False),
                Item('view_data', show_label=False),
                Item('reset_data', show_label=False),
                Item('scale'),
                )

    def get_mayavi(self):
        return self.application.get_service(IMAYAVI)

    def _make_data(self):
        dims = [64, 64, 64]
        np = dims[0]*dims[1]*dims[2]
        x, y, z = scipy.ogrid[-5:5:dims[0]*1j,-5:5:dims[1]*1j,-5:5:dims[2]*1j]
        x = x.astype('f')
        y = y.astype('f')
        z = z.astype('f')        
        s = (scipy.sin(x*y*z)/(x*y*z))
        s = s.transpose().copy() # This makes the data contiguous.
        return s
    
    def _create_data_fired(self):
        mayavi = self.get_mayavi()
        from enthought.mayavi.sources.array_source import ArraySource
        s = self._make_data()
        src = ArraySource(transpose_input_array=False, scalar_data=s)
        self.source = src
        mayavi.add_source(src)        

    def _reset_data_fired(self):
        self.source.scalar_data = self._make_data()

    def _view_data_fired(self):
        mayavi = self.get_mayavi()
        from enthought.mayavi.modules.outline import Outline
        from enthought.mayavi.modules.image_plane_widget import ImagePlaneWidget
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
        numpy.mod(data, 1.0, data)
        src.update()
# END OF CODE THAT COULD BE IN A SEPARATE MODULE.
######################################################################


######################################################################
# The following code is the small amount of envisage code that brings
# the users code (above) and Envisage/MayaVi UI together.

from enthought.envisage.workbench.action.action_plugin_definition import \
     Action, Location, WorkbenchActionSet
from enthought.envisage.core.core_plugin_definition import \
     ApplicationObject
from enthought.mayavi.action.common import WorkbenchAction, get_imayavi
from enthought.envisage.workbench.workbench_plugin_definition import \
     Workbench, View

######################################################################
# Workbench actions.

# A simple example menu item action.

class AddModuleManager(WorkbenchAction):
    """Adds a module manager to the tree.
    """
    def perform(self):
        """ Performs the action.
        """
        from enthought.mayavi.core.module_manager import ModuleManager
        mm = ModuleManager()
        mv = get_imayavi(self.window)        
        mv.add_module(mm)


######################################################################
# The extension items.

# The menu bar action extension item.
add_mm = Action(
    id            = "user.ModuleManager",
    class_name    = "mayavi_custom_ui.AddModuleManager",
    name          = "&User Defined ModuleManager",
    tooltip       = "Add a user defined ModuleManager to the current source",
    description   = "Add a user defined ModuleManager to the current source",
    locations = [Location(path="MenuBar/VisualizeMenu/additions"),]
)

# The action set collects all the actions, menus etc.  The id and name
# are not important but 
action_set = WorkbenchActionSet(id='user.mayavi2.action_set',
                                name='User.MayaVi2.ActionSet',
                                actions=[add_mm])

# An elegant way to publish an object for all envisagers to use via
# the UOL -- here we publish the above Worker class as a service.
worker_app_obj = ApplicationObject(class_name='mayavi_custom_ui.Worker',
                                   uol='service://mayavi_custom_ui.Worker')

# Now add the view of our worker.
views = [View(name='Custom MayaVi2 View',
              id = 'mayavi_custom_ui.Worker',
              uol = 'service://mayavi_custom_ui.Worker',
              traits_ui_view = 'view',
              position = 'left')
         ]
workbench = Workbench(views=views)

######################################################################
# The all important extensions and requires.  These are injected into
# Envisage by the MayaVi2 UI plugin.
extensions = [worker_app_obj, action_set, workbench]
requires = []
