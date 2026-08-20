# Author: Eric Larson
# License: BSD Style.

import pytest

from traits.api import HasTraits, provides
from traits.etsconfig.api import ETSConfig

from mayavi.plugins._workbench_fixes import fix_view_chooser


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


@pytest.mark.skipif(ETSConfig.toolkit == 'null',
                    reason='the shell needs a UI toolkit')
def test_python_shell_builds():
    """Test that pyface's Python shell can be built (gh-1409).

    On PyQt6 it cannot without `restore_qfont_typewriter`, and this is what
    catches the alias going missing again -- it already did once, having been
    nested inside a `fix_python_shell_view` that envisage 8.0.1 retired.
    """
    from pyface.api import GUI, PythonShell
    from pyface.qt import QtGui

    from mayavi.plugins._workbench_fixes import restore_qfont_typewriter

    restore_qfont_typewriter()
    GUI()  # the toolkit application object the widget needs
    shell = PythonShell(QtGui.QWidget())
    shell.create()
    try:
        assert shell.control is not None
    finally:
        shell.destroy()
