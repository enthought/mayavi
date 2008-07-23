"""The base source object from which all MayaVi sources derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import List, Str
from enthought.persistence.state_pickler import set_state

# Local imports
from enthought.mayavi.core.base import Base
from enthought.mayavi.core.pipeline_base import PipelineBase
from enthought.mayavi.core.module import Module
from enthought.mayavi.core.module_manager import ModuleManager
from enthought.mayavi.core.common import handle_children_state, exception
from enthought.mayavi.core.pipeline_info import PipelineInfo
from enthought.mayavi.core.adder_node import ModuleFilterAdderNode
from enthought.mayavi.preferences.api import preference_manager

######################################################################
# Utility functions.
######################################################################
def is_filter(object):
    from enthought.mayavi.core.filter import Filter
    return isinstance(object, Filter)


######################################################################
# `Source` class.
######################################################################
class Source(PipelineBase):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The children of this source in the tree view.  These objects all
    # get the output of this source.
    children = List(Base)

    # The icon
    icon = 'source.ico'

    # The human-readable type for this object
    type = Str(' data source')

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['none'])

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'])

    ######################################################################
    # `object` interface
    ######################################################################
    def __set_pure_state__(self, state):
        # Do everything but our kids.
        set_state(self, state, ignore=['children'])
        # Setup children.
        handle_children_state(self.children, state.children)
        # Now setup the children.
        set_state(self, state, first=['children'], ignore=['*'])
    

    ######################################################################
    # `Source` interface
    ######################################################################
    def add_module(self, module):
        """ Adds a module smartly.  If no ModuleManager instances are
        children, it first creates a new ModuleManager and then adds
        the module to it.  If not it adds the module to the first
        available ModuleManager instance."""
        
        mm = None
        for child in self.children:
            if isinstance(child, ModuleManager):
                mm = child
        if mm is None:
            mm = ModuleManager(source=self, scene=self.scene)
            if self.running:
                mm.start()
            self.children.append(mm)
        mm.children.append(module)


    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.
        """
        # Do nothing if we are already running.
        if self.running:
            return
        
        # Start all our children.
        for obj in self.children:
            try:
                obj.start()
            except:
                exception()

        # Call parent method to set the running state.
        super(Source, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Stop all our children.
        for obj in self.children:
            obj.stop()

        # Call parent method to set the running state.
        super(Source, self).stop()
        
    def add_child(self, child):
        """This method intelligently adds a child to this object in
        the MayaVi pipeline.        
        """
        if is_filter(child):
            # It is a Filter, so append to children.
            self.children.append(child)
        elif isinstance(child, Source):
            # A non-filter source object.  This should be added to the
            # scene.            
            self.scene.add_child(child)
        elif isinstance(child, Module):
            # Modules should be added carefully via add_module.
            self.add_module(child)
        elif isinstance(child, ModuleManager):
            self.children.append(child)
        else:
            self.children.append(child)

    def remove_child(self, child):
        """Remove specified child from our children.
        """
        self.children.remove(child)

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_can_add(self, node, add_object):
        """ Returns whether a given object is droppable on the node.
        """
        from enthought.mayavi.core.filter import Filter
        try:
            if issubclass(add_object, Filter) or \
                   issubclass(add_object, ModuleManager):
                return True
        except TypeError:
            if isinstance(add_object, Filter) or \
                   isinstance(add_object, ModuleManager):
                return True
        return False

    def tno_drop_object(self, node, dropped_object):
        """ Returns a droppable version of a specified object.
        """
        if is_filter(dropped_object) or \
               isinstance(dropped_object, ModuleManager):
            return dropped_object


    ######################################################################
    # Non-public interface
    ######################################################################
    def _children_changed(self, old, new):
        self._handle_children(old, new)

    def _children_items_changed(self, list_event):
        self._handle_children(list_event.removed, list_event.added)        

    def _handle_children(self, removed, added):
        # Stop all the removed children.
        for obj in removed:
            obj.stop()

        # Process the new objects.
        for obj in added:
            obj.set(scene=self.scene, parent=self)
            if isinstance(obj, ModuleManager):
                obj.source = self
            elif is_filter(obj):
                obj.inputs.append(self)
            if self.running:
                try:
                    obj.start()
                except:
                    exception()

    def _get_children_ui_list(self):
        """ Trait getter for scenes_ui Property.
        """
        if preference_manager.root.show_helper_nodes:
            node = ModuleFilterAdderNode(object=self)
            return [node] + self.children
        else:
            return self.children

    def _scene_changed(self, old, new):
        super(Source, self)._scene_changed(old, new)
        for obj in self.children:
            obj.scene = new

    def _visible_changed(self,value):
        for c in self.children:
            c.visible = value           

        super(Source,self)._visible_changed(value)

    def _menu_helper_default(self):
        from enthought.mayavi.core.traits_menu import FilterMenuHelper
        return FilterMenuHelper(object=self)
