"""Regression test for mlab.savefig(size=...) on an onscreen figure (gh-1288).

The first savefig used to capture at the window's size instead of the
requested one: set_size resized the embedded scene widget, which the
enclosing layout immediately reasserted, and the pre-layout widget size
inflated the auto magnification.
"""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import os
import shutil
import subprocess
import sys

import pytest

_SCRIPT = """
import os
import tempfile

from mayavi import mlab
from tvtk.api import tvtk


def png_size(fname):
    r = tvtk.PNGReader(file_name=fname)
    r.update()
    ext = r.output.extent
    return (ext[1] + 1, ext[3] + 1)


d = tempfile.mkdtemp()
# explicit, since both cases below are relative to it: (100, 80) is smaller
# than the window and (1200, 900) larger, exercising the magnification path
mlab.figure(size=(400, 350))
sizes = []
for n in range(3):
    mlab.test_contour3d()
    mlab.draw()
    fname = os.path.join(d, 'i%d.png' % n)
    mlab.savefig(fname, size=(100, 80))
    mlab.clf()
    sizes.append(png_size(fname))
# the first save is the regression: it saw the unsettled window size
assert sizes == [(100, 80)] * 3, sizes

# larger than the window exercises the magnification path
big = os.path.join(d, 'big.png')
mlab.savefig(big, size=(1200, 900))
assert png_size(big) == (1200, 900), png_size(big)
print('OK')
"""


@pytest.mark.timeout(180)
def test_savefig_size_onscreen():
    if sys.platform != 'linux':
        pytest.skip('needs xvfb-run or an X display; exercised on Linux')
    from traits.etsconfig.api import ETSConfig
    if ETSConfig.toolkit not in ('', 'qt', 'qt4'):
        pytest.skip(f'Qt-only test, got toolkit={ETSConfig.toolkit!r}')
    cmd = [sys.executable, '-c', _SCRIPT]
    xvfb = shutil.which('xvfb-run')
    if xvfb is not None:
        # a fresh server keeps windows off the developer's desktop, and
        # nests fine inside CI's own Xvfb
        cmd = [xvfb, '-a'] + cmd
    elif not os.environ.get('DISPLAY'):
        pytest.skip('no display and no xvfb-run')
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=150)
    assert res.returncode == 0, res.stdout + res.stderr
    assert 'OK' in res.stdout, res.stdout
