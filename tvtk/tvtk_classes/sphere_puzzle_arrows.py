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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class SpherePuzzleArrows(PolyDataAlgorithm):
    """
    SpherePuzzleArrows - Visualize permutation of the sphere puzzle.
    
    Superclass: PolyDataAlgorithm
    
    SpherePuzzleArrows creates
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpherePuzzleArrows, obj, update, **traits)
    
    permutation = traits.Array(shape=(32,), value=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Permutation is an array of puzzle piece ids. Arrows will be
        generated for any id that does not contain itself. Permutation[3]
        = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow
        from location 3 to 10.
        """
    )
    def _permutation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPermutation,
                        self.permutation)

    def set_permutation_component(self, *args):
        """
        V.set_permutation_component(int, int)
        C++: void SetPermutationComponent(int comp, int val)
        Permutation is an array of puzzle piece ids. Arrows will be
        generated for any id that does not contain itself. Permutation[3]
        = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow
        from location 3 to 10.
        """
        ret = self._wrap_call(self._vtk_obj.SetPermutationComponent, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('permutation', 'GetPermutation'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'permutation', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpherePuzzleArrows, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SpherePuzzleArrows properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['permutation']),
            title='Edit SpherePuzzleArrows properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpherePuzzleArrows properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

