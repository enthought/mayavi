"""
Custom nodes for a Tree Editor that provide views for adding various nodes
to the tree.
"""
# Authors: Judah De Paula <judah@enthought.com>
#          Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import (HasTraits, Str, Property, Any, Button,
                                  List, Instance, provides,
                                  ToolbarButton)
from traitsui.api import View, Item, Group,\
        TextEditor, TreeEditor, TreeNode, ListEditor, ITreeNode
from pyface.api import ImageResource
from pyface.resource.api import resource_path

# Local imports.
from .registry import registry

###############################################################################
# AdderNode class
###############################################################################
@provides(ITreeNode)
class AdderNode(TreeNode):
    """ Base class that will display a TreeNode to add items to the tree.
    """

    # String to be shown in the TreeEditor.
    label = Str('Base AdderNode')

    # Default tooltip for this class.
    tooltip = Str('Add an item')

    # The parent object that should be manipulated for adding children.
    object =  Any

    # Duck-typing is necessary since Mayavi assumes nodes always have scenes.
    scene = Property

    # Trait view to show in the Mayavi current object panel.
    view = View(Group(label='AdderNode'))

    def dialog_view(self):
        """ View shown by double-clicking on the node.  Same as in Base().
        """
        view = self.trait_view()
        view.buttons = [ ]
        view.title = self.label
        view.icon = ImageResource('add.ico')
        view.resizable = True
        view.width = 350
        view.height = 650
        return view

    def _get_scene(self):
        """ Trait Property getter for 'scene'.
        """
        object = self.object
        if isinstance(object, AdderNode):
            return None
        if object is not None:
            return object.scene
        else:
            return None

    #------------------------------------------------------------------------
    # The ITreeNode interface needed by the Qt tree_editor
    #------------------------------------------------------------------------

    def get_label(self):
        return self.label

    def get_icon(self, obj, is_expanded=False):
        return self.icon_name

    def get_icon_path(self):
        return resource_path()

    def get_tooltip(self):
        return self.tooltip

    def allows_children(self):
        return False

    def get_children_id(self, node=None):
        return []

    def when_label_changed(self, label_updated, remove):
        return

    def when_column_labels_change(self, listener, remove):
        return

###############################################################################
# SceneAdderNode class
###############################################################################
class SceneAdderNode(AdderNode):
    """ Subclass for adding Scene nodes to a Mayavi Engine node.
    """

    # String to be shown in the TreeEditor.
    label = Str('Add a new scene')

    # The name of the icon
    icon_name = Str('add_scene.png')

    # Button for the View.
    add_scene = Button('Add a new scene',
                      image=ImageResource('add_scene.png'))

    # Trait view to show in the Mayavi current object panel.
    view = View(Group(Item('add_scene', show_label=False, style='custom'),
                      label='Add a scene'))


    def _add_scene_fired(self):
        """ Trait handler for when the add_scene button is clicked.
        """
        self.object.new_scene()


###############################################################################
# DocumentedItem class
###############################################################################
class DocumentedItem(HasTraits):
    """ Container to hold a name and a documentation for an action.
    """

    # Name of the action
    name = Str

    # Button to trigger the action
    add = ToolbarButton('Add', orientation='horizontal',
                    image=ImageResource('add.ico'))

    # Object the action will apply on
    object = Any

    # Two lines documentation for the action
    documentation = Str

    view = View('_',
                Item('add', style='custom', show_label=False),
                Item('documentation', style='readonly',
                    editor=TextEditor(multi_line=True),
                    resizable=True,
                    show_label=False),
                )

    def _add_fired(self):
        """ Trait handler for when the add_source button is clicked in
            one of the sub objects in the list.
        """
        action = getattr(self.object.menu_helper, self.id)
        action()


def documented_item_factory(name='', documentation='',
                id='', object=None):
    """ Factory for creating a DocumentedItem with the right button
        label.
    """
    documentation = documentation.replace('\n', '')
    documentation = documentation.replace('  ', '')

    class MyDocumentedItem(DocumentedItem):
        add = ToolbarButton('%s' % name, orientation='horizontal',
                        image=ImageResource('add.ico'))

    return MyDocumentedItem(
                        name=name,
                        documentation=documentation,
                        id=id,
                        object=object)


