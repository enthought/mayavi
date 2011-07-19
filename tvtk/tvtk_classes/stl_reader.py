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


class STLReader(PolyDataAlgorithm):
    """
    STLReader - read ASCII or binary stereo lithography files
    
    Superclass: PolyDataAlgorithm
    
    STLReader is a source object that reads ASCII or binary stereo
    lithography files (.stl files). The file_name must be specified to
    STLReader. The object automatically detects whether the file is
    ASCII or binary.
    
    .stl files are quite inefficient since they duplicate vertex
    definitions. By setting the Merging boolean you can control whether
    the point data is merged after reading. Merging is performed by
    default, however, merging requires a large amount of temporary
    storage since a 3d hash table must be constructed.
    
    Caveats:
    
    Binary files written on one system may not be readable on other
    systems. STLWriter uses VAX or PC byte ordering and swaps bytes on
    other systems.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSTLReader, obj, update, **traits)
    
    merging = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off merging of points/triangles.
        """
    )
    def _merging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMerging,
                        self.merging_)

    scalar_tags = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off tagging of solids with scalars.
        """
    )
    def _scalar_tags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarTags,
                        self.scalar_tags_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a spatial locator for merging points. By default an
        instance of MergePoints is used.
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of stereo lithography file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('merging', 'GetMerging'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('scalar_tags', 'GetScalarTags'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'merging',
    'release_data_flag', 'scalar_tags', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(STLReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['merging', 'scalar_tags'], [], ['file_name']),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

