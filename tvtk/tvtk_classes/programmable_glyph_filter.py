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


class ProgrammableGlyphFilter(PolyDataAlgorithm):
    """
    ProgrammableGlyphFilter - control the generation and placement of
    glyphs at input points
    
    Superclass: PolyDataAlgorithm
    
    ProgrammableGlyphFilter is a filter that allows you to place a
    glyph at each input point in the dataset. In addition, the filter is
    programmable which means the user has control over the generation of
    the glyph. The glyphs can be controlled via the point data attributes
    (e.g., scalars, vectors, etc.) or any other information in the input
    dataset.
    
    This is the way the filter works. You must define an input dataset
    which at a minimum contains points with associated attribute values.
    Also, the Source instance variable must be set which is of type
    PolyData. Then, for each point in the input, the point_id is set to
    the current point id, and a user-defined function is called (i.e.,
    glyph_method). In this method you can manipulate the Source data
    (including changing to a different Source object). After the
    glyph_method is called, ProgrammableGlyphFilter will invoke an
    Update() on its Source object, and then copy its data to the output
    of the ProgrammableGlyphFilter. Therefore the output of this
    filter is of type PolyData.
    
    Another option to this filter is the way you color the glyphs. You
    can use the scalar data from the input or the source. The instance
    variable color_mode controls this behavior.
    
    Caveats:
    
    This filter operates on point data attributes. If you want to use
    cell data attributes, use a filter like CellCenters to generate
    points at the centers of cells, and then use these points.
    
    Note that the data attributes (cell and point) are passed to the
    output of this filter from the Source object. This works well as long
    as you are not changing the class of the Source object during
    execution. However, if the class of the Source object changes, then
    the potential exists that the data attributes might change during
    execution (e.g., scalars available from one source and not the next),
    possibly fouling up the copying of data attributes to the output. In
    this case, you may have to manually set the output's copy flags
    (e.g., copy_scalars_on/_off(), copy_vectors_on/_off(), etc.) to control
    what's being copied.
    
    See Also:
    
    Glyph3D TensorGlyph CellCenters
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableGlyphFilter, obj, update, **traits)
    
    color_mode = traits.Trait('color_by_input',
    tvtk_base.TraitRevPrefixMap({'color_by_input': 0, 'color_by_source': 1}), help=\
        """
        Either color by the input or source scalar data.
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Set/Get the source to use for this glyph. Note: you can change
        the source during execution of this filter.
        """
    )

    def _get_point(self):
        return self._vtk_obj.GetPoint()
    point = traits.Property(_get_point, help=\
        """
        
        """
    )

    def _get_point_data(self):
        return wrap_vtk(self._vtk_obj.GetPointData())
    point_data = traits.Property(_get_point_data, help=\
        """
        Get the set of point data attributes for the input. A convenience
        to the programmer to be used in the glyph_method(). Only valid
        during the Execute() method of this filter.
        """
    )

    def _get_point_id(self):
        return self._vtk_obj.GetPointId()
    point_id = traits.Property(_get_point_id, help=\
        """
        Get the current point id during processing. Value only valid
        during the Execute() method of this filter. (Meant to be called
        by the glyph_method().)
        """
    )

    def set_glyph_method(self, *args):
        """
        V.set_glyph_method(function)
        C++: void SetGlyphMethod(void (*f)(void *) , void *arg)
        Specify function to be called for each input point.
        """
        ret = self._wrap_call(self._vtk_obj.SetGlyphMethod, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('color_mode',
    'GetColorMode'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'color_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProgrammableGlyphFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['color_mode'], []),
            title='Edit ProgrammableGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

