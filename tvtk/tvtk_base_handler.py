""" Handler and UI elements for tvtk objects.
"""
# Author: Vibha Srinivasan <vibha@enthought.com>
# Copyright (c) 2008-2020,  Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Str, Instance, Property, Button, List, Enum
from traitsui.handler import Handler
from traitsui.ui_info import UIInfo
from traitsui.item import Item
from traitsui.view import View
from traits.trait_base import user_name_for, xgetattr

def TableEditor(*args, **kw):
   from .value_column import ObjectColumn, ValueColumn
   from traitsui.api import TableEditor as _E
   return _E(columns=[ObjectColumn(name='name'), ValueColumn(name='value')])


class TraitsViewObject(HasTraits):
   """ Wrapper for all items to be included in the full traits view of the TVTKBase
   object.
   """

   # Trait name (name of the trait that is to be included in the view).
   name = Str

   # The TVTKBase object for which we are building a view.
   parent = Instance(HasTraits)



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
   _full_traits_list = Property(List, editor=TableEditor)

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
