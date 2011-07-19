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

from tvtk.tvtk_classes.extract_selection_base import ExtractSelectionBase


class ExtractSelectedFrustum(ExtractSelectionBase):
    """
    ExtractSelectedFrustum - Returns the portion of the input dataset
    that 
    
    Superclass: ExtractSelectionBase
    
    This class intersects the input data_set with a frustum and determines
    which cells and points lie within the frustum. The frustum is defined
    with a Planes containing six cutting planes. The output is a
    data_set that is either a shallow copy of the input dataset with two
    new "vtk_insidedness" attribute arrays, or a completely new
    unstructured_grid that contains only the cells and points of the input
    that are inside the frustum. The preserve_topology flag controls which
    occurs. When preserve_topology is off this filter adds a scalar array
    called OriginalCellIds that says what input cell produced each
    output cell. This is an example of a Pedigree ID which helps to trace
    back results.
    
    See Also:
    
    ExtractGeometry, AreaPicker, ExtractSelection, Selection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSelectedFrustum, obj, update, **traits)
    
    inside_out = tvtk_base.false_bool_trait(help=\
        """
        When on, extracts cells outside the frustum instead of inside.
        """
    )
    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    show_bounds = tvtk_base.false_bool_trait(help=\
        """
        When On, this returns an unstructured grid that outlines
        selection area. Off is the default.
        """
    )
    def _show_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowBounds,
                        self.show_bounds_)

    containing_cells = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets/gets the intersection test type. Only meaningful when
        field_type is Selection::POINT
        """
    )
    def _containing_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContainingCells,
                        self.containing_cells)

    field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets/gets the intersection test type.
        """
    )
    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    def _get_frustum(self):
        return wrap_vtk(self._vtk_obj.GetFrustum())
    def _set_frustum(self, arg):
        old_val = self._get_frustum()
        self._wrap_call(self._vtk_obj.SetFrustum,
                        deref_vtk(arg))
        self.trait_property_changed('frustum', old_val, arg)
    frustum = traits.Property(_get_frustum, _set_frustum, help=\
        """
        Set the selection frustum. The planes object must contain six
        planes.
        """
    )

    def _get_clip_points(self):
        return wrap_vtk(self._vtk_obj.GetClipPoints())
    clip_points = traits.Property(_get_clip_points, help=\
        """
        Return eight points that define the selection frustum. Valid if
        create Frustum was used, invalid if set_frustum was.
        """
    )

    def create_frustum(self, *args):
        """
        V.create_frustum([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: void CreateFrustum(double vertices[32])
        Given eight vertices, creates a frustum. each pt is x,y,z,1 in
        the following order near lower left, far lower left near upper
        left, far upper left near lower right, far lower right near upper
        right, far upper right
        """
        ret = self._wrap_call(self._vtk_obj.CreateFrustum, *args)
        return ret

    _updateable_traits_ = \
    (('field_type', 'GetFieldType'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('preserve_topology', 'GetPreserveTopology'), ('debug', 'GetDebug'),
    ('inside_out', 'GetInsideOut'), ('containing_cells',
    'GetContainingCells'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('show_bounds', 'GetShowBounds'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'inside_out',
    'preserve_topology', 'release_data_flag', 'show_bounds',
    'containing_cells', 'field_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSelectedFrustum, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSelectedFrustum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['inside_out', 'preserve_topology', 'show_bounds'], [],
            ['containing_cells', 'field_type']),
            title='Edit ExtractSelectedFrustum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSelectedFrustum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

