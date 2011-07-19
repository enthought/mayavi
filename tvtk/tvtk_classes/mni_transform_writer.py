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

from tvtk.tvtk_classes.algorithm import Algorithm


class MNITransformWriter(Algorithm):
    """
    MNITransformWriter - A writer for MNI transformation files.
    
    Superclass: Algorithm
    
    The MNI .xfm file format is used to store geometrical
    transformations.  Three kinds of transformations are supported by the
    file format: affine, thin-plate spline, and grid transformations.
    This file format was developed at the mc_connell Brain Imaging Centre
    at the Montreal Neurological Institute and is used by their software.
    
    See Also:
    
    MINCImageWriter MNITransformReader
    
    Thanks:
    
    Thanks to David Gobbi for writing this class and Atamai Inc. for
    contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMNITransformWriter, obj, update, **traits)
    
    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set the transform.
        """
    )

    comments = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set comments to be added to the file.
        """
    )
    def _comments_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComments,
                        self.comments)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_descriptive_name(self):
        return self._vtk_obj.GetDescriptiveName()
    descriptive_name = traits.Property(_get_descriptive_name, help=\
        """
        Get the name of this file format.
        """
    )

    def _get_file_extensions(self):
        return self._vtk_obj.GetFileExtensions()
    file_extensions = traits.Property(_get_file_extensions, help=\
        """
        Get the entension for this file format.
        """
    )

    def _get_number_of_transforms(self):
        return self._vtk_obj.GetNumberOfTransforms()
    number_of_transforms = traits.Property(_get_number_of_transforms, help=\
        """
        Get the number of transforms that will be written.
        """
    )

    def add_transform(self, *args):
        """
        V.add_transform(AbstractTransform)
        C++: virtual void AddTransform(AbstractTransform *transform)
        Add another transform to the file.  The next time that
        set_transform is called, all added transforms will be removed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddTransform, *my_args)
        return ret

    def write(self):
        """
        V.write()
        C++: virtual void Write()
        Write the file.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('comments',
    'GetComments'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'comments', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MNITransformWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MNITransformWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['comments', 'file_name']),
            title='Edit MNITransformWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MNITransformWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

