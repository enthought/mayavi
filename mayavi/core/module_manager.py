"""Manages a collection of module objects.  Also manages the lookup
tables.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2018,  Enthought, Inc.
# License: BSD Style.

import numpy

import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

# Enthought library imports.
from traits.api import List, Instance, Trait, TraitPrefixList, \
                                 HasTraits, Str
from apptools.persistence.state_pickler import set_state

# Local imports
from tvtk.api import tvtk
from mayavi.core.base import Base
from mayavi.core.module import Module
from mayavi.core.lut_manager import LUTManager
from mayavi.core.common import handle_children_state, exception
from mayavi.core.pipeline_info import PipelineInfo


def get_new_output(input, update=True):
    if update and hasattr(input, 'update'):
        input.update()
    if input.is_a('vtkDataObject'):
        return input
    else:
        if input.output is not None:
            result = input.output
        else:
            obj = input.get_output_information(0).get(
                vtk.vtkDataSet.DATA_OBJECT()
            )
            result = obj
        return result


class DataSetHelper(object):
    def __init__(self, input):
        self.dataset = dsa.WrapDataObject(
            tvtk.to_vtk(get_new_output(input, update=True))
        )
        self._composite = isinstance(self.dataset, dsa.CompositeDataSet)
        self._scalars = None
        self._vectors = None

    def _find_attr_name_for_composite_data(self, attr, mode):
        prop = 'PointData' if mode == 'point' else 'CellData'
        for obj in self.dataset:
            da = getattr(obj, prop)
            if attr == 'scalars':
                s = da.GetScalars()
            else:
                s = da.GetVectors()
            if s is not None:
                return s.GetName()

    def _get_attr(self, da, attr, mode):
        if self._composite:
            name = self._find_attr_name_for_composite_data(attr, mode)
            return name,  da[name]
        else:
            if attr == 'scalars':
                s = da.GetScalars()
            else:
                s = da.GetVectors()
            if s is not None:
                name = s.GetName()
                if name is None or len(name) == 0:
                    s.SetName(mode + '_' + attr)
                return name, da[name]

    def get_range(self, attr='scalars', mode='point'):
        assert mode in ('point', 'cell')
        assert attr in ('scalars', 'vectors')
        dataset = self.dataset
        da = dataset.PointData if mode == 'point' else dataset.CellData
        x = self._get_attr(da, attr, mode)
        if x is None:
            return None, [0.0, 1.0]
        name, x = x
        if self._composite:
            # Don't bother with Nans for composite data for now.
            if isinstance(x, dsa.VTKNoneArray):
                res = [0.0, 1.0]
            elif attr == 'scalars':
                res = [algs.min(x), algs.max(x)]
            else:
                max_norm = numpy.sqrt(algs.max(algs.sum(x*x, axis=1)))
                res = [0.0, max_norm]
        else:
            has_nan = numpy.isnan(x).any()
            if attr == 'scalars':
                if has_nan:
                    res = [float(numpy.nanmin(x)), float(numpy.nanmax(x))]
                else:
                    res = list(x.GetRange())
            else:
                if has_nan:
                    d_mag = numpy.sqrt((x*x).sum(axis=1))
                    res = [float(numpy.nanmin(d_mag)),
                           float(numpy.nanmax(d_mag))]
                else:
                    res = [0.0, x.GetMaxNorm()]
        return name, res


######################################################################
# `DataAttributes` class.
######################################################################
class DataAttributes(HasTraits):
    """A simple helper class used to store some attributes of an input
    data object."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The name of the input data array.
    name = Str('')

    # The range of the data array.
    range = List

    def _get_np_arr(self, arr):
        data_array = arr.to_array()
        data_has_nan = numpy.isnan(data_array).any()
        return data_array, data_has_nan

    def compute_scalar(self, helper, mode='point'):
        """Compute the scalar range from given VTK data array.  Mode
        can be 'point' or 'cell'."""
        name, rng = helper.get_range(attr='scalars', mode=mode)
        if name:
            self.name = name
            self.range = rng

    def compute_vector(self, helper, mode='point'):
        """Compute the vector range from given VTK data array.  Mode
        can be 'point' or 'cell'."""
        name, rng = helper.get_range(attr='vectors', mode=mode)
        if name:
            self.name = name
            self.range = rng

    def config_lut(self, lut_mgr):
        """Set the attributes of the LUTManager."""
        rng = [0.0, 1.0]
        if len(self.range) > 0:
            rng = self.range

        lut_mgr.default_data_range = list(rng)
        lut_mgr.default_data_name = self.name


