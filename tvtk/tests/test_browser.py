import unittest

from tvtk.api import tvtk
from tvtk.pipeline.browser import SimpleTreeGenerator, FullTreeGenerator


class TestSimpleTreeGenerator(unittest.TestCase):
    def setUp(self):
        self.cs = cs = tvtk.ConeSource()
        self.ef = ef = tvtk.ElevationFilter(input_connection=cs.output_port)
        self.m = m = tvtk.PolyDataMapper(input_connection=ef.output_port)
        self.a = tvtk.Actor(mapper=m)

    def _make_tree_generator(self):
        return SimpleTreeGenerator()

    def test_has_children_is_correct(self):
        # Given/When
        tg = self._make_tree_generator()

        # Then
        self.assertEqual(tg.has_children(self.cs), True)
        self.assertEqual(tg.has_children(self.a), True)
        self.assertEqual(tg.has_children(self.m), True)
        self.assertEqual(tg.has_children(self.ef), True)
        self.assertEqual(tg.has_children(self.a.property), False)

    def test_get_children(self):
        # Given
        tg = self._make_tree_generator()

        # When/Then
        kids = tg.get_children(self.cs)
        self.assertEqual(len(kids), 0)

        kids = tg.get_children(self.ef)
        self.assertEqual(len(kids), 1)
        self.assertEqual(list(kids.values()), [[self.cs]])

        kids = tg.get_children(self.m)
        self.assertEqual(len(kids), 2)
        self.assertEqual(kids['input'], [self.ef])
        self.assertEqual(kids['lookup_table'], self.m.lookup_table)

        kids = tg.get_children(self.a)
        self.assertEqual(len(kids), 3)
        self.assertEqual(kids['mapper'], self.m)
        self.assertEqual(kids['property'], self.a.property)
        self.assertEqual(kids['texture'], None)


class TestFullTreeGenrator(TestSimpleTreeGenerator):
    def _make_tree_generator(self):
        return FullTreeGenerator()

    def test_has_children_is_correct(self):
        # Given/When
        tg = self._make_tree_generator()

        # Then
        self.assertEqual(tg.has_children(self.cs), True)
        self.assertEqual(tg.has_children(self.a), True)
        self.assertEqual(tg.has_children(self.m), True)
        self.assertEqual(tg.has_children(self.ef), True)
        self.assertEqual(tg.has_children(self.a.property), True)

    def test_get_children(self):
        # Given
        tg = self._make_tree_generator()

        # When/Then
        kids = tg.get_children(self.cs)
        self.assertEqual(len(kids), 0)

        kids = tg.get_children(self.ef)
        self.assertEqual(len(kids), 1)
        self.assertEqual(list(kids.values()), [[self.cs]])

        kids = tg.get_children(self.m)
        self.assertEqual(len(kids), 3)
        self.assertEqual(kids['input'], [self.ef])
        self.assertEqual(kids['lookup_table'], self.m.lookup_table)

        kids = tg.get_children(self.a)
        self.assertEqual(len(kids), 7)
        self.assertEqual(kids['mapper'], self.m)
        self.assertEqual(kids['property'], self.a.property)
        self.assertEqual(kids['texture'], None)
        self.assertEqual(kids['user_transform'], None)
        self.assertEqual(kids['user_matrix'], None)

    def test_glyph_pipeline(self):
        # Given
        rta = tvtk.RTAnalyticSource()
        cs = tvtk.ConeSource()
        g = tvtk.Glyph3D(input_connection=rta.output_port)
        g.set_source_connection(cs.output_port)
        m = tvtk.PolyDataMapper(input_connection=g.output_port)

        tg = self._make_tree_generator()

        # When/Then
        kids = tg.get_children(cs)
        self.assertEqual(len(kids), 0)
        kids = tg.get_children(rta)
        self.assertEqual(len(kids), 0)

        kids = tg.get_children(g)
        self.assertEqual(len(kids), 2)
        self.assertEqual(kids['input'], [rta, cs])

        kids = tg.get_children(m)
        self.assertEqual(len(kids), 3)
        self.assertEqual(kids['input'], [g])
        self.assertEqual(kids['lookup_table'], m.lookup_table)


if __name__ == '__main__':
    unittest.main()
