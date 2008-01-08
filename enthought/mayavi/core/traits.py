#-------------------------------------------------------------------------------
#
#  SimpleDRange: is basically similar to a Range trait which obtains
#  the lower and upper limits of the range from traits on the object.
#  It is "simple" because it does not add listeners to change the
#  value when the lower and upper limits change.  When the RangeEditor
#  is in use it does add listeners but when the UI is not used nothing
#  is done to change the value.  This is therefore the users
#  responsibility.  This trait should work fine when embedded into a
#  List.
#
#  DRange: is a 'dynamic range' trait whose value is constrained to
#  lie within a range whose low and high values are determined by
#  other traits defined on the same object.
#  
#  Caveat:
#   The problem with this trait is that the listeners (for changes to
#   the low and high limit traits) are added only when the attribute
#   is read or set.  Thus if the limits are set before the listeners
#   are activated then the value will be set correctly only when it is
#   accessed and not when the low and high traits are changed.
#
#   **Please note that DRange does not work properly when embedded
#     inside a List trait.**
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
#  Date: 09/10/2006
#
#  (c) Copyright 2006 by Enthought, Inc.
#  
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from weakref import ref

from enthought.traits.api \
    import Property, TraitFactory, TraitError, TraitHandler, Trait
from enthought.traits.ui.api \
    import RangeEditor, EnumEditor

from enthought.traits.trait_handlers import RangeTypes

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
# The Trait handler for the SimpleDRange trait.
#--------------------------------------------------------------------------------

