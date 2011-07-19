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

from tvtk.tvtk_classes.object import Object


class OpenGLHardwareSupport(Object):
    """
    OpenGLHardwareSupport - open_gl rendering window
    
    Superclass: Object
    
    OpenGLHardwareSupport is an implementation of methods used to
    query open_gl and the hardware of what kind of graphics support is
    available. When VTK supports more than one Graphics API an abstract
    super class HardwareSupport should be implemented for this class
    to derive from.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLHardwareSupport, obj, update, **traits)
    
    def _get_extension_manager(self):
        return wrap_vtk(self._vtk_obj.GetExtensionManager())
    def _set_extension_manager(self, arg):
        old_val = self._get_extension_manager()
        self._wrap_call(self._vtk_obj.SetExtensionManager,
                        deref_vtk(arg))
        self.trait_property_changed('extension_manager', old_val, arg)
    extension_manager = traits.Property(_get_extension_manager, _set_extension_manager, help=\
        """
        Set/Get a reference to a RenderWindow which is Required for
        most methods of this class to work.
        """
    )

    def _get_number_of_fixed_texture_units(self):
        return self._vtk_obj.GetNumberOfFixedTextureUnits()
    number_of_fixed_texture_units = traits.Property(_get_number_of_fixed_texture_units, help=\
        """
        Return the number of fixed-function texture units.
        """
    )

    def _get_number_of_texture_units(self):
        return self._vtk_obj.GetNumberOfTextureUnits()
    number_of_texture_units = traits.Property(_get_number_of_texture_units, help=\
        """
        Return the total number of texture image units accessible by a
        shader program.
        """
    )

    def _get_supports_multi_texturing(self):
        return self._vtk_obj.GetSupportsMultiTexturing()
    supports_multi_texturing = traits.Property(_get_supports_multi_texturing, help=\
        """
        Test if multi_texturing is supported.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLHardwareSupport, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLHardwareSupport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit OpenGLHardwareSupport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLHardwareSupport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

