"""The base source object from which all MayaVi sources derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import List, Str
from apptools.persistence.state_pickler import set_state
from traitsui.menu import Action
from tvtk.api import write_data
from apptools.scripting.api import recordable

# Local imports
from mayavi.core.base import Base
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.module import Module
from mayavi.core.module_manager import ModuleManager
from mayavi.core.common import handle_children_state, \
                                         exception, error
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.adder_node import ModuleFilterAdderNode

######################################################################
# Utility functions.
######################################################################
def is_filter(object):
    from mayavi.core.filter import Filter
    return isinstance(object, Filter)


######################################################################
# `Source` class.
######################################################################
class Source(PipelineBase):
    """ Base class for the sources objects in the pipeline.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The children of this source in the tree view.  These objects all
    # get the output of this source.
    children = List(Base, record=True)

    # The icon
    icon = 'source.ico'

    # The human-readable type for this object
    type = Str(' data source')

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['none'])

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'])

    # The adder node dialog class
    _adder_node_class = ModuleFilterAdderNode

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
            if self.recorder is not None:
                index = len(self.children) - 1
                self.recorder.register(mm, parent=self,
                                       trait_name_on_parent='children[%d]'%index)
        mm.children.append(module)

    @recordable
    def save_output(self, fname):
        """Save our output (by default the first of our outputs) to the
        specified filename as a VTK file.  Both old style and new style
        XML files are supported.
        """
        if len(self.outputs) > 0:
            write_data(self.get_output_dataset(), fname)
        else:
            error('Object has no outputs to save!')

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
            self.parent.add_child(child)
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
        from mayavi.core.filter import Filter
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
            obj.trait_set(scene=self.scene, parent=self)
            if isinstance(obj, ModuleManager):
                obj.source = self
            elif is_filter(obj):
                obj.inputs.append(self)
            if self.running:
                try:
                    obj.start()
                except:
                    exception()

    def _scene_changed(self, old, new):
        super(Source, self)._scene_changed(old, new)
        for obj in self.children:
            obj.scene = new

    def _visible_changed(self,value):
        for c in self.children:
            c.visible = value

        super(Source,self)._visible_changed(value)

    def _menu_helper_default(self):
        from mayavi.core.traits_menu import FilterMenuHelper
        return FilterMenuHelper(object=self)

    def _extra_menu_items(self):
        """Return a save output menu action."""
        save_output = Action(name='Save output to file',
                             action='object._save_output_action',
                             enabled_when='len(object.outputs) > 0')
        return [save_output]

    def _save_output_action(self):
        """Pops up a dialog box for the action to ask for a file."""
        # FIXME: in a refactor this should all go in a separate view
        # related object.
        from pyface.api import FileDialog, OK
        wildcard = 'All files (*.*)|*.*|'\
                   'VTK XML files (*.xml)|*.xml|'\
                   'Image Data (*.vti)|*.vti|'\
                   'Poly Data (*.vtp)|*.vtp|'\
                   'Rectilinear Grid (*.vtr)|*.vtr|'\
                   'Structured Grid (*.vts)|*.vts|'\
                   'Unstructured Grid (*.vtu)|*.vtu|'\
                   'Old-style VTK files (*.vtk)|*.vtk'

        dialog = FileDialog(title='Save output to file',
                            action='save as', wildcard=wildcard
                            )
        if dialog.open() == OK:
            self.save_output(dialog.path)
