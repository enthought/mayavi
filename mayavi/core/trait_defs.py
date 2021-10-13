#---------------------------------------------------------------------------
#
#  DEnum: is a 'dynamic enum' trait whose values are obtained from
#  another trait on the object.
#
#  Caveat:
#   The problem with this trait is that the listeners (for changes to
#   the valid values) are added only when the attribute is read or
#   set.  Thus if the acceptable list of values are changed before the
#   listeners are activated then the value will be set correctly only
#   when it is accessed and not when the values are set.
#
#  Written by: David C. Morrill and Prabhu Ramachandran
#
#  (c) Copyright 2006-2020 by Enthought, Inc.
#
#---------------------------------------------------------------------------

from traits.api import (CArray, Int, NO_COMPARE, Property, TraitError,
    TraitFactory, TraitType)
from traitsui.api import EnumEditor
from traits.traits import trait_cast
import numbers

#---------------------------------------------------------------------------
#  Utility functions:
#---------------------------------------------------------------------------

def super_getattr(object, name, *args):
    """Works the same way as getattr, except that name can be of the
    form 'a.b.c' (as many levels as you like).  For example:

    >>> class A:
    ... pass
    ...
    >>> a = A()
    >>> a.b = A()
    >>> a.b.c = 1
    >>> super_getattr(a, 'b.c')
    1
    >>> super_getattr(a.b, 'c')
    1
    """
    if '.' in name:
        attrs = name.split('.')
        last = attrs.pop()
        obj = object
        for attr in attrs:
            obj = getattr(obj, attr)
        return getattr(obj, last, *args)
    else:
        return getattr(object, name, *args)

def super_setattr(object, name, value):
    """Works the same way as setattr, except that name can be of the
    form 'a.b.c' (as many levels as you like).  For example:

    >>> class A:
    ... pass
    ...
    >>> a = A()
    >>> a.b = A()
    >>> super_setattr(a, 'b.c', 1)
    >>> a.b.c
    1
    """
    if '.' in name:
        attrs = name.split('.')
        last = attrs.pop()
        obj = object
        for attr in attrs:
            obj = getattr(obj, attr)
        setattr(obj, last, value)
    else:
        setattr(object, name, value)


#--------------------------------------------------------------------------------
# Helper class for DEnum trait.
#--------------------------------------------------------------------------------
class DEnumHelper(object):
    """Defines a bunch of staticmethods that collect all the helper
    functions needed for the DEnum trait.
    """

    ######################################################################
    # Get/Set functions for the property.
    def get_value ( object, name ):
        return super_getattr(object, DEnumHelper._init_listeners(object, name))
    get_value = staticmethod(get_value)

    def set_value ( object, name, value ):
        _name = DEnumHelper._init_listeners( object, name )
        trait = object.trait( name )
        values = super_getattr(object, trait.values_name)
        if value not in values:
            raise TraitError(object, name,"one of %s"%values, value)
        old = super_getattr(object, _name)
        super_setattr( object, _name, value )
        object.trait_property_changed(name, old, value)
    set_value = staticmethod(set_value)

    ######################################################################
    #  Makes a default EnumEditor for the trait:
    def make_editor ( trait = None ):
        return EnumEditor( name=trait.values_name )
    make_editor = staticmethod(make_editor)

    ######################################################################
    # Ensures that the listeners are initialized.
    def _init_listeners ( object, name ):
        _name = '_' + name
        if not hasattr( object, _name ):
            trait = object.trait( name )
            DEnumHelper._add_listeners( object, name, trait.values_name)
            default = trait.default or ''
            values = super_getattr( object, trait.values_name )
            if values:
                if default is None or default not in values:
                    default = values[0]
            super_setattr( object, _name, default )

        return _name
    _init_listeners = staticmethod(_init_listeners)

    def _add_listeners ( object, name, values_name ):
        def check_values(object, values_name, old, new):
            cur_choice = super_getattr(object, name)
            if cur_choice not in new:
                if new:
                    super_setattr(object, name, new[0])
                else:
                    super_setattr(object, name, '')

        def check_values_items(object, values_name, list_event):
            cur_choice = super_getattr(object, name)
            values = super_getattr(object, values_name[:-6])
            if cur_choice not in values:
                if values:
                    super_setattr(object, name, values[0])
                else:
                    super_setattr(object, name, '')

        object.on_trait_change( check_values,  values_name )
        object.on_trait_change( check_values_items, values_name + '_items' )
    _add_listeners = staticmethod(_add_listeners)


