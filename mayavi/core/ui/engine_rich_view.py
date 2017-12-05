"""A view of the pipeline with a panel to edit objects.

"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traitsui.api import Item, View, HSplit, InstanceEditor
from traitsui.menu import Action, Separator
from pyface.image_resource import ImageResource
from pyface.api import GUI
from mayavi.core.adder_node import SceneAdderNode

# Local imports.
from mayavi.core.scene import Scene
from mayavi.preferences.preference_manager_view import \
    preference_manager_view
from mayavi.core.ui.engine_view import EngineView, \
            EngineViewHandler


class EngineRichViewHandler(EngineViewHandler):
    """ A handler for the EngineRichView object.
    """

    def init_info(self, info):
        """ Informs the handler what the UIInfo object for a View will be.
        Overridden here to add a callback on the creation of the view.

        """
        super(EngineRichViewHandler, self).init_info(info)
        info.on_trait_change(self.select_selected, 'initialized')
        return


    def select_selected(self, initialized):
        """ Force the tree editor to select the current engine selection,
            and eventually collapse other scenes.
        """
        # We need to explore the editors to find the one we are
        # interested in, and to switch its selection to None, and then
        # back to what we are interested in.
        editors = self.info.ui._editors
        if editors is not None:
            for editor in editors:
                if editor.factory is self.info.object.tree_editor:
                    tree_editor = editor
                    break
            else:
                return
        else:
            return

        # We switch the selection to None, but we avoid
        # trait callback, to avoid changing the engine's
        # current_selection.
        tree_editor.trait_set(selected=None, trait_change_notify=False)
        current_selection = self.info.object.engine.current_selection
        GUI.set_trait_later(tree_editor, 'selected', current_selection)

        # If we are selecting a scene, collapse the others
        if isinstance(current_selection, Scene) and \
                                    hasattr(tree_editor._tree, 'Collapse'):
            # The wx editor can collapse, dunno for the Qt
            for scene in self.info.object.engine.scenes:
                if scene is not current_selection:
                    tree_editor._tree.Collapse(
                                            tree_editor._get_object_nid(scene))


    def _on_dclick(self, object):
        """ Called when a node in the tree editor is double-clicked.
        """
        if isinstance(object, SceneAdderNode):
            self.info.object._perform_new_scene()
        else:
            # In this view, we want the dialogs not to be modals, so that
            # the EngineRichView window can be closed while leaving
            # objects dialogs open.
            object.edit_traits(view=object.dialog_view())


##############################################################################
# EngineRichView class.
##############################################################################
class EngineRichView(EngineView):
    """ A view displaying the engine's object tree, alongside with a
        panel to edit the objects.
    """

    ###########################################################################
    # `HasTraits` interface.
    ###########################################################################
    def default_traits_view(self):
        """The default traits view of the Engine View.
        """
        view = View(HSplit(
                        Item('engine',
                            id='mayavi.engine_rich_view.pipeline_view',
                            springy=True,
                            resizable=True,
                            editor=self.tree_editor,
                            dock='tab',
                            label='Pipeline'),
                        Item('engine',
                            id='mayavi.engine_rich_view.current_selection',
                            editor=InstanceEditor(
                                        view='current_selection_view'),
                            springy=True,
                            resizable=True,
                            style='custom'),
                    show_labels=False,
                    id='mayavi.engine_rich_view_group',
                    ),
                    id='mayavi.engine_rich_view',
                    help=False,
                    resizable=True,
                    undo=False,
                    revert=False,
                    ok=False,
                    cancel=False,
                    title='Mayavi pipeline',
                    icon=self.icon,
                    toolbar=self.toolbar,
                    handler=EngineRichViewHandler)
        return view


    def _actions_default(self):
        """ Append a preferences action to the toolbar: this view of the
            engine is meant to be a powerful view giving access to
            all of Mayavi's functionality.
        """
        preferences_action = \
            Action(
                image=ImageResource('preferences.png',
                                     search_path=self._image_path),
                tooltip="Modify Mayavi's preferences",
                checked=False,
                defined_when='True',
                perform=preference_manager_view.dialog_view,
            )

        actions = super(EngineRichView, self)._actions_default()
        actions.extend((Separator(), preferences_action))
        return actions

    ###########################################################################
    # EngineRichView interface.
    ###########################################################################

    def scene_editing_view(self, scene):
        # Selecting an object if good, because it forces the HSplit to
        # choose a sensible split ratio
        for mayavi_scene in self.engine.scenes:
            sc = mayavi_scene.scene
            # Support for the `MlabSceneModel` where the `scene_editor`
            # trait contains the scene.
            s = getattr(sc, 'scene_editor', sc)
            if s is scene:
                self.engine.current_selection = mayavi_scene

        return self.edit_traits()


### EOF ######################################################################
