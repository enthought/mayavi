"""Tests for mayavi.core.customize."""

import unittest

# We need this import of NullEngine since importing customize first can
# result in circular imports.
from mayavi.core.null_engine import NullEngine

from mayavi.core import customize


class TestCustomize(unittest.TestCase):
    def test_import_contrib(self):
        """Test the import_contrib function."""
        for mname in ('mayavi.api',
                      'mayavi',
                      'mayavi.core',
                      'mayavi.core.base'):
            mod = customize._import_contrib(mname)
            self.assertEqual(mod.__name__, mname)


if __name__ == '__main__':
    unittest.main()
