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

from tvtk.tvtk_classes.importer import Importer


class VRMLImporter(Importer):
    """
    VRMLImporter - imports VRML 2.0 files.
    
    Superclass: Importer
    
    VRMLImporter imports VRML 2.0 files into vtk.
    
    Caveats:
    
    These nodes are currently supported:
         Appearance                              indexed_face_set
         Box                                     indexed_line_set
         Color                                   Material
         Cone                                    Shape
         Coordinate                              Sphere
         Cylinder                                Transform
         directional_light
    
    As you can see this implementation focuses on getting the geometry
    translated.  The routes and scripting nodes are ignored since they
    deal with directly accessing a nodes internal structure based on the
    VRML spec. Since this is a translation the internal data structures
    differ greatly from the VRML spec and the External Authoring
    Interface (see the VRML spec). The DEF/USE mechanism does allow the
    Vtk user to extract objects from the scene and directly manipulate
    them using the native language (Tcl, Python, Java, or whatever
    language Vtk is wrapped in). This, in a way, removes the need for the
    route and script mechanism (not completely though).
    
    Thanks:
    
    
     Thanks to Russ Coucher of Areva for numerous bug fixes and a new
    test.
    
    See Also:
    
    Importer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVRMLImporter, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the file to read.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_vrmldef_object(self, *args):
        """
        V.get_vrmldef_object(string) -> Object
        C++: Object *GetVRMLDEFObject(const char *name)
        In the VRML spec you can DEF and USE nodes (name them), This
        routine will return the associated VTK object which was created
        as a result of the DEF mechanism Send in the name from the VRML
        file, get the VTK object. You will have to check and correctly
        cast the object since this only returns Objects.
        """
        ret = self._wrap_call(self._vtk_obj.GetVRMLDEFObject, *args)
        return wrap_vtk(ret)

    def enter_field(self, *args):
        """
        V.enter_field(string)
        C++: void enterField(const char *)
        Needed by the yacc/lex grammar used
        """
        ret = self._wrap_call(self._vtk_obj.enterField, *args)
        return ret

    def enter_node(self, *args):
        """
        V.enter_node(string)
        C++: void enterNode(const char *)
        Needed by the yacc/lex grammar used
        """
        ret = self._wrap_call(self._vtk_obj.enterNode, *args)
        return ret

    def exit_field(self):
        """
        V.exit_field()
        C++: void exitField()
        Needed by the yacc/lex grammar used
        """
        ret = self._vtk_obj.exitField()
        return ret
        

    def exit_node(self):
        """
        V.exit_node()
        C++: void exitNode()
        Needed by the yacc/lex grammar used
        """
        ret = self._vtk_obj.exitNode()
        return ret
        

    def use_node(self, *args):
        """
        V.use_node(string)
        C++: void useNode(const char *)
        Needed by the yacc/lex grammar used
        """
        ret = self._wrap_call(self._vtk_obj.useNode, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('file_name',
    'GetFileName'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VRMLImporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name']),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

