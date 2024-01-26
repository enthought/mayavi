"""A simple filter that thresholds on input data.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2010, Enthought, Inc.
# License: BSD Style.

import numpy as np

# Enthought library imports.
from traits.api import Instance, Range, Float, Bool, \
                                 Property, Enum
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from tvtk.common import vtk_major_version, vtk_minor_version

# Local imports
from mayavi.core.filter import Filter
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.utils import DataSetHelper


######################################################################
# `Threshold` class.
######################################################################
class Threshold(Filter):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The threshold filter used.
    threshold_filter = Property(Instance(tvtk.Object, allow_none=False), record=True)

    # The filter type to use, specifies if the cells or the points are
    # cells filtered via a threshold.
    filter_type = Enum('cells', 'points',
                       desc='if thresholding is done on cells or points')

    # Lower threshold (this is a dynamic trait that is changed when
    # input data changes).
    lower_threshold = Range(value=-1.0e20,
                            low='_data_min',
                            high='_data_max',
                            enter_set=True,
                            auto_set=False,
                            desc='the lower threshold of the filter')

    # Upper threshold (this is a dynamic trait that is changed when
    # input data changes).
    upper_threshold = Range(value=1.0e20,
                            low='_data_min',
                            high='_data_max',
                            enter_set=True,
                            auto_set=False,
                            desc='the upper threshold of the filter')

    # Automatically reset the lower threshold when the upstream data
    # changes.
    auto_reset_lower = Bool(True, desc='if the lower threshold is '
                            'automatically reset when upstream '
                            'data changes')

    # Automatically reset the upper threshold when the upstream data
    # changes.
    auto_reset_upper = Bool(True, desc='if the upper threshold is '
                            'automatically reset when upstream '
                            'data changes')

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data',
                                         'unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])

    # Our view.
    view = View(Group(Group(Item(name='filter_type'),
                            Item(name='lower_threshold'),
                            Item(name='auto_reset_lower'),
                            Item(name='upper_threshold'),
                            Item(name='auto_reset_upper')),
                      Item(name='_'),
                      Group(Item(name='threshold_filter',
                                 show_label=False,
                                 visible_when='object.filter_type == "cells"',
                                 style='custom', resizable=True)),
                      ),
                resizable=True
                )

    ########################################
    # Private traits.

    # These traits are used to set the limits for the thresholding.
    # They store the minimum and maximum values of the input data.
    _data_min = Float(-1e20)
    _data_max = Float(1e20)

    # The threshold filter for cell based filtering
    _threshold = Instance(tvtk.Threshold, args=(), allow_none=False)

    # The threshold filter for points based filtering.
    _threshold_points = Instance(tvtk.ThresholdPoints, args=(), allow_none=False)

    # Internal data to
    _first = Bool(True)

    ######################################################################
    # `object` interface.
    ######################################################################
    def __get_pure_state__(self):
        d = super(Threshold, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('_first', '_data_min', '_data_max'):
            d.pop(name, None)

        return d

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def setup_pipeline(self):
        attrs = ['all_scalars', 'attribute_mode',
                 'component_mode', 'selected_component']
        self._threshold.on_trait_change(self._threshold_filter_edited,
                                        attrs)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if len(self.inputs) == 0:
            return

        # By default we set the input to the first output of the first
        # input.
        fil = self.threshold_filter
        self.configure_connection(fil, self.inputs[0])
        self._update_ranges()
        self._set_outputs([self.threshold_filter])

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        if len(self.inputs) == 0:
            return

        self._update_ranges()

        # Propagate the data_changed event.
        self.data_changed = True

    ######################################################################
    # Non-public interface
    ######################################################################
    def _lower_threshold_changed(self, new_value):
        fil = self.threshold_filter
        if (vtk_major_version, vtk_minor_version) >= (9, 1):
            fil.lower_threshold = new_value
        else:
            fil.threshold_between(new_value, self.upper_threshold)
        fil.update()
        self.data_changed = True

    def _upper_threshold_changed(self, new_value):
        fil = self.threshold_filter
        if (vtk_major_version, vtk_minor_version) >= (9, 1):
            fil.upper_threshold = new_value
        else:
            fil.threshold_between(self.lower_threshold, new_value)
        fil.update()
        self.data_changed = True

    def _update_ranges(self):
        """Updates the ranges of the input.
        """
        data_range = self._get_data_range()
        if len(data_range) == 0:
            return

        dr = data_range
        if self._first:
            self._data_min, self._data_max = dr
            self.trait_set(lower_threshold=dr[0], trait_change_notify=False)
            self.upper_threshold = dr[1]
            self._first = False
            return

        # Decide whether to change 'lower' or 'upper' first, to avoid
        # ending up with inconsistent bounds (max < min) in the lower_threshold
        # and upper_threshold Range traits.
        if dr[0] <= self._data_min:
            # Safe to change lower bound first: intermediate range is [dr[0],
            # self._data_max], and dr[0] <= self._data_min <= self._data_max.
            change_lower_first = True
        else:
            # Safe to change upper bound first: intermediate range is [self._data_min, dr[1]],
            # and self._data_min < dr[0] <= dr[1].
            change_lower_first = False

        if change_lower_first:
            if self.auto_reset_lower:
                self._data_min = dr[0]
                notify = not self.auto_reset_upper
                self.trait_set(lower_threshold = dr[0],
                               trait_change_notify=notify)
            if self.auto_reset_upper:
                self._data_max = dr[1]
                self.upper_threshold = dr[1]
        else:
            if self.auto_reset_upper:
                self._data_max = dr[1]
                notify = not self.auto_reset_lower
                self.trait_set(upper_threshold = dr[1],
                         trait_change_notify=notify)
            if self.auto_reset_lower:
                self._data_min = dr[0]
                self.lower_threshold = dr[0]

    def _get_data_range(self):
        """Returns the range of the input scalar data."""
        dsh = DataSetHelper(self.inputs[0].outputs[0])
        name, rng = dsh.get_range('scalars', 'point')
        if name is not None:
            return rng
        else:
            name, rng = dsh.get_range('scalars', 'cell')
            if name is None:
                return []
            else:
                return rng

    def _auto_reset_lower_changed(self, value):
        if len(self.inputs) == 0:
            return
        if value:
            dr = self._get_data_range()
            self._data_min = dr[0]
            self.lower_threshold = dr[0]

    def _auto_reset_upper_changed(self, value):
        if len(self.inputs) == 0:
            return
        if value:
            dr = self._get_data_range()
            self._data_max = dr[1]
            self.upper_threshold = dr[1]

    def _get_threshold_filter(self):
        if self.filter_type == 'cells':
            return self._threshold
        else:
            return self._threshold_points

    def _filter_type_changed(self, value):
        if value == 'cells':
            old = self._threshold_points
            new = self._threshold
        else:
            old = self._threshold
            new = self._threshold_points
        self.trait_property_changed('threshold_filter', old, new)

    def _threshold_filter_changed(self, old, new):
        if len(self.inputs) == 0:
            return
        fil = new
        self.configure_connection(fil, self.inputs[0].outputs[0])
        if (vtk_major_version, vtk_minor_version) >= (9, 1):
            fil.lower_threshold = self.lower_threshold
            fil.upper_threshold = self.upper_threshold
        else:
            fil.threshold_between(self.lower_threshold,
                                  self.upper_threshold)
        fil.update()
        self._set_outputs([fil])

    def _threshold_filter_edited(self):
        self.threshold_filter.update()
        self.data_changed = True
