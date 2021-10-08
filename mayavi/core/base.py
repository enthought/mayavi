"""The base object from which all MayaVi pipeline objects derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import pickle
from copy import deepcopy
import os
import logging
import importlib

# Enthought library imports.
from traits.api import (Any, Instance, Property, Bool, Str, Python,
                        HasTraits, WeakRef, on_trait_change)
from traitsui.api import TreeNodeObject
from tvtk.pyface.tvtk_scene import TVTKScene
from apptools.persistence import state_pickler
from pyface.resource.api import resource_path
from pyface.image_resource import ImageResource
from traitsui.menu import Menu, Action, Separator
from traitsui.api import View
from apptools.scripting.api import Recorder

# Local imports.
from mayavi.preferences.api import preference_manager
from mayavi.core.common import get_engine

# Setup a logger for this module.
logger = logging.getLogger(__name__)

# Subdirectory that the Base class will check for possible external views.
UI_DIR_NAME = ['ui']

# ------------------------------------------------------------------------------
#  The core tree node menu actions:
# ------------------------------------------------------------------------------

NewAction = 'NewAction'
CopyAction = Action(
    name='Copy',
    action='editor._menu_copy_node',
    enabled_when='editor._is_copyable(object)'
)
CutAction = Action(
    name='Cut',
    action='editor._menu_cut_node',
    enabled_when='editor._is_cutable(object)'
)
PasteAction = Action(
    name='Paste',
    action='editor._menu_paste_node',
    enabled_when='editor._is_pasteable(object)'
)
DeleteAction = Action(
    name='Delete',
    action='editor._menu_delete_node',
    enabled_when='editor._is_deletable(object)'
)
RenameAction = Action(
    name='Rename',
    action='editor._menu_rename_node',
    enabled_when='editor._is_renameable(object)'
)
standard_menu_actions = [
    Separator(),
    CutAction,
    CopyAction,
    PasteAction,
    Separator(),
    RenameAction,
    DeleteAction,
    Separator(),
]


######################################################################
# `Base` class.
######################################################################
class Base(TreeNodeObject):
    # The version of this class.  Used for persistence.
    __version__ = 0

    ########################################
    # Traits

    # The scene (RenderWindow) associated with this component.
    scene = Instance(TVTKScene, record=False)

    # Is this object running as part of the mayavi pipeline.
    running = Property(Bool, record=False)

    # The object's name.
    name = Str('')

    # The default icon.
    icon = 'module.ico'

    # The human readable type for this object
    type = Str('', record=False)

    # Is this object visible or not.
    visible = Bool(True, desc='if the object is visible')

    # Extend the children list with an AdderNode when a TreeEditor needs it.
    children_ui_list = Property(depends_on=['children'], record=False)

    # The parent of this object, i.e. self is an element of the parents
    # children.  If there is no notion of a parent/child relationship
    # this trait is None.
    parent = WeakRef(record=False)

    # A helper for the right click menus, context sensitivity etc.
    menu_helper = Instance(HasTraits, record=False)

    # Our recorder.
    recorder = Instance(Recorder, record=False)

    ##################################################
    # Private traits
    _is_running = Bool(False)

    # This is used to save the state of the object when it is not
    # running.  When the object "starts", the state is loaded.  This
    # is done because a stopped object will not have a meaningful VTK
    # pipeline setup, so setting its state will lead to all kinds of
    # errors.
    _saved_state = Any('')

    # Hide and show actions
    _HideShowAction = Instance(Action,
                               kw={'name': 'Hide/Show',
                                   'action': 'object._hideshow'}, )

    # The menu shown on right-click for this.
    _menu = Instance(Menu, transient=True)

    # Path to the icon for this object.
    _icon_path = Str()

    # Adder node: a dialog to add children to this object
    _adder_node_class = None

    # Name of the file that may host the hand-crafted view
    _view_filename = Str(transient=True)

    # Hand crafted view.
    _module_view = Instance(View, transient=True)

    # Work around problem with HasPrivateTraits.
    __ = Python
    ##################################################

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        """Method used by the state_pickler.
        """
        d = self.__dict__.copy()
        for attr in ('scene', '_is_running', '__sync_trait__',
                     '__traits_listener__', '_icon_path',
                     '_menu', '_HideShowAction', 'menu_helper',
                     'parent', 'parent_', '_module_view', '_listener_cache',
                     '_view_filename', 'mlab_source'):
            d.pop(attr, None)
        return d

    def __getstate__(self):
        """Allows standard pickle to work via the state_pickler.
        """
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        """Allows standard pickle to work via the state_pickler.
        """
        self.__init__()
        # Get the state from the string and update it.
        state = state_pickler.loads_state(str_state)
        state_pickler.update_state(state)
        # Save the state and load it if we are running.
        self._saved_state = pickle.dumps(state)
        if self.running:
            self._load_saved_state()

    def __deepcopy__(self, memo):
        """Method used by copy.deepcopy().  This also uses the
        state_pickler to work correctly.
        """
        # Create a new instance.
        new = self.__class__()
        # If we have a saved state, use it for the new instance.  If
        # not, get our state and save that.
        saved_state = self._saved_state
        if len(saved_state) == 0:
            state = state_pickler.get_state(self)
            # FIXME: This is for streamline seed point widget position which
            # does not get serialized correctly
            try:
                st = state.children[0].children[4]
                l_pos = st.seed.widget.position
                st.seed.widget.position = [pos.item() for pos in l_pos]
            except (IndexError, AttributeError):
                pass
            saved_state = pickle.dumps(state)
        new._saved_state = saved_state
        # In the unlikely case that a new instance is running, load
        # the saved state.
        if new.running:
            new._load_saved_state()
        return new

    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """Invoked when this object is added to the mayavi pipeline.
        """
        self.running = True
        self._load_saved_state()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        self.running = False

    def add_child(self, child):
        """This method intelligently adds a child to this object in
        the MayaVi pipeline.
        """
        raise NotImplementedError

    def remove_child(self, child):
        """Remove specified child from our children.
        """
        raise NotImplementedError()

    def remove(self):
        """Remove ourselves from the mayavi pipeline.
        """
        if self.parent is not None:
            e = get_engine(self)
            self.parent.remove_child(self)
            if e.current_object is self:
                e.current_object = self.parent

    def render(self):
        """Invokes render on the scene, this in turn invokes Render on
        the VTK pipeline.
        """
        s = self.scene
        if s is not None:
            s.render()

    def dialog_view(self):
        """ Returns a view with an icon and a title.
        """
        view = self.trait_view()
        icon = self._icon_path + os.sep + 'images' + os.sep + self.icon
        view.icon = ImageResource(icon)
        view.title = "Edit%s: %s" % (self.type, self.name)
        view.buttons = ['OK', 'Cancel']
        return view

    def trait_view(self, name=None, view_element=None):
        """ Gets or sets a ViewElement associated with an object's class.

        Overridden here to search for a separate file in the same directory
        for the view to use for this object. The view should be declared in
        the file named <class name>_view. If a file with this name is not
        found, the trait_view method on the base class will be called.
        """

        # If a name is specified, then call the HasTraits trait_view method
        # which will return (or assign) the *view_element* associated with
        # *name*.
        if name:
            return super(Base, self).trait_view(name, view_element)

        view = self._load_view_cached(name, view_element)
        # Uncomment this when developping views.
        # view = self._load_view_non_cached(name, view_element)
        return view

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_get_label(self, node):
        """Gets the label to display for a specified object.
        """
        if self.name == '':
            self.name = self.__class__.__name__
        return self.name

    def tno_get_view(self, node):
        """Gets the View to use when editing an object.
        """
        view = self.trait_view()
        view.kind = 'subpanel'
        return view

    def tno_confirm_delete(self, node):
        """Confirms that a specified object can be deleted or not.
        """
        if preference_manager.root.confirm_delete:
            return None
        else:
            return True

    def tno_get_menu(self, node):
        """ Returns the contextual pop-up menu.
        """
        if self._menu is None:
            return super(Base, self).tno_get_menu(node)
        return self._menu

    def tno_get_icon(self, node, is_expanded):
        return self.icon

    def tno_get_icon_path(self, node):
        return self._icon_path

    def tno_delete_child(self, node, index):
        if len(self.children_ui_list) > len(self.children):
            del self.children[index - 1]
        else:
            del self.children[index]

    def tno_append_child(self, node, child):
        """ Appends a child to the object's children.
        """
        self.children.append(child)

    def tno_insert_child(self, node, index, child):
        """ Inserts a child into the object's children.
        """
        if len(self.children_ui_list) > len(self.children):
            idx = index - 1
        else:
            idx = index
        self.children[idx:idx] = [child]

    ######################################################################
    # Non-public interface
    ######################################################################
    def _get_running(self):
        return self._is_running

    def _set_running(self, new):
        if self._is_running == new:
            return
        else:
            old = self._is_running
            self._is_running = new
            self.trait_property_changed('running', old, new)

    def _get_children_ui_list(self):
        """ Getter for Traits Property children_ui_list.

        For the base class, do not add anything to the children list.
        """
        if ((not preference_manager.root.show_helper_nodes or
             len(self.children) > 0)
            or self._adder_node_class is None
            or (not self.type == ' scene' and
                'none' in self.output_info.datasets)):
            # We can't use isinstance, as we would have circular
            # imports
            return self.children
        else:
            return [self._adder_node_class(object=self)]

    @on_trait_change('children[]')
    def _trigger_children_ui_list(self, old, new):
        """ Trigger a children_ui_list change when scenes changed.
        """
        self.trait_property_changed('children_ui_list', old, new)

    def _visible_changed(self, value):
        # A hack to set the name when the tree view is not active.
        # `self.name` is set only when tno_get_label is called and this
        # is never called when the tree view is not shown leading to an
        # empty name.
        if len(self.name) == 0:
            self.tno_get_label(None)
        if value:
            self.name = self.name.replace(' [Hidden]', '')
        else:
            n = self.name
            if ' [Hidden]' not in n:
                self.name = "%s [Hidden]" % n

    def _load_view_cached(self, name, view_element):
        """ Use a cached view for the object, for faster refresh.
        """
        if self._module_view is not None:
            view = self._module_view
        else:
            logger.debug("No view found for [%s] in [%s]. "
                         "Using the base class trait_view instead.",
                         self, self._view_filename)
            view = super(Base, self).trait_view(name, view_element)
        return view

    def _load_view_non_cached(self, name, view_element):
        """ Loads the view by execing a file. Useful when tweaking
            views.
        """
        result = {}
        view_filename = self._view_filename
        try:
            exec(compile(
                open(view_filename).read(), view_filename, 'exec'), {}, result
            )
            view = result['view']
        except IOError:
            logger.debug("No view found for [%s] in [%s]. "
                         "Using the base class trait_view instead.",
                         self, view_filename)
            view = super(Base, self).trait_view(name, view_element)
        return view

    def _hideshow(self):
        if self.visible:
            self.visible = False
        else:
            self.visible = True

    def _load_saved_state(self):
        """Load the saved state (if any) of this object.
        """
        saved_state = self._saved_state
        if len(saved_state) > 0:
            state = pickle.loads(saved_state)
            if hasattr(self, '__set_pure_state__'):
                self.__set_pure_state__(state)
            else:
                state_pickler.set_state(self, state)
            self._saved_state = ''

    def __view_filename_default(self):
        """ The name of the file that will host the view.
        """
        module = self.__module__.split('.')
        class_filename = module[-1] + '.py'
        module_dir_name = module[1:-1]
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        view_filename = os.path.join(*([base_dir] + module_dir_name
                                       + UI_DIR_NAME + [class_filename]))
        return view_filename

    def __module_view_default(self):
        """ Try to load a view for this object.
        """
        view_filename = self._view_filename
        if os.path.exists(view_filename):
            spec = importlib.util.spec_from_file_location(
                'view', view_filename
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            view = module.view
        else:
            view = None
        return view

    def __menu_default(self):
        extras = []
        if self.menu_helper is not None:
            extras = self.menu_helper.actions + self._extra_menu_items()
        menu_actions = [Separator()] + extras + \
            [Separator(), self._HideShowAction, Separator()] + \
            deepcopy(standard_menu_actions)
        return Menu(*menu_actions)

    def __icon_path_default(self):
        return resource_path()

    def _extra_menu_items(self):
        """Override this to generate any new menu actions you want on
        the right click menu."""
        return []
