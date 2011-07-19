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

from tvtk.tvtk_classes.cell import Cell


class GenericCell(Cell):
    """
    GenericCell - provides thread-safe access to cells
    
    Superclass: Cell
    
    GenericCell is a class that provides access to concrete types of
    cells. It's main purpose is to allow thread-safe access to cells,
    supporting the DataSet::GetCell(vtkGenericCell *) method.
    GenericCell acts like any type of cell, it just dereferences an
    internal representation. The set_cell_type() methods use #define
    constants; these are defined in the file CellType.h.
    
    See Also:
    
    Cell DataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericCell, obj, update, **traits)
    
    cell_type = traits.Trait('empty_cell',
    tvtk_base.TraitRevPrefixMap({'polyhedron': 42, 'voxel': 11, 'pyramid': 14, 'wedge': 13, 'quadratic_pyramid': 27, 'triangle': 5, 'line': 3, 'polygon': 7, 'hexahedron': 12, 'quadratic_triangle': 22, 'quadratic_hexahedron': 25, 'triangle_strip': 6, 'bi_quadratic_quadratic_wedge': 32, 'quadratic_linear_quad': 30, 'poly_vertex': 2, 'pixel': 8, 'cubic_line': 35, 'empty_cell': 0, 'convex_point_set': 41, 'vertex': 1, 'quadratic_tetra': 24, 'tri_quadratic_hexahedron': 29, 'quad': 9, 'bi_quadratic_triangle': 34, 'quadratic_quad': 23, 'quadratic_wedge': 26, 'hexagonal_prism': 16, 'tetra': 10, 'quadratic_linear_wedge': 31, 'pentagonal_prism': 15, 'bi_quadratic_quad': 28, 'quadratic_edge': 21, 'bi_quadratic_quadratic_hexahedron': 33, 'poly_line': 4}), help=\
        """
        This method is used to support the
        DataSet::GetCell(vtkGenericCell *) method. It allows
        GenericCell to act like any cell type by dereferencing an
        internal instance of a concrete cell type. When you set the cell
        type, you are resetting a pointer to an internal cell which is
        then used for computation.
        """
    )
    def _cell_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellType,
                        self.cell_type_)

    def instantiate_cell(self, *args):
        """
        V.instantiate_cell(int) -> Cell
        C++: static Cell *InstantiateCell(int cellType)
        Instantiate a new Cell based on it's cell type value
        """
        ret = self._wrap_call(self._vtk_obj.InstantiateCell, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('cell_type', 'GetCellType'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cell_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericCell, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['cell_type'], []),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

