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

from tvtk.tvtk_classes.painter import Painter


class SurfaceLICPainter(Painter):
    """
    SurfaceLICPainter - painter that performs LIC on the surface of
    
    Superclass: Painter
    
    SurfaceLICPainter painter performs LIC on the surface of arbitrary
     geometry. Point vectors are used as the vector field for generating
    the LIC.
     The implementation is based on "Image Space Based Visualization on
    Unsteady
     Flow on Surfaces" by Laramee, Jobard and Hauser appeared in
    proceedings of
     IEEE Visualization '03, pages 131-138.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSurfaceLICPainter, obj, update, **traits)
    
    enhanced_lic = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable enhanced LIC that improves image quality by
        increasing inter-streamline contrast while suppressing artifacts.
        Enhanced LIC performs two passes of LIC, with a 3x3 Laplacian
        high-pass filter in between that processes the output of pass #1
        LIC and forwards the result as the input 'noise' to pass #2 LIC.
        This flag is automatically turned off during user interaction.
        """
    )
    def _enhanced_lic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnhancedLIC,
                        self.enhanced_lic_)

    enable = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable this painter.
        """
    )
    def _enable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnable,
                        self.enable_)

    number_of_steps = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of integration steps in each direction.
        """
    )
    def _number_of_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSteps,
                        self.number_of_steps)

    step_size = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the step size (in pixels).
        """
    )
    def _step_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStepSize,
                        self.step_size)

    lic_intensity = traits.Trait(0.8, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Control the contribution of the LIC in the final output image.
        0.0 produces same result as disabling LIC alltogether, while 1.0
        implies show LIC result alone.
        """
    )
    def _lic_intensity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLICIntensity,
                        self.lic_intensity)

    def _get_lic_success(self):
        return self._vtk_obj.GetLICSuccess()
    lic_success = traits.Property(_get_lic_success, help=\
        """
        Check if the LIC process runs properly.
        """
    )

    def _get_rendering_preparation_success(self):
        return self._vtk_obj.GetRenderingPreparationSuccess()
    rendering_preparation_success = traits.Property(_get_rendering_preparation_success, help=\
        """
        Check if prepare_for_rendering passes.
        """
    )

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *)
        Returns true is the rendering context supports extensions needed
        by this painter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def set_input_array_to_process(self, *args):
        """
        V.set_input_array_to_process(int, string)
        C++: void SetInputArrayToProcess(int fieldAssociation,
            const char *name)
        V.set_input_array_to_process(int, int)
        C++: void SetInputArrayToProcess(int fieldAssociation,
            int fieldAttributeType)
        Set the vectors to used for applying LIC. By default point
        vectors are used. Arguments are same as those passed to
        Algorithm::SetInputArrayToProcess except the first 3 arguments
        i.e. idx, port, connection.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputArrayToProcess, *args)
        return ret

    _updateable_traits_ = \
    (('enable', 'GetEnable'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('enhanced_lic', 'GetEnhancedLIC'),
    ('debug', 'GetDebug'), ('number_of_steps', 'GetNumberOfSteps'),
    ('step_size', 'GetStepSize'), ('lic_intensity', 'GetLICIntensity'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['debug', 'enable', 'enhanced_lic', 'global_warning_display',
    'lic_intensity', 'number_of_steps', 'step_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SurfaceLICPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SurfaceLICPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enable', 'enhanced_lic'], [], ['lic_intensity',
            'number_of_steps', 'step_size']),
            title='Edit SurfaceLICPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SurfaceLICPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

