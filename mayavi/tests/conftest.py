"""Pytest configuration for the mayavi test suite."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import pytest
from traits.api import pop_exception_handler, push_exception_handler

from mayavi.tests.common import fail_instead_of_dialogs

# One filter per line, "#" comments allowed.
WARNING_LINES = r"""
error::
# unsatisfiable until pyface.workbench moves -- see tvtk/WORKAROUNDS.md
ignore:Workbench will be moved from pyface:PendingDeprecationWarning
# should be fixed in traits
ignore: module 'sre_.+' is deprecated:DeprecationWarning
"""


# VTK's own numpy_support.vtk_to_numpy assigns to .shape, which NumPy 2.5
# deprecated; fixed in 9.7, so keep it an error there -- see
# tvtk/WORKAROUNDS.md
OLD_VTK_WARNING_LINES = r"""
ignore:Setting the shape on a NumPy array has been deprecated:DeprecationWarning
"""


def pytest_configure(config):
    """Add the warning filters this suite needs."""
    from tvtk.common import vtk_major_version, vtk_minor_version
    lines = WARNING_LINES
    if (vtk_major_version, vtk_minor_version) < (9, 7):
        lines += OLD_VTK_WARNING_LINES
    # Later entries win, so skip any the other suite's conftest already added:
    # a second "error::" would outrank the ignores it put there (`pytest mayavi
    # tvtk` runs both, and pluggy calls the two hooks in reverse load order).
    existing = config.getini('filterwarnings')
    for line in lines.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and line not in existing:
            config.addinivalue_line('filterwarnings', line)


@pytest.fixture(autouse=True)
def no_modal_dialogs(monkeypatch):
    """Apply `fail_instead_of_dialogs` for the duration of each test."""
    fail_instead_of_dialogs(monkeypatch.setattr)


@pytest.fixture(autouse=True, scope='session')
def reraise_notification_exceptions():
    """Let an exception inside a traits notification reach the test.

    Traits logs and swallows those, which leaves a test asserting against a
    half-built pipeline -- so this belongs to the whole run, and is popped
    again at the end of it.  It used to be pushed at import time by
    test_mlab_integration.py and never popped, which meant every module
    collected after that one silently inherited it and running a module on
    its own behaved differently from running the suite.
    """
    push_exception_handler(reraise_exceptions=True)
    yield
    pop_exception_handler()
