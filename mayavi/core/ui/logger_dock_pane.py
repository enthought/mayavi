from traits.api import Str, List, Dict, Instance
from pyface.api import PythonShell
from pyface.tasks.api import TraitsDockPane
from apptools.logger.plugin.view.logger_view import LoggerView


class LoggerDockPane(TraitsDockPane):
    id = 'logger_dock_pane'
    name = 'Logger'

    def _model_default(self):
        return LoggerView()

    def default_traits_view(self):
        return  self.model.trait_view()