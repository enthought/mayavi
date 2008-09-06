#-------------------------------------------------------------------------------
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
#  (c) Copyright 2006-2008 by Enthought, Inc.
#  
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from enthought.traits.api import (Property, TraitFactory, TraitError)
from enthought.traits.ui.api import EnumEditor


#-------------------------------------------------------------------------------
#  Utility functions:
#-------------------------------------------------------------------------------

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
            raise TraitError, (object, name,
                               "one of %s"%values,
                               value )
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

