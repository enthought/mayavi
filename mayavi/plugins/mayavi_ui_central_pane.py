from pyface.tasks.api import TaskPane

class MayaviUICentralPane(TaskPane):
    id = 'mayavi.ui.central_pane'
    name = 'Mayavi Central Pane'

    editor = Instance(SOMETHING )

    def create(self, parent):
        self.editor = PythonEditor(parent)
        self.control = self.editor.control

    def destroy(self):
        self.editor.destroy()
        self.control = self.editor = None