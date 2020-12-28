from pyface.tasks.api import TraitsDockPane

class CurrentSelectionDockPane(TraitsDockPane):

    id = 'current_slection_dock_pane'
    name = 'Mayavi Object Editor'

    def _model_default(self):
        return self._get_engine(self.task.window)

    def _get_engine(self, window):
        """Return the Mayavi engine of the particular window."""
        from mayavi.core.engine import Engine
        return window.application.get_service(Engine)

    def default_traits_view(self):
        return  self.model.trait_view()
