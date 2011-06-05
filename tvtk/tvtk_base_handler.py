""" Handler and UI elements for tvtk objects.
"""
# Author: Vibha Srinivasan <vibha@enthought.com>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Str, Instance, Property, Button, List, Enum
from traitsui.api import Handler, UIInfo, TableEditor, View, Item
from traitsui.table_column import ObjectColumn
from traits.trait_base \
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

   # A reference to the UIInfo object.
   info = Instance(UIInfo)

   # Type of view (of info.object) to display.
   view_type = Enum(['Basic', 'Advanced'])

   # The view for the object (that is, info.object)
   view = Property(depends_on='view_type')

   # List of TraitsViewObject items, where each item contains information
   # about the trait to display as a row in a table editor.
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
       """ Returns a list of objects to be included in the table editor for
       the full traits view.
       """
       return [TraitsViewObject(name=name, parent = self.info.object)
                          for name in self.info.object._full_traitnames_list_]

   def _get_view(self):
      """ Returns the view (for info.object) to be displayed in the
      InstanceEditor.
      """
      if self.view_type ==  "Basic":
           view = self.info.object.trait_view('view')
      else:
           view = self.info.object.trait_view('full_traits_view')
      # This method is called when the default traits view for the object is
      # displayed. The default traits view already has a title, so do not
      # display a title for the contained view.
      view.title = ''
      return view


#### EOF ###################################################################
