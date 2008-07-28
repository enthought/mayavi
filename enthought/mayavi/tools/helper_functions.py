"""
Helper functions for mlab. These combine creation of the data sources,
and applying the modules to them to make standard visualization
operation. They should always return the module object created, for
consistency, and because retrieving the data_source from a module object
is possible via tools._find_data

Each helper function should have a test function assoiciated with it,
both for testing and to ilustrate its use.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

from modules import VectorsFactory, StreamlineFactory, GlyphFactory, \
            IsoSurfaceFactory, SurfaceFactory, ContourSurfaceFactory
from sources import vectorscatter, vectorfield, scalarscatter, \
            scalarfield, linesource, array2dsource, gridsource
from filters import ExtractVectorNormFactory, WarpScalarFactory, \
            TubeFactory, ExtractEdgesFactory
from auto_doc import traits_doc, dedent
import tools
from enthought.traits.api import Array, Callable, CFloat, HasTraits, \
    List, Trait, Any, Instance
import numpy

def document_pipeline(pipeline):
    def the_function(*args, **kwargs): 
        return pipeline(*args, **kwargs)
    
    if hasattr(pipeline, 'doc'):
        doc = pipeline.doc
    elif pipeline.__doc__ is not None:
        doc = pipeline.__doc__
    else:
        doc = ''

    the_function.__doc__  = dedent("""%s

    **Keyword arguments:**
    %s""") % ( dedent(doc),
                traits_doc(pipeline.get_all_traits()), )
    
    return the_function


############################################################################# 
class Pipeline(HasTraits):
    """ Functor used to build pipelines for helper functions """
    #doc = ''
    _source_function = Callable()

    _pipeline = List()

    # Traits here only for documentation purposes
    figure = Instance('enthought.mayavi.core.scene.Scene',
                help='Figure to populate.')

    def __call__(self, *args, **kwargs):
        """ Builds the source and runs through the pipeline, returning
        the last object created by the pipeline."""
        self.store_kwargs(kwargs)
        self.source = self._source_function(*args, **kwargs)
        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        return self.build_pipeline()

    def store_kwargs(self, kwargs):
        """ Merges the given keyword argument, with traits default and
            store the resulting dictionary in self.kwargs."""
        kwargs = kwargs.copy()
        name = kwargs.pop('name', None)
        all_traits = self.get_all_traits()
        if not set(kwargs.keys()).issubset(all_traits.keys()):
            raise ValueError, "Invalid keyword arguments : %s" % \
                    ', '.join(str(k) for k in 
                              set(kwargs.keys()).difference(all_traits.keys()) )
        traits = self.get(self.class_trait_names())
        [traits.pop(key) for key in traits.keys() if key[0]=='_' ]
        traits.update(kwargs)
        self.kwargs = traits

    def build_pipeline(self):
        """ Runs through the pipeline, applying pipe after pipe. """
        object = self.source
        for pipe in self.pipeline:
            keywords = set(pipe.class_trait_names())
            keywords.remove('trait_added')
            keywords.remove('trait_modified')
            this_kwargs = {}
            for key, value in self.kwargs.iteritems():
                if key in keywords:
                    this_kwargs[key] = value
            object = pipe(object, **this_kwargs)._target
        return object

    def get_all_traits(self):
        """ Returns all the traits of class, and the classes in the pipeline.
        """
        traits = {}
        for pipe in self._pipeline:
            traits.update(pipe.class_traits())
        traits.update(self.class_traits())
        traits.pop('trait_added')
        traits.pop('trait_modified')
        return traits


############################################################################# 

quiver3d = Pipeline( 
            doc="""
    Plots glyphs (like arrows) indicating the direction of the vectors
    for a 3D volume of data supplied as arguments.

    **Function signatures**::
    
        quiver3d(u, v, w, ...)
        quiver3d(x, y, z, u, v, w, ...)
        quiver3d(x, y, z, f, ...)
    
    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors. """,
            _source_function=vectorscatter,
            _pipeline=[VectorsFactory, ] 
        )
quiver3d = document_pipeline(quiver3d)


def test_quiver3d():
    dims = [8, 8, 8]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = numpy.mgrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = numpy.sin
    cos = numpy.cos
    u = cos(x)
    v = sin(y)
    w = sin(x*z)

    obj = quiver3d(x, y, z, u, v, w, mode='cone', extent=(0,1, 0,1, 0,1),
                   scale_factor=0.9)

    return u, v, w, obj

def test_quiver3d_2d_data():
    dims = [32, 32]
    xmin, xmax, ymin, ymax = [-5,5,-5,5]
    x, y = numpy.mgrid[xmin:xmax:dims[0]*1j,
                       ymin:ymax:dims[1]*1j]
    x = x.astype('f')
    y = y.astype('f')

    sin = numpy.sin
    cos = numpy.cos
    u = cos(x)
    v = sin(y)
    w = numpy.zeros_like(x)

    return quiver3d(x, y, w, u, v, w, colormap="Purples",
                                scale_factor=0.5, mode="2dthick_arrow")


############################################################################# 
class Flow(Pipeline):
    """
    Creates streamlines following the flow of a vector field. 
                      
    **Function signatures**::
    
        flow(u, v, w, ...)
        flow(x, y, z, u, v, w, ...)
        flow(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If the x, y and z arrays are passed they are supposed to have been
    generated by `numpy.mgrid`. The function builds a scalar field assuming 
    the points are regularily spaced.

    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors."""

    scalars = Array(help="""optional scalar data.""")

    _source_function = Callable(vectorfield)

    _pipeline = [ExtractVectorNormFactory, StreamlineFactory, ] 

    def __call__(self, *args, **kwargs):
        """ Override the call to be able to choose whether to apply an
        ExtractVectorNorm filter.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        self.store_kwargs(kwargs)
        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        if tools._has_scalar_data(self.source):
            self.pipeline.pop(0)
        return self.build_pipeline()


flow = document_pipeline(Flow())

def test_flow():
    dims = [32, 32, 32]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = numpy.mgrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = numpy.sin
    cos = numpy.cos
    u = cos(x/2.)
    v = sin(y/2.)
    w = sin(x*z/4.)

    obj = flow(x, y, z, u, v, w, linetype='tube')
    return u, v, w, obj

def test_flow_scalars():
    dims = [32, 32, 32]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = numpy.mgrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = numpy.sin
    cos = numpy.cos
    u = cos(x/2.)
    v = sin(y/2.)
    w = sin(x*z/8.)
    t = x*z

    obj = flow(u, v, w, scalars=t, seedtype='plane',
                    linetype='tube', colormap='Spectral')

    return u, v, w, obj


############################################################################# 
class Points3d(Pipeline):
    """ 
    Plots glyphs (like points) at the position of the supplied data.

    **Function signatures**::

        points3d(scalardata, ...)
        points3d(x, y, z...)
        points3d(x, y, z, s, ...)
        points3d(x, y, z, f, ...)

    If only one positional argument is passed, it should be VTK data
    object with scalar data.

    If only 3 arrays x, y, z all the points are drawn with the same size
    and color

    If 4 positional arguments are passed the last one can be an array s
    or a callable f that gives the size and color of the glyph."""

    _source_function = Callable(scalarscatter)

    _pipeline = [GlyphFactory, ]


points3d = document_pipeline(Points3d())


def test_points3d():
    t = numpy.linspace(0, 4*numpy.pi, 20)
    cos = numpy.cos
    sin = numpy.sin

    x = sin(2*t)
    y = cos(t)
    z = cos(2*t)
    s = 2+sin(t)

    points3d(x, y, z, s, colormap="copper", scale_factor=.25)


def test_molecule():
    """Generates and shows a Caffeine molecule."""
    o = [[30, 62, 19],[8, 21, 10]]
    ox, oy, oz = map(numpy.array, zip(*o))
    n = [[31, 21, 11], [18, 42, 14], [55, 46, 17], [56, 25, 13]]
    nx, ny, nz = map(numpy.array, zip(*n))
    c = [[5, 49, 15], [30, 50, 16], [42, 42, 15], [43, 29, 13], [18, 28, 12],
         [32, 6, 8], [63, 36, 15], [59, 60, 20]]
    cx, cy, cz = map(numpy.array, zip(*c))
    h = [[23, 5, 7], [32, 0, 16], [37, 5, 0], [73, 36, 16], [69, 60, 20],
         [54, 62, 28], [57, 66, 12], [6, 59, 16], [1, 44, 22], [0, 49, 6]]
    hx, hy, hz = map(numpy.array, zip(*h))

    oxygen = points3d(ox, oy, oz, scale_factor=16, scale_mode='none',
                                resolution=20, color=(1,0,0), name='Oxygen')
    nitrogen = points3d(nx, ny, nz, scale_factor=20, scale_mode='none', 
                                resolution=20, color=(0,0,1), name='Nitrogen')
    carbon = points3d(cx, cy, cz, scale_factor=20, scale_mode='none', 
                                resolution=20, color=(0,1,0), name='Carbon')
    hydrogen = points3d(hx, hy, hz, scale_factor=10, scale_mode='none', 
                                resolution=20, color=(1,1,1), name='Hydrogen')

    return oxygen, nitrogen, carbon, hydrogen

############################################################################# 
class Contour3d(Pipeline):
    """
    Plots iso-surfaces for a 3D volume of data suplied as arguments.

    **Function signatures**::

        contour3d(scalars, ...)
        contour3d(scalarfield, ...)"""

    _source_function = Callable(scalarfield)

    _pipeline = [IsoSurfaceFactory, ]


contour3d = document_pipeline(Contour3d())


def test_contour3d():
    dims = [64, 64, 64]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = numpy.ogrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = numpy.sin
    scalars = x*x*0.5 + y*y + z*z*2.0

    obj = contour3d(scalars, contours=4, transparent=True)
    return obj, scalars


############################################################################# 
class Plot3d(Pipeline):
    """
    Draws lines between points.

    **Function signatures**::

        plot3d(x, y, z, ...)
        plot3d(x, y, z, s, ...)"""

    tube_radius = CFloat(0.025, adapts='filter.radius',
                        desc = """radius of the tubes used to represent the
                        lines""")

    _source_function = Callable(linesource)

    _pipeline = [TubeFactory, SurfaceFactory, ]

    def __call__(self, *args, **kwargs):
        """ Override the call to be able to choose whether to apply
        filters.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        self.store_kwargs(kwargs)
        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        if self.kwargs['tube_radius'] == None:
            self.pipeline.remove(TubeFactory)
        return self.build_pipeline()


plot3d = document_pipeline(Plot3d())


def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    pi = numpy.pi
    dphi = pi/1000.0 
    phi = numpy.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = numpy.cos(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    y = numpy.sin(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    z = numpy.sin(n_long*mu/n_mer)*0.5

    l = plot3d(x, y, z, numpy.sin(mu), tube_radius=0.025, colormap='Spectral')
    return l


############################################################################# 
class ImShow(Pipeline):
    """
    Allows one to view a 2D Numeric array as an image.  This works
    best for very large arrays (like 1024x1024 arrays).

    **Function signatures**::

        imshow(2darray, ...)"""

    _source_function = Callable(array2dsource)

    _pipeline = [SurfaceFactory, ]


imshow = document_pipeline(ImShow())


def test_imshow():
    return imshow(numpy.random.random((10,10)), colormap='gist_earth')


############################################################################# 
class Surf(Pipeline):
    """
    Plots a surface using regularly spaced elevation data supplied as a 2D 
    array.

    **Function signatures**::

        surf(s, ...)
        surf(x, y, s, ...)
        surf(x, y, f, ...)        
    
    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinnates of positions corresponding to the s values. 
    
    z is the elevation matrix.
    
    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value. For 
    arbitrary-shaped position arrays (non-orthogonal grids), see the mesh 
    function.

    If only 1 array s is passed the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is 
    created."""

    _source_function = Callable(array2dsource)

    _pipeline = [WarpScalarFactory, SurfaceFactory]


    warp_scale = Any('auto', help="""scale of the z axis (warped from
                        the value of the scalar). By default this scale
                        is calculated to give a pleasant aspect ratio to
                        the plot. You can overright this behavoir by
                        specifying a float value.""")

    mask = Array(help="boolean mask array to suppress some data points.")

    def __call__(self, *args, **kwargs):
        """ Override the call to be able to scale automaticaly the axis.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        if self.warp_scale == 'auto' and not 'extent' in kwargs:
            try:
                xi, xf, yi, yf, zi, zf = self.source.data.bounds
            except AttributeError:
                xi, xf, yi, yf, zi, zf = self.source.image_data.bounds
            zf = 0.3*((xf - xi) + (yf - yi))
            kwargs['extent'] = (xi, xf, yi, yf, zi, zf)
            kwargs['warp_scale'] = 1.
        self.store_kwargs(kwargs)

        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        return self.build_pipeline()



surf = document_pipeline(Surf())


def test_simple_surf():
    """Test Surf with a simple collection of points."""
    x, y = numpy.mgrid[0:3:1,0:3:1]
    return surf(x, y, numpy.asarray(x, 'd'))


def test_surf():
    """Test surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = numpy.sin, numpy.cos
        return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)

    x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = surf(x, y, f)
    #cs = contour_surf(x, y, f, contour_z=0)
    return s


def test_surf_wigner():
    def cat(x,y, alpha, eta = 1, purity = 1):
        """ Multiphoton shrodinger cat. eta is the fidelity, alpha the number
            of photons"""
        cos = numpy.cos
        exp = numpy.exp
        return (1 + eta*(exp(-x**2 -(y-alpha)**2)  + exp(-x**2 -
        (y+alpha)**2) + 2 * purity * exp(-x**2 - y**2) * cos(2* alpha * x))/(2
        *
        (1 + exp(- alpha**2))))/2
    x, y = numpy.mgrid[-5:5:0.1, -5:5:0.1]



############################################################################# 
class Mesh(Pipeline):
    """
    Plots a surface using grid-spaced data supplied as 2D arrays.

    **Function signatures**::

        mesh(x, y, z, ...)
    
    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is implied by the connectivity on 
    the arrays. 

    For simple structures (such as orthogonal grids) prefer the surf function,
    as it will create more efficient data structures.
    """

    scale_mode = Trait('none', {'none':'data_scaling_off',
                                'scalar':'scale_by_scalar',
                                'vector':'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    scale_factor = CFloat(0.05,
                        desc = """scale factor of the glyphs used to represent 
                        the vertices, in fancy_mesh mode. """)

    tube_radius = Trait(0.025, CFloat, None,
                        help = """radius of the tubes used to represent the
                        lines, in mesh mode. If None, simple lines are used.
                        """)

    scalars = Array(help="""optional scalar data.""")

    mask = Array(help="boolean mask array to suppress some data points.")

    representation = Trait('surface', 'wireframe', 'points', 'mesh',
                    'fancymesh',
                    desc="""the representation type used for the surface.""")

    _source_function = Callable(gridsource)

    _pipeline = [ExtractEdgesFactory, GlyphFactory, TubeFactory, 
                        SurfaceFactory]
    
    def __call__(self, *args, **kwargs):
        """ Override the call to be able to choose whether to apply
        filters.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        self.store_kwargs(kwargs)
        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        if not self.kwargs['representation'] in ('mesh', 'fancymesh'):
            self.pipeline.remove(ExtractEdgesFactory)
            self.pipeline.remove(TubeFactory)
            self.pipeline.remove(GlyphFactory)
        else:
            if self.kwargs['tube_radius'] == None:
                self.pipeline.remove(TubeFactory)
            if not self.kwargs['representation'] == 'fancymesh':
                self.pipeline.remove(GlyphFactory)
            self.kwargs['representation'] = 'surface'
        return self.build_pipeline()


mesh = document_pipeline(Mesh())


def test_mesh():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin
    dphi, dtheta = pi/250.0, pi/250.0
    [phi,theta] = numpy.mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
    m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
    r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
    x = r*sin(phi)*cos(theta)
    y = r*cos(phi)
    z = r*sin(phi)*sin(theta);

    return mesh(x, y, z, colormap="bone")

def test_mesh_sphere():
    """Create a simple sphere and test the mesh."""
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin    
    du, dv = pi/20.0, pi/20.0
    phi, theta = numpy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
    r = 1.0
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)
    s = mesh(x, y, z, representation='mesh', colormap='jet',
                    tube_radius=None)
                   #tube_radius=None, sphere_radius=0.025)

