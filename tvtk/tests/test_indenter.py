"""Tests for indenter.py."""

# Author: Prabhu Ramachandran
# License: BSD style
# Copyright (c) 2004-2020, Enthought, Inc.

import unittest
try:
    import cStringIO
except ImportError:
    import io as cStringIO

from tvtk import indenter


class TestIndent(unittest.TestCase):
    def test_basic(self):
        """Simple tests for indenter."""
        id = indenter.Indent()
        self.assertEqual(str(id), '')
        id.incr()
        self.assertEqual(str(id), '    ')
        id.incr()
        self.assertEqual(str(id), '        ')
        id.decr()
        self.assertEqual(str(id), '    ')
        id.decr()
        self.assertEqual(str(id), '')
        id.incr(); id.incr()
        id.reset()
        self.assertEqual(str(id), '')

    def test_format(self):
        """Tests if formatting works ok."""
        id = indenter.Indent()
        id.incr()
        # test one liner with trailing newlines
        txt = """class foo:\n\n   \n   \n"""
        t1 = id.format(txt)
        self.assertEqual(t1, '    class foo:\n')
        # test one liner with no trailing newline.
        txt = """class foo:"""
        t1 = id.format(txt)
        self.assertEqual(t1, '    class foo:\n')

        # test multi-line text.
        txt = """print("hi!")
        if name == 'hi':
            print("hi, hi!")
        """
        res = """    print("hi!")\n    if name == 'hi':\n        print("hi, hi!")\n"""
        self.assertEqual(id.format(txt), res)

        txt = """
        class Foo:
            def __init__(self):
                pass
            def _get_a(self):
                return self._a"""
        res = """    class Foo:
        def __init__(self):
            pass
        def _get_a(self):
            return self._a""" + '\n'
        self.assertEqual(id.format(txt), res)


