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


class OpenGLExtensionManager(Object):
    """
    OpenGLExtensionManager - Interface class for querying and using
    open_gl extensions.
    
    Superclass: Object
    
    OpenGLExtensionManager acts as an interface to open_gl extensions. 
    It provides methods to query open_gl extensions on the current or a
    given render window and to load extension function pointers. 
    Currently does not support GLU extensions since the GLU library is
    not linked to VTK.
    
    Before using OpenGLExtensionManager, an open_gl context must be
    created. This is generally done with a RenderWindow.  Note that
    simply creating the RenderWindow is not sufficient.  Usually you
    have to call Render before the actual open_gl context is created.  You
    can specify the render_window with the set_render_window
    method.vtk_open_gl_extension_manager *extensions =
    OpenGLExtensionManager::New();
    extensions->_set_render_window(renwin);
    If no RenderWindow is specified, the current open_gl context (if
    any) is used.
    
    Generally speaking, when using open_gl extensions, you will need an
    OpenGLExtensionManager and the prototypes defined in
    vtkgl.h.#include "vtk_open_gl_extension_manager.h"
    #include "vtkgl.h"
    The vtkgl.h include file contains all the constants and function
        pointers required for using open_gl extensions in a portable and
        namespace safe way.  vtkgl.h is built from parsed glext.h,
        glxext.h, and wglext.h files.  Snapshots of these files are
        distributed with VTK, but you can also set CMake options to use
        other files.
    
    To use an open_gl extension, you first need to make an instance of
    OpenGLExtensionManager and give it a RenderWindow.  You can
    then query the OpenGLExtensionManager to see if the extension is
    supported with the extension_supported method.  Valid names for
    extensions are given in the open_gl extension registry at
    http://www.opengl.org/registry/ . You can also grep vtkgl.h (which
    will be in the binary build directory if VTK is not installed) for
    appropriate names.  There are also special extensions GL_VERSION_X_X
    (where X_X is replaced with a major and minor version, respectively)
    which contain all the constants and functions for open_gl versions for
    which the gl.h header file is of an older version than the driver.
    
    if (   !extensions->_extension_supported("_gl__version__1__2")
        || !extensions->_extension_supported("_gl__arb_multitexture") ) {
      {
      ErrorMacro("Required extensions not supported!");
      }
    
    Once you have verified that the extensions you want exist, before you
    use them you have to load them with the load_extension method.
    
    extensions->_load_extension("_gl__version__1__2");
    extensions->_load_extension("_gl__arb_multitexture");
    
    Alternatively, you can use the load_supported_extension method, which
    checks whether the requested extension is supported and, if so, loads
    it. The load_supported_extension method will not raise any errors or
    warnings if it fails, so it is important for callers to pay attention
    to the return value.
    
    if (   extensions->_load_supported_extension("_gl__version__1__2")
        && extensions->_load_supported_extension("_gl__arb_multitexture") ) {
      {
      vtkgl::ActiveTexture(vtkgl::TEXTURE0_ARB);
      }
    else
      {
      ErrorMacro("Required extensions could not be loaded!");
      }
    
    Once you have queried and loaded all of the extensions you need, you
    can delete the OpenGLExtensionManager.  To use a constant of an
    extension, simply replace the "GL_" prefix with "vtkgl::".  Likewise,
    replace the "gl" prefix of functions with "vtkgl::".  In rare cases,
    an extension will add a type. In this case, add vtkgl:: to the type
    (i.e. vtkgl::GLchar).
    
    extensions->Delete();
    ...
    vtkgl::ActiveTexture(vtkgl::TEXTURE0_ARB);
    
    For wgl extensions, replace the "WGL_" and "wgl" prefixes with
    "vtkwgl::".  For gl_x extensions, replace the "GLX_" and "gl_x"
    prefixes with "vtkgl_x::".
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLExtensionManager, obj, update, **traits)
    
    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Set/Get the render window to query extensions on.  If set to
        null, justs queries the current render window.
        """
    )

    def _get_extensions_string(self):
        return self._vtk_obj.GetExtensionsString()
    extensions_string = traits.Property(_get_extensions_string, help=\
        """
        Returns a string listing all available extensions.  Call Update
        first to validate this string.
        """
    )

    def extension_supported(self, *args):
        """
        V.extension_supported(string) -> int
        C++: virtual int ExtensionSupported(const char *name)
        Returns true if the extension is supported, false otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.ExtensionSupported, *args)
        return ret

    def load_as_arb_extension(self, *args):
        """
        V.load_as_arb_extension(string)
        C++: virtual void LoadAsARBExtension(const char *name)
        Similar to load_core_promoted_extension(). It loads an EXT extension
        into the pointers of its ARB equivalent.
        """
        ret = self._wrap_call(self._vtk_obj.LoadAsARBExtension, *args)
        return ret

    def load_core_promoted_extension(self, *args):
        """
        V.load_core_promoted_extension(string)
        C++: virtual void LoadCorePromotedExtension(const char *name)
        Loads all the functions associated with the given core-promoted
        extension into the appropriate static members of vtkgl associated
        with the open_gl version that promoted the extension as a core
        feature. This method emits a warning if the requested extension
        is not supported. It emits an error if the extension does not
        load successfully.
        
        For instance, extension GL_ARB_multitexture was promoted as a
        core feature into open_gl 1.3. An implementation that uses this
        feature has to (IN THIS ORDER), check if open_gl 1.3 is supported
        with extension_supported("_gl__version__1__3"), if true, load the
        extension with load_extension("_gl__version__1__3"). If false, test
        for the extension with
        extension_supported("_gl__arb_multitexture"),if true load the
        extension with this method
        load_core_promoted_extension("_gl__arb_multitexture"). If any of those
        loading stage succeeded, use vtgl::_active_texture() in any case,
        NOT vtgl::_active_texture_arb(). This method avoids the use of if
        statements everywhere in implementations using core-promoted
        extensions. Without this method, the implementation code should
        look like:int
        opengl__1__3=extensions->_extension_supported("_gl__version__1__3");
        if(opengl_1_3)
        {
          extensions->_load_extension("_gl__version__1__3");
        }
        else
        {
         if(extensions->_extension_supported("_gl__arb_multitexture"))
         {
          extensions->_load_core_promoted_extension("_gl__arb_multitexture");
         }
         else
         {
          ErrorMacro("Required multitexture feature is not
        supported!");
         }
        }
        ...
        if(opengl_1_3)
        {
         vtkgl::ActiveTexture(vtkgl::TEXTURE0)
        }
        else
        {
         vtkgl::ActiveTextureARB(vtkgl::TEXTURE0_ARB)
        }
        Thanks to this method, the code looks like:int
        opengl__1__3=extensions->_extension_supported("_gl__version__1__3");
        if(opengl_1_3)
        {
          extensions->_load_extension("_gl__version__1__3");
        }
        else
        {
         if(extensions->_extension_supported("_gl__arb_multitexture"))
         {
          extensions->_load_core_promoted_extension(" ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.LoadCorePromotedExtension, *args)
        return ret

    def load_extension(self, *args):
        """
        V.load_extension(string)
        C++: virtual void LoadExtension(const char *name)
        Loads all the functions associated with the given extension into
        the appropriate static members of vtkgl. This method emits a
        warning if the requested extension is not supported. It emits an
        error if the extension does not load successfully.
        """
        ret = self._wrap_call(self._vtk_obj.LoadExtension, *args)
        return ret

    def load_supported_extension(self, *args):
        """
        V.load_supported_extension(string) -> int
        C++: virtual int LoadSupportedExtension(const char *name)
        Returns true if the extension is supported and loaded
        successfully, false otherwise. This method will "fail
        silently/gracefully" if the extension is not supported or does
        not load properly. It emits neither warnings nor errors. It is up
        to the caller to determine if the extension loaded properly by
        paying attention to the return value.
        """
        ret = self._wrap_call(self._vtk_obj.LoadSupportedExtension, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Updates the extensions string.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLExtensionManager, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLExtensionManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit OpenGLExtensionManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLExtensionManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

