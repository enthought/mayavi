"""Tests for wrapper_gen.py.

The helper methods are checked directly; the emitters are checked by
generating wrappers for a handful of classes, which is what the build does
for all of them.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) Prabhu Ramachandran, Enthought, Inc.
# License: BSD Style.

import os
import shutil
import tempfile
import unittest
import vtk

from tvtk import wrapper_gen
from tvtk.code_gen import TVTKGenerator

_cache = wrapper_gen.WrapperGenerator()

# One class per emitter path: toggle and state traits (Property), the
# input/output plumbing (ContourFilter, Glyph3D), array arguments (PolyData,
# CellArray), a `special_traits` file name (XMLPolyDataReader) and a scalar
# type (ImageReslice).  Their ancestors come along for free, so this covers
# roughly four times as many classes as it names.
GENERATED_CLASSES = [
    'vtkActor', 'vtkAppendPolyData', 'vtkCamera', 'vtkCellArray',
    'vtkContourFilter', 'vtkGlyph3D', 'vtkImageData', 'vtkImageReslice',
    'vtkLookupTable', 'vtkOpenGLRenderer', 'vtkPlaneWidget', 'vtkPolyData',
    'vtkPolyDataMapper', 'vtkPolyDataNormals', 'vtkProperty',
    'vtkRenderWindow', 'vtkScalarBarActor', 'vtkStreamTracer',
    'vtkStructuredGrid', 'vtkTextProperty', 'vtkTransform',
    'vtkUnstructuredGrid', 'vtkVolumeProperty', 'vtkXMLPolyDataReader',
]


class TestWrapperGenerator(unittest.TestCase):
    def setUp(self):
        self.wg = _cache

    def test_find_type(self):
        wg = self.wg
        sigs = ['int', 'vtkOpenGLVolumeMapper',
                ('int', 'int', 'float', 'list'),
                ('int', 'vtkActor', 'vtkXMLReader'),
                ['vtkImageActor', 'vtkExporter'],
                ['int', 'vtkDataArray', 'vtkCellArray',
                 'vtkIdTypeArray']
                ]
        expect = ['basic', 'vtk', 'basic', 'vtk', 'vtk', 'array']
        for i, sig in enumerate(sigs):
            self.assertEqual(expect[i], wg._find_type(sig))

    def test_sig_types(self):
        wg = self.wg
        meths = [vtk.vtkProperty.GetColor,
                 vtk.vtkProperty.GetRepresentation,
                 vtk.vtkStructuredPointsReader.GetOutput,
                 vtk.vtkPolyData.SetPoints,
                 vtk.vtkPolyData.SetPolys,
                 vtk.vtkQuad.CellBoundary,
                 vtk.vtkContourFilter.SetLocator
                 ]
        expect = [('basic', 'basic'),
                  ('basic', None),
                  ('vtk', 'basic'),
                  ('basic', 'array'),
                  ('basic', 'array'),
                  ('basic', 'array'),
                  ('basic', 'vtk'),
                  ]
        for i, meth in enumerate(meths):
            sig = wg.parser.get_method_signature(meth)
            self.assertEqual(expect[i], wg._find_sig_type(sig))
        sig = [(['int'], ['int']),
               (['vtkStructuredPoints'], ['vtkFooClass'])]
        self.assertEqual(('vtk', 'vtk'), wg._find_sig_type(sig))

    def test_unicode_return_value(self):
        wg = self.wg
        meth = vtk.vtkDelimitedTextReader.GetUTF8RecordDelimiters
        expect = 'unicode' if '-> unicode' in meth.__doc__ else 'string'
        sig = wg.parser.get_method_signature(meth)
        self.assertEqual(sig[0][0][0], expect)


class TestGeneratedCode(unittest.TestCase):
    """Check the code the generator emits, not just its helpers."""

    @classmethod
    def setUpClass(cls):
        # ~0.2s for the whole list, so generate once and read the output
        # in each test
        cls.tmp_dir = tempfile.mkdtemp()
        gen = TVTKGenerator(cls.tmp_dir)
        gen.write_wrapper_classes(GENERATED_CLASSES)
        cls.sources = {}
        for name in os.listdir(gen.out_dir):
            if name.endswith('.py'):
                with open(os.path.join(gen.out_dir, name),
                          encoding='utf-8') as fh:
                    cls.sources[name] = fh.read()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_dir)

    def test_compiles(self):
        self.assertGreater(len(self.sources), len(GENERATED_CLASSES))
        for name, source in self.sources.items():
            with self.subTest(name):
                compile(source, name, 'exec')

    def test_ancestors_are_generated(self):
        # write_wrapper_classes pulls in the ancestors so that
        # _updateable_traits_ can be assembled
        self.assertIn('object.py', self.sources)
        self.assertIn('class Property(Object):', self.sources['property.py'])

    def test_toggle_and_state_traits(self):
        source = self.sources['property.py']
        self.assertIn('edge_visibility = tvtk_base.false_bool_trait(',
                      source)
        self.assertIn('representation = tvtk_base.RevPrefixMap(', source)
        self.assertIn('_updateable_traits_', source)

    def test_input_output_methods(self):
        self.assertIn('def _get_input(self):',
                      self.sources['contour_filter.py'])

    def test_special_trait(self):
        self.assertIn('file_name = tvtk_base.vtk_file_name(',
                      self.sources['xml_reader.py'])


if __name__ == "__main__":
    unittest.main()
