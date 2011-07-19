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


class OnePieceExtentTranslator(ExtentTranslator):
    """
    OnePieceExtentTranslator - Returns the whole extent for any piece..
    
    Superclass: ExtentTranslator
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOnePieceExtentTranslator, obj, update, **traits)
    
    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('extent',
    'GetExtent'), ('reference_count', 'GetReferenceCount'),
    ('ghost_level', 'GetGhostLevel'), ('piece', 'GetPiece'),
    ('number_of_pieces', 'GetNumberOfPieces'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'extent', 'ghost_level',
    'number_of_pieces', 'piece', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OnePieceExtentTranslator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OnePieceExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['extent', 'ghost_level', 'number_of_pieces',
            'piece', 'whole_extent']),
            title='Edit OnePieceExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OnePieceExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

