"""A grid plane component.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Enum, Int, Range
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from apptools.persistence import state_pickler

# Local imports.
from mayavi.core.component import Component
from mayavi.core.common import error


def _get_extent(inp):
    """Get the extents from the given input.
    """
    d = inp.dimensions
    return [0, d[0]-1, 0, d[1]-1, 0, d[2]-1]


######################################################################
# `GridPlane` class.
######################################################################
class GridPlane(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The TVTK object that extracts the grid plane.  This is created
    # dynamically based on the input data type.
    plane = Instance(tvtk.Object)

    # The axis which is normal to the plane chosen.
    axis = Enum('x', 'y', 'z',
                desc='specifies the axis normal to the grid plane')

    # The position of the grid plane.
    position = Range(value=0, low='_low', high='_high',
                     enter_set=True, auto_set=False)

    ########################################
    # Private traits.

    # Determines the lower limit of the position trait and is always 0.
    _low = Int(0)

    # Determines the upper limit of the position trait.  The value is
    # dynamically set depending on the input data and state of the
    # axis trait.  The default is some large value to avoid errors in
    # cases where the user may set the position before adding the
    # object to the mayavi tree.
    _high = Int(10000)

    ########################################
    # View related traits.

    # The View for this object.
    view = View(Group(Item(name='axis'),
                      Item(name='position', enabled_when='_high > 0'))
                )

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(GridPlane, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('plane', '_low', '_high'):
            d.pop(name, None)

        return d

    def __set_pure_state__(self, state):
        state_pickler.set_state(self, state)
        self._position_changed(self.position)

    ######################################################################
    # `Component` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* its tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.
        """
        pass

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if len(self.inputs) == 0:
            return
        input = self.inputs[0].get_output_dataset()
        plane = None
        if input.is_a('vtkStructuredGrid'):
            plane = tvtk.StructuredGridGeometryFilter()
        elif input.is_a('vtkStructuredPoints') or input.is_a('vtkImageData'):
            plane = tvtk.ImageDataGeometryFilter()
        elif input.is_a('vtkRectilinearGrid'):
            plane = tvtk.RectilinearGridGeometryFilter()
        else:
            msg = "The GridPlane component does not support the %s dataset."\
                  % (input.class_name)
            error(msg)
            raise TypeError(msg)

        self.configure_connection(plane, self.inputs[0])
        self.plane = plane
        self.plane.update()
        self.outputs = [plane]
        self._update_limits()
        self._update_extents()
        # If the data is 2D make sure that we default to the
        # appropriate axis.
        extents = list(_get_extent(input))
        diff = [y-x for x, y in zip(extents[::2], extents[1::2])]
        if diff.count(0) > 0:
            self.axis = ['x', 'y', 'z'][diff.index(0)]

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self._update_limits()
        self._update_extents()
        # Propagate the data_changed event.
        self.data_changed = True

    def has_output_port(self):
        """ The filter has an output port."""
        return True

    def get_output_object(self):
        """ Returns the output port."""
        return self.plane.output_port

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _get_axis_index(self):
        return {'x': 0, 'y': 1, 'z': 2}[self.axis]

    def _update_extents(self):
        inp = self.plane.input
        extents = list(_get_extent(inp))
        pos = self.position
        axis = self._get_axis_index()
        extents[2*axis] = pos
        extents[2*axis+1] = pos
        try:
            self.plane.set_extent(extents)
        except AttributeError:
            self.plane.extent = extents

    def _update_limits(self):
        extents = _get_extent(self.plane.input)
        axis = self._get_axis_index()
        pos = min(self.position, extents[2*axis+1])
        self._high = extents[2*axis+1]
        return pos

    def _axis_changed(self, val):
        if len(self.inputs) == 0:
            return
        pos = self._update_limits()
        if self.position == pos:
            self._update_extents()
            self.data_changed = True
        else:
            self.position = pos

    def _position_changed(self, val):
        if len(self.inputs) == 0:
            return
        self._update_extents()
        self.data_changed = True
