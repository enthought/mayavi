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


class Importer(Object):
    """
    Importer - importer abstract class
    
    Superclass: Object
    
    Importer is an abstract class that specifies the protocol for
    importing actors, cameras, lights and properties into a
    RenderWindow. The following takes place:
    1) Create a render_window and Renderer if none is provided.
    2) Call import_begin, if import_begin returns False, return
    3) Call read_data, which calls: a) Import the Actors b) Import the
       cameras c) Import the lights d) Import the Properties
    7) Call import_end
    
    Subclasses optionally implement the import_actors, import_cameras,
    import_lights and import_properties or read_data methods. An import_begin
    and import_end can optionally be provided to perform Importer-specific
    initialization and termination.  The Read method initiates the import
    process. If a render_window is provided, its Renderer will contained
    the imported objects. If the render_window has no Renderer, one is
    created. If no render_window is provided, both a render_window and
    Renderer will be created. Both the render_window and Renderer can be
    accessed using Get methods.
    
    See Also:
    
    ThreeDSImporter Exporter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImporter, obj, update, **traits)
    
    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    renderer = traits.Property(_get_renderer, help=\
        """
        
        """
    )

    def read(self):
        """
        V.read()
        C++: void Read()"""
        ret = self._vtk_obj.Read()
        return ret
        

    def update(self):
        """
        V.update()
        C++: void Update()"""
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Importer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Importer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Importer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Importer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