class TraitSimpleDRange ( TraitHandler ):
    """Ensures that a trait attribute lies within a specified numeric
    range.  The range itself is obtained from the traits named via
    'low_name' and 'high_name' on the object.

    TraitSimpleDRange is the underlying handler for the
    `SimpleDRange()` trait factory.

    Any value assigned to a trait containing a TraitRange handler must
    be of the correct type and in the numeric range defined by the
    traits 'low_name' and 'high_name'.  No automatic coercion takes
    place. For example::

        class Person(HasTraits):
            age = Trait(0, TraitSimpleDRange(low_name='_low', high_name='_high'))
            _low = Int(0)
            _high = Int(150)

    This example defines a **Person** class, which has an **age** trait
    attribute, which must be an integer/long in the range from 0 to 150.
    """
    def __init__ ( self, low_name, high_name, default=None, is_float=True,
                   exclude_low = False, exclude_high = False ):
        """ Creates a TraitRange handler.

        Parameters
        ----------
        low_name : Str
            The minimum value that the trait can accept as a trait on
            the object.  
        high_name : Str
            The maximum value that the trait can accept as a trait on
            the object.  
        default : Float/Int/Long
            The default value of the trait.
        is_float : Boolean
            Is the value a floating point value or not.
        exclude_low : Boolean
            Should the *low* value be exclusive (or inclusive)
        exclude_high : Boolean
            Should the *high* value be exclusive (or inclusive)

        Description
        -----------
        The *low_name* and *high_name* traits must be of the same
        Python numeric type, either **int**, **long** or
        **float**. Alternatively, one of the values may be **None**,
        to indicate that that portion of the range is unbounded. The
        *exclude_low* and *exclude_high* values can be used to specify
        whether the *low* and *high* values should be exclusive (or
        inclusive).
        """

        if default is not None:            
            vtype = type(default)
        else:
            if is_float:
                vtype = float
            else:
                vtype = int
        if vtype not in RangeTypes:
            raise TraitError, ("TraitSimpleDRange can only be use for int, long or "
                               "float values, but a value of type %s was "
                               "specified." % vtype)
        if vtype is float:
            self.validate = self.float_validate
            kind           = 4
            self.type_desc = 'a floating point number'
        elif vtype is long:
            self.validate = self.long_validate
            self.type_desc = 'a long integer'
        else:
            self.validate = self.int_validate
            kind = 3
            self.type_desc = 'an integer'
        exclude_mask = 0
        if exclude_low:
            exclude_mask |= 1
        if exclude_high:
            exclude_mask |= 2
        #if vtype is not long:
        #    self.fast_validate = ( kind, low, high, exclude_mask )

        # Assign type-corrected arguments to handler attributes
        self.default      = default
        self.low_name     = low_name
        self.high_name    = high_name
        self.exclude_low  = exclude_low
        self.exclude_high = exclude_high
        self.object = None # A weakref to the object.
        self.vtype = vtype

    def _get_low(self):
        if (self.object is None) or (self.object() is None):
            val = 0
        else:
            try:
                val = getattr(self.object(), self.low_name)
            except AttributeError:
                # FIXME: This seems necessary for the case where the
                # trait is embedded inside another like a List.
                obj = getattr(self.object(), 'object')
                val = getattr(obj, self.low_name)
        return self.vtype(val)
    
    def _get_high(self):
        if (self.object is None) or (self.object() is None):
            val = 1
        else:
            try:
                val = getattr(self.object(), self.high_name)
            except AttributeError:
                # FIXME: This seems necessary for the case where the
                # trait is embedded inside another like a List.
                obj = getattr(self.object(), 'object')
                val = getattr(obj, self.high_name)
        return self.vtype(val)

    low = property(_get_low)
    high = property(_get_high)

    def _set_object(self, object):
        if object is None:
            self.object = None
            return
        if (self.object is None) or (self.object() != object):
            self.object = ref(object)

    def float_validate ( self, object, name, value ):
        self._set_object(object)
        try:
            if (isinstance( value, RangeTypes ) and
                ((self.low  is None) or
                 (self.exclude_low and (self.low < value)) or
                 ((not self.exclude_low) and (self.low <= value))) and
                ((self.high is None) or
                 (self.exclude_high and (self.high > value)) or
                 ((not self.exclude_high) and (self.high >= value)))):
               return float( value )
        except:
            pass
        self.error( object, name, self.repr( value ) )

    def int_validate ( self, object, name, value ):
        self._set_object(object)
        try:
            if (isinstance( value, int ) and
                ((self.low  is None) or
                 (self.exclude_low and (self.low < value)) or
                 ((not self.exclude_low) and (self.low <= value))) and
                ((self.high is None) or
                 (self.exclude_high and (self.high > value)) or
                 ((not self.exclude_high) and (self.high >= value)))):
               return value
        except:
            pass
        self.error( object, name, self.repr( value ) )

    def long_validate ( self, object, name, value ):
        self._set_object(object)
        try:
            if (isinstance( value, long ) and
                ((self.low  is None) or
                 (self.exclude_low and (self.low < value)) or
                 ((not self.exclude_low) and (self.low <= value))) and
                ((self.high is None) or
                 (self.exclude_high and (self.high > value)) or
                 ((not self.exclude_high) and (self.high >= value)))):
               return value
        except:
            pass
        self.error( object, name, self.repr( value ) )

    def info ( self ):
        if self.low is None:
            if self.high is None:
                return self.type_desc
            return '%s <%s %s' % (
                   self.type_desc, '='[ self.exclude_high: ], self.high )
        elif self.high is None:
            return  '%s >%s %s' % (
                    self.type_desc, '='[ self.exclude_low: ], self.low )
        return '%s <%s %s <%s %s' % (
               self.low, '='[ self.exclude_low: ], self.type_desc,
               '='[ self.exclude_high: ], self.high )

    def get_editor ( self, trait ):
        auto_set = trait.auto_set
        if auto_set is None:
            auto_set = True
        low_name = self.low_name
        if '.' in low_name:
            low_name = low_name.split('.')[-1]
        high_name = self.high_name
        if '.' in high_name:
            high_name = high_name.split('.')[-1]
        is_float = True
        value = 0.0
        if self.vtype is not float:
            is_float = False
            value = 0
            
        return RangeEditor( self,
                            low = value,
                            high = value,                          
                            low_name  = low_name,
                            high_name = high_name,
                            mode       = trait.mode or 'auto',
                            cols       = trait.cols or 3,
                            auto_set   = auto_set,
                            enter_set  = trait.enter_set or False,
                            is_float   = is_float,
                            label_width = trait.label_width or 0,
                            format = trait.format or '%s'
                            )

