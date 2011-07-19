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


class LandmarkTransform(LinearTransform):
    """
    LandmarkTransform - a linear transform specified by two
    corresponding point sets
    
    Superclass: LinearTransform
    
    A LandmarkTransform is defined by two sets of landmarks, the
    transform computed gives the best fit mapping one onto the other, in
    a least squares sense. The indices are taken to correspond, so point
    1 in the first set will get mapped close to point 1 in the second
    set, etc. Call set_source_landmarks and set_target_landmarks to specify
    the two sets of landmarks, ensure they have the same number of
    points.
    
    Caveats:
    
    Whenever you add, subtract, or set points you must call Modified() on
    the Points object, or the transformation might not update.
    
    See Also:
    
    LinearTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLandmarkTransform, obj, update, **traits)
    
    mode = traits.Trait('similarity',
    tvtk_base.TraitRevPrefixMap({'rigid_body': 6, 'affine': 12, 'similarity': 7}), help=\
        """
        Set the number of degrees of freedom to constrain the solution
        to. Rigidbody (VTK_LANDMARK_RIGIDBODY): rotation and translation
        only. Similarity (VTK_LANDMARK_SIMILARITY): rotation, translation
        and
                   isotropic scaling. Affine (VTK_LANDMARK_AFFINE):
        collinearity is preserved.
               Ratios of distances along a line are preserved. The
        default is similarity.
        """
    )
    def _mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMode,
                        self.mode_)

    def _get_source_landmarks(self):
        return wrap_vtk(self._vtk_obj.GetSourceLandmarks())
    def _set_source_landmarks(self, arg):
        old_val = self._get_source_landmarks()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetSourceLandmarks,
                        my_arg[0])
        self.trait_property_changed('source_landmarks', old_val, arg)
    source_landmarks = traits.Property(_get_source_landmarks, _set_source_landmarks, help=\
        """
        Specify the source and target landmark sets. The two sets must
        have the same number of points.  If you add or change points in
        these objects, you must call Modified() on them or the
        transformation might not update.
        """
    )

    def _get_target_landmarks(self):
        return wrap_vtk(self._vtk_obj.GetTargetLandmarks())
    def _set_target_landmarks(self, arg):
        old_val = self._get_target_landmarks()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetTargetLandmarks,
                        my_arg[0])
        self.trait_property_changed('target_landmarks', old_val, arg)
    target_landmarks = traits.Property(_get_target_landmarks, _set_target_landmarks, help=\
        """
        Specify the source and target landmark sets. The two sets must
        have the same number of points.  If you add or change points in
        these objects, you must call Modified() on them or the
        transformation might not update.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('mode',
    'GetMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LandmarkTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LandmarkTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['mode'], []),
            title='Edit LandmarkTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LandmarkTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

