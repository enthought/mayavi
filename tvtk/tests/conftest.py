"""Pytest configuration for the tvtk test suite."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import pytest
from traits.api import pop_exception_handler, push_exception_handler

# One filter per line, "#" comments allowed.
WARNING_LINES = r"""
error::
# these tests instantiate every VTK class and read every getter, deprecated
# ones included; the parenthetical wording varies far too much to match on
ignore:Call to deprecated .*Deprecated since version.*:DeprecationWarning
# unsatisfiable until pyface.workbench moves -- see tvtk/WORKAROUNDS.md
ignore:Workbench will be moved from pyface:PendingDeprecationWarning
# should be fixed in traits
ignore: module 'sre_.+' is deprecated:DeprecationWarning
"""


def pytest_configure(config):
    """Add the warning filters this suite needs."""
    # Later entries win, so skip any the other suite's conftest already added:
    # a second "error::" would outrank the ignores it put there (`pytest mayavi
    # tvtk` runs both, and pluggy calls the two hooks in reverse load order).
    existing = config.getini('filterwarnings')
    for line in WARNING_LINES.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and line not in existing:
            config.addinivalue_line('filterwarnings', line)


@pytest.fixture(autouse=True, scope='session')
def reraise_notification_exceptions():
    """Let an exception inside a traits notification reach the test.

    A copy of the mayavi suite's fixture, which tvtk cannot import from: it
    is the layer below.  Without it, running this suite on its own swallows
    what running it after mayavi's would raise.
    """
    push_exception_handler(reraise_exceptions=True)
    yield
    pop_exception_handler()
