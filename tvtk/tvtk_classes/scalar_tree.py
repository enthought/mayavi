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

from tvtk.tvtk_classes.object import Object


class ScalarTree(Object):
    """
    ScalarTree - organize data according to scalar values (used to
    accelerate contouring operations)
    
    Superclass: Object
    
    ScalarTree is an abstract class that defines the API to concrete
    scalar tree subclasses. A scalar tree is a data structure that
    organizes data according to its scalar value. This allows rapid
    access to data for those algorithms that access the data based on
    scalar value. For example, isocontouring operates on cells based on
    the scalar (isocontour) value.
    
    To use subclasses of this class, you must specify a dataset to
    operate on, and then specify a scalar value in the init_traversal()
    method. Then calls to get_next_cell() return cells whose scalar data
    contains the scalar value specified.
    
    See Also:
    
    SimpleScalarTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarTree, obj, update, **traits)
    
    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Build the tree from the points/cells defining this dataset.
        """
    )

    def build_tree(self):
        """
        V.build_tree()
        C++: virtual void BuildTree()
        Construct the scalar tree from the dataset provided. Checks build
        times and modified time from input and reconstructs the tree if
        necessary.
        """
        ret = self._vtk_obj.BuildTree()
        return ret
        

    def init_traversal(self, *args):
        """
        V.init_traversal(float)
        C++: virtual void InitTraversal(double scalarValue)
        Begin to traverse the cells based on a scalar value. Returned
        cells will have scalar values that span the scalar value
        specified.
        """
        ret = self._wrap_call(self._vtk_obj.InitTraversal, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Initialize locator. Frees memory and resets object as
        appropriate.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

