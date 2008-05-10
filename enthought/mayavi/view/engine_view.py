"""The MayaVi view in Envisage.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import join

# Enthought library imports.
from enthought.traits.api import Instance, HasTraits
from enthought.traits.ui.api import \
     Group, Item, TreeEditor, TreeNode, ObjectTreeNode, View
from enthought.resource.resource_path import resource_path
from enthought.pyface.image_resource import ImageResource

# Local imports.
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.core.base import Base

##############################################################################
# EngineView class.
##############################################################################
class EngineView(HasTraits):
    """ A view displaying the engine's object tree. """

    # The MayaVi engine we are a view of.
    engine = Instance(Engine, allow_none=True)

    icon = ImageResource(join(resource_path(), 'images', 'mv2.ico'))

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
        # Now setup the view.
        nodes = [TreeNode(node_for=[Engine],
                          children='scenes',
                          label='name',
                          auto_open=True,
                          copy=False,
                          delete=False,
                          rename=False,
                          ),
                 ObjectTreeNode(node_for=[Base],
                                children='children',
                                label='name',
                                auto_open=True,
                                copy=True,
                                delete=True,
                                rename=True,
                                ),
                 ]
        
        tree_editor = TreeEditor(editable=False,
                                 hide_root=True,
                                 on_dclick=self._on_dclick,
                                 on_select=self._on_select,
                                 orientation='vertical',
                                 nodes=nodes
                                 )


        view = View(Group(Item(name='engine',
                               id='engine',
                               editor=tree_editor,
                               resizable=True ),
                          show_labels=False,
                          show_border=False,
                          orientation='vertical'),
                    id='enthought.mayavi.engine',
                    help=False,
                    resizable=True,
                    undo=False,
                    revert=False,
                    ok=False,
                    cancel=False,
                    title='Mayavi pipeline',
                    icon=self.icon,
                    width=0.3,
                    height=0.3)
        return view

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _on_dclick(self, object):
        object.edit_traits(view=object.dialog_view())

    def _on_select(self, object):
        self.engine._on_select(object)
