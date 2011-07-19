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


class MarchingSquares(PolyDataAlgorithm):
    """
    MarchingSquares - generate isoline(s) from structured points set
    
    Superclass: PolyDataAlgorithm
    
    MarchingSquares is a filter that takes as input a structured
    points set and generates on output one or more isolines.  One or more
    contour values must be specified to generate the isolines. 
    Alternatively, you can specify a min/max scalar range and the number
    of contours to generate a series of evenly spaced contour values.
    
    To generate contour lines the input data must be of topological
    dimension 2 (i.e., an image). If not, you can use the image_range ivar
    to select an image plane from an input volume. This avoids having to
    extract a plane first (using ExtractSubVolume).  The filter deals
    with this by first trying to use the input data directly, and if not
    a 2d image, then uses the image_range ivar to reduce it to an image.
    
    Caveats:
    
    This filter is specialized to images. If you are interested in
    contouring other types of data, use the general ContourFilter.
    
    See Also:
    
    ContourFilter MarchingCubes SliceCubes DividingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMarchingSquares, obj, update, **traits)
    
    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        
        """
    )

    image_range = traits.Array(shape=(6,), value=(0, 2147483647, 0, 2147483647, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the i-j-k index range which define a plane on which to
        generate contour lines. Using this ivar it is possible to input a
        3d volume directly and then generate contour lines on one of the
        i-j-k planes, or a portion of a plane.
        """
    )
    def _image_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageRange,
                        self.image_range)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Methods to set contour values
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
        Methods to set contour values
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('image_range', 'GetImageRange'),
    ('number_of_contours', 'GetNumberOfContours'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'image_range', 'number_of_contours',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MarchingSquares, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MarchingSquares properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['image_range', 'number_of_contours']),
            title='Edit MarchingSquares properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MarchingSquares properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

