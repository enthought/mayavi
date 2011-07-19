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


class Testing(Object):
    """
    Testing - a unified VTK regression testing framework
    
    Superclass: Object
    
    This is a VTK regression testing framework. Looks like this:
    
    
     Testing* t = Testing::New();
    
    
     Two options for setting arguments
    
    
     Option 1:
     for ( cc = 1; cc < argc; cc ++ )
       {
       t->_add_argument(argv[cc]);
       }
    
    
     Option 2:
     t->_add_argument("-_d");
     t->_add_argument(my_data_dir);
     t->_add_argument("-_v");
     t->_add_argument(my_valid_image);
    
    
     ...
    
    
     Two options of doing testing:
    
    
     Option 1:
     t->_set_render_window(ren_win);
     int res = t->_regression_test(threshold);
    
    
     Option 2:
     int res = t->_regression_test(test_image, threshold);
    
    
     ...
    
    
     if ( res == Testing::PASSED )
       {
       Test passed
       }
     else
       {
       Test failed
       }
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTesting, obj, update, **traits)
    
    front_buffer = tvtk_base.false_bool_trait(help=\
        """
        Use front buffer for tests. By default use back buffer.
        """
    )
    def _front_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrontBuffer,
                        self.front_buffer_)

    valid_image_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the name of the valid image file
        """
    )
    def _valid_image_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidImageFileName,
                        self.valid_image_file_name)

    verbose = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set verbosity level. A level of 0 is quiet.
        """
    )
    def _verbose_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerbose,
                        self.verbose)

    border_offset = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Number of pixels added as borders to avoid problems with window
        decorations added by some window managers.
        """
    )
    def _border_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderOffset,
                        self.border_offset)

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Set and get the render window that will be used for regression
        testing.
        """
    )

    temp_directory = traits.String(r"/home/varoquau/dev/enthought/Testing/Temporary", enter_set=True, auto_set=False, help=\
        """
        Get some paramters from the command line arguments, env, or
        defaults
        """
    )
    def _temp_directory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTempDirectory,
                        self.temp_directory)

    data_root = traits.String(r"/home/varoquau/dev/VTKData", enter_set=True, auto_set=False, help=\
        """
        Get some paramters from the command line arguments, env, or
        defaults
        """
    )
    def _data_root_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataRoot,
                        self.data_root)

    def get_argument(self, *args):
        """
        V.get_argument(string) -> string
        C++: char *GetArgument(const char *arg)
        Search for a specific argument by name and return its value
        (assumed to be the next on the command tail). Up to caller to
        delete the returned string.
        """
        ret = self._wrap_call(self._vtk_obj.GetArgument, *args)
        return ret

    def _get_front_buffer_max_value(self):
        return self._vtk_obj.GetFrontBufferMaxValue()
    front_buffer_max_value = traits.Property(_get_front_buffer_max_value, help=\
        """
        Use front buffer for tests. By default use back buffer.
        """
    )

    def _get_front_buffer_min_value(self):
        return self._vtk_obj.GetFrontBufferMinValue()
    front_buffer_min_value = traits.Property(_get_front_buffer_min_value, help=\
        """
        Use front buffer for tests. By default use back buffer.
        """
    )

    def _get_image_difference(self):
        return self._vtk_obj.GetImageDifference()
    image_difference = traits.Property(_get_image_difference, help=\
        """
        Get the image difference.
        """
    )

    def add_argument(self, *args):
        """
        V.add_argument(string)
        C++: void AddArgument(const char *argv)
        Pass the command line arguments into this class to be processed.
        Many of the Get methods such as get_valid_image and get_baseline_root
        rely on the arguments to be passed in prior to retrieving these
        values. Just call add_argument for each argument that was passed
        into the command line
        """
        ret = self._wrap_call(self._vtk_obj.AddArgument, *args)
        return ret

    def clean_arguments(self):
        """
        V.clean_arguments()
        C++: void CleanArguments()"""
        ret = self._vtk_obj.CleanArguments()
        return ret
        

    def compare_average_of_l2_norm(self, *args):
        """
        V.compare_average_of_l2_norm(DataSet, DataSet, float) -> int
        C++: int CompareAverageOfL2Norm(DataSet *pdA, DataSet *pdB,
            double tol)
        V.compare_average_of_l2_norm(DataArray, DataArray, float) -> int
        C++: int CompareAverageOfL2Norm(DataArray *daA,
            DataArray *daB, double tol)
        Compute the average L2 norm between all point data data arrays of
        types float and double present in the data sets "ds_a" and "ds_b"
        (this includes instances of Points) Compare the result of each
        L2 comutation to "tol".
        """
        my_args = deref_array(args, [('vtkDataSet', 'vtkDataSet', 'float'), ('vtkDataArray', 'vtkDataArray', 'float')])
        ret = self._wrap_call(self._vtk_obj.CompareAverageOfL2Norm, *my_args)
        return ret

    def is_flag_specified(self, *args):
        """
        V.is_flag_specified(string) -> int
        C++: int IsFlagSpecified(const char *flag)
        Is some arbitrary user flag ("-X", "-Z" etc) specified
        """
        ret = self._wrap_call(self._vtk_obj.IsFlagSpecified, *args)
        return ret

    def is_interactive_mode_specified(self):
        """
        V.is_interactive_mode_specified() -> int
        C++: int IsInteractiveModeSpecified()
        Is the interactive mode specified?
        """
        ret = self._vtk_obj.IsInteractiveModeSpecified()
        return ret
        

    def is_valid_image_specified(self):
        """
        V.is_valid_image_specified() -> int
        C++: int IsValidImageSpecified()
        Is a valid image specified on the command line areguments?
        """
        ret = self._vtk_obj.IsValidImageSpecified()
        return ret
        

    def regression_test(self, *args):
        """
        V.regression_test(float) -> int
        C++: virtual int RegressionTest(double thresh)
        V.regression_test(ImageData, float) -> int
        C++: virtual int RegressionTest(ImageData *image,
            double thresh)
        Perform the test and return result. At the same time the output
        will be written cout
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegressionTest, *my_args)
        return ret

    _updateable_traits_ = \
    (('temp_directory', 'GetTempDirectory'), ('debug', 'GetDebug'),
    ('valid_image_file_name', 'GetValidImageFileName'), ('verbose',
    'GetVerbose'), ('reference_count', 'GetReferenceCount'),
    ('front_buffer', 'GetFrontBuffer'), ('border_offset',
    'GetBorderOffset'), ('data_root', 'GetDataRoot'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'front_buffer', 'global_warning_display', 'border_offset',
    'data_root', 'temp_directory', 'valid_image_file_name', 'verbose'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Testing, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Testing properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['front_buffer'], [], ['border_offset', 'data_root',
            'temp_directory', 'valid_image_file_name', 'verbose']),
            title='Edit Testing properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Testing properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

