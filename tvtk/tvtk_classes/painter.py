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


class Painter(Object):
    """
    Painter - Abstract class for drawing poly data.
    
    Superclass: Object
    
    This defines the interface for a Painter. Painters are helpers used
    by Mapper to perform the rendering. The mapper sets up a chain of
    painters and passes the render request to the painter. Every painter
    may have a delegate painter to which the render request is forwarded.
    The Painter may modify the request or data before passing it to the
    delegate painter. All the information to control the rendering must
    be passed to the painter using the Information object. A concrete
    painter may read special keys from the Information object and
    affect the rendering.
    
    See Also:
    
    PainterPolyDataMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPainter, obj, update, **traits)
    
    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    def _set_information(self, arg):
        old_val = self._get_information()
        self._wrap_call(self._vtk_obj.SetInformation,
                        deref_vtk(arg))
        self.trait_property_changed('information', old_val, arg)
    information = traits.Property(_get_information, _set_information, help=\
        """
        Get/Set the information object associated with this painter.
        """
    )

    progress = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the execution progress of a process object.
        """
    )
    def _progress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgress,
                        self.progress)

    def _get_delegate_painter(self):
        return wrap_vtk(self._vtk_obj.GetDelegatePainter())
    def _set_delegate_painter(self, arg):
        old_val = self._get_delegate_painter()
        self._wrap_call(self._vtk_obj.SetDelegatePainter,
                        deref_vtk(arg))
        self.trait_property_changed('delegate_painter', old_val, arg)
    delegate_painter = traits.Property(_get_delegate_painter, _set_delegate_painter, help=\
        """
        Set/Get the painter to which this painter should propagare its
        draw calls.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the data object to paint. Currently we only support one data
        object per painter chain.
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> DataObject
        C++: virtual DataObject *GetOutput()
        Get the output data object from this painter. The default
        implementation simply forwards the input data object as the
        output.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    def _get_time_to_draw(self):
        return self._vtk_obj.GetTimeToDraw()
    time_to_draw = traits.Property(_get_time_to_draw, help=\
        """
        Get the time required to draw the geometry last time it was
        rendered. Default implementation adds the current time_to_draw with
        that of the delegate painter.
        """
    )

    def CONSERVE_MEMORY(self):
        """
        V.conserve__memory() -> InformationIntegerKey
        C++: static InformationIntegerKey *CONSERVE_MEMORY()
        Keys used to specify control the behaviour of the painter. When
        on, the painter avoids using more memory than it has to.  Thus,
        auxiliary data structures for faster rendering may not be built. 
        Is off by default.
        """
        ret = wrap_vtk(self._vtk_obj.CONSERVE_MEMORY())
        return ret
        

    def HIGH_QUALITY(self):
        """
        V.high__quality() -> InformationIntegerKey
        C++: static InformationIntegerKey *HIGH_QUALITY()
        Keys used to specify control the behaviour of the painter. When
        off, the painter may make approximations that will make the
        rendering go faster but may degrade image quality.  Is on by
        default.
        """
        ret = wrap_vtk(self._vtk_obj.HIGH_QUALITY())
        return ret
        

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Release any graphics resources that are being consumed by this
        painter. The parameter window could be used to determine which
        graphic resources to release. The call is propagated to the
        delegate painter, if any.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def render(self, *args):
        """
        V.render(Renderer, Actor, int, bool)
        C++: virtual void Render(Renderer *renderer, Actor *actor,
            unsigned long typeflags, bool forceCompileOnly)
        Generates rendering primitives of appropriate type(s). Multiple
        types of primitives can be requested by or-ring the primitive
        flags. Default implementation calls update_delegate_painter() to
        update the deletagate painter and then calls render_internal().
        force_compile_only is passed to the display list painters.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def STATIC_DATA(self):
        """
        V.static__data() -> InformationIntegerKey
        C++: static InformationIntegerKey *STATIC_DATA()
        Keys used to specify control the behaviour of the painter. When
        on, the painter assumes that the poly data changes infrequently.
        It is thus more likely to take time and memory to build auxiliary
        data structures for faster frame rates.  Is off by default.
        """
        ret = wrap_vtk(self._vtk_obj.STATIC_DATA())
        return ret
        

    def update_bounds(self, *args):
        """
        V.update_bounds([float, float, float, float, float, float])
        C++: virtual void UpdateBounds(double bounds[6])
        Expand or shrink the estimated bounds of the object based on the
        geometric transformations performed in the painter. If the
        painter does not modify the geometry, the bounds are passed
        through.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateBounds, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Painter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Painter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Painter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Painter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

