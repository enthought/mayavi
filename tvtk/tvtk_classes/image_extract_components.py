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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageExtractComponents(ThreadedImageAlgorithm):
    """
    ImageExtractComponents - Outputs a single component
    
    Superclass: ThreadedImageAlgorithm
    
    ImageExtractComponents takes an input with any number of
    components and outputs some of them.  It does involve a copy of the
    data.
    
    See Also:
    
    ImageAppendComponents
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageExtractComponents, obj, update, **traits)
    
    components = traits.Array(shape=(3,), value=(0, 1, 2), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the components to extract.
        """
    )
    def _components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponents,
                        self.components)

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Get the number of components to extract. This is set implicitly
        by the set_components() method.
        """
    )

    _updateable_traits_ = \
    (('number_of_threads', 'GetNumberOfThreads'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('components', 'GetComponents'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'components', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageExtractComponents, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageExtractComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['components', 'number_of_threads']),
            title='Edit ImageExtractComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageExtractComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

