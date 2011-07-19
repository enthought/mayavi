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

from tvtk.tvtk_classes.structured_grid_algorithm import StructuredGridAlgorithm


class BlankStructuredGrid(StructuredGridAlgorithm):
    """
    BlankStructuredGrid - translate point attribute data into a
    blanking field
    
    Superclass: StructuredGridAlgorithm
    
    BlankStructuredGrid is a filter that sets the blanking field in a
    StructuredGrid dataset. The blanking field is set by examining a
    specified point attribute data array (e.g., scalars) and converting
    values in the data array to either a "1" (visible) or "0" (blanked)
    value in the blanking array. The values to be blanked are specified
    by giving a min/max range. All data values in the data array
    indicated and laying within the range specified (inclusive on both
    ends) are translated to a "off" blanking value.
    
    See Also:
    
    StructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBlankStructuredGrid, obj, update, **traits)
    
    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the data array name to use to generate the blanking
        field. Alternatively, you can specify the array id. (If both are
        set, the array name takes precedence.)
        """
    )
    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component in the data array to use to generate the
        blanking field.
        """
    )
    def _component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponent,
                        self.component)

    min_blanking_value = traits.Float(9.99999968029e+37, enter_set=True, auto_set=False, help=\
        """
        Specify the lower data value in the data array specified which
        will be converted into a "blank" (or off) value in the blanking
        array.
        """
    )
    def _min_blanking_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinBlankingValue,
                        self.min_blanking_value)

    max_blanking_value = traits.Float(9.99999968029e+37, enter_set=True, auto_set=False, help=\
        """
        Specify the upper data value in the data array specified which
        will be converted into a "blank" (or off) value in the blanking
        array.
        """
    )
    def _max_blanking_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxBlankingValue,
                        self.max_blanking_value)

    array_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Specify the data array id to use to generate the blanking field.
        Alternatively, you can specify the array name. (If both are set,
        the array name takes precedence.)
        """
    )
    def _array_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayId,
                        self.array_id)

    _updateable_traits_ = \
    (('array_id', 'GetArrayId'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('component', 'GetComponent'),
    ('progress_text', 'GetProgressText'), ('min_blanking_value',
    'GetMinBlankingValue'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('max_blanking_value', 'GetMaxBlankingValue'), ('array_name',
    'GetArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_id', 'array_name', 'component',
    'max_blanking_value', 'min_blanking_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BlankStructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['array_id', 'array_name', 'component',
            'max_blanking_value', 'min_blanking_value']),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

