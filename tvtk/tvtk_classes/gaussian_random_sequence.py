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

from tvtk.tvtk_classes.random_sequence import RandomSequence


class GaussianRandomSequence(RandomSequence):
    """
    GaussianRandomSequence - Gaussian sequence of pseudo random numbers
    
    Superclass: RandomSequence
    
    GaussianRandomSequence is a sequence of pseudo random numbers
    distributed according to the Gaussian/normal distribution (mean=0 and
    standard deviation=1)
    
    This is just an interface.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGaussianRandomSequence, obj, update, **traits)
    
    def get_scaled_value(self, *args):
        """
        V.get_scaled_value(float, float) -> float
        C++: virtual double GetScaledValue(double mean,
            double standardDeviation)
        Convenient method to return a value given the mean and standard
        deviation of the Gaussian distribution from the the Gaussian
        distribution of mean=0 and standard deviation=1.0. There is an
        initial implementation that can be overridden by a subclass.
        """
        ret = self._wrap_call(self._vtk_obj.GetScaledValue, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GaussianRandomSequence, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GaussianRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GaussianRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GaussianRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

