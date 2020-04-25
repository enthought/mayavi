"""ivtk - Interactive TVTK.

A utility module that makes VTK/TVTK easier to use from the Python
interpreter.  For a standalone application simply run this file.  To
use this under IPython (with --gui=qt) use the `viewer()` helper
function or use the `IVTK` class.  The widget can also make use of the
tvtk pipeline browser.

Here is example usage of the viewer along with tvtk under IPython:

    >>> from tvtk.tools import ivtk
    >>> from tvtk.api import tvtk
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
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import os.path

# Enthought library imports.
from pyface.api import FileDialog, GUI, OK, PythonShell
from pyface.api import SplitApplicationWindow, ApplicationWindow
from pyface.api import SplitPanel
from tvtk.pyface.api import Scene, DecoratedScene
from pyface.action.api import Action, MenuBarManager,\
     MenuManager, Separator
from pyface.image_resource import ImageResource
from pyface.resource.api import resource_path

from traits.api import Float, Str, Instance, Callable

from tvtk.api import tvtk

from tvtk.pipeline.browser import PipelineBrowser

######################################################################
# The scene icon.
######################################################################
def mk_scene_icon():
    icon_path = os.path.join(resource_path(), 'images', 'scene.ico')
    return ImageResource(icon_path)

scene_icon = mk_scene_icon()

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
        extensions = ['*.png', '*.jpg', '*.tiff', '*.bmp', '*.ps',
                      '*.eps', '*.pdf', '*.tex', '*.rib', '*.wrl',
                      '*.oogl', '*.vrml', '*.obj', '*.iv', '*.pov',
                      '*.x3d']
        descriptions = ["PNG", "JPG", "TIFF", "Bitmap", "PostScript",
                        "EPS", "PDF", "Tex", "RIB", "WRL",
                        "Geomview", "VRML", "Wavefront", "Open Inventor",
                        "Povray", "X3D"]
        wildcard = ""
        for description, extension in zip(descriptions, extensions):
            wildcard += "{} ({})|{}|".format(description,
                                             extension,
                                             extension)
        wildcard += "Determine by extension (*.*)|(*.*)"

        dlg = FileDialog(parent=self._window.control, action='save as',
                wildcard=wildcard, title="Save scene to image")
        if dlg.open() == OK:
            self._window.scene.save(dlg.path)


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
# `SceneWithBrowser` class.
######################################################################
class SceneWithBrowser(SplitPanel):
    """ Provides an Scene along with an embedded PyCrust Python shell.
    In the shell, 'scene' and 's' are bound to the Scene."""

    # The ratio of the size of the left/top pane to the right/bottom pane.
    ratio = Float(0.3)

    # The direction in which the panel is split.
    direction = Str('vertical')

    # The `Scene` instance into which VTK renders.
    scene = Instance(Scene)

    # The `PythonShell` instance.
    browser = Instance(PipelineBrowser)

    ###########################################################################
    # `IWidget` interface.
    ###########################################################################
    def destroy(self):
        if self.scene is not None:
            self.scene.close()
        super(SceneWithBrowser, self).destroy()

    ###########################################################################
    # Protected 'SplitPanel' interface.
    ###########################################################################
    def _create_lhs(self, parent):
        """ Creates the left hand side or top depending on the style. """
        self._create_scene(parent)
        self.browser = PipelineBrowser(self.scene)
        if parent is not None:
            parent.show()
        self.browser.show(parent=parent)
        return self.browser._ui.control

    def _create_rhs(self, parent):
        """ Creates the right hand side or bottom depending on the
        style.  's' and 'scene' are bound to the Scene instance."""
        self._create_scene(parent)
        self.scene.renderer.background = 0.5, 0.5, 0.5
        return self.scene.control

    ###########################################################################
    # Private 'SceneWithBrowser' interface.
    ###########################################################################
    def _create_scene(self, parent):
        """ Make sure that the scene has been created. """
        if self.scene is None:
            self.scene = DecoratedScene(parent)


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
        self.title = 'TVTK Scene'
        # Create the window's menu bar.
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # `IWindow` interface.
    ###########################################################################
    def close(self):
        if self.scene is not None:
            self.scene.close()
        super(IVTKWithCrust, self).close()

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
        self.title = 'TVTK Scene'
        # Create the window's menu bar.
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # `IWindow` interface.
    ###########################################################################
    def close(self):
        if self.scene is not None:
            self.scene.close()
        super(IVTKWithCrustAndBrowser, self).close()

    ###########################################################################
    # Protected 'SplitApplicationWindow' interface.
    ###########################################################################

    # The icon of the window
    icon = Instance(ImageResource, scene_icon)

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

    # The callable (or class) to create the scene instance
    _scene_factory = Callable(DecoratedScene)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, **traits):
        """ Creates a new application window. """

        # Base class constructor.
        super(IVTK, self).__init__(**traits)
        self.title = 'TVTK Scene'
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # `IWindow` interface.
    ###########################################################################
    def close(self):
        if self.scene is not None:
            self.scene.close()
        super(IVTK, self).close()

    ###########################################################################
    # Protected 'ApplicationWindow' interface.
    ###########################################################################

    # The icon of the window
    icon = Instance(ImageResource, scene_icon)

    def _create_contents(self, parent):
        """ Create the contents of the window. """

        self.scene = self._scene_factory(parent)

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
        self.title = 'TVTK Scene'
        self.menu_bar_manager = create_ivtk_menu(self)

    ###########################################################################
    # `IWindow` interface.
    ###########################################################################
    def close(self):
        if self.scene is not None:
            self.scene.close()
        super(IVTKWithBrowser, self).close()

    ###########################################################################
    # Protected 'ApplicationWindow' interface.
    ###########################################################################

    # The icon of the window
    icon = Instance(ImageResource, scene_icon)

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
      is called from within a wxPython app (or with ipython --gui=qt)
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
