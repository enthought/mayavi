# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from vtk.numpy_interface import dataset_adapter as dsa

# Enthought library imports.
from traits.api import Int, Instance, Str, TraitError
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from apptools.persistence import state_pickler

# Local imports.
from mayavi.core.common import error
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.filters.optional import Optional
from mayavi.filters.mask_points import MaskPoints
from mayavi.filters.user_defined import UserDefined
from mayavi.components.actor2d import Actor2D
from mayavi.core.common import handle_children_state


################################################################################
# `Labels` class.
################################################################################
class Labels(Module):

    """
    Allows a user to label the current dataset or the current actor of
    the active module.
    """

    # Used for persistence.
    __version__ = 0

    # The object which we are labeling.
    object = Instance(PipelineBase, record=False)

    # The label format string.
    label_format = Str('', enter_set=True, auto_set=False,
                       desc='the label format string')

    # Number of points to label.
    number_of_labels = Int(25, enter_set=True, auto_set=False,
                           desc='the number of points to label')

    # The filter used for masking of the points.
    mask = Instance(MaskPoints, record=True)

    # Filter to select visible points.
    visible_points = Instance(Optional, record=True)

    # The 2D actor for the labels.
    actor = Instance(Actor2D, record=True)

    # The text property of the labels.
    property = Instance(tvtk.TextProperty, record=True)

    # The mapper for the labels.
    mapper = Instance(tvtk.LabeledDataMapper, args=(), record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # Private traits.

    # The input used for the labeling.
    input = Instance(PipelineBase)

    # The id of the object in the modulemanager only used for
    # persistence.
    object_id = Int(-2)


    ########################################
    # View related traits.

    view = View(Group(Item(name='number_of_labels'),
                      Item(name='label_format'),
                      Item(name='mapper',
                           style='custom',
                           show_label=False,
                           resizable=True),
                      Item(name='mask',
                           style='custom',
                           resizable=True,
                           show_label=False),
                      label='Labels'
                      ),
                Group(
                      Item(name='visible_points',
                           style='custom',
                           resizable=True,
                           show_label=False),
                      label='VisiblePoints'
                      ),
                Group(Item(name='property',
                           style='custom',
                           show_label=False,
                           resizable=True),
                      label='TextProperty'),
                resizable=True)

    ######################################################################
    # `object` interface.
    ######################################################################
    def __get_pure_state__(self):
        self._compute_object_id()
        d = super(Labels, self).__get_pure_state__()
        for name in ('object', 'mapper', 'input'):
            d.pop(name, None)
        # Must pickle the components.
        d['components'] = self.components
        return d

    def __set_pure_state__(self, state):
        handle_children_state(self.components, state.components)
        state_pickler.set_state(self, state)
        self.update_pipeline()

    ######################################################################
    # `Module` interface.
    ######################################################################
    def setup_pipeline(self):
        mask = MaskPoints()
        mask.filter.trait_set(generate_vertices=True, random_mode=True)
        self.mask = mask
        v = UserDefined(filter=tvtk.SelectVisiblePoints(),
                        name='VisiblePoints')
        self.visible_points = Optional(filter=v, enabled=False)
        mapper = tvtk.LabeledDataMapper()
        self.mapper = mapper
        self.actor = Actor2D(mapper=mapper)
        self.property = mapper.label_text_property
        self.property.on_trait_change(self.render)
        self.components = [self.mask, self.visible_points, self.actor]

    def update_pipeline(self):
        mm = self.module_manager
        if mm is None:
            return

        self._find_input() # Calculates self.input
        self.mask.inputs = [self.input]
        self.visible_points.inputs = [self.mask]
        self.actor.inputs = [self.visible_points]
        self._number_of_labels_changed(self.number_of_labels)
        self._label_format_changed(self.label_format)

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _find_input(self):
        mm = self.module_manager
        if self.object is None:
            if self.object_id == -1:
                self.input = mm.source
            elif self.object_id > -1:
                obj = mm.children[self.object_id]
                if hasattr(obj, 'actor'):
                    self.trait_set(object=obj, trait_change_notify=False)
                    self.input = obj.actor.inputs[0]
                else:
                    self.input = mm.source
        else:
            o = self.object
            if hasattr(o, 'module_manager'):
                # A module.
                if hasattr(o, 'actor'):
                    self.input = o.actor.inputs[0]
                else:
                    self.input = o.module_manager.source

        if self.input is None:
            if self.object_id == -2:
                self.input = mm.source
            else:
                error('No object to label!')
                return

    def _number_of_labels_changed(self, value):
        if self.input is None:
            return
        f = self.mask.filter
        inp = self.input.get_output_dataset()
        data_obj = dsa.WrapDataObject(tvtk.to_vtk(inp))
        npts = data_obj.GetNumberOfPoints()
        typ = type(f.on_ratio)
        f.on_ratio = typ(max(npts/value, 1))
        if self.mask.running:
            f.update()
            self.mask.data_changed = True

    def _label_format_changed(self, value):
        if len(value) > 0:
            self.mapper.label_format = value
            self.render()
        else:
            try:
                self.mapper.label_format = None
            except TraitError:
                self.mapper.label_format = '%g'
            self.render()

    def _object_changed(self, value):
        self.update_pipeline()

    def _compute_object_id(self):
        mm = self.module_manager
        input = self.input
        self.object_id = -2
        if input is mm.source:
            self.object_id = -1
            return
        for id, child in enumerate(mm.children):
            if child is self.object:
                self.object_id = id
                return

    def _scene_changed(self, old, new):
        self.visible_points.filter.filter.renderer = new.renderer
        super(Labels, self)._scene_changed(old, new)
