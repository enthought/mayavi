"""Actions to start various filters.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

from pyface.action.api import Action
from traits.api import Instance

from mayavi.plugins.script import get_imayavi
from mayavi.core.registry import registry
from mayavi.core.metadata import Metadata
from mayavi.core.pipeline_base import PipelineBase

def new_class(name, bases, dict_):
    try:
        import new
        return new.classobj(name, bases, dict_)
    except ImportError:
        return type(name, bases, dict_)

######################################################################
# `FilterAction` class.
######################################################################
class FilterAction(Action):

    # The Metadata associated with this particular action.
    metadata = Instance(Metadata)

    mayavi = Instance('mayavi.plugins.script.Script')

    # We disable the actions by default since these are dynamically
    # enabled depending on the current selection or object.
    enabled = False

    def __init__(self, **traits):
        super(FilterAction, self).__init__(**traits)
        self.mayavi.engine.on_trait_change(self._update_enabled,
                                           ['current_selection',
                                            'current_object'])

    ###########################################################################
    # 'Action' interface.
    ###########################################################################
    def perform(self, event):
        """ Performs the action. """
        callable = self.metadata.get_callable()
        obj = callable()
        mv = self.mayavi
        mv.add_filter(obj)
        mv.engine.current_selection = obj

    def _update_enabled(self, obj):
        if isinstance(obj, PipelineBase):
            e = obj.menu_helper.check_active(self.metadata)
            self.enabled = e
        else:
            self.enabled = False

    def _mayavi_default(self):
        return get_imayavi(self.window)


######################################################################
# Creating the filter actions automatically.
for filter in registry.filters:
    d = {'tooltip': filter.tooltip,
         'description': filter.desc,
         'metadata': filter}
    action = new_class(filter.id, (FilterAction,), d)
    globals()[filter.id] = action
