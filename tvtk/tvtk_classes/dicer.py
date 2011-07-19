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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class Dicer(DataSetAlgorithm):
    """
    Dicer - abstract superclass to divide dataset into pieces
    
    Superclass: DataSetAlgorithm
    
    Subclasses of Dicer divides the input dataset into separate
    pieces.  These pieces can then be operated on by other filters (e.g.,
    Threshold). One application is to break very large polygonal
    models into pieces and performing viewing and occlusion culling on
    the pieces. Multiple pieces can also be streamed through the
    visualization pipeline.
    
    To use this filter, you must specify the execution mode of the
    filter; i.e., set the way that the piece size is controlled (do this
    by setting the dice_mode ivar). The filter does not change the
    geometry or topology of the input dataset, rather it generates
    integer numbers that indicate which piece a particular point belongs
    to (i.e., it modifies the point and cell attribute data). The integer
    number can be placed into the output scalar data, or the output field
    data.
    
    Caveats:
    
    The number of pieces generated may not equal the specified number of
    pieces. Use the method get_number_of_actual_pieces() after filter
    execution to get the actual number of pieces generated.
    
    See Also:
    
    OBBDicer ConnectedDicer SpatialDicer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDicer, obj, update, **traits)
    
    field_data = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which controls whether to generate point scalar
        data or point field data. If this flag is off, scalar data is
        generated.  Otherwise, field data is generated. Note that the
        generated the data are integer numbers indicating which piece a
        particular point belongs to.
        """
    )
    def _field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldData,
                        self.field_data_)

    dice_mode = traits.Trait('number_of_points_per_piece',
    tvtk_base.TraitRevPrefixMap({'number_of_points_per_piece': 0, 'memory_limit_per_piece': 2, 'specified_number_of_pieces': 1}), help=\
        """
        Specify the method to determine how many pieces the data should
        be broken into. By default, the number of points per piece is
        used.
        """
    )
    def _dice_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiceMode,
                        self.dice_mode_)

    memory_limit = traits.Trait(50000, traits.Range(100, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control piece size based on a memory limit.  (This ivar has
        effect only when the dice_mode is set to
        set_dice_mode_to_memory_limit()). The memory limit should be set in
        kilobytes.
        """
    )
    def _memory_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMemoryLimit,
                        self.memory_limit)

    number_of_points_per_piece = traits.Trait(5000, traits.Range(1000, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control piece size based on the maximum number of points per
        piece. (This ivar has effect only when the dice_mode is set to
        set_dice_mode_to_number_of_points().)
        """
    )
    def _number_of_points_per_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPointsPerPiece,
                        self.number_of_points_per_piece)

    number_of_pieces = traits.Trait(10, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of pieces the object is to be separated into.
        (This ivar has effect only when the dice_mode is set to
        set_dice_mode_to_specified_number()). Note that the ivar
        number_of_pieces is a target - depending on the particulars of the
        data, more or less number of pieces than the target value may be
        created.
        """
    )
    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    def _get_number_of_actual_pieces(self):
        return self._vtk_obj.GetNumberOfActualPieces()
    number_of_actual_pieces = traits.Property(_get_number_of_actual_pieces, help=\
        """
        Use the following method after the filter has updated to
        determine the actual number of pieces the data was separated
        into.
        """
    )

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
            return super(Dicer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Dicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['field_data'], ['dice_mode'], ['memory_limit',
            'number_of_pieces', 'number_of_points_per_piece']),
            title='Edit Dicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Dicer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