###############################################################################
# ListAdderNode class
###############################################################################
class ListAdderNode(AdderNode):
    """ A node for adding object, with a list of objects to add generated
        from the registry.
    """

    # The list of items to display to the user.
    items_list = List(DocumentedItem)

    # A reference to the registry, to generate this list.
    items_list_source = List()

    # Selected item
    selected_item = Instance(DocumentedItem)

    # A reference to self, to allow to build the tree view.
    self = Instance(AdderNode)

    # The icon of the displayed objects
    icon_name = Str('add.ico')

    def _self_default(self):
        return self

    def default_traits_view(self):
        nodes = [TreeNode(node_for=[AdderNode],
                          label='name',
                          copy=False,
                          delete=False,
                          rename=False,
                          children='items_list',
                          ),
                 TreeNode(node_for=[DocumentedItem],
                          label='name',
                          copy=False,
                          delete=False,
                          rename=False,
                          icon_item=self.icon_name,
                          ),
                 ]

        tree_editor = TreeEditor(editable=False,
                                 hide_root=True,
                                 orientation='vertical',
                                 selected='object.selected_item',
                                 nodes=nodes,
                                 on_dclick='object._on_tree_dclick',
                                 )

        view = View(Item('self',
                            show_label=False,
                            editor=tree_editor,
                            resizable=True,
                            springy=True,
                            height=0.5),
                    Item('selected_item', style='custom', show_label=False,
                            height=0.5),
                    resizable=True)
        return view


    def _object_changed(self, value):
        """ Trait handler for when the self.object trait changes.
        """
        result = []
        if value is not None:
            # Don't need 'x', but do need to generate the actions.
            x = value.menu_helper.actions
            for src in self.items_list_source:
                if not self._is_action_suitable(value, src):
                    continue
                name = src.menu_name.replace('&','')
                result.append(
                        documented_item_factory(
                                name=name,
                                documentation=src.help,
                                id=src.id,
                                object=value)
                        )
        self.items_list = result


    def _is_action_suitable(self, object, src):
        """ Check that the action described by src can be applied on the
            given object.
        """
        if  hasattr(object.menu_helper, 'check_%s' % src.id) \
                and getattr(object.menu_helper, 'check_%s' % src.id)():
            return True
        else:
            return False

    def _on_tree_dclick(self, object):
        """ Called when an user double clicks on an item in the tree
            view.
        """
        object._add_fired()


###############################################################################
# SourceAdderNode class
###############################################################################
class SourceAdderNode(ListAdderNode):
    """ Tree node that presents a view to the user to add a scene source.
    """

    # Button for adding a data file, with automatic format checking.
    open_file = ToolbarButton('Load data from file',
                                orientation='horizontal',
                                image=ImageResource('file.png'))

    # A reference to the registry, to generate this list.
    items_list_source = [source for source in registry.sources
                         if len(source.extensions) == 0]

    # The string to display on the icon in the TreeEditor.
    label = 'Add Data Source'

    # The icon of the displayed objects
    icon_name = Str('source.ico')

    # Trait view to show in the Mayavi current object panel.
    def default_traits_view(self):
        return View(Group(Group(Item('open_file', style='custom'),
                      show_labels=False, show_border=False),
                      Item('items_list', style='readonly',
                            editor=ListEditor(style='custom')),
                      show_labels=False,
                      label='Add a data source'))

    def _open_file_fired(self):
        """ Trait handler for when the open_file button is clicked.
        """
        self.object.menu_helper.open_file_action()

    def _is_action_suitable(self, object, src):
        return True


###############################################################################
# ModuleAdderNode class
###############################################################################
class ModuleAdderNode(ListAdderNode):
    """ Tree node that presents a view to the user to add modules.
    """
    # String to be shown in the TreeEditor.
    label = Str('Add a visualization module')

    # The icon of the displayed objects
    icon_name = Str('module.ico')

    # A reference to the registry, to generate this list.
    items_list_source = registry.modules

    def _object_changed(self, value):
        if value is not None:
            value.menu_helper._build_filter_actions()
        ListAdderNode._object_changed(self, value)


###############################################################################
# FilterAdderNode class
###############################################################################
class FilterAdderNode(ListAdderNode):
    """ Tree node that presents a view to the user to add filters.
    """
    # String to be shown in the TreeEditor.
    label = Str('Add a processing filter')

    # The icon of the displayed objects
    icon_name = Str('filter.ico')

    # A reference to the registry, to generate this list.
    items_list_source = registry.filters


###############################################################################
# ModuleFilterAdderNode class
###############################################################################
class ModuleFilterAdderNode(AdderNode):
    """ Tree node that presents a view to the user to add filter and
        modules.
    """

    # The string to display on the icon in the TreeEditor.
    label = 'Add module or filter'

    # An adder node for modules
    modules = Instance(ModuleAdderNode, ())

    # An adder node for filters
    filters = Instance(FilterAdderNode, ())

    def _object_changed(self):
        """ Propagate the object to the sub nodes.
        """
        self.filters.object = self.object
        self.modules.object = self.object

    # Trait view to show in the Mayavi current object panel.
    view = View(
                Group(Item('modules', style='custom', springy=True,
                            resizable=True,
                            height=1.,
                            ),
                    show_labels=False,
                    label='Visualization modules'),
                Group(Item('filters', style='custom', springy=True,
                            resizable=True,
                            height=1.,
                            ),
                    show_labels=False,
                    label='Processing filters'),
                )


### EOF #######################################################################
