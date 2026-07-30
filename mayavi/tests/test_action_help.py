import unittest
from unittest.mock import patch

from mayavi.action import help as action_help


class TestBrowserOpen(unittest.TestCase):
    def test_macos_passes_url_as_one_argument(self):
        url = '/tmp/Mayavi Docs; unexpected-command'
        with patch.object(action_help.sys, 'platform', 'darwin'):
            with patch.object(action_help.subprocess, 'Popen') as popen:
                action_help.browser_open(url)

        popen.assert_called_once_with(['open', url])


if __name__ == '__main__':
    unittest.main()
