"""
Helper functions for mlab. These combine creation of the data sources,
and applying the modules to them to make standard visualization
operation. They should always return the module object created, for
consistency, and because retrieving the vtk data source from a module object
is possible via tools.get_vtk_src

Each helper function should have a test function associated with it,
both for testing and to ilustrate its use.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from .modules import VectorsFactory, StreamlineFactory, GlyphFactory, \
            IsoSurfaceFactory, SurfaceFactory, ContourSurfaceFactory, \
            ImageActorFactory, ImagePlaneWidgetFactory, glyph_mode_dict
from .sources import vector_scatter, vector_field, scalar_scatter, \
            scalar_field, line_source, array2d_source, grid_source, \
            triangular_mesh_source, vertical_vectors_source
from .filters import ExtractVectorNormFactory, WarpScalarFactory, \
            TubeFactory, ExtractEdgesFactory, PolyDataNormalsFactory, \
            StripperFactory
from .animator import animate
from mayavi.core.scene import Scene
from .auto_doc import traits_doc, dedent
from . import tools
from traits.api import Array, Bool, Callable, CFloat, HasTraits, \
    List, Trait, Any, Instance, TraitError
import numpy as np



def document_pipeline(pipeline):

    def the_function(*args, **kwargs):
        return pipeline(*args, **kwargs)

    if hasattr(pipeline, 'doc'):
        doc = pipeline.doc
    elif pipeline.__doc__ is not None:
        doc = pipeline.__doc__
    else:
        doc = ''

    the_function.__doc__ = dedent("""%s

    **Keyword arguments:**
    %s""") % (dedent(doc),
              traits_doc(pipeline.get_all_traits()),)

    return the_function


#############################################################################
class Pipeline(HasTraits):
    """ Function used to build pipelines for helper functions """
    #doc = ''
    _source_function = Callable()

    _pipeline = List()

    # Traits here only for documentation purposes
    figure = Instance('mayavi.core.scene.Scene',
                help='Figure to populate.')

    def __call__(self, *args, **kwargs):
        """ Calls the logics of the factory, but only after disabling
            rendering, if needed.
        """
        # First retrieve the scene, if any.
        if 'figure' in kwargs:
            figure = kwargs['figure']
            assert isinstance(figure, Scene) or figure is None
            scene = getattr(figure, 'scene', None)
        else:
            scene = tools.gcf().scene
        if scene is not None:
            self._do_redraw = not scene.disable_render
            scene.disable_render = True
        # Then call the real logic
        output = self.__call_internal__(*args, **kwargs)
        # And re-enable the rendering, if needed.
        if scene is not None:
            scene.disable_render = not self._do_redraw
        return output

    def __call_internal__(self, *args, **kwargs):
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
        all_traits = self.get_all_traits()
        if not set(kwargs.keys()).issubset(list(all_traits.keys())):
            raise ValueError("Invalid keyword arguments : %s" % \
                    ', '.join(
                        str(k) for k in
                        set(kwargs.keys()).difference(list(all_traits.keys()))))
        traits = self.trait_get(self.class_trait_names())
        [traits.pop(key) for key in list(traits.keys()) if key[0] == '_']
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
            for key, value in self.kwargs.items():
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
class Points3d(Pipeline):
    """
    Plots glyphs (like points) at the position of the supplied data.

    **Function signatures**::

        points3d(x, y, z...)
        points3d(x, y, z, s, ...)
        points3d(x, y, z, f, ...)

    x, y and z are numpy arrays, or lists, all of the same shape, giving
    the positions of the points.

    If only 3 arrays x, y, z are given, all the points are drawn with the
    same size and color.

    In addition, you can pass a fourth array s of the same
    shape as x, y, and z giving an associated scalar value for each
    point, or a function f(x, y, z) returning the scalar value. This
    scalar value can be used to modulate the color and the size of the
    points."""

    _source_function = Callable(scalar_scatter)

    _pipeline = [GlyphFactory, ]

    scale_factor = Any('auto', help='The scaling applied to the glyphs. '
                        'the size of the glyph is by default calculated '
                        'from the inter-glyph spacing. Specify a float to '
                        'give the maximum glyph size in drawing units'
                        )

    def __call_internal__(self, *args, **kwargs):
        """ Override the call to be able to scale automatically the glyphs.
        """
        scale_factor = kwargs.get('scale_factor', 'auto')
        if scale_factor == 'auto':
            kwargs['scale_factor'] = 1
        g = Pipeline.__call_internal__(self, *args, **kwargs)
        if scale_factor == 'auto':
            g.glyph.glyph.scale_factor = \
                             tools._typical_distance(g.mlab_source.dataset)
            g.glyph.glyph.clamping = True
        else:
            g.glyph.glyph.clamping = False
        return g

points3d = document_pipeline(Points3d())


def test_points3d():
    t = np.linspace(0, 4 * np.pi, 20)

    x = np.sin(2 * t)
    y = np.cos(t)
    z = np.cos(2 * t)
    s = 2 + np.sin(t)

    return points3d(x, y, z, s, colormap="copper", scale_factor=.25)

@animate
def test_points3d_anim(obj=None):
    """Animates the test_points3d example."""
    g = obj if obj is not None else test_points3d()
    t = np.linspace(0, 4 * np.pi, 20)
    # Animate the points3d.
    ms = g.mlab_source
    for i in range(10):
        ms.z = np.cos(2 * t * 0.1 * (i + 1))
        yield


def test_molecule():
    """Generates and shows a Caffeine molecule."""
    o = [[30, 62, 19], [8, 21, 10]]
    ox, oy, oz = list(map(np.array, zip(*o)))
    n = [[31, 21, 11], [18, 42, 14], [55, 46, 17], [56, 25, 13]]
    nx, ny, nz = list(map(np.array, zip(*n)))
    c = [[5, 49, 15], [30, 50, 16], [42, 42, 15], [43, 29, 13], [18, 28, 12],
         [32, 6, 8], [63, 36, 15], [59, 60, 20]]
    cx, cy, cz = list(map(np.array, zip(*c)))
    h = [[23, 5, 7], [32, 0, 16], [37, 5, 0], [73, 36, 16], [69, 60, 20],
         [54, 62, 28], [57, 66, 12], [6, 59, 16], [1, 44, 22], [0, 49, 6]]
    hx, hy, hz = list(map(np.array, zip(*h)))

    oxygen = points3d(ox, oy, oz, scale_factor=16, scale_mode='none',
                                resolution=20, color=(1, 0, 0), name='Oxygen')
    nitrogen = points3d(nx, ny, nz, scale_factor=20, scale_mode='none',
                                resolution=20, color=(0, 0, 1),
                                name='Nitrogen')
    carbon = points3d(cx, cy, cz, scale_factor=20, scale_mode='none',
                                resolution=20, color=(0, 1, 0), name='Carbon')
    hydrogen = points3d(hx, hy, hz, scale_factor=10, scale_mode='none',
                                resolution=20, color=(1, 1, 1),
                                name='Hydrogen')

    return oxygen, nitrogen, carbon, hydrogen

#############################################################################


class Quiver3D(Points3d):
    """
    Plots glyphs (like arrows) indicating the direction of the vectors
    at the positions supplied.

    **Function signatures**::

        quiver3d(u, v, w, ...)
        quiver3d(x, y, z, u, v, w, ...)
        quiver3d(x, y, z, f, ...)

    u, v, w are numpy arrays giving the components of the vectors.

    If only 3 arrays, u, v, and w are passed, they must be 3D arrays, and
    the positions of the arrows are assumed to be the indices of the
    corresponding points in the (u, v, w) arrays.

    If 6 arrays, (x, y, z, u, v, w) are passed, the 3 first arrays give
    the position of the arrows, and the 3 last the components. They
    can be of any shape.

    If 4 positional arguments, (x, y, z, f) are passed, the last one must be
    a callable, f, that returns vectors components (u, v, w) given the
    positions (x, y, z)."""

    scalars = Array(help="""optional scalar data.""")

    _source_function = Callable(vector_scatter)

    _pipeline = [VectorsFactory, ]


quiver3d = document_pipeline(Quiver3D())


def test_quiver3d():
    x, y, z = np.mgrid[-2:3, -2:3, -2:3]
    r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
    u = y * np.sin(r) / (r + 0.001)
    v = -x * np.sin(r) / (r + 0.001)
    w = np.zeros_like(z)
    obj = quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
    return obj


def test_quiver3d_cone():
    xmin, xmax, ymin, ymax, zmin, zmax = [-5, 5, -5, 5, -5, 5]
    x, y, z = np.mgrid[-5:5:8j, -5:5:8j, -5:5:8j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    u = np.cos(x)
    v = np.sin(y)
    w = np.sin(x * z)

    obj = quiver3d(x, y, z, u, v, w, mode='cone', extent=(0, 1, 0, 1, 0, 1),
                   scale_factor=0.9)

    return obj


def test_quiver3d_2d_data():
    dims = [32, 32]
    xmin, xmax, ymin, ymax = [-5, 5, -5, 5]
    x, y = np.mgrid[xmin:xmax:dims[0] * 1j,
                    ymin:ymax:dims[1] * 1j]
    x = x.astype('f')
    y = y.astype('f')

    u = np.cos(x)
    v = np.sin(y)
    w = np.zeros_like(x)

    return quiver3d(x, y, w, u, v, w, colormap="Purples",
                                scale_factor=0.5, mode="2dthick_arrow")


#############################################################################
class Flow(Pipeline):
    """
    Creates a trajectory of particles following the flow of a vector field.

    **Function signatures**::

        flow(u, v, w, ...)
        flow(x, y, z, u, v, w, ...)
        flow(x, y, z, f, ...)

    u, v, w are numpy arrays giving the components of the vectors.

    If only 3 arrays, u, v, and w are passed, they must be 3D arrays, and
    the positions of the arrows are assumed to be the indices of the
    corresponding points in the (u, v, w) arrays.

    If 6 arrays, (x, y, z, u, v, w) are passed, the 3 first arrays give
    the position of the arrows, and the 3 last the components. The x, y
    and z arrays are then supposed to have been generated by
    `numpy.mgrid`, in other words, they are 3D arrays, with positions
    lying on a 3D orthogonal and regularly spaced grid with nearest
    neighbor in space matching nearest neighbor in the array. The
    function builds a vector field assuming  the points are regularly
    spaced.

    If 4 positional arguments, (x, y, z, f) are passed, the last one must be
    a callable, f, that returns vectors components (u, v, w) given the
    positions (x, y, z)."""

    scalars = Array(help="""optional scalar data.""")

    _source_function = Callable(vector_field)

    _pipeline = [ExtractVectorNormFactory, StreamlineFactory, ]

    def __call_internal__(self, *args, **kwargs):
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
    x, y, z = np.mgrid[-4:4:40j, -4:4:40j, 0:4:20j]
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2 + 0.1)
    u = y * np.sin(r) / r
    v = -x * np.sin(r) / r
    w = np.ones_like(z)*0.05
    obj = flow(u, v, w)
    return obj


def test_flow_tubes():
    dims = [32, 32, 32]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5, 5, -5, 5, -5, 5]
    x, y, z = np.mgrid[xmin:xmax:dims[0] * 1j,
                       ymin:ymax:dims[1] * 1j,
                       zmin:zmax:dims[2] * 1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    u = np.cos(x / 2.)
    v = np.sin(y / 2.)
    w = np.sin(x * z / 4.)

    obj = flow(x, y, z, u, v, w, linetype='tube')
    return obj


@animate
def test_flow_anim(obj=None):
    obj = obj if obj is not None else test_flow_tubes()
    # Now animate the flow.
    ms = obj.mlab_source
    x, y, z = ms.x, ms.y, ms.z
    for i in range(10):
        u = np.cos(x / 2. + np.pi * (i + 1) / 10.)
        w = np.sin(x * z / 4. + np.pi * (i + 1) / 10.)
        ms.trait_set(u=u, w=w)
        yield


def test_flow_scalars():
    dims = [32, 32, 32]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5, 5, -5, 5, -5, 5]
    x, y, z = np.mgrid[xmin:xmax:dims[0] * 1j,
                       ymin:ymax:dims[1] * 1j,
                       zmin:zmax:dims[2] * 1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    u = np.cos(x / 2.)
    v = np.sin(y / 2.)
    w = np.sin(x * z / 8.)
    t = x * z

    obj = flow(u, v, w, scalars=t, seedtype='plane',
               linetype='tube', colormap='Spectral')

    return obj


#############################################################################
class Contour3d(Pipeline):
    """
    Plots iso-surfaces for a 3D volume of data supplied as arguments.

    **Function signatures**::

        contour3d(scalars, ...)
        contour3d(x, y, z, scalars, ...)

    scalars is a 3D numpy arrays giving the data on a grid.

    If 4 arrays, (x, y, z, scalars) are passed, the 3 first arrays give the
    position, and the last the scalar value. The x, y and z arrays are then
    supposed to have been generated by `numpy.mgrid`, in other words, they are
    3D arrays, with positions lying on a 3D orthogonal and regularly spaced
    grid with nearest neighbor in space matching nearest neighbor in the array.
    The function builds a scalar field assuming  the points are regularly
    spaced."""

    _source_function = Callable(scalar_field)

    _pipeline = [IsoSurfaceFactory, ]


contour3d = document_pipeline(Contour3d())


def test_contour3d():
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]

    scalars = x * x * 0.5 + y * y + z * z * 2.0

    obj = contour3d(scalars, contours=4, transparent=True)
    return obj


@animate
def test_contour3d_anim(obj=None):
    obj = obj if obj is not None else test_contour3d()
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    # Now animate the contours.
    ms = obj.mlab_source
    for i in range(1, 10):
        ms.scalars = x * x * 0.5 + y * x * 0.1 * (i + 1) + z * z * 0.25
        yield


#############################################################################
class VolumeSlice(Pipeline):
    """
    Plots an interactive image plane sliced through a 3D volume of data
    supplied as argument.

    **Function signatures**::

        volume_slice(scalars, ...)
        volume_slice(x, y, z, scalars, ...)

    scalars is a 3D numpy arrays giving the data on a grid.

    If 4 arrays, (x, y, z, scalars) are passed, the 3 first arrays give the
    position, and the last the scalar value. The x, y and z arrays are then
    supposed to have been generated by `numpy.mgrid`, in other words, they are
    3D arrays, with positions lying on a 3D orthogonal and regularly spaced
    grid with nearest neighbor in space matching nearest neighbor in the array.
    The function builds a scalar field assuming  the points are regularly
    spaced."""

    _source_function = Callable(scalar_field)

    _pipeline = [ImagePlaneWidgetFactory, ]


volume_slice = document_pipeline(VolumeSlice())


def test_volume_slice():
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]

    scalars = x * x * 0.5 + y * y + z * z * 2.0

    obj = volume_slice(scalars, plane_orientation='x_axes')
    return obj


@animate
def test_volume_slice_anim(obj=None):
    obj = obj if obj is not None else test_volume_slice()
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    # Now animate the contours.
    ms = obj.mlab_source
    for i in range(1, 10):
        ms.scalars = x * x * 0.5 + y * x * 0.1 * (i + 1) + z * z * 0.25
        yield


#############################################################################
class Plot3d(Pipeline):
    """
    Draws lines between points.

    **Function signatures**::

        plot3d(x, y, z, ...)
        plot3d(x, y, z, s, ...)

    x, y, z and s are numpy arrays or lists of the same shape. x, y and z
    give the positions of the successive points of the line. s is an
    optional scalar value associated with each point."""

    tube_radius = Trait(0.025, CFloat, None,
                        adapts='filter.radius',
                        help="""radius of the tubes used to represent the
                        lines, If None, simple lines are used.
                        """)

    _source_function = Callable(line_source)

    _pipeline = [StripperFactory, TubeFactory, SurfaceFactory, ]

    def __call_internal__(self, *args, **kwargs):
        """ Override the call to be able to choose whether to apply
        filters.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        self.store_kwargs(kwargs)
        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        if self.kwargs['tube_radius'] is None:
            self.pipeline.remove(TubeFactory)
            self.pipeline.remove(StripperFactory)
        return self.build_pipeline()


