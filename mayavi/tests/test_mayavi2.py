"""Tests for the ``mayavi2`` command line application."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import os
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

from mayavi.core.null_engine import NullEngine
from mayavi.tests.common import get_example_data

try:
    from mayavi.plugins.script import Script
except ImportError:  # the `app` extra is not installed
    Script = None


def import_mayavi2(argv=()):
    """Import the module afresh with `argv` in place.

    It parses the command line at import time -- which is why nothing may
    import it while the real argv belongs to something else, pytest included.
    """
    with patch.object(sys, 'argv', ['mayavi2'] + list(argv)):
        sys.modules.pop('mayavi.scripts.mayavi2', None)
        import mayavi.scripts.mayavi2
        return mayavi.scripts.mayavi2


class StubApp:
    """Stand-in for MayaviApp: process_cmd_line only wants `script`."""

    def __init__(self):
        engine = NullEngine()
        engine.start()
        self.script = Script(engine=engine)


def unbind_from_main(test):
    """Undo what run_script leaves in __main__.

    It binds `mayavi` there once and skips the binding ever after, so without
    this the second test in a process would drive the first one's engine.
    """
    main = sys.modules['__main__'].__dict__
    names = ('mayavi', 'engine', '__file__')
    before = {name: main[name] for name in names if name in main}

    def restore():
        for name in names:
            main.pop(name, None)
        main.update(before)

    test.addCleanup(restore)


@unittest.skipIf(Script is None, "requires the app extra")
class TestParseCmdLine(unittest.TestCase):
    def setUp(self):
        self.mayavi2 = import_mayavi2()

    def test_string_and_list_agree(self):
        as_list = self.mayavi2.parse_cmd_line(['-d', 'foo.vtk', '-m', 'Axes'])
        self.assertEqual(as_list, self.mayavi2.parse_cmd_line('-d foo.vtk '
                                                              '-m Axes'))
        self.assertEqual(as_list[0], [('-d', 'foo.vtk'), ('-m', 'Axes')])

    def test_long_options(self):
        opts, args = self.mayavi2.parse_cmd_line(
            ['--data', 'foo.vtk', '--module', 'Axes', '--offscreen'])
        self.assertEqual(opts, [('--data', 'foo.vtk'), ('--module', 'Axes'),
                                ('--offscreen', '')])
        self.assertEqual(args, [])

    def test_trailing_arguments(self):
        self.assertEqual(self.mayavi2.parse_cmd_line(['-n', 'a.mv2'])[1],
                         ['a.mv2'])

    def test_unknown_option_exits(self):
        with self.assertRaises(SystemExit) as cm:
            self.mayavi2.parse_cmd_line(['--no-such-option'])
        self.assertEqual(cm.exception.code, 1)

    def test_usage_lists_the_options(self):
        usage = self.mayavi2.usage()
        for option in ('--data', '--module', '--filter', '--offscreen'):
            self.assertIn(option, usage)


@unittest.skipIf(Script is None, "requires the app extra")
class TestImportTimeOptions(unittest.TestCase):
    """-h, -V and -o are acted on while the module is being imported."""

    def test_help_exits_cleanly(self):
        with self.assertRaises(SystemExit) as cm:
            import_mayavi2(['-h'])
        self.assertEqual(cm.exception.code, 0)

    def test_version_exits_cleanly(self):
        with self.assertRaises(SystemExit) as cm:
            import_mayavi2(['--version'])
        self.assertEqual(cm.exception.code, 0)

    def test_offscreen(self):
        self.assertTrue(import_mayavi2(['-o', '-d', 'foo.vtk']).OFFSCREEN)
        self.assertFalse(import_mayavi2(['-d', 'foo.vtk']).OFFSCREEN)


@unittest.skipIf(Script is None, "requires the app extra")
class TestProcessCmdLine(unittest.TestCase):
    def setUp(self):
        self.mayavi2 = import_mayavi2()
        self.app = StubApp()
        self.engine = self.app.script.engine
        unbind_from_main(self)

    def run_cmd_line(self, arguments):
        opts, args = self.mayavi2.parse_cmd_line(arguments)
        self.mayavi2.process_cmd_line(self.app, opts, args)

    def test_data_module_and_filter(self):
        self.run_cmd_line(['-d', get_example_data('fieldfile.vtk'),
                           '-m', 'Outline', '-f', 'ExtractEdges',
                           '-m', 'Surface'])
        source = self.engine.scenes[0].children[0]
        self.assertEqual(len(source.children), 2)
        names = [child.__class__.__name__ for child in source.children]
        self.assertIn('ExtractEdges', names)

    def test_dotted_module_name(self):
        self.run_cmd_line(['-d', get_example_data('fieldfile.vtk'),
                           '-m', 'mayavi.modules.outline.Outline'])
        modules = self.engine.scenes[0].children[0].children[0].children
        self.assertEqual([m.__class__.__name__ for m in modules], ['Outline'])

    def test_user_defined_filter(self):
        self.run_cmd_line(['-d', get_example_data('fieldfile.vtk'),
                           '-f', 'UserDefined:CellDerivatives'])
        filters = self.engine.scenes[0].children[0].children
        self.assertEqual(filters[0].filter.class_name, 'vtkCellDerivatives')

    def test_non_file_source(self):
        self.run_cmd_line(['-d', 'ParametricSurface', '-m', 'Surface'])
        source = self.engine.scenes[0].children[0]
        self.assertEqual(source.__class__.__name__, 'ParametricSurface')

    def test_missing_file_is_reported(self):
        with self.assertLogs('mayavi', level='ERROR') as logged:
            self.run_cmd_line(['-d', 'no_such_file.vtk', '-m', 'Outline'])
        self.assertIn('does not exist', '\n'.join(logged.output))
        # the option after the bad one is not processed
        self.assertEqual(self.engine.scenes[0].children, [])

    def test_new_scene_and_module_manager(self):
        self.run_cmd_line(['-d', get_example_data('fieldfile.vtk'), '-M',
                           '-n'])
        self.assertEqual(len(self.engine.scenes), 2)
        source = self.engine.scenes[0].children[0]
        self.assertEqual(source.children[-1].__class__.__name__,
                         'ModuleManager')

    def test_set_applies_to_the_last_object(self):
        self.run_cmd_line(['-d', get_example_data('fieldfile.vtk'),
                           '-m', 'Outline', '-s', 'actor.property.opacity=0.5'])
        outline = self.engine.scenes[0].children[0].children[0].children[0]
        self.assertEqual(outline.actor.property.opacity, 0.5)

    def test_trailing_script_argument(self):
        tmp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp_dir)
        path = os.path.join(tmp_dir, 'script.py')
        with open(path, 'w') as fh:
            fh.write('mayavi.new_scene()\n')
        self.run_cmd_line([path])
        self.assertEqual(len(self.engine.scenes), 1)


@unittest.skipIf(Script is None, "requires the app extra")
class TestRunScript(unittest.TestCase):
    def setUp(self):
        self.mayavi2 = import_mayavi2()
        self.app = StubApp()
        unbind_from_main(self)
        self.tmp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp_dir)

    def write_script(self, body):
        path = os.path.join(self.tmp_dir, 'script.py')
        with open(path, 'w') as fh:
            fh.write(body)
        return path

    def test_binds_the_script_instance(self):
        path = self.write_script('mayavi.new_scene()\nassert engine is not '
                                 'None\n')
        self.assertFalse(self.mayavi2.run_script(self.app.script, path))
        self.assertEqual(len(self.app.script.engine.scenes), 1)

    def test_reports_a_failure(self):
        path = self.write_script('raise RuntimeError("boom")\n')
        # the suite re-raises what mayavi would otherwise swallow; this is the
        # one place where the swallowing itself is under test
        with patch('mayavi.core.common.reraise_exceptions', False):
            self.assertTrue(self.mayavi2.run_script(self.app.script, path))
