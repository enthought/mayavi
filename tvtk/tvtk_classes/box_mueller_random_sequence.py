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

from tvtk.tvtk_classes.gaussian_random_sequence import GaussianRandomSequence


class BoxMuellerRandomSequence(GaussianRandomSequence):
    """
    BoxMuellerRandomSequence - Gaussian sequence of pseudo random
    numbers implemented with the Box-Mueller transform
    
    Superclass: GaussianRandomSequence
    
    GaussianRandomSequence is a sequence of pseudo random numbers
    distributed according to the Gaussian/normal distribution (mean=0 and
    standard deviation=1).
    
    It based is calculation from a uniformly distributed pseudo random
    sequence. The initial sequence is a MinimalStandardRandomSequence.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoxMuellerRandomSequence, obj, update, **traits)
    
    def _get_uniform_sequence(self):
        return wrap_vtk(self._vtk_obj.GetUniformSequence())
    def _set_uniform_sequence(self, arg):
        old_val = self._get_uniform_sequence()
        self._wrap_call(self._vtk_obj.SetUniformSequence,
                        deref_vtk(arg))
        self.trait_property_changed('uniform_sequence', old_val, arg)
    uniform_sequence = traits.Property(_get_uniform_sequence, _set_uniform_sequence, help=\
        """
        Return the uniformly distributed sequence of random numbers.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoxMuellerRandomSequence, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BoxMuellerRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit BoxMuellerRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoxMuellerRandomSequence properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

