#!/usr/bin/env python
""" A simple example showing an Mandelbrot set.

Author: Ilan Schnell <ischnell@enthought.com>
Copyright 2008, Enthought, Inc.
License: BSD Style.
"""

print "This script is numerically intensive and requires a lot of memory."
print "Please be patient..."

import hashlib

from numpy import ogrid, log
from scipy import weave


from enthought.mayavi import mlab


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
        
        for(i = 0; i < n; i++) {
                long *out = (long *)op;
                
                *out = iterations(*(double *)ip0,
                                  *(double *)ip1);
                
                ip0 += is0;
                ip1 += is1;
                op += os;
        }
}

static PyUFuncGenericFunction f_functions[] = {
        PyUFunc_0,
};

static char f_types[] = {
        NPY_DOUBLE, NPY_DOUBLE, NPY_LONG,
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
            "returns iterations for z = x + i y",   /* doc */
            0);
            ''',
                      support_code=support_code,
                      verbose=0,
                      customize=ufunc_info)

##############################################################################
# Now mandel is a UFunc which takes x, y and returns the number of iterations
# for the start point z = x + iy in the complex plane to diverge.
##############################################################################
@mlab.show
def view():
    x, y = ogrid[-3.0:+2.0:500j, -2.5:+2.5:500j]

    # mandel_array is a 2D numpy array with the height for each point
    mandel_array = log(log(mandel(x, y)))

    P = mlab.pipeline

    mandel_struct2d = P.array2d_source(x, y, mandel_array)
    mandel_warp = P.warp_scalar(mandel_struct2d)
    mandel_triangles = P.triangle_filter(mandel_warp)
    mandel_triangles = P.quadric_decimation(mandel_triangles)
    mandel_elevation = P.elevation_filter(mandel_triangles,
                          low_point  = [0, 0, mandel_array.min()],
                          high_point = [0, 0, mandel_array.max()])

    P.surface(mandel_elevation, colormap='jet', extent=(0,1, 0,1, 0, 0.3))

if __name__ == '__main__':
    view()

