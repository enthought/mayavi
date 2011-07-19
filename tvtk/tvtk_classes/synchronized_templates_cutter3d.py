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

from tvtk.tvtk_classes.synchronized_templates3d import SynchronizedTemplates3D


class SynchronizedTemplatesCutter3D(SynchronizedTemplates3D):
    """
    SynchronizedTemplatesCutter3D - generate cut surface from
    structured points
    
    Superclass: SynchronizedTemplates3D
    
    SynchronizedTemplatesCutter3D is an implementation of the
    synchronized template algorithm. Note that CutFilter will
    automatically use this class when appropriate.
    
    See Also:
    
    ContourFilter SynchronizedTemplates3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSynchronizedTemplatesCutter3D, obj, update, **traits)
    
    def _get_cut_function(self):
        return wrap_vtk(self._vtk_obj.GetCutFunction())
    def _set_cut_function(self, arg):
        old_val = self._get_cut_function()
        self._wrap_call(self._vtk_obj.SetCutFunction,
                        deref_vtk(arg))
        self.trait_property_changed('cut_function', old_val, arg)
    cut_function = traits.Property(_get_cut_function, _set_cut_function, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('array_component', 'GetArrayComponent'), ('progress_text',
    'GetProgressText'), ('compute_normals', 'GetComputeNormals'),
    ('compute_scalars', 'GetComputeScalars'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_contours',
    'GetNumberOfContours'), ('input_memory_limit', 'GetInputMemoryLimit'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'global_warning_display',
    'release_data_flag', 'array_component', 'input_memory_limit',
    'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SynchronizedTemplatesCutter3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_gradients', 'compute_normals',
            'compute_scalars'], [], ['array_component', 'input_memory_limit',
            'number_of_contours']),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

