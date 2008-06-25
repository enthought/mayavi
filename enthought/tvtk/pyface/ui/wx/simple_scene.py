#------------------------------------------------------------------------------
#
#  Copyright (c) 2005, Enthought, Inc.
#  All rights reserved.
#  
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#  
#  Author: Enthought, Inc.
#
#------------------------------------------------------------------------------

""" A simple TVTK scene.
"""

# Major package imports.
from vtk.wx.wxVTKRenderWindow import wxVTKRenderWindow
import wx

# Enthought library imports.
from enthought.pyface.api import Widget
from enthought.traits.api import Any, Float, Property
from enthought.tvtk.api import tvtk


class SimpleScene(Widget):
    """ A simple TVTK scene. """


    ###########################################################################
    # 'object' interface.
    ###########################################################################

    def __init__(self, parent, **traits):
        """ Creates a new panel. """

        # Base class constructor.
        super(SimpleScene, self).__init__(**traits)

        # Create the widget's toolkit-specific control.
        self.control = self._create_control(parent)

        # fixme: Need this to stop actors being garbage collected!!!
        self._actors= []
        
        return

    ###########################################################################
    # 'SimpleScene' interface.
    ###########################################################################

    def render(self):
        """ Force the scene to be rendered. """

        self.control.Render()
        
        return
    
    def _get_renderer(self):
        """ Returns the scene's one and only renderer. """
        
        return self._renderer

    renderer = Property(_get_renderer)
    
    def _get_camera(self):
        """ Returns the active camera. """

        return self._renderer.active_camera

    camera = Property(_get_camera)
        
    def _get_actors(self):
        """ Returns all of the actors in the scene.

        This method just delegates to the scene's single renderer.
        
        """

        return self._renderer.actors    

    actors = Property(_get_actors)
    
    def add_actor(self, actor):
        """ Add an actor to the scene.
        
        This method just delegates to the scene's single renderer.
        
        """
        
        self._actors.append(actor)
        self._renderer.add_actor(actor)

        # fixme: for now, render on trait change.
        if hasattr(actor, 'on_trait_change'):
            actor.on_trait_change(self.render)

        return
        
    def remove_actor(self, actor):
        """ Remove an actor from the scene.
        
        This method just delegates to the scene's single renderer.
        
        """

        return self._renderer.remove_actor(actor)

    ###########################################################################
    # Private interface.
    ###########################################################################
    
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the widget. """

        self.control = window = wxVTKRenderWindow(parent, -1)
        
        # For some reason the size of the window needs to be changed
        # to prevent severe problems under Linux.
        parent.Show(1)
        wx.Yield()
        window.SetSize(parent.GetSize())

        # Because of the way the VTK widget is setup, and because we
        # set the size above, the window sizing is usually completely
        # messed up when the application window is shown.  To work
        # around this a dynamic IDLE event handler is added and
        # immediately removed once it executes.  This event handler
        # simply forces a resize to occur.
        def _do_idle(event, window=window):
            # Get the toplevel window.
            w = window
            while w and not w.IsTopLevel():
                w = w.GetParent()
            # Force a resize
            sz = w.GetSize()
            w.SetSize((sz[0]-1, sz[1]-1))
            w.SetSize(sz)
            # Remove the handler.
            wx.EVT_IDLE(window, None)
        
        wx.EVT_IDLE(window, _do_idle)
        
        # Reach in and grab the actual VTK render window.
        render_window = window.GetRenderWindow()

        # Add a renderer!
        self._renderer = tvtk.Renderer()
        render_window.AddRenderer(tvtk.to_vtk(self._renderer))
        
        return window
    
#### EOF ######################################################################