plot3d = document_pipeline(Plot3d())


def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
    mu = phi * n_mer
    x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    z = np.sin(n_long * mu / n_mer) * 0.5

    l = plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
    return l

@animate
def test_plot3d_anim(obj=None):
    """Generates a pretty set of lines and animates it."""

    # Run the standard example and get the module generated.
    obj = obj if obj is not None else test_plot3d()

    # Some data from the test example for the animation.
    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi, 'd')
    mu = phi * n_mer

    # Now animate the data.
    ms = obj.mlab_source
    for i in range(10):
        x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer +
                                     np.pi * (i + 1) / 5.) * 0.5)
        scalars = np.sin(mu + np.pi * (i + 1) / 5)
        ms.trait_set(x=x, scalars=scalars)
        yield

#############################################################################
class ImShow(Pipeline):
    """
    View a 2D array as an image.

    **Function signatures**::

        imshow(s, ...)

    s is a 2 dimension array. The values of s are mapped to a color using
    the colormap."""

    _source_function = Callable(array2d_source)

    _pipeline = [ImageActorFactory, ]


imshow = document_pipeline(ImShow())


def test_imshow():
    """ Use imshow to visualize a 2D 10x10 random array.
    """
    s = np.random.random((10, 10))
    return imshow(s, colormap='gist_earth')


