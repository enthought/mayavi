"""Keep pytest away from the integration tests."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

# These are not pytest tests: each is a script subclassing TestCase(Mayavi),
# driven by run.py.  Collecting them launches the Mayavi2 application and waits
# for someone to close the window, so a bare `pytest` at the repo root has to
# skip the whole tree.  See integrationtests/mayavi/README.txt.
collect_ignore_glob = ['*']
