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


class MergeFilter(DataSetAlgorithm):
    """
    MergeFilter - extract separate components of data from different
    datasets
    
    Superclass: DataSetAlgorithm
    
    MergeFilter is a filter that extracts separate components of data
    from different datasets and merges them into a single dataset. The
    output from this filter is of the same type as the input (i.e.,
    DataSet.) It treats both cell and point data set attributes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeFilter, obj, update, **traits)
    
    def _get_geometry(self):
        return wrap_vtk(self._vtk_obj.GetGeometry())
    def _set_geometry(self, arg):
        old_val = self._get_geometry()
        self._wrap_call(self._vtk_obj.SetGeometry,
                        deref_vtk(arg))
        self.trait_property_changed('geometry', old_val, arg)
    geometry = traits.Property(_get_geometry, _set_geometry, help=\
        """
        Specify object from which to extract geometry information. Old
        style. Use set_geometry_connection() instead.
        """
    )

    def _get_vectors(self):
        return wrap_vtk(self._vtk_obj.GetVectors())
    def _set_vectors(self, arg):
        old_val = self._get_vectors()
        self._wrap_call(self._vtk_obj.SetVectors,
                        deref_vtk(arg))
        self.trait_property_changed('vectors', old_val, arg)
    vectors = traits.Property(_get_vectors, _set_vectors, help=\
        """
        Set / get the object from which to extract vector information.
        Old style. Use set_vectors_connection() instead.
        """
    )

    def _get_scalars(self):
        return wrap_vtk(self._vtk_obj.GetScalars())
    def _set_scalars(self, arg):
        old_val = self._get_scalars()
        self._wrap_call(self._vtk_obj.SetScalars,
                        deref_vtk(arg))
        self.trait_property_changed('scalars', old_val, arg)
    scalars = traits.Property(_get_scalars, _set_scalars, help=\
        """
        Specify object from which to extract scalar information. Old
        style. Use set_scalars_connection() instead.
        """
    )

    def _get_normals(self):
        return wrap_vtk(self._vtk_obj.GetNormals())
    def _set_normals(self, arg):
        old_val = self._get_normals()
        self._wrap_call(self._vtk_obj.SetNormals,
                        deref_vtk(arg))
        self.trait_property_changed('normals', old_val, arg)
    normals = traits.Property(_get_normals, _set_normals, help=\
        """
        Set / get the object from which to extract normal information.
        Old style. Use set_normals_connection() instead.
        """
    )

    def _get_t_coords(self):
        return wrap_vtk(self._vtk_obj.GetTCoords())
    def _set_t_coords(self, arg):
        old_val = self._get_t_coords()
        self._wrap_call(self._vtk_obj.SetTCoords,
                        deref_vtk(arg))
        self.trait_property_changed('t_coords', old_val, arg)
    t_coords = traits.Property(_get_t_coords, _set_t_coords, help=\
        """
        Set / get the object from which to extract texture coordinates
        information. Old style. Use set_t_coords_connection() instead.
        """
    )

    def _get_tensors(self):
        return wrap_vtk(self._vtk_obj.GetTensors())
    def _set_tensors(self, arg):
        old_val = self._get_tensors()
        self._wrap_call(self._vtk_obj.SetTensors,
                        deref_vtk(arg))
        self.trait_property_changed('tensors', old_val, arg)
    tensors = traits.Property(_get_tensors, _set_tensors, help=\
        """
        Set / get the object from which to extract tensor data. Old
        style. Use set_tensors_connection() instead.
        """
    )

    def add_field(self, *args):
        """
        V.add_field(string, DataSet)
        C++: void AddField(const char *name, DataSet *input)
        Set the object from which to extract a field and the name of the
        field. Note that this does not create pipeline connectivity.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddField, *my_args)
        return ret

    def set_geometry_connection(self, *args):
        """
        V.set_geometry_connection(AlgorithmOutput)
        C++: void SetGeometryConnection(AlgorithmOutput *algOutput)
        Specify object from which to extract geometry information.
        Equivalent to set_input_connection(_0, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGeometryConnection, *my_args)
        return ret

    def set_normals_connection(self, *args):
        """
        V.set_normals_connection(AlgorithmOutput)
        C++: void SetNormalsConnection(AlgorithmOutput *algOutput)
        Set  the connection from which to extract normal information.
        Equivalent to set_input_connection(_3, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetNormalsConnection, *my_args)
        return ret

    def set_scalars_connection(self, *args):
        """
        V.set_scalars_connection(AlgorithmOutput)
        C++: void SetScalarsConnection(AlgorithmOutput *algOutput)
        Specify object from which to extract scalar information.
        Equivalent to set_input_connection(_1, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetScalarsConnection, *my_args)
        return ret

    def set_t_coords_connection(self, *args):
        """
        V.set_t_coords_connection(AlgorithmOutput)
        C++: void SetTCoordsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract texture coordinates
        information. Equivalent to set_input_connection(_4, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTCoordsConnection, *my_args)
        return ret

    def set_tensors_connection(self, *args):
        """
        V.set_tensors_connection(AlgorithmOutput)
        C++: void SetTensorsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract tensor data. Equivalent
        to set_input_connection(_5, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTensorsConnection, *my_args)
        return ret

    def set_vectors_connection(self, *args):
        """
        V.set_vectors_connection(AlgorithmOutput)
        C++: void SetVectorsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract vector information.
        Equivalent to set_input_connection(_2, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVectorsConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

