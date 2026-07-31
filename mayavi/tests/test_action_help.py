import unittest
from unittest.mock import patch

from mayavi.action import help as action_help


class TestBrowserOpen(unittest.TestCase):
    def test_opens_url(self):
        url = '/tmp/Mayavi Docs; unexpected-command'
        with patch.object(action_help.webbrowser, 'open') as open_mock:
            action_help.browser_open(url)

        open_mock.assert_called_once_with(url, autoraise=1)


if __name__ == '__main__':
    unittest.main()
