#!/usr/bin/env python
""" A simple example showing an Mandelbrot set.

Author: Ilan Schnell <ischnell@enthought.com>
Copyright 2008, Enthought, Inc.
License: BSD Style.
"""
print "This script is numerically intensive and requires a lot of memory."
print "Please be patient..."

import hashlib

import numpy
from scipy import weave

from enthought.mayavi import mlab as M

M.options.backend = 'envisage'


support_code = '''
#define D 500    /* max number of iterations */

long iterations(double cr, double ci)
{
        long d = 1;
        double zr=cr, zi=ci, zr2, zi2;
        for(;;) {
                zr2 = zr * zr;
                zi2 = zi * zi;
                if( zr2+zi2 > 16.0 ) return d;
                if( ++d == D ) return D;
                zi = 2.0 * zr * zi + ci;
                zr = zr2 - zi2 + cr;
        }
}

static void
PyUFunc_0(char **args, npy_intp *dimensions, npy_intp *steps, void *func)
{
        npy_intp i, n;
        npy_intp is0 = steps[0];
        npy_intp is1 = steps[1];
        npy_intp os = steps[2];
        char *ip0 = args[0];
        char *ip1 = args[1];
        char *op = args[2];
        n = dimensions[0];
        double cr, ci;
        
        for(i = 0; i < n; i++) {
                cr = *(double *)ip0;
                ci = *(double *)ip1;
                double *out = (double *)op;
                
                *out = log(log(iterations(cr, ci)));
                
                ip0 += is0;
                ip1 += is1;
                op += os;
        }
}

static PyUFuncGenericFunction f_functions[] = {
        PyUFunc_0,
};

static char f_types[] = {
        NPY_DOUBLE, NPY_DOUBLE, NPY_DOUBLE,
};
'''

ufunc_info = weave.base_info.custom_info()
ufunc_info.add_header('"numpy/ufuncobject.h"')

mandel = weave.inline('/*' + hashlib.md5(support_code).hexdigest() + '''*/
import_ufunc();

return_val = PyUFunc_FromFuncAndData(
            f_functions,
            NULL,
            f_types,
            1,             /* ntypes */
            2,             /* nin */
            1,             /* nout */
            PyUFunc_None,  /* identity */
            "mandel",      /* name */
            "returns depth from cr, ci",         /* doc */
            0);
            ''',
                      support_code=support_code,
                      verbose=0,
                      customize=ufunc_info)
########################################################################
# Now mandel is a UFunc which takes x, y and returns the height.
# The height is the log of the log of the number of iterations for
# the point z = x + iy in the complex plane.
########################################################################

x, y = numpy.ogrid[-3.0:+2.0:500j, -2.25:+2.25:500j]

P = M.pipeline

mandel_array = P.array2dsource(x, y, mandel)
mandel_warp = P.warpscalar(mandel_array)
mandel_triangles = P.trianglefilter(mandel_warp)
mandel_triangles = P.quadricdecimation(mandel_triangles)
mandel_elevation = P.elevationfilter(mandel_triangles,
                      low_point  = [0, 0, -0.4],
                      high_point = [0, 0,  1.9])

P.surface(mandel_elevation, colormap='jet')
