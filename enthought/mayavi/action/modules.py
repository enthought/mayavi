"""Actions to start various modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

import new

# Enthought library imports.
from enthought.pyface.action.api import Action
from enthought.traits.api import Instance

# Local imports.
from enthought.mayavi.plugins.script import get_imayavi
from enthought.mayavi.core.registry import registry
from enthought.mayavi.core.metadata import Metadata

######################################################################
# `AddModuleManager` class.
######################################################################
class AddModuleManager(Action):
    """ An action that adds a ModuleManager to the tree. """

    tooltip       = "Add a ModuleManager to the current source/filter"

    description   = "Add a ModuleManager to the current source/filter"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.core.module_manager import ModuleManager
        mm = ModuleManager()
        mv = get_imayavi(self.window)
        mv.add_module(mm)

######################################################################
# `ModuleAction` class.
######################################################################
class ModuleAction(Action):

    # The Metadata associated with this particular action.
    metadata = Instance(Metadata)

    ###########################################################################
    # 'Action' interface.
    ###########################################################################
    def perform(self, event):
        """ Performs the action. """
        callable = self.metadata.get_callable()
        obj = callable()
        mv = get_imayavi(self.window)
        mv.add_module(obj)


######################################################################
# Creating the module actions automatically.
for module in registry.modules:
    d = {'tooltip': module.tooltip,
         'description': module.desc,
         'metadata': module}
    action = new.classobj(module.id, (ModuleAction,), d)
    globals()[module.id] = action

