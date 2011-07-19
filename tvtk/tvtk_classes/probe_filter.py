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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class ProbeFilter(DataSetAlgorithm):
    """
    ProbeFilter - sample data values at specified point locations
    
    Superclass: DataSetAlgorithm
    
    ProbeFilter is a filter that computes point attributes (e.g.,
    scalars, vectors, etc.) at specified point positions. The filter has
    two inputs: the Input and Source. The Input geometric structure is
    passed through the filter. The point attributes are computed at the
    Input point positions by interpolating into the source data. For
    example, we can compute data values on a plane (plane specified as
    Input) from a volume (Source). The cell data of the source data is
    copied to the output based on in which source cell each input point
    is. If an array of the same name exists both in source's point and
    cell data, only the one from the point data is probed.
    
    This filter can be used to resample data, or convert one dataset form
    into another. For example, an unstructured grid (vtk_unstructured_grid)
    can be probed with a volume (three-dimensional ImageData), and
    then volume rendering techniques can be used to visualize the
    results. Another example: a line or curve can be used to probe data
    to produce x-y plots along that line or curve.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProbeFilter, obj, update, **traits)
    
    spatial_match = tvtk_base.false_bool_trait(help=\
        """
        This flag is used only when a piece is requested to update.  By
        default the flag is off.  Because no spatial correspondence
        between input pieces and source pieces is known, all of the
        source has to be requested no matter what piece of the output is
        requested.  When there is a spatial correspondence, the
        user/application can set this flag.  This hint allows the breakup
        of the probe operation to be much more efficient.  When piece m
        of n is requested for update by the user, then only n of m needs
        to be requested of the source.
        """
    )
    def _spatial_match_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpatialMatch,
                        self.spatial_match_)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Specify the point locations used to probe input. Any geometry can
        be used. Old style. Do not use unless for backwards
        compatibility.
        """
    )

    valid_point_mask_array_name = traits.String(r"vtkValidPointMask", enter_set=True, auto_set=False, help=\
        """
        Returns the name of the char array added to the output with
        values 1 for valid points and 0 for invalid points. Set to
        "vtk_valid_point_mask" by default.
        """
    )
    def _valid_point_mask_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidPointMaskArrayName,
                        self.valid_point_mask_array_name)

    def _get_valid_points(self):
        return wrap_vtk(self._vtk_obj.GetValidPoints())
    valid_points = traits.Property(_get_valid_points, help=\
        """
        Get the list of point ids in the output that contain attribute
        data interpolated from the source.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the point locations used to probe input. Any geometry can
        be used. New style. Equivalent to set_input_connection(_1,
        alg_output).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('spatial_match', 'GetSpatialMatch'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('valid_point_mask_array_name', 'GetValidPointMaskArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'spatial_match', 'progress_text',
    'valid_point_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProbeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['spatial_match'], [],
            ['valid_point_mask_array_name']),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

