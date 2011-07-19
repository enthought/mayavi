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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class AssignAttribute(PassInputTypeAlgorithm):
    """
    AssignAttribute - Labels a field as an attribute
    
    Superclass: PassInputTypeAlgorithm
    
    AssignAttribute is use to label a field (vtk_data_array) as an
    attribute. A field name or an attribute to labeled can be specified.
    For example:
     aa->Assign("foo", DataSetAttributes::SCALARS, 
                AssignAttribute::POINT_DATA);
      tells AssignAttribute to make the array in the point data called
    "foo" the active scalars. On the other hand,
     aa->_assign(vtk_data_set_attributes::_vectors, DataSetAttributes::SCALARS, 
                AssignAttribute::POINT_DATA);
      tells AssignAttribute to make the active vectors also the active
    scalars. The same can be done more easily from Tcl by using the
    Assign() method which takes strings:
     aa Assign "foo" SCALARS POINT_DATA 
     or
     aa Assign SCALARS VECTORS POINT_DATA
    
     attribute_types: SCALARS, VECTORS, NORMALS, TCOORDS, TENSORS
     Attribute locations: POINT_DATA, CELL_DATA
     
    
    Caveats:
    
    When using Tcl, Java, Python or Visual Basic bindings, the array name
    can not be one of the  attribute_types when calling Assign() which
    takes strings as arguments. The Tcl (Java etc.) command will always
    assume the string corresponds to an attribute type when the argument
    is one of the attribute_types. In this situation, use the Assign()
    which takes enums.
    
    See Also:
    
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray RearrangeFields SplitField
    MergeFields
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssignAttribute, obj, update, **traits)
    
    def assign(self, *args):
        """
        V.assign(int, int, int)
        C++: void Assign(int inputAttributeType, int attributeType,
            int attributeLoc)
        V.assign(string, int, int)
        C++: void Assign(const char *fieldName, int attributeType,
            int attributeLoc)
        V.assign(string, string, string)
        C++: void Assign(const char *name, const char *attributeType,
            const char *attributeLoc)
        Label an attribute as another attribute.
        """
        ret = self._wrap_call(self._vtk_obj.Assign, *args)
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
            return super(AssignAttribute, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AssignAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AssignAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AssignAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

