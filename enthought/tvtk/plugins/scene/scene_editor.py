#!/usr/bin/env python
"""A Scene Editor that is placed in the work area.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.core.plugin import Plugin
from enthought.traits.api import Instance, Str, Event
from enthought.pyface.tvtk.scene import Scene
from enthought.pyface.tvtk.decorated_scene import DecoratedScene

from enthought.envisage.workbench.api import Editor

# Local imports.
from enthought.tvtk.plugins.scene.services import ITVTKSCENE

##############################################################################
# Handy functions
def _id_generator():
    """Returns a sequence of numbers for the title of the scene editor
    window."""
    n = 1
    while True:
        yield(n)
        n += 1

_id_generator = _id_generator()


##############################################################################
# SceneEditor class
class SceneEditor(Editor):

    # The TVTK scene object.
    scene = Instance(Scene)

    # The Scene plugin that we are part of.
    plugin = Instance(Plugin)

    # Our name -- this is really for compatibility with the UI plugin.
    # The workbench plugin's editor already defines a name trait.
    name = Str

    # Our id -- this is really for compatibility with the UI plugin.
    # The workbench plugin's editor already defines an 'id' trait.
    id = Str
    
    #### Events #####

    ## FIXME: These are temporary and should be removed once (and if)
    ## Martin adds them to the framework.

    # The editor has been activated.
    activated = Event

    # The editor is being closed.
    closing = Event

    # The editor has been closed.
    closed = Event

    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        super(SceneEditor, self).__init__(**traits)

        # The plugin trait is only set when _create_contents is
        # called.  This is because self.window is None in __init__.

        # We add ourselves to the plugin's `editors` attribute only
        # when the widget is created in `_create_contents`.

        # Set our name with a suitable id.
        self.id = self.name = 'TVTK Scene %d'%(_id_generator.next())        

    ###########################################################################
    # 'Window' interface.
    ###########################################################################
    def preferences_changed(self, value):
        """This is called when any of the plugin preferences changed."""
        key, old, new = value.key, value.old, value.new
        scene = self.scene
        if key == 'background_color':
            scene.renderer.background = new
        if key == 'foreground_color':
            scene.foreground = new
        if key == 'magnification':
            scene.magnification = new            
        scene.render()
    
    ###########################################################################
    # FIXME: these should be changed when the framework's editor has
    # lifecycle events added.
    # 'Editor' interface
    ###########################################################################
    def destroy_control(self):
        """ Destroys the toolkit-specific control that represents the
        editor.  This is overridden from parent Editor class to add
        lifecyle events.
        """
        if self.control is not None:
            self.closing = self
            
        super(SceneEditor, self).destroy_control()

        if self.control is not None:
            self.closed = self

    def set_focus(self):
        """ Sets the focus to the appropriate control in the editor.

        By default we set the focus to be the editor's top-level control.
        Override this method if you need to give focus to some other child
        control.
        """
        super(SceneEditor, self).set_focus()
        if self.control is not None:
            self.activated = self

    ###########################################################################
    # Protected 'Window' interface.
    ###########################################################################
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the window.

        This method is intended to be overridden if necessary.  By default we
        just create an empty frame.

        """
        frame = super(SceneEditor, self)._create_control(parent)
        frame.SetSize((500, 500))
        return frame

    def _create_contents(self, parent):
        """ Creates the window contents. """
        # Make sure that the plugin we are part of is started.
        app = self.window.application
        self.plugin = app.get_service(ITVTKSCENE)
        plugin = self.plugin
        
        prefs = plugin.preferences
        scene = DecoratedScene(parent, stereo=prefs.get('stereo'),
                               magnification=prefs.get('magnification'),
                               foreground=prefs.get('foreground_color'))
        scene.renderer.background = prefs.get('background_color')

        scene.render()        
        self.scene = scene

        # Add this editor to the plugin's editors.  We do this only
        # here and not at initialization time because the browser
        # plugin listens for this and requires that the scene
        # attribute be set.
        plugin.editors.append(self)
        plugin.current_editor = self

        return self.scene.control

    create_control = _create_contents

    def _closing_fired(self, event):
        """This event fires when the window closes."""
        # Remove ourselves from the plugin at this time.
        self.plugin.editors.remove(self)

    def _activated_fired(self, event):
        """This event fires when this frame/editor is activated."""
        self.plugin.current_editor = self
