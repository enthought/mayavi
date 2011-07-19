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

from tvtk.tvtk_classes.image_decompose_filter import ImageDecomposeFilter


class ImageEuclideanDistance(ImageDecomposeFilter):
    """
    ImageEuclideanDistance - computes 3d Euclidean DT 
    
    Superclass: ImageDecomposeFilter
    
    ImageEuclideanDistance implements the Euclidean DT using Saito's
    algorithm. The distance map produced contains the square of the
    Euclidean distance values.
    
    The algorithm has a o(n^(D+1)) complexity over nxnx...xn images in D
    dimensions. It is very efficient on relatively small images.
    Cuisenaire's algorithms should be used instead if n >> 500. These are
    not implemented yet.
    
    For the special case of images where the slice-size is a multiple of
    2^N with a large N (typically for 256x256 slices), Saito's algorithm
    encounters a lot of cache conflicts during the 3rd iteration which
    can slow it very significantly. In that case, one should use
    ::_set_algorithm_to_saito_cached() instead for better performance.
    
    References:
    
    T. Saito and J.I. Toriwaki. New algorithms for Euclidean distance
    transformations of an n-dimensional digitised picture with
    applications. Pattern Recognition, 27(11). pp. 1551--1565, 1994.
    
    O. Cuisenaire. Distance Transformation: fast algorithms and
    applications to medical image processing. ph_d Thesis, Universite
    catholique de Louvain, October 1999.
    http://ltswww.epfl.ch/~cuisenai/papers/oc_thesis.pdf
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageEuclideanDistance, obj, update, **traits)
    
    initialize = tvtk_base.true_bool_trait(help=\
        """
        Used to set all non-zero voxels to maximum_distance before
        starting the distance transformation. Setting Initialize off
        keeps the current value in the input image as starting point.
        This allows to superimpose several distance maps.
        """
    )
    def _initialize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialize,
                        self.initialize_)

    consider_anisotropy = tvtk_base.true_bool_trait(help=\
        """
        Used to define whether Spacing should be used in the computation
        of the distances
        """
    )
    def _consider_anisotropy_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConsiderAnisotropy,
                        self.consider_anisotropy_)

    algorithm = traits.Trait('saito',
    tvtk_base.TraitRevPrefixMap({'saito_cached': 0, 'saito': 1}), help=\
        """
        Selects a Euclidean DT algorithm.
        1. Saito
        2. Saito-cached More algorithms will be added later on.
        """
    )
    def _algorithm_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlgorithm,
                        self.algorithm_)

    maximum_distance = traits.Float(2147483647.0, enter_set=True, auto_set=False, help=\
        """
        Any distance bigger than this->_maximum_distance will not ne
        computed but set to this->_maximum_distance instead.
        """
    )
    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    _updateable_traits_ = \
    (('dimensionality', 'GetDimensionality'), ('maximum_distance',
    'GetMaximumDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('algorithm', 'GetAlgorithm'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('initialize', 'GetInitialize'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('consider_anisotropy',
    'GetConsiderAnisotropy'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'consider_anisotropy', 'debug',
    'global_warning_display', 'initialize', 'release_data_flag',
    'algorithm', 'dimensionality', 'maximum_distance',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageEuclideanDistance, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['consider_anisotropy', 'initialize'], ['algorithm'],
            ['dimensionality', 'maximum_distance', 'number_of_threads']),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

