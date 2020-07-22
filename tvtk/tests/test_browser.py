import unittest

from tvtk.api import tvtk
from tvtk.pipeline.browser import (SimpleTreeGenerator, FullTreeGenerator,
                                   PipelineBrowser)


class TestSimpleTreeGenerator(unittest.TestCase):
    def setUp(self):
        self.cs = cs = tvtk.ConeSource()
        self.ef = ef = tvtk.ElevationFilter(input_connection=cs.output_port)
        self.m = m = tvtk.PolyDataMapper(input_connection=ef.output_port)
        self.a = tvtk.Actor(mapper=m)
        self.ren = tvtk.Renderer()
        self.ren.add_actor(self.a)
        self.renwin = tvtk.RenderWindow()
        self.renwin.add_renderer(self.ren)

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
        self.assertEqual(tg.has_children(self.ren), True)
        self.assertEqual(tg.has_children(self.renwin), True)

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

        kids = tg.get_children(self.ren)
        self.assertEqual(len(kids), 2)
        self.assertEqual(kids['view_props'][0], self.a)
        self.assertEqual(len(kids['view_props']), 1)
        self.assertTrue(kids['active_camera'].is_a('vtkCamera'))

        kids = tg.get_children(self.renwin)
        self.assertEqual(len(kids), 1)
        self.assertEqual(kids['renderers'][0], self.ren)


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
        self.assertEqual(tg.has_children(self.ren), True)
        self.assertEqual(tg.has_children(self.renwin), True)

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

        kids = tg.get_children(self.ren)
        self.assertTrue(len(kids) in [6, 7, 8])
        self.assertEqual(kids['view_props'][0], self.a)
        self.assertEqual(len(kids['view_props']), 1)
        self.assertTrue(kids['active_camera'].is_a('vtkCamera'))

        kids = tg.get_children(self.renwin)
        self.assertTrue(len(kids) > 0 and len(kids) < 3)
        self.assertEqual(kids['renderers'][0], self.ren)

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


class TestPipelineBrowser(unittest.TestCase):
    def test_simple_usage(self):
        # Given
        cs = tvtk.ConeSource()
        ef = tvtk.ElevationFilter(input_connection=cs.output_port)

        # When
        p = PipelineBrowser(root_object=[ef])

        # Then
        self.assertEqual(len(p._root.children), 1)
        kids = list(p._root.children)
        self.assertEqual(kids[0].name, 'ElevationFilter')
        gk = list(kids[0].children)
        self.assertEqual(len(gk), 1)
        self.assertEqual(gk[0].name, 'ConeSource')
        ggk = list(gk[0].children)
        self.assertEqual(len(ggk), 0)

        # Check if the default traits_view returns correctly.
        p.default_traits_view()

        # When
        # Check if editing a selected object fires a ui change.
        self.count = 0

        def callback():
            self.count += 1

        p.on_trait_change(callback, 'object_edited')
        p._on_select(gk[0])
        cs.height = 2.0

        # Then
        self.assertTrue(self.count > 0)


if __name__ == '__main__':
    unittest.main()