class TestVTKDocMassager(unittest.TestCase):
    def test_doc_massage(self):
        """Test massage method."""
        doc = "This is a test.  All VTK classes and vtk classes\n"\
              "are named like this: vtkActor, vtkLODProperty,\n"\
              "vtkXMLDataReader, vtk3DSImporter etc.  The methods \n"\
              "of a VTK object are like GetData, GetOutput, \n"\
              "SetRepresentationToWireframe.  Ivars are named like\n"\
              "SpecularColor, Write3DPropsAsRasterImage etc."
        ret = "This is a test.  All VTK classes and vtk classes\n"\
              "are named like this: Actor, LODProperty,\n"\
              "XMLDataReader, ThreeDSImporter etc.  The methods \n"\
              "of a VTK object are like get_data, get_output, \n"\
              "set_representation_to_wireframe.  Ivars are named like\n"\
              "specular_color, write3d_props_as_raster_image etc."
        dm = indenter.VTKDocMassager()
        self.assertEqual(dm.massage(doc), ret)

    def test_rename_class(self):
        """Test if VTK classes are renamed correctly."""
        dm = indenter.VTKDocMassager()
        t = 'vtkFooBar vtkXMLDataReader vtk3DSReader vtk2000Bug'
        r = dm._rename_class(t)
        correct = 'FooBar XMLDataReader ThreeDSReader Two000Bug'
        self.assertEqual(r, correct)

    def test_remove_sig(self):
        """Test if function signature is removed correctly."""
        dm = indenter.VTKDocMassager()
        t = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
            'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
            'V.GetOutput() -> vtkStructuredPoints\n'\
            'C++: vtkStructuredPoints *GetOutput ();\n\n'\
            ' Set/Get the output of this reader.\n'
        r = dm._remove_sig(t)
        correct = ' Set/Get the output of this reader.\n'
        self.assertEqual(r, correct)
        t = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
            'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
            'V.GetOutput() -> vtkStructuredPoints\n'\
            'C++: vtkStructuredPoints *GetOutput ();\n\n'
        r = dm._remove_sig(t)
        correct = ''
        self.assertEqual(r, correct)

    def test_class_doc(self):
        """Test if class docs are generated correctly."""
        dm = indenter.VTKDocMassager()
        indent = indenter.Indent()
        out = cStringIO.StringIO()
        doc = "vtkLODProperty, vtkXMLDataReader, vtk3DSImporter\n"\
              "SetRepresentationToWireframe, Write3DPropsAsRasterImage"
        dm.write_class_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        correct = '''    r"""
    LODProperty, XMLDataReader, ThreeDSImporter
    set_representation_to_wireframe, write3d_props_as_raster_image
    """\n'''
        self.assertEqual(ret, correct)

        # Test empty doc
        out = cStringIO.StringIO()
        doc = ""
        dm.write_class_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        self.assertEqual(ret, '    r"""\n    \n    """\n')

    def test_trait_doc(self):
        """Test if trait docs are generated correctly."""
        dm = indenter.VTKDocMassager()
        indent = indenter.Indent()
        out = cStringIO.StringIO()
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'\
              'vtkLODProperty, vtkXMLDataReader, vtk3DSImporter\n'\
              'SetRepresentationToWireframe, Write3DPropsAsRasterImage'
        dm.write_trait_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        correct = '''    r"""
    LODProperty, XMLDataReader, ThreeDSImporter
    set_representation_to_wireframe, write3d_props_as_raster_image
    """\n'''
        self.assertEqual(ret, correct)

        # Test empty doc.
        out = cStringIO.StringIO()
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'
        dm.write_trait_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        self.assertEqual(ret, '    r"""\n    \n    """\n')

    def test_method_doc(self):
        """Test if method docs are generated correctly."""
        dm = indenter.VTKDocMassager()
        indent = indenter.Indent()
        out = cStringIO.StringIO()
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'\
              'vtkLODProperty, vtkXMLDataReader, vtk3DSImporter\n'\
              'SetRepresentationToWireframe, Write3DPropsAsRasterImage'
        dm.write_method_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        correct = '''    r"""
    V.get_output(int) -> StructuredPoints
    V.get_output() -> StructuredPoints

    LODProperty, XMLDataReader, ThreeDSImporter
    set_representation_to_wireframe, write3d_props_as_raster_image
    """\n'''
        self.assertEqual(ret, correct)

        # Test empty doc.
        out = cStringIO.StringIO()
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'
        dm.write_method_doc(doc, out, indent)
        out.seek(0)
        ret = out.read()
        correct = '''    r"""
    V.get_output(int) -> StructuredPoints
    V.get_output() -> StructuredPoints
    """\n'''
        self.assertEqual(ret, correct)

        # Test doc with escape characters in it. xref: enthought/mayavi#1130
        out = cStringIO.StringIO()
        doc = r"""
GetProminentComponentValues(self, comp:int,
    values:vtkVariantArray, uncertainty:float=1.e-6,
    minimumProminence:float=1.e-3) -> None
C++: virtual void GetProminentComponentValues(int comp,
    vtkVariantArray *values, double uncertainty=1.e-6,
    double minimumProminence=1.e-3)

Populate the given vtkVariantArray with a set of distinct values.
In practice, $N >= \frac{5}{P}\mathrm{ln}\left(\frac{1}{PU}\right)$
""".lstrip()
        dm.write_method_doc(doc, out, indent)
        ret = out.getvalue()
        correct = '''    r"""
    GetProminentComponentValues(self, comp:int,
    values:VariantArray, uncertainty:float=1.e-6,
    minimumProminence:float=1.e-3) -> None
     virtual void GetProminentComponentValues(int comp,
    VariantArray *values, double uncertainty=1.e-6,
    double minimumProminence=1.e-3)

    Populate the given VariantArray with a set of distinct values.
    In practice, $N >= \\frac{5}{P}\\mathrm{ln}\\left(\\frac{1}{PU}\\right)$
    """\n'''
        self.assertEqual(ret, correct)
        # Check that ret is a valid representation of a string. This
        # will raise a DeprecationWarning if ret still contains invalid
        # escape sequences.
        self.assertIsInstance(eval(ret), str)

    def test_get_method_doc(self):
        """Test if get_method_doc works correctly."""
        dm = indenter.VTKDocMassager()
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'\
              'vtkLODProperty, vtkXMLDataReader, vtk3DSImporter\n'\
              'SetRepresentationToWireframe, Write3DPropsAsRasterImage'
        ret = dm.get_method_doc(doc)
        correct = 'get_output(int) -> StructuredPoints\n'\
                  'get_output() -> StructuredPoints\n\n'\
                  'LODProperty, XMLDataReader, ThreeDSImporter\n'\
                  'set_representation_to_wireframe, '\
                  'write3d_props_as_raster_image'
        self.assertEqual(ret, correct)

        # Test empty doc (only signature exists).
        doc = 'V.GetOutput(int) -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput (int idx);\n'\
              'V.GetOutput() -> vtkStructuredPoints\n'\
              'C++: vtkStructuredPoints *GetOutput ();\n\n'
        ret = dm.get_method_doc(doc)
        correct = 'get_output(int) -> StructuredPoints\n'\
                  'get_output() -> StructuredPoints\n'
        self.assertEqual(ret, correct)


if __name__ == "__main__":
    unittest.main()
