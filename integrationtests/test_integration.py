"""Run the integration tests under pytest, one subprocess per script.

The scripts in ``mayavi/`` are not pytest modules: each subclasses
``TestCase(Mayavi)``, stands the Mayavi2 application up around itself and
drives it from a real Qt event loop, and is meant to be run as ``python
test_contour.py``.  Letting pytest import them would hand it a pile of
``Test*`` classes it cannot instantiate, and running them in one process would
leak engine and scene state from each into the next -- which is why ``run.py``
has always shelled out per script.

So does this, and pytest gets one case per script with the script's own output
as the failure message.  ``conftest.py`` keeps collection out of ``mayavi/``;
this file sits beside it so that it is still collected itself.
"""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT_DIR = Path(__file__).parent / 'mayavi'
SCRIPTS = sorted(p.name for p in SCRIPT_DIR.glob('test_*.py'))

# The whole suite takes about two minutes; the slowest single script is
# test_mlab_show at ~30 s.  This is only here so that one that wedges fails the
# job instead of hanging it until the runner's own limit.
TIMEOUT = 300


@pytest.mark.parametrize('script', SCRIPTS)
def test_integration(script):
    proc = subprocess.run([sys.executable, script], cwd=SCRIPT_DIR,
                          timeout=TIMEOUT, capture_output=True, text=True)
    if proc.returncode != 0:
        # the script reports through its exit status, so its streams are the
        # only account of what went wrong
        pytest.fail(
            '%s failed (exit status %d)\n\n--- stdout ---\n%s\n--- stderr ---\n%s'
            % (script, proc.returncode, proc.stdout[-3000:],
               proc.stderr[-3000:]),
            pytrace=False)
