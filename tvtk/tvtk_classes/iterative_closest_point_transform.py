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

from tvtk.tvtk_classes.linear_transform import LinearTransform


class IterativeClosestPointTransform(LinearTransform):
    """
    IterativeClosestPointTransform - Implementation of the ICP
    algorithm.
    
    Superclass: LinearTransform
    
    Match two surfaces using the iterative closest point (ICP) algorithm.
    The core of the algorithm is to match each vertex in one surface with
    the closest surface point on the other, then apply the transformation
    that modify one surface to best match the other (in a least square
    sense). This has to be iterated to get proper convergence of the
    surfaces.
    
    Note:
    
    Use TransformPolyDataFilter to apply the resulting ICP transform
    to your data. You might also set it to your actor's user transform.
    
    Note:
    
    This class makes use of LandmarkTransform internally to compute
    the best fit. Use the get_landmark_transform member to get a pointer to
    that transform and set its parameters. You might, for example,
    constrain the number of degrees of freedom of the solution (i.e.
    rigid body, similarity, etc.) by checking the LandmarkTransform
    documentation for its set_mode member.
    
    See Also:
    
    LandmarkTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIterativeClosestPointTransform, obj, update, **traits)
    
    start_by_matching_centroids = tvtk_base.false_bool_trait(help=\
        """
        Starts the process by translating source centroid to target
        centroid. The default is Off.
        """
    )
    def _start_by_matching_centroids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartByMatchingCentroids,
                        self.start_by_matching_centroids_)

    check_mean_distance = tvtk_base.false_bool_trait(help=\
        """
        Force the algorithm to check the mean distance between two
        iterations. Default is Off.
        """
    )
    def _check_mean_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckMeanDistance,
                        self.check_mean_distance_)

    mean_distance_mode = traits.Trait('rms',
    tvtk_base.TraitRevPrefixMap({'rms': 0, 'absolute_value': 1}), help=\
        """
        Specify the mean distance mode. This mode expresses how the mean
        distance is computed. The RMS mode is the square root of the
        average of the sum of squares of the closest point distances. The
        Absolute Value mode is the mean of the sum of absolute values of
        the closest point distances. The default is VTK_ICP_MODE_RMS
        """
    )
    def _mean_distance_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMeanDistanceMode,
                        self.mean_distance_mode_)

    maximum_number_of_landmarks = traits.Int(200, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of landmarks sampled in your dataset.
        If your dataset is dense, then you will typically not need all
        the points to compute the ICP transform. The default is 200.
        """
    )
    def _maximum_number_of_landmarks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfLandmarks,
                        self.maximum_number_of_landmarks)

    def _get_target(self):
        return wrap_vtk(self._vtk_obj.GetTarget())
    def _set_target(self, arg):
        old_val = self._get_target()
        self._wrap_call(self._vtk_obj.SetTarget,
                        deref_vtk(arg))
        self.trait_property_changed('target', old_val, arg)
    target = traits.Property(_get_target, _set_target, help=\
        """
        Specify the source and target data sets.
        """
    )

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set/Get a spatial locator for speeding up the search process. An
        instance of CellLocator is used by default.
        """
    )

    maximum_number_of_iterations = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the  maximum number of iterations. Default is 50.
        """
    )
    def _maximum_number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfIterations,
                        self.maximum_number_of_iterations)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Specify the source and target data sets.
        """
    )

    maximum_mean_distance = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum mean distance between two iteration. If the
        mean distance is lower than this, the convergence stops. The
        default is 0.01.
        """
    )
    def _maximum_mean_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumMeanDistance,
                        self.maximum_mean_distance)

    def _get_landmark_transform(self):
        return wrap_vtk(self._vtk_obj.GetLandmarkTransform())
    landmark_transform = traits.Property(_get_landmark_transform, help=\
        """
        Get the internal landmark transform. Use it to constrain the
        number of degrees of freedom of the solution (i.e. rigid body,
        similarity, etc.).
        """
    )

    def _get_mean_distance(self):
        return self._vtk_obj.GetMeanDistance()
    mean_distance = traits.Property(_get_mean_distance, help=\
        """
        Get the mean distance between the last two iterations.
        """
    )

    def _get_number_of_iterations(self):
        return self._vtk_obj.GetNumberOfIterations()
    number_of_iterations = traits.Property(_get_number_of_iterations, help=\
        """
        Get the number of iterations since the last update
        """
    )

    _updateable_traits_ = \
    (('maximum_mean_distance', 'GetMaximumMeanDistance'),
    ('maximum_number_of_landmarks', 'GetMaximumNumberOfLandmarks'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('start_by_matching_centroids',
    'GetStartByMatchingCentroids'), ('maximum_number_of_iterations',
    'GetMaximumNumberOfIterations'), ('check_mean_distance',
    'GetCheckMeanDistance'), ('reference_count', 'GetReferenceCount'),
    ('mean_distance_mode', 'GetMeanDistanceMode'))
    
    _full_traitnames_list_ = \
    (['check_mean_distance', 'debug', 'global_warning_display',
    'start_by_matching_centroids', 'mean_distance_mode',
    'maximum_mean_distance', 'maximum_number_of_iterations',
    'maximum_number_of_landmarks'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IterativeClosestPointTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IterativeClosestPointTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['check_mean_distance', 'start_by_matching_centroids'],
            ['mean_distance_mode'], ['maximum_mean_distance',
            'maximum_number_of_iterations', 'maximum_number_of_landmarks']),
            title='Edit IterativeClosestPointTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IterativeClosestPointTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

