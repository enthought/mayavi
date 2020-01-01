"""A contour component.  This component wraps around the
tvtk.ContourFilter and provides convenient options to either
automatically generate a specified number of contours between a given
minimum and maximum value or explicitly specify the contours.  This
component may be used for any input data.  The component also provides
a convenient option to create "filled contours".

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, List, Tuple, Bool, Range, \
                                 Float, Property
from tvtk.api import tvtk

# Local imports.
from mayavi.core.module_manager import DataSetHelper
from mayavi.core.component import Component
from mayavi.core.common import error
from mayavi.components.common \
     import get_module_source, convert_to_poly_data


######################################################################
# `Contour` class.
######################################################################
class Contour(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The contour filter being currently used.
    contour_filter = Property

    # Specify if filled contours are generated.
    filled_contours = Bool(
        False, desc='if filled contours are to be generated'
    )

    # Specify if contours are generated explicitly or automatically.
    auto_contours = Bool(
        False,
        desc='if contours are given explicitly or automatically computed'
    )

    # Number of contours, used when `auto_contours` are chosen.
    number_of_contours = Range(1, 100000, enter_set=True, auto_set=False,
                               desc='number of contours to generate')

    # Minimum contour, this is the starting value when `auto_contours`
    # is turned on.
    minimum_contour = Range(value=0.0,
                            low='_data_min',
                            high='_data_max',
                            enter_set=True,
                            auto_set=False,
                            desc='the starting contour value')

    # Maximum contour, this is the last contour when `auto_contours`
    # is turned on.
    maximum_contour = Range(value=0.0,
                            low='_data_min',
                            high='_data_max',
                            enter_set=True,
                            auto_set=False,
                            desc='the ending contour value')

    # The explicit contours to create.  These specify the contours
    # explicitly and are used when `auto_contours` is turned off.  The
    # traits of the items in the list are dynamically generated based
    # on input data.
    contours = List(Range(value='_default_contour',
                          low='_data_min',
                          high='_data_max',
                          enter_set=True,
                          auto_set=False,
                          ),
                    rows=3,
                    desc='explicitly the contours to be generated')

    # Specify if the filled contour option should be shown in the view
    # or not.  This is useful in situations like the iso_surface
    # module where it does not make sense to use filled contours at
    # all.
    show_filled_contours = Bool(True)

    # Specify if the lower and upper bound for the data is to be
    # automatically reset or not.
    auto_update_range = Bool(
        True,
        desc='if the contour range is updated automatically'
    )

    ########################################
    # The component's view is picked up from ui/contour.py

    ########################################
    # Private traits.

    _current_range = Tuple

    # The minimum value of the input data.  Set to a very large negative value
    # to avoid errors prior to the object being added to the mayavi
    # tree.
    _data_min = Float(-1e20, enter_set=True, auto_set=False)

    # The maximum value of the input data.  Set to a very large value
    # to avoid errors prior to the object being added to the mayavi
    # tree.
    _data_max = Float(1e20, enter_set=True, auto_set=False)

    # The default value of the contour to add, this property is computed
    # from the _data_min and _data_max traits and used when the user
    # adds a contour manually from the UI when auto_contours are turned
    # off.
    _default_contour = Property(Float)

    # The contour filter.
    _cont_filt = Instance(tvtk.ContourFilter, args=())

    # The filled contour filter.  This filter generates the filled contours.
    _fill_cont_filt = Instance(tvtk.BandedPolyDataContourFilter, args=(),
                               kw={'clipping': 1, 'scalar_mode': 'value'})

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(Contour, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('_data_min', '_data_max', '_default_contour'):
            d.pop(name, None)

        return d

    ######################################################################
    # `Component` interface
    ######################################################################
    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if not self._has_input():
            return
        cf = self._set_contour_input()
        first = False
        if len(self._current_range) == 0:
            first = True
        self._update_ranges()
        # If this is the first time, create a default contour
        if first:
            cr = self._current_range
            self.contours = [(cr[0] + cr[1])/2]
            self.minimum_contour = cr[0]
            self.maximum_contour = cr[1]
        self.outputs = [cf]

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self._update_ranges()
        # Propagage the data changed event.
        self.data_changed = True

    def has_output_port(self):
        """ The contour filter has an output port."""
        return True

    def get_output_object(self):
        """ Returns the output port."""
        return self.contour_filter.output_port

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _contours_items_changed(self, list_event):
        if self.auto_contours or not self._has_input():
            return
        cf = self.contour_filter
        added, removed, index = (list_event.added, list_event.removed,
                                 list_event.index)
        if len(added) == len(removed):
            cf.set_value(index, added[0])
            cf.update()
            self.data_changed = True
        else:
            self._contours_changed(self.contours)

    def _contours_changed(self, values):
        if self.auto_contours or not self._has_input():
            return
        cf = self.contour_filter
        cf.number_of_contours = len(values)
        for i, x in enumerate(values):
            cf.set_value(i, x)
        cf.update()
        self.data_changed = True

    def _update_ranges(self):
        # Here we get the module's source since the input of this
        # component may not in general represent the entire object.
        if not self.auto_update_range:
            return
        src = get_module_source(self.inputs[0])
        dsh = DataSetHelper(src.outputs[0])
        name, rng = dsh.get_range('scalars', 'point')
        if name is None:
            error('Cannot contour: No scalars in input data!')
            rng = (0.0, 1.0)
        if rng != self._current_range:
            self.trait_set(_data_min=rng[0], _data_max=rng[1],
                           trait_change_notify=False)
            self._clip_contours(rng)
            self._current_range = rng

    def _minimum_contour_changed(self, value):
        self._do_auto_contours()

    def _maximum_contour_changed(self, value):
        self._do_auto_contours()

    def _number_of_contours_changed(self, value):
        self._do_auto_contours()

    def _auto_contours_changed(self, value):
        if value:
            self._do_auto_contours()
        else:
            self._contours_changed(self.contours)

    def _auto_update_range_changed(self, value):
        if value:
            rng = self._data_min, self._data_max
            self._current_range = rng
            self._update_ranges()
            self.trait_property_changed('_data_min', rng[0],
                                        self._data_min)
            self.trait_property_changed('_data_max', rng[1],
                                        self._data_max)

    def _do_auto_contours(self):
        if not self._has_input():
            return
        if self.auto_contours:
            minc, maxc = self.minimum_contour, self.maximum_contour
            self.contour_filter.generate_values(self.number_of_contours,
                                                min(minc, maxc),
                                                max(minc, maxc))
            self.data_changed = True

    def _filled_contours_changed(self, val):
        if not self._has_input():
            return
        cf = self._set_contour_input()
        # This will trigger a change.
        self._auto_contours_changed(self.auto_contours)
        self.outputs = [cf]

    def _get_contour_filter(self):
        if self.filled_contours:
            return self._fill_cont_filt
        else:
            return self._cont_filt

    def _set_contour_input(self):
        """Sets the input to the appropriate contour filter and
        returns the currently used contour filter.
        """
        inp = self.inputs[0].outputs[0]
        cf = self.contour_filter
        if self.filled_contours:
            inp = convert_to_poly_data(inp)
            self.configure_input(cf, inp)
        else:
            self.configure_input(cf, inp)
        cf.update()
        return cf

    def _has_input(self):
        """Returns if this component has a valid input."""
        if (len(self.inputs) > 0) and \
           (len(self.inputs[0].outputs) > 0):
            return True
        else:
            return False

    def _clip_contours(self, rng):
        """Clips the contour related values when the data range has
        changed.  The new range is given as the argument.
        """
        ctr = []
        dmin, dmax = rng
        ctr = [min(max(x, dmin), dmax) for x in self.contours]
        if self.auto_contours or ctr != self.contours:
            self.contours = ctr
            self.trait_set(minimum_contour=self._data_min,
                           maximum_contour=self._data_max,
                           trait_change_notify=False)
            self._do_auto_contours()

    def _get__default_contour(self):
        return (self._data_min + self._data_max)*0.5
