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

from tvtk.tvtk_classes.function_set import FunctionSet


class GenericInterpolatedVelocityField(FunctionSet):
    """
    GenericInterpolatedVelocityField - Interface for obtaining
    
    Superclass: FunctionSet
    
    GenericInterpolatedVelocityField acts as a continuous velocity
    field by performing cell interpolation on the underlying DataSet.
    This is a concrete sub-class of FunctionSet with
    number_of_independent_variables = 4 (x,y,z,t) and number_of_functions = 3
    (u,v,w). Normally, every time an evaluation is performed, the cell
    which contains the point (x,y,z) has to be found by calling find_cell.
    This is a computationally expansive operation. In certain cases, the
    cell search can be avoided or shortened by providing a guess for the
    cell iterator. For example, in streamline integration, the next
    evaluation is usually in the same or a neighbour cell. For this
    reason, GenericInterpolatedVelocityField stores the last cell
    iterator. If caching is turned on, it uses this iterator as the
    starting point.
    
    Caveats:
    
    GenericInterpolatedVelocityField is not thread safe. A new
    instance should be created by each thread.
    
    See Also:
    
    FunctionSet GenericStreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericInterpolatedVelocityField, obj, update, **traits)
    
    caching = tvtk_base.true_bool_trait(help=\
        """
        Turn caching on/off.
        """
    )
    def _caching_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaching,
                        self.caching_)

    def _get_cache_hit(self):
        return self._vtk_obj.GetCacheHit()
    cache_hit = traits.Property(_get_cache_hit, help=\
        """
        Caching statistics.
        """
    )

    def _get_cache_miss(self):
        return self._vtk_obj.GetCacheMiss()
    cache_miss = traits.Property(_get_cache_miss, help=\
        """
        Caching statistics.
        """
    )

    def _get_last_cell(self):
        return wrap_vtk(self._vtk_obj.GetLastCell())
    last_cell = traits.Property(_get_last_cell, help=\
        """
        Return the cell cached from last evaluation.
        """
    )

    def _get_last_data_set(self):
        return wrap_vtk(self._vtk_obj.GetLastDataSet())
    last_data_set = traits.Property(_get_last_data_set, help=\
        """
        Returns the last dataset that was visited. Can be used as a first
        guess as to where the next point will be as well as to avoid
        searching through all datasets to get more information about the
        point.
        """
    )

    def get_last_local_coordinates(self, *args):
        """
        V.get_last_local_coordinates([float, float, float]) -> int
        C++: int GetLastLocalCoordinates(double pcoords[3])
        Returns the interpolation weights cached from last evaluation if
        the cached cell is valid (returns 1). Otherwise, it does not
        change w and returns 0.
        """
        ret = self._wrap_call(self._vtk_obj.GetLastLocalCoordinates, *args)
        return ret

    def _get_vectors_selection(self):
        return self._vtk_obj.GetVectorsSelection()
    vectors_selection = traits.Property(_get_vectors_selection, help=\
        """
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in NULL and the filter will use the
        active vector array.
        """
    )

    def add_data_set(self, *args):
        """
        V.add_data_set(GenericDataSet)
        C++: virtual void AddDataSet(GenericDataSet *dataset)
        Add a dataset used for the implicit function evaluation. If more
        than one dataset is added, the evaluation point is searched in
        all until a match is found. THIS FUNCTION DOES NOT CHANGE THE
        REFERENCE COUNT OF dataset FOR THREAD SAFETY REASONS.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *my_args)
        return ret

    def clear_last_cell(self):
        """
        V.clear_last_cell()
        C++: void ClearLastCell()
        Set the last cell id to -1 so that the next search does not start
        from the previous cell
        """
        ret = self._vtk_obj.ClearLastCell()
        return ret
        

    def copy_parameters(self, *args):
        """
        V.copy_parameters(GenericInterpolatedVelocityField)
        C++: virtual void CopyParameters(
            GenericInterpolatedVelocityField *from)
        Copy the user set parameters from source. This copies the Caching
        parameters. Sub-classes can add more after chaining.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyParameters, *my_args)
        return ret

    def select_vectors(self, *args):
        """
        V.select_vectors(string)
        C++: void SelectVectors(const char *fieldName)
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in NULL and the filter will use the
        active vector array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectVectors, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('caching', 'GetCaching'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['caching', 'debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['caching'], [], []),
            title='Edit GenericInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

