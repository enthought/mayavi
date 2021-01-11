from pyface.tasks.api import TraitsDockPane
from traits.etsconfig.api import ETSConfig
from traits.api import Instance
from mayavi.core.engine import Engine

class EngineDockPane(TraitsDockPane):

    id = 'engine_pane'
    name = 'Mayavi Engine'

    engine = Instance(Engine)

    def _model_default(self):
        from mayavi.core.ui.engine_view import EngineView
        return EngineView(engine=self.engine)

    def default_traits_view(self):
        return self.model.trait_view()

    def create_contents(self, parent):
        """ Create and return the toolkit-specific contents of the dock pane.
        """
        if ETSConfig.toolkit.startswith('qt'):
            from pyface.qt import QtGui
            self._panel = QtGui.QMainWindow()
            self._content = super(EngineDockPane, self).create_contents(self._panel)
            self._panel.setCentralWidget(self._content)
            return self._panel

        self.ui = self.edit_traits(kind="subpanel", parent=parent)
        return self.ui.control