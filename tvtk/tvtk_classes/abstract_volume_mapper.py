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

from tvtk.tvtk_classes.abstract_mapper3d import AbstractMapper3D


class AbstractVolumeMapper(AbstractMapper3D):
    """
    AbstractVolumeMapper - Abstract class for a volume mapper
    
    Superclass: AbstractMapper3D
    
    AbstractVolumeMapper is the abstract definition of a volume
    mapper. Specific subclasses deal with different specific types of
    data input
    
    See Also:
    
    VolumeMapper UnstructuredGridVolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractVolumeMapper, obj, update, **traits)
    
    scalar_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_point_data': 1, 'use_cell_data': 2, 'use_cell_field_data': 4, 'use_point_field_data': 3}), help=\
        """
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (_scalar_mode_to_default), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (_scalar_mode_to_use_point_data) or cell data
        (_scalar_mode_to_use_cell_data). You can also choose to get the scalars
        from an array in point field data (_scalar_mode_to_use_point_field_data)
        or cell field data (_scalar_mode_to_use_cell_field_data).  If scalars
        are coming from a field data array, you must call
        select_scalar_array.
        """
    )
    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    def _get_array_access_mode(self):
        return self._vtk_obj.GetArrayAccessMode()
    array_access_mode = traits.Property(_get_array_access_mode, help=\
        """
        Get the array name or number and component to use for rendering.
        """
    )

    def _get_array_id(self):
        return self._vtk_obj.GetArrayId()
    array_id = traits.Property(_get_array_id, help=\
        """
        Get the array name or number and component to use for rendering.
        """
    )

    def _get_array_name(self):
        return self._vtk_obj.GetArrayName()
    array_name = traits.Property(_get_array_name, help=\
        """
        Get the array name or number and component to use for rendering.
        """
    )

    def _get_data_object_input(self):
        return wrap_vtk(self._vtk_obj.GetDataObjectInput())
    data_object_input = traits.Property(_get_data_object_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_data_set_input(self):
        return wrap_vtk(self._vtk_obj.GetDataSetInput())
    data_set_input = traits.Property(_get_data_set_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_gradient_magnitude_bias(self):
        return self._vtk_obj.GetGradientMagnitudeBias()
    gradient_magnitude_bias = traits.Property(_get_gradient_magnitude_bias, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
        """
    )

    def _get_gradient_magnitude_scale(self):
        return self._vtk_obj.GetGradientMagnitudeScale()
    gradient_magnitude_scale = traits.Property(_get_gradient_magnitude_scale, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
        """
    )

    def render(self, *args):
        """
        V.render(Renderer, Volume)
        C++: virtual void Render(Renderer *ren, Volume *vol)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Render the
        volume
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def select_scalar_array(self, *args):
        """
        V.select_scalar_array(int)
        C++: virtual void SelectScalarArray(int arrayNum)
        V.select_scalar_array(string)
        C++: virtual void SelectScalarArray(const char *arrayName)
        When scalar_mode is set to use_point_field_data or use_cell_field_data,
        you can specify which scalar array to use during rendering. The
        transfer function in the VolumeProperty (attached to the
        calling Volume) will decide how to convert vectors to colors.
        """
        ret = self._wrap_call(self._vtk_obj.SelectScalarArray, *args)
        return ret

    def set_input(self, *args):
        """
        V.set_input(DataSet)
        C++: virtual void SetInput(DataSet *)
        Set/Get the input data
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('scalar_mode',
    'GetScalarMode'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractVolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['scalar_mode'], []),
            title='Edit AbstractVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

