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

from tvtk.tvtk_classes.abstract_transform import AbstractTransform


class WarpTransform(AbstractTransform):
    """
    WarpTransform - superclass for nonlinear geometric transformations
    
    Superclass: AbstractTransform
    
    WarpTransform provides a generic interface for nonlinear warp
    transformations.
    
    See Also:
    
    ThinPlateSplineTransform GridTransform GeneralTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWarpTransform, obj, update, **traits)
    
    inverse_iterations = traits.Int(500, enter_set=True, auto_set=False, help=\
        """
        Set the maximum number of iterations for the inverse
        transformation.  The default is 500, but usually only 2 to 5
        iterations are used.  The inversion method is fairly robust, and
        it should converge for nearly all smooth transformations that do
        not fold back on themselves.
        """
    )
    def _inverse_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseIterations,
                        self.inverse_iterations)

    inverse_tolerance = traits.Float(0.001, enter_set=True, auto_set=False, help=\
        """
        Set the tolerance for inverse transformation. The default is
        0.001.
        """
    )
    def _inverse_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseTolerance,
                        self.inverse_tolerance)

    def _get_inverse_flag(self):
        return self._vtk_obj.GetInverseFlag()
    inverse_flag = traits.Property(_get_inverse_flag, help=\
        """
        Get the inverse flag of the transformation.  This flag is set to
        zero when the transformation is first created, and is flipped
        each time Inverse() is called.
        """
    )

    def template_transform_inverse(self, *args):
        """
        V.template_transform_inverse((float, float, float), [float, float,
            float])
        C++: void TemplateTransformInverse(const double in[3],
            double out[3])
        V.template_transform_inverse((float, float, float), [float, float,
            float], [[float, float, float], [float, float, float], [float,
             float, float]])
        C++: void TemplateTransformInverse(const double in[3],
            double out[3], double derivative[3][3])
        Do not use these methods.  They exists only as a work-around for
        internal templated functions (I really didn't want to make the
        Forward/Inverse methods public, is there a decent work around for
        this sort of thing?)
        """
        ret = self._wrap_call(self._vtk_obj.TemplateTransformInverse, *args)
        return ret

    def template_transform_point(self, *args):
        """
        V.template_transform_point((float, float, float), [float, float,
            float])
        C++: void TemplateTransformPoint(const double in[3],
            double out[3])
        V.template_transform_point((float, float, float), [float, float,
            float], [[float, float, float], [float, float, float], [float,
             float, float]])
        C++: void TemplateTransformPoint(const double in[3],
            double out[3], double derivative[3][3])
        Do not use these methods.  They exists only as a work-around for
        internal templated functions (I really didn't want to make the
        Forward/Inverse methods public, is there a decent work around for
        this sort of thing?)
        """
        ret = self._wrap_call(self._vtk_obj.TemplateTransformPoint, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('inverse_iterations',
    'GetInverseIterations'), ('inverse_tolerance', 'GetInverseTolerance'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'inverse_iterations',
    'inverse_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WarpTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WarpTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['inverse_iterations', 'inverse_tolerance']),
            title='Edit WarpTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WarpTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

