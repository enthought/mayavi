
from enthought.traits.api import HasTraits, Dict, Property, Str, List
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



class _Box(HasTraits):
    # contains 1) contents and 2) item
    # self.item will return something to put into a View
    _item = Property
    
    def __init__(contents):
        print "initing a box"
        self.contents = contents
    
    def _get__item(self):
        return Item('contents')


############################################################################
# The Wizard class
############################################################################

class Wizard(HasTraits):
    
    data_sources = Dict
    
    data_list = List(_Box)
    
    def _data_sources_changed(self):
        print "The list should change now"
        print self.data_sources.keys()
        self.data_list = [ _Box(key) for key in self.data_sources.keys() ]
        
    view = Property
    
    def _get_view(self):
        return View([box._item for box in self.data_list],
                        buttons=OKCancelButtons,
                        title='Import arrays wizard')
  
                    
wizard = Wizard(data_sources={'1':11, '2':21, '5':31})

print "here I am"

print wizard.data_sources

print "more"

print wizard.data_list

wizard.edit_traits()

