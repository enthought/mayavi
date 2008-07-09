"""
A custom node for a Tree Editor that provides views for adding various nodes
to the tree.
"""
# Author: Judah De Paula <judah@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.
from enthought.traits.api import HasTraits, Str, Property, Any
from enthought.traits.ui.api import View, Item, Group


class AdderNode(HasTraits):
    label = Str('AdderNode')
    tooltip = Str('Add an item')
    object =  Any
    scene = Property
    
    
    def dialog_view(self):
        view = self.trait_view()    
        view.buttons = ['OK', 'Cancel']
        view.title = self.label
        return view
    
    
    def trait_view(self):
        view = View(Group(label='test 2'))
        return view
    
    
    def _get_scene(self):
        if self.object is not None:
            return self.object.scene
        else:
            return None
