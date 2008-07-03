
from enthought.traits.api import HasTraits, Dict, Property, Str, Button
from enthought.traits.ui.api import EnumEditor, View, Item, HGroup, \
    Spring


############################################################################
# The Wizard class
############################################################################
class Wizard(HasTraits):

    ok_button = Button(label='OK')

    cancel_button = Button(label='Cancel')

    def _ok_button_fired(self):
        if self.ui:
            self.ui.dispose()
            self._build_data_source()

    def _cancel_button_fired(self):
        if self.ui:
            self.ui.dispose()

    data_sources = Dict

    _selected_data_source = Str

    _data_sources_labels = Property(depends_on='data_sources')

    def _get__data_sources_labels(self):
        return self.data_sources.keys()

    view = View(Item('_selected_data_source', 
                    editor=EnumEditor(name='_data_sources_labels')), 
                HGroup(Spring(), 
                      'cancel_button', 
                      'ok_button', 
                      show_labels=False),
                    title='Import arrays wizard')

    def _build_data_source(self):
        """ This is where we apply the selections made by the user in
            in the wizard to build the data source.
        """
        print "building source"
  

    def wizard_view(self):
        """ Pops up the view of the wizard, and keeps the reference it to
            be able to close it.
        """
        self.ui = self.edit_traits()


wizard = Wizard(data_sources={'1':1, '2':2, '3':3})

wizard.wizard_view()

