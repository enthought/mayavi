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

from tvtk.tvtk_classes.outline_source import OutlineSource


class OutlineCornerSource(OutlineSource):
    """
    OutlineCornerSource - create wireframe outline corners around
    bounding box
    
    Superclass: OutlineSource
    
    OutlineCornerSource creates wireframe outline corners around a
    user-specified bounding box.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutlineCornerSource, obj, update, **traits)
    
    corner_factor = traits.Trait(0.2, traits.Range(0.001, 0.5, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the relative size of the corners
        to the length of the corresponding bounds
        """
    )
    def _corner_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerFactor,
                        self.corner_factor)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('corner_factor', 'GetCornerFactor'), ('corners', 'GetCorners'),
    ('progress_text', 'GetProgressText'), ('bounds', 'GetBounds'),
    ('box_type', 'GetBoxType'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('generate_faces', 'GetGenerateFaces'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_faces',
    'global_warning_display', 'release_data_flag', 'box_type', 'bounds',
    'corner_factor', 'corners', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OutlineCornerSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OutlineCornerSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_faces'], ['box_type'], ['bounds',
            'corner_factor', 'corners']),
            title='Edit OutlineCornerSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutlineCornerSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

