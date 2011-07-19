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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class ProcrustesAlignmentFilter(PointSetAlgorithm):
    """
    ProcrustesAlignmentFilter - aligns a set of pointsets together
    
    Superclass: PointSetAlgorithm
    
    ProcrustesAlignmentFilter is a filter that takes a set of
    pointsets (any object derived from PointSet) and aligns them in a
    least-squares sense to their mutual mean. The algorithm is iterated
    until convergence, as the mean must be recomputed after each
    alignment.
    
    Call set_number_of_inputs(n) before calling set_input(_0) ...
    set_input(n-_1).
    
    Retrieve the outputs using get_output(_0) ... get_output(n-_1).
    
    The default (in LandmarkTransform) is for a similarity alignment.
    For a rigid-body alignment (to build a 'size-and-shape' model) use:
    
    
       get_landmark_transform()->_set_mode_to_rigid_body().
    
    Affine alignments are not normally used but are left in for
    completeness:
    
    
       get_landmark_transform()->_set_mode_to_affine().
    
    ProcrustesAlignmentFilter is an implementation of:
    
    
       J.C. Gower (1975)
       Generalized Procrustes Analysis. Psychometrika, 40:33-51.
    
    Caveats:
    
    All of the input pointsets must have the same number of points.
    
    Thanks:
    
    Tim Hutton and Rasmus Paulsen who developed and contributed this
    class
    
    See Also:
    
    LandmarkTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProcrustesAlignmentFilter, obj, update, **traits)
    
    start_from_centroid = tvtk_base.false_bool_trait(help=\
        """
        When on, the initial alignment is to the centroid of the cohort
        curves.  When off, the alignment is to the centroid of the first
        input.  Default is off for backward compatibility.
        """
    )
    def _start_from_centroid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartFromCentroid,
                        self.start_from_centroid_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> PointSet
        C++: PointSet *GetInput(int idx)
        Retrieve the input point set with index idx (usually only for
        pipeline tracing).
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(int, PointSet)
        C++: void SetInput(int idx, PointSet *p)
        V.set_input(int, DataObject)
        C++: void SetInput(int idx, DataObject *input)
        Specify the input pointset with index idx. Call set_number_of_inputs
        before calling this function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def _get_landmark_transform(self):
        return wrap_vtk(self._vtk_obj.GetLandmarkTransform())
    landmark_transform = traits.Property(_get_landmark_transform, help=\
        """
        Get the internal landmark transform. Use it to constrain the
        number of degrees of freedom of the alignment (i.e. rigid body,
        similarity, etc.). The default is a similarity alignment.
        """
    )

    def _get_mean_points(self):
        return wrap_vtk(self._vtk_obj.GetMeanPoints())
    mean_points = traits.Property(_get_mean_points, help=\
        """
        Get the estimated mean point cloud
        """
    )

    def set_number_of_inputs(self, *args):
        """
        V.set_number_of_inputs(int)
        C++: void SetNumberOfInputs(int n)
        Specify how many pointsets are going to be given as input.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfInputs, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('start_from_centroid',
    'GetStartFromCentroid'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'start_from_centroid', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProcrustesAlignmentFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['start_from_centroid'], [], []),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

