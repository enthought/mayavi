"""
Filter factories and their associated functions for mlab.

Module functions meant to be applied to a data source object should take
only one positional argument, the data object, to be easily used in
helper functions.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Prabhu Ramachandran
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

from traits.api import Instance, CFloat, CInt, CArray, Trait, \
            Enum, Property, Any, String
from tvtk.common import camel2enthought
from tvtk.api import tvtk
import mayavi.filters.api as filters
from mayavi.core.registry import registry
from .pipe_base import PipeFactory, make_function

# This the list is dynamically populated further down below at the end.
__all__ = ['tube', 'warp_scalar', 'threshold', 'elevation_filter',
            'set_active_attribute', 'user_defined'
          ]

def new_class(name, bases, dict_):
    try:
        import new
        return new.classobj(name, bases, dict_)
    except ImportError:
        return type(name, bases, dict_)

##############################################################################
class TubeFactory(PipeFactory):
    """Applies the Tube mayavi filter to the given VTK object."""

    _target = Instance(filters.Tube, ())

    tube_sides = CInt(6, adapts='filter.number_of_sides',
                        desc="""number of sides of the tubes used to
                        represent the lines.""")

    tube_radius = CFloat(0.05, adapts='filter.radius',
                        desc="""radius of the tubes used to represent the
                        lines.""")


tube = make_function(TubeFactory)


##############################################################################
class WarpScalarFactory(PipeFactory):
    """Applies the WarpScalar mayavi filter to the given VTK object."""

    _target = Instance(filters.WarpScalar, ())

    warp_scale = CFloat(1.0, adapts="filter.scale_factor",
                            help="scale of the warp scalar")

warp_scalar = make_function(WarpScalarFactory)


##############################################################################
class ThresholdFactory(PipeFactory):
    """Applies the Threshold mayavi filter to the given VTK object."""

    _target = Instance(filters.Threshold, ())

    filter_type = Enum('cells', 'points', adapts='filter_type',
                    help="If threshold is put on cells or points")

    low = Trait(None, None, CFloat, help="The lower threshold")

    def _low_changed(self):
        if self.low is None:
            pass
        else:
            self._target.lower_threshold = self.low

    up = Trait(None, None, CFloat, help="The upper threshold")

    def _up_changed(self):
        if self.up is None:
            pass
        else:
            self._target.upper_threshold = self.up


threshold = make_function(ThresholdFactory)


##############################################################################
class ElevationFilterFactory(PipeFactory):
    """Applies the Elevation Filter mayavi filter to the given VTK object."""

    high_point = CArray(default=[0, 0, 1], shape=(3,),
                    adapts="filter.high_point",
                    help="The end point of the projection line")

    low_point = CArray(default=[0, 0, 0], shape=(3,),
                    adapts="filter.low_point",
                    help="The start point of the projection line")

    _target = Instance(filters.ElevationFilter, ())

elevation_filter = make_function(ElevationFilterFactory)


##############################################################################
class SetActiveAttributeFactory(PipeFactory):
    """ Applies the SetActiveAttribute Filter mayavi filter to the given
        VTK object.
    """

    point_scalars = String(
                    adapts="point_scalars_name",
                    help="The name of the active point scalars")

    point_vectors = String(
                    adapts="point_vectors_name",
                    help="The name of the active point vectors")

    point_tensors = String(
                    adapts="point_tensors_name",
                    help="The name of the active point tensors")

    cell_scalars = String(
                    adapts="cell_scalars_name",
                    help="The name of the active cell scalars")

    cell_vectors = String(
                    adapts="cell_vectors_name",
                    help="The name of the active cell vectors")

    cell_tensors = String(
                    adapts="cell_tensors_name",
                    help="The name of the active cell tensors")

    _target = Instance(filters.SetActiveAttribute, ())

set_active_attribute = make_function(SetActiveAttributeFactory)


##############################################################################
class UserDefinedFactory(PipeFactory):
    """Applies the UserDefined mayavi filter to the given TVTK object."""

    _target = Instance(filters.UserDefined, ())

    filter = Instance(tvtk.Object, adapts="filter",
                      help="the tvtk filter to adapt. This"
                           "be either an instance of the filter, or the"
                           "name of this filter.")

    def __init__(self, parent, **kwargs):
        if 'filter' in kwargs:
            filter = kwargs['filter']
            if not isinstance(filter, tvtk.Object):
                try:
                    filter = getattr(tvtk, filter)
                except AttributeError:
                    raise Exception('Filter %s unknown to TVTK' % filter)
                kwargs['filter'] = filter()
                self._target.filter = kwargs['filter']
                self._target.setup_filter()
            else:
                self._target.filter = kwargs['filter']
            if not 'name' in kwargs:
                kwargs['name'] = 'UserDefined(%s)' % \
                        kwargs['filter'].__class__.__name__
        super(UserDefinedFactory, self).__init__(parent, **kwargs)

user_defined = make_function(UserDefinedFactory)


############################################################################
# Automatically generated filters from registry.
############################################################################
class _AutomaticFilterFactory(PipeFactory):
    """The base class for any auto-generated factory classes.

    NOTE: This class requires that the `_metadata` trait be set to
    the metadata object for the object for which this is a factory.
    """

    # The target.
    _target = Property

    # The saved target that is created once and then always returned.
    _saved_target = Any(None)

    def _get__target(self):
        """Getter for the _target trait."""
        if self._saved_target is None:
            self._saved_target = self._metadata.get_callable()()

        return self._saved_target


def _make_functions(namespace):
    """Make the functions for adding filters and add them to the
    namespace automatically.
    """
    for fil in registry.filters:
        func_name = camel2enthought(fil.id)
        class_name = fil.id
        if func_name.endswith('_filter'):
            func_name = func_name[:-7]
            class_name = class_name[:-6]
        class_name = class_name + 'Factory'

        # Don't create any that are already defined.
        if class_name in namespace:
            continue

        # The class to wrap.
        klass = new_class(
            class_name, (_AutomaticFilterFactory,), {'__doc__': fil.help, }
        )
        klass._metadata = fil

        # The mlab helper function.
        func = make_function(klass)

        # Inject class/function into the namespace and __all__.
        namespace[class_name] = klass
        namespace[func_name] = func
        __all__.append(func_name)

# Create the module related functions.
_make_functions(locals())
