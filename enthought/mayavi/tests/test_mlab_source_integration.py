"""
Test for the various mlab source functions. 

These tests are higher level than the tests testing directly the
MlabSource subclasses. They are meant to capture errors in the formatting
of the input arguments.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest
import numpy as N

from enthought.mayavi.tools import sources

################################################################################
# `BaseTestSource`
################################################################################ 
class BaseTestSource(unittest.TestCase):
    def setUp(self):
        return


    def tearDown(self):
        return


    def all_close(self, a, b):
        """ Similar to numpy's allclose, but works also for a=None.
        """
        if None in (a, b):
            self.assert_(a==b)
        else:
            self.assert_(N.allclose(a, a))


    def check_positions(self, source, x, y, z):
        """ Check that the position vectors of the source do correspond
            to the given input positions 
        """
        self.assert_(N.allclose(source.mlab_source.x, x))
        self.assert_(N.allclose(source.mlab_source.y, y))
        self.assert_(N.allclose(source.mlab_source.z, z))


    def check_vectors(self, source, u, v, w):
        """ Check that the vector data corresponds to the given arrays.
        """
        self.all_close(source.mlab_source.u, u)
        self.all_close(source.mlab_source.v, v)
        self.all_close(source.mlab_source.w, w)


    def check_scalars(self, source, s):
        """ Check that the scalar data corresponds to the given array.
        """
        self.all_close(source.mlab_source.scalars, s)


################################################################################
# `TestScalarScatter`
################################################################################ 
class TestScalarScatter(BaseTestSource):

    def test_input_args(self):
        """ Check that scalar_scatter can take different input arguments """

        # Check for a single number as position vectors.
        ss = sources.scalar_scatter(0, 0, 0, figure=None)
        self.check_positions(ss, 0, 0, 0)
        self.check_scalars(ss, None)
        self.check_vectors(ss, None, None, None)

        # Check for a single number as scalar data, and no position
        # vectors.
        ss = sources.scalar_scatter(0, figure=None)
        self.check_positions(ss, 0, 0, 0)
        self.check_scalars(ss, 0)
        self.check_vectors(ss, None, None, None)

        # Check for a list as position vectors.
        ss = sources.scalar_scatter([0, 1], [0, 1], [0, 1], figure=None)
        self.check_positions(ss, [0, 1], [0, 1], [0, 1])
        self.check_scalars(ss, None)
        self.check_vectors(ss, None, None, None)

        # Check for a list as scalar data, and no position vectors.
        ss = sources.scalar_scatter([0, 1], figure=None)
        self.check_scalars(ss, [0, 1])
        self.check_vectors(ss, None, None, None)

        # Check for a 1D array as position vectors.
        a = N.array([0, 1])
        ss = sources.scalar_scatter(a, a, a, figure=None)
        self.check_positions(ss, a, a, a)
        self.check_scalars(ss, None)
        self.check_vectors(ss, None, None, None)

        # Check for a 1D array as a scalar data, and no position vectors.
        ss = sources.scalar_scatter(a, figure=None)
        self.check_scalars(ss, a)
        self.check_vectors(ss, None, None, None)

        # Check for a 2D array as position vectors.
        a = N.array([[0, 1], [2, 3]])
        ss = sources.scalar_scatter(a, a, a, figure=None)
        self.check_positions(ss, a, a, a)
        self.check_scalars(ss, None)
        self.check_vectors(ss, None, None, None)

        # Check for a 2D array as scalar data, and no position vectors.
        ss = sources.scalar_scatter(a, figure=None)
        self.check_scalars(ss, a)
        self.check_vectors(ss, None, None, None)

        # Check for a 2D array as scalar data, and no position vectors.
        ss = sources.scalar_scatter(a, figure=None)
        self.check_scalars(ss, a)
        self.check_vectors(ss, None, None, None)


################################################################################
# `TestVectorScatter`
################################################################################ 
class TestVectorScatter(BaseTestSource):

    def test_input_args(self):
        """ Check that vector_scatter can take different input arguments """

        # Check for a single number as a position vector.
        ss = sources.vector_scatter(0, 0, 0, 0, 0, 0, figure=None)
        self.check_positions(ss, 0, 0, 0)
        self.check_scalars(ss, None)
        self.check_vectors(ss, 0, 0, 0)

        # Check for no position vectors, and single numbers for vector
        # data.
        ss = sources.vector_scatter(0, 0, 0, figure=None)
        self.check_positions(ss, 0, 0, 0)
        self.check_scalars(ss, None)
        self.check_vectors(ss, 0, 0, 0)

        # Check for a list as a position vector.
        ss = sources.vector_scatter([0, 1], [0, 1], [0, 1], 
                                    [0, 1], [0, 1], [0, 1], figure=None)
        self.check_positions(ss, [0, 1], [0, 1], [0, 1])
        self.check_scalars(ss, None)
        self.check_vectors(ss, [0, 1], [0, 1], [0, 1])

        # Check for a lists as a vector data, and no position vectors
        ss = sources.vector_scatter([0, 1], [0, 1], [0, 1], figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, [0, 1], [0, 1], [0, 1])

        # Check for a 1D array as a position vector.
        a = N.array([0, 1])
        ss = sources.vector_scatter(a, a, a, a, a, a, figure=None)
        self.check_positions(ss, a, a, a)
        self.check_scalars(ss, None)
        self.check_vectors(ss, a, a, a)

        # Check for a 1D array as vector data, and no position vectors.
        ss = sources.vector_scatter(a, a, a, figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, a, a, a)

        # Check for a 2D array as a position vector.
        a = N.array([[0, 1], [2, 3]])
        ss = sources.vector_scatter(a, a, a, a, a, a, figure=None)
        self.check_positions(ss, a, a, a)
        self.check_scalars(ss, None)
        self.check_vectors(ss, a, a, a)

        # Check for a 2D array as vector data, and no position vectors.
        ss = sources.vector_scatter(a, a, a, figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, a, a, a)

        # Check for a 3D array as a position vector.
        x, y, z = N.mgrid[0:3, 0:3, 0:3]
        ss = sources.vector_scatter(x, y, z, x, y, z, figure=None)
        self.check_positions(ss, x, y, z)
        self.check_scalars(ss, None)
        self.check_vectors(ss, x, y, z)

        # Check for a 3D array as vector data, and no position vectors.
        x, y, z = N.mgrid[0:3, 0:3, 0:3]
        ss = sources.scalar_scatter(z, figure=None)
        self.check_scalars(ss, z)
        X, Y, Z = N.indices(z.shape)
        self.check_positions(ss, X, Y, Z)


################################################################################
# `TestArray2DSource`
################################################################################ 
class TestArray2DSource(BaseTestSource):

    def test_input_args(self):
        """ Check that array2d_source can take different input arguments """
        
        # Check for a single number as data and no position arrays.
        ss = sources.array2d_source(0, figure=None)
        self.check_scalars(ss, 0)

        # Check for a list as data, and no position arrays.
        ss = sources.array2d_source([0, 1], figure=None)
        self.check_scalars(ss, [0, 1])

        # Check for a 1D array as data, and no position arrays.
        a = N.array([0, 1])
        ss = sources.array2d_source(a, figure=None)
        self.check_scalars(ss, a)

        # Check for a 2D array as data, and no position arrays.
        a = N.array([[0, 1], [2, 3]])
        ss = sources.array2d_source(a, figure=None)
        self.check_scalars(ss, a)

        # Check for 2 lists as positions vectors, and a 2D list as data
        x = [0, 1]
        y = [0, 1]
        s = [[0, 1], [2, 3]]
        ss = sources.array2d_source(x, y, s, figure=None)
        self.check_scalars(ss, s)

        # Check for an ogrid as position vectors, and a function for the
        # scalars
        x, y = N.ogrid[-3:3, -3:3]
        f = lambda x, y: x**2 + y**2
        ss = sources.array2d_source(x, y, f, figure=None)
        self.check_scalars(ss, f(x, y))

        # Check for an mgrid as position vectors, and a 2D array for the
        # scalars
        x, y = N.mgrid[-3:3, -3:3]
        s = N.zeros_like(x)
        ss = sources.array2d_source(x, y, x, figure=None)
        self.check_scalars(ss, s)


################################################################################
# `TestScalarField`
################################################################################ 
class TestScalarField(BaseTestSource):

    def test_input_args(self):
        """ Check that scalar_field can take different input arguments """
        
        # Check for 2D arrays as positions vectors, and a function for
        # the data
        f = lambda x, y, z: x**2 + y**2
        x, y = N.mgrid[-3:3, -3:3]
        z = N.zeros_like(x)
        ss = sources.scalar_field(x, y, z, f, figure=None)
        self.check_positions(ss, x, y, z)
        s = f(x, y, z)
        self.check_scalars(ss, s)

        # Check for a 2D array as data, and no position vectors
        s = N.random.random((10, 10))
        ss = sources.scalar_field(s, figure=None)
        self.check_scalars(ss, s)

        # Check for a 3D array as data, and no position vectors
        s = N.random.random((10, 10, 10))
        ss = sources.scalar_field(s, figure=None)
        self.check_scalars(ss, s)

        # Check for a 3D array as data, and 3D arrays as position
        x, y, z = N.mgrid[-3:3, -3:3, -3:3]
        ss = sources.scalar_field(x, y, z, z, figure=None)
        self.check_positions(ss, x, y, z)
        self.check_scalars(ss, z)


################################################################################
# `TestVectorField`
################################################################################ 
class TestVectorField(BaseTestSource):

    def test_input_args(self):
        """ Check that vector_field can take different input arguments """
        
        # Check for 2D arrays as positions vectors, and a function for
        # the data
        x, y = N.mgrid[-3:3, -3:3]
        z = N.zeros_like(x)
        def f(x, y, z):
            return y, z, x
        ss = sources.vector_field(x, y, z, f, figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, y, z, x)

        # Check for a 2D array as data, and no position vectors
        u = N.random.random((10, 10))
        v = N.random.random((10, 10))
        w = N.random.random((10, 10))
        ss = sources.vector_field(u, v, w, figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, u, v, w)

        # Check for a 3D array as data, and no position vectors
        u = N.random.random((10, 10, 10))
        v = N.random.random((10, 10, 10))
        w = N.random.random((10, 10, 10))
        ss = sources.vector_field(u, v, w, figure=None)
        self.check_scalars(ss, None)
        self.check_vectors(ss, u, v, w)

        # Check for a 3D array as data, and 3D arrays as position
        x, y, z = N.mgrid[-3:3, -3:3, -3:3]
        ss = sources.vector_field(x, y, z, y, z, x, figure=None)
        self.check_scalars(ss, None)
        self.check_positions(ss, x, y, z)
        self.check_vectors(ss, y, z, x)

################################################################################
# `TestLineSource`
################################################################################ 
class TestLineSource(BaseTestSource):

    def test_input_args(self):
        """ Check that vector_field can take different input arguments """

        # Check for numbers as position vectors
        ss = sources.line_source(0, 0, 0, figure=None)
        self.check_positions(ss, 0, 0, 0)
        self.check_scalars(ss, None)

        # Check for lists as position vectors and as data
        ss = sources.line_source([0, 1], [0, 1], [0, 1], [2, 3], figure=None)
        self.check_positions(ss, [0, 1], [0, 1], [0, 1])
        self.check_scalars(ss, [2, 3])

        # Check for arrays as position vectors and a function as data
        x, y, z = N.random.random((3, 10))
        f = lambda x, y, z: x + y + z
        ss = sources.line_source(x, y, z, f, figure=None)
        self.check_positions(ss, x, y, z)
        self.check_scalars(ss, f)


if __name__ == '__main__':
    unittest.main()

