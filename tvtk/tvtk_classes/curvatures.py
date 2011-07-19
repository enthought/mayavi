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


class Curvatures(PolyDataAlgorithm):
    """
    Curvatures - compute curvatures (Gauss and mean) of a Polydata
    object
    
    Superclass: PolyDataAlgorithm
    
    Curvatures takes a polydata input and computes the curvature of
    the mesh at each point. Four possible methods of computation are
    available :
    
    Gauss Curvature discrete Gauss curvature (K) computation,$K(vertex v)
    = 2*PI-\sum_{facet neighbs f of v} (angle_f at v) $ The contribution
    of every facet is for the moment weighted by $Area(facet)/3 $ The
    units of Gaussian Curvature are $[1/m^2] $
    
    Mean Curvature$H(vertex v) = average over edges neighbs e of H(e)
    $$H(edge e) = length(e)*dihedral_angle(e) $ NB: dihedral_angle is the
    ORIENTED angle between -PI and PI, this means that the surface is
    assumed to be orientable the computation creates the orientation The
    units of Mean Curvature are [1/m]
    
    Maximum ( $k_max $) and Minimum ( $k_min $) Principal
    Curvatures$k_max = H + sqrt(H^2 - K) $$k_min = H - sqrt(H^2 - K) $
    Excepting spherical and planar surfaces which have equal principal
    curvatures, the curvature at a point on a surface varies with the
    direction one "sets off" from the point. For all directions, the
    curvature will pass through two extrema: a minimum ( $k_min $) and a
    maximum ( $k_max $) which occur at mutually orthogonal directions to
    each other.
    
    NB. The sign of the Gauss curvature is a geometric ivariant, it
    should be +ve when the surface looks like a sphere, -ve when it looks
    like a saddle, however, the sign of the Mean curvature is not, it
    depends on the convention for normals - This code assumes that
    normals point outwards (ie from the surface of a sphere outwards). If
    a given mesh produces curvatures of opposite senses then the flag
    invert_mean_curvature can be set and the Curvature reported by the Mean
    calculation will be inverted.
    
    Thanks:
    
    Philip Batchelor philipp.batchelor@kcl.ac.uk for creating and
    contributing the class and Andrew Maclean a.maclean@acfr.usyd.edu.au
    for cleanups and fixes. Thanks also to Goodwin Lawlor for
    contributing patch to calculate principal curvatures
    
    See Also:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCurvatures, obj, update, **traits)
    
    invert_mean_curvature = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which inverts the mean curvature calculation for
        meshes with inward pointing normals (default false)
        """
    )
    def _invert_mean_curvature_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInvertMeanCurvature,
                        self.invert_mean_curvature_)

    curvature_type = traits.Trait('gaussian',
    tvtk_base.TraitRevPrefixMap({'mean': 1, 'minimum': 3, 'gaussian': 0, 'maximum': 2}), help=\
        """
        Set/Get Curvature type VTK_CURVATURE_GAUSS: Gaussian curvature,
        stored as data_array "Gauss_Curvature" VTK_CURVATURE_MEAN : Mean
        curvature, stored as data_array "Mean_Curvature"
        """
    )
    def _curvature_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurvatureType,
                        self.curvature_type_)

    _updateable_traits_ = \
    (('curvature_type', 'GetCurvatureType'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('invert_mean_curvature',
    'GetInvertMeanCurvature'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'invert_mean_curvature', 'release_data_flag', 'curvature_type',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Curvatures, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Curvatures properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['invert_mean_curvature'], ['curvature_type'], []),
            title='Edit Curvatures properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Curvatures properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

