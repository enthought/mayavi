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

from tvtk.tvtk_classes.extent_translator import ExtentTranslator


class ImageDataLIC2DExtentTranslator(ExtentTranslator):
    """
    ImageDataLIC2DExtentTranslator 
    
    Superclass: ExtentTranslator
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDataLIC2DExtentTranslator, obj, update, **traits)
    
    def _get_input_extent_translator(self):
        return wrap_vtk(self._vtk_obj.GetInputExtentTranslator())
    def _set_input_extent_translator(self, arg):
        old_val = self._get_input_extent_translator()
        self._wrap_call(self._vtk_obj.SetInputExtentTranslator,
                        deref_vtk(arg))
        self.trait_property_changed('input_extent_translator', old_val, arg)
    input_extent_translator = traits.Property(_get_input_extent_translator, _set_input_extent_translator, help=\
        """
        
        """
    )

    input_whole_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _input_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputWholeExtent,
                        self.input_whole_extent)

    def _get_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetAlgorithm())
    def _set_algorithm(self, arg):
        old_val = self._get_algorithm()
        self._wrap_call(self._vtk_obj.SetAlgorithm,
                        deref_vtk(arg))
        self.trait_property_changed('algorithm', old_val, arg)
    algorithm = traits.Property(_get_algorithm, _set_algorithm, help=\
        """
        Set the ImageDataLIC2D algorithm for which this extent
        translator is being used.
        """
    )

    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('input_whole_extent',
    'GetInputWholeExtent'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('extent', 'GetExtent'),
    ('reference_count', 'GetReferenceCount'), ('ghost_level',
    'GetGhostLevel'), ('piece', 'GetPiece'), ('number_of_pieces',
    'GetNumberOfPieces'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'extent', 'ghost_level',
    'input_whole_extent', 'number_of_pieces', 'piece', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDataLIC2DExtentTranslator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDataLIC2DExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['extent', 'ghost_level', 'input_whole_extent',
            'number_of_pieces', 'piece', 'whole_extent']),
            title='Edit ImageDataLIC2DExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDataLIC2DExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

