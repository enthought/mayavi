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

from tvtk.tvtk_classes.poly_data_source import PolyDataSource


class SpatialRepresentationFilter(PolyDataSource):
    """
    SpatialRepresentationFilter - generate polygonal model of spatial
    search object (i.e., a Locator)
    
    Superclass: PolyDataSource
    
    SpatialRepresentationFilter generates an polygonal representation
    of a spatial search (vtk_locator) object. The representation varies
    depending upon the nature of the spatial search object. For example,
    the representation for OBBTree is a collection of oriented
    bounding boxes. Ths input to this filter is a dataset of any type,
    and the output is polygonal data. You must also specify the spatial
    search object to use.
    
    Generally spatial search objects are used for collision detection and
    other geometric operations, but in this filter one or more levels of
    spatial searchers can be generated to form a geometric approximation
    to the input data. This is a form of data simplification, generally
    used to accelerate the rendering process. Or, this filter can be used
    as a debugging/ visualization aid for spatial search objects.
    
    This filter can generate one or more output PolyData corresponding
    to different levels in the spatial search tree. The output data is
    retrieved using the get_output(id) method, where id ranges from 0
    (root level) to Level. Note that the output for level "id" is not
    computed unless a get_output(id) method is issued. Thus, if you desire
    three levels of output (say 2,4,7), you would have to invoke
    get_output(_2), get_output(_4), and get_output(_7). (Also note that the
    Level ivar is computed automatically depending on the size and nature
    of the input data.) There is also another get_output() method that
    takes no parameters. This method returns the leafs of the spatial
    search tree, which may be at different levels.
    
    Caveats:
    
    You can specify the number of levels of to generate with the
    max_levels ivar. However, when the spatial search tree is built, this
    number of levels may not actually be generated. The actual number
    available can be found in the Levels ivar. Note that the value of
    Levels may change after filter execution.
    
    See Also:
    
    Locator PointLocator CellLocator OBBTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpatialRepresentationFilter, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set / get the input data or filter.
        """
    )

    def _get_spatial_representation(self):
        return wrap_vtk(self._vtk_obj.GetSpatialRepresentation())
    def _set_spatial_representation(self, arg):
        old_val = self._get_spatial_representation()
        self._wrap_call(self._vtk_obj.SetSpatialRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('spatial_representation', old_val, arg)
    spatial_representation = traits.Property(_get_spatial_representation, _set_spatial_representation, help=\
        """
        Set/Get the locator that will be used to generate the
        representation.
        """
    )

    def _get_level(self):
        return self._vtk_obj.GetLevel()
    level = traits.Property(_get_level, help=\
        """
        Get the maximum number of outputs actually available.
        """
    )

    def reset_output(self):
        """
        V.reset_output()
        C++: void ResetOutput()
        Reset requested output levels
        """
        ret = self._vtk_obj.ResetOutput()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpatialRepresentationFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['release_data_flag']),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

