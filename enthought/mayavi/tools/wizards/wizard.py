
from enthought.traits.api import HasTraits, Dict, Property, Str
from enthought.traits.ui.api import EnumEditor, View, Item, Handler
from enthought.traits.ui.menu import OKCancelButtons
from enthought.pyface.api import GUI

############################################################################
# The WizardHandler class
############################################################################
class WizardHandler(Handler):
    
    def closed(self, info, is_ok):
        if is_ok:
            info.object._build_data_source()


############################################################################
# The Wizard class
############################################################################
class Wizard(HasTraits):

    data_sources = Dict

    _selected_data_source = Str

    _data_sources_labels = Property(depends_on='data_sources')

    def _get__data_sources_labels(self):
        return self.data_sources.keys()

    view = View(Item('_selected_data_source', 
                    editor=EnumEditor(name='_data_sources_labels')), 
                    handler=WizardHandler(),
                    buttons=OKCancelButtons,
                    title='Import arrays wizard')


    def _build_data_source(self):
        """ This is where we apply the selections made by the user in
            in the wizard to build the data source.
        """
        print "building source"
   

wizard = Wizard(data_sources={'1':1, '2':2, '3':3})

wizard.edit_traits()

