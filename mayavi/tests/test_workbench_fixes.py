# Author: Eric Larson
# License: BSD Style.

import sys

import pytest

from traits.api import HasTraits, provides
from traits.etsconfig.api import ETSConfig

from mayavi.plugins._workbench_fixes import (
    fix_python_shell_view, fix_view_chooser)


@pytest.fixture
def node_class():
    from pyface.workbench.action.view_chooser import IViewTreeNode

    original = IViewTreeNode.is_node_for
    fix_view_chooser()
    yield IViewTreeNode
    IViewTreeNode.is_node_for = original


def test_view_chooser_rejects_non_views(node_class):
    """Test that the view chooser's tree can classify a non-view (gh-1409)."""
    assert node_class().is_node_for(HasTraits()) is False


def test_view_chooser_accepts_views(node_class):
    """Test that objects providing IView still get the view node."""
    from pyface.workbench.api import IView

    @provides(IView)
    class FakeView(HasTraits):
        pass

    assert node_class().is_node_for(FakeView()) is True


@pytest.mark.skipif(ETSConfig.toolkit == 'null',
                    reason='the dialog needs a UI toolkit')
def test_view_chooser_dialog(node_class):
    """Test that "View -> Other..." builds its dialog (gh-1409)."""
    from pyface.api import GUI
    from pyface.workbench.api import WorkbenchWindow
    from pyface.workbench.action.view_chooser import ViewChooser

    GUI()  # the toolkit application object the editors need
    chooser = ViewChooser(window=WorkbenchWindow())
    # 'panel' rather than 'live': same editors, no window on screen
    ui = chooser.edit_traits(kind='panel')
    ui.dispose()


@pytest.fixture
def shell_view_module():
    from envisage.plugins.python_shell.view import python_shell_view

    shell, destroy = (python_shell_view.PythonShell,
                      python_shell_view.PythonShellView.destroy_control)
    fix_python_shell_view()
    yield python_shell_view
    python_shell_view.PythonShell = shell
    python_shell_view.PythonShellView.destroy_control = destroy


@pytest.mark.skipif(ETSConfig.toolkit == 'null',
                    reason='the shell needs a UI toolkit')
def test_python_shell_view(shell_view_module):
    """Test that "View -> Other... -> Python" creates its shell (gh-1409)."""
    from envisage.api import Application
    from envisage.ui.workbench.api import Workbench, WorkbenchWindow
    from pyface.api import GUI

    GUI()
    # 'application' is a delegate, so the workbench is what carries it
    window = WorkbenchWindow(
        workbench=Workbench(application=Application(id='test')))
    view = shell_view_module.PythonShellView(window=window)
    stdout = sys.stdout
    try:
        assert view.create_control(None) is not None
        # the interpreter behind 'namespace', which is what used to raise
        view.bind('answer', 42)
        assert view.namespace['answer'] == 42
    finally:
        view.destroy_control()
    assert sys.stdout is stdout


@pytest.mark.skipif(ETSConfig.toolkit == 'null',
                    reason='the null backend has no workbench View')
def test_python_shell_view_destroy_uncreated(shell_view_module):
    """Test that tearing down a view that never opened stays quiet."""
    # pyface's 'add_view' does exactly this when 'create_control' raises, and
    # an AttributeError here is what buried the real error in gh-1409.
    shell_view_module.PythonShellView().destroy_control()
