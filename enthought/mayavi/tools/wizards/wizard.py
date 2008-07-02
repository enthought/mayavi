
from enthought.traits.api import HasTraits, Dict, Property, Str
from enthought.traits.ui.api import EnumEditor, View, Item

class Wizard(HasTraits):

    data_sources = Dict

    _selected_data_source = Str

    _data_sources_labels = Property(depends_on='data_sources')

    def _get__data_sources_labels(self):
        return self.data_sources.keys()

    view = View(Item('_selected_data_source', 
                    editor=EnumEditor(name='_data_sources_labels')))

wizard = Wizard(data_sources={'1':1, '2':2, '3':3})

wizard.edit_traits()