#############################################################################
class Surf(Pipeline):
    """
    Plots a surface using regularly-spaced elevation data supplied as a 2D
    array.

    **Function signatures**::

        surf(s, ...)
        surf(x, y, s, ...)
        surf(x, y, f, ...)

    s is the elevation matrix, a 2D array, where indices along the first
    array axis represent x locations, and indices along the second array
    axis represent y locations.

    x and y can be 1D or 2D arrays such as returned by numpy.ogrid or
    numpy.mgrid. Arrays returned by numpy.meshgrid require a transpose
    first to obtain correct indexing order.
    The points should be located on an orthogonal grid (possibly
    non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value. For
    arbitrary-shaped position arrays (non-orthogonal grids), see the mesh
    function.

    If only 1 array s is passed, the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.

    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinates of positions corresponding to the s values."""

    _source_function = Callable(array2d_source)

    _pipeline = [WarpScalarFactory, PolyDataNormalsFactory, SurfaceFactory]

    warp_scale = Any(1, help="""scale of the z axis (warped from
                        the value of the scalar). By default this scale
                        is a float value.

                        If you specify 'auto', the scale is calculated to
                        give a pleasant aspect ratio to the plot,
                        whatever the bounds of the data.

                        If you specify a value for warp_scale in
                        addition to an extent, the warp scale will be
                        determined by the warp_scale, and the plot be
                        positioned along the z axis with the zero of the
                        data centered on the center of the extent. If you
                        are using explicit extents, this is the best way
                        to control the vertical scale of your plots.

                        If you want to control the extent (or range)
                        of the surface object, rather than its scale,
                        see the `extent` keyword argument.
                        """)

    mask = Array(help="""boolean mask array to suppress some data points.
                 Note: this works based on colormapping of scalars and will
                 not work if you specify a solid color using the
                 `color` keyword.""")

    def __call_internal__(self, *args, **kwargs):
        """ Override the call to be able to scale automatically the axis.
        """
        self.source = self._source_function(*args, **kwargs)
        kwargs.pop('name', None)
        # Deal with both explicit warp scale and extent, this is
        # slightly hairy. The wigner example is a good test case for
        # this.
        if not 'warp_scale' in kwargs and not 'extent' in kwargs:
            try:
                xi, xf, yi, yf, _, _ = self.source.data.bounds
                zi, zf = self.source.data.scalar_range
            except AttributeError:
                xi, xf, yi, yf, _, _ = self.source.image_data.bounds
                zi, zf = self.source.image_data.scalar_range
            aspect_ratios = [(zf - zi) / (xf - xi), (zf - zi) / (yf - yi)]
            if min(aspect_ratios) < 0.01 or max(aspect_ratios) > 100:
                print('Warning: the range of your scalar values differs by ' \
                'more than a factor 100 than the range of the grid values ' \
                'and you did not '\
                'specify a warp_scale. You could try warp_scale="auto".')
        if 'warp_scale' in kwargs and not kwargs['warp_scale'] == 'auto' \
                and 'extent' in kwargs:
            # XXX: I should use the logging module.
            print('Warning: both warp_scale and extent keyword argument ' \
            'specified, the z bounds of the extents will be overridden')
            xi, xf, yi, yf, zi, zf = kwargs['extent']
            zo = 0.5 * (zi + zf)
            try:
                si, sf = self.source.data.scalar_range
            except AttributeError:
                si, sf = self.source.image_data.scalar_range
            z_span = kwargs['warp_scale'] * abs(sf - si)
            zi = zo + si * kwargs['warp_scale']
            zf = zi + z_span
            kwargs['extent'] = (xi, xf, yi, yf, zi, zf)
            kwargs['warp_scale'] = 1
        elif kwargs.get('warp_scale', 1) == 'auto':
            if 'extent' in kwargs:
                if 'warp_scale' in kwargs:
                    print("Warning: extent specified, warp_scale='auto' " \
                    "ignored.")
            else:
                try:
                    xi, xf, yi, yf, _, _ = self.source.data.bounds
                    zi, zf = self.source.data.scalar_range
                except AttributeError:
                    xi, xf, yi, yf, _, _ = self.source.image_data.bounds
                    zi, zf = self.source.image_data.scalar_range
                z0 = zf - zi
                dz = 0.3 * ((xf - xi) + (yf - yi))
                zi = z0 - 0.5 * dz
                zf = z0 + 0.5 * dz
                kwargs['extent'] = (xi, xf, yi, yf, zi, zf)
            kwargs['warp_scale'] = 1.
        self.store_kwargs(kwargs)

        # Copy the pipeline so as not to modify it for the next call
        self.pipeline = self._pipeline[:]
        return self.build_pipeline()