#-------------------------------------------------------------------------------
#  Defines the DEnum property:
#-------------------------------------------------------------------------------
DEnum = Property(DEnumHelper.get_value, DEnumHelper.set_value,
                 values_name = 'values',
                 editor  = (DEnumHelper.make_editor, {'trait': None})
                 )

DEnum = TraitFactory(DEnum)


##########################################################################
# `ShadowProperty` trait type.
##########################################################################
class ShadowProperty(TraitType):

    # Not really necessary but specifies the attribute up front.
    trait_type = None

    # Call the notifiers smartly only when the value has really changed.
    # If this is set to False, the notification will always occur.
    smart_notify = True

    def __init__(self, trait_type, smart_notify=True, **metadata):
        """Defines a shadow property trait that is best explained by
        example::

            class Thing(HasTraits):
                x = ShadowProperty(Float, smart_notify=False)
                def _x_changed(self, value):
                    print(value)

        In this example, the actual value of the property (`x`) will be
        stored in `_x` and `_x_changed` will be called regardless
        whether the value actually changed or not.  If `smart_notify` is
        set to `True` then the handler is called only if the value has
        actually changed.

        Note that the validation uses the validation of the specified
        `trait_type` parameter.
        """
        self.trait_type = trait_cast(trait_type)
        self.smart_notify = smart_notify
        super(ShadowProperty, self).__init__(**metadata)

    def validate(self, object, name, value):
        """Validates that a specified value is valid for this trait.
        """
        trt = self.trait_type
        if trt is not None and hasattr(trt, 'validate'):
            value = trt.validate(object, name, value)
        return value

    def get(self, object, name):
        """Get the value of the trait."""
        shadow = self._get_shadow(name)
        d = object.__dict__
        if shadow in d:
            return d[shadow]
        else:
            return None

    def set(self, object, name, value):
        """Set the value of the trait."""
        old = self.get(object, name)
        shadow = self._get_shadow(name)
        object.__dict__[shadow] = value
        # Fire a trait property changed.
        fire = True
        if self.smart_notify:
            if old is value:
                fire = False
        if fire and self._check_notification(object):
            object.trait_property_changed(name, old, value)

    def _get_shadow(self, name):
        """Get the shadow attribute name to use."""
        return '_' + name

    def _check_notification(self, object):
        """Checks to see if notifications are allowed or not i.e. has
        the trait been set via:
         object.trait_set(name=value, trait_change_notify=False)
        """
        if hasattr(object, '_get_trait_change_notify'):
            return object._get_trait_change_notify()
        else:
            # Traits won't tell us so we find out by adding a dynamic
            # trait, changing it and then seeing if the callback was
            # called, sigh!
            attr = '_testing_Notification_handlers_tmp_dont_touch'

            def callback(value):
                callback.value = value
            callback.value = -1
            object.add_trait(attr, Int)
            object.on_trait_change(callback, attr)
            setattr(object, attr, 1)
            status = False
            if callback.value == 1:
                status = True
            object.on_trait_change(callback, attr, remove=True)
            object.remove_trait(attr)
            return status


class ArrayOrNone(CArray):
    """ Either an array-like object or None.
    """

    def __init__(self, *args, **metadata):
        metadata['comparison_mode'] = NO_COMPARE
        super(ArrayOrNone, self).__init__(*args, **metadata)

    def validate(self, object, name, value):
        if value is None:
            return value
        return super(ArrayOrNone, self).validate(object, name, value)

    def get_default_value(self):
        return (0, None)


class ArrayNumberOrNone(CArray):
    """ Either an array-like, number converted to a 1D array, or None.
    """

    def __init__(self, *args, **metadata):
        metadata['comparison_mode'] = NO_COMPARE
        super(ArrayNumberOrNone, self).__init__(*args, **metadata)

    def validate(self, object, name, value):
        if value is None:
            return value
        elif isinstance(value, numbers.Number):
            # Local import to avoid explicit dependency.
            import numpy
            value = numpy.atleast_1d(value)
        return super(ArrayNumberOrNone, self).validate(object, name, value)

    def get_default_value(self):
        return (0, None)
