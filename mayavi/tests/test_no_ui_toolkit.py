"""
Tests to try and ensure that important mayavi imports work with no UI.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

import sys
import unittest

from traits.etsconfig.api import ETSConfig


class TestNoUIToolkit(unittest.TestCase):

    """Test if any important mayavi imports work with no UI
    whatsoever."""

    def setUp(self):
        self.orig_tk = ETSConfig.toolkit
        ETSConfig._toolkit = 'null'

        # Import something from Pyface to force any potential imports
        # from a UI toolkit.  Why did I pick Pyface? Well, adder_node
        # imports ImageResource and this seems to trigger some UI
        # toolkit import and this makes life difficult as far as the
        # testing goes.  Forcing the issue here should let us test
        # safely since the Pyface imports will be done.
        from pyface.api import GUI

        # Remove any references to wx and Qt
        saved = {}
        for mod in ['wx', 'PyQt4', 'PySide']:
            saved[mod] = sys.modules.pop(mod, None)
        self.saved = saved

    def tearDown(self):
        ETSConfig._toolkit = self.orig_tk
        # Add back any any references to wx and Qt
        for mod in ['wx', 'PyQt4', 'PySide']:
            m = self.saved[mod]
            if m is not None:
                sys.modules[mod] = m

    def test_no_ui(self):
        """Test if mayavi imports work without any UI (wx or PyQt4)."""
        # These imports should work without any UI.
        from mayavi import mlab
        from mayavi.api import Engine
        from mayavi.sources.api import VTKDataSource
        from mayavi.filters.api import Optional
        from mayavi.modules.api import Outline
        from mayavi.preferences.api import preference_manager

        # Should not have triggered an import wx or PyQt4.
        self.assertEqual('wx' in sys.modules, False)
        self.assertEqual('PyQt4' in sys.modules, False)
        self.assertEqual('PySide' in sys.modules, False)


if __name__ == '__main__':
    unittest.main()
