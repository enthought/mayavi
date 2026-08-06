"""Runtime fixes for the (unmaintained) pyface workbench code.

Mayavi is the last consumer of ``pyface.workbench`` and of envisage's views
onto it, so bugs there are ours to carry until a release fixes them.  Both
patches here are on the "View -> Other..." path and are needed to open the
Python shell from it; see tvtk/WORKAROUNDS.md for the cull rules.
"""
# License: BSD Style.

import logging
import sys

logger = logging.getLogger(__name__)


def fix_view_chooser():
    """Repair ``IViewTreeNode.is_node_for`` if the installed pyface needs it.

    pyface's "View -> Other..." dialog adapts by calling the interface,
    ``IView(obj, Undefined)``.  traits deprecated that in 6.0 and removed it
    in 7.0, so with traits >= 7 the dialog raises ``TypeError`` instead of
    opening (mayavi gh-1409, pyface gh-1263).  pyface gh-1264 fixed it on
    main, but pyface's latest release (8.0.0) predates that commit.
    """
    from pyface.workbench.action.view_chooser import IViewTreeNode

    try:
        IViewTreeNode().is_node_for(object())
    except TypeError:
        pass
    else:
        return

    from pyface.workbench.api import IView
    from traits.adaptation.api import adapt
    from traits.api import Undefined

    def is_node_for(self, obj):
        # 'is obj' rather than 'is not None': objects that merely *adapt* to
        # IView are deliberately not handled by this node.
        return adapt(obj, IView, default=Undefined) is obj

    IViewTreeNode.is_node_for = is_node_for
    logger.debug('Patched pyface IViewTreeNode.is_node_for (gh-1409)')


def _restore_qfont_typewriter():
    """Put back the ``QFont.TypeWriter`` alias PyQt6 dropped, for pyface.

    pyface names that style hint unscoped, the way PyQt5 and PySide expose it,
    in its console widget, its code editor and its font registry.  PyQt6 has
    only the scoped enums, so building the Python shell there raises
    ``AttributeError: type object 'QFont' has no attribute 'TypeWriter'``.  One
    alias covers every one of those call sites.
    """
    try:
        from pyface.qt import QtGui
    except ImportError:     # a toolkit with no Qt behind it
        return
    if hasattr(QtGui.QFont, 'TypeWriter'):
        return
    QtGui.QFont.TypeWriter = QtGui.QFont.StyleHint.TypeWriter
    logger.debug('Restored QFont.TypeWriter for pyface (gh-1409)')


def fix_python_shell_view():
    """Repair envisage's Python shell view against pyface's widget API.

    pyface 8.0 split widget construction in two -- ``PythonShell(parent)``
    leaves ``control`` at None until ``create()`` is called -- and envisage
    never made the second call, so picking "Python" in "View -> Other..."
    dies reading ``self.namespace`` off a shell that has no interpreter yet
    (the next failure along gh-1409, on 7.0.4 and on envisage main).  Building
    the shell for real then needs `_restore_qfont_typewriter` under PyQt6.

    It surfaces as ``AttributeError: no attribute '_service_id'`` instead:
    pyface's ``add_view`` runs ``destroy_control()`` from the except branch
    that handles a failed ``create_control()``, and that unregisters a service
    ``create_control()`` assigns on its last line.  Both halves are patched,
    the second so the next such failure keeps its own traceback.
    """
    _restore_qfont_typewriter()

    from envisage.plugins.python_shell.view import python_shell_view

    view_class = python_shell_view.PythonShellView
    if getattr(view_class.destroy_control, '_mayavi_patched', False):
        return

    class _CreatedPythonShell(python_shell_view.PythonShell):
        """A ``PythonShell`` whose control exists once ``__init__`` returns."""

        def __init__(self, parent=None, **traits):
            super().__init__(parent=parent, **traits)
            self.create()

        def create(self, parent=None):
            # Idempotent, so an envisage that grows its own create() call is
            # left alone rather than building the control twice.
            if self.control is None:
                super().create(parent)

    original_destroy_control = view_class.destroy_control

    def destroy_control(self):
        if hasattr(self, '_service_id'):
            original_destroy_control(self)
            return
        # A create_control() that failed part way still redirected sys.stdout
        # into the shell it went on to give up on, so unwind that much.
        logger.debug('Python shell view was never fully created')
        python_shell_view.View.destroy_control(self)
        if self.original_stdout is not None:
            self.on_trait_change(
                self._on_write_stdout, 'stdout_text', remove=True)
            sys.stdout = self.original_stdout

    destroy_control._mayavi_patched = True

    python_shell_view.PythonShell = _CreatedPythonShell
    view_class.destroy_control = destroy_control
    logger.debug('Patched envisage PythonShellView (gh-1409)')
