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

from tvtk.tvtk_classes.structured_grid_algorithm import StructuredGridAlgorithm


class BlankStructuredGridWithImage(StructuredGridAlgorithm):
    """
    BlankStructuredGridWithImage - blank a structured grid with an
    image
    
    Superclass: StructuredGridAlgorithm
    
    This filter can be used to set the blanking in a structured grid with
    an image. The filter takes two inputs: the structured grid to blank,
    and the image used to set the blanking. Make sure that the dimensions
    of both the image and the structured grid are identical.
    
    Note that the image is interpreted as follows: zero values indicate
    that the structured grid point is blanked; non-zero values indicate
    that the structured grid point is visible. The blanking data must be
    unsigned char.
    
    See Also:
    
    StructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBlankStructuredGridWithImage, obj, update, **traits)
    
    def _get_blanking_input(self):
        return wrap_vtk(self._vtk_obj.GetBlankingInput())
    def _set_blanking_input(self, arg):
        old_val = self._get_blanking_input()
        self._wrap_call(self._vtk_obj.SetBlankingInput,
                        deref_vtk(arg))
        self.trait_property_changed('blanking_input', old_val, arg)
    blanking_input = traits.Property(_get_blanking_input, _set_blanking_input, help=\
        """
        Set / get the input image used to perform the blanking.
        """
    )

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
            return super(BlankStructuredGridWithImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BlankStructuredGridWithImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit BlankStructuredGridWithImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BlankStructuredGridWithImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

