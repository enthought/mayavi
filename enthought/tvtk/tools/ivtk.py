#!/usr/bin/env python
"""ivtk - Interactive TVTK.

A utility module that makes VTK/TVTK easier to use from the Python
interpreter.  For a standalone application simply run this file.  To
use this under IPython (with -wthread) use the `viewer()` helper
function or use the `IVTK` class.  The widget can also make use of the
tvtk pipeline browser.

Here is example usage of the viewer along with tvtk under IPython:

    >>> from enthought.tvtk.tools import ivtk
    >>> from enthought.tvtk.api import tvtk
    >>> cs = tvtk.ConeSource()
    >>> m = tvtk.PolyDataMapper()
    >>> m.input = cs.output
    >>> a = tvtk.Actor()
    >>> a.mapper = m
    >>> v = ivtk.viewer()
    >>> v.scene.add_actors(a)
    >>> v.scene.reset_zoom()

"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import os
import os.path

import wx

# Enthought library imports.
from enthought.pyface.api import GUI, PythonShell
from enthought.pyface.api import SplitApplicationWindow, ApplicationWindow
from enthought.pyface.split_widget import SplitWidget
from enthought.pyface.tvtk.decorated_scene import Scene, DecoratedScene
from enthought.pyface.action.api import Action, Group, MenuBarManager,\
     MenuManager, Separator

from enthought.traits.api import Float, Str, Instance, Trait

from enthought.tvtk.api import tvtk

from enthought.tvtk.pipeline.browser import PipelineBrowser


######################################################################
# `ExitAction` class.
######################################################################
class ExitAction(Action):
    """ Exits the application. """
    def __init__(self, window):
        """ Creates a new action. """
        self._window = window
        self.name = "E&xit"

    def perform(self):
        """ Performs the action. """
        self._window.close()


######################################################################
# `SaveImageAction` class.
######################################################################
class SaveImageAction(Action):
    """Saves the rendered scene to an image."""
    def __init__(self, window):
        self._window = window
        self.name = "S&ave Scene"

    def perform(self):
        """Pops up a dialog used to save the scene to an image."""
        extns = ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.bmp', '*.ps', '*.eps',
                 '*.tex', '*.rib', '*.wrl', '*.oogl', '*.pdf', '*.vrml', '*.obj',
                 '*.iv']
        dlg = wx.FileDialog(self._window.control, style=wx.SAVE,
                            wildcard='|'.join(extns),
                            message="Save scene to image")
        rc = (dlg.ShowModal() == wx.ID_OK)
        filename = os.path.abspath(dlg.GetPath())
        dlg.Destroy()
        if rc:
            self._window.scene.save(filename)


######################################################################
# `SaveToClipboardAction` class.
######################################################################
class SaveToClipboardAction(Action):
    """ Saves rendered scene to the Clipboard. """
    def __init__(self, window):
        """ Creates a new action. """
        self._window = window
        self.name = "&Copy"

    def perform(self):
        """ Performs the action. """
        self._window.scene.save_to_clipboard()
        

######################################################################
# `SpecialViewAction` class.
######################################################################
class SpecialViewAction(Action):
    """Sets the scene to a particular view."""
    def __init__(self, window, name, view):
        """ Creates a new action. """
        self._window = window
        self.name = name
        self.view = view

    def perform(self):
        """ Performs the action. """
        # Hack!  Works tho.
        try:
            meth = getattr(self._window.scene, self.view)
            meth()
        except AttributeError:
            pass    


def create_ivtk_menu(obj):
    """Creates a menu bar suitable for all IVTK windows.

    Parameters
    ----------

    - obj : A Pyface application window.

      This is the window which requires the menu items.
    """
    
    menu_bar_manager = MenuBarManager(
        MenuManager(SaveImageAction(obj),
                    Separator(),
                    ExitAction(obj),
                    name = '&File',
                    ),
        MenuManager(SaveToClipboardAction(obj),
                    name = '&Edit',
                    ),
        MenuManager(SpecialViewAction(obj, "&Reset Zoom", 'reset_zoom'),
                    Separator(),
                    SpecialViewAction(obj, "&Isometric", 'isometric_view'),
                    SpecialViewAction(obj, "&X positive", 'x_plus_view'),
                    SpecialViewAction(obj, "X negative", 'x_minus_view'),
                    SpecialViewAction(obj, "&Y positive", 'y_plus_view'),
                    SpecialViewAction(obj, "Y negative", 'y_minus_view'),
                    SpecialViewAction(obj, "&Z positive", 'z_plus_view'),
                    SpecialViewAction(obj, "Z negative", 'z_minus_view'),
                    name = '&View',
                    )
        )
    return menu_bar_manager


######################################################################
# `OrderedSplitWidget` class.
######################################################################
class OrderedSplitWidget(SplitWidget):

    # Specifies the creation order of the lhs and rhs.
    creation_order = Trait("left-right", "left-right", "right-left")

    def _create_splitter(self, parent):
        """ Create the toolkit-specific control that represents the widget. """

        sizer = wx.BoxSizer(wx.VERTICAL)
        splitter = wx.SplitterWindow(parent, -1, style=wx.CLIP_CHILDREN)
        splitter.SetSizer(sizer)
        splitter.SetAutoLayout(True)

        # If we don't set the minimum pane size, the user can drag the sash and
        # make one pane disappear!
        splitter.SetMinimumPaneSize(50)

        if self.creation_order == "left-right":
            # Left hand side/top.
            lhs = self._create_lhs(splitter)
            sizer.Add(lhs, 1, wx.EXPAND)

            # Right hand side/bottom.
            rhs = self._create_rhs(splitter)
            sizer.Add(rhs, 1, wx.EXPAND)
        else:
            # Right hand side/bottom.
            rhs = self._create_rhs(splitter)
            sizer.Add(rhs, 1, wx.EXPAND)

            # Left hand side/top.
            lhs = self._create_lhs(splitter)
            sizer.Prepend(lhs, 1, wx.EXPAND)
        
        # Resize the splitter to fit the sizer's minimum size.
        sizer.Fit(splitter)

        # Split the window in the appropriate direction.
        #
        # fixme: Notice that on the initial split, we DON'T specify the split
        # ratio.  If we do then sadly, wx won't let us move the sash 8^()
        if self.direction == 'vertical':
            splitter.SplitVertically(lhs, rhs)

        else:
            splitter.SplitHorizontally(lhs, rhs)

        # We respond to the FIRST size event to make sure that the split ratio
        # is correct when the splitter is laid out in its parent.
        wx.EVT_SIZE(splitter, self._on_size)

        return splitter


######################################################################
# `SceneWithBrowser` class.
######################################################################
class SceneWithBrowser(OrderedSplitWidget):
    """ Provides an Scene along with an embedded PyCrust Python shell.
    In the shell, 'scene' and 's' are bound to the Scene."""

    # The ratio of the size of the left/top pane to the right/bottom pane.
    ratio = Float(0.3)

    # The direction in which the panel is split.
    direction = Str('vertical')

    # Creation order of widget.
    creation_order = Str('right-left')

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    # The `PythonShell` instance.
    browser = Instance(PipelineBrowser)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, parent, **traits):
        """ Creates a new window. """
        # Base class constructor.
        super(SceneWithBrowser, self).__init__(**traits)
        # Create the control.
        self.control = self._create_splitter(parent)

    ###########################################################################
    # Protected 'OrderedSplitWidget' interface.
    ###########################################################################
    def _create_lhs(self, parent):
        """ Creates the left hand side or top depending on the style. """
        self.browser = PipelineBrowser(self.scene)
        self.browser.show(parent=parent)
        return self.browser.ui.control

    def _create_rhs(self, parent):
        """ Creates the right hand side or bottom depending on the
        style.  's' and 'scene' are bound to the Scene instance."""
        self.scene = DecoratedScene(parent)
        self.scene.renderer.background = 0.5, 0.5, 0.5        
        return self.scene.control



######################################################################
# `IVTKWithCrust` class.
######################################################################
class IVTKWithCrust(SplitApplicationWindow):
    """ Provides an Scene along with an embedded PyCrust Python shell.
    In the shell, 'scene' and 's' are bound to the Scene."""

    # The ratio of the size of the left/top pane to the right/bottom pane.
    ratio = Float(0.7)

    # The direction in which the panel is split.
    direction = Str('horizontal')

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    # The `PythonShell` instance.
    python_shell = Instance(PythonShell)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, **traits):
        """ Creates a new window. """

        # Base class constructor.
        super(IVTKWithCrust, self).__init__(**traits)
        self.title = 'Interactive TVTK'
        # Create the window's menu bar.
        self.menu_bar_manager = create_ivtk_menu(self)


    ###########################################################################
    # Protected 'SplitApplicationWindow' interface.
    ###########################################################################
    def _create_lhs(self, parent):
        """ Creates the left hand side or top depending on the style. """

        self.scene = DecoratedScene(parent)
        self.scene.renderer.background = 0.5, 0.5, 0.5        
        return self.scene.control

    def _create_rhs(self, parent):
        """ Creates the right hand side or bottom depending on the
        style.  's' and 'scene' are bound to the Scene instance."""

        self.python_shell = PythonShell(parent)
        self.python_shell.bind('scene', self.scene)
        self.python_shell.bind('s', self.scene)
        self.python_shell.bind('tvtk', tvtk)
        
        return self.python_shell.control


######################################################################
# `IVTKWithCrustAndBrowser` class.
######################################################################
class IVTKWithCrustAndBrowser(SplitApplicationWindow):
    """ Provides an Scene along with an embedded PyCrust Python shell.
    In the shell, 'scene' and 's' are bound to the Scene."""

    # The ratio of the size of the left/top pane to the right/bottom pane.
    ratio = Float(0.7)

    # The direction in which the panel is split.
    direction = Str('horizontal')

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    # The `PipelineBrowser` instance.
    browser = Instance(PipelineBrowser)

    # The ordered split window to use.
    browser_scene = Instance(SceneWithBrowser)

    # The `PythonShell` instance.
    python_shell = Instance(PythonShell)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, **traits):
        """ Creates a new window. """

        # Base class constructor.
        super(IVTKWithCrustAndBrowser, self).__init__(**traits)
        self.title = 'Interactive TVTK'
        # Create the window's menu bar.
        self.menu_bar_manager = create_ivtk_menu(self)


    ###########################################################################
    # Protected 'SplitApplicationWindow' interface.
    ###########################################################################
    def _create_lhs(self, parent):
        """ Creates the left hand side or top depending on the style. """
        self.browser_scene = SceneWithBrowser(parent)
        self.scene = self.browser_scene.scene
        self.browser = self.browser_scene.browser
        return self.browser_scene.control

    def _create_rhs(self, parent):
        """ Creates the right hand side or bottom depending on the
        style.  's' and 'scene' are bound to the Scene instance."""

        self.python_shell = PythonShell(parent)
        self.python_shell.bind('scene', self.scene)
        self.python_shell.bind('s', self.scene)
        self.python_shell.bind('browser', self.browser)
        self.python_shell.bind('b', self.browser)
        self.python_shell.bind('tvtk', tvtk)
        
        return self.python_shell.control


######################################################################
# `IVTK` class.
######################################################################
class IVTK(ApplicationWindow):
    """ Provides an Scene along without an embedded Python shell.
    This is useful when scripting from the vanilla Python or IPython
    interpreter."""

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, **traits):
        """ Creates a new application window. """

        # Base class constructor.
        super(IVTK, self).__init__(**traits)
        self.title = 'Interactive TVTK'
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # Protected 'ApplicationWindow' interface.
    ###########################################################################
    def _create_contents(self, parent):
        """ Create the contents of the window. """

        self.scene = DecoratedScene(parent)
        self.scene.renderer.background = 0.5, 0.5, 0.5

        return self.scene.control
    
######################################################################
# `IVTKWithBrowser` class.
######################################################################
class IVTKWithBrowser(ApplicationWindow):
    """ Provides an Scene along without an embedded Python shell.
    This is useful when scripting from the vanilla Python or IPython
    interpreter."""

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    # The `PipelineBrowser` instance.
    browser = Instance(PipelineBrowser)

    # The ordered split window to use.
    browser_scene = Instance(SceneWithBrowser)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, **traits):
        """ Creates a new application window. """

        # Base class constructor.
        super(IVTKWithBrowser, self).__init__(**traits)
        self.title = 'Interactive TVTK'
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # Protected 'ApplicationWindow' interface.
    ###########################################################################
    def _create_contents(self, parent):
        """ Create the contents of the window. """

        self.browser_scene = SceneWithBrowser(parent)
        self.scene = self.browser_scene.scene
        self.browser = self.browser_scene.browser
        return self.browser_scene.control


######################################################################
# Utility functions.
######################################################################
def viewer(browser=True, instantiate_gui=False):
    """Creates an IVTK instance, opens the window and returns the
    embedded scene inside it.  This is useful from an IPython/vanilla
    Python shell.  It returns the viewer window instance.

    Parameters
    ----------

    - browser : `bool` (default, True)
    
      If True, creates an IVTK scene with an embedded PipelineBrowser.
      If False, does not create it.

    - instantiate_gui : `bool` (default: False)

      If True, create an instance of GUI().  This is useful when this
      function is invoked from within an IPython shell.  OTOH, if this
      is called from within a wxPython app (or with ipython -wthread)
      you don't want to start another GUI instance.
    """
    if instantiate_gui:
        gui = GUI()
    if browser:
        v = IVTKWithBrowser(size=(600,600))
    else:
        v = IVTK(size=(600,600))
    v.open()
    return v


def main():
    # Create the GUI.
    gui = GUI()
    # Create and open an application window.
    window = IVTKWithCrustAndBrowser(size=(800,600))
    window.open()
    # Start the GUI event loop!
    gui.start_event_loop()
    

if __name__ == '__main__':
    main()
