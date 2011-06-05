#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" An example of using a TVTK scene. """


# Standard library imports.
import random

# Enthought library imports.
from pyface.api import FileDialog
from pyface.api import GUI
from pyface.api import OK
from pyface.api import PythonShell
from pyface.api import SplitApplicationWindow
from tvtk.pyface.api import Scene
from tvtk.pyface.actors import arrow_actor, axes_actor, cone_actor, \
                                         cube_actor, cylinder_actor, \
                                         earth_actor, sphere_actor
from pyface.action.api import Action, Group, MenuBarManager, \
                                        MenuManager, Separator

from traits.api import Float, Str, Instance


class ExitAction(Action):
    """ Exits the application. """
    def __init__(self, window):
        """ Creates a new action. """
        self._window = window
        self.name = "E&xit"

    def perform(self):
        """ Performs the action. """
        self._window.close()


class SaveImageAction(Action):
    """Saves the rendered scene to an image."""
    def __init__(self, window):
        self._window = window
        self.name = "S&ave Scene"

    def perform(self):
        """Pops up a dialog used to save the scene to an image."""
        extns = ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.bmp', '*.ps',
                 '*.eps', '*.tex', '*.rib', '*.wrl', '*.oogl', '*.pdf',
                 '*.vrml', '*.obj', '*.iv']
        dlg = FileDialog(parent=self._window.control, action='save as',
                wildcard='|'.join(extns), title="Save scene to image")
        if dlg.open() == OK:
            self._window.scene.save(dlg.path)


class SaveToClipboardAction(Action):
    """ Saves rendered scene to the Clipboard. """
    def __init__(self, window):
        """ Creates a new action. """
        self._window = window
        self.name = "&Copy"

    def perform(self):
        """ Performs the action. """
        self._window.scene.save_to_clipboard()


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


class ExampleWindow(SplitApplicationWindow):
    """ An example application window. """

    # The actors we can create.
    ACTORS = [
        arrow_actor, axes_actor, cone_actor, cube_actor, cylinder_actor,
        earth_actor, sphere_actor
    ]

    # The ratio of the size of the left/top pane to the right/bottom pane.
    ratio = Float(0.75)

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
        super(ExampleWindow, self).__init__(**traits)

        # Create the window's menu bar.
        self._create_my_menu_bar()


    ###########################################################################
    # Protected 'SplitApplicationWindow' interface.
    ###########################################################################

    def _create_lhs(self, parent):
        """ Creates the left hand side or top depending on the style. """

        self.scene = Scene(parent)
        self.scene.renderer.background = 0.1, 0.2, 0.4

        # Add some actors.
        for i in range(10):
            func = random.choice(ExampleWindow.ACTORS)
            actor = func()

            # Place the actor randomly.
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            z = random.uniform(-3, 3)

            actor.position = x, y, z

            # Add the actor to the scene.
            self.scene.add_actors(actor)

        # Render it all!
        self.scene.render()

        # Reset the zoom nicely.
        self.scene.reset_zoom()

        return self.scene.control

    def _create_rhs(self, parent):
        """ Creates the right hand side or bottom depending on the style. """

        self.python_shell = PythonShell(parent)
        self.python_shell.bind('scene', self.scene)
        self.python_shell.bind('s', self.scene)

        return self.python_shell.control


    ###########################################################################
    # Private interface.
    ###########################################################################

    def _create_my_menu_bar(self):
        """ Creates the window's menu bar. """

        self.menu_bar_manager = MenuBarManager(
            MenuManager(
                SaveImageAction(self),
                Separator(),
                ExitAction(self),
                name = '&File',
            ),
            MenuManager(
                SaveToClipboardAction(self),
                name = '&Edit',
            ),
            MenuManager(
                SpecialViewAction(self, "&Reset Zoom", 'reset_zoom'),
                Separator(),
                SpecialViewAction(self, "&Isometric", 'isometric_view'),
                SpecialViewAction(self, "&X positive", 'x_plus_view'),
                SpecialViewAction(self, "X negative", 'x_minus_view'),
                SpecialViewAction(self, "&Y positive", 'y_plus_view'),
                SpecialViewAction(self, "Y negative", 'y_minus_view'),
                SpecialViewAction(self, "&Z positive", 'z_plus_view'),
                SpecialViewAction(self, "Z negative", 'z_minus_view'),
                name = '&View',
            )
        )



# Application entry point.
if __name__ == '__main__':
    # Create the GUI.
    gui = GUI()

    # Create and open an application window.
    window = ExampleWindow(size=(600,600))
    window.open()

    # Start the GUI event loop!
    gui.start_event_loop()

##### EOF #####################################################################
