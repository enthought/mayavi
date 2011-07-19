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


class SelectPolyData(PolyDataAlgorithm):
    """
    SelectPolyData - select portion of polygonal mesh; generate
    selection scalars
    
    Superclass: PolyDataAlgorithm
    
    SelectPolyData is a filter that selects polygonal data based on
    defining a "loop" and indicating the region inside of the loop. The
    mesh within the loop consists of complete cells (the cells are not
    cut). Alternatively, this filter can be used to generate scalars.
    These scalar values, which are a distance measure to the loop, can be
    used to clip, contour. or extract data (i.e., anything that an
    implicit function can do).
    
    The loop is defined by an array of x-y-z point coordinates.
    (Coordinates should be in the same coordinate space as the input
    polygonal data.) The loop can be concave and non-planar, but not
    self-intersecting. The input to the filter is a polygonal mesh (only
    surface primitives such as triangle strips and polygons); the output
    is either a) a portion of the original mesh laying within the
    selection loop (_generate_selection_scalars_off); or b) the same
    polygonal mesh with the addition of scalar values
    (_generate_selection_scalars_on).
    
    The algorithm works as follows. For each point coordinate in the
    loop, the closest point in the mesh is found. The result is a loop of
    closest point ids from the mesh. Then, the edges in the mesh
    connecting the closest points (and laying along the lines forming the
    loop) are found. A greedy edge tracking procedure is used as follows.
    At the current point, the mesh edge oriented in the direction of and
    whose end point is closest to the line is chosen. The edge is
    followed to the new end point, and the procedure is repeated. This
    process continues until the entire loop has been created.
    
    To determine what portion of the mesh is inside and outside of the
    loop, three options are possible. 1) the smallest connected region,
    2) the largest connected region, and 3) the connected region closest
       to a user specified point. (Set the ivar selection_mode.)
    
    Once the loop is computed as above, the generate_selection_scalars
    controls the output of the filter. If on, then scalar values are
    generated based on distance to the loop lines. Otherwise, the cells
    laying inside the selection loop are output. By default, the mesh
    lying within the loop is output; however, if inside_out is on, then
    the portion of the mesh lying outside of the loop is output.
    
    The filter can be configured to generate the unselected portions of
    the mesh as output by setting generate_unselected_output. Use the
    method get_unselected_output to access this output. (Note: this flag is
    pertinent only when generate_selection_scalars is off.)
    
    Caveats:
    
    Make sure that the points you pick are on a connected surface. If
    not, then the filter will generate an empty or partial result. Also,
    self-intersecting loops will generate unpredictable results.
    
    During processing of the data, non-triangular cells are converted to
    triangles if generate_selection_scalars is off.
    
    See Also:
    
    ImplicitSelectionLoop
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectPolyData, obj, update, **traits)
    
    generate_unselected_output = tvtk_base.false_bool_trait(help=\
        """
        Control whether a second output is generated. The second output
        contains the polygonal data that's not been selected.
        """
    )
    def _generate_unselected_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateUnselectedOutput,
                        self.generate_unselected_output_)

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. When off, the mesh within the loop is
        extracted. When on, the mesh outside the loop is extracted.
        """
    )
    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    generate_selection_scalars = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag to control behavior of the filter. If
        generate_selection_scalars is on, then the output of the filter is
        the same as the input, except that scalars are generated. If off,
        the filter outputs the cells laying inside the loop, and does not
        generate scalars.
        """
    )
    def _generate_selection_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateSelectionScalars,
                        self.generate_selection_scalars_)

    selection_mode = traits.Trait('smallest_region',
    tvtk_base.TraitRevPrefixMap({'closest_point_region': 2, 'smallest_region': 0, 'largest_region': 1}), help=\
        """
        Control how inside/outside of loop is defined.
        """
    )
    def _selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMode,
                        self.selection_mode_)

    def _get_loop(self):
        return wrap_vtk(self._vtk_obj.GetLoop())
    def _set_loop(self, arg):
        old_val = self._get_loop()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetLoop,
                        my_arg[0])
        self.trait_property_changed('loop', old_val, arg)
    loop = traits.Property(_get_loop, _set_loop, help=\
        """
        Set/Get the array of point coordinates defining the loop. There
        must be at least three points used to define a loop.
        """
    )

    def _get_selection_edges(self):
        return wrap_vtk(self._vtk_obj.GetSelectionEdges())
    selection_edges = traits.Property(_get_selection_edges, help=\
        """
        Return the (mesh) edges of the selection region.
        """
    )

    def _get_unselected_output(self):
        return wrap_vtk(self._vtk_obj.GetUnselectedOutput())
    unselected_output = traits.Property(_get_unselected_output, help=\
        """
        Return output that hasn't been selected (if
        genreate_unselected_output is enabled).
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('selection_mode', 'GetSelectionMode'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('inside_out',
    'GetInsideOut'), ('generate_unselected_output',
    'GetGenerateUnselectedOutput'), ('generate_selection_scalars',
    'GetGenerateSelectionScalars'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_selection_scalars',
    'generate_unselected_output', 'global_warning_display', 'inside_out',
    'release_data_flag', 'selection_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_selection_scalars',
            'generate_unselected_output', 'inside_out'], ['selection_mode'], []),
            title='Edit SelectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

