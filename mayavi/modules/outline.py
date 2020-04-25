""" A module that displays the outline for the given data, either as a
    box, or the corners of the bounding box.
"""

# Authors: Prabhu Ramachandran <prabhu_r [at] users.sf.net>
#          KK Rai (kk.rai [at] iitb.ac.in)
#          R. Ambareesha (ambareesha [at] iitb.ac.in)
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Enum, Property, Bool, \
    DelegatesTo
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from tvtk.common import is_old_pipeline

# Local imports
from mayavi.core.module import Module
from mayavi.components.actor import Actor
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `Outline` class.
######################################################################
class Outline(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The `Outline` filter which can either be an instance of
    # `OutlineFilter` or `OutlineCornerFilter`. The `ObjectBase` class
    # is the superclass of both the `OutlineFilter` and the
    # `OutlineCornerFilter`.
    outline_filter = Property(Instance(tvtk.ObjectBase,
                                        allow_none=False), record=True)

    # Enum to set the outline type.
    outline_mode = Enum('full', 'cornered',
                        desc='if outline mode is "full" or "cornered"')

    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    # An outline source, optionally used to choose the bounds of the
    # outline.
    outline_source = Instance(tvtk.OutlineSource, ())

    bounds = DelegatesTo('outline_source',
                desc="the bounds of the outline: xmin, xmax, ymin, ymax")

    manual_bounds = Bool(
                desc="whether the bounds are automatically inferred from "
                     "the data source")

    # Create the UI for the traits.

    # The controls for the outline_filter should be enabled only when the
    # Cornered Outline Filter is selected.
    view = View(Group(
                    Group(
                        Item(name='outline_mode'),
                        Item(name='outline_filter',
                                style='custom',
                                enabled_when='outline_mode == "cornered"',
                                visible_when='outline_mode == "cornered"',
                                resizable=True,
                                show_label=False),
                    label='Outline',
                    show_labels=False),
                    Group('manual_bounds',
                            Item('bounds', enabled_when='manual_bounds'),
                            label='Bounds',
                            ),
                    Item(name='actor', style='custom'),
                    layout='tabbed',
                    show_labels=False),
                resizable=True)

    ########################################
    # Private traits.

    # We make these private traits and cache them because if we create
    # these anew each time the `outline_mode` changes, then we loose
    # any settings the user changed on the previous mode.
    _full_outline = Instance(tvtk.OutlineFilter, args=(),
                             allow_none=False)
    _cornered_outline = Instance(tvtk.OutlineCornerFilter, args=(),
                                 allow_none=False)

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        # When any trait on the outline filters change call the render
        # method.
        self._full_outline.on_trait_change(self.render)
        self._cornered_outline.on_trait_change(self.render)

        # In the new pipeline, vtkCompositeDataPipeline complains if
        # an outline filter is configured without an input connection
        self.configure_connection(self.outline_filter, self.outline_source)

        self.actor = Actor()

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        self._outline_mode_changed(self.outline_mode)
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    def render(self):
        if not is_old_pipeline():
            self.outline_filter.update()
        super(Outline, self).render()

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _outline_mode_changed(self, value):
        """This method is invoked (automatically) when the 'outline_mode'
        attribute is changed.
        """
        # Properties don't fire events, so we fire an event here so UI
        # elements and any listners can update due to the changed mode.
        new = self.outline_filter
        old = self._cornered_outline
        if new is self._full_outline:
            old = self._cornered_outline
        self.trait_property_changed('outline_filter', old, new)

        mm = self.module_manager
        if mm is None:
            return

        # Set the input of the filter.
        self._manual_bounds_changed()

        # The module has a list of outputs, but at this stage,
        # the output of the newly instantiated filter will be its only output.
        self.outputs = [self.outline_filter]

    def _get_outline_filter(self):
        if self.outline_mode == 'full':
            return self._full_outline
        else:
            return self._cornered_outline

    def _actor_changed(self, old, new):
        new.scene = self.scene
        new.inputs = [self]
        self._change_components(old, new)

    def _manual_bounds_changed(self):
        if self.manual_bounds:
            if is_old_pipeline():
                self.outline_filter.input = self.outline_source.output
            else:
                self.outline_filter.input_connection = self.outline_source.output_port
        else:
            # Set the input of the filter.
            mm = self.module_manager
            self.configure_connection(self.outline_filter, mm.source)
        self.render()

    def _bounds_changed(self):
        self.outline_filter.update()
        self.pipeline_changed = True
