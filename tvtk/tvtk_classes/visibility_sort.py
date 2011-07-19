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


class VisibilitySort(Object):
    """
    VisibilitySort - Abstract class that can sort cell data along a
    viewpoint.
    
    Superclass: Object
    
    VisibilitySort encapsulates a method for depth sorting the cells
    of a DataSet for a given viewpoint.  It should be noted that
    subclasses are not required to give an absolutely correct sorting. 
    Many types of unstructured grids may have sorting cycles, meaning
    that there is no possible correct sorting.  Some subclasses also only
    give an approximate sorting in the interest of speed.
    
    Note:
    
    The Input field of this class tends to causes reference cycles.  To
    help break these cycles, garbage collection is enabled on this object
    and the input parameter is traced.  For this to work, though, an
    object in the loop holding the visibility sort should also report
    that to the garbage collector.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVisibilitySort, obj, update, **traits)
    
    direction = traits.Trait('back_to_front',
    tvtk_base.TraitRevPrefixMap({'front_to_back': 1, 'back_to_front': 0}), help=\
        """
        Set/Get the sorting direction.  Be default, the direction is set
        to back to front.
        """
    )
    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the data set containing the cells to sort.
        """
    )

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera that specifies the viewing parameters.
        """
    )

    max_cells_returned = traits.Trait(2147483647, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of cells that get_next_cells will return
        in one invocation.
        """
    )
    def _max_cells_returned_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxCellsReturned,
                        self.max_cells_returned)

    def _get_model_transform(self):
        return wrap_vtk(self._vtk_obj.GetModelTransform())
    def _set_model_transform(self, arg):
        old_val = self._get_model_transform()
        self._wrap_call(self._vtk_obj.SetModelTransform,
                        deref_vtk(arg))
        self.trait_property_changed('model_transform', old_val, arg)
    model_transform = traits.Property(_get_model_transform, _set_model_transform, help=\
        """
        Set/Get the matrix that transforms from object space to world
        space. Generally, you get this matrix from a call to get_matrix of
        a Prop3D (vtk_actor).
        """
    )

    def _get_inverse_model_transform(self):
        return wrap_vtk(self._vtk_obj.GetInverseModelTransform())
    inverse_model_transform = traits.Property(_get_inverse_model_transform, help=\
        """
        
        """
    )

    def _get_next_cells(self):
        return wrap_vtk(self._vtk_obj.GetNextCells())
    next_cells = traits.Property(_get_next_cells, help=\
        """
        To facilitate incremental sorting algorithms, the cells are
        retrieved in an iteration process.  That is, call init_traversal
        to start the iteration and call get_next_cells to get the cell IDs
        in order. However, for efficiencies sake, get_next_cells returns an
        ordered list of several id's in once call (but not necessarily
        all).  get_next_cells will return NULL once the entire sorted list
        is output.  The IdTypeArray returned from get_next_cells is a
        cached array, so do not delete it.  At the same note, do not
        expect the array to be valid after subsequent calls to
        get_next_cells.
        """
    )

    def init_traversal(self):
        """
        V.init_traversal()
        C++: virtual void InitTraversal()
        To facilitate incremental sorting algorithms, the cells are
        retrieved in an iteration process.  That is, call init_traversal
        to start the iteration and call get_next_cells to get the cell IDs
        in order. However, for efficiencies sake, get_next_cells returns an
        ordered list of several id's in once call (but not necessarily
        all).  get_next_cells will return NULL once the entire sorted list
        is output.  The IdTypeArray returned from get_next_cells is a
        cached array, so do not delete it.  At the same note, do not
        expect the array to be valid after subsequent calls to
        get_next_cells.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('direction', 'GetDirection'), ('max_cells_returned',
    'GetMaxCellsReturned'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'direction',
    'max_cells_returned'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VisibilitySort, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VisibilitySort properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['direction'], ['max_cells_returned']),
            title='Edit VisibilitySort properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VisibilitySort properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

