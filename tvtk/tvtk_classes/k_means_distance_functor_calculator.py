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

from tvtk.tvtk_classes.k_means_distance_functor import KMeansDistanceFunctor


class KMeansDistanceFunctorCalculator(KMeansDistanceFunctor):
    """
    KMeansDistanceFunctorCalculator - measure distance from k-means
    cluster centers using a user-specified expression
    
    Superclass: KMeansDistanceFunctor
    
    This is a subclass of the default k-means distance functor that
    allows the user to specify a distance function as a string. The
    provided expression is evaluated whenever the parenthesis operator is
    invoked but this is much slower than the default distance
    calculation.
    
    User-specified distance expressions should be written in terms of two
    vector variables named "x" and "y". The length of the vectors will be
    determined by the k-means request and all columns of interest in the
    request must contain values that may be converted to a floating point
    representation. (Strings and Object pointers are not allowed.) An
    example distance expression is "sqrt( (x0-y0)^2 + (x1-y1)^2 )" which
    computes Euclidian distance in a plane defined by the first 2
    coordinates of the vectors specified.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKMeansDistanceFunctorCalculator, obj, update, **traits)
    
    def _get_function_parser(self):
        return wrap_vtk(self._vtk_obj.GetFunctionParser())
    def _set_function_parser(self, arg):
        old_val = self._get_function_parser()
        self._wrap_call(self._vtk_obj.SetFunctionParser,
                        deref_vtk(arg))
        self.trait_property_changed('function_parser', old_val, arg)
    function_parser = traits.Property(_get_function_parser, _set_function_parser, help=\
        """
        Set/get the string containing an expression which evaluates to
        the distance metric used for k-means computation. The scalar
        variables "x0", "x1", ... "xn" and "y0", "y1", ..., "yn" refer to
        the coordinates involved in the computation.
        """
    )

    distance_expression = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/get the distance function expression.
        """
    )
    def _distance_expression_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceExpression,
                        self.distance_expression)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('distance_expression',
    'GetDistanceExpression'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'distance_expression'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KMeansDistanceFunctorCalculator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit KMeansDistanceFunctorCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['distance_expression']),
            title='Edit KMeansDistanceFunctorCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KMeansDistanceFunctorCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

