from pyface.tasks.api import TraitsDockPane


class EngineDockPane(TraitsDockPane):

    id = 'engine_pane'
    name = 'Mayavi Engine'

    def _model_default(self):
        from mayavi.core.ui.engine_view import EngineView
        return EngineView(engine=self._get_engine(self.task.window))

    def _get_engine(self, window):
        """Return the Mayavi engine of the particular window."""
        from mayavi.core.engine import Engine
        return window.application.get_service(Engine)

    def default_traits_view(self):
        return  self.model.trait_view()
