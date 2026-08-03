"""Pytest configuration for the mayavi test suite."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import pytest

# One filter per line, "#" comments allowed.
WARNING_LINES = r"""
error::
# unsatisfiable until pyface.workbench moves
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


def fail_instead_of_dialogs(set_attr=setattr):
    """Keep mayavi's error reporting from blocking (or hiding) a test run.

    A failure inside a pipeline update -- including a warning raised as an
    error -- is swallowed by a bare ``except:`` and shown in a modal pyface
    box, so on a headed toolkit the run stops until someone clicks OK and the
    test then passes regardless.  Re-raise instead, and route the genuinely
    user-facing messages to the log only.

    `set_attr` is the hook the fixture below uses to get its changes undone
    again; the integration scripts, which are whole processes of their own,
    take the default and keep them.
    """
    from mayavi.core import common
    set_attr(common, 'reraise_exceptions', True)
    if common.pyface is not None:
        for name in ('error', 'warning', 'information'):
            set_attr(common.pyface, name,
                     lambda parent, msg, *args, _name=name, **kwargs:
                         common.logger.info('pyface.%s: %s', _name, msg))


@pytest.fixture(autouse=True)
def no_modal_dialogs(monkeypatch):
    """Apply `fail_instead_of_dialogs` for the duration of each test."""
    fail_instead_of_dialogs(monkeypatch.setattr)
