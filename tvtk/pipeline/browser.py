"""A tvtk pipeline browser.

An abstract `TreeGenerator` class defines the interface of a tree
generator.  This class is responsible for generating the list of
children.  Often tvtk object's children are collections of various
objects, some sequences and some simple objects.  In order to provide
a unified interface to all children, all of these objects are wrapped
using the `CompositeIterable` which presents all children as a single
iterable.

`SimpleTreeGenerator` does not do extensive analysis of the passed
object in order to compute the children.  `FullTreeGenerator` however
uses the algorithm that MayaVi-1.x uses and therefore generates a
large number of objects.

The `PipelineBrowser` class presents the view of the pipeline as a
tree.  It allows one to specify the TreeGenerator instance.  The
`TreeEditor` from the traits package is used to represent the view.  A
`TVTKLeafNode` defines a node that has no children.  A
`TVTKBranchNode` is a node that has children.  The nodes basically
wrap up the tvtk object and present an interface suitable for the
TreeEditor.

TODO:

 * When a node is selected, the actor involved could be highlighted.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import re

# Enthought library imports.
from traits.api import (HasTraits, Property, Any, Instance, Event,
                        Trait, List, Str, Dict, Python)
from traitsui.api import \
     TreeEditor, TreeNodeObject, ObjectTreeNode, View, Item, Group, VSplit
from traitsui.menu import Menu, Action

from tvtk.api import tvtk
from tvtk import messenger
from tvtk.tvtk_base import TVTKBase
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk.common import camel2enthought


######################################################################
# Utility functions.
######################################################################
def is_iterable(x):
    return hasattr(x, '__iter__')


def get_icon(object_name):
    """Given the name of the object, this function returns an
    appropriate icon image name.  If no icon is appropriate it returns
    the empty string."""

    # The mapping from names to icons.
    icon_map = {'actor': 'actor.png',
                'camera': 'camera.png',
                'coordinate': 'coordinate.png',
                'filter': 'filter.png',
                'lookuptable': 'lookuptable.png',
                'mapper': 'mapper.png',
                'polydata': 'polydata.png',
                'property': 'property.png',
                'reader': 'reader.png',
                'renderer': 'renderer.png',
                'rendererwindowinteractor': 'rendererwindowinteractor.png',
                'source': 'source.png',
                'texture': 'texture.png',
                'window': 'window.png',
                'writer': 'writer.png',
                }

    # Lower case the name.
    name = object_name.lower()

    for key in icon_map:
        if name.endswith(key):
            return icon_map[key]

    # No valid icon for this object.
    return ''


######################################################################
# `TreeGenerator` class.
######################################################################
class TreeGenerator(HasTraits):
    """Encapsulates the methods that generate the tree via the
    `get_children` method."""

    def has_children(self, obj):
        """Returns True if object `obj` has children."""
        raise NotImplementedError

    def get_children(self, obj):
        """Returns a dictionary containing the children of the object
        `obj`."""
        raise NotImplementedError

    def get_node(self, obj):
        """Get a node object representing this object."""
        raise NotImplementedError

    def get_nodes(self, menu):
        """Returns a list of nodes for the tree editor.  The menu
        entries to use for the nodes are passed as `menu`."""
        raise NotImplementedError


######################################################################
# `SimpleTreeGenerator` class.
######################################################################
class SimpleTreeGenerator(TreeGenerator):
    """This particular class generates a simple pipeline
    representation.  Not every possible object is obtained."""

    def has_children(self, obj):
        """Returns true of the object has children, false if not.  This is
        very specific to tvtk objects."""
        if isinstance(obj, (tvtk.RenderWindow, tvtk.Renderer,
                            tvtk.Collection)):
            return True

        for attribute in ['source', 'get_input', 'input', 'mapper', 'property',
                          'texture', 'text_property', 'volume_property',
                          'lookup_table', 'producer_port', 'producer',
                          'get_input_algorithm']:
            if hasattr(obj, attribute):
                return True

        return False

    def get_children(self, obj):
        """Returns the child objects of a particular tvtk object in a
        dictionary, the keys are the trait names.  This is used to
        generate the tree in the browser."""
        kids = {}
        def _add_kid(key, x):
            if x is None:
                kids[key] = None
            else:
                if type(x) in (type([]), type(())):
                    x1 = [i for i in x if isinstance(i, TVTKBase)]
                    if x1:
                        kids[key] = x1
                elif isinstance(x, TVTKBase):
                    kids[key] = x

        if isinstance(obj, tvtk.RenderWindow):
            return {'renderers':obj.renderers}
        elif isinstance(obj, tvtk.Renderer):
            if hasattr(obj, 'view_props'):
                return {'view_props':obj.view_props,
                        'active_camera':obj.active_camera}
            else:
                return {'props':obj.props,
                        'active_camera':obj.active_camera}

        #if isinstance(obj, tvtk.Collection):
        #    _add_kid(obj)

        # Misc. properties.
        for attribute in ['mapper', 'property', 'texture',
                          'text_property', 'volume_property',
                          'lookup_table', 'producer']:
            if hasattr(obj, attribute):
                _add_kid(attribute, getattr(obj, attribute))

        # Check for sources and inputs.
        if hasattr(obj, 'number_of_sources'):
            srcs = [obj.get_source(i)
                    for i in range(obj.number_of_sources)]
            _add_kid('source', srcs)
        elif hasattr(obj, 'source'):
            _add_kid('source', obj.source)

        if hasattr(obj, 'get_input_algorithm'):
            inputs = []
            if hasattr(obj, 'number_of_input_ports'):
                inputs = [obj.get_input_algorithm(i, j)
                          for i in range(obj.number_of_input_ports)
                          for j in range(
                                  obj.get_number_of_input_connections(i))]
            elif hasattr(obj, 'get_input'):
                inputs = [obj.get_input(i)
                          for i in range(obj.number_of_inputs)]
            _add_kid('input', inputs)
        elif hasattr(obj, 'input'):
            _add_kid('input', obj.input)

        if hasattr(obj, 'producer_port'):
            _add_kid('producer_port', obj.producer_port)

        return kids

    def get_node(self, obj):
        """Get a node object representing the object passed."""
        if self.has_children(obj):
            return TVTKBranchNode(object=obj, tree_generator=self)
        else:
            return TVTKLeafNode(object=obj)

    def get_nodes(self, menu):
        """Returns a list of nodes for the tree editor.  The menu
        entries to use are given as `menu`"""
        nodes = [ObjectTreeNode(node_for=[TVTKBranchNode],
                                view=View(Group(Item('object', style='custom'),
                                                show_labels=False)),
                                auto_open=False,
                                children='children', label='name', menu=menu,
                                rename=False, delete=False, copy=False,
                                insert=False),
                 ObjectTreeNode(node_for=[TVTKLeafNode],
                                view=View(Group(Item('object', style='custom'),
                                                show_labels=False)),
                                auto_open=False,
                                label='name', menu=menu, rename=False,
                                delete=False, copy=False, insert=False),
                 ObjectTreeNode(node_for=[TVTKCollectionNode],
                                auto_open=True, children='children',
                                label='name', menu=menu, rename=False,
                                delete=False, copy=False, insert=False),
                 ]
        return nodes


######################################################################
# `FullTreeGenerator` class.
######################################################################
class FullTreeGenerator(SimpleTreeGenerator):
    """This particular class picks up a lot more children in the
    pipeline and is similar to the code used in MayaVi-1.x's pipeline
    browser."""

    def __init__(self, **traits):
        super(FullTreeGenerator, self).__init__(**traits)
        self.last_transform = 0

    def get_children(self, obj):
        """Returns the child objects of a particular tvtk object in a
        dictionary, the keys are the trait names.  This is used to
        generate the tree in the browser."""

        vtk_obj = tvtk.to_vtk(obj)
        methods = self._get_methods(vtk_obj)

        kids = {}
        def _add_kid(key, x):
            if x is None:
                kids[key] = None
            else:
                if type(x) in (type([]), type(())):
                    x1 = [i for i in x if isinstance(i, TVTKBase)]
                    if x1:
                        kids[key] = x1
                elif isinstance(x, TVTKBase):
                    if hasattr(x, '__iter__'):
                        # Don't add iterable objects that contain non
                        # acceptable nodes
                        if len(list(x)) and isinstance(list(x)[0], TVTKBase):
                            kids[key] = x
                    else:
                        kids[key] = x

        for method in methods:
            attr = camel2enthought(method[0])
            if hasattr(obj, attr):
                _add_kid(attr, getattr(obj, attr))

        # Check for sources and inputs.
        if hasattr(obj, 'number_of_sources'):
            srcs = [obj.get_source(i)
                    for i in range(obj.number_of_sources)]
            _add_kid('source', srcs)
        elif hasattr(obj, 'source'):
            _add_kid('source', obj.source)

        if hasattr(obj, 'get_input_algorithm'):
            inputs = []
            if hasattr(obj, 'number_of_input_ports'):
                inputs = [obj.get_input_algorithm(i, j)
                          for i in range(obj.number_of_input_ports)
                          for j in range(
                                  obj.get_number_of_input_connections(i))]
            _add_kid('input', inputs)
        elif hasattr(obj, 'get_input'):
            inputs = [obj.get_input(i)
                      for i in range(obj.number_of_inputs)]
            _add_kid('input', inputs)
        elif hasattr(obj, 'input'):
            _add_kid('input', obj.input)

        if hasattr(obj, 'producer_port'):
            _add_kid('producer_port', obj.producer_port)

        return kids

    def has_children(self, obj):
        """Returns true of the object has children, false if not.  This is
        very specific to tvtk objects."""
        result = super(FullTreeGenerator, self).has_children(obj)
        # FIXME: This is inefficient.  We probably should cache the
        # get_children call.
        if not result and self.get_children(obj):
            return True
        return result

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _get_methods(self, vtk_obj):
        """Obtain the various methods from the passed object."""

        def _remove_method(name, methods, method_names):
            """Removes methods if they have a particular name."""
            try:
                idx = method_names.index(name)
            except ValueError:
                pass
            else:
                del methods[idx], method_names[idx]
            return methods, method_names

        # The following code basically gets the 'str' representation
        # of the VTK object and parses it to obtain information about
        # the object's children.  It is a hack but has worked well for
        # a *very* long time with MayaVi-1.x and before.

        # Oops, this isn't a VTK object.
        if not hasattr(vtk_obj, 'GetClassName'):
            return []

        methods = str(vtk_obj)
        methods = methods.split("\n")
        del methods[0]

        # using only the first set of indented values.
        patn = re.compile(r"  \S")
        for method in methods[:]:
            if patn.match(method):
                if method.find(":") == -1:
                    methods.remove(method)
                elif method[1].find("none") > -1:
                    methods.remove(method)
            else:
                methods.remove(method)

        # Props/Prop is deprecated in more recent VTK releases.
        for method in methods[:]:
            if method.strip()[:6] == "Props:":
                if hasattr(vtk_obj, "GetViewProps"):
                    methods.remove(method)
                    methods.append("ViewProps: ")
            elif method.strip()[:5] == "Prop:":
                if hasattr(vtk_obj, "GetViewProp"):
                    methods.remove(method)
                    methods.append("ViewProp: ")

        method_names = []
        for i in range(0, len(methods)):
            strng = methods[i].replace(" ", "")
            methods[i] = strng.split(":")
            method_names.append(methods[i][0])

        if re.match(r"vtk\w*Renderer", vtk_obj.GetClassName()):
            methods.append(["ActiveCamera", ""])

        if re.match(r"vtk\w*Assembly", vtk_obj.GetClassName()):
            methods.append(["Parts", ""])
            methods.append(["Volumes", ""])
            methods.append(["Actors", ""])

        if vtk_obj.IsA('vtkAbstractTransform'):
            if self.last_transform > 0:
                _remove_method('Inverse', methods, method_names)
            else:
                self.last_transform += 1
        else:
            self.last_transform = 0

        # Some of these object are removed because they arent useful in
        # the browser.  I check for Source and Input anyway so I dont need
        # them.
        for name in('Output', 'FieldData', 'CellData', 'PointData',
                    'Source', 'Input', 'ExtentTranslator', 'ProgressText',
                    'Interactor', 'Lights', 'Information', 'Executive'):
            _remove_method(name, methods, method_names)

        return methods


######################################################################
# `CompositeIterable` class.
######################################################################
class CompositeIterable(HasTraits):

    """This class allows one to iterate over a bunch of disparate
    objects treating them as one single iterable.  Each of the
    iterated objects is wrapped with a suitable Node class so that the
    object may be used in a Traits Tree Editor.
    """

    tree_generator = Instance(TreeGenerator)

    def __init__(self, args, **traits):
        super(CompositeIterable, self).__init__(**traits)
        self.args = args

    def __iter__(self):
        tg = self.tree_generator
        for arg in self.args:
            if is_iterable(arg):
                for x in arg:
                    yield tg.get_node(x)
            else:
                yield tg.get_node(arg)

    def __len__(self):
        x = 0
        for arg in self.args:
            if is_iterable(arg):
                x += len(arg)
            else:
                x += 1
        return x


######################################################################
# `TVTKLeafNode` class.
######################################################################
class TVTKLeafNode(TreeNodeObject):
    """Represents a leaf in the tree view."""

    # The tvtk object being wrapped.
    object = Instance(TVTKBase)
    # Name to show on the view.
    name = Property

    # Work around problem with HasPrivateTraits.
    __ = Python

    def __hash__(self):
        return hash(tvtk.to_vtk(self.object))

    def _get_name(self):
        return self.object.__class__.__name__

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_get_icon(self, node, is_expanded):
        """ Returns the icon for a specified object.
        """
        icon = get_icon(self.name)
        if icon:
            return icon
        else:
            return super(TVTKLeafNode, self).tno_get_icon(node, is_expanded)


######################################################################
# `TVTKBranchNode` class.
######################################################################
class TVTKBranchNode(TreeNodeObject):
    """Represents a branch in the tree view.  The `children` trait
    produces an iterable that represents the children of the branch.
    """
    # The tvtk object being wrapped.
    object = Instance(TVTKBase)
    # Children of the object.
    children = Property
    # Name to show on the view.
    name = Property
    # Tree generator to use.
    tree_generator = Instance(TreeGenerator)
    # Cache of children.
    children_cache = Dict

    # Work around problem with HasPrivateTraits.
    __ = Python

    def __init__(self, **traits):
        super(TVTKBranchNode, self).__init__(**traits)

    def __del__(self):
        try:
            self._remove_listners()
        except:
            pass

    def __hash__(self):
        return hash(tvtk.to_vtk(self.object))

    def _get_children_from_cache(self):
        return [x for x in self.children_cache.values() if x is not None]

    def _create_children(self):
        kids = self.tree_generator.get_children(self.object)
        self.children_cache = kids
        self._setup_listners()

    def _setup_listners(self):
        object = self.object
        kids = self.children_cache
        for key, val in kids.items():
            if isinstance(val, tvtk.Collection):
                vtk_obj = tvtk.to_vtk(val)
                messenger.connect(vtk_obj, 'ModifiedEvent',
                                  self._notify_children)
            else:
                object.on_trait_change(self._notify_children, key)

    def _remove_listners(self):
        object = self.object
        kids = self.children_cache
        for key, val in kids.items():
            if isinstance(val, tvtk.Collection):
                vtk_obj = tvtk.to_vtk(val)
                messenger.disconnect(vtk_obj, 'ModifiedEvent',
                                     self._notify_children)
            else:
                object.on_trait_change(self._notify_children, key, remove=True)

    def _notify_children(self, obj=None, name=None, old=None, new=None):
        old_val = self._get_children_from_cache()
        self._remove_listners()
        self._create_children()
        new_val = self._get_children_from_cache()
        self.trait_property_changed('children', old_val, new_val)

    def _get_children(self):
        if not self.children_cache:
            self._create_children()
        kids = self._get_children_from_cache()
        tg = self.tree_generator
        return CompositeIterable(kids, tree_generator=tg)

    def _get_name(self):
        return self.object.__class__.__name__

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_get_icon(self, node, is_expanded):
        """ Returns the icon for a specified object.
        """
        icon = get_icon(self.name)
        if icon:
            return icon
        else:
            return super(TVTKBranchNode, self).tno_get_icon(node, is_expanded)


######################################################################
# `TVTKCollectionNode` class.
######################################################################
class TVTKCollectionNode(TreeNodeObject):
    """Represents a collection of typically unconnected roots in the
    tree view.
    """
    # List of child nodes.
    object = List(TVTKBase)
    # Children of the object.
    children = Property
    # Name to show on the view.
    name = Str
    # Tree generator to use.
    tree_generator = Instance(TreeGenerator)

    # Work around problem with HasPrivateTraits.
    __ = Python

    def __init__(self, **traits):
        super(TVTKCollectionNode, self).__init__(**traits)

    def _get_children(self):
        tg = self.tree_generator
        return CompositeIterable(self.object, tree_generator=tg)


######################################################################
# `CloseHandler` class.
######################################################################
class UICloseHandler(TVTKBaseHandler):
    """This class cleans up after the UI for the object is closed."""
    # The browser associated with this UI.
    browser = Any

    def close(self, info, is_ok):
        """This method is invoked when the user closes the UI."""
        obj = info.object
        obj.on_trait_change(self.browser.render, remove=True)
        return True


######################################################################
# `PipelineBrowser` class.
######################################################################
class PipelineBrowser(HasTraits):
    # The tree generator to use.
    tree_generator = Trait(FullTreeGenerator(),
                           Instance(TreeGenerator))

    # The TVTK render window(s) associated with this browser.
    renwins = List

    # The root object to view in the pipeline.  If None (default), the
    # root object is the render_window of the Scene instance passed at
    # object instantiation time.
    root_object = List(TVTKBase)

    selected = Instance(TVTKBase)

    # This is fired when an object has been changed on the UI. Use this when
    # you do not set the renwins list with the render windows but wish to do
    # your own thing when the object traits are edited on the UI.
    object_edited = Event

    # Private traits.
    # The root of the tree to display.
    _root = Any
    _ui = Any

    ###########################################################################
    # `object` interface.
    ###########################################################################
    def __init__(self, renwin=None, **traits):
        """Initializes the object.

        Parameters
        ----------

        - renwin: `Scene` instance.  Defaults to None.

          This may be passed in addition to the renwins attribute
          which can be a list of scenes.

        """
        super(PipelineBrowser, self).__init__(**traits)
        self._ui = None
        self.view = None
        if renwin:
            self.renwins.append(renwin)

        self._root_object_changed(self.root_object)

    def default_traits_view(self):
        menu = Menu(Action(name='Refresh', action='editor.update_editor'),
                    Action(name='Expand all', action='editor.expand_all'))
        self.menu = menu

        nodes = self.tree_generator.get_nodes(menu)

        self.tree_editor = TreeEditor(nodes=nodes,
                                      editable=False,
                                      orientation='vertical',
                                      hide_root=True,
                                      on_select=self._on_select,
                                      on_dclick=self._on_dclick)
        view = View(Group(VSplit(Item(name='_root',
                                      editor=self.tree_editor,
                                      resizable=True),
                                 Item(name='selected',
                                      style='custom',
                                      resizable=True),
                                 show_labels=False,
                                 show_border=False)),
                    title='Pipeline browser',
                    help=False,
                    resizable=True, undo=False, revert=False,
                    width=.3, height=.3)
        return view

    ###########################################################################
    # `PipelineBrowser` interface.
    ###########################################################################
    def show(self, parent=None):
        """Show the tree view if not already show.  If optional
        `parent` widget is passed, the tree is displayed inside the
        passed parent widget."""
        # If UI already exists, raise it and return.
        if self._ui is not None and self._ui.control is not None:
            try:
                self._ui.control.Raise()
            except AttributeError:
                pass
            else:
                return
        else:
            # No active ui, create one.
            view = self.default_traits_view()
            if parent is not None:
                self._ui = view.ui(self, parent=parent, kind='subpanel')
            else:
                self._ui = view.ui(self, parent=parent)

    def update(self):
        """Update the tree view."""
        # This is a hack.
        if self._ui is not None and self._ui.control is not None:
            try:
                ed = self._ui._editors[0]
                ed.update_editor()
                self._ui.control.Refresh()
            except (AttributeError, IndexError):
                pass
    # Another name for update.
    refresh = update

    def render(self):
        """Calls render on all render windows associated with this
        browser."""
        self.object_edited = True
        for rw in self.renwins:
            rw.render()

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _make_default_root(self):
        tree_gen = self.tree_generator
        objs = [x.render_window for x in self.renwins]
        node = TVTKCollectionNode(object=objs, name="Root",
                                  tree_generator=tree_gen)
        return node

    def _tree_generator_changed(self, tree_gen):
        """Traits event handler."""
        if self._root:
            root_obj = self._root.object
        else:
            root_obj = self.root_object
        if root_obj:
            ro = root_obj
            if not hasattr(root_obj, '__len__'):
                ro = [root_obj]

            self._root = TVTKCollectionNode(object=ro,
                                            name="Root",
                                            tree_generator=tree_gen)
        else:
            self._root = self._make_default_root()

        self.tree_editor.nodes = tree_gen.get_nodes(self.menu)
        self.update()

    def _root_object_changed(self, root_obj):
        """Trait handler called when the root object is assigned to."""
        tg = self.tree_generator
        if root_obj:
            self._root = TVTKCollectionNode(object=root_obj, name="Root",
                                            tree_generator=tg)
        else:
            self._root = self._make_default_root()
            self.root_object = self._root.object
        self.update()

    def _root_object_items_changed(self, list_event):
        """Trait handler called when the items of the list change."""
        self._root_object_changed(self.root_object)

    def _on_dclick(self, obj):
        """Callback that is called when nodes are double-clicked."""
        if hasattr(obj, 'object') and hasattr(obj.object, 'edit_traits'):
            object = obj.object
            view = object.trait_view()
            view.handler = UICloseHandler(browser=self)
            object.on_trait_change(self.render)
            ui = object.edit_traits(view=view)

    def _on_select(self, obj):
        if hasattr(obj, 'object') and hasattr(obj.object, 'edit_traits'):
            new = obj.object
            old = self.selected
            if new != old:
                self.selected = new
            if old is not None:
                old.on_trait_change(self.render, remove=True)
            if new is not None:
                new.on_trait_change(self.render)



######################################################################
# Test cases.
######################################################################
def main(instantiate_gui=True):
    """Simple test case."""
    from tvtk.tools import ivtk

    v = ivtk.viewer(browser=False, instantiate_gui=instantiate_gui)
    cs = tvtk.ConeSource()
    m = tvtk.PolyDataMapper(input_connection=cs.output_port)
    a = tvtk.Actor(mapper=m)
    v.scene.add_actor(a)
    v.scene.reset_zoom()

    b = PipelineBrowser(v.scene)
    b.show()

    return v, b, a


if __name__ == '__main__':
    from pyface.api import GUI
    gui = GUI()
    v, b, a = main(instantiate_gui=False)
    gui.start_event_loop()
