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

from tvtk.tvtk_classes.prop3d import Prop3D


class Actor(Prop3D):
    """
    Actor - represents an object (geometry & properties) in a rendered
    scene 
    
    Superclass: Prop3D
    
    Actor is used to represent an entity in a rendering scene.  It
    inherits functions related to the actors position, and orientation
    from Prop. The actor also has scaling and maintains a reference to
    the defining geometry (i.e., the mapper), rendering properties, and
    possibly a texture map. Actor combines these instance variables
    into one 4x4 transformation matrix as follows: [x y z 1] = [x y z 1]
    Translate(-origin) Scale(scale) Rot(y) Rot(x) Rot (z) Trans(origin)
    Trans(position)
    
    See Also:
    
    Property Texture Mapper Assembly Follower LODActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkActor, obj, update, **traits)
    
    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Returns the Mapper that this actor is getting its data from.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set/Get the property object that controls this actors surface
        properties.  This should be an instance of a Property object. 
        Every actor must have a property associated with it.  If one
        isn't specified, then one will be generated automatically.
        Multiple actors can share one property object.
        """
    )

    def _get_backface_property(self):
        return wrap_vtk(self._vtk_obj.GetBackfaceProperty())
    def _set_backface_property(self, arg):
        old_val = self._get_backface_property()
        self._wrap_call(self._vtk_obj.SetBackfaceProperty,
                        deref_vtk(arg))
        self.trait_property_changed('backface_property', old_val, arg)
    backface_property = traits.Property(_get_backface_property, _set_backface_property, help=\
        """
        Set/Get the property object that controls this actors backface
        surface properties.  This should be an instance of a Property
        object. If one isn't specified, then the front face properties
        will be used.  Multiple actors can share one property object.
        """
    )

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    def _set_texture(self, arg):
        old_val = self._get_texture()
        self._wrap_call(self._vtk_obj.SetTexture,
                        deref_vtk(arg))
        self.trait_property_changed('texture', old_val, arg)
    texture = traits.Property(_get_texture, _set_texture, help=\
        """
        Set/Get the texture object to control rendering texture maps. 
        This will be a Texture object. An actor does not need to have
        an associated texture map and multiple actors can share one
        texture.
        """
    )

    def _get_next_part(self):
        return wrap_vtk(self._vtk_obj.GetNextPart())
    next_part = traits.Property(_get_next_part, help=\
        """
        The following methods are for compatibility. The methods will be
        deprecated in the near future. Use Prop::GetNextPath() (and
        related functionality) to get the parts in an assembly (or more
        correctly, the paths in the assembly).
        """
    )

    def _get_number_of_parts(self):
        return self._vtk_obj.GetNumberOfParts()
    number_of_parts = traits.Property(_get_number_of_parts, help=\
        """
        The following methods are for compatibility. The methods will be
        deprecated in the near future. Use Prop::GetNextPath() (and
        related functionality) to get the parts in an assembly (or more
        correctly, the paths in the assembly).
        """
    )

    def apply_properties(self):
        """
        V.apply_properties()
        C++: virtual void ApplyProperties()
        Apply the current properties to all parts that compose this
        actor. This method is overloaded in Assembly to apply the
        assemblies' properties to all its parts in a recursive manner.
        Typically the use of this method is to set the desired properties
        in the assembly, and then push the properties down to the
        assemblies parts with apply_properties().
        """
        ret = self._vtk_obj.ApplyProperties()
        return ret
        

    def init_part_traversal(self):
        """
        V.init_part_traversal()
        C++: virtual void InitPartTraversal()
        The following methods are for compatibility. The methods will be
        deprecated in the near future. Use Prop::GetNextPath() (and
        related functionality) to get the parts in an assembly (or more
        correctly, the paths in the assembly).
        """
        ret = self._vtk_obj.InitPartTraversal()
        return ret
        

    def make_property(self):
        """
        V.make_property() -> Property
        C++: virtual Property *MakeProperty()
        Create a new property suitable for use with this type of Actor.
        For example, a MesaActor should create a MesaProperty in
        this function.   The default is to just call Property::New.
        """
        ret = wrap_vtk(self._vtk_obj.MakeProperty())
        return ret
        

    def render(self, *args):
        """
        V.render(Renderer, Mapper)
        C++: virtual void Render(Renderer *, Mapper *)
        This causes the actor to be rendered. It in turn will render the
        actor's property, texture map and then mapper. If a property
        hasn't been assigned, then the actor will create one
        automatically. Note that a side effect of this method is that the
        pipeline will be updated.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'), ('orientation',
    'GetOrientation'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Actor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Actor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale']),
            title='Edit Actor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Actor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