surf = document_pipeline(Surf())


def test_simple_surf():
    """Test Surf with a simple collection of points."""
    x, y = np.mgrid[0:3:1, 0:3:1]
    return surf(x, y, np.asarray(x, 'd'))

@animate
def test_simple_surf_anim(obj=None):
    """Test Surf with a simple collection of points and animate it."""
    obj = obj if obj is not None else test_simple_surf()

    ms = obj.mlab_source
    x = ms.x
    for i in range(10):
        ms.scalars = np.asarray(x * 0.1 * (i + 1), 'd')
        yield


def test_surf():
    """Test surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = np.sin, np.cos
        return sin(x + y) + sin(2 * x - y) + cos(3 * x + 4 * y)

    x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = surf(x, y, f)
    #cs = contour_surf(x, y, f, contour_z=0)
    return s


def test_surf_wigner():
    def cat(x, y, alpha=2, eta=1, purity=1):
        """ Multiphoton shrodinger cat. eta is the fidelity, alpha the number
            of photons"""
        cos = np.cos
        exp = np.exp
        return (1 + eta * (exp(-x ** 2 - (y - alpha) ** 2)
                + exp(-x ** 2 - (y + alpha) ** 2)
                + 2 * purity * exp(-x ** 2 - y ** 2) *
                        cos(2 * alpha * x)) / (2 * (1 + exp(-alpha ** 2)))) / 2
    x, y = np.mgrid[-5:5:0.1, -5:5:0.1]
    return surf(x, y, cat)


#############################################################################
class Mesh(Pipeline):
    """
    Plots a surface using grid-spaced data supplied as 2D arrays.

    **Function signatures**::

        mesh(x, y, z, ...)

    x, y, z are 2D arrays, all of the same shape, giving the positions of
    the vertices of the surface. The connectivity between these points is
    implied by the connectivity on the arrays.

    For simple structures (such as orthogonal grids) prefer the `surf`
    function, as it will create more efficient data structures. For mesh
    defined by triangles rather than regular implicit connectivity, see the
    `triangular_mesh` function.
    """

    scale_mode = Trait('none', {'none': 'data_scaling_off',
                                'scalar': 'scale_by_scalar',
                                'vector': 'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    scale_factor = CFloat(0.05,
                        desc="""scale factor of the glyphs used to represent
                        the vertices, in fancy_mesh mode. """)

    tube_radius = Trait(0.025, CFloat, None,
                        help="""radius of the tubes used to represent the
                        lines, in mesh mode. If None, simple lines are used.
                        """)

    scalars = Array(help="""optional scalar data.""")

    mask = Array(help="""boolean mask array to suppress some data points.
                 Note: this works based on colormapping of scalars and will
                 not work if you specify a solid color using the
                 `color` keyword.""")

    representation = Trait('surface', 'wireframe', 'points', 'mesh',
                    'fancymesh',
                    desc="""the representation type used for the surface.""")

    _source_function = Callable(grid_source)

    _pipeline = [ExtractEdgesFactory, GlyphFactory, TubeFactory,
                        SurfaceFactory]

    def __call_internal__(self, *args, **kwargs):
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
            self.pipeline = [PolyDataNormalsFactory, ] + self.pipeline
        else:
            if self.kwargs['tube_radius'] is None:
                self.pipeline.remove(TubeFactory)
            if not self.kwargs['representation'] == 'fancymesh':
                self.pipeline.remove(GlyphFactory)
            self.kwargs['representation'] = 'surface'
        return self.build_pipeline()


mesh = document_pipeline(Mesh())


def test_mesh():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = np.pi
    cos = np.cos
    sin = np.sin
    dphi, dtheta = pi / 250.0, pi / 250.0
    [phi, theta] = np.mgrid[0:pi + dphi * 1.5:dphi,
                            0:2 * pi + dtheta * 1.5:dtheta]
    m0 = 4
    m1 = 3
    m2 = 2
    m3 = 3
    m4 = 6
    m5 = 2
    m6 = 6
    m7 = 4
    r = sin(m0 * phi) ** m1 + cos(m2 * phi) ** m3 + \
        sin(m4 * theta) ** m5 + cos(m6 * theta) ** m7
    x = r * sin(phi) * cos(theta)
    y = r * cos(phi)
    z = r * sin(phi) * sin(theta)

    return mesh(x, y, z, colormap="bone")


def test_mesh_sphere(r=1.0, npts=(100, 100), colormap='jet'):
    """Create a simple sphere."""
    pi = np.pi
    cos = np.cos
    sin = np.sin
    np_phi = npts[0] * 1j
    np_theta = npts[1] * 1j
    phi, theta = np.mgrid[0:pi:np_phi, 0:2 * pi:np_theta]
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)
    return mesh(x, y, z, colormap=colormap)

@animate
def test_mesh_sphere_anim(obj=None, r=1.0, npts=(100, 100), colormap='jet'):
    """Create a simple sphere and animate it."""
    obj = obj if obj is not None else test_mesh_sphere(r, npts, colormap)
    pi = np.pi
    cos = np.cos
    np_phi = npts[0] * 1j
    np_theta = npts[1] * 1j
    phi, theta = np.mgrid[0:pi:np_phi, 0:2 * pi:np_theta]

    ms = obj.mlab_source
    for i in range(1, 10):
        z = (r + i * 0.25) * cos(phi)
        ms.trait_set(z=z, scalars=z)
        yield

def test_mesh_mask_custom_colors(r=1.0, npts=(100, 100)):
    """Create a sphere with masking and using a custom colormap.

    Note that masking works only when scalars are set.  The custom colormap
    illustrates how one can completely customize the colors with numpy arrays.
    In this case we use a simple 2 color colormap.
    """
    # Create the data like for test_mesh_sphere.
    pi = np.pi
    cos = np.cos
    sin = np.sin
    np_phi = npts[0] * 1j
    np_theta = npts[1] * 1j
    phi, theta = np.mgrid[0:pi:np_phi, 0:2 * pi:np_theta]
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)

    # Setup the mask array.
    mask = np.zeros_like(x).astype(bool)
    mask[::5] = True
    mask[:,::5] = True

    # Create the mesh with the default colormapping.
    m = mesh(x, y, z, scalars=z, mask=mask)

    # Setup the colormap. This is an array of (R, G, B, A) values (each in
    # range 0-255), there should be at least 2 colors in the array.  If you
    # want a constant color set the two colors to the same value.
    colors = np.zeros((2, 4), dtype='uint8')
    colors[0,2] = 255
    colors[1,1] = 255
    # Set the alpha value to fully visible.
    colors[:,3] = 255

    # Now setup the lookup table to use these colors.
    m.module_manager.scalar_lut_manager.lut.table = colors
    return m


def test_fancy_mesh():
    """Create a fancy looking mesh using mesh (example taken from octaviz)."""
    pi = np.pi
    cos = np.cos
    du, dv = pi / 20.0, pi / 20.0
    u, v = np.mgrid[0.01:pi + du * 1.5:du, 0:2 * pi + dv * 1.5:dv]
    x = (1 - cos(u)) * cos(u + 2 * pi / 3) * cos(v + 2 * pi / 3.0) * 0.5
    y = (1 - cos(u)) * cos(u + 2 * pi / 3) * cos(v - 2 * pi / 3.0) * 0.5
    z = -cos(u - 2 * pi / 3.)

    m = mesh(x, y, z, representation='fancymesh',
                   tube_radius=0.0075, colormap="RdYlGn")
    return m


#############################################################################
class ContourSurf(Pipeline):
    """
    Plots a the contours of a surface using grid-spaced data for
    elevation supplied as a 2D array.

    **Function signatures**::

        contour_surf(s, ...)
        contour_surf(x, y, s, ...)
        contour_surf(x, y, f, ...)

    s is the elevation matrix, a 2D array. The contour lines plotted
    are lines of equal s value.

    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value. For
    arbitrary-shaped position arrays (non-orthogonal grids), see the mesh
    function.

    If only 1 array s is passed, the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.

    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinates of positions corresponding to the s values."""

    _source_function = Callable(array2d_source)

    _pipeline = [WarpScalarFactory, ContourSurfaceFactory]


contour_surf = document_pipeline(ContourSurf())


def test_contour_surf():
    """Test contour_surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = np.sin, np.cos
        return sin(x + y) + sin(2 * x - y) + cos(3 * x + 4 * y)

    x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = contour_surf(x, y, f)
    return s

