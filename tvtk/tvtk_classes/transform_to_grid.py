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


class TransformToGrid(Algorithm):
    """
    TransformToGrid - create a grid for a GridTransform
    
    Superclass: Algorithm
    
    TransformToGrid takes any transform as input and produces a grid
    for use by a GridTransform.  This can be used, for example, to
    invert a grid transform, concatenate two grid transforms, or to
    convert a thin plate spline transform into a grid transform.
    
    See Also:
    
    GridTransform ThinPlateSplineTransform AbstractTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformToGrid, obj, update, **traits)
    
    grid_scalar_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'char': 2, 'unsigned_char': 3, 'float': 11, 'unsigned_short': 5, 'short': 4}), help=\
        """
        Get/Set the scalar type of the grid.  The default is double.
        """
    )
    def _grid_scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridScalarType,
                        self.grid_scalar_type_)

    grid_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSpacing,
                        self.grid_spacing)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the transform which will be converted into a grid.
        """
    )

    grid_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridExtent,
                        self.grid_extent)

    grid_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridOrigin,
                        self.grid_origin)

    def _get_displacement_scale(self):
        return self._vtk_obj.GetDisplacementScale()
    displacement_scale = traits.Property(_get_displacement_scale, help=\
        """
        Get the scale and shift to convert integer grid elements into
        real values:  dx = scale*di + shift.  If the grid is of double
        type, then scale = 1 and shift = 0.
        """
    )

    def _get_displacement_shift(self):
        return self._vtk_obj.GetDisplacementShift()
    displacement_shift = traits.Property(_get_displacement_shift, help=\
        """
        Get the scale and shift to convert integer grid elements into
        real values:  dx = scale*di + shift.  If the grid is of double
        type, then scale = 1 and shift = 0.
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> ImageData
        C++: ImageData *GetOutput()
        Get the output data object for a port on this algorithm.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('grid_origin', 'GetGridOrigin'), ('grid_scalar_type',
    'GetGridScalarType'), ('progress_text', 'GetProgressText'),
    ('grid_spacing', 'GetGridSpacing'), ('grid_extent', 'GetGridExtent'),
    ('reference_count', 'GetReferenceCount'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'grid_scalar_type', 'grid_extent', 'grid_origin',
    'grid_spacing', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformToGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['grid_scalar_type'], ['grid_extent',
            'grid_origin', 'grid_spacing']),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

