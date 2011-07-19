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


class PointSource(PolyDataAlgorithm):
    """
    PointSource - create a random cloud of points
    
    Superclass: PolyDataAlgorithm
    
    PointSource is a source object that creates a user-specified
    number of points within a specified radius about a specified center
    point. By default location of the points is random within the sphere.
    It is also possible to generate random points only on the surface of
    the sphere.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointSource, obj, update, **traits)
    
    distribution = traits.Trait('uniform',
    tvtk_base.TraitRevPrefixMap({'shell': 0, 'uniform': 1}), help=\
        """
        Specify the distribution to use.  The default is a uniform
        distribution.  The shell distribution produces random points on
        the surface of the sphere, none in the interior.
        """
    )
    def _distribution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistribution,
                        self.distribution_)

    radius = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the radius of the point cloud.  If you are generating a
        Gaussian distribution, then this is the standard deviation for
        each of x, y, and z.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    number_of_points = traits.Trait(10, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of points to generate.
        """
    )
    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    _updateable_traits_ = \
    (('number_of_points', 'GetNumberOfPoints'), ('center', 'GetCenter'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('radius', 'GetRadius'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('distribution',
    'GetDistribution'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'distribution', 'center', 'number_of_points',
    'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['distribution'], ['center', 'number_of_points',
            'radius']),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

