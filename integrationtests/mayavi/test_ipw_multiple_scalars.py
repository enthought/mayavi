
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2009,  Prabhu Ramachandran
# License: BSD Style.

# Local imports.
from common import TestCase
from numpy import zeros, random
from tvtk.api import tvtk


class TestIPWMultipleScalars(TestCase):

    """Tests the IPW with multiple scalars.  We have this in addition to
    the unittests since some of these errors only show up when the view
    is active."""

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.vtk_data_source import VTKDataSource
        from mayavi.modules.api import ImagePlaneWidget

        # Create dataset with multiple scalars.
        arr1 = zeros(27, 'f')
        for n in range(27):
            arr1[n] = (1+float(n))/10.0
        arr2 = (arr1 + 1).astype('d')
        arr3 = arr1 + 2.0*(0.5 - random.random(27))
        arr3 = arr3.astype('f')

        p = tvtk.ImageData(dimensions=[3,3,3], spacing=[1,1,1])

        p.point_data.scalars = arr1
        p.point_data.scalars.name = 'first'
        j2 = p.point_data.add_array(arr2)
        p.point_data.get_array(j2).name='second'
        j3 = p.point_data.add_array(arr3)
        p.point_data.get_array(j3).name='third'

        # Make the pipeline.
        self.new_scene()
        src = VTKDataSource(data=p)
        script.add_source(src)
        ipw = ImagePlaneWidget()
        script.add_module(ipw)

        # Test.
        ipw = ipw.ipw
        scalars = ipw.input.point_data.scalars
        r = scalars.range
        expect = min(arr1), max(arr1)
        assert r == expect
        o = src.outputs[0]
        o.update_traits()

        src.point_scalars_name = 'second'
        scalars = ipw.input.point_data.scalars
        r = scalars.range
        expect = min(arr2), max(arr2)
        assert r == expect
        o.update_traits()

        src.point_scalars_name = 'third'
        scalars = ipw.input.point_data.scalars
        r = scalars.range
        expect = min(arr3), max(arr3)
        assert r == expect
        o.update_traits()


if __name__ == '__main__':
    t = TestIPWMultipleScalars()
    t.test()
