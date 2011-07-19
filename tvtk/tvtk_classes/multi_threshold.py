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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class MultiThreshold(MultiBlockDataSetAlgorithm):
    """
    MultiThreshold - Threshold cells within multiple intervals
    
    Superclass: MultiBlockDataSetAlgorithm
    
    This filter can be substituted for a chain of several Threshold
    filters and can also perform more sophisticated subsetting
    operations. It generates a MultiBlockDataSet as its output. This
    multiblock dataset contains a UnstructuredGrid for each
    thresholded subset you request. A thresholded subset can be a set
    defined by an interval over a point or cell attribute of the mesh;
    these subsets are called interval_sets. A thresholded subset can also
    be a boolean combination of one or more interval_sets; these subsets
    are called boolean_sets. boolean_sets allow complex logic since their
    output can depend on multiple intervals over multiple variables
    defined on the input mesh. This is useful because it eliminates the
    need for thresholding several times and then appending the results,
    as can be required with Threshold when one wants to remove some
    range of values (e.g., a notch filter). Cells are not repeated when
    they belong to more than one interval unless those intervals have
    different output grids.
    
    Another advantage this filter provides over Threshold is the
    ability to threshold on non-scalar (i.e., vector, tensor, etc.)
    attributes without first computing an array containing some norm of
    the desired attribute. MultiThreshold provides $L_1 $, $L_2 $, and
    $L_{\infty} $ norms.
    
    This filter makes a distinction between intermediate subsets and
    subsets that will be output to a grid. Each intermediate subset you
    create with add_interval_set or add_boolean_set is given a unique integer
    identifier (via the return values of these member functions). If you
    wish for a given set to be output, you must call output_set and pass
    it one of these identifiers. The return of output_set is the integer
    index of the output set in the multiblock dataset created by this
    filter.
    
    For example, if an input mesh defined three attributes T, P, and s,
    one might wish to find cells that satisfy "T < 320 [K] && ( P > 101 [k_pa] || s < 0.1 [k_j/kg/_k]
    )". To accomplish this with a MultiThreshold filter,
    
    MultiThreshold* thr; int interval_sets[_3];
    
    interval_sets[_0] = thr->_add_interval_set( Math::NegInf(), 320.,
    MultiThreshold::CLOSED, MultiThreshold::OPEN,
        DataObject::FIELD_ASSOCIATION_POINTS, "T", 0, 1 );
    interval_sets[_1] = thr->_add_interval_set( 101., Math::Inf(),
    MultiThreshold::OPEN, MultiThreshold::CLOSED,
        DataObject::FIELD_ASSOCIATION_CELLS, "P", 0, 1 );
    interval_sets[_2] = thr->_add_interval_set( Math::NegInf(), 0.1,
    MultiThreshold::CLOSED, MultiThreshold::OPEN,
        DataObject::FIELD_ASSOCIATION_POINTS, "s", 0, 1 );
    
    int intermediate = thr->_add_boolean_set( MultiThreshold::OR, 2,
    &interval_sets[_1] );
    
    int intersection[2]; intersection[0] = interval_sets[_0];
    intersection[1] = intermediate; int output_set = thr->_add_boolean_set(
    MultiThreshold::AND, 2, intersection );
    
    int output_grid_index = thr->_output_set( output_set ); thr->Update(); 
    The result of this filter will be a multiblock dataset that contains
    a single child with the desired cells. If we had also called
    thr->_output_set( interval_sets[_0] );, there would be two child meshes
    and one would contain all cells with T < 320 [K]. In that case, the
    output can be represented by this graph\dot digraph multi_threshold {
      set0 [shape=rect,style=filled,label="point T(0) in [-Inf,320["]
      set1 [shape=rect,label="cell P(0) in ]101,Inf]"]
      set2 [shape=rect,label="point s(0) in [-Inf,0.1["]
      set3 [shape=rect,label="OR"]
      set4 [shape=rect,style=filled,label="AND"]
      set0 -> set4
      set1 -> set3
      set2 -> set3
      set3 -> set4 }\enddot The filled rectangles represent sets that are
    output.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiThreshold, obj, update, **traits)
    
    def add_bandpass_interval_set(self, *args):
        """
        V.add_bandpass_interval_set(float, float, int, string, int, int)
            -> int
        C++: int AddBandpassIntervalSet(double xmin, double xmax,
            int assoc, const char *arrayName, int component,
            int allScalars)
        These convenience members make it easy to insert closed
        intervals. The "notch" interval is accomplished by creating a
        bandpass interval and applying a NAND operation. In this case,
        the set ID returned in the NAND operation set ID. Note that you
        can pass xmin == xmax when creating a bandpass threshold to
        retrieve elements matching exactly one value (since the intervals
        created by these routines are closed).
        """
        ret = self._wrap_call(self._vtk_obj.AddBandpassIntervalSet, *args)
        return ret

    def add_highpass_interval_set(self, *args):
        """
        V.add_highpass_interval_set(float, int, string, int, int) -> int
        C++: int AddHighpassIntervalSet(double xmin, int assoc,
            const char *arrayName, int component, int allScalars)
        These convenience members make it easy to insert closed
        intervals. The "notch" interval is accomplished by creating a
        bandpass interval and applying a NAND operation. In this case,
        the set ID returned in the NAND operation set ID. Note that you
        can pass xmin == xmax when creating a bandpass threshold to
        retrieve elements matching exactly one value (since the intervals
        created by these routines are closed).
        """
        ret = self._wrap_call(self._vtk_obj.AddHighpassIntervalSet, *args)
        return ret

    def add_interval_set(self, *args):
        """
        V.add_interval_set(float, float, int, int, int, string, int, int)
            -> int
        C++: int AddIntervalSet(double xmin, double xmax, int omin,
            int omax, int assoc, const char *arrayName, int component,
            int allScalars)
        V.add_interval_set(float, float, int, int, int, int, int, int)
            -> int
        C++: int AddIntervalSet(double xmin, double xmax, int omin,
            int omax, int assoc, int attribType, int component,
            int allScalars)
        Add a mesh subset to be computed by thresholding an attribute of
        the input mesh. The subset can then be added to an output mesh
        with ouput_set() or combined with other sets using add_boolean_set.
        If you wish to include all cells with values below some number a,
        call with xmin set to Math::NegInf() and xmax set to a.
        Similarly, if you wish to include all cells with values above
        some number a, call with xmin set to a and xmax set to
        Math::Inf(). When specifying Inf() or neg_inf() for an
        endpoint, it does not matter whether you specify and open or
        closed endpoint.
        
        When creating intervals, any integers can be used for the IDs of
        output meshes. All that matters is that the same ID be used if
        intervals should output to the same mesh. The outputs are ordered
        with ascending IDs in output block 0.
        
        It is possible to specify an invalid interval, in which case
        these routines will return -1. Invalid intervals occur when
        - an array does not exist,
        - center is invalid,
        - xmin == xmax and omin and/or omax are MultiThreshold::OPEN,
          or
        - xmin > xmax.
        - xmin or xmax is not a number (i.e., IEEE na_n). Having both xmin
        and xmax equal na_n is allowed. Math provides a portable way to
        specify IEEE infinities and Nan. Note that specifying an interval
        completely out of the bounds of an attribute is considered valid.
          In fact, it is occasionally useful to create a closed interval
          with both endpoints set to $\infty $ or both endpoints set to
          $-\infty $ in order to locate cells with problematic values.
        
        @param xmin The minimum attribute val ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.AddIntervalSet, *args)
        return ret

    def add_lowpass_interval_set(self, *args):
        """
        V.add_lowpass_interval_set(float, int, string, int, int) -> int
        C++: int AddLowpassIntervalSet(double xmax, int assoc,
            const char *arrayName, int component, int allScalars)
        These convenience members make it easy to insert closed
        intervals. The "notch" interval is accomplished by creating a
        bandpass interval and applying a NAND operation. In this case,
        the set ID returned in the NAND operation set ID. Note that you
        can pass xmin == xmax when creating a bandpass threshold to
        retrieve elements matching exactly one value (since the intervals
        created by these routines are closed).
        """
        ret = self._wrap_call(self._vtk_obj.AddLowpassIntervalSet, *args)
        return ret

    def add_notch_interval_set(self, *args):
        """
        V.add_notch_interval_set(float, float, int, string, int, int) -> int
        C++: int AddNotchIntervalSet(double xlo, double xhi, int assoc,
            const char *arrayName, int component, int allScalars)
        These convenience members make it easy to insert closed
        intervals. The "notch" interval is accomplished by creating a
        bandpass interval and applying a NAND operation. In this case,
        the set ID returned in the NAND operation set ID. Note that you
        can pass xmin == xmax when creating a bandpass threshold to
        retrieve elements matching exactly one value (since the intervals
        created by these routines are closed).
        """
        ret = self._wrap_call(self._vtk_obj.AddNotchIntervalSet, *args)
        return ret

    def output_set(self, *args):
        """
        V.output_set(int) -> int
        C++: int OutputSet(int setId)
        Create an output mesh containing a boolean or interval subset of
        the input mesh.
        """
        ret = self._wrap_call(self._vtk_obj.OutputSet, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Remove all the intervals currently defined.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiThreshold, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MultiThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

