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

from tvtk.tvtk_classes.structured_grid_source import StructuredGridSource


class PLOT3DReader(StructuredGridSource):
    """
    PLOT3DReader - read plot3d data files
    
    Superclass: StructuredGridSource
    
    PLOT3DReader is a reader object that reads plot3d formatted files
    and generates structured grid(s) on output. plot3d is a computer
    graphics program designed to visualize the grids and solutions of
    computational fluid dynamics. Please see the "_plot3d User's Manual"
    available from NASA Ames Research Center, Moffett Field CA.
    
    plot3d files consist of a grid file (also known as XYZ file), an
    optional solution file (also known as a Q file), and an optional
    function file that contains user created data (currently
    unsupported). The Q file contains solution  information as follows:
    the four parameters free stream mach number (Fsmach), angle of attack
    (Alpha), Reynolds number (Re), and total integration time (Time).
    This information is stored in an array called Properties in the
    field_data of each output (tuple 0: fsmach, tuple 1: alpha, tuple 2:
    re, tuple 3: time). In addition, the solution file contains the flow
    density (scalar), flow momentum (vector), and flow energy (scalar).
    
    The reader can generate additional scalars and vectors (or
    "functions") from this information. To use PLOT3DReader, you must
    specify the particular function number for the scalar and vector you
    want to visualize. This implementation of the reader provides the
    following functions. The scalar functions are:
    -1  - don't read or compute any scalars 100 - density 110 - pressure
       120 - temperature 130 - enthalpy 140 - internal energy 144 -
       kinetic energy 153 - velocity magnitude 163 - stagnation energy
       170 - entropy 184 - swirl.
    
    The vector functions are:
    -1  - don't read or compute any vectors 200 - velocity 201 -
       vorticity 202 - momentum 210 - pressure gradient.
    
    (Other functions are described in the plot3d spec, but only those
    listed are implemented here.) Note that by default, this reader
    creates the density scalar (100) and momentum vector (202) as output.
    (These are just read in from the solution file.) Please note that the
    validity of computation is a function of this class's gas constants
    (R, Gamma) and the equations used. They may not be suitable for your
    computational domain.
    
    Additionally, you can read other data and associate it as a
    DataArray into the output's point attribute data. Use the method
    add_function() to list all the functions that you'd like to read.
    add_function() accepts an integer parameter that defines the function
    number.
    
    See Also:
    
    StructuredGridSource StructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPLOT3DReader, obj, update, **traits)
    
    multi_grid = tvtk_base.false_bool_trait(help=\
        """
        Does the file to be read contain information about number of
        grids. In some plot3d files, the first value contains the number
        of grids (even if there is only 1). If reading such a file, set
        this to true.
        """
    )
    def _multi_grid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMultiGrid,
                        self.multi_grid_)

    force_read = tvtk_base.false_bool_trait(help=\
        """
        Try to read a binary file even if the file length seems to be
        inconsistent with the header information. Use this with caution,
        if the file length is not the same as calculated from the header.
        either the file is corrupt or the settings are wrong.
        """
    )
    def _force_read_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceRead,
                        self.force_read_)

    two_dimensional_geometry = tvtk_base.false_bool_trait(help=\
        """
        If only two-dimensional data was written to the file, turn this
        on.
        """
    )
    def _two_dimensional_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoDimensionalGeometry,
                        self.two_dimensional_geometry_)

    do_not_reduce_number_of_outputs = tvtk_base.true_bool_trait(help=\
        """
        If this is on, the reader will never reduce the number of outputs
        after reading a file with n grids and producing n outputs. If the
        file read afterwards contains fewer grids, the extra outputs will
        be empty. This option can be used by application which rely on
        the initial number of outputs not shrinking.
        """
    )
    def _do_not_reduce_number_of_outputs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDoNotReduceNumberOfOutputs,
                        self.do_not_reduce_number_of_outputs_)

    i_blanking = tvtk_base.false_bool_trait(help=\
        """
        Is there iblanking (point visibility) information in the file. If
        there is iblanking arrays, these will be read and assigned to the
        point_visibility array of the output.
        """
    )
    def _i_blanking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIBlanking,
                        self.i_blanking_)

    binary_file = tvtk_base.true_bool_trait(help=\
        """
        Is the file to be read written in binary format (as opposed to
        ascii).
        """
    )
    def _binary_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinaryFile,
                        self.binary_file_)

    has_byte_count = tvtk_base.false_bool_trait(help=\
        """
        Were the arrays written with leading and trailing byte counts ?
        Usually, files written by a fortran program will contain these
        byte counts whereas the ones written by C/C++ won't.
        """
    )
    def _has_byte_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHasByteCount,
                        self.has_byte_count_)

    byte_order = traits.Trait('big_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        Set the byte order of the file (remember, more Unix workstations
        write big endian whereas PCs write little endian). Default is big
        endian (since most older plot3d files were written by
        workstations).
        """
    )
    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    uvinf = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the x-component of the free-stream velocity. Default is
        1.0.
        """
    )
    def _uvinf_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUvinf,
                        self.uvinf)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d geometry filename.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    vvinf = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the y-component of the free-stream velocity. Default is
        1.0.
        """
    )
    def _vvinf_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVvinf,
                        self.vvinf)

    scalar_function_number = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Specify the scalar function to extract. If ==(-1), then no scalar
        function is extracted.
        """
    )
    def _scalar_function_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFunctionNumber,
                        self.scalar_function_number)

    vector_function_number = traits.Int(202, enter_set=True, auto_set=False, help=\
        """
        Specify the vector function to extract. If ==(-1), then no vector
        function is extracted.
        """
    )
    def _vector_function_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorFunctionNumber,
                        self.vector_function_number)

    xyz_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d geometry filename.
        """
    )
    def _xyz_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXYZFileName,
                        self.xyz_file_name)

    wvinf = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the z-component of the free-stream velocity. Default is
        1.0.
        """
    )
    def _wvinf_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWvinf,
                        self.wvinf)

    r = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the gas constant. Default is 1.0.
        """
    )
    def _r_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetR,
                        self.r)

    function_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d Function Filename (optional)
        """
    )
    def _function_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunctionFileName,
                        self.function_file_name)

    gamma = traits.Float(1.4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio of specific heats. Default is 1.4.
        """
    )
    def _gamma_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGamma,
                        self.gamma)

    q_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d solution filename.
        """
    )
    def _q_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFileName,
                        self.q_file_name)

    def _get_number_of_grids(self):
        return self._vtk_obj.GetNumberOfGrids()
    number_of_grids = traits.Property(_get_number_of_grids, help=\
        """
        This returns the number of outputs this reader will produce. This
        number is equal to the number of grids in the current file. This
        method has to be called before getting any output if the number
        of outputs will be greater than 1 (the first output is always the
        same). Note that every time this method is invoked, the header
        file is opened and part of the header is read.
        """
    )

    def add_function(self, *args):
        """
        V.add_function(int)
        C++: void AddFunction(int functionNumber)
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._wrap_call(self._vtk_obj.AddFunction, *args)
        return ret

    def can_read_binary_file(self, *args):
        """
        V.can_read_binary_file(string) -> int
        C++: virtual int CanReadBinaryFile(const char *fname)
        Return 1 if the reader can read the given file name. Only
        meaningful for binary files.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadBinaryFile, *args)
        return ret

    def remove_all_functions(self):
        """
        V.remove_all_functions()
        C++: void RemoveAllFunctions()
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._vtk_obj.RemoveAllFunctions()
        return ret
        

    def remove_function(self, *args):
        """
        V.remove_function(int)
        C++: void RemoveFunction(int)
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveFunction, *args)
        return ret

    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('force_read', 'GetForceRead'),
    ('binary_file', 'GetBinaryFile'), ('file_name', 'GetFileName'),
    ('has_byte_count', 'GetHasByteCount'), ('two_dimensional_geometry',
    'GetTwoDimensionalGeometry'), ('vvinf', 'GetVvinf'), ('debug',
    'GetDebug'), ('vector_function_number', 'GetVectorFunctionNumber'),
    ('progress', 'GetProgress'), ('i_blanking', 'GetIBlanking'),
    ('do_not_reduce_number_of_outputs', 'GetDoNotReduceNumberOfOutputs'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('function_file_name', 'GetFunctionFileName'), ('multi_grid',
    'GetMultiGrid'), ('xyz_file_name', 'GetXYZFileName'), ('uvinf',
    'GetUvinf'), ('progress_text', 'GetProgressText'), ('q_file_name',
    'GetQFileName'), ('r', 'GetR'), ('release_data_flag',
    'GetReleaseDataFlag'), ('scalar_function_number',
    'GetScalarFunctionNumber'), ('reference_count', 'GetReferenceCount'),
    ('wvinf', 'GetWvinf'), ('abort_execute', 'GetAbortExecute'), ('gamma',
    'GetGamma'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'binary_file', 'debug',
    'do_not_reduce_number_of_outputs', 'force_read',
    'global_warning_display', 'has_byte_count', 'i_blanking',
    'multi_grid', 'release_data_flag', 'two_dimensional_geometry',
    'byte_order', 'file_name', 'function_file_name', 'gamma',
    'progress_text', 'q_file_name', 'r', 'release_data_flag',
    'scalar_function_number', 'uvinf', 'vector_function_number', 'vvinf',
    'wvinf', 'xyz_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PLOT3DReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['binary_file', 'do_not_reduce_number_of_outputs',
            'force_read', 'has_byte_count', 'i_blanking', 'multi_grid',
            'two_dimensional_geometry'], ['byte_order'], ['file_name',
            'function_file_name', 'gamma', 'q_file_name', 'r',
            'release_data_flag', 'scalar_function_number', 'uvinf',
            'vector_function_number', 'vvinf', 'wvinf', 'xyz_file_name']),
            title='Edit PLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

