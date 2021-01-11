from pyface.tasks.api import TraitsDockPane
from traits.api import Instance
from mayavi.core.engine import Engine

class CurrentSelectionDockPane(TraitsDockPane):

    id = 'current_slection_dock_pane'
    name = 'Mayavi Object Editor'

    engine = Instance(Engine)

    def _model_default(self):
        return self.engine

    def default_traits_view(self):
        return  self.model.trait_view()