#############################################################################

# Expose only the glyphs that make (more or less) sense for a barchart.
bar_mode_dict = dict()
for item in ('cube', '2dtriangle', '2dsquare', '2dvertex', '2dthick_cross',
             '2ddiamond', '2dcross', '2dcircle'):
    bar_mode_dict[item] = glyph_mode_dict[item]


class BarChart(Pipeline):
    """
    Plots vertical glyphs (like bars) scaled vertical, to do
    histogram-like plots.

    This functions accepts a wide variety of inputs, with positions given
    in 2-D or in 3-D.

    **Function signatures**::

        barchart(s, ...)
        barchart(x, y, s, ...)
        barchart(x, y, f, ...)
        barchart(x, y, z, s, ...)
        barchart(x, y, z, f, ...)

    If only one positional argument is passed, it can be a 1-D, 2-D, or 3-D
    array giving the length of the vectors. The positions of the data
    points are deducted from the indices of array, and an
    uniformly-spaced data set is created.

    If 3 positional arguments (x, y, s) are passed the last one must be
    an array s, or a callable, f, that returns an array. x and y give the
    2D coordinates of positions corresponding to the s values.

    If 4 positional arguments (x, y, z, s) are passed, the 3 first are
    arrays giving the 3D coordinates of the data points, and the last one
    is an array s, or a callable, f, that returns an array giving the
    data value.
    """

    _source_function = Callable(vertical_vectors_source)

    _pipeline = [VectorsFactory, ]

    mode = Trait('cube', bar_mode_dict,
                    desc='The glyph used to represent the bars.')

    lateral_scale = CFloat(0.9, desc='The lateral scale of the glyph, '
                'in units of the distance between nearest points')

    auto_scale = Bool(True, desc='whether to compute automatically the '
                           'lateral scaling of the glyphs. This might be '
                           'computationally expensive.')

    def __call_internal__(self, *args, **kwargs):
        """ Override the call to be able to scale automatically the axis.
        """
        g = Pipeline.__call_internal__(self, *args, **kwargs)
        gs = g.glyph.glyph_source
        # Use a cube source for glyphs.
        if not 'mode' in kwargs:
            gs.glyph_source = gs.glyph_dict['cube_source']
        # Position the glyph tail on the point.
        gs.glyph_position = 'tail'
        gs.glyph_source.center = (0.0, 0.0, 0.5)
        g.glyph.glyph.orient = False
        if not 'color' in kwargs:
            g.glyph.color_mode = 'color_by_scalar'
        if not 'scale_mode' in kwargs:
            g.glyph.scale_mode = 'scale_by_vector_components'
        g.glyph.glyph.clamping = False
        # The auto-scaling code. It involves finding the minimum
        # distance between points, which can be very expensive. We
        # shortcut this calculation for structured data
        if len(args) == 1 or self.auto_scale:
            min_axis_distance = 1
        else:
            x, y, z = g.mlab_source.x, g.mlab_source.y, g.mlab_source.z
            min_axis_distance = \
                    tools._min_axis_distance(x, y, z)
        scale_factor = g.glyph.glyph.scale_factor * min_axis_distance
        lateral_scale = kwargs.pop('lateral_scale', self.lateral_scale)
        try:
            g.glyph.glyph_source.glyph_source.y_length = \
                    lateral_scale / (scale_factor)
            g.glyph.glyph_source.glyph_source.x_length = \
                    lateral_scale / (scale_factor)
        except TraitError:
            " Not all types of glyphs have controlable y_length and x_length"

        return g