# Constant for a ModuleManager class and it's View.
LUT_DATA_MODE_TYPES = ['auto', 'point data', 'cell data']


######################################################################
# `ModuleManager` class.
######################################################################
class ModuleManager(Base):
    """ The module manager node (represented as 'Colors and Legends').
    """

    # The source object this is connected to.
    source = Instance(Base)

    # The modules contained by this manager.
    children = List(Module, record=True)

    # The data type to use for the LUTs.  Changing this setting will
    # change the data range and name of the lookup table/legend bar.
    # If set to 'auto', it automatically looks for cell and point data
    # with point data being preferred over cell data and chooses the
    # one available.  If set to 'point data' it uses the input point
    # data for the LUT and if set to 'cell data' it uses the input
    # cell data.
    lut_data_mode = Trait('auto',
                          TraitPrefixList(LUT_DATA_MODE_TYPES),
                          desc='specify the data type used by the lookup tables',
                          )

    # The scalar lookup table manager.
    scalar_lut_manager = Instance(LUTManager, args=(), record=True)

    # The vector lookup table manager.
    vector_lut_manager = Instance(LUTManager, args=(), record=True)

    # The name of the ModuleManager.
    name = Str('Colors and legends')

    # The icon
    icon = Str('modulemanager.ico')

    # The human-readable type for this object
    type = Str(' colors and legends')

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['any'])

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'])

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(ModuleManager, self).__get_pure_state__()
        # Source is setup dynamically, don't pickle it.
        d.pop('source', None)
        return d

    def __set_pure_state__(self, state):
        # Do everything but our kids.
        set_state(self, state, ignore=['children'])
        # Setup children.
        handle_children_state(self.children, state.children)
        # Now setup the children.
        set_state(self, state, first=['children'], ignore=['*'])
        self.update()

    ######################################################################
    # `ModuleManager` interface
    ######################################################################
    def update(self):
        """Update any internal data.

        This is invoked when the source changes or when there are
        pipeline/data changes upstream.
        """
        if len(self.source.outputs) == 0:
            return

        input = self.source.outputs[0]
        helper = DataSetHelper(input)

        self._setup_scalar_data(helper)
        self._setup_vector_data(helper)

    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.
        """
        # Do nothing if we are already running.
        if self.running:
            return

        # Setup event handlers.
        self._setup_event_handlers()

        # Start all our children.
        for obj in self.children:
            obj.start()
        for obj in (self.scalar_lut_manager, self.vector_lut_manager):
            obj.start()

        # Call parent method to set the running state.
        super(ModuleManager, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Teardown event handlers.
        self._teardown_event_handlers()

        # Stop all our children.
        for obj in self.children:
            obj.stop()
        for obj in (self.scalar_lut_manager, self.vector_lut_manager):
            obj.stop()

        # Call parent method to set the running state.
        super(ModuleManager, self).stop()

    def add_child(self, child):
        """This method intelligently adds a child to this object in
        the MayaVi pipeline.
        """
        if isinstance(child, Module):
            self.children.append(child)
        else:
            # Ask our source to deal with it.
            self.source.add_child(child)

    def remove_child(self, child):
        """Remove specified child from our children.
        """
        self.children.remove(child)

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_can_add(self, node, add_object):
        """ Returns whether a given object is droppable on the node.
        """
        try:
            if issubclass(add_object, Module):
                return True
        except TypeError:
            if isinstance(add_object, Module):
                return True
        return False

    def tno_drop_object(self, node, dropped_object):
        """ Returns a droppable version of a specified object.
        """
        if isinstance(dropped_object, Module):
            return dropped_object

    ######################################################################
    # Non-public interface
    ######################################################################
    def _children_changed(self, old, new):
        self._handle_children(old, new)

    def _children_items_changed(self, list_event):
        self._handle_children(list_event.removed, list_event.added)

    def _handle_children(self, removed, added):
        # Stop all the old children.
        for obj in removed:
            obj.stop()
        # Setup and start the new ones.
        for obj in added:
            obj.trait_set(module_manager=self, scene=self.scene, parent=self)
            if self.running:
                # It makes sense to start children only if we are running.
                # If not, the children will be started when we start.
                try:
                    obj.start()
                except:
                    exception()

    def _source_changed(self):
        self.output_info.copy_traits(self.source.output_info)
        self.update()

    def _setup_event_handlers(self):
        src = self.source
        src.on_trait_event(self.update, 'pipeline_changed')
        src.on_trait_event(self.update, 'data_changed')

    def _teardown_event_handlers(self):
        src = self.source
        src.on_trait_event(self.update, 'pipeline_changed', remove=True)
        src.on_trait_event(self.update, 'data_changed', remove=True)

    def _scene_changed(self, value):
        for obj in self.children:
            obj.scene = value
        for obj in (self.scalar_lut_manager, self.vector_lut_manager):
            obj.scene = value

    def _lut_data_mode_changed(self, value):
        self.update()

    def _setup_scalar_data(self, helper):
        """Computes the scalar range and an appropriate name for the
        lookup table."""
        data_attr = DataAttributes(name='No scalars')
        point_data_attr = DataAttributes(name='No scalars')
        point_data_attr.compute_scalar(helper, 'point')
        cell_data_attr = DataAttributes(name='No scalars')
        cell_data_attr.compute_scalar(helper, 'cell')

        if self.lut_data_mode == 'auto':
            if len(point_data_attr.range) > 0:
                data_attr.copy_traits(point_data_attr)
            elif len(cell_data_attr.range) > 0:
                data_attr.copy_traits(cell_data_attr)
        elif self.lut_data_mode == 'point data':
            data_attr.copy_traits(point_data_attr)
        elif self.lut_data_mode == 'cell data':
            data_attr.copy_traits(cell_data_attr)

        data_attr.config_lut(self.scalar_lut_manager)

    def _setup_vector_data(self, helper):
        data_attr = DataAttributes(name='No vectors')
        point_data_attr = DataAttributes(name='No vectors')
        point_data_attr.compute_vector(helper, 'point')
        cell_data_attr = DataAttributes(name='No vectors')
        cell_data_attr.compute_vector(helper, 'cell')

        if self.lut_data_mode == 'auto':
            if len(point_data_attr.range) > 0:
                data_attr.copy_traits(point_data_attr)
            elif len(cell_data_attr.range) > 0:
                data_attr.copy_traits(cell_data_attr)
        elif self.lut_data_mode == 'point data':
            data_attr.copy_traits(point_data_attr)
        elif self.lut_data_mode == 'cell data':
            data_attr.copy_traits(cell_data_attr)

        data_attr.config_lut(self.vector_lut_manager)

    def _visible_changed(self, value):
        for c in self.children:
            c.visible = value
        self.scalar_lut_manager.visible = value
        self.vector_lut_manager.visible = value

        super(ModuleManager, self)._visible_changed(value)

    def _menu_helper_default(self):
        from mayavi.core.traits_menu import ModuleMenuHelper
        return ModuleMenuHelper(object=self)
