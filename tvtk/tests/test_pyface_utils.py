import mock
import unittest

from pyface.api import FileDialog, NO, OK


class TestPopupSave(unittest.TestCase):

    def _make_mock_file_dialog(self, return_value):
        m = mock.Mock(spec=FileDialog)
        m.open.return_value = return_value
        m.path = 'mock'
        return m

    def test_popup_save_with_user_ok(self):
        with mock.patch('pyface.api.FileDialog') as fd:
            fd.return_value = self._make_mock_file_dialog(OK)
            from tvtk.pyface.utils import popup_save
            x = popup_save()

        self.assertEqual(x, 'mock')

    def test_popup_save_with_user_not_ok(self):
        with mock.patch('pyface.api.FileDialog') as fd:
            fd.return_value = self._make_mock_file_dialog(NO)
            from tvtk.pyface.utils import popup_save
            x = popup_save()

        self.assertEqual(x, '')


if __name__ == '__main__':
    unittest.main()
