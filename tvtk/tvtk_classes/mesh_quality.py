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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class MeshQuality(DataSetAlgorithm):
    """
    MeshQuality - Calculate functions of quality of the elements
    
    Superclass: DataSetAlgorithm
    
    MeshQuality computes one or more functions of (geometric) quality
    for each 2-D and 3-D cell (triangle, quadrilateral, tetrahedron, or
    hexahedron) of a mesh. These functions of quality are then averaged
    over the entire mesh. The minimum, average, maximum, and unbiased
    variance of quality for each type of cell is stored in the output
    mesh's field_data. The field_data arrays are named "Mesh Triangle
    Quality," "Mesh Quadrilateral Quality," "Mesh Tetrahedron Quality,"
    and "Mesh Hexahedron Quality." Each array has a single tuple with 5
    components. The first 4 components are the quality statistics
    mentioned above; the final value is the number of cells of the given
    type. This final component makes aggregation of statistics for
    distributed mesh data possible.
    
    By default, the per-cell quality is added to the mesh's cell data, in
    an array named "Quality." Cell types not supported by this filter
    will have an entry of 0. Use save_cell_quality_off() to store only the
    final statistics.
    
    This version of the filter written by Philippe Pebay and David
    Thompson overtakes an older version written by Leila Baghdadi, Hanif
    Ladak, and David Steinman at the Imaging Research Labs, Robarts
    Research Institute. That version only supported tetrahedral radius
    ratio. See the compatibility_mode_on() member for information on how to
    make this filter behave like the previous implementation. For more
    information on the triangle quality functions of this class, cf.
    Pebay & Baker 2003, Analysis of triangle quality measures, Math Comp
    72:244. For more information on the quadrangle quality functions of
    this class, cf. Pebay 2004, Planar Quadrangle Quality Measures, Eng
    Comp 20:2.
    
    Caveats:
    
    While more general than before, this class does not address many cell
    types, including wedges and pyramids in 3d and triangle strips and
    fans in 2d (among others). Most quadrilateral quality functions are
    intended for planar quadrilaterals only. The minimal angle is not,
    strictly speaking, a quality function, but it is provided because of
    its useage by many authors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMeshQuality, obj, update, **traits)
    
    compatibility_mode = tvtk_base.false_bool_trait(help=\
        """
        compatibility_mode governs whether, when both a quality function
        and cell volume are to be stored as cell data, the two values are
        stored in a single array. When compatibility mode is off (the
        default), two separate arrays are used -- one labeled "Quality"
        and the other labeled "Volume". When compatibility mode is on,
        both values are stored in a single array, with volume as the
        first component and quality as the second component.
        
        Enabling compatibility_mode changes the default tetrahedral
        quality function to VTK_QUALITY_RADIUS_RATIO and turns volume
        computation on. (This matches the default behavior of the initial
        implementation of MeshQuality.) You may change quality
        function and volume computation without leaving compatibility
        mode.
        
        Disabling compatibility mode does not affect the current volume
        computation or tetrahedral quality function settings.
        
        The final caveat to compatibility_mode is that regardless of its
        setting, the resulting array will be of type DoubleArray
        rather than the original FloatArray. This is a safety function
        to keep the authors from diving off of the Combinatorial Coding
        Cliff into Certain Insanity.
        """
    )
    def _compatibility_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompatibilityMode,
                        self.compatibility_mode_)

    volume = tvtk_base.false_bool_trait(help=\
        """
        These methods are deprecated. The functionality of computing cell
        volume is being removed until it can be computed for any 3d cell.
        (The previous implementation only worked for tetrahedra.)
        
        For now, turning on the volume computation will put this filter
        into "compatibility mode," where tetrahedral cell volume is
        stored in first component of each output tuple and the radius
        ratio is stored in the second component. You may also use
        compatibility_mode_on()/_off() to enter this mode. In this mode,
        cells other than tetrahedra will have report a volume of 0.0 (if
        volume computation is enabled).
        
        By default, volume computation is disabled and compatibility mode
        is off, since it does not make a lot of sense for meshes with
        non-tetrahedral cells.
        """
    )
    def _volume_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVolume,
                        self.volume_)

    ratio = tvtk_base.true_bool_trait(help=\
        """
        These methods are deprecated. Use get/_set_save_cell_quality()
        instead.
        
        Formerly, set_ratio could be used to disable computation of the
        tetrahedral radius ratio so that volume alone could be computed.
        Now, cell quality is always computed, but you may decide not to
        store the result for each cell. This allows average cell quality
        of a mesh to be calculated without requiring per-cell storage.
        """
    )
    def _ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRatio,
                        self.ratio_)

    save_cell_quality = tvtk_base.true_bool_trait(help=\
        """
        This variable controls whether or not cell quality is stored as
        cell data in the resulting mesh or discarded (leaving only the
        aggregate quality average of the entire mesh, recorded in the
        field_data).
        """
    )
    def _save_cell_quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSaveCellQuality,
                        self.save_cell_quality_)

    tet_quality_measure = traits.Trait('aspect_ratio',
    tvtk_base.TraitRevPrefixMap({'volume': 19, 'aspect_frobenius': 3, 'collapse_ratio': 7, 'aspect_beta': 29, 'distortion': 15, 'shape_and_size': 14, 'scaled_jacobian': 10, 'shape': 13, 'min_angle': 6, 'radius_ratio': 2, 'jacobian': 25, 'aspect_ratio': 1, 'aspect_gamma': 27, 'relative_size_squared': 12, 'edge_ratio': 0, 'condition': 9}), help=\
        """
        Set/Get the particular estimator used to measure the quality of
        tetrahedra. The default is VTK_QUALITY_RADIUS_RATIO (identical to
        Verdict's aspect ratio beta) and valid values also include
        VTK_QUALITY_ASPECT_RATIO, VTK_QUALITY_ASPECT_FROBENIUS,
        VTK_QUALITY_EDGE_RATIO, VTK_QUALITY_COLLAPSE_RATIO,
        VTK_QUALITY_ASPECT_BETA, VTK_QUALITY_ASPECT_GAMMA,
        VTK_QUALITY_VOLUME, VTK_QUALITY_CONDITION, VTK_QUALITY_JACOBIAN,
        VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_SHAPE,
        VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE_AND_SIZE,
        and VTK_QUALITY_DISTORTION.
        """
    )
    def _tet_quality_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTetQualityMeasure,
                        self.tet_quality_measure_)

    triangle_quality_measure = traits.Trait('aspect_ratio',
    tvtk_base.TraitRevPrefixMap({'aspect_frobenius': 3, 'area': 28, 'distortion': 15, 'shape_and_size': 14, 'scaled_jacobian': 10, 'shape': 13, 'min_angle': 6, 'radius_ratio': 2, 'aspect_ratio': 1, 'relative_size_squared': 12, 'edge_ratio': 0, 'condition': 9, 'max_angle': 8}), help=\
        """
        Set/Get the particular estimator used to function the quality of
        triangles. The default is VTK_QUALITY_RADIUS_RATIO and valid
        values also include VTK_QUALITY_ASPECT_RATIO,
        VTK_QUALITY_ASPECT_FROBENIUS, and VTK_QUALITY_EDGE_RATIO,
        VTK_QUALITY_MIN_ANGLE, VTK_QUALITY_MAX_ANGLE,
        VTK_QUALITY_CONDITION, VTK_QUALITY_SCALED_JACOBIAN,
        VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE,
        VTK_QUALITY_SHAPE_AND_SIZE, and VTK_QUALITY_DISTORTION.
        """
    )
    def _triangle_quality_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTriangleQualityMeasure,
                        self.triangle_quality_measure_)

    quad_quality_measure = traits.Trait('edge_ratio',
    tvtk_base.TraitRevPrefixMap({'distortion': 15, 'shape': 13, 'radius_ratio': 2, 'shear_and_size': 24, 'relative_size_squared': 12, 'shape_and_size': 14, 'med_aspect_frobenius': 4, 'area': 28, 'stretch': 20, 'skew': 17, 'warpage': 26, 'edge_ratio': 0, 'min_angle': 6, 'jacobian': 25, 'max_edge_ratios': 16, 'shear': 11, 'scaled_jacobian': 10, 'condition': 9, 'max_angle': 8, 'oddy': 23, 'taper': 18, 'max_aspect_frobenius': 5, 'aspect_ratio': 1}), help=\
        """
        Set/Get the particular estimator used to measure the quality of
        quadrilaterals. The default is VTK_QUALITY_EDGE_RATIO and valid
        values also include VTK_QUALITY_RADIUS_RATIO,
        VTK_QUALITY_ASPECT_RATIO, VTK_QUALITY_MAX_EDGE_RATIO
        VTK_QUALITY_SKEW, VTK_QUALITY_TAPER, VTK_QUALITY_WARPAGE,
        VTK_QUALITY_AREA, VTK_QUALITY_STRETCH, VTK_QUALITY_MIN_ANGLE,
        VTK_QUALITY_MAX_ANGLE, VTK_QUALITY_ODDY, VTK_QUALITY_CONDITION,
        VTK_QUALITY_JACOBIAN, VTK_QUALITY_SCALED_JACOBIAN,
        VTK_QUALITY_SHEAR, VTK_QUALITY_SHAPE,
        VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE_AND_SIZE,
        VTK_QUALITY_SHEAR_AND_SIZE, and VTK_QUALITY_DISTORTION.
        
        Scope: Except for VTK_QUALITY_EDGE_RATIO, these estimators are
        intended for planar quadrilaterals only; use at your own risk if
        you really want to assess non-planar quadrilateral quality with
        those.
        """
    )
    def _quad_quality_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuadQualityMeasure,
                        self.quad_quality_measure_)

    hex_quality_measure = traits.Trait('max_aspect_frobenius',
    tvtk_base.TraitRevPrefixMap({'oddy': 23, 'volume': 19, 'med_aspect_frobenius': 4, 'taper': 18, 'stretch': 20, 'skew': 17, 'max_aspect_frobenius': 5, 'relative_size_squared': 12, 'diagonal': 21, 'distortion': 15, 'shape_and_size': 14, 'scaled_jacobian': 10, 'shape': 13, 'shear': 11, 'jacobian': 25, 'shear_and_size': 24, 'max_edge_ratios': 16, 'dimension': 22, 'edge_ratio': 0, 'condition': 9}), help=\
        """
        Set/Get the particular estimator used to measure the quality of
        hexahedra. The default is VTK_QUALITY_MAX_ASPECT_FROBENIUS and
        valid values also include VTK_QUALITY_EDGE_RATIO,
        VTK_QUALITY_MAX_ASPECT_FROBENIUS, VTK_QUALITY_MAX_EDGE_RATIO,
        VTK_QUALITY_SKEW, VTK_QUALITY_TAPER, VTK_QUALITY_VOLUME,
        VTK_QUALITY_STRETCH, VTK_QUALITY_DIAGONAL, VTK_QUALITY_DIMENSION,
        VTK_QUALITY_ODDY, VTK_QUALITY_CONDITION, VTK_QUALITY_JACOBIAN,
        VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_SHEAR,
        VTK_QUALITY_SHAPE, VTK_QUALITY_RELATIVE_SIZE_SQUARED,
        VTK_QUALITY_SHAPE_AND_SIZE, VTK_QUALITY_SHEAR_AND_SIZE, and
        VTK_QUALITY_DISTORTION.
        """
    )
    def _hex_quality_measure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHexQualityMeasure,
                        self.hex_quality_measure_)

    def hex_condition(self, *args):
        """
        V.hex_condition(Cell) -> float
        C++: static double HexCondition(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexCondition, *my_args)
        return ret

    def hex_diagonal(self, *args):
        """
        V.hex_diagonal(Cell) -> float
        C++: static double HexDiagonal(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexDiagonal, *my_args)
        return ret

    def hex_dimension(self, *args):
        """
        V.hex_dimension(Cell) -> float
        C++: static double HexDimension(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexDimension, *my_args)
        return ret

    def hex_distortion(self, *args):
        """
        V.hex_distortion(Cell) -> float
        C++: static double HexDistortion(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexDistortion, *my_args)
        return ret

    def hex_edge_ratio(self, *args):
        """
        V.hex_edge_ratio(Cell) -> float
        C++: static double HexEdgeRatio(Cell *cell)
        This is a static function used to calculate the edge ratio of a
        hexahedron. It assumes that you pass the correct type of cell --
        no type checking is performed because this method is called from
        the inner loop of the Execute() member function. The edge ratio
        of a hexahedron $H $ is:$\frac{|H|_\infty}{|H|_0} $, where
        $|H|_\infty $ and $|H|_0 $ respectively denote the greatest and
        the smallest edge lengths of $H $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexEdgeRatio, *my_args)
        return ret

    def hex_jacobian(self, *args):
        """
        V.hex_jacobian(Cell) -> float
        C++: static double HexJacobian(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexJacobian, *my_args)
        return ret

    def hex_max_aspect_frobenius(self, *args):
        """
        V.hex_max_aspect_frobenius(Cell) -> float
        C++: static double HexMaxAspectFrobenius(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexMaxAspectFrobenius, *my_args)
        return ret

    def hex_max_edge_ratio(self, *args):
        """
        V.hex_max_edge_ratio(Cell) -> float
        C++: static double HexMaxEdgeRatio(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexMaxEdgeRatio, *my_args)
        return ret

    def hex_med_aspect_frobenius(self, *args):
        """
        V.hex_med_aspect_frobenius(Cell) -> float
        C++: static double HexMedAspectFrobenius(Cell *cell)
        This is a static function used to calculate the average Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexMedAspectFrobenius, *my_args)
        return ret

    def hex_oddy(self, *args):
        """
        V.hex_oddy(Cell) -> float
        C++: static double HexOddy(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexOddy, *my_args)
        return ret

    def hex_relative_size_squared(self, *args):
        """
        V.hex_relative_size_squared(Cell) -> float
        C++: static double HexRelativeSizeSquared(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexRelativeSizeSquared, *my_args)
        return ret

    def hex_scaled_jacobian(self, *args):
        """
        V.hex_scaled_jacobian(Cell) -> float
        C++: static double HexScaledJacobian(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexScaledJacobian, *my_args)
        return ret

    def hex_shape(self, *args):
        """
        V.hex_shape(Cell) -> float
        C++: static double HexShape(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexShape, *my_args)
        return ret

    def hex_shape_and_size(self, *args):
        """
        V.hex_shape_and_size(Cell) -> float
        C++: static double HexShapeAndSize(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexShapeAndSize, *my_args)
        return ret

    def hex_shear(self, *args):
        """
        V.hex_shear(Cell) -> float
        C++: static double HexShear(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexShear, *my_args)
        return ret

    def hex_shear_and_size(self, *args):
        """
        V.hex_shear_and_size(Cell) -> float
        C++: static double HexShearAndSize(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexShearAndSize, *my_args)
        return ret

    def hex_skew(self, *args):
        """
        V.hex_skew(Cell) -> float
        C++: static double HexSkew(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexSkew, *my_args)
        return ret

    def hex_stretch(self, *args):
        """
        V.hex_stretch(Cell) -> float
        C++: static double HexStretch(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexStretch, *my_args)
        return ret

    def hex_taper(self, *args):
        """
        V.hex_taper(Cell) -> float
        C++: static double HexTaper(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexTaper, *my_args)
        return ret

    def hex_volume(self, *args):
        """
        V.hex_volume(Cell) -> float
        C++: static double HexVolume(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 8 corner tetrahedra of a hexahedron, when the
        reference tetrahedral elements are right isosceles at the
        hexahedron vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HexVolume, *my_args)
        return ret

    def quad_area(self, *args):
        """
        V.quad_area(Cell) -> float
        C++: static double QuadArea(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadArea, *my_args)
        return ret

    def quad_aspect_ratio(self, *args):
        """
        V.quad_aspect_ratio(Cell) -> float
        C++: static double QuadAspectRatio(Cell *cell)
        This is a static function used to calculate the aspect ratio of a
        planar quadrilateral. It assumes that you pass the correct type
        of cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function. Use
        at your own risk with nonplanar quadrilaterals. The aspect ratio
        of a planar quadrilateral $q $ is:$\frac{|q|_1|q|_\infty}{4{\cal
        A}} $, where $|q|_1 $, $|q|_\infty $ and ${\cal A} $ respectively
        denote the perimeter, the greatest edge length and the area of $q
        $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadAspectRatio, *my_args)
        return ret

    def quad_condition(self, *args):
        """
        V.quad_condition(Cell) -> float
        C++: static double QuadCondition(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadCondition, *my_args)
        return ret

    def quad_distortion(self, *args):
        """
        V.quad_distortion(Cell) -> float
        C++: static double QuadDistortion(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadDistortion, *my_args)
        return ret

    def quad_edge_ratio(self, *args):
        """
        V.quad_edge_ratio(Cell) -> float
        C++: static double QuadEdgeRatio(Cell *cell)
        This is a static function used to calculate the edge ratio of a
        quadrilateral. It assumes that you pass the correct type of cell
        -- no type checking is performed because this method is called
        from the inner loop of the Execute() member function. The edge
        ratio of a quadrilateral $q $ is:$\frac{|q|_\infty}{|q|_0} $,
        where $|q|_\infty $ and $|q|_0 $ respectively denote the greatest
        and the smallest edge lengths of $q $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadEdgeRatio, *my_args)
        return ret

    def quad_jacobian(self, *args):
        """
        V.quad_jacobian(Cell) -> float
        C++: static double QuadJacobian(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadJacobian, *my_args)
        return ret

    def quad_max_angle(self, *args):
        """
        V.quad_max_angle(Cell) -> float
        C++: static double QuadMaxAngle(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadMaxAngle, *my_args)
        return ret

    def quad_max_aspect_frobenius(self, *args):
        """
        V.quad_max_aspect_frobenius(Cell) -> float
        C++: static double QuadMaxAspectFrobenius(Cell *cell)
        This is a static function used to calculate the maximal Frobenius
        aspect of the 4 corner triangles of a planar quadrilateral, when
        the reference triangle elements are right isosceles at the
        quadrangle vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function. Use
        at your own risk with nonplanar quadrilaterals. The Frobenius
        aspect of a triangle $t $, when the reference element is right
        isosceles at vertex $V $, is:$\frac{f^2+g^2}{4{\cal A}} $, where
        $f^2+g^2 $ and $\cal A $ respectively denote the sum of the
        squared lengths of the edges attached to $V $ and the area of $t
        $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadMaxAspectFrobenius, *my_args)
        return ret

    def quad_max_edge_ratios(self, *args):
        """
        V.quad_max_edge_ratios(Cell) -> float
        C++: static double QuadMaxEdgeRatios(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadMaxEdgeRatios, *my_args)
        return ret

    def quad_med_aspect_frobenius(self, *args):
        """
        V.quad_med_aspect_frobenius(Cell) -> float
        C++: static double QuadMedAspectFrobenius(Cell *cell)
        This is a static function used to calculate the average Frobenius
        aspect of the 4 corner triangles of a planar quadrilateral, when
        the reference triangle elements are right isosceles at the
        quadrangle vertices. It assumes that you pass the correct type of
        cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function. Use
        at your own risk with nonplanar quadrilaterals. The Frobenius
        aspect of a triangle $t $, when the reference element is right
        isosceles at vertex $V $, is:$\frac{f^2+g^2}{4{\cal A}} $, where
        $f^2+g^2 $ and $\cal A $ respectively denote the sum of the
        squared lengths of the edges attached to $V $ and the area of $t
        $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadMedAspectFrobenius, *my_args)
        return ret

    def quad_min_angle(self, *args):
        """
        V.quad_min_angle(Cell) -> float
        C++: static double QuadMinAngle(Cell *cell)
        This is a static function used to calculate the minimal
        (nonoriented) angle of a quadrilateral, expressed in degrees. It
        assumes that you pass the correct type of cell -- no type
        checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadMinAngle, *my_args)
        return ret

    def quad_oddy(self, *args):
        """
        V.quad_oddy(Cell) -> float
        C++: static double QuadOddy(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadOddy, *my_args)
        return ret

    def quad_radius_ratio(self, *args):
        """
        V.quad_radius_ratio(Cell) -> float
        C++: static double QuadRadiusRatio(Cell *cell)
        This is a static function used to calculate the radius ratio of a
        planar quadrilateral. The name is only used by analogy with the
        triangle radius ratio, because in general a quadrilateral does
        not have a circumcircle nor an incircle. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function. Use at your own risk with nonplanar quadrilaterals. The
        radius ratio of a planar quadrilateral $q $
        is:$\frac{|q|_2h_{\max}}{\min_i{\cal A}_i} $, where $|q|_2 $,
        $h_{\max} $ and $\min{\cal A}_i $ respectively denote the sum of
        the squared edge lengths, the greatest amongst diagonal and edge
        lengths and the smallest area of the 4 triangles extractable from
        $q $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadRadiusRatio, *my_args)
        return ret

    def quad_relative_size_squared(self, *args):
        """
        V.quad_relative_size_squared(Cell) -> float
        C++: static double QuadRelativeSizeSquared(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadRelativeSizeSquared, *my_args)
        return ret

    def quad_scaled_jacobian(self, *args):
        """
        V.quad_scaled_jacobian(Cell) -> float
        C++: static double QuadScaledJacobian(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadScaledJacobian, *my_args)
        return ret

    def quad_shape(self, *args):
        """
        V.quad_shape(Cell) -> float
        C++: static double QuadShape(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadShape, *my_args)
        return ret

    def quad_shape_and_size(self, *args):
        """
        V.quad_shape_and_size(Cell) -> float
        C++: static double QuadShapeAndSize(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadShapeAndSize, *my_args)
        return ret

    def quad_shear(self, *args):
        """
        V.quad_shear(Cell) -> float
        C++: static double QuadShear(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadShear, *my_args)
        return ret

    def quad_shear_and_size(self, *args):
        """
        V.quad_shear_and_size(Cell) -> float
        C++: static double QuadShearAndSize(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadShearAndSize, *my_args)
        return ret

    def quad_skew(self, *args):
        """
        V.quad_skew(Cell) -> float
        C++: static double QuadSkew(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadSkew, *my_args)
        return ret

    def quad_stretch(self, *args):
        """
        V.quad_stretch(Cell) -> float
        C++: static double QuadStretch(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadStretch, *my_args)
        return ret

    def quad_taper(self, *args):
        """
        V.quad_taper(Cell) -> float
        C++: static double QuadTaper(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadTaper, *my_args)
        return ret

    def quad_warpage(self, *args):
        """
        V.quad_warpage(Cell) -> float
        C++: static double QuadWarpage(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.QuadWarpage, *my_args)
        return ret

    def tet_aspect_beta(self, *args):
        """
        V.tet_aspect_beta(Cell) -> float
        C++: static double TetAspectBeta(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetAspectBeta, *my_args)
        return ret

    def tet_aspect_frobenius(self, *args):
        """
        V.tet_aspect_frobenius(Cell) -> float
        C++: static double TetAspectFrobenius(Cell *cell)
        This is a static function used to calculate the Frobenius
        condition number of the transformation matrix from a regular
        tetrahedron to a tetrahedron. It assumes that you pass the
        correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function. The Frobenius aspect of a tetrahedron $K $, when the
        reference element is regular,
        is:$\frac{\frac{3}{2}(l_{11}+l_{22}+l_{33}) -
        (l_{12}+l_{13}+l_{23})} {3(\sqrt{2}\det{T})^\frac{2}{3}} $, where
        $T $ and $l_{ij} $ respectively denote the edge matrix of $K $
        and the entries of $L=T^t\,T $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetAspectFrobenius, *my_args)
        return ret

    def tet_aspect_gamma(self, *args):
        """
        V.tet_aspect_gamma(Cell) -> float
        C++: static double TetAspectGamma(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetAspectGamma, *my_args)
        return ret

    def tet_aspect_ratio(self, *args):
        """
        V.tet_aspect_ratio(Cell) -> float
        C++: static double TetAspectRatio(Cell *cell)
        This is a static function used to calculate the aspect ratio of a
        tetrahedron. It assumes that you pass the correct type of cell --
        no type checking is performed because this method is called from
        the inner loop of the Execute() member function. The aspect ratio
        of a tetrahedron $K $ is:$\frac{|K|_\infty}{2\sqrt{6}r} $, where
        $|K|_\infty $ and $r $ respectively denote the greatest edge
        length and the inradius of $K $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetAspectRatio, *my_args)
        return ret

    def tet_collapse_ratio(self, *args):
        """
        V.tet_collapse_ratio(Cell) -> float
        C++: static double TetCollapseRatio(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetCollapseRatio, *my_args)
        return ret

    def tet_condition(self, *args):
        """
        V.tet_condition(Cell) -> float
        C++: static double TetCondition(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetCondition, *my_args)
        return ret

    def tet_distortion(self, *args):
        """
        V.tet_distortion(Cell) -> float
        C++: static double TetDistortion(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetDistortion, *my_args)
        return ret

    def tet_edge_ratio(self, *args):
        """
        V.tet_edge_ratio(Cell) -> float
        C++: static double TetEdgeRatio(Cell *cell)
        This is a static function used to calculate the edge ratio of a
        tetrahedron. It assumes that you pass the correct type of cell --
        no type checking is performed because this method is called from
        the inner loop of the Execute() member function. The edge ratio
        of a tetrahedron $K $ is:$\frac{|K|_\infty}{|K|_0} $, where
        $|K|_\infty $ and $|K|_0 $ respectively denote the greatest and
        the smallest edge lengths of $K $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetEdgeRatio, *my_args)
        return ret

    def tet_jacobian(self, *args):
        """
        V.tet_jacobian(Cell) -> float
        C++: static double TetJacobian(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetJacobian, *my_args)
        return ret

    def tet_min_angle(self, *args):
        """
        V.tet_min_angle(Cell) -> float
        C++: static double TetMinAngle(Cell *cell)
        This is a static function used to calculate the minimal
        (nonoriented) dihedral angle of a tetrahedron, expressed in
        degrees. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetMinAngle, *my_args)
        return ret

    def tet_radius_ratio(self, *args):
        """
        V.tet_radius_ratio(Cell) -> float
        C++: static double TetRadiusRatio(Cell *cell)
        This is a static function used to calculate the radius ratio of a
        tetrahedron. It assumes that you pass the correct type of cell --
        no type checking is performed because this method is called from
        the inner loop of the Execute() member function. The radius ratio
        of a tetrahedron $K $ is:$\frac{R}{3r} $, where $R $ and $r $
        respectively denote the circumradius and the inradius of $K $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetRadiusRatio, *my_args)
        return ret

    def tet_relative_size_squared(self, *args):
        """
        V.tet_relative_size_squared(Cell) -> float
        C++: static double TetRelativeSizeSquared(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetRelativeSizeSquared, *my_args)
        return ret

    def tet_scaled_jacobian(self, *args):
        """
        V.tet_scaled_jacobian(Cell) -> float
        C++: static double TetScaledJacobian(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetScaledJacobian, *my_args)
        return ret

    def tet_shape(self, *args):
        """
        V.tet_shape(Cell) -> float
        C++: static double TetShape(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetShape, *my_args)
        return ret

    def tet_shapeand_size(self, *args):
        """
        V.tet_shapeand_size(Cell) -> float
        C++: static double TetShapeandSize(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetShapeandSize, *my_args)
        return ret

    def tet_volume(self, *args):
        """
        V.tet_volume(Cell) -> float
        C++: static double TetVolume(Cell *cell)
        This is a static function used to calculate the collapse ratio of
        a tetrahedron. The collapse ratio is a dimensionless number
        defined as the smallest ratio of the height of a vertex above its
        opposing triangle to the longest edge of that opposing triangle
        across all vertices of the tetrahedron. It assumes that you pass
        the correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TetVolume, *my_args)
        return ret

    def triangle_area(self, *args):
        """
        V.triangle_area(Cell) -> float
        C++: static double TriangleArea(Cell *cell)
        This is a static function used to calculate the area of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleArea, *my_args)
        return ret

    def triangle_aspect_frobenius(self, *args):
        """
        V.triangle_aspect_frobenius(Cell) -> float
        C++: static double TriangleAspectFrobenius(Cell *cell)
        This is a static function used to calculate the Frobenius
        condition number of the transformation matrix from an equilateral
        triangle to a triangle. It assumes that you pass the correct type
        of cell -- no type checking is performed because this method is
        called from the inner loop of the Execute() member function. The
        Frobenius aspect of a triangle $t $, when the reference element
        is equilateral, is:$\frac{|t|^2_2}{2\sqrt{3}{\cal A}} $, where
        $|t|^2_2 $ and $\cal A $ respectively denote the sum of the
        squared edge lengths and the area of $t $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleAspectFrobenius, *my_args)
        return ret

    def triangle_aspect_ratio(self, *args):
        """
        V.triangle_aspect_ratio(Cell) -> float
        C++: static double TriangleAspectRatio(Cell *cell)
        This is a static function used to calculate the aspect ratio of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function. The aspect ratio of
        a triangle $t $ is:$\frac{|t|_\infty}{2\sqrt{3}r} $, where
        $|t|_\infty $ and $r $ respectively denote the greatest edge
        length and the inradius of $t $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleAspectRatio, *my_args)
        return ret

    def triangle_condition(self, *args):
        """
        V.triangle_condition(Cell) -> float
        C++: static double TriangleCondition(Cell *cell)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleCondition, *my_args)
        return ret

    def triangle_distortion(self, *args):
        """
        V.triangle_distortion(Cell) -> float
        C++: static double TriangleDistortion(Cell *cell)
        This is a static function used to calculate the distortion of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleDistortion, *my_args)
        return ret

    def triangle_edge_ratio(self, *args):
        """
        V.triangle_edge_ratio(Cell) -> float
        C++: static double TriangleEdgeRatio(Cell *cell)
        This is a static function used to calculate the edge ratio of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function. The edge ratio of a
        triangle $t $ is:$\frac{|t|_\infty}{|t|_0} $, where $|t|_\infty $
        and $|t|_0 $ respectively denote the greatest and the smallest
        edge lengths of $t $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleEdgeRatio, *my_args)
        return ret

    def triangle_max_angle(self, *args):
        """
        V.triangle_max_angle(Cell) -> float
        C++: static double TriangleMaxAngle(Cell *cell)
        This is a static function used to calculate the maximal
        (nonoriented) angle of a triangle, expressed in degrees. It
        assumes that you pass the correct type of cell -- no type
        checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleMaxAngle, *my_args)
        return ret

    def triangle_min_angle(self, *args):
        """
        V.triangle_min_angle(Cell) -> float
        C++: static double TriangleMinAngle(Cell *cell)
        This is a static function used to calculate the minimal
        (nonoriented) angle of a triangle, expressed in degrees. It
        assumes that you pass the correct type of cell -- no type
        checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleMinAngle, *my_args)
        return ret

    def triangle_radius_ratio(self, *args):
        """
        V.triangle_radius_ratio(Cell) -> float
        C++: static double TriangleRadiusRatio(Cell *cell)
        This is a static function used to calculate the radius ratio of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function. The radius ratio of
        a triangle $t $ is:$\frac{R}{2r} $, where $R $ and $r $
        respectively denote the circumradius and the inradius of $t $.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleRadiusRatio, *my_args)
        return ret

    def triangle_relative_size_squared(self, *args):
        """
        V.triangle_relative_size_squared(Cell) -> float
        C++: static double TriangleRelativeSizeSquared(Cell *cell)
        This is a static function used to calculate the square of the
        relative size of a triangle. It assumes that you pass the correct
        type of cell -- no type checking is performed because this method
        is called from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleRelativeSizeSquared, *my_args)
        return ret

    def triangle_scaled_jacobian(self, *args):
        """
        V.triangle_scaled_jacobian(Cell) -> float
        C++: static double TriangleScaledJacobian(Cell *cell)
        This is a static function used to calculate the scaled Jacobian
        of a triangle. It assumes that you pass the correct type of cell
        -- no type checking is performed because this method is called
        from the inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleScaledJacobian, *my_args)
        return ret

    def triangle_shape(self, *args):
        """
        V.triangle_shape(Cell) -> float
        C++: static double TriangleShape(Cell *cell)
        This is a static function used to calculate the shape of a
        triangle. It assumes that you pass the correct type of cell -- no
        type checking is performed because this method is called from the
        inner loop of the Execute() member function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleShape, *my_args)
        return ret

    def triangle_shape_and_size(self, *args):
        """
        V.triangle_shape_and_size(Cell) -> float
        C++: static double TriangleShapeAndSize(Cell *cell)
        This is a static function used to calculate the product of shape
        and relative size of a triangle. It assumes that you pass the
        correct type of cell -- no type checking is performed because
        this method is called from the inner loop of the Execute() member
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleShapeAndSize, *my_args)
        return ret

    _updateable_traits_ = \
    (('ratio', 'GetRatio'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('tet_quality_measure',
    'GetTetQualityMeasure'), ('compatibility_mode',
    'GetCompatibilityMode'), ('hex_quality_measure',
    'GetHexQualityMeasure'), ('progress_text', 'GetProgressText'),
    ('triangle_quality_measure', 'GetTriangleQualityMeasure'), ('volume',
    'GetVolume'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('save_cell_quality', 'GetSaveCellQuality'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('quad_quality_measure', 'GetQuadQualityMeasure'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compatibility_mode', 'debug',
    'global_warning_display', 'ratio', 'release_data_flag',
    'save_cell_quality', 'volume', 'hex_quality_measure',
    'quad_quality_measure', 'tet_quality_measure',
    'triangle_quality_measure', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MeshQuality, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MeshQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compatibility_mode', 'ratio', 'save_cell_quality',
            'volume'], ['hex_quality_measure', 'quad_quality_measure',
            'tet_quality_measure', 'triangle_quality_measure'], []),
            title='Edit MeshQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MeshQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

