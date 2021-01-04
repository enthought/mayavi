from traits.api import Str, List, Dict, Instance
from pyface.api import PythonShell
from pyface.tasks.api import DockPane

import sys

class PseudoFile(object):
    """ Simulates a normal File object.
    """

    def __init__(self, write):
        self.write = write

    def readline(self):
        pass

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    def isatty(self):
        return 1


class PythonShellDockPane(DockPane):
    id = 'python_shell_dock_pane'
    name = 'Python Shell'

    def create_contents(self, parent):

        self.shell = shell =  PythonShell(parent)
        self.task.window.application.register_service(PythonShell, shell)

        return self.shell.control
