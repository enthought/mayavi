# Author: Prabhu Ramachandran
# License: BSD style
# Copyright (c) 2004, Enthought, Inc.

"""Tests for vtk_parser.py.

Note that the `test_parse_all` parses every single class in
VTK-Python.  It organizes the methods and also tries to obtain the
method signature for every method in every class.  If this runs
without crashing or raising any exceptions, then it shows that the
vtk_parser will work for any VTK class.  The test will show a few VTK
error messages but they are usually harmless.

"""

import unittest
from tvtk import vtk_parser
from tvtk import vtk_module as vtk
from tvtk.common import vtk_major_version, vtk_minor_version

import time # Only used when timing.
import sys  # Only used when debugging.


# This is a little expensive to create so we cache it.
_cache = vtk_parser.VTKMethodParser()


class TestVTKParser(unittest.TestCase):
    def setUp(self):
        self.p = _cache

    def test_methods(self):
        """Check get_methods."""
        p = self.p
        meths = p.get_methods(vtk.vtkFloatArray)

        # Check if special methods are removed.
        for m in meths:
            self.assertEqual((m.find('__') == -1), True)

    def test_parse(self):
        """Check if the methods are organized correctly."""
        p = self.p
        # Simple case of a vtkObject.
        p.parse(vtk.vtkObject())
        self.assertIn(p.get_toggle_methods(),
                        [{'Debug': False, 'GlobalWarningDisplay': 1},
                        {'Debug': False, 'GlobalWarningDisplay': 0}])
        self.assertEqual(p.get_state_methods(), {})
        self.assertEqual(p.get_get_methods(), ['GetCommand', 'GetMTime'])

        # Tolerate old and new (9.2.2+)
        msg = f'{p} get_get_set_methods() dict should be (nearly) empty'
        try:
            self.assertEqual(p.get_get_set_methods(), {}, msg=msg)
        except AssertionError:
            self.assertEqual(p.get_get_set_methods(),
                             {'ObjectName': ('', None)}, msg=msg)

        res = ['AddObserver', 'BreakOnError', 'HasObserver',
               'InvokeEvent', 'IsA', 'Modified', 'NewInstance',
               'Register', 'RemoveObserver', 'RemoveObservers',
               'SafeDownCast', 'UnRegister', 'RemoveAllObservers']
        for i in p.get_other_methods():
            self.assertEqual(i in res, True)

        # Parse a fairly complex case of a vtkProperty with the same
        # parser object.
        p.parse(vtk.vtkProperty)
        self.assertEqual(p.toggle_meths, p.get_toggle_methods())
        res = {'EdgeVisibility': 0, 'BackfaceCulling': 0,
               'FrontfaceCulling': 0}
        if 'Shading' in p.get_toggle_methods():
            res['Shading'] = 0

        result = p.get_toggle_methods()
        for key in res:
            self.assertEqual(key in result, True)
            self.assertEqual(result[key], res[key])

        res = {'Interpolation': [['Gouraud', 1], ['Flat', 0],
                                 ['Gouraud', 1], ['Phong', 2]],
               'Representation': [['Surface', 2], ['Points', 0],
                                  ['Surface', 2], ['Wireframe', 1]]}
        res['Interpolation'].insert(-1, ['PBR', 3])

        self.assertEqual(p.get_state_methods(), res)
        self.assertEqual(p.state_meths, p.get_state_methods())

        obj = vtk.vtkProperty()
        if hasattr(vtk, 'VTK_LARGE_FLOAT'):
            int_max = vtk.VTK_LARGE_INTEGER
            float_max = vtk.VTK_LARGE_FLOAT
        else:
            int_max = vtk.VTK_INT_MAX
            float_max = vtk.VTK_FLOAT_MAX

        res = {'Ambient': (0.0, (0.0, 1.0)),
               'AmbientColor': ((1.0, 1.0, 1.0), None),
               'Color': ((1.0, 1.0, 1.0), None),
               'Diffuse': (1.0, (0.0, 1.0)),
               'DiffuseColor': ((1.0, 1.0, 1.0), None),
               'EdgeColor': ((1.0, 1.0, 1.0), None),
               'LineStipplePattern': (65535, None),
               'LineStippleRepeatFactor': (1, (1, int_max)),
               'LineWidth': (1.0, (0.0, float_max)),
               'Opacity': (1.0, (0.0, 1.0)),
               'PointSize': (1.0, (0.0, float_max)),
               'ReferenceCount': (1, None),
               'Specular': (0.0, (0.0, 1.0)),
               'SpecularColor': ((1.0, 1.0, 1.0), None),
               'SpecularPower': (1.0, (0.0, 100.0))}
        if ('ReferenceCount' not in p.get_get_set_methods()):
            del res['ReferenceCount']
        res['MaterialName'] = (None, None)
        res['VertexColor'] = ((0.5, 1.0, 0.5), None)
        res['EmissiveFactor'] = ((1.0, 1.0, 1.0), None)
        res['Metallic'] = (0., float_max)
        res['NormalScale'] = (1., None)
        res['OcclusionStrength'] = (1., float_max)
        res['Roughness'] = (0.5, float_max)
        if (vtk_major_version, vtk_minor_version) >= (9, 1):
            res['Anisotropy'] = (0.0, (0.0, 1.0))
            res['AnisotropyRotation'] = (0.0, (0.0, 1.0))
            res['BaseIOR'] = (1.5, (1.0, 9.999999680285692e+37))
            res['CoatColor'] = ((1.0, 1.0, 1.0), None)
            res['CoatIOR'] = (2.0, (1.0, 9.999999680285692e+37))
            res['CoatNormalScale'] = (1.0, (0.0, 1.0))
            res['CoatRoughness'] = (0.0, (0.0, 1.0))
            res['CoatStrength'] = (0.0, (0.0, 1.0))
            res['EdgeTint'] = ((1.0, 1.0, 1.0), None)
            res['SelectionColor'] = ((1.0, 0.0, 0.0, 1.0), None)
            res['SelectionLineWidth'] = (2.0, None)
            res['SelectionPointSize'] = (2.0, None)
        if (vtk_major_version, vtk_minor_version) >= (9, 3):
            res['EdgeOpacity'] = (1.0, None)

        result = list(p.get_get_set_methods().keys())
        if hasattr(obj, 'GetTexture'):
            result.remove('Texture')
        if hasattr(obj, 'GetInformation'):
            result.remove('Information')
        self.assertEqual(sorted(res.keys()), sorted(result))
        self.assertEqual(p.get_set_meths, p.get_get_set_methods())
        for x in res:
            if res[x][1]:
                # This is necessary since the returned value is not
                # usually exactly the same as defined in the header file.
                default = getattr(obj, 'Get%s' % x)()
                val = getattr(obj, 'Get%sMinValue' % x)(), \
                      getattr(obj, 'Get%sMaxValue' % x)()
                self.assertEqual(p.get_get_set_methods()[x],
                                 (default, val))

        if hasattr(obj, 'GetTexture'):
            expect = ['GetMaterial', 'GetMaterialName',
                      'GetNumberOfTextures', 'GetShaderProgram']
            if hasattr(obj, 'GetMaterialName'):
                if hasattr(obj, 'GetShaderDeviceAdapter2'):
                    expect.append('GetShaderDeviceAdapter2')
                msg = "%s not in %s"%(p.get_get_methods(), expect)
                self.assertTrue(all([x in expect for x in sorted(p.get_get_methods())]), msg)
            else:
                expect.remove('GetMaterialName')
                self.assertEqual(p.get_get_methods(), expect)
        else:
            self.assertEqual(p.get_get_methods(), [])
        self.assertEqual(p.get_meths, p.get_get_methods())

        res = ['BackfaceRender', 'DeepCopy', 'Render']
        if hasattr(obj, 'GetTexture'):
            res = ['AddShaderVariable', 'BackfaceRender', 'DeepCopy',
                   'ReleaseGraphicsResources', 'RemoveAllTextures',
                   'RemoveTexture', 'Render']
            res.extend(['SetBaseColorTexture', 'SetEmissiveTexture',
                        'SetNormalTexture', 'SetORMTexture'])
            if vtk_major_version == 9 and vtk_minor_version > 0:
                res.extend([
                    'ComputeIORFromReflectance', 'ComputeReflectanceFromIOR',
                    'ComputeReflectanceOfBaseLayer', 'SetAnisotropyTexture',
                    'SetCoatNormalTexture'
                ])

        if hasattr(obj, 'PostRender'):
            res.append('PostRender')
            res.sort()
        self.assertEqual(p.get_other_methods(), res)
        self.assertEqual(p.other_meths, p.get_other_methods())

    def test_parse_image_reslice(self):
        """Check if the vtkImageReslice is parsed correctly."""
        p = self.p
        p.parse(vtk.vtkImageReslice)
        state_meths = p.get_state_methods()
        self.assertEqual('OutputSpacing' not in state_meths, True)
        self.assertEqual('OutputOrigin' not in state_meths, True)
        self.assertEqual('OutputExtent' not in state_meths, True)

    def test_props_allocated_rendertime_is_not_a_get_set_method(self):
        p = self.p
        a = vtk.vtkActor()
        if hasattr(a, 'GetAllocatedRenderTime'):
            p.parse(vtk.vtkProp)
            self.assertFalse('AllocatedRenderTime' in p.get_get_set_methods())

    def test_method_signature(self):
        """Check if VTK method signatures are parsed correctly."""
        p = self.p

        # Simple tests.
        o = vtk.vtkProperty()
        self.assertEqual([(['string'], None)],
                         p.get_method_signature(o.GetClassName))
        if hasattr(vtk, 'vtkArrayCoordinates'):
            self.assertEqual([([('float', 'float', 'float')], None),
                              ([None], (['float', 'float', 'float'],)),
                              ([None], ('float', 'float', 'float'))],
                             p.get_method_signature(o.GetColor))
        else:
            self.assertEqual([([('float', 'float', 'float')], None),
                              ([None], (('float', 'float', 'float'),))],
                             p.get_method_signature(o.GetColor))
        if hasattr(vtk, 'vtkArrayCoordinates'):
            self.assertEqual([([None], ('float', 'float', 'float')),
                              ([None], (['float', 'float', 'float'],))],
                             p.get_method_signature(o.SetColor))

        else:
            self.assertEqual([([None], ('float', 'float', 'float')),
                              ([None], (('float', 'float', 'float'),))],
                             p.get_method_signature(o.SetColor))

        # Test vtkObjects args.
        o = vtk.vtkContourFilter()
        sig = p.get_method_signature(o.SetInputData)
        if len(sig) == 1:
            self.assertEqual([([None], ['vtkDataSet'])],
                             sig)

        self.assertEqual([(['vtkPolyData'], None),
                          (['vtkPolyData'], ['int'])],
                         p.get_method_signature(o.GetOutput))

        # Test if function arguments work.
        if vtk_major_version == 9 and vtk_minor_version > 0:
            self.assertEqual([(['int'], ('int', 'function', 'float'))],
                             p.get_method_signature(o.AddObserver))
        else:
            self.assertEqual([(['int'], ('int', 'function'))],
                             p.get_method_signature(o.AddObserver))
        # This one's for completeness.
        if ((len(p.get_method_signature(o.RemoveObserver))) == 2):
            self.assertEqual([([None], ['vtkCommand']), ([None], ['int'])],
                             p.get_method_signature(o.RemoveObserver))
        else:
            self.assertEqual([([None], ['int'])],
                             p.get_method_signature(o.RemoveObserver))


    def test_special_non_state_methods(self):
        """Check exceptional cases that are not state methods."""
        p = self.p
        p.parse(vtk.vtkDataObject)
        self.assertTrue('UpdateExtent' not in p.get_state_methods())

        p.parse(vtk.vtkImageImport)
        self.assertTrue('DataExtent' not in p.get_state_methods())
        self.assertTrue('DataExtent' in p.get_get_set_methods())

    def test_no_tree(self):
        """Check if parser is usable without the tree."""
        p = vtk_parser.VTKMethodParser(use_tree=False)
        self.assertEqual(p.get_tree(), None)
        self.p = p
        self.test_methods()
        self.test_parse()
        self.test_method_signature()

        # Now check that it really works for abstract classes.
        # abstract classes that have state methods
        abs_class = [vtk.vtkDicer, vtk.vtkMapper, vtk.vtkScalarsToColors,
                     vtk.vtkUnstructuredGridVolumeMapper,
                     vtk.vtkVolumeMapper]
        if hasattr(vtk, 'vtkXMLWriterBase'):
            abs_class.append(vtk.vtkXMLWriterBase)
        else:
            abs_class.append(vtk.vtkXMLWriter)
        if hasattr(vtk, 'vtkStreamer'):
            abs_class.append(vtk.vtkStreamer)

        for k in abs_class:
            p.parse(k)
            # Make sure we did get the state methods.
            self.assertEqual(len(p.get_state_methods()) > 0, True)

            for key, values in p.get_state_methods().items():
                for val in values:
                    # No state information is obtainable since no
                    # class tree is created.
                    self.assertTrue(val[1] in [None, 0, 1, 2])

    def test_parse_all(self):
        """Check if all VTK classes are parseable."""

        # This test is a tough one because every single class in the
        # VTK API is parsed.  A few VTK error messages (not test
        # errors) might be seen on screen but these are normal.

        # t1 = time.clock()
        p = self.p
        ignore = ['mutable', 'exc', 'kits', 'util']
        for obj in dir(vtk):
            k = getattr(vtk, obj)
            if hasattr(k, '__bases__') and obj not in ignore:
                # print(k.__name__, end=' ')
                # sys.stdout.flush()
                p.parse(k)
                for method in p.get_methods(k):
                    meth = getattr(k, method)
                    if callable(meth):
                        p.get_method_signature(meth)
        # print(time.clock() - t1, 'seconds')


if __name__ == "__main__":
    unittest.main()
