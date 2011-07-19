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


class HyperStreamline(PolyDataAlgorithm):
    """
    HyperStreamline - generate hyperstreamline in arbitrary dataset
    
    Superclass: PolyDataAlgorithm
    
    HyperStreamline is a filter that integrates through a tensor field
    to generate a hyperstreamline. The integration is along the maximum
    eigenvector and the cross section of the hyperstreamline is defined
    by the two other eigenvectors. Thus the shape of the hyperstreamline
    is "tube-like", with the cross section being elliptical.
    Hyperstreamlines are used to visualize tensor fields.
    
    The starting point of a hyperstreamline can be defined in one of two
    ways. First, you may specify an initial position. This is a x-y-z
    global coordinate. The second option is to specify a starting
    location. This is cell_id, sub_id, and  cell parametric coordinates.
    
    The integration of the hyperstreamline occurs through the major
    eigenvector field. integration_step_length controls the step length
    within each cell (i.e., this is the fraction of the cell length). The
    length of the hyperstreamline is controlled by
    maximum_propagation_distance. This parameter is the length of the
    hyperstreamline in units of distance. The tube itself is composed of
    many small sub-tubes - number_of_sides controls the number of sides in
    the tube, and step_length controls the length of the sub-tubes.
    
    Because hyperstreamlines are often created near regions of
    singularities, it is possible to control the scaling of the tube
    cross section by using a logarithmic scale. Use log_scaling_on to turn
    this capability on. The Radius value controls the initial radius of
    the tube.
    
    See Also:
    
    TensorGlyph Streamer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperStreamline, obj, update, **traits)
    
    log_scaling = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off logarithmic scaling. If scaling is on, the log base
        10 of the computed eigenvalues are used to scale the cross
        section radii.
        """
    )
    def _log_scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogScaling,
                        self.log_scaling_)

    integration_direction = traits.Trait('forward',
    tvtk_base.TraitRevPrefixMap({'forward': 0, 'backward': 1, 'integrate_both_directions': 2}), help=\
        """
        Specify the direction in which to integrate the hyperstreamline.
        """
    )
    def _integration_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationDirection,
                        self.integration_direction_)

    integration_eigenvector = traits.Trait('major',
    tvtk_base.TraitRevPrefixMap({'major': 0, 'medium': 1, 'minor': 2}), help=\
        """
        Set / get the eigenvector field through which to ingrate. It is
        possible to integrate using the major, medium or minor
        eigenvector field.  The major eigenvector is the eigenvector
        whose corresponding eigenvalue is closest to positive infinity.
        The minor eigenvector is the eigenvector whose corresponding
        eigenvalue is closest to negative infinity.  The medium
        eigenvector is the eigenvector whose corresponding eigenvalue is
        between the major and minor eigenvalues.
        """
    )
    def _integration_eigenvector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationEigenvector,
                        self.integration_eigenvector_)

    terminal_eigenvalue = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/get terminal eigenvalue.  If major eigenvalue falls below
        this value, hyperstreamline terminates propagation.
        """
    )
    def _terminal_eigenvalue_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminalEigenvalue,
                        self.terminal_eigenvalue)

    integration_step_length = traits.Trait(0.2, traits.Range(0.001, 0.5, enter_set=True, auto_set=False), help=\
        """
        Set / get a nominal integration step size (expressed as a
        fraction of the size of each cell).
        """
    )
    def _integration_step_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationStepLength,
                        self.integration_step_length)

    start_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the start of the hyperstreamline in the global coordinate
        system. Starting from position implies that a search must be
        performed to find initial cell to start integration from.
        """
    )
    def _start_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPosition,
                        self.start_position)

    number_of_sides = traits.Trait(6, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set / get the number of sides for the hyperstreamlines. At a
        minimum, number of sides is 3.
        """
    )
    def _number_of_sides_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSides,
                        self.number_of_sides)

    radius = traits.Trait(0.5, traits.Range(0.0001, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set / get the initial tube radius. This is the maximum
        "elliptical" radius at the beginning of the tube. Radius varies
        based on ratio of eigenvalues.  Note that tube section is
        actually elliptical and may become a point or line in cross
        section in some cases.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    maximum_propagation_distance = traits.Trait(100.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set / get the maximum length of the hyperstreamline expressed as
        absolute distance (i.e., arc length) value.
        """
    )
    def _maximum_propagation_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPropagationDistance,
                        self.maximum_propagation_distance)

    step_length = traits.Trait(0.01, traits.Range(9.9999999999999995e-07, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / get the length of a tube segment composing the
        hyperstreamline. The length is specified as a fraction of the
        diagonal length of the input bounding box.
        """
    )
    def _step_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStepLength,
                        self.step_length)

    def get_start_location(self, *args):
        """
        V.get_start_location(int, [float, float, float]) -> int
        C++: IdType GetStartLocation(int &subId, double pcoords[3])
        Get the starting location of the hyperstreamline in the cell
        coordinate system. Returns the cell that the starting point is
        in.
        """
        ret = self._wrap_call(self._vtk_obj.GetStartLocation, *args)
        return ret

    def set_start_location(self, *args):
        """
        V.set_start_location(int, int, [float, float, float])
        C++: void SetStartLocation(IdType cellId, int subId,
            double pcoords[3])
        V.set_start_location(int, int, float, float, float)
        C++: void SetStartLocation(IdType cellId, int subId, double r,
            double s, double t)
        Specify the start of the hyperstreamline in the cell coordinate
        system. That is, cell_id and sub_id (if composite cell), and
        parametric coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetStartLocation, *args)
        return ret

    def integrate_major_eigenvector(self):
        """
        V.integrate_major_eigenvector()
        C++: void IntegrateMajorEigenvector()
        Use the major eigenvector field as the vector field through which
        to integrate.  The major eigenvector is the eigenvector whose
        corresponding eigenvalue is closest to positive infinity.
        """
        ret = self._vtk_obj.IntegrateMajorEigenvector()
        return ret
        

    def integrate_medium_eigenvector(self):
        """
        V.integrate_medium_eigenvector()
        C++: void IntegrateMediumEigenvector()
        Use the medium eigenvector field as the vector field through
        which to integrate. The medium eigenvector is the eigenvector
        whose corresponding eigenvalue is between the major and minor
        eigenvalues.
        """
        ret = self._vtk_obj.IntegrateMediumEigenvector()
        return ret
        

    def integrate_minor_eigenvector(self):
        """
        V.integrate_minor_eigenvector()
        C++: void IntegrateMinorEigenvector()
        Use the minor eigenvector field as the vector field through which
        to integrate. The minor eigenvector is the eigenvector whose
        corresponding eigenvalue is closest to negative infinity.
        """
        ret = self._vtk_obj.IntegrateMinorEigenvector()
        return ret
        

    _updateable_traits_ = \
    (('integration_eigenvector', 'GetIntegrationEigenvector'),
    ('log_scaling', 'GetLogScaling'), ('maximum_propagation_distance',
    'GetMaximumPropagationDistance'), ('release_data_flag',
    'GetReleaseDataFlag'), ('integration_step_length',
    'GetIntegrationStepLength'), ('start_position', 'GetStartPosition'),
    ('number_of_sides', 'GetNumberOfSides'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('radius', 'GetRadius'), ('integration_direction',
    'GetIntegrationDirection'), ('step_length', 'GetStepLength'),
    ('terminal_eigenvalue', 'GetTerminalEigenvalue'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'log_scaling',
    'release_data_flag', 'integration_direction',
    'integration_eigenvector', 'integration_step_length',
    'maximum_propagation_distance', 'number_of_sides', 'progress_text',
    'radius', 'start_position', 'step_length', 'terminal_eigenvalue'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperStreamline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperStreamline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['log_scaling'], ['integration_direction',
            'integration_eigenvector'], ['integration_step_length',
            'maximum_propagation_distance', 'number_of_sides', 'radius',
            'start_position', 'step_length', 'terminal_eigenvalue']),
            title='Edit HyperStreamline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperStreamline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

