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


class AddMembershipArray(PassInputTypeAlgorithm):
    """
    AddMembershipArray - Add an array to the output indicating 
    
    Superclass: PassInputTypeAlgorithm
    
    This filter takes an input selection, DataSetAttribute
    information, and data object and adds a bit array to the output
    DataSetAttributes indicating whether each index was selected or
    not.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAddMembershipArray, obj, update, **traits)
    
    input_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _input_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputArrayName,
                        self.input_array_name)

    output_array_name = traits.String(r"membership", enter_set=True, auto_set=False, help=\
        """
        The name of the array added to the output DataSetAttributes
        indicating membership. Defaults to "membership".
        """
    )
    def _output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputArrayName,
                        self.output_array_name)

    field_type = traits.Trait(-1, traits.Range(-1, 5, enter_set=True, auto_set=False), help=\
        """
        The field type to add the membership array to.
        """
    )
    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    def _get_input_values(self):
        return wrap_vtk(self._vtk_obj.GetInputValues())
    def _set_input_values(self, arg):
        old_val = self._get_input_values()
        my_arg = deref_array([arg], [['vtkAbstractArray']])
        self._wrap_call(self._vtk_obj.SetInputValues,
                        my_arg[0])
        self.trait_property_changed('input_values', old_val, arg)
    input_values = traits.Property(_get_input_values, _set_input_values, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('output_array_name', 'GetOutputArrayName'), ('field_type',
    'GetFieldType'), ('abort_execute', 'GetAbortExecute'),
    ('input_array_name', 'GetInputArrayName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'field_type', 'input_array_name',
    'output_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AddMembershipArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AddMembershipArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['field_type', 'input_array_name',
            'output_array_name']),
            title='Edit AddMembershipArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AddMembershipArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

