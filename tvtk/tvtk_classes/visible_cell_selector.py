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


class VisibleCellSelector(Object):
    """
    VisibleCellSelector - A helper that orchestrates color buffer
    
    Superclass: Object
    
    DEPRECATED: Please refer to HardwareSelector instead. This class
    can be used to determine what cells are visible within a given
    rectangle of the render_window. To use it, call in order,
    set_renderer(), set_area(), set_processor_id(), set_render_passes(), and
    then Select(). Select will cause the attached Renderer to render
    in a special color mode, where each cell is given it own color so
    that later inspection of the Rendered Pixels can determine what cells
    are visible. In practice up to five different rendering passes may
    occur depending on your choices in set_render_passes. After Select(), a
    list of the visible cells can be obtained by calling
    get_selected_ids().
    
    Limitations: Antialiasing will break this class. If your graphics
    card settings force their use this class will return invalid results.
    
    Currently only cells from poly_data_mappers can be selected from. When
    Renderer is put into a select_mode, it temporarily swaps in a new
    IdentColoredPainter to do the color index rendering of each cell
    in each Prop that it renders. Until alternatives to
    IdentColoredPainter exist that can do a similar coloration of
    other DataSet types, only polygonal data can be selected. If you
    need to select other data types, consider using DataSetMapper and
    turning on it's pass_through_cell_ids feature, or using
    FrustumExtractor.
    
    Only Opaque geometry in Actors is selected from. Assemblies and
    LODMappers are not currently supported.
    
    During selection, visible datasets that can not be selected from are
    temporarily hidden so as not to produce invalid indices from their
    colors.
    
    See Also:
    
    IdentColoredPainter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVisibleCellSelector, obj, update, **traits)
    
    processor_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Call to let this know what processor number to render as in the
        processor select pass. Internally this adds 1 to pid because 0 is
        reserved for miss.
        """
    )
    def _processor_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessorId,
                        self.processor_id)

    def get_area(self, *args):
        """
        V.get_area(int, int, int, int)
        C++: void GetArea(unsigned int &x0, unsigned int &y0,
            unsigned int &x1, unsigned int &y1)
        The caller of set_area can use to check for cropped limits.
        """
        ret = self._wrap_call(self._vtk_obj.GetArea, *args)
        return ret

    def set_area(self, *args):
        """
        V.set_area(int, int, int, int)
        C++: void SetArea(unsigned int x0, unsigned int y0,
            unsigned int x1, unsigned int y1)
        Call to set the selection area region. This crops the selected
        area to the renderers pixel limits.
        """
        ret = self._wrap_call(self._vtk_obj.SetArea, *args)
        return ret

    def get_actor_from_id(self, *args):
        """
        V.get_actor_from_id(int) -> Prop
        C++: Prop *GetActorFromId(IdType id)
        After a select, this will return a pointer to the actor
        corresponding to a particular id. This will return NULL if id is
        out of range.
        """
        ret = self._wrap_call(self._vtk_obj.GetActorFromId, *args)
        return wrap_vtk(ret)

    def get_selected_ids(self, *args):
        """
        V.get_selected_ids(IdTypeArray)
        C++: void GetSelectedIds(IdTypeArray *ToCopyInto)
        V.get_selected_ids(Selection)
        C++: void GetSelectedIds(Selection *ToCopyInto)
        After Select(), this will return the list of selected Ids. The
        processor_id and Actor Id are returned in the first two
        components. The cell_id is returned in the last two components
        (only 64 bits total).
        """
        my_args = deref_array(args, [['vtkIdTypeArray'], ['vtkSelection']])
        ret = self._wrap_call(self._vtk_obj.GetSelectedIds, *my_args)
        return ret

    def get_selected_vertices(self, *args):
        """
        V.get_selected_vertices(IdTypeArray, IdTypeArray)
        C++: void GetSelectedVertices(IdTypeArray *VertexPointers,
            IdTypeArray *VertexIds)
        After Select(), (assuming do_vertex_id is on), the will return
        arrays that describe which cell vertices are visible. The
        vertex_pointers array contains one index into the vertex_ids array
        for every visible cell. Any index may be -1 in which case no
        vertices were visible for that cell. The vertex_ids array contains
        a set of integers for each cell that has visible vertices. The
        first entry in the set is the number of visible vertices. The
        rest are visible vertex ranks. A set such at 2,0,4, means that a
        particular polygon's first and fifth vertices were visible.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedVertices, *my_args)
        return ret

    def print_selected_ids(self, *args):
        """
        V.print_selected_ids(IdTypeArray)
        C++: void PrintSelectedIds(IdTypeArray *IdsToPrint)
        For debugging - prints out the list of selected ids.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.PrintSelectedIds, *my_args)
        return ret

    def select(self):
        """
        V.select()
        C++: void Select()
        Execute the selection algorithm.
        """
        ret = self._vtk_obj.Select()
        return ret
        

    def set_render_passes(self, *args):
        """
        V.set_render_passes(int, int, int, int, int, int)
        C++: void SetRenderPasses(int DoProcessor, int DoActor,
            int DoCellIdHi, int DoCellIdMid, int DoCellIdLo,
            int DoVertexId=0)
        Call to let this know what selection render passes to do. If you
        have only one processor or one actor, you can leave do_processor
        and do_actor as false (the default). If you have less than 2^48
        cells in any actor, you do not need the cell_id_hi pass, or
        similarly if you have less than 2^24 cells, you do not need
        do_cell_id_mid. The do_point_id will enable another render pass for
        determining visible vertices.
        """
        ret = self._wrap_call(self._vtk_obj.SetRenderPasses, *args)
        return ret

    def set_renderer(self, *args):
        """
        V.set_renderer(Renderer)
        C++: virtual void SetRenderer(Renderer *)
        Call to let this know where to select within.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRenderer, *my_args)
        return ret

    _updateable_traits_ = \
    (('processor_id', 'GetProcessorId'), ('reference_count',
    'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'processor_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VisibleCellSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VisibleCellSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['processor_id']),
            title='Edit VisibleCellSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VisibleCellSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

