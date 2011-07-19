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

from tvtk.tvtk_classes.warp_transform import WarpTransform


class ThinPlateSplineTransform(WarpTransform):
    """
    ThinPlateSplineTransform - a nonlinear warp transformation
    
    Superclass: WarpTransform
    
    ThinPlateSplineTransform describes a nonlinear warp transform
    defined by a set of source and target landmarks. Any point on the
    mesh close to a source landmark will be moved to a place close to the
    corresponding target landmark. The points in between are interpolated
    smoothly using Bookstein's Thin Plate Spline algorithm.
    
    To obtain a correct TPS warp, use the r2_log_r kernel if your data is
    2d, and the R kernel if your data is 3d. Or you can specify your own
    RBF. (Hence this class is more general than a pure TPS transform.)
    
    Caveats:
    
    1) The inverse transform is calculated using an iterative method, and
    is several times more expensive than the forward transform.
    2) Whenever you add, subtract, or set points you must call Modified()
       on the Points object, or the transformation might not update.
    3) Collinear point configurations (except those that lie in the XY
       plane) result in an unstable transformation.
    
    See Also:
    
    GridTransform GeneralTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThinPlateSplineTransform, obj, update, **traits)
    
    basis = traits.Trait('r2_log_r',
    tvtk_base.TraitRevPrefixMap({'r': 1, 'r2_log_r': 2}), help=\
        """
        Specify the radial basis function to use.  The default is r2_log_r
        which is appropriate for 2d. Use |R| (_set_basis_to_r) if your data
        is 3d. Alternatively specify your own basis function, however
        this will mean that the transform will no longer be a true
        thin-plate spline.
        """
    )
    def _basis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBasis,
                        self.basis_)

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
        Set the source landmarks for the warp.  If you add or change the
        Points object, you must call Modified() on it or the
        transformation might not update.
        """
    )

    sigma = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the 'stiffness' of the spline. The default is 1.0.
        """
    )
    def _sigma_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSigma,
                        self.sigma)

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
        Set the target landmarks for the warp.  If you add or change the
        Points object, you must call Modified() on it or the
        transformation might not update.
        """
    )

    _updateable_traits_ = \
    (('inverse_iterations', 'GetInverseIterations'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('basis',
    'GetBasis'), ('reference_count', 'GetReferenceCount'), ('debug',
    'GetDebug'), ('sigma', 'GetSigma'), ('inverse_tolerance',
    'GetInverseTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'basis', 'inverse_iterations',
    'inverse_tolerance', 'sigma'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThinPlateSplineTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThinPlateSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['basis'], ['inverse_iterations',
            'inverse_tolerance', 'sigma']),
            title='Edit ThinPlateSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThinPlateSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

