"""
Data sources classes and their associated functions for mlab.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Prabhu Ramachandran
# Copyright (c) 2007-2008, Enthought, Inc. 
# License: BSD Style.

import numpy
from enthought.tvtk.tools import mlab
from enthought.tvtk.api import tvtk
from enthought.tvtk.common import camel2enthought
from enthought.mayavi.sources.array_source import ArraySource

from enthought.mayavi.core.registry import registry

import tools
from engine_manager import engine_manager

__all__ = [ 'vectorscatter', 'vectorfield', 'scalarscatter', 'scalarfield',
    'linesource', 'array2dsource', 'gridsource', 'open'
]

def _make_glyph_data(points, vectors=None, scalars=None):
    """Makes the data for glyphs using mlab.
    """
    g = mlab.Glyphs(points, vectors, scalars)
    return g.poly_data

############################################################################
# Argument processing
############################################################################

def convert_to_arrays(args):
    """ Converts a list of iterables to a list of arrays or callables, 
        if needed.
    """
    args = list(args)
    for index, arg in enumerate(args):
        if not hasattr(arg, 'shape') and not callable(arg):
            args[index] = numpy.array(arg)
    return args

def process_regular_vectors(*args):
    """ Converts different signatures to (x, y, z, u, v, w). """
    args = convert_to_arrays(args)
    if len(args)==3:
        u, v, w = args
        assert len(u.shape)==3, "3D array required"
        x, y, z = numpy.indices(u.shape)
    elif len(args)==6:
        x, y, z, u, v, w = args
    elif len(args)==4:
        x, y, z, f = args
        if not callable(f):
            raise ValueError, "When 4 arguments are provided, the fourth must be a callable"
        u, v, w = f(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"

    assert ( x.shape == y.shape and
            y.shape == z.shape and
            u.shape == z.shape and
            v.shape == u.shape and
            w.shape == v.shape ), "argument shape are not equal"

    return x, y, z, u, v, w

def process_regular_scalars(*args):
    """ Converts different signatures to (x, y, z, s). """
    args = convert_to_arrays(args)
    if len(args)==1:
        s = args[0]
        assert len(s.shape)==3, "3D array required"
        x, y, z = numpy.indices(s.shape)
    elif len(args)==3:
        x, y, z = args
        s = None 
    elif len(args)==4:
        x, y, z, s = args
        if callable(s):
            s = s(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"

    assert ( x.shape == y.shape and
            y.shape == z.shape and
            ( s is None
                or s.shape == z.shape ) ), "argument shape are not equal"

    return x, y, z, s

def process_regular_2d_scalars(*args, **kwargs):
    """ Converts different signatures to (x, y, s). """
    args = convert_to_arrays(args)
    if len(args)==1:
        s = args[0]
        assert len(s.shape)==2, "2D array required"
        x, y = numpy.indices(s.shape)
    elif len(args)==3:
        x, y, s = args
        if callable(s):
            s = s(x, y)
    else:
        raise ValueError, "wrong number of arguments"
    assert len(s.shape)==2, "2D array required"

    if 'mask' in kwargs:
        mask = kwargs['mask']
        s[mask.astype('bool')] = numpy.nan
        # The NaN tric only works with floats.
        s = s.astype('float')

    return x, y, s


############################################################################
# Sources 
############################################################################

def vectorscatter(*args, **kwargs):
    """ Creates scattered vector data. 
    
    **Function signatures**::

        vectorscatter(u, v, w, ...)
        vectorscatter(x, y, z, u, v, w, ...)
        vectorscatter(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors.

    **Keyword arguments**:
    
        :name: the name of the vtk object created.

        :scalars: optional scalar data.
       
        :figure: optionally, the figure on which to add the data source."""
    x, y, z, u, v, w = process_regular_vectors(*args)

    points = numpy.c_[x.ravel(), y.ravel(), z.ravel()]
    vectors = numpy.c_[u.ravel(), v.ravel(), w.ravel()]
    scalars = kwargs.pop('scalar', None)
    name = kwargs.pop('name', 'VectorScatter')

    data_source = _make_glyph_data(points, vectors, scalars)
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def vectorfield(*args, **kwargs):
    """ Creates vector field data. 
    
    **Function signatures**::

        vectorsfield(u, v, w, ...)
        vectorsfield(x, y, z, u, v, w, ...)
        vectorsfield(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If the x, y and z arrays are passed, they should have been generated
    by `numpy.mgrid` or `numpy.ogrid`. The function builds a scalar field
    assuming the points are regularily spaced on an orthogonal grid.

    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors.

    **Keyword arguments**:
        
        :name: the name of the vtk object created.

        :scalars: optional scalar data.
       
        :figure: optionally, the figure on which to add the data source."""
    x, y, z, u, v, w = process_regular_vectors(*args)

    dx = x[1, 0, 0] - x[0, 0, 0]
    dy = y[0, 1, 0] - y[0, 0, 0]
    dz = z[0, 0, 1] - z[0, 0, 0]

    vectors = numpy.concatenate([u[..., numpy.newaxis],
                            v[..., numpy.newaxis],
                            w[..., numpy.newaxis] ],
                            axis=3)
                            
    scalars = kwargs.pop('scalars', None)
    kwargs = {}
    if scalars is not None:
        kwargs['scalar_data'] = scalars
        
    data_source = ArraySource(transpose_input_array=True,
                    vector_data=vectors,
                    origin=[x.min(), y.min(), z.min()],
                    spacing=[dx, dy, dz],
                    **kwargs)

    name = kwargs.pop('name', 'VectorField')
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def scalarscatter(*args, **kwargs):
    """
    Creates scattered scalar data. 
    
    **Function signatures**::

        scalarscatter(s, ...)
        scalarscatter(x, y, z, s, ...)
        scalarscatter(x, y, z, s, ...)
        scalarscatter(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.

    **Keyword arguments**:
    
        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source."""
    x, y, z, s = process_regular_scalars(*args)

    points = numpy.c_[x.ravel(), y.ravel(), z.ravel()]

    if s is not None:
        s = s.ravel()

    data_source = _make_glyph_data(points, None, s)

    name = kwargs.pop('name', 'ScalarScatter')
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def scalarfield(*args, **kwargs):
    """
    Creates a scalar field data.
                      
    **Function signatures**::
    
        scalarfield(s, ...)
        scalarfield(x, y, z, s, ...)
        scalarfield(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of arrays.

    If the x, y and z arrays are passed they are supposed to have been
    generated by `numpy.mgrid`. The function builds a scalar field assuming 
    the points are regularily spaced.

    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.
    
    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source."""
    x, y, z, s = process_regular_scalars(*args)

    points = numpy.c_[x.ravel(), y.ravel(), z.ravel()]
    dx = x[1, 0, 0] - x[0, 0, 0]
    dy = y[0, 1, 0] - y[0, 0, 0]
    dz = z[0, 0, 1] - z[0, 0, 0]        

    data_source = ArraySource(scalar_data=s,
                    origin=[points[0, 0], points[0, 1], points[0, 2]],
                    spacing=[dx, dy, dz])

    name = kwargs.pop('name', 'ScalarField')
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def linesource(*args, **kwargs):
    """
    Creates line data.
    
    **Function signatures**::
    
        linesource(x, y, z, ...)
        linesource(x, y, z, s, ...)
        linesource(x, y, z, f, ...)

        If 4 positional arguments are passed the last one must be an array s, or
        a callable, f, that returns an array. 

    **Keyword arguments**:
    
        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source."""
    if len(args)==1:
        raise ValueError, "wrong number of arguments"    
    x, y, z, s = process_regular_scalars(*args)

    points = numpy.c_[x.ravel(), y.ravel(), z.ravel()]
    np = len(points) - 1
    lines  = numpy.zeros((np, 2), 'l')
    lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
    lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
    data_source = tvtk.PolyData(points=points, lines=lines)

    if s is not None:
        s = s.ravel()
        data_source.point_data.scalars = s
        data_source.point_data.scalars.name = 'scalars'

    name = kwargs.pop('name', 'LineSource')
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def array2dsource(*args, **kwargs):
    """
    Creates structured 2D data from a 2D array.
    
    **Function signatures**::

        array2dsource(s, ...)
        array2dsource(x, y, s, ...)
        array2dsource(x, y, f, ...)

    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinnates of positions corresponding to the s values. 
    
    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value.

    If only 1 array s is passed the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.

    **Keyword arguments**:
    
        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source."""
    if len(args) == 1 :
        args = convert_to_arrays(args)
        s = args[0]
        nx, ny = s.shape
        if 'mask' in kwargs:
            mask = kwargs['mask']
            s[mask.astype('bool')] = numpy.nan
            # The NaN tric only works with floats.
            s = s.astype('float')

        data_source = ArraySource(transpose_input_array=True,
                    scalar_data=s,
                    origin=[-nx/2., ny/2., 0],
                    spacing=[1, 1, 1])
    else:
        x, y, s = process_regular_2d_scalars(*args, **kwargs)
        # Do some magic to extract the first row/column, independently of
        # the shape of x and y
        x = numpy.atleast_2d(x.squeeze().T)[0, :].squeeze()
        y = numpy.atleast_2d(y.squeeze())[0, :].squeeze()
        data_source = mlab._create_structured_points_direct(x, y)
        s = s.T
        s = s.ravel()
        data_source.point_data.scalars = s
        data_source.point_data.scalars.name = 'scalars'
        data_source.scalar_type = 'unsigned_char'
        data_source.number_of_scalar_components = 1

    name = kwargs.pop('name', 'Array2DSource')
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def gridsource(x, y, z, **kwargs):
    """
    Creates 2D grid data.

    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is implied by the connectivity on
    the arrays.
    
    For simple structures (such as orthogonal grids) prefer the array2dsource
    function, as it will create more efficient data structures. 

    **Keyword arguments**:
    
        :name: the name of the vtk object created.
        
        :scalars: optional scalar data.
       
        :figure: optionally, the figure on which to add the data source.
        """
    scalars = kwargs.pop('scalars', None)
    if scalars is None:
        scalars = z
    name    = kwargs.pop('name', 'GridSource')
    triangles, points = mlab.make_triangles_points(x, y, z, scalars)
    data_source = mlab.make_triangle_polydata(triangles, points, scalars)
    figure = kwargs.pop('figure', None)
    return tools._add_data(data_source, name, figure=figure)


def open(filename, figure=None):
    """Open a supported data file given a filename.  Returns the source
    object if a suitable reader was found for the file.
    """
    if figure is None:
        engine = tools.get_engine()
    else:
        engine = engine_manager.find_figure_engine(figure)
        engine.current_scene = figure
    src = engine.open(filename)
    return src
    
############################################################################
# Automatically generated sources from registry.
############################################################################
def _create_data_source(metadata):
    """Creates a data source and adds it to the mayavi engine given
    metadata of the source.  Returns the created source.  
    """
    factory = metadata.get_callable()
    src = factory()
    engine = tools.get_engine()
    engine.add_source(src)
    return src

def _make_functions(namespace):
    """Make the automatic functions and add them to the namespace."""
    for src in registry.sources:
        if len(src.extensions) == 0:
            func_name = camel2enthought(src.id)
            if func_name.endswith('_source'):
                func_name = func_name[:-7]
            func = lambda metadata=src: _create_data_source(metadata)
            func.__doc__ = src.help
            func.__name__ = func_name
            # Inject function into the namespace and __all__.
            namespace[func_name] = func
            __all__.append(func_name)

_make_functions(locals())
