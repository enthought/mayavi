"""Keep pytest out of the example scripts themselves."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# The examples are scripts, not test modules: importing one builds a scene,
# opens a dialog or stands the Mayavi2 application up at import time.
# test_examples.py, beside this file, runs them the way they expect -- one
# subprocess each -- so it is collected normally.
collect_ignore_glob = ['mayavi/*', 'tvtk/*']