def test_fancy_mesh():
    """Create a fancy looking mesh using mesh (example taken from octaviz)."""
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin
    du, dv = pi/20.0, pi/20.0
    u, v = numpy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
    x = (1- cos(u))*cos(u+2*pi/3) * cos(v + 2*pi/3.0)*0.5
    y = (1- cos(u))*cos(u+2*pi/3) * cos(v - 2*pi/3.0)*0.5
    z = -cos(u-2*pi/3.)

    m = mesh(x, y, z, representation='fancymesh',
                   tube_radius=0.0075, colormap="RdYlGn")


############################################################################# 
class ContourSurf(Pipeline):
    """
    Plots a the contours of asurface using grid spaced data supplied as 2D 
    arrays.

    **Function signatures**::

        contour_surf(s, ...)
        contour_surf(x, y, s, ...)
        contour_surf(x, y, f, ...)        

    If only one array s is passed the x and y arrays are assumed to be made 
    of the indices of s.
    s is the elevation matrix."""

    _source_function = Callable(array2dsource)

    _pipeline = [WarpScalarFactory, ContourSurfaceFactory]


contour_surf = document_pipeline(ContourSurf())


def test_contour_surf():
    """Test contour_surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = numpy.sin, numpy.cos
        return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)

    x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = contour_surf(x, y, f)
    return s

