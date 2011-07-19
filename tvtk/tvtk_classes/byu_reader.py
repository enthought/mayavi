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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class BYUReader(PolyDataAlgorithm):
    """
    BYUReader - read MOVIE.BYU polygon files
    
    Superclass: PolyDataAlgorithm
    
    BYUReader is a source object that reads MOVIE.BYU polygon files.
    These files consist of a geometry file (.g), a scalar file (.s), a
    displacement or vector file (.d), and a 2d texture coordinate file
    (.t).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBYUReader, obj, update, **traits)
    
    read_scalar = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the scalar file.
        """
    )
    def _read_scalar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadScalar,
                        self.read_scalar_)

    read_displacement = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the displacement file.
        """
    )
    def _read_displacement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadDisplacement,
                        self.read_displacement_)

    read_texture = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the texture coordinate file. Specify
        name of geometry file_name.
        """
    )
    def _read_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadTexture,
                        self.read_texture_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of geometry file_name (alias).
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    scalar_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of scalar file_name.
        """
    )
    def _scalar_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFileName,
                        self.scalar_file_name)

    geometry_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of geometry file_name.
        """
    )
    def _geometry_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryFileName,
                        self.geometry_file_name)

    part_number = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the part number to be read.
        """
    )
    def _part_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPartNumber,
                        self.part_number)

    texture_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of texture coordinates file_name.
        """
    )
    def _texture_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureFileName,
                        self.texture_file_name)

    displacement_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of displacement file_name.
        """
    )
    def _displacement_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementFileName,
                        self.displacement_file_name)

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns 1 if this file can be read and 0 if the file cannot be
        read. Because BYU files do not have anything in the header
        specifying the file type, the result is not definitive.  Invalid
        files may still return 1 although a valid file will never return
        0.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    _updateable_traits_ = \
    (('read_scalar', 'GetReadScalar'), ('scalar_file_name',
    'GetScalarFileName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('displacement_file_name', 'GetDisplacementFileName'),
    ('progress_text', 'GetProgressText'), ('read_displacement',
    'GetReadDisplacement'), ('debug', 'GetDebug'), ('part_number',
    'GetPartNumber'), ('abort_execute', 'GetAbortExecute'),
    ('texture_file_name', 'GetTextureFileName'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('read_texture', 'GetReadTexture'),
    ('geometry_file_name', 'GetGeometryFileName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_displacement', 'read_scalar', 'read_texture',
    'release_data_flag', 'displacement_file_name', 'file_name',
    'geometry_file_name', 'part_number', 'progress_text',
    'scalar_file_name', 'texture_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BYUReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['read_displacement', 'read_scalar', 'read_texture'],
            [], ['displacement_file_name', 'file_name', 'geometry_file_name',
            'part_number', 'scalar_file_name', 'texture_file_name']),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

