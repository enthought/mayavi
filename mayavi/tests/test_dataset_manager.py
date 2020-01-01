"""
Test for the dataset_manager.py module.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Enthought, Inc.
# License: BSD Style.

import unittest
import numpy as N

from tvtk.api import tvtk
from mayavi.core.dataset_manager import DatasetManager


def make_data():
    points = N.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], # tets
                    [1,0,0], [2,0,0], [1,1,0], [1,0,1],
                    [2,0,0], [3,0,0], [2,1,0], [2,0,1],
                    ], 'f')
    tets = N.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    tet_type = tvtk.Tetra().cell_type
    ug = tvtk.UnstructuredGrid(points=points)
    ug.set_cells(tet_type, tets)
    # Setup the point attributes.
    temp = N.random.random(12)
    v = N.random.randn(12, 3)
    ten = N.random.randn(12, 9)
    a = tvtk.FloatArray(name='p')
    a.from_array(N.random.randn(12))
    ug.point_data.add_array(a)
    ug.point_data.scalars = temp
    ug.point_data.scalars.name = 't'
    ug.point_data.vectors = v
    ug.point_data.vectors.name = 'v'
    ug.point_data.tensors = ten
    ug.point_data.tensors.name = 'ten'
    # Setup the cell attributes.
    temp = N.random.random(3)
    v = N.random.randn(3, 3)
    ten = N.random.randn(3, 9)
    ug.cell_data.scalars = temp
    ug.cell_data.scalars.name = 't'
    ug.cell_data.vectors = v
    ug.cell_data.vectors.name = 'v'
    ug.cell_data.tensors = ten
    ug.cell_data.tensors.name = 'ten'
    return ug


class TestDataSetManager(unittest.TestCase):
    def setUp(self):
        self.data = make_data()
        self.dm = DatasetManager(dataset=self.data)
        return

    def tearDown(self):
        return

    def test_point_arrays(self):
        "Are the point data arrays of the manager setup right?"
        dm = self.dm
        sc = sorted(dm.point_scalars.keys())
        self.assertEqual(sc, ['p', 't'])
        vec = list(dm.point_vectors.keys())
        self.assertEqual(vec, ['v'])
        ten = list(dm.point_tensors.keys())
        self.assertEqual(ten, ['ten'])

    def test_point_array_view(self):
        "Are the manager's point arrays views of the VTK data?"
        # Check that the array we have is really a view of the VTK data.
        dm = self.dm
        data = self.data
        t = dm.point_scalars['t']
        t[0] += 1.0
        self.assertEqual(t[0], data.point_data.scalars[0])

        v = dm.point_vectors['v']
        v[0][0] += 1.0
        self.assertEqual(v[0][0], data.point_data.vectors[0][0])

        ten = dm.point_tensors['ten']
        ten[0][0] += 1.0
        self.assertEqual(ten[0][0], data.point_data.tensors[0][0])

    def test_cell_arrays(self):
        "Are the cell arrays of the manager setup right?"
        dm = self.dm
        sc = list(dm.cell_scalars.keys())
        self.assertEqual(sc, ['t'])
        vec = list(dm.cell_vectors.keys())
        self.assertEqual(vec, ['v'])
        ten = list(dm.cell_tensors.keys())
        self.assertEqual(ten, ['ten'])

    def test_cell_array_view(self):
        "Are the manager's cell arrays views of the VTK data?"
        # Check that the array we have is really a view of the VTK data.
        dm = self.dm
        data = self.data
        t = dm.cell_scalars['t']
        t[0] += 1.0
        self.assertEqual(t[0], data.cell_data.scalars[0])

        v = dm.cell_vectors['v']
        v[0][0] += 1.0
        self.assertEqual(v[0][0], data.cell_data.vectors[0][0])

        ten = dm.cell_tensors['ten']
        ten[0][0] += 1.0
        self.assertEqual(ten[0][0], data.cell_data.tensors[0][0])

    def test_remove_array(self):
        "Does the remove_array method work correctly."
        dm = self.dm
        data = self.data
        dm.remove_array('t', 'point')
        self.assertEqual(len(dm.point_scalars), 1)
        self.assertEqual(list(dm.point_scalars.keys()), ['p'])
        dm.remove_array('ten', 'point')
        self.assertEqual(len(dm.point_tensors), 0)
        # Make sure the default category is point.
        dm.remove_array('v')
        self.assertEqual(len(dm.point_vectors), 0)

        # Cell arrays.
        dm.remove_array('t', 'cell')
        self.assertEqual(len(dm.cell_scalars), 0)
        dm.remove_array('ten', 'cell')
        self.assertEqual(len(dm.cell_tensors), 0)
        dm.remove_array('v', 'cell')
        self.assertEqual(len(dm.cell_vectors), 0)

    def test_rename_array(self):
        "Does array renaming work."
        dm = self.dm
        data = self.data

        dm.rename_array('ten', 'ten1', 'point')
        self.assertEqual(list(dm.point_tensors.keys()), ['ten1'])
        pd = data.point_data
        arrs = [pd.get_array_name(x) for x in
                range(pd.number_of_arrays)]
        arrs.sort()
        self.assertEqual(arrs, ['p', 't', 'ten1', 'v'])

        dm.rename_array('t', 'temp', 'cell')
        self.assertEqual(list(dm.cell_scalars.keys()), ['temp'])
        cd = data.cell_data
        arrs = [cd.get_array_name(x) for x in
                range(cd.number_of_arrays)]
        arrs.sort()
        self.assertEqual(arrs, ['temp', 'ten', 'v'])

    def test_add_array(self):
        "Does the add_array method work."
        dm = self.dm
        data = self.data
        pd = data.point_data
        cd = data.cell_data

        # Point data.
        s = N.random.randn(12)
        v = N.random.randn(12,3)
        t = N.random.randn(12, 9)
        dm.add_array(s, 'scalar')
        sc = sorted(self.dm.point_scalars.keys())
        self.assertEqual(sc, ['p', 'scalar', 't'])
        x = pd.get_array('scalar')
        self.assertNotEqual(x, None)
        dm.add_array(v, 'vector')
        vc = sorted(self.dm.point_vectors.keys())
        self.assertEqual(vc, ['v', 'vector'])
        x = pd.get_array('vector')
        self.assertNotEqual(x, None)
        dm.add_array(t, 'tensor')
        vc = sorted(self.dm.point_tensors.keys())
        self.assertEqual(vc, ['ten', 'tensor'])
        x = pd.get_array('tensor')
        self.assertNotEqual(x, None)

        # cell data.
        s = N.random.randn(3)
        v = N.random.randn(3, 3)
        t = N.random.randn(3, 9)
        dm.add_array(s, 'scalar', 'cell')
        sc = sorted(self.dm.cell_scalars.keys())
        self.assertEqual(sc, ['scalar', 't'])
        x = cd.get_array('scalar')
        self.assertNotEqual(x, None)
        dm.add_array(v, 'vector', 'cell')
        vc = sorted(self.dm.cell_vectors.keys())
        self.assertEqual(vc, ['v', 'vector'])
        x = cd.get_array('vector')
        self.assertNotEqual(x, None)
        dm.add_array(t, 'tensor', 'cell')
        vc = sorted(self.dm.cell_tensors.keys())
        self.assertEqual(vc, ['ten', 'tensor'])
        x = cd.get_array('tensor')
        self.assertNotEqual(x, None)

    def test_activate(self):
        "Does activating a particular array work."
        dm = self.dm
        data = self.dm.output

        dm.activate('p')
        self.assertEqual(data.point_data.scalars.name, 'p')
        dm.activate('t')
        self.assertEqual(data.point_data.scalars.name, 't')

        s = N.random.randn(3)
        dm.add_array(s, 'foo', 'cell')
        dm.activate('foo', 'cell')
        self.assertEqual(data.cell_data.scalars.name, 'foo')
        dm.activate('t', 'cell')
        self.assertEqual(data.cell_data.scalars.name, 't')


if __name__ == '__main__':
    unittest.main()
