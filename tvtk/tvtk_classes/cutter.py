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


class Cutter(PolyDataAlgorithm):
    """
    Cutter - Cut DataSet with user-specified implicit function
    
    Superclass: PolyDataAlgorithm
    
    Cutter is a filter to cut through data using any subclass of
    ImplicitFunction. That is, a polygonal surface is created
    corresponding to the implicit function F(x,y,z) = value(s), where you
    can specify one or more values used to cut with.
    
    In VTK, cutting means reducing a cell of dimension N to a cut surface
    of dimension N-1. For example, a tetrahedron when cut by a plane
    (i.e., Plane implicit function) will generate triangles. (In
    comparison, clipping takes a N dimensional cell and creates N
    dimension primitives.)
    
    Cutter is generally used to "slice-through" a dataset, generating
    a surface that can be visualized. It is also possible to use
    Cutter to do a form of volume rendering. Cutter does this by
    generating multiple cut surfaces (usually planes) which are ordered
    (and rendered) from back-to-front. The surfaces are set translucent
    to give a volumetric rendering effect.
    
    Note that data can be cut using either 1) the scalar values
    associated with the dataset or 2) an implicit function associated
    with this class. By default, if an implicit function is set it is
    used to clip the data set, otherwise the dataset scalars are used to
    perform the clipping.
    
    See Also:
    
    ImplicitFunction ClipPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCutter, obj, update, **traits)
    
    generate_cut_scalars = tvtk_base.false_bool_trait(help=\
        """
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data.
        """
    )
    def _generate_cut_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCutScalars,
                        self.generate_cut_scalars_)

    sort_by = traits.Trait('sort_by_value',
    tvtk_base.TraitRevPrefixMap({'sort_by_cell': 1, 'sort_by_value': 0}), help=\
        """
        Set the sorting order for the generated polydata. There are two
        possibilities:
          Sort by value = 0 - This is the most efficient sort. For each
        cell,
             all contour values are processed. This is the default.
          Sort by cell = 1 - For each contour value, all cells are
        processed.
             This order should be used if the extracted polygons must be
        rendered
             in a back-to-front or front-to-back order. This is very
        problem
             dependent. For most applications, the default order is fine
        (and faster).
        
        Sort by cell is going to have a problem if the input has 2d and
        3d cells. Cell data will be scrambled becauses with PolyData
        output, verts and lines have lower cell ids than triangles.
        """
    )
    def _sort_by_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSortBy,
                        self.sort_by_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a spatial locator for merging points. By default, an
        instance of MergePoints is used.
        """
    )

    def _get_cut_function(self):
        return wrap_vtk(self._vtk_obj.GetCutFunction())
    def _set_cut_function(self, arg):
        old_val = self._get_cut_function()
        self._wrap_call(self._vtk_obj.SetCutFunction,
                        deref_vtk(arg))
        self.trait_property_changed('cut_function', old_val, arg)
    cut_function = traits.Property(_get_cut_function, _set_cut_function, help=\
        """
        
        """
    )

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Get the ith contour value.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Set a particular contour value at contour number i. The index i
        ranges between 0<=i<_number_of_contours.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of contours to place into the list. You only
        really need to use this method to reduce list size. The method
        set_value() will automatically increase list size as needed.
        """
    )
    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Generate num_contours equally spaced contour values between
        specified range. Contour values will include min/max range
        values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('sort_by', 'GetSortBy'),
    ('debug', 'GetDebug'), ('generate_cut_scalars',
    'GetGenerateCutScalars'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_contours', 'GetNumberOfContours'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_cut_scalars',
    'global_warning_display', 'release_data_flag', 'sort_by',
    'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Cutter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Cutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_cut_scalars'], ['sort_by'],
            ['number_of_contours']),
            title='Edit Cutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Cutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

