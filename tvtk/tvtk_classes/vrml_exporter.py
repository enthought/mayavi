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

from tvtk.tvtk_classes.exporter import Exporter


class VRMLExporter(Exporter):
    """
    VRMLExporter - export a scene into VRML 2.0 format.
    
    Superclass: Exporter
    
    VRMLExporter is a concrete subclass of Exporter that writes
    VRML 2.0 files. This is based on the VRML 2.0 draft #3 but it should
    be pretty stable since we aren't using any of the newer features.
    
    See Also:
    
    Exporter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVRMLExporter, obj, update, **traits)
    
    speed = traits.Float(4.0, enter_set=True, auto_set=False, help=\
        """
        Specify the Speed of navigation. Default is 4.
        """
    )
    def _speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpeed,
                        self.speed)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the VRML file to write.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('file_name',
    'GetFileName'), ('speed', 'GetSpeed'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name', 'speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VRMLExporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VRMLExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'speed']),
            title='Edit VRMLExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VRMLExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

