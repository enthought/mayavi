"""Pytest configuration for the tvtk test suite."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# One filter per line, "#" comments allowed.
WARNING_LINES = r"""
error::
# these tests instantiate every VTK class and read every getter, deprecated
# ones included; the parenthetical wording varies far too much to match on
ignore:Call to deprecated .*Deprecated since version.*:DeprecationWarning
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
