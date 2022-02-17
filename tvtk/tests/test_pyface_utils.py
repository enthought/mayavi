import unittest
from unittest.mock import Mock, patch
from traits.etsconfig.api import ETSConfig

from pyface.api import FileDialog, NO, OK


class TestPopupSave(unittest.TestCase):

    def _make_mock_file_dialog(self, return_value):
        m = Mock(spec=FileDialog)
        m.open.return_value = return_value
        m.path = 'mock'
        return m

    @unittest.skipIf(ETSConfig.toolkit == 'null',
                     'Test meaningless with null toolkit.')
    def test_popup_save_with_user_ok(self):
        with patch('pyface.api.FileDialog') as fd:
            fd.return_value = self._make_mock_file_dialog(OK)
            from tvtk.pyface.utils import popup_save
            x = popup_save()

        self.assertEqual(x, 'mock')

    @unittest.skipIf(ETSConfig.toolkit == 'null',
                     'Test meaningless with null toolkit.')
    def test_popup_save_with_user_not_ok(self):
        with patch('pyface.api.FileDialog') as fd:
            fd.return_value = self._make_mock_file_dialog(NO)
            from tvtk.pyface.utils import popup_save
            x = popup_save()

        self.assertEqual(x, '')


if __name__ == '__main__':
    unittest.main()