barchart = document_pipeline(BarChart())


def test_barchart():
    """ Demo the bar chart plot with a 2D array.
    """
    s = np.abs(np.random.random((3, 3)))
    return barchart(s)


#############################################################################
class TriangularMesh(Mesh):
    """
    Plots a surface using a mesh defined by the position of its vertices
    and the triangles connecting them.

    **Function signatures**::

        triangular_mesh(x, y, z, triangles ...)

    x, y, z are arrays giving the positions of the vertices of the surface.
    triangles is a list of triplets (or an array) list the vertices in
    each triangle. Vertices are indexes by their appearance number in the
    position arrays.

    For simple structures (such as rectangular grids) prefer the surf or
    mesh functions, as they will create more efficient data structures.
    """

    _source_function = Callable(triangular_mesh_source)

triangular_mesh = document_pipeline(TriangularMesh())


def test_triangular_mesh():
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 8
    t = np.linspace(-np.pi, np.pi, n)
    z = np.exp(1j * t)
    x = z.real.copy()
    y = z.imag.copy()
    z = np.zeros_like(x)

    triangles = [(0, i, i + 1) for i in range(1, n)]
    x = np.r_[0, x]
    y = np.r_[0, y]
    z = np.r_[1, z]
    t = np.r_[0, t]

    return triangular_mesh(x, y, z, triangles, scalars=t)


def set_picker_props(figure=None, pick_type="point_picker", tolerance=0.025, text_color=None):
    if figure is None:
        figure = tools.gcf()
    figure.scene.picker.set_picker_props(pick_type, tolerance, text_color)
