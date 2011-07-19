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


class ApplyColors(PassInputTypeAlgorithm):
    """
    ApplyColors - apply colors to a data set.
    
    Superclass: PassInputTypeAlgorithm
    
    ApplyColors performs a coloring of the dataset using default
    colors, lookup tables, annotations, and/or a selection. The output is
    a four-component UnsignedCharArray containing RGBA tuples for each
    element in the dataset. The first input is the dataset to be colored,
    which may be a Table, Graph subclass, or DataSet subclass.
    The API of this algorithm refers to "points" and "cells". For
    Graph, the "points" refer to the graph vertices and "cells" refer
    to graph edges. For Table, "points" refer to table rows. For
    DataSet subclasses, the meaning is obvious.
    
    The second (optional) input is a AnnotationLayers object, which
    stores a list of annotation layers, with each layer holding a list of
    Annotation objects. The annotation specifies a subset of data
    along with other properties, including color. For annotations with
    color properties, this algorithm will use the color to color
    elements, using a "top one wins" strategy.
    
    The third (optional) input is a Selection object, meant for
    specifying the current selection. You can control the color of the
    selection.
    
    The algorithm takes two input arrays, specified with
    set_input_array_to_process(_0, 0, 0,
    DataObject::FIELD_ASSOCIATION_POINTS, name) and
    set_input_array_to_process(_1, 0, 0,
    DataObject::FIELD_ASSOCIATION_CELLS, name). These set the point
    and cell data arrays to use to color the data with the associated
    lookup table. For Graph, Table inputs, you would use
    FIELD_ASSOCIATION_VERTICES, FIELD_ASSOCIATION_EDGES, or
    FIELD_ASSOCIATION_ROWS as appropriate.
    
    To use the color array generated here, you should do the following:
    
    
     mapper->_set_scalar_mode_to_use_cell_field_data();
     mapper->_select_color_array("vtk_apply_colors color");
     mapper->_set_scalar_visibility(true);
    
    Colors are assigned with the following priorities:  If an item is
    part of the selection, it is colored with that color. Otherwise, if
    the item is part of an annotation, it is colored
         with the color of the final (top) annotation in the set of
    layers. Otherwise, if the lookup table is used, it is colored using
    the
         lookup table color for the data value of the element. Otherwise
    it will be colored with the default color. 
    
    Note: The opacity of an unselected item is defined by the
    multiplication of default opacity, lookup table opacity, and
    annotation opacity, where opacity is taken as a number from 0 to 1.
    So items will never be more opaque than any of these three opacities.
    Selected items are always given the selection opacity directly.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkApplyColors, obj, update, **traits)
    
    use_cell_lookup_table = tvtk_base.false_bool_trait(help=\
        """
        If on, uses the cell lookup table to set the colors of
        unannotated, unselected elements of the data.
        """
    )
    def _use_cell_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCellLookupTable,
                        self.use_cell_lookup_table_)

    scale_cell_lookup_table = tvtk_base.true_bool_trait(help=\
        """
        If on, uses the range of the data to scale the lookup table
        range. Otherwise, uses the range defined in the lookup table.
        """
    )
    def _scale_cell_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleCellLookupTable,
                        self.scale_cell_lookup_table_)

    use_current_annotation_color = tvtk_base.false_bool_trait(help=\
        """
        Use the annotation to color the current annotation (i.e. the
        current selection). Otherwise use the selection color attributes
        of this filter.
        """
    )
    def _use_current_annotation_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCurrentAnnotationColor,
                        self.use_current_annotation_color_)

    use_point_lookup_table = tvtk_base.false_bool_trait(help=\
        """
        If on, uses the point lookup table to set the colors of
        unannotated, unselected elements of the data.
        """
    )
    def _use_point_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUsePointLookupTable,
                        self.use_point_lookup_table_)

    scale_point_lookup_table = tvtk_base.true_bool_trait(help=\
        """
        If on, uses the range of the data to scale the lookup table
        range. Otherwise, uses the range defined in the lookup table.
        """
    )
    def _scale_point_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalePointLookupTable,
                        self.scale_point_lookup_table_)

    default_point_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The default point opacity for all unannotated, unselected
        elements of the data. This is used if use_point_lookup_table is off.
        """
    )
    def _default_point_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultPointOpacity,
                        self.default_point_opacity)

    selected_point_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The point opacity for all selected elements of the data. This is
        used if the selection input is available.
        """
    )
    def _selected_point_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedPointOpacity,
                        self.selected_point_opacity)

    def _get_cell_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetCellLookupTable())
    def _set_cell_lookup_table(self, arg):
        old_val = self._get_cell_lookup_table()
        self._wrap_call(self._vtk_obj.SetCellLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('cell_lookup_table', old_val, arg)
    cell_lookup_table = traits.Property(_get_cell_lookup_table, _set_cell_lookup_table, help=\
        """
        The lookup table to use for cell colors. This is only used if
        input array 1 is set and use_cell_lookup_table is on.
        """
    )

    selected_cell_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _selected_cell_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedCellColor,
                        self.selected_cell_color, False)

    default_cell_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _default_cell_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultCellColor,
                        self.default_cell_color, False)

    point_color_output_array_name = traits.String(r"vtkApplyColors color", enter_set=True, auto_set=False, help=\
        """
        The output array name for the point color RGBA array. Default is "vtk_apply_colors
        color".
        """
    )
    def _point_color_output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointColorOutputArrayName,
                        self.point_color_output_array_name)

    cell_color_output_array_name = traits.String(r"vtkApplyColors color", enter_set=True, auto_set=False, help=\
        """
        The output array name for the cell color RGBA array. Default is "vtk_apply_colors
        color".
        """
    )
    def _cell_color_output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellColorOutputArrayName,
                        self.cell_color_output_array_name)

    default_cell_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The default cell opacity for all unannotated, unselected elements
        of the data. This is used if use_cell_lookup_table is off.
        """
    )
    def _default_cell_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultCellOpacity,
                        self.default_cell_opacity)

    def _get_point_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetPointLookupTable())
    def _set_point_lookup_table(self, arg):
        old_val = self._get_point_lookup_table()
        self._wrap_call(self._vtk_obj.SetPointLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('point_lookup_table', old_val, arg)
    point_lookup_table = traits.Property(_get_point_lookup_table, _set_point_lookup_table, help=\
        """
        The lookup table to use for point colors. This is only used if
        input array 0 is set and use_point_lookup_table is on.
        """
    )

    selected_cell_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The cell opacity for all selected elements of the data. This is
        used if the selection input is available.
        """
    )
    def _selected_cell_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedCellOpacity,
                        self.selected_cell_opacity)

    selected_point_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _selected_point_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedPointColor,
                        self.selected_point_color, False)

    default_point_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _default_point_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultPointColor,
                        self.default_point_color, False)

    _updateable_traits_ = \
    (('use_point_lookup_table', 'GetUsePointLookupTable'),
    ('use_cell_lookup_table', 'GetUseCellLookupTable'),
    ('scale_point_lookup_table', 'GetScalePointLookupTable'),
    ('selected_point_color', 'GetSelectedPointColor'),
    ('selected_cell_opacity', 'GetSelectedCellOpacity'),
    ('default_cell_opacity', 'GetDefaultCellOpacity'),
    ('selected_cell_color', 'GetSelectedCellColor'),
    ('point_color_output_array_name', 'GetPointColorOutputArrayName'),
    ('cell_color_output_array_name', 'GetCellColorOutputArrayName'),
    ('scale_cell_lookup_table', 'GetScaleCellLookupTable'),
    ('use_current_annotation_color', 'GetUseCurrentAnnotationColor'),
    ('default_cell_color', 'GetDefaultCellColor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('selected_point_opacity', 'GetSelectedPointOpacity'), ('debug',
    'GetDebug'), ('default_point_color', 'GetDefaultPointColor'),
    ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('default_point_opacity', 'GetDefaultPointOpacity'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scale_cell_lookup_table',
    'scale_point_lookup_table', 'use_cell_lookup_table',
    'use_current_annotation_color', 'use_point_lookup_table',
    'cell_color_output_array_name', 'default_cell_color',
    'default_cell_opacity', 'default_point_color',
    'default_point_opacity', 'point_color_output_array_name',
    'progress_text', 'selected_cell_color', 'selected_cell_opacity',
    'selected_point_color', 'selected_point_opacity'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ApplyColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ApplyColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scale_cell_lookup_table', 'scale_point_lookup_table',
            'use_cell_lookup_table', 'use_current_annotation_color',
            'use_point_lookup_table'], [], ['cell_color_output_array_name',
            'default_cell_color', 'default_cell_opacity', 'default_point_color',
            'default_point_opacity', 'point_color_output_array_name',
            'selected_cell_color', 'selected_cell_opacity',
            'selected_point_color', 'selected_point_opacity']),
            title='Edit ApplyColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ApplyColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

