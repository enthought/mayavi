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

from tvtk.tvtk_classes.algorithm import Algorithm


class AbstractMapper(Algorithm):
    """
    AbstractMapper - abstract class specifies interface to map data
    
    Superclass: Algorithm
    
    AbstractMapper is an abstract class to specify interface between
    data and graphics primitives or software rendering techniques.
    Subclasses of AbstractMapper can be used for rendering 2d data,
    geometry, or volumetric data.
    
    See Also:
    
    AbstractMapper3D Mapper PolyDataMapper VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractMapper, obj, update, **traits)
    
    def _get_clipping_planes(self):
        return wrap_vtk(self._vtk_obj.GetClippingPlanes())
    def _set_clipping_planes(self, arg):
        old_val = self._get_clipping_planes()
        self._wrap_call(self._vtk_obj.SetClippingPlanes,
                        deref_vtk(arg))
        self.trait_property_changed('clipping_planes', old_val, arg)
    clipping_planes = traits.Property(_get_clipping_planes, _set_clipping_planes, help=\
        """
        Get/Set the PlaneCollection which specifies the clipping
        planes.
        """
    )

    def get_scalars(self, *args):
        """
        V.get_scalars(DataSet, int, int, int, string, int)
            -> DataArray
        C++: static DataArray *GetScalars(DataSet *input,
            int scalarMode, int arrayAccessMode, int arrayId,
            const char *arrayName, int &cellFlag)
        Internal helper function for getting the active scalars. The
        scalar mode indicates where the scalars come from.  The cell_flag
        is a return value that is set when the scalars actually are cell
        scalars. (0 for point scalars, 1 for cell scalars, 2 for field
        scalars) The array_access_mode is used to indicate how to retrieve
        the scalars from field data, per id or per name (if the
        scalar_mode indicates that).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetScalars, *my_args)
        return wrap_vtk(ret)

    def _get_time_to_draw(self):
        return self._vtk_obj.GetTimeToDraw()
    time_to_draw = traits.Property(_get_time_to_draw, help=\
        """
        Get the time required to draw the geometry last time it was
        rendered
        """
    )

    def add_clipping_plane(self, *args):
        """
        V.add_clipping_plane(Plane)
        C++: void AddClippingPlane(Plane *plane)
        Specify clipping planes to be applied when the data is mapped (at
        most 6 clipping planes can be specified).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddClippingPlane, *my_args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Release any graphics resources that are being consumed by this
        mapper. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def remove_all_clipping_planes(self):
        """
        V.remove_all_clipping_planes()
        C++: void RemoveAllClippingPlanes()
        Specify clipping planes to be applied when the data is mapped (at
        most 6 clipping planes can be specified).
        """
        ret = self._vtk_obj.RemoveAllClippingPlanes()
        return ret
        

    def remove_clipping_plane(self, *args):
        """
        V.remove_clipping_plane(Plane)
        C++: void RemoveClippingPlane(Plane *plane)
        Specify clipping planes to be applied when the data is mapped (at
        most 6 clipping planes can be specified).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveClippingPlane, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(AbstractMapper)
        C++: void ShallowCopy(AbstractMapper *m)
        Make a shallow copy of this mapper.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
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
            return super(AbstractMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AbstractMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

