"""A VTK interactor scene which provides a convenient toolbar that
allows the user to set the camera view, turn on the axes indicator
etc.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>,
#          Dave Peterson <dpeterson@enthought.com>
# Copyright (c) 2006-2016, Enthought, Inc.
# License: BSD Style.

# System imports.
from os.path import dirname

import os
from pyface.qt import QtGui

# Enthought library imports.
from pyface.api import ImageResource
from pyface.action.api import ToolBarManager, Group, Action
from tvtk.api import tvtk
from traits.api import Instance, false, Either, List

# Local imports.
from .scene import Scene, popup_save


###########################################################################
# 'DecoratedScene' class
###########################################################################
class DecoratedScene(Scene):
    """A VTK interactor scene which provides a convenient toolbar that
    allows the user to set the camera view, turn on the axes indicator
    etc.
    """
    #######################################################################
    # Traits
    #######################################################################

    if hasattr(tvtk, 'OrientationMarkerWidget'):
        # The tvtk orientation marker widget.  This only exists in VTK
        # 5.x.
        marker = Instance(tvtk.OrientationMarkerWidget, ())

        # The tvtk axes that will be shown for the orientation.
        axes = Instance(tvtk.AxesActor, ())
    else:
        marker = None
        axes = None

    # Determine if the orientation axis is shown or not.
    show_axes = false

    # The list of actions represented in the toolbar
    actions = List(Either(Action, Group))

    ##########################################################################
    # `object` interface
    ##########################################################################
    def __init__(self, parent, **traits):
        super(DecoratedScene, self).__init__(parent, **traits)
        self._setup_axes_marker()

    def __get_pure_state__(self):
        """Allows us to pickle the scene."""
        # The control attribute is not picklable since it is a VTK
        # object so we remove it.
        d = super(DecoratedScene, self).__get_pure_state__()
        for x in ['_content', '_panel', '_tool_bar', 'actions']:
            d.pop(x, None)
        return d

    ##########################################################################
    # Non-public interface.
    ##########################################################################
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the widget.

            Overridden to wrap the Scene control within a panel that
            also contains a toolbar.
        """
        # Create a panel as a wrapper of the scene toolkit control.  This
        # allows us to also add additional controls.
        self._panel = QtGui.QMainWindow()

        # Add our toolbar to the panel.
        tbm = self._get_tool_bar_manager()
        self._tool_bar = tbm.create_tool_bar(self._panel)
        self._panel.addToolBar(self._tool_bar)

        # Create the actual scene content
        self._content = super(DecoratedScene, self)._create_control(self._panel)
        self._panel.setCentralWidget(self._content)

        return self._panel

    def _setup_axes_marker(self):
        axes = self.axes
        if axes is None:
            # For VTK versions < 5.0.
            return

        axes.trait_set(
            normalized_tip_length=(0.4, 0.4, 0.4),
            normalized_shaft_length=(0.6, 0.6, 0.6),
            shaft_type='cylinder'
            )

        p = axes.x_axis_caption_actor2d.caption_text_property
        axes.y_axis_caption_actor2d.caption_text_property = p
        axes.z_axis_caption_actor2d.caption_text_property = p
        p.trait_set(color=(1,1,1), shadow=False, italic=False)
        self._background_changed(self.background)

        self.marker.trait_set(key_press_activation=False)
        self.marker.orientation_marker = axes

    def _get_tool_bar_manager(self):
        """ Returns the tool_bar_manager for this scene.
        """
        tbm = ToolBarManager( *self.actions )
        return tbm


    def _get_image_path(self):
        """Returns the directory which contains the images used by the
        toolbar."""

        # So that we can find the images.
        import tvtk.pyface.api

        return dirname(tvtk.pyface.api.__file__)

    def _toggle_projection(self):
        """ Toggle between perspective and parallel projection, this
        is used for the toolbar.
        """
        if self._panel is not None:
            self.parallel_projection = not self.parallel_projection

    def _toggle_axes(self, *args):
        """Used by the toolbar to turn on/off the axes indicator.
        """
        if self._panel is not None:
            self.show_axes = not self.show_axes

    def _save_snapshot(self):
        """Invoked by the toolbar menu to save a snapshot of the scene
        to an image.  Note that the extension of the filename
        determines what image type is saved.  The default is PNG.
        """
        if self._panel is not None:
            path = popup_save(self._panel)
            if len(path) > 0:
                # The extension of the path will determine the actual
                # image type saved.
                self.save(path)

    def _configure_scene(self):
        """Invoked when the toolbar icon for configuration is clicked.
        """
        self.edit_traits()

    ######################################################################
    # Trait handlers.
    ######################################################################
    def _show_axes_changed(self):
        marker = self.marker
        if (self._vtk_control is not None) and (marker is not None):
            if not self.show_axes:
                marker.interactor = None
                marker.enabled = False
            else:
                marker.interactor = self.interactor
                marker.enabled = True
            self.render()

    def _background_changed(self, value):
        # Depending on the background, this sets the axes text and
        # outline color to something that should be visible.
        axes = self.axes
        if (self._vtk_control is not None) and (axes is not None):
            p = self.axes.x_axis_caption_actor2d.caption_text_property
            m = self.marker
            s = value[0] + value[1] + value[2]
            if s <= 1.0:
                p.color = (1,1,1)
                m.set_outline_color(1,1,1)
            else:
                p.color = (0,0,0)
                m.set_outline_color(0,0,0)
            self.render()

    def _actions_default(self):
        return [
            Group(
                Action(
                    image = ImageResource('16x16/x-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the -X axis",
                    on_perform = self.x_minus_view,
                    ),
                Action(
                    image = ImageResource('16x16/x-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the +X axis",
                    on_perform = self.x_plus_view,
                    ),
                Action(
                    image = ImageResource('16x16/y-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the -Y axis",
                    on_perform = self.y_minus_view,
                    ),
                Action(
                    image = ImageResource('16x16/y-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the +Y axis",
                    on_perform = self.y_plus_view,
                    ),
                Action(
                    image = ImageResource('16x16/z-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the -Z axis",
                    on_perform = self.z_minus_view,
                    ),
                Action(
                    image = ImageResource('16x16/z-axis',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "View along the +Z axis",
                    on_perform = self.z_plus_view,
                    ),
                Action(
                    image = ImageResource('16x16/isometric',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "Obtain an isometric view",
                    on_perform = self.isometric_view,
                    ),
                ),
            Group(
                Action(
                    image = ImageResource('16x16/parallel',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = 'Toggle parallel projection',
                    style="toggle",
                    on_perform = self._toggle_projection,
                    checked = self.parallel_projection,
                    ),
                Action(
                    image = ImageResource('16x16/origin_glyph',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = 'Toggle axes indicator',
                    style="toggle",
                    enabled=(self.marker is not None),
                    on_perform = self._toggle_axes,
                    checked = self.show_axes,
                    ),
                Action(
                    image = ImageResource('16x16/fullscreen',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = 'Full Screen (press "q" or "e" or Esc to exit fullscreen)',
                    style="push",
                    on_perform = self._full_screen_fired,
                    ),
                ),
            Group(
                Action(
                    image = ImageResource('16x16/save',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = "Save a snapshot of this scene",
                    on_perform = self._save_snapshot,
                    ),
                Action(
                    image = ImageResource('16x16/configure',
                        search_path = [self._get_image_path()],
                        ),
                    tooltip = 'Configure the scene',
                    style="push",
                    on_perform = self._configure_scene,
                    ),
                ),
            ]
