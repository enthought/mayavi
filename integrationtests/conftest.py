"""Keep pytest out of the integration scripts themselves."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# The files in mayavi/ are not pytest tests: each is a script subclassing
# TestCase(Mayavi), meant to be run as `python test_contour.py`.  Collecting
# them would hand pytest Test* classes it cannot instantiate and stand up the
# Mayavi2 application at import time.  test_integration.py, beside this file,
# runs them the way they expect -- one subprocess each -- so it is collected
# normally.  See integrationtests/mayavi/README.txt.
collect_ignore_glob = ['mayavi/*']