#-------------------------------------------------------------------------------
#  Defines the SimpleDRange trait.
#-------------------------------------------------------------------------------

def SimpleDRange ( low_name, high_name, default = None, is_float = True,
                   exclude_low = False, exclude_high = False,
                   **metadata ):
    value = 0
    if default is not None:
        value = default
    return Trait(value, TraitSimpleDRange( low_name, high_name,
                                           default, is_float,
                                           exclude_low, exclude_high ), 
                 **metadata )

SimpleDRange = TraitFactory( SimpleDRange )    
    
#--------------------------------------------------------------------------------
# Helper class for DRange trait.
#--------------------------------------------------------------------------------
class DRangeHelper(object):
    """Defines a bunch of staticmethods that collect all the helper
    functions needed for the DRange trait.
    """
    
    ######################################################################
    # Get/Set functions for the property.    
    def get_value ( object, name ):
        return super_getattr( object, DRangeHelper._init_listeners( object, name ) )
    get_value = staticmethod(get_value)

    def set_value ( object, name, value ):
        _name = DRangeHelper._init_listeners( object, name )
        trait = object.trait( name )
        if type(value) not in [int, long, float]:
            raise TraitError, (object, name,
                               "an integer, a long integer "
                               "or a floating point number",
                               value )
        low   = super_getattr( object, trait.low_name )
        if value < low:
            value = low
        else:
            high  = super_getattr( object, trait.high_name )
            if value > high:
                value = high
        old = super_getattr(object, _name)
        super_setattr( object, _name, value )
        object.trait_property_changed(name, old, value)
    set_value = staticmethod(set_value)

    def default_value(default_value_type=None, default_value=0):
        return (0, 0)
    default_value = staticmethod(default_value)

    ######################################################################
    #  Makes a default RangeEditor for the trait
    def make_editor ( trait = None ):
        low     = 0
        default = trait.default
        if default is not None:
            is_float = isinstance( default, float )
        else:
            is_float = (not trait.int)
        if is_float:
            low = 0.0
        return RangeEditor( low         = low,
                            high        = low,
                            low_name    = trait.low_name, 
                            high_name   = trait.high_name,
                            mode        = trait.mode or 'auto',
                            cols        = trait.cols or 3,
                            auto_set    = trait.auto_set or True,
                            enter_set   = trait.enter_set or False,
                            is_float    = is_float,
                            format      = trait.format,
                            label_width = trait.label_width )
    make_editor = staticmethod(make_editor)

    ######################################################################
    # Ensures that the range low/high value listeners are initialized.    
    def _init_listeners ( object, name ):
        _name = '_' + name
        if not hasattr( object, _name ):
            trait = object.trait( name )
            DRangeHelper._add_listeners( object, name, trait.low_name, trait.high_name )
            default = trait.default
            if default is None:
                default = super_getattr( object, trait.low_name )
            else:
                low = super_getattr(object, trait.low_name)
                if default < low:
                    default = low
                else:
                    high = super_getattr(object, trait.high_name)
                    if default > high:
                        default = high
            super_setattr( object, _name, default )

        return _name
    _init_listeners = staticmethod(_init_listeners)

    def _add_listeners ( object, name, low, high ):
        def check_low ( object, low_name, old, new ):
            if super_getattr( object, name ) < new:
                super_setattr( object, name, new )

        def check_high ( object, high_name, old, new ):
            if super_getattr( object, name ) > new:
                super_setattr( object, name, new )

        object.on_trait_change( check_low,  low )
        object.on_trait_change( check_high, high )
    _add_listeners = staticmethod(_add_listeners)

    
#-------------------------------------------------------------------------------
#  Defines the DRange property:
#-------------------------------------------------------------------------------

DRange = Property( DRangeHelper.get_value,
                   DRangeHelper.set_value,
                   low_name     = 'low', 
                   high_name    = 'high', 
                   format       = '%s', 
                   label_width  = 0,
                   default_value= DRangeHelper.default_value,
                   editor       = ( DRangeHelper.make_editor, { 'trait': None } ) )

DRange = TraitFactory( DRange )


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
