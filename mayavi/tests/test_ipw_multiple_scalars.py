import unittest

from numpy import zeros, random
from tvtk.api import tvtk
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.core.null_engine import NullEngine
from mayavi.modules.image_plane_widget import ImagePlaneWidget

class TestIPWMultipleScalars(unittest.TestCase):
    def setUp(self):
        # Create dataset with multiple scalars.
        arr1 = zeros(27, 'f')
        for n in range(27):
            arr1[n] = (1+float(n))/10.0
        arr2 = (arr1 + 1).astype('d')
        arr3 = arr1 + 2.0*(0.5 - random.random(27))
        arr3 = arr3.astype('f')

        p = tvtk.ImageData(dimensions=[3,3,3],spacing=[1,1,1])
        p.point_data.scalars = arr1
        p.point_data.scalars.name = 'first'
        j2 = p.point_data.add_array(arr2)
        p.point_data.get_array(j2).name='second'
        j3 = p.point_data.add_array(arr3)
        p.point_data.get_array(j3).name='third'
        self.img = p
        self.first = arr1
        self.second = arr2
        self.third = arr3

        # Setup the mayavi pipeline.
        e = NullEngine()
        e.start()
        e.new_scene()
        self.e = e

        src = VTKDataSource(data=p)
        e.add_source(src)
        self.src = src
        ipw = ImagePlaneWidget()
        e.add_module(ipw)
        self.ipw = ipw

    def tearDown(self):
        self.e.stop()
        return

    def test_ipw(self):
        """Test the image plane widget."""
        arr1, arr2, arr3 = self.first, self.second, self.third
        ipw = self.ipw.ipw
        
        scalars = ipw.input.point_data.scalars

        r = scalars.range
        expect = min(arr1), max(arr1)
        self.assertEqual(r, expect)
        o = self.src.outputs[0]
        o.update_traits()
        st = ipw.input.scalar_type_as_string
        self.assertEqual(scalars.data_type, 10)
        self.assertEqual(st, 'float')

        self.src.point_scalars_name = 'second'
        scalars = ipw.input.point_data.scalars
        r = scalars.range
        expect = min(arr2), max(arr2)
        self.assertEqual(r, expect)
        o.update_traits()
        st = ipw.input.scalar_type_as_string
        self.assertEqual(scalars.data_type, 11)
        self.assertEqual(st, 'double')

        self.src.point_scalars_name = 'third'
        scalars = ipw.input.point_data.scalars
        r = scalars.range
        expect = min(arr3), max(arr3)
        self.assertEqual(r, expect)
        o.update_traits()
        st = ipw.input.scalar_type_as_string
        self.assertEqual(scalars.data_type, 10)
        self.assertEqual(st, 'float')

if __name__ == '__main__':
    unittest.main()
