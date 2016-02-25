"""Used by tvtk_base_handler to create a UI.
"""
from traitsui.table_column import ObjectColumn


class ValueColumn(ObjectColumn):
   """ Column to display the trait value for each trait of a tvtk object.
   """

   def get_object ( self, object ):
        """ Returns the actual object being edited.
        Overridden here to return the tvtk object (which is the parent trait of object).

        """
        return object.parent


   def target_name ( self, object ):
        """ Returns the target object and name for the column.
        Overridden here to return the trait name (which is the object's name trait) rather than the
        column's name trait.

        """
        name   = object.name
        object = self.get_object( object )
        col    = name.rfind( '.' )
        if col < 0:
            return ( object, name )

        return ( xgetattr( object, name[ :col ] ), name[ col + 1: ] )


   def get_raw_value ( self, object ):
        """ Gets the unformatted value of the column for a specified object.
        Overridden here to return the trait name (which is the object's name trait) rather than the
        column's name trait.

        """
        try:
            target, name = self.target_name( object )
            return xgetattr( target, name )
        except:
            return None
