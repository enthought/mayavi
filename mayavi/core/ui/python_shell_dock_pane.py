from traits.api import Str, List, Dict, Instance
from pyface.api import PythonShell
from pyface.tasks.api import DockPane


class PythonShellDockPane(DockPane):
    id = 'python_shell_dock_pane'
    name = 'Python Shell'

    def create_contents(self, parent):
        """ Create the python shell task pane

        This wraps the standard pyface PythonShell

        self.shell = shell = PythonShell(parent)
        shell.on_trait_change(self._on_key_pressed, "key_pressed")
        shell.on_trait_change(self._on_command_executed, "command_executed")

        # Write application standard out to this shell instead of to DOS window
        self.on_trait_change(
            self._on_write_stdout, "stdout_text", dispatch="ui"
        )
        self.original_stdout = sys.stdout
        sys.stdout = PseudoFile(self._write_stdout)

        # Namespace contributions.
        for bindings in self._bindings:
            for name, value in bindings.items():
                self.bind(name, value)

        for command in self._commands:
            self.execute_command(command)

        # We take note of the starting set of names and types bound in the
        # interpreter's namespace so that we can show the user what they have
        # added or removed in the namespace view.
        self._namespace_types = set(
            (name, type(value)) for name, value in self.namespace.items()
        )

        # Register the view as a service.
        app = self.window.application
        self._service_id = app.register_service(IPythonShell, self)

        return self.shell.control
        """
        
        self.shell = PythonShell(parent)
        return self.shell.control

    

