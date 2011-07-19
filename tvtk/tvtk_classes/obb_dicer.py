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

from tvtk.tvtk_classes.dicer import Dicer


class OBBDicer(Dicer):
    """
    OBBDicer - divide dataset into spatially aggregated pieces
    
    Superclass: Dicer
    
    OBBDicer separates the cells of a dataset into spatially
    aggregated pieces using a Oriented Bounding Box (OBB). These pieces
    can then be operated on by other filters (e.g., Threshold). One
    application is to break very large polygonal models into pieces and
    performing viewing and occlusion culling on the pieces.
    
    Refer to the superclass documentation (vtk_dicer) for more
    information.
    
    See Also:
    
    Dicer ConnectedDicer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOBBDicer, obj, update, **traits)
    
    _updateable_traits_ = \
    (('memory_limit', 'GetMemoryLimit'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('number_of_points_per_piece', 'GetNumberOfPointsPerPiece'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'), ('dice_mode',
    'GetDiceMode'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('field_data', 'GetFieldData'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_pieces', 'GetNumberOfPieces'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'field_data', 'global_warning_display',
    'release_data_flag', 'dice_mode', 'memory_limit', 'number_of_pieces',
    'number_of_points_per_piece', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OBBDicer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OBBDicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['field_data'], ['dice_mode'], ['memory_limit',
            'number_of_pieces', 'number_of_points_per_piece']),
            title='Edit OBBDicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OBBDicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

