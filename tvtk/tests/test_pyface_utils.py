import mock
import unittest

from pyface.api import OK, FileDialog


class TestPopupSave(unittest.TestCase):

    def _make_mock(self):
        m = mock.Mock(spec=FileDialog)
        m.open.return_value = OK
        m.path = 'mock'
        return m

    def test_popup_save(self):
        with mock.patch('pyface.api.FileDialog') as fd:
            fd.return_value = self._make_mock()
            from tvtk.pyface.ui.qt4.scene import popup_save
            x = popup_save()

        self.assertEqual(x, 'mock')



if __name__ == '__main__':
    unittest.main()
