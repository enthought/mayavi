"""Run the examples the gallery does not, one subprocess per script.

``docs/source/render_examples.py`` executes every example it can shoot a
figure of, which is most of ``examples/mayavi``.  This covers the rest --
``examples/tvtk``, the explorer application, the top-level ones, and the few
in the gallery directories that neither show a figure nor open a dialog -- so
that between the two every example in the repository is run somewhere.

Which examples those are is asked of the renderer rather than listed here: one
that stops being rendered starts being run by this instead, with no list to
keep in step.
"""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
DOCS_SOURCE = HERE.parent / 'docs' / 'source'

# No example takes anything like this long; it is here so that one that will
# never finish fails the run instead of hanging it.
TIMEOUT = 120


def _rendered_examples():
    """The examples the gallery runs, from the renderer that runs them."""
    # docs/source holds mayavi/ and tvtk/ subdirectories, and a namespace
    # package beats an installed one wherever it turns up on sys.path -- so
    # bind the real ones before putting it there.  See CLAUDE.md.
    import mayavi                                      # noqa: F401
    import tvtk.api                                    # noqa: F401
    sys.path.insert(0, str(DOCS_SOURCE))
    try:
        from render_examples import rendered_examples
        return rendered_examples()
    finally:
        sys.path.remove(str(DOCS_SOURCE))


def _unrendered_examples():
    every = {path.resolve() for path in HERE.glob('*/**/*.py')
             if path.name != 'conftest.py'}
    return sorted(every - {Path(name) for name in _rendered_examples()})


EXAMPLES = _unrendered_examples()


@pytest.mark.parametrize(
    'example', EXAMPLES, ids=[str(path.relative_to(HERE)) for path in EXAMPLES])
def test_example(example, tmp_path):
    # a fresh working directory each time: several examples write a file
    # beside themselves (off_screen.py's example.png, the mayavi2 application's
    # saved window layout), and none of these read one
    code = ('from mayavi.tests.common import run_example_headless\n'
            'run_example_headless(%r)\n' % str(example))
    proc = subprocess.run([sys.executable, '-c', code], cwd=tmp_path,
                          timeout=TIMEOUT, capture_output=True, text=True)
    if proc.returncode != 0:
        pytest.fail(
            '%s failed (exit status %d)\n\n--- stdout ---\n%s\n--- stderr ---\n%s'
            % (example.relative_to(HERE), proc.returncode, proc.stdout[-3000:],
               proc.stderr[-3000:]),
            pytrace=False)
