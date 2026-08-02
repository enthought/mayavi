"""End to end tests for off screen rendering.

Nothing else in the suite renders through ``mlab.options.offscreen``, which is
how the off screen branch of ``tvtk_scene._create_control`` came to pick a
render window that segfaults on arrival without CI ever noticing --
https://github.com/enthought/mayavi/issues/1332.

Each case gets its own interpreter.  The option is process-global and the
engine it installs leaks into whatever runs next, and a render window that
cannot initialize takes the process down with it, which this way costs one
test rather than the whole run.

"""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import os
import subprocess
import sys
import textwrap

import pytest


# The backends vtkOpenGLRenderWindow::New() can hand back on Linux, each
# forced in turn so that none of them is left to whatever the machine running
# the tests happens to prefer.  OSMesa has no other coverage anywhere, and
# mayavi carried an OSMesa-specific workaround for years that nothing ever
# exercised.  Elsewhere there is only the one native window to pick from.
BACKENDS = [None]
if sys.platform.startswith('linux'):
    BACKENDS += ['vtkXOpenGLRenderWindow', 'vtkEGLRenderWindow',
                 'vtkOSOpenGLRenderWindow']

# What can VTK, on its own, render off screen with here?  If it cannot render
# at all then neither can mayavi, and that is not a mayavi bug to fail on.
PROBE = """
import vtk

renwin = vtk.vtkRenderWindow()
renwin.SetOffScreenRendering(1)
renwin.SetSize(50, 50)
renwin.AddRenderer(vtk.vtkRenderer())
renwin.Render()
print(renwin.GetClassName())
"""

RENDER = """
import sys

import numpy as np
from mayavi import mlab

mlab.options.offscreen = True
figure = mlab.figure(size=(200, 150))
renwin = figure.scene.render_window
assert renwin.off_screen_rendering, 'window is on screen'
print('render_window=%s' % renwin.class_name)
mlab.test_contour3d()
image = mlab.screenshot()
mlab.savefig(sys.argv[1])
mlab.close(all=True)

colors = np.unique(image.reshape(-1, image.shape[-1]), axis=0)
assert len(colors) > 1, 'nothing was drawn, the image is a flat %s' % colors
"""

# Importing this is all it takes to be worth testing: it sets
# options.offscreen itself, and used to preload OSMesa at import time.
IMPORT_REMOTE = """
import mayavi.tools.remote.remote_scene as remote_scene

from mayavi.tools.engine_manager import options
assert options.offscreen, 'importing remote_scene no longer forces offscreen'
print('imported=%s' % remote_scene.__name__)
"""


def _backend_env(backend):
    return None if backend is None else {'VTK_DEFAULT_OPENGL_WINDOW': backend}


def _coverage_env():
    """Have the child record coverage too, when we are running under it.

    coverage ships a ``.pth`` that calls ``process_startup()`` whenever
    COVERAGE_PROCESS_CONFIG or COVERAGE_PROCESS_START is set, so the child
    needs nothing from us but the environment.  It writes its own suffixed
    data file, which the parent run combines.  Without this every module
    these tests exercise is reported as never imported, since coverage does
    not follow subprocesses on its own.

    """
    try:
        import coverage
    except ImportError:
        return {}
    current = coverage.Coverage.current()
    if current is None:
        return {}
    try:
        # Hand the child our live config, so it lands in the same data file
        # under the same source filter.  Preferred over pointing it at
        # .coveragerc, which does not have whatever ``--cov=`` narrowed the
        # run to (and which pytest-cov names whether or not it exists).
        return {'COVERAGE_PROCESS_CONFIG': current.config.serialize()}
    except AttributeError:  # coverage too old to serialize a config
        config_file = current.config.config_file
        if config_file and os.path.exists(config_file):
            return {'COVERAGE_PROCESS_START': config_file}
        return {}


def _run(source, *args, env=None):
    """Run `source` in a fresh interpreter, with `env` added to ours."""
    child_env = dict(os.environ, **_coverage_env())
    child_env.update(env or {})
    return subprocess.run(
        [sys.executable, '-c', textwrap.dedent(source), *args],
        capture_output=True, text=True, env=child_env,
    )


def _probe(env=None):
    """The class VTK renders off screen with under `env`; skip if it cannot."""
    probe = _run(PROBE, env=env)
    if probe.returncode != 0:
        pytest.skip(
            'VTK itself cannot render off screen in this environment:\n'
            + probe.stderr
        )
    return probe.stdout.strip().splitlines()[-1]


def _require_backend(backend):
    """Skip unless VTK really renders off screen on `backend` here."""
    env = _backend_env(backend)
    expected = _probe(env)
    if backend is not None and expected != backend:
        # VTK_DEFAULT_OPENGL_WINDOW states a preference, not a demand: the
        # cascade carries on past the backend asked for when that one will
        # not initialize (X11 with no display, EGL with no driver, ...).
        pytest.skip(
            'VTK falls back to %s rather than %s here' % (expected, backend)
        )
    return env, expected


@pytest.mark.timeout(60)  # a whole interpreter, import and render
@pytest.mark.parametrize('backend', BACKENDS)
def test_offscreen_render(tmp_path, backend):
    env, expected = _require_backend(backend)
    saved = tmp_path / 'offscreen.png'
    result = _run(RENDER, str(saved), env=env)
    assert result.returncode == 0, result.stderr
    assert saved.stat().st_size > 0
    # The whole of gh-1332 is mayavi rendering with a window VTK would not
    # have chosen, so hold it to the class the probe just got.  It also keeps
    # a VTK that ignored the variable from passing every case off as coverage
    # of the one default backend.
    assert 'render_window=%s' % expected in result.stdout


@pytest.mark.timeout(60)
@pytest.mark.parametrize('backend', BACKENDS)
def test_remote_scene_importable(backend):
    """``mayavi.tools.remote`` is imported by the notebook widget manager."""
    env, _ = _require_backend(backend)
    result = _run(IMPORT_REMOTE, env=env)
    assert result.returncode == 0, result.stderr
    assert 'imported=' in result.stdout


@pytest.mark.timeout(60)
@pytest.mark.skipif(
    not sys.platform.startswith('linux'),
    reason='__EGL_VENDOR_LIBRARY_FILENAMES is a libglvnd (Linux) knob',
)
def test_offscreen_render_without_an_egl_driver(tmp_path):
    """Off screen rendering must not need EGL when something else will do.

    The wheels ship EGL support everywhere, so the class being importable says
    nothing about whether there is a driver behind it -- a slim container with
    ``libgl1`` and an Xvfb display typically has none.  Point libglvnd at a
    vendor file that does not exist to get the same situation here.

    """
    env = {
        '__EGL_VENDOR_LIBRARY_FILENAMES': str(tmp_path / 'no-such-driver.json')
    }
    expected = _probe(env)
    saved = tmp_path / 'offscreen.png'
    result = _run(RENDER, str(saved), env=env)
    assert result.returncode == 0, result.stderr
    assert saved.stat().st_size > 0
    assert 'render_window=%s' % expected in result.stdout
