"""Actions to start various modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Local imports.
from mayavi.core.registry import registry
from mayavi.core.metadata import ModuleMetadata
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.action.filters import FilterAction, new_class

######################################################################
# `ModuleAction` class.
######################################################################
class ModuleAction(FilterAction):

    ###########################################################################
    # 'Action' interface.
    ###########################################################################
    def perform(self, event):
        """ Performs the action. """
        callable = self.metadata.get_callable()
        obj = callable()
        mv = self.mayavi
        mv.add_module(obj)
        mv.engine.current_selection = obj


######################################################################
# `AddModuleManager` class.
######################################################################
class AddModuleManager(ModuleAction):
    """ An action that adds a ModuleManager to the tree. """

    tooltip       = "Add a ModuleManager to the current source/filter"

    description   = "Add a ModuleManager to the current source/filter"

    metadata = ModuleMetadata(id="AddModuleManager",
                class_name="mayavi.core.module_manager.ModuleManager",
                menu_name="&Add ModuleManager",
                tooltip="Add a ModuleManager to the current source/filter",
                description="Add a ModuleManager to the current source/filter",
                input_info = PipelineInfo(datasets=['any'],
                                  attribute_types=['any'],
                                  attributes=['any'])
                )

    def perform(self, event):
        """ Performs the action. """
        from mayavi.core.module_manager import ModuleManager
        mm = ModuleManager()
        mv = self.mayavi
        mv.add_module(mm)
        mv.engine.current_selection = mm


######################################################################
# Creating the module actions automatically.
for module in registry.modules:
    d = {'tooltip': module.tooltip,
         'description': module.desc,
         'metadata': module}
    action = new_class(module.id, (ModuleAction,), d)
    globals()[module.id] = action
