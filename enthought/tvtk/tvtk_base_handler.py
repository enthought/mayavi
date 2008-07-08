""" Handler and UI elements for tvtk objects.
"""
# Author: Vibha Srinivasan <vibha@enthought.com>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

from enthought.traits.api import HasTraits, Str, Instance, Property, Button, List
from enthought.traits.ui.api import Handler, UIInfo, TableEditor
from enthought.traits.ui.table_column import ObjectColumn
from enthought.traits.trait_base \
    import user_name_for, xgetattr

class TraitsViewObject(HasTraits):
   """ Wrapper for all items to be included in the full traits view of the TVTKBase
   object. 
   """

   # Trait name (name of the trait that is to be included in the view).
   name = Str

   # The TVTKBase object for which we are building a view.
   parent = Instance(HasTraits)


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


""" A handler for the TVTKBase object. 
"""

class TVTKBaseHandler(Handler):
   """ A handler for the TVTKBase object. 
   """

   # Currently the only purpose of this class is to contribute a button which
   # when clicked will display the 'full view' for the tvtk object. We may
   # want to change the implementation so the 'full_view' appears through some
   # selection on the menu bar, and in that case, this handler class can be 
   # disposed of.
   advanced_view = Button('Display Advanced View')

   # A reference to the UIInfo object.
   info = Instance(UIInfo)

   # List of TraitsViewObject items, where each item contains information about the trait name
   # to display as a row in a table editor.
   _full_traits_list = Property(List, editor = TableEditor(columns = 
                                           [ObjectColumn(name='name'), 
                                            ValueColumn(name='value')]))

   def init_info(self, info):
       """ Informs the handler what the UIInfo object for a View will be.
       Overridden here to save a reference to the info object.
        
       """
       self.info = info
       return


   def _get__full_traits_list(self):
       return [TraitsViewObject(name=name, parent = self.info.object) 
                               for name in self.info.object._full_traitnames_list_]

 
   def _advanced_view_fired(self):
       """ Displays the full traits view for this object.
       Called when the 'advanced view' button is clicked.
       """
       self.info.object.edit_traits('full_traits_view')
       return 

#### EOF ###################################################################