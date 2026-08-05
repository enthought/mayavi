"""Runtime fixes for the (unmaintained) pyface workbench code.

pyface's "View -> Other..." dialog adapts by calling the interface,
``IView(obj, Undefined)``.  traits deprecated that in 6.0 and removed it in
7.0, so with traits >= 7 the dialog raises ``TypeError`` instead of opening
(mayavi gh-1409, pyface gh-1263).  pyface gh-1264 fixed it on main, but
pyface's latest release (8.0.0) predates that commit, so mayavi patches the
method itself until a release carries the fix -- see tvtk/WORKAROUNDS.md.
"""
# License: BSD Style.

import logging

logger = logging.getLogger(__name__)


def fix_view_chooser():
    """Repair ``IViewTreeNode.is_node_for`` if the installed pyface needs it."""
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
