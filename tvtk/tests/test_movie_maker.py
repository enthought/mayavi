import mock
import os
import shutil
import tempfile
import unittest

from tvtk.pyface.movie_maker import MovieMaker


class TestMovieMaker(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_does_nothing_when_record_is_off(self):
        # Given
        mm = MovieMaker(record=False)
        mm._save_scene = mock.MagicMock()

        # When
        mm.animation_start()
        mm.animation_step()
        mm.animation_step()
        mm.animation_stop()

        # Then
        mm._save_scene.assert_not_called()

    def test_calls_save_scene_when_record_is_on(self):
        # Given
        mm = MovieMaker(record=True)
        mm._save_scene = mock.MagicMock()

        # When
        mm.animation_start()
        mm.animation_step()
        mm.animation_step()
        mm.animation_stop()

        # Then
        self.assertEqual(mm._save_scene.call_count, 3)

    def test_calls_save_scene_with_record_movie(self):
        # Given
        mm = MovieMaker(record=False)
        mm._save_scene = mock.MagicMock()
        mm.animation_start = mock.MagicMock()
        mm.animation_stop = mock.MagicMock()

        # When
        with mm.record_movie():
            mm.animation_step()
            mm.animation_step()

        # Then
        mm.animation_start.assert_called_once_with()
        self.assertEqual(mm._save_scene.call_count, 2)
        mm.animation_stop.assert_called_once_with()
        self.assertEqual(mm.record, False)

    def test_directory_updates_correctly(self):
        # Given
        mm = MovieMaker(record=True, directory=self.root)
        mm._save_scene = mock.MagicMock()

        # When
        with mm.record_movie():
            mm.animation_step()

        # Then
        self.assertEqual(mm._subdir, 'movie001')

        # When.
        os.makedirs(os.path.join(self.root, mm._subdir, 'movie001'))
        with mm.record_movie():
            mm.animation_step()

        # Then
        self.assertEqual(mm._subdir, 'movie002')


if __name__ == '__main__':
    unittest.main()
