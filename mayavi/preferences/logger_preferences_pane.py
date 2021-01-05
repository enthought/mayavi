"""Logger Preferences for Mayavi
"""
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from apptools.preferences.api import PreferencesHelper
from traits.api import (Bool, Enum, Tuple, Range, List,
        Str, Instance, HasTraits)
from traitsui.api import View, Group, InstanceEditor, Item, EnumEditor
from envisage.ui.tasks.api import PreferencesPane
        
from mayavi.preferences.api import preference_manager

from apptools.logger.plugin.logger_preferences import LoggerPreferences

class LoggerPreferencesPane(PreferencesPane):

    #### 'Controller' interface ###############################################

    #: The preferences helper for which this pane is a view.
    model = Instance(PreferencesHelper)

    #### 'PreferencesPane' interface ##########################################

    #: An identifier for the pane (unique within a category).
    id = Str("Logger")

    #: The ID of the category in which to place the pane.
    category = Str("Logger")

    #: The pane appears after the pane with this ID.
    before = Str

    #: The pane appears after the pane with this ID.
    after = Str

    def _model_default(self):
        return LoggerPreferences()

    traits_view = View(
        Group(
            Group(
                Item(
                    name="level",
                    editor=EnumEditor(
                        values={
                            "Debug": "1:Debug",
                            "Info": "2:Info",
                            "Warning": "3:Warning",
                            "Error": "4:Error",
                            "Critical": "5:Critical",
                        },
                    ),
                    style="simple",
                ),
                label="Logger Settings",
                show_border=True,
            ),
            Group(Item(name="10")),
            Group(
                Group(
                    Group(
                        Item(
                            name="enable_agent", label="Enable quality agent"
                        ),
                        show_left=False,
                    ),
                    Group(
                        Item(name="smtp_server", label="SMTP server"),
                        Item(name="from_address"),
                        Item(name="to_address"),
                        enabled_when="enable_agent==True",
                    ),
                ),
                label="Quality Agent Settings",
                show_border=True,
            ),
        ),
    )