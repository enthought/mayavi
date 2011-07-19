# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class ApplyIcons(PassInputTypeAlgorithm):
    """
    ApplyIcons - apply icons to a data set.
    
    Superclass: PassInputTypeAlgorithm
    
    ApplyIcons performs a iconing of the dataset using default icons,
    lookup tables, annotations, and/or a selection. The output is a
    IntArray containing the icon index for each element in the
    dataset. The first input is the dataset to be iconed, which may be a
    Table, Graph subclass, or DataSet subclass.
    
    The second (optional) input is a AnnotationLayers object, which
    stores a list of annotation layers, with each layer holding a list of
    Annotation objects. The annotation specifies a subset of data
    along with other properties, including icon. For annotations with
    icon properties, this algorithm will use the icon index of annotated
    elements, using a "top one wins" strategy.
    
    The third (optional) input is a Selection object, meant for
    specifying the current selection. You can control the icon of the
    selection, or whether there is a set of selected icons at a
    particular offset in the icon sheet.
    
    The algorithm takes an input array, specified with
    set_input_array_to_process(_0, 0, 0,
    DataObject::FIELD_ASSOCIATION_POINTS, name) This sets data arrays
    to use to icon the data with the associated lookup table. For
    Graph and Table inputs, you would use
    FIELD_ASSOCIATION_VERTICES, FIELD_ASSOCIATION_EDGES, or
    FIELD_ASSOCIATION_ROWS as appropriate. The icon array will be added
    to the same set of attributes that the input array came from. If
    there is no input array, the icon array will be applied to the
    attributes associated with the attribute_type parameter.
    
    Icons are assigned with the following priorities:  If an item is part
    of the selection, it is glyphed with that icon. Otherwise, if the
    item is part of an annotation, it is glyphed
         with the icon of the final (top) annotation in the set of
    layers. Otherwise, if a lookup table is used, it is glyphed using the
         lookup table icon for the data value of the element. Otherwise
    it will be glyphed with the default icon. 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkApplyIcons, obj, update, **traits)
    
    use_lookup_table = tvtk_base.false_bool_trait(help=\
        """
        If on, uses the point lookup table to set the colors of
        unannotated, unselected elements of the data.
        """
    )
    def _use_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLookupTable,
                        self.use_lookup_table_)

    selection_mode = traits.Trait('ignore_selection',
    tvtk_base.TraitRevPrefixMap({'selected_icon': 0, 'ignore_selection': 3, 'selected_offset': 1, 'annotation_icon': 2}), help=\
        """
        Changes the behavior of the icon to use for selected items. 
        SELECTED_ICON uses selected_icon as the icon for all selected
        elements. SELECTED_OFFSET uses selected_icon as an offset to add
        to all selected elements. ANNOTATION_ICON uses the ICON_INDEX()
        property of the current annotation. IGNORE_SELECTION does not
        change the icon based on the current selection.  The default is
        IGNORE_SELECTION.
        """
    )
    def _selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMode,
                        self.selection_mode_)

    selected_icon = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The point icon for all selected elements of the data. This is
        used if the annotation input has a current selection.
        """
    )
    def _selected_icon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedIcon,
                        self.selected_icon)

    icon_output_array_name = traits.String(r"vtkApplyIcons icon", enter_set=True, auto_set=False, help=\
        """
        The output array name for the point icon index array. Default is "vtk_apply_icons
        icon".
        """
    )
    def _icon_output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconOutputArrayName,
                        self.icon_output_array_name)

    default_icon = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The default point icon for all unannotated, unselected elements
        of the data. This is used if use_point_lookup_table is off.
        """
    )
    def _default_icon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultIcon,
                        self.default_icon)

    attribute_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        The attribute type to append the icon array to, used only if the
        input array is not specified or does not exist. This is set to
        one of the attribute_types enum in DataObject (e.g. POINT,
        CELL, VERTEX EDGE, FIELD).
        """
    )
    def _attribute_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeType,
                        self.attribute_type)

    def clear_all_icon_types(self):
        """
        V.clear_all_icon_types()
        C++: void ClearAllIconTypes()
        Edits the lookup table to use for point icons. This is only used
        if input array 0 is set and use_point_lookup_table is on.
        """
        ret = self._vtk_obj.ClearAllIconTypes()
        return ret
        

    def set_icon_type(self, *args):
        """
        V.set_icon_type(Variant, int)
        C++: void SetIconType(Variant v, int icon)
        V.set_icon_type(float, int)
        C++: void SetIconType(double v, int icon)
        V.set_icon_type(string, int)
        C++: void SetIconType(const char *v, int icon)
        Edits the lookup table to use for point icons. This is only used
        if input array 0 is set and use_point_lookup_table is on.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetIconType, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('attribute_type', 'GetAttributeType'), ('selection_mode',
    'GetSelectionMode'), ('progress_text', 'GetProgressText'),
    ('icon_output_array_name', 'GetIconOutputArrayName'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('selected_icon', 'GetSelectedIcon'),
    ('progress', 'GetProgress'), ('use_lookup_table',
    'GetUseLookupTable'), ('default_icon', 'GetDefaultIcon'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_lookup_table', 'selection_mode',
    'attribute_type', 'default_icon', 'icon_output_array_name',
    'progress_text', 'selected_icon'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ApplyIcons, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ApplyIcons properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_lookup_table'], ['selection_mode'],
            ['attribute_type', 'default_icon', 'icon_output_array_name',
            'selected_icon']),
            title='Edit ApplyIcons properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ApplyIcons properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

