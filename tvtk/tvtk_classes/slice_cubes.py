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


class SliceCubes(Object):
    """
    SliceCubes - generate isosurface(s) from volume four slices at a
    time
    
    Superclass: Object
    
    SliceCubes is a special version of the marching cubes filter.
    Instead of ingesting an entire volume at once it processes only four
    slices at a time. This way, it can generate isosurfaces from huge
    volumes. Also, the output of this object is written to a marching
    cubes triangle file. That way, output triangles do not need to be
    held in memory.
    
    To use SliceCubes you must specify an instance of VolumeReader
    to read the data. Set this object up with the proper file prefix,
    image range, data origin, data dimensions, header size, data mask,
    and swap bytes flag. The SliceCubes object will then take over and
    read slices as necessary. You also will need to specify the name of
    an output marching cubes triangle file.
    
    Caveats:
    
    This process object is both a source and mapper (i.e., it reads and
    writes data to a file). This is different than the other marching
    cubes objects (and most process objects in the system). It's
    specialized to handle very large data.
    
    This object only extracts a single isosurface. This compares with the
    other contouring objects in vtk that generate multiple surfaces.
    
    To read the output file use MCubesReader.
    
    See Also:
    
    MarchingCubes ContourFilter MCubesReader DividingCubes
    VolumeReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSliceCubes, obj, update, **traits)
    
    limits_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of marching cubes limits file. The limits file
        speeds up subsequent reading of output triangle file.
        """
    )
    def _limits_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitsFileName,
                        self.limits_file_name)

    def _get_reader(self):
        return wrap_vtk(self._vtk_obj.GetReader())
    def _set_reader(self, arg):
        old_val = self._get_reader()
        self._wrap_call(self._vtk_obj.SetReader,
                        deref_vtk(arg))
        self.trait_property_changed('reader', old_val, arg)
    reader = traits.Property(_get_reader, _set_reader, help=\
        """
        Set/get object to read slices.
        """
    )

    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get isosurface contour value.
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of marching cubes output file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def update(self):
        """
        V.update()
        C++: void Update()"""
        ret = self._vtk_obj.Update()
        return ret
        

    def write(self):
        """
        V.write()
        C++: void Write()"""
        ret = self._vtk_obj.Write()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('file_name', 'GetFileName'), ('limits_file_name',
    'GetLimitsFileName'), ('value', 'GetValue'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name', 'limits_file_name',
    'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SliceCubes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SliceCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'limits_file_name', 'value']),
            title='Edit SliceCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SliceCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

