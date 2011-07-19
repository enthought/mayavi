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

from tvtk.tvtk_classes.object import Object


class ExtentTranslator(Object):
    """
    ExtentTranslator - Generates a structured extent from unstructured.
    
    Superclass: Object
    
    ExtentTranslator generates a structured extent from an
    unstructured extent.  It uses a recursive scheme that splits the
    largest axis.  A hard coded extent can be used for a starting point.
    
    Caveats:
    
    This object is still under development.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtentTranslator, obj, update, **traits)
    
    def get_split_mode(self):
        """
        V.get_split_mode() -> int
        C++: int GetSplitMode()
        How should the streamer break up extents. Block mode tries to
        break an extent up into cube blocks.  It always chooses the
        largest axis to split. Slab mode first breaks up the Z axis.  If
        it gets to one slice, then it starts breaking up other axes.
        """
        ret = self._vtk_obj.GetSplitMode()
        return ret
        

    def set_split_mode_to_block(self):
        """
        V.set_split_mode_to_block()
        C++: void SetSplitModeToBlock()
        How should the streamer break up extents. Block mode tries to
        break an extent up into cube blocks.  It always chooses the
        largest axis to split. Slab mode first breaks up the Z axis.  If
        it gets to one slice, then it starts breaking up other axes.
        """
        self._vtk_obj.SetSplitModeToBlock()

    def set_split_mode_to_x_slab(self):
        """
        V.set_split_mode_to_x_slab()
        C++: void SetSplitModeToXSlab()
        How should the streamer break up extents. Block mode tries to
        break an extent up into cube blocks.  It always chooses the
        largest axis to split. Slab mode first breaks up the Z axis.  If
        it gets to one slice, then it starts breaking up other axes.
        """
        self._vtk_obj.SetSplitModeToXSlab()

    def set_split_mode_to_y_slab(self):
        """
        V.set_split_mode_to_y_slab()
        C++: void SetSplitModeToYSlab()
        How should the streamer break up extents. Block mode tries to
        break an extent up into cube blocks.  It always chooses the
        largest axis to split. Slab mode first breaks up the Z axis.  If
        it gets to one slice, then it starts breaking up other axes.
        """
        self._vtk_obj.SetSplitModeToYSlab()

    def set_split_mode_to_z_slab(self):
        """
        V.set_split_mode_to_z_slab()
        C++: void SetSplitModeToZSlab()
        How should the streamer break up extents. Block mode tries to
        break an extent up into cube blocks.  It always chooses the
        largest axis to split. Slab mode first breaks up the Z axis.  If
        it gets to one slice, then it starts breaking up other axes.
        """
        self._vtk_obj.SetSplitModeToZSlab()

    piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the piece/_num_pieces. Set the whole_extent and then call
        piece_to_extent. The result can be obtained from the Extent ivar.
        """
    )
    def _piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPiece,
                        self.piece)

    number_of_pieces = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the piece/_num_pieces. Set the whole_extent and then call
        piece_to_extent. The result can be obtained from the Extent ivar.
        """
    )
    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    whole_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the piece/_num_pieces. Set the whole_extent and then call
        piece_to_extent. The result can be obtained from the Extent ivar.
        """
    )
    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    def piece_to_extent(self):
        """
        V.piece_to_extent() -> int
        C++: virtual int PieceToExtent()
        These are the main methods that should be called. These methods
        are responsible for converting a piece to an extent. The
        signatures without arguments are only thread safe when each
        thread accesses a different instance. The signatures with
        arguements are fully thread safe.
        """
        ret = self._vtk_obj.PieceToExtent()
        return ret
        

    def piece_to_extent_by_points(self):
        """
        V.piece_to_extent_by_points() -> int
        C++: virtual int PieceToExtentByPoints()
        These are the main methods that should be called. These methods
        are responsible for converting a piece to an extent. The
        signatures without arguments are only thread safe when each
        thread accesses a different instance. The signatures with
        arguements are fully thread safe.
        """
        ret = self._vtk_obj.PieceToExtentByPoints()
        return ret
        

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
            return super(ExtentTranslator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['extent', 'ghost_level', 'number_of_pieces',
            'piece', 'whole_extent']),
            title='Edit ExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

