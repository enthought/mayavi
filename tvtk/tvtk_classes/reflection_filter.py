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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ReflectionFilter(DataObjectAlgorithm):
    """
    ReflectionFilter - reflects a data set across a plane
    
    Superclass: DataObjectAlgorithm
    
    The ReflectionFilter reflects a data set across one of the planes
    formed by the data set's bounding box. Since it converts data sets
    into unstructured grids, it is not effeicient for structured data
    sets.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReflectionFilter, obj, update, **traits)
    
    copy_input = tvtk_base.true_bool_trait(help=\
        """
        If on (the default), copy the input geometry to the output. If
        off, the output will only contain the reflection.
        """
    )
    def _copy_input_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyInput,
                        self.copy_input_)

    plane = traits.Trait('x_min',
    tvtk_base.TraitRevPrefixMap({'y_min': 1, 'y_max': 4, 'z_max': 5, 'y': 7, 'z_min': 2, 'x_max': 3, 'x_min': 0, 'x': 6, 'z': 8}), help=\
        """
        Set the normal of the plane to use as mirror.
        """
    )
    def _plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlane,
                        self.plane_)

    center = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If the reflection plane is set to X, Y or Z, this variable is use
        to set the position of the plane.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    _updateable_traits_ = \
    (('copy_input', 'GetCopyInput'), ('center', 'GetCenter'),
    ('progress_text', 'GetProgressText'), ('plane', 'GetPlane'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'copy_input', 'debug', 'global_warning_display',
    'release_data_flag', 'plane', 'center', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReflectionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['copy_input'], ['plane'], ['center']),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

