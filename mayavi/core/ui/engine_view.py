"""The MayaVi view in Envisage.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import join

# Enthought library imports.
from traits.api import Instance, HasTraits, Any, Delegate, \
        List, Either
from traitsui.api import (Item, TreeEditor, TreeNode,
        ObjectTreeNode, View, Handler, UIInfo)
from traitsui.menu import ToolBar, Action, Separator
from pyface.resource.resource_path import resource_path
from pyface.image_resource import ImageResource
from apptools.scripting.api import start_recording, stop_recording

# Local imports.
from mayavi.core.engine import Engine
from mayavi.core.base import Base
from mayavi.core.adder_node import ModuleFilterAdderNode, \
        SourceAdderNode, ModuleAdderNode, FilterAdderNode, \
        SceneAdderNode, AdderNode
from mayavi.action.help import open_help_index, open_tvtk_docs

class EngineViewHandler(Handler):
    """ A handler for the EngineView object.
    """

    info = Instance(UIInfo)

    def init_info(self, info):
        """ Informs the handler what the UIInfo object for a View will be.
        Overridden here to save a reference to the info object.
        """
        self.info = info
        return


    def _on_dclick(self, object):
        """ Called when a node in the tree editor is double-clicked.
        """
        if isinstance(object, SceneAdderNode):
            self.info.object._perform_new_scene()
        else:
            object.edit_traits(view=object.dialog_view(),
                               parent=self.info.ui.control)

    def _on_select(self, object):
        """ Called when a node in the tree editor is selected.
        """
        self.info.object.engine._on_select(object)


class AdderTreeNode(TreeNode):
    """ TreeNode for the adder nodes.
    """

    children=''
    label='label'
    auto_open=True
    copy=False
    delete_me=False
    rename_me=False
    tooltip='tooltip'
    icon_path=resource_path()
    icon_item='add.ico'


##############################################################################
# EngineView class.
##############################################################################
class EngineView(HasTraits):
    """ A view displaying the engine's object tree. """

    # The MayaVi engine we are a view of.
    engine = Instance(Engine, allow_none=True)

    # Path used to search for images
    _image_path = [join(resource_path(), 'images'), ]

    # The icon of the dialog
    icon = ImageResource('mv2.ico', search_path=_image_path)

    # Nodes on the tree.
    nodes = Any

    # TreeEditor
    tree_editor = Instance(TreeEditor)

    # Toolbar
    toolbar = Instance(ToolBar)

    # Toolbar actions.
    actions = List(Either(Action, Separator))

    # Some delegates, for the toolbar to update
    scenes = Delegate('engine')
    current_selection = Delegate('engine')

    ###########################################################################
    # `object` interface.
    ###########################################################################
    def __init__(self, **traits):
        super(EngineView, self).__init__(**traits)


    ###########################################################################
    # `HasTraits` interface.
    ###########################################################################
    def default_traits_view(self):
        """The default traits view of the Engine View.
        """

        view = View(Item(name='engine',
                               id='engine',
                               editor=self.tree_editor,
                               resizable=True,
                               show_label=False),
                    id='mayavi.engine',
                    help=False,
                    resizable=True,
                    scrollable=True,
                    undo=False,
                    revert=False,
                    ok=False,
                    cancel=False,
                    icon=self.icon,
                    title = 'Mayavi pipeline',
                    toolbar=self.toolbar,
                    handler=EngineViewHandler)
        return view


    def _nodes_default(self):
        """ The default value of the cached nodes list.
        """
        # Now setup the view.
        nodes = [TreeNode(node_for=[Engine],
                          children='children_ui_list',
                          label='=Mayavi',
                          auto_open=False,
                          copy=False,
                          delete=False,
                          rename=True,
                          ),
                 ObjectTreeNode(node_for=[Base],
                                children='children_ui_list',
                                label='name',
                                auto_open=True,
                                copy=True,
                                delete=True,
                                rename=True,
                                tooltip='=Right click for more options',
                                ),
                 AdderTreeNode(node_for=[SceneAdderNode],
                               icon_item='add_scene.png',
                               ),
                 AdderTreeNode(node_for=[SourceAdderNode],
                               icon_item='add_source.png',
                               ),
                 AdderTreeNode(node_for=[ModuleFilterAdderNode],
                               icon_item='add_module.png',
                               ),
                 ]
        return nodes


    def _tree_editor_default(self):
        return TreeEditor(editable=False,
                                 hide_root=True,
                                 on_dclick='handler._on_dclick',
                                 on_select='handler._on_select',
                                 orientation='vertical',
                                 selected='object.engine.current_selection',
                                 nodes=self.nodes
                        )

    def _toolbar_default(self):
        toolbar = ToolBar(*self.actions)
        toolbar.image_size = (16, 16)
        toolbar.show_tool_names = False
        toolbar.show_divider = False
        return toolbar

    def _actions_default(self):
        add_scene = \
            Action(
                image=ImageResource('add_scene.png',
                                            search_path=self._image_path),
                tooltip="Create a new scene",
                defined_when='True',
                enabled_when='True',
                perform=self._perform_new_scene,
            )

        add_source = \
            Action(
                image=ImageResource('add_source.png',
                                            search_path=self._image_path),
                tooltip="Add a data source",
                defined_when='True',
                enabled_when='len(scenes) > 0',
                perform=self._perform_add_source,
            )

        add_module = \
            Action(
                image=ImageResource('add_module.png',
                                            search_path=self._image_path),
                tooltip="Add a visualization module",
                defined_when='True',
                # isinstance doesn't work in enabled_when
                enabled_when=\
                    'current_selection is not None and'
                    '( hasattr(current_selection, "output_info")'
                    'or current_selection.__class__.__name__ =='
                    '"ModuleFilterAdderNode")',
                perform=self._perform_add_module,
            )

        add_filter = \
            Action(
                image=ImageResource('add_filter.png',
                                            search_path=self._image_path),
                tooltip="Add a processing filter",
                defined_when='True',
                enabled_when=\
                    'current_selection is not None and'
                    '( ( hasattr(current_selection, "output_info")'
                    ' and not current_selection.type in (" module", '
                    ' " module manager"))'
                    'or current_selection.__class__.__name__ =='
                    '"ModuleFilterAdderNode")',
                perform=self._perform_add_filter,
             )

        help = \
            Action(
                image=ImageResource('help-action.png',
                                            search_path=self._image_path),
                tooltip="Help on the Mayavi pipeline",
                defined_when='True',
                enabled_when='True',
                perform=open_help_index,
            )

        tvtk_docs = \
            Action(
                image=ImageResource('reader.png',
                                            search_path=self._image_path),
                tooltip="Search the VTK class browser",
                defined_when='True',
                enabled_when='True',
                perform=open_tvtk_docs,
            )

        record = \
            Action(
                image=ImageResource('record.png',
                                     search_path=self._image_path),
                tooltip="Start/Stop script recording",
                style='toggle',
                checked=False,
                defined_when='True',
                enabled_when='engine is not None',
                perform=self._perform_record,
            )

        # Check the record icon if the engine already has a recorder
        # set.
        if self.engine is not None and self.engine.recorder is not None:
            record.checked = True

        return [tvtk_docs, Separator(), add_scene, add_source, add_module,
                add_filter, Separator(), help, record]


    ###########################################################################
    # Private interface.
    ###########################################################################
    def _perform_new_scene(self):
        self.engine.new_scene()
        self.engine.current_selection = self.engine.current_scene

    def _perform_add_source(self):
        adder = SourceAdderNode(object=self.engine.current_scene)
        adder.edit_traits(view=adder.dialog_view())


    def _perform_add_module(self):
        object = self.engine.current_selection
        if isinstance(object, AdderNode):
            object = object.object
        adder = ModuleAdderNode(object=object)
        adder.edit_traits(view=adder.dialog_view())

    def _perform_add_filter(self):
        object = self.engine.current_selection
        if isinstance(object, AdderNode):
            object = object.object
        adder = FilterAdderNode(object=object)
        adder.edit_traits(view=adder.dialog_view())

    def _perform_record(self):
        e = self.engine
        if e.recorder is None:
            start_recording(e, known=True, script_id='engine')
        else:
            stop_recording(e, save=False)

    def _recorder_changed_for_engine(self, recorder):
        """Called when the recorder trait on the engine trait of this
        object changes.

        This basically toggles the recording action when someone
        attaches a recorder to the engine.
        """
        record_action = None
        for action in self.actions:
            if hasattr(action, 'tooltip') and \
               action.tooltip.endswith('recording'):
                record_action = action
                break

        if record_action is not None:
            if recorder is not None:
                record_action.checked = True
            else:
                record_action.checked = False


### EOF ######################################################################
