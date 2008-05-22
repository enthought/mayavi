"""The base object from which all MayaVi pipeline objects derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import cPickle
from copy import deepcopy
import os

# Enthought library imports.
from enthought.traits.api import Instance, Property, Bool, Str, Python
from enthought.traits.ui.api import TreeNodeObject
from enthought.pyface.tvtk.tvtk_scene import TVTKScene
from enthought.persistence import state_pickler
from enthought.resource.api import resource_path
from enthought.pyface.image_resource import ImageResource
from enthought.traits.ui.menu \
    import Menu, Action, Separator

# Local imports.
from enthought.mayavi.preferences.api import preference_manager


#-------------------------------------------------------------------------------
#  The core tree node menu actions:
#-------------------------------------------------------------------------------

NewAction    = 'NewAction'
CopyAction   = Action( name         = 'Copy',
                       action       = 'editor._menu_copy_node',
                       enabled_when = 'editor._is_copyable(object)' )
CutAction    = Action( name         = 'Cut',
                       action       = 'editor._menu_cut_node',
                       enabled_when = 'editor._is_cutable(object)' )
PasteAction  = Action( name         = 'Paste',
                       action       = 'editor._menu_paste_node',
                       enabled_when = 'editor._is_pasteable(object)' )
DeleteAction = Action( name         = 'Delete',
                       action       = 'editor._menu_delete_node',
                       enabled_when = 'editor._is_deletable(object)' )
RenameAction = Action( name         = 'Rename',
                       action       = 'editor._menu_rename_node',
                       enabled_when = 'editor._is_renameable(object)' )
standard_menu_actions = [ CutAction, CopyAction, PasteAction, Separator(),
                    DeleteAction, Separator(), RenameAction, Separator() ]


######################################################################
# `Base` class.
######################################################################
class Base(TreeNodeObject):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The scene (RenderWindow) associated with this component.
    scene = Instance(TVTKScene)

    # Is this object running as part of the mayavi pipeline.
    running = Property(Bool)

    # The object's name.
    name = Str('')

    # The default icon.
    icon = 'module.ico'

    # The human readable type for this object
    type = Str('')

    # Is this object visible or not. 
    visible = Bool(True, desc='if the object is visible')


    ##################################################
    # Private traits
    _is_running = Bool(False)

    # This is used to save the state of the object when it is not
    # running.  When the object "starts", the state is loaded.  This
    # is done because a stopped object will not have a meaningful VTK
    # pipeline setup, so setting its state will lead to all kinds of
    # errors.
    _saved_state = Str('')

    # Hide and show actions
    _HideShowAction = Instance(Action,  
                            {'name': 'Hide', 'action': 'object._hideshow'}, )

    _menu = Instance(Menu)

    def __menu_default(self):
        menu_actions = deepcopy(standard_menu_actions) \
                        + [self._HideShowAction ]
        return Menu( *menu_actions)

    _icon_path = Str()

    def __icon_path_default(self):
        return resource_path()

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
                     '__traits_listener__',
                     '_menu', '_HideShowAction'):
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
        self._saved_state = cPickle.dumps(state)
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
            saved_state = cPickle.dumps(state)
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
        icon = self._icon_path + os.sep + 'images' + os.sep \
                            + self.icon
        view.icon = ImageResource(icon)
        view.title = "Edit%s: %s" % (self.type, self.name)
        view.buttons = ['OK', 'Cancel']
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

    def tno_get_menu ( self, node ):
        """ Returns the contextual pop-up menu.
        """
        if self._menu is None:
            return super(Base, self).tno_get_menu(node)
        return self._menu

    def tno_get_icon(self, node, is_expanded):
        return self.icon

    def tno_get_icon_path(self, node):
        return self._icon_path


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

    def _running_changed(self):
        if self.running:
            if ' [Stopped]' in self.name:
                self.name = self.name.replace(' [Stopped]', '')
        else:
            self.name = "%s [Stopped]" % self.name

    def _visible_changed(self , value):
        if value:
            self._HideShowAction.name = "Hide"
            self.name = self.name.replace(' [Hidden]', '')
        else:
            self._HideShowAction.name = "Show"
            self.name = "%s [Hidden]" % self.name

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
            state = cPickle.loads(saved_state)
            if hasattr(self, '__set_pure_state__'):
                self.__set_pure_state__(state)
            else:
                state_pickler.set_state(self, state)
            self._saved_state = ''
