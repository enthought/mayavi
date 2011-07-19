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


class CubeSource(PolyDataAlgorithm):
    """
    CubeSource - create a polygonal representation of a cube
    
    Superclass: PolyDataAlgorithm
    
    CubeSource creates a cube centered at origin. The cube is
    represented with four-sided polygons. It is possible to specify the
    length, width, and height of the cube independently.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCubeSource, obj, update, **traits)
    
    z_length = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the length of the cube in the z-direction.
        """
    )
    def _z_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZLength,
                        self.z_length)

    x_length = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the length of the cube in the x-direction.
        """
    )
    def _x_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXLength,
                        self.x_length)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    y_length = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the length of the cube in the y-direction.
        """
    )
    def _y_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYLength,
                        self.y_length)

    def set_bounds(self, *args):
        """
        V.set_bounds(float, float, float, float, float, float)
        C++: void SetBounds(double xMin, double xMax, double yMin,
            double yMax, double zMin, double zMax)
        V.set_bounds([float, float, float, float, float, float])
        C++: void SetBounds(double bounds[6])
        Convenience method allows creation of cube by specifying bounding
        box.
        """
        ret = self._wrap_call(self._vtk_obj.SetBounds, *args)
        return ret

    _updateable_traits_ = \
    (('z_length', 'GetZLength'), ('center', 'GetCenter'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'), ('x_length',
    'GetXLength'), ('y_length', 'GetYLength'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'progress_text', 'x_length',
    'y_length', 'z_length'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CubeSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CubeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'x_length', 'y_length',
            'z_length']),
            title='Edit CubeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CubeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

