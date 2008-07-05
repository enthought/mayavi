"""Actions to start various filters.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

import new

from enthought.pyface.action.api import Action
from enthought.traits.api import Instance

from enthought.mayavi.plugins.script import  get_imayavi
from enthought.mayavi.core.registry import registry
from enthought.mayavi.core.metadata import Metadata


######################################################################
# `FilterAction` class.
######################################################################
class FilterAction(Action):

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
        mv.add_filter(obj)


######################################################################
# Creating the filter actions automatically.
for filter in registry.filters:
    d = {'tooltip': filter.tooltip,
         'description': filter.desc,
         'metadata': filter}
    action = new.classobj(filter.id, (FilterAction,), d)
    globals()[filter.id] = action

