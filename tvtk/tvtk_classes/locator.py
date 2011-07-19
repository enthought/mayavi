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


class Locator(Object):
    """
    Locator - abstract base class for objects that accelerate spatial
    searches
    
    Superclass: Object
    
    Locator is an abstract base class for spatial search objects, or
    locators. The principle behind locators is that they divide 3-space
    into small pieces (or "buckets") that can be quickly found in
    response to queries like point location, line intersection, or
    object-object intersection.
    
    The purpose of this base class is to provide ivars and methods shared
    by all locators. The generate_representation() is one such interesting
    method. This method works in conjunction with LocatorFilter to
    create polygonal representations for the locator. For example, if the
    locator is an OBB tree (i.e., OBBTree.h), then the representation
    is a set of one or more oriented bounding boxes, depending upon the
    specified level.
    
    Locators typically work as follows. One or more "entities", such as
    points or cells, are inserted into the tree. These entities are
    associated with one or more buckets. Then, when performing geometric
    operations, the operations are performed first on the buckets, and
    then if the operation tests positive, then on the entities in the
    bucket. For example, during collision tests, the locators are
    collided first to identify intersecting buckets. If an intersection
    is found, more expensive operations are then carried out on the
    entities in the bucket.
    
    To obtain good performance, locators are often organized in a tree
    structure.  In such a structure, there are frequently multiple
    "levels" corresponding to different nodes in the tree. So the word
    level (in the context of the locator) can be used to specify a
    particular representation in the tree.  For example, in an octree
    (which is a tree with 8 children), level 0 is the bounding box, or
    root octant, and level 1 consists of its eight children.
    
    See Also:
    
    PointLocator CellLocator OBBTree MergePoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLocator, obj, update, **traits)
    
    automatic = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether locator depth/resolution of locator is
        computed automatically from average number of entities in bucket.
        If not set, there will be an explicit method to control the
        construction of the locator (found in the subclass).
        """
    )
    def _automatic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomatic,
                        self.automatic_)

    tolerance = traits.Trait(0.001, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify absolute tolerance (in world coordinates) for performing
        geometric operations.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    max_level = traits.Trait(8, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the maximum allowable level for the tree. If the Automatic
        ivar is off, this will be the target depth of the locator.
        Initial value is 8.
        """
    )
    def _max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLevel,
                        self.max_level)

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Build the locator from the points/cells defining this dataset.
        """
    )

    def _get_build_time(self):
        return self._vtk_obj.GetBuildTime()
    build_time = traits.Property(_get_build_time, help=\
        """
        Return the time of the last data structure build.
        """
    )

    def _get_level(self):
        return self._vtk_obj.GetLevel()
    level = traits.Property(_get_level, help=\
        """
        Get the level of the locator (determined automatically if
        Automatic is true). The value of this ivar may change each time
        the locator is built. Initial value is 8.
        """
    )

    def build_locator(self):
        """
        V.build_locator()
        C++: virtual void BuildLocator()
        Build the locator from the input dataset.
        """
        ret = self._vtk_obj.BuildLocator()
        return ret
        

    def free_search_structure(self):
        """
        V.free_search_structure()
        C++: virtual void FreeSearchStructure()
        Free the memory required for the spatial data structure.
        """
        ret = self._vtk_obj.FreeSearchStructure()
        return ret
        

    def generate_representation(self, *args):
        """
        V.generate_representation(int, PolyData)
        C++: virtual void GenerateRepresentation(int level,
            PolyData *pd)
        Method to build a representation at a particular level. Note that
        the method get_level() returns the maximum number of levels
        available for the tree. You must provide a PolyData object
        into which to place the data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GenerateRepresentation, *my_args)
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
        

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Cause the locator to rebuild itself if it or its input dataset
        has changed.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_level', 'GetMaxLevel'), ('debug',
    'GetDebug'), ('tolerance', 'GetTolerance'), ('automatic',
    'GetAutomatic'))
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'max_level',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Locator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Locator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic'], [], ['max_level', 'tolerance']),
            title='Edit Locator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Locator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

