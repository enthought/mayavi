"""
Custom nodes for a Tree Editor that provide views for adding various nodes
to the tree.
"""
# Authors: Judah De Paula <judah@enthought.com>
#          Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.
from enthought.traits.api import HasTraits, Str, Property, Any, Button, Enum, List
from enthought.traits.ui.api import View, Item, Group

from enthought.mayavi.core.registry import registry


class AdderNode(HasTraits):
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
        view.buttons = ['OK', 'Cancel']
        view.title = self.label
        return view
    
    def _get_scene(self):
        """ Trait Property getter for 'scene'.
        """
        if self.object is not None:
            return self.object.scene
        else:
            return None



class SceneAdderNode(AdderNode):
    """ Subclass for adding Scene nodes to a Mayavi Engine node.
    """
    
    # Button for the View.
    add_scene = Button('Add a new scene')  
    
    # Trait view to show in the Mayavi current object panel.
    view = View(Group(Item('add_scene'), 
                      label='Add a scene'))
    
    
    def _add_scene_fired(self):
        """ Trait handler for when the add_scene button is clicked.
        """
        self.object.new_scene()
  
  
###############################################################################
class SourceAdderNode(AdderNode):
    """ Tree node that presents a view to the user to add a scene source.
    """
    
    # Button for adding a data file, with automatic format checking.
    open_file = Button('Open File')        
    
    # Button for adding a source.
    add_source = Button('Add Source')
    
    # View object to display a list of source names.    
    source = Enum(values='names')

    # The source names to display to the user.
    names = List(Str)

    # The mapping of the source name and how to access the code.
    mapping = List(Str)
    
    # The string to display on the icon in the TreeEditor.
    label = 'Add Source'
    
    # Trait view to show in the Mayavi current object panel.
    view = View(Group(Group(Item('open_file'),
                            label='Add a source from a file',
                            show_border=True),
                      Group(Item('source'),
                            Item('add_source'),
                            label='Add a Mayavi source',
                            show_border=True),
                      label='Add a source'))


    def _object_changed(self, value):
        """ Trait handler for when the self.object trait changes.
        """
        result = []
        mapping = []
        if value is not None:
            for src in registry.sources:
                if len(src.extensions) == 0:
                    result.append(src.menu_name.replace('&',''))
                    mapping.append(src.id)
        self.names = result
        self.mapping = mapping
        # Don't need 'x', but do need to generate the actions.
        x = value._menu_helper.actions


    def _open_file_fired(self):
        """ Trait handler for when the open_file button is clicked.
        """
        self.object._menu_helper.open_file_action()


    def _add_source_fired(self):
        """ Trait handler for when the add_source button is clicked.
        """
        src = self.source
        index = self.names.index(src)
        id = self.mapping[index]
        action = getattr(self.object._menu_helper, id)
        action()
    
    
###############################################################################
class FilterAdderNode(AdderNode):  
    """ Tree node that presents a view to the user to add filters or modules.
    """
    
    # Text to show on the icon in the TreeEditor
    label = 'Add Module/Filter'

    # View Button for adding a module to the source.
    add_module = Button('Add Module')    
    
    # Object that the View can use for the user to select a module.
    module = Enum(values='module_names')
    
    # The name of the module to display to the user.
    module_names = List(Str)
    
    # The mayavi lookup value to use the module code.
    module_mapping = List(Str)
    
    # View Button for adding a filter to the source.
    add_filter = Button('Add Filter')        
    
    # Object that the View can use for the user to select a module.
    filter = Enum(values='filter_names')
    
    # The name of the filter to display to the user.
    filter_names = List(Str)
    
    # The mayavi lookup value to use the filter code.
    filter_mapping = List(Str)

    # The View to show in the selected object panel.
    view = View(Group(Group(Item('filter'),
                           Item('add_filter'),
                           label='Filters',
                           show_border=True),
                      Group(Item('module'),
                           Item('add_module'),
                           label='Modules',
                           show_border=True),
                      )
                )
    
    
    def _object_changed(self, value):
        """ Trait handler for when self.object is changed.
        """
        if value is None:
            return
        
        # First calculate modules.
        module_names = []
        module_mapping = []
        # Don't use x, but the call triggers some assignments.
        x = value._menu_helper.actions
        for mod in registry.modules:
            chk = getattr(self.object._menu_helper, 'check_' + mod.id)
            if chk():
                module_names.append(mod.menu_name.replace('&',''))
                module_mapping.append(mod.id)
        self.module_names = module_names
        self.module_mapping = module_mapping

        # Second, calculate filters.
        filter_names = []
        filter_mapping = []
        for fil in registry.filters:
            chk = getattr(self.object._menu_helper, 'check_' + fil.id)
            if chk():
                filter_names.append(fil.menu_name.replace('&',''))
                filter_mapping.append(fil.id)
        self.filter_names = filter_names
        self.filter_mapping = filter_mapping
    
    
    def _add_module_fired(self):
        """ Trait handler for when add_module button is clicked.
        """
        mod = self.module
        index = self.module_names.index(mod)
        id = self.module_mapping[index]
        action = getattr(self.object._menu_helper, id)
        action()


    def _add_filter_fired(self):
        """ Trait handler for when add_filter button is clicked.
        """
        fil = self.filter
        index = self.filter_names.index(fil)
        id = self.filter_mapping[index]
        action = getattr(self.object._menu_helper, id)
        action()

### EOF #######################################################################
