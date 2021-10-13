"""A module that provides Matlab like 3d visualization functionality.

The general idea is shamelessly stolen from the `high-level API`_
provided by Octaviz_. Some of the test cases and demos are also
translated from there!

.. _Octaviz: http://octaviz.sourceforge.net/
.. _high-level API: http://octaviz.sourceforge.net/index.php?page=manpagesq

The implementation provided here is object oriented and each
visualization capability is implemented as a class that has traits.
So each of these may be configured.  Each visualization class derives
(ultimately) from MLabBase which is responsible for adding/removing
its actors into the render window.  The classes all require that the
RenderWindow be a `pyface.tvtk.scene.Scene` instance (this constraint
can be relaxed if necessary later on).

This module offers the following broad class of functionality:

`Figure`
  This basically manages all of the objects rendered.  Just like
  figure in any Matlab like environment.  A convenience function
  called `figure` may be used to create a nice Figure instance.

`Glyphs`
  This and its subclasses let one place glyphs at points specified as
  inputs.  The subclasses are: `Arrows`, `Cones`, `Cubes`,
  `Cylinders`, `Spheres`, and `Points`.

`Line3`
  Draws lines between the points specified at initialization time.

`Outline`
  Draws an outline for the contained objects.

`Title`
  Draws a title for the entire figure.

`LUTBase`
  Manages a lookup table and a scalar bar (legend) for it.  This is
  subclassed by all classes that need a LUT.

`SurfRegular`
  MayaVi1's imv.surf like functionality that plots surfaces given x
  (1D), y(1D) and z (or a callable) arrays.

`SurfRegularC`
  Also plots contour lines.

`TriMesh`
  Given triangle connectivity and points, plots a mesh of them.

`FancyTriMesh`
  Plots the mesh using tubes and spheres so its fancier.

`Mesh`
  Given x, y generated from numpy.mgrid, and a z to go with it.  Along
  with optional scalars.  This class builds the triangle connectivity
  (assuming that x, y are from numpy.mgrid) and builds a mesh and
  shows it.

`FancyMesh`
  Like mesh but shows the mesh using tubes and spheres.

`Surf`
  This generates a surface mesh just like Mesh but renders the mesh as
  a surface.

`Contour3`
  Shows contour for a mesh.

`ImShow`
  Allows one to view large numeric arrays as image data using an image
  actor.  This is just like MayaVi1's `mayavi.tools.imv.viewi`.

To see nice examples of all of these look at the `test_*` functions at
the end of this file.  Here is a quick example that uses these test
functions::

 >>> from tvtk.tools import mlab
 >>> f = mlab.figure()
 >>> mlab.test_surf(f) # Create a spherical harmonic.
 >>> f.pop() # Remove it.
 >>> mlab.test_molecule(f) # Show a caffeine molecule.
 >>> f.renwin.reset_zoom() # Scale the view.
 >>> f.pop() # Remove this.
 >>> mlab.test_lines(f) # Show pretty lines.
 >>> f.clear() # Remove all the stuff on screen.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

import numpy

from traits.api import HasTraits, List, Instance, Any, Float, Bool, \
                                 Str, Trait, Int
from pyface.api import GUI

from tvtk.api import tvtk
from tvtk.tvtk_base import TVTKBase, vtk_color_trait
from tvtk.common import configure_input_data
from tvtk.tools import ivtk

# Set this to False to not use LOD Actors.
USE_LOD_ACTOR = True


######################################################################
# Utility functions.
######################################################################
def _make_actor(**kwargs):
    """Return a TVTK actor.  If `mlab.USE_LOD_ACTOR` is `True` it
    returns an LODActor if not it returns a normal actor.
    """
    if USE_LOD_ACTOR:
        r = tvtk.LODActor(number_of_cloud_points=1500)
        r.property.point_size = 2.0
        r.trait_set(**kwargs)
        return r
    else:
        return tvtk.Actor(**kwargs)


def _create_structured_points_direct(x, y, z=None):
    """Creates a StructuredPoints object given input data in the form
    of numpy arrays.

    Input Arguments:
       x -- Array of x-coordinates.  These should be regularly spaced.

       y -- Array of y-coordinates.  These should be regularly spaced.

       z -- Array of z values for the x, y values given.  The values
       should be computed such that the z values are computed as x
       varies fastest and y next.  If z is None then no scalars are
       associated with the structured points.  Only the structured
       points data set is created.
    """

    nx = len(x)
    ny = len(y)
    if z is not None:
        nz = numpy.size(z)
        assert nx*ny == nz, "len(x)*len(y) != len(z)"\
               "You passed nx=%d, ny=%d,  nz=%d"%(nx, ny, nz)

    xmin, ymin = x[0], y[0]
    dx, dy= (x[1] - x[0]), (y[1] - y[0])

    sp = tvtk.StructuredPoints(dimensions=(nx,ny,1),
                               origin=(xmin, ymin, 0),
                               spacing=(dx, dy, 1))
    if z is not None:
        sp.point_data.scalars = numpy.ravel(z)
        sp.point_data.scalars.name = 'scalars'
    return sp


def sampler(xa, ya, func, *args, **kwargs):
    """Samples a function at an array of ordered points (with equal
    spacing) and returns an array of scalars as per VTK's requirements
    for a structured points data set, i.e. x varying fastest and y
    varying next.

    Input Arguments:
        xa -- Array of x points.

        ya -- Array if y points.

        func -- function of x, and y to sample.

        args -- additional positional arguments for func()
        (default is empty)

        kwargs -- a dict of additional keyword arguments for func()
        (default is empty)
    """
    ret = func(xa[:,None] + numpy.zeros_like(ya),
               numpy.transpose(ya[:,None] + numpy.zeros_like(xa)),
               *args, **kwargs
               )
    return numpy.transpose(ret)


def _check_sanity(x, y, z):
    """Checks the given arrays to see if they are suitable for
    surf."""
    msg = "Only ravelled or 2D arrays can be viewed! "\
          "This array has shape %s" % str(z.shape)
    assert len(z.shape) <= 2, msg

    if len( z.shape ) == 2:
        msg = "len(x)*len(y) != len(z.flat).  You passed "\
              "nx=%d, ny=%d, shape of z=%s"%(len(x), len(y), z.shape)
        assert z.shape[0]*z.shape[1] == len(x)*len(y), msg

        msg = "length of y(%d) and x(%d) must match shape of z "\
              "%s. (Maybe you need to swap x and y?)"%(len(y), len(x),
                                                        str(z.shape))
        assert z.shape == (len(y), len(x)), msg


def squeeze(a):
    "Returns a with any ones from the shape of a removed"
    a = numpy.asarray(a)
    b = numpy.asarray(a.shape)
    val = numpy.reshape(a,
                          tuple(numpy.compress(numpy.not_equal(b, 1), b)))
    return val


def make_surf_actor(x, y, z, warp=1, scale=[1.0, 1.0, 1.0],
                    make_actor=True, *args, **kwargs):
    """Creates a surface given regularly spaced values of x, y and the
    corresponding z as arrays.  Also works if z is a function.
    Currently works only for regular data - can be enhanced later.

    Parameters
    ----------

        x -- Array of x points (regularly spaced)

        y -- Array if y points (regularly spaced)

        z -- A 2D array for the x and y points with x varying fastest
        and y next.  Also will work if z is a callable which supports
        x and y arrays as the arguments.

        warp -- If true, warp the data to show a 3D surface
        (default = 1).

        scale -- Scale the x, y and z axis as per passed values.
        Defaults to [1.0, 1.0, 1.0].

        make_actor -- also create actors suitably (default True)

        args -- additional positional arguments for func()
        (default is empty)

        kwargs -- a dict of additional keyword arguments for func()
        (default is empty)
    """

    if callable(z):
        zval = numpy.ravel(sampler(x, y, z, *args, **kwargs))
        x, y = squeeze(x), squeeze(y)
    else:
        x, y = squeeze(x), squeeze(y)
        _check_sanity(x, y, z)
        zval = numpy.ravel(z)
        assert len(zval) > 0, "z is empty - nothing to plot!"

    xs = x*scale[0]
    ys = y*scale[1]
    data = _create_structured_points_direct(xs, ys, zval)
    if not make_actor:
        return data
    if warp:
        geom_f = tvtk.ImageDataGeometryFilter()
        configure_input_data(geom_f, data)

        warper = tvtk.WarpScalar(scale_factor=scale[2])
        configure_input_data(warper, geom_f.output)
        normals = tvtk.PolyDataNormals(feature_angle=45)
        configure_input_data(normals, warper.output)

        mapper = tvtk.PolyDataMapper(scalar_range=(min(zval),max(zval)))
        configure_input_data(mapper, normals.output)
    else:
        mapper = tvtk.PolyDataMapper(scalar_range=(min(zval),max(zval)))
        configure_input_data(mapper, data)
    actor = _make_actor(mapper=mapper)
    return data, actor


def make_triangle_polydata(triangles, points, scalars=None):
    t = numpy.asarray(triangles, 'l')
    assert t.shape[1] == 3, "The list of polygons must be Nx3."

    if scalars is not None:
        assert len(points) == len(numpy.ravel(scalars))

    pd = tvtk.PolyData(points=points, polys=t)
    if scalars is not None:
        pd.point_data.scalars = numpy.ravel(scalars)
        pd.point_data.scalars.name = 'scalars'
    return pd


def make_triangles_points(x, y, z, scalars=None):
    """Given x, y, and z co-ordinates made using numpy.mgrid and
    optional scalars.  This function returns triangles and points
    corresponding to a mesh formed by them.

    Parameters
    ----------

    - x : array
        A list of x coordinate values formed using numpy.mgrid.
    - y : array
        A list of y coordinate values formed using numpy.mgrid.
    - z : array
        A list of z coordinate values formed using numpy.mgrid.
    - scalars : array (optional)
        Scalars to associate with the points.
    """
    assert len(x.shape) == 2, "Array x must be 2 dimensional."
    assert len(y.shape) == 2, "Array y must be 2 dimensional."
    assert len(z.shape) == 2, "Array z must be 2 dimensional."
    assert x.shape == y.shape, "Arrays x and y must have same shape."
    assert y.shape == z.shape, "Arrays y and z must have same shape."

    nx, ny = x.shape
    i, j = numpy.mgrid[0:nx-1,0:ny-1]
    i, j = numpy.ravel(i), numpy.ravel(j)
    t1 = i*ny+j, (i+1)*ny+j, (i+1)*ny+(j+1)
    t2 = (i+1)*ny+(j+1), i*ny+(j+1), i*ny+j
    nt = len(t1[0])
    triangles = numpy.zeros((nt*2, 3), 'l')
    triangles[0:nt,0], triangles[0:nt,1], triangles[0:nt,2] = t1
    triangles[nt:,0], triangles[nt:,1], triangles[nt:,2] = t2

    points = numpy.zeros((nx, ny, 3), 'd')
    points[:,:,0], points[:,:,1], points[:,:,2] = x, y, z
    points = numpy.reshape(points, (nx*ny, 3))

    return triangles, points



######################################################################
# `MLabBase` class.
######################################################################
class MLabBase(HasTraits):
    # List of actors.
    actors = List(TVTKBase)
    # Renderwindow to render into.
    renwin = Any

    def update(self):
        self.renwin.render()

    def render(self):
        if self.renwin:
            self.renwin.render()

    def _renwin_changed(self, old, new):
        if old:
            old.remove_actors(self.actors)
            old.render()
        if new:
            new.add_actors(self.actors)
            new.render()

    def _actors_changed(self, old, new):
        self._handle_actors(old, new)

    def _actors_items_changed(self, list_event):
        self._handle_actors(list_event.removed, list_event.added)

    def _handle_actors(self, removed, added):
        rw = self.renwin
        if rw:
            rw.remove_actors(removed)
            rw.add_actors(added)
            rw.render()



######################################################################
# `Glyphs` class.
######################################################################
class Glyphs(MLabBase):
    # The source glyph which is placed at various locations.
    glyph_source = Any

    # A Glyph3D instance replicates the glyph_sources at various
    # points.
    glyph = Instance(tvtk.Glyph3D, (), {'vector_mode':'use_vector',
                                        'scale_mode':'data_scaling_off'})

    # Color of the glyphs.
    color = vtk_color_trait((1.0, 1.0, 1.0))

    def __init__(self, points, vectors=None, scalars=None, **traits):
        super(Glyphs, self).__init__(**traits)

        if vectors is not None:
            assert len(points) == len(vectors)
        if scalars is not None:
            assert len(points) == len(scalars)

        self.points = points
        self.vectors = vectors
        self.scalars = scalars

        polys = numpy.arange(0, len(points), 1, 'l')
        polys = numpy.reshape(polys, (len(points), 1))
        pd = tvtk.PolyData(points=points, polys=polys)
        if self.vectors is not None:
            pd.point_data.vectors = vectors
            pd.point_data.vectors.name = 'vectors'
        if self.scalars is not None:
            pd.point_data.scalars = scalars
            pd.point_data.scalars.name = 'scalars'

        self.poly_data = pd

        configure_input_data(self.glyph, pd)
        if self.glyph_source:
            self.glyph.source = self.glyph_source.output

        mapper = tvtk.PolyDataMapper(input=self.glyph.output)
        actor = _make_actor(mapper=mapper)
        actor.property.color = self.color
        self.actors.append(actor)

    def update(self):
        self.poly_data.update()
        self.renwin.render()

    def _color_changed(self, val):
        if self.actors:
            self.actors[0].property.color = val
        self.render()

    def _glyph_source_changed(self, val):
        self.glyph.source = val.output
        self.render()


######################################################################
# `Arrows` class.
######################################################################
class Arrows(Glyphs):
    # The arrow glyph which is placed at various locations.
    glyph_source = Instance(tvtk.ArrowSource, ())

######################################################################
# `Cones` class.
######################################################################
class Cones(Glyphs):
    # The cone glyph which is placed at various locations.
    glyph_source = Instance(tvtk.ConeSource, ())

    # Radius of the cone.
    radius = Float(0.05, desc='radius of the cone')

    def __init__(self, points, vectors=None, scalars=None, **traits):
        super(Cones, self).__init__(points, vectors, scalars, **traits)
        self._radius_changed(self.radius)

    def _radius_changed(self, val):
        self.glyph_source.radius = val
        self.render()


######################################################################
# `Cubes` class.
######################################################################
class Cubes(Glyphs):
    # The cube glyph which is placed at various locations.
    glyph_source = Instance(tvtk.CubeSource, ())
    # The side length of the cube.
    length = Float(0.05, desc='side length of the cube')

    def __init__(self, points, vectors=None, scalars=None, **traits):
        super(Cubes, self).__init__(points, vectors, scalars, **traits)
        self._radius_changed(self.radius)

    def _length_changed(self, val):
        self.glyph_source.x_length = val
        self.glyph_source.y_length = val
        self.glyph_source.z_length = val
        self.render()


######################################################################
# `Cylinders` class.
######################################################################
class Cylinders(Glyphs):
    # The cylinder glyph which is placed at various locations.
    glyph_source = Instance(tvtk.CylinderSource, ())


######################################################################
# `Spheres` class.
######################################################################
class Spheres(Glyphs):
    # The sphere which is placed at various locations.
    glyph_source = Instance(tvtk.SphereSource, (),
                            {'phi_resolution':15,
                             'theta_resolution':30})
    # Radius of the sphere.
    radius = Float(0.05, desc='radius of the sphere')

    def __init__(self, points, vectors=None, scalars=None, **traits):
        super(Spheres, self).__init__(points, vectors, scalars, **traits)
        self._radius_changed(self.radius)

    def _radius_changed(self, val):
        self.glyph_source.radius = val
        self.render()


######################################################################
# `Points` class.
######################################################################
class Points(Glyphs):
    # The point which is placed at various locations.
    glyph_source = Instance(tvtk.PointSource, (),
                            {'radius':0, 'number_of_points':1})


######################################################################
# `Line3` class.
######################################################################
class Line3(MLabBase):
    # Radius of the tube filter.
    radius = Float(0.01, desc='radius of the tubes')
    # Should a tube filter be used or not.
    use_tubes = Bool(True,
                     desc='specifies if the tube filter should be used')

    # The Tube filter used to generate tubes from the lines.
    tube_filter = Instance(tvtk.TubeFilter, (), {'number_of_sides':6})

    # Color of the actor.
    color = vtk_color_trait((1.0, 1.0, 1.0))

    def __init__(self, points, **traits):
        super(MLabBase, self).__init__(**traits)

        assert len(points[0]) == 3, "The points must be 3D"

        self.points = points

        np = len(points) - 1
        lines = numpy.zeros((np, 2), 'l')
        lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
        lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
        pd = tvtk.PolyData(points=points, lines=lines)
        self.poly_data = pd

        mapper = tvtk.PolyDataMapper()
        self.mapper = mapper
        tf = self.tube_filter
        tf.radius = self.radius
        if self.use_tubes:
            configure_input_data(tf, pd)
            configure_input_data(mapper, tf.output)

        a = _make_actor(mapper=mapper)
        a.property.color = self.color
        self.actors.append(a)

    def _radius_changed(self, val):
        self.tube_filter.radius = val
        self.render()

    def _use_tubes_changed(self, val):
        if val:
            tf = self.tube_filter
            configure_input_data(tf, self.poly_data)
            configure_input_data(self.mapper, tf.output)
        else:
            configure_input_data(self.mapper, self.poly_data)
        self.render()

    def _color_changed(self, val):
        if self.actors:
            self.actors[0].property.color = val
        self.render()


######################################################################
# `Outline` class.
######################################################################
class Outline(MLabBase):
    # The axis instance to use to annotate the outline
    axis = Instance(tvtk.CubeAxesActor2D, (),
                    {'label_format':"%4.2g", 'fly_mode':"outer_edges",
                     'font_factor':1.25, 'number_of_labels':5,
                     'corner_offset':0.0, 'scaling':0})
    # The outline source.
    outline = Instance(tvtk.OutlineSource, ())

    def __init__(self, **traits):
        super(Outline, self).__init__(**traits)

        out_mapper = tvtk.PolyDataMapper(input=self.outline.output)
        out_actor = _make_actor(mapper=out_mapper)
        axis = self.axis
        if hasattr(axis, 'view_prop'):
            axis.view_prop = out_actor
        else:
            axis.prop = out_actor

        self.actors.extend([out_actor, axis])

    def update(self):
        if self.renwin:
            rw = self.renwin
            v1, v2 = [x.visibility for x in self.actors]
            self.actors[0].visibility = 0
            self.actors[1].visibility = 0
            rw.render()
            bounds = rw.renderer.compute_visible_prop_bounds()
            self.outline.bounds = bounds
            rw.render()
            self.actors[0].visibility = v1
            self.actors[1].visibility = v2

    def _renwin_changed(self, old, new):
        super(Outline, self)._renwin_changed(old, new)
        if old:
            old.on_trait_change(self.update, 'actor_added', remove=True)
            old.on_trait_change(self.update, 'actor_removed', remove=True)
        if new:
            self.axis.camera = new.renderer.active_camera
            new.on_trait_change(self.update, 'actor_added')
            new.on_trait_change(self.update, 'actor_removed')


######################################################################
# `Title` class.
######################################################################
class Title(MLabBase):
    # Text of the title.
    text = Str('Title', desc='text of the title')

    # The text actor that renders the title.
    text_actor = Instance(tvtk.TextActor, ())

    def __init__(self, **traits):
        super(Title, self).__init__(**traits)

        ta = self.text_actor
        ta.trait_set(text_scale_mode='prop', height=0.05, input=self.text)
        pc = ta.position_coordinate
        pc.coordinate_system = 'normalized_viewport'
        pc.value = 0.25, 0.925, 0.0
        self.actors.append(self.text_actor)

    def _text_changed(self, val):
        self.text_actor.input = val
        self.render()

######################################################################
# `LUTBase` class.
######################################################################
class LUTBase(MLabBase):
    # The choices for the lookuptable
    lut_type = Trait('red-blue', 'red-blue', 'blue-red',
                     'black-white', 'white-black',
                     desc='the type of the lookup table')

    # The LookupTable instance.
    lut = Instance(tvtk.LookupTable, ())

    # The scalar bar.
    scalar_bar = Instance(tvtk.ScalarBarActor, (),
                          {'orientation':'horizontal',
                           'width':0.8, 'height':0.17})

    # The scalar_bar widget.
    scalar_bar_widget = Instance(tvtk.ScalarBarWidget, ())

    # The legend name for the scalar bar.
    legend_text = Str('Scalar', desc='the title of the legend')

    # Turn on/off the visibility of the scalar bar.
    show_scalar_bar = Bool(False,
                           desc='specifies if scalar bar is shown or not')

    def __init__(self, **traits):
        super(LUTBase, self).__init__(**traits)
        self.lut.number_of_colors = 256
        self._lut_type_changed(self.lut_type)
        self.scalar_bar.trait_set(lookup_table=self.lut,
                            title=self.legend_text)
        pc = self.scalar_bar.position_coordinate
        pc.coordinate_system = 'normalized_viewport'
        pc.value = 0.1, 0.01, 0.0
        self.scalar_bar_widget.trait_set(scalar_bar_actor=self.scalar_bar,
                                   key_press_activation=False)

    def _lut_type_changed(self, val):
        if val == 'red-blue':
            hue_range = 0.0, 0.6667
            saturation_range = 1.0, 1.0
            value_range = 1.0, 1.0
        elif val == 'blue-red':
            hue_range = 0.6667, 0.0
            saturation_range = 1.0, 1.0
            value_range = 1.0, 1.0
        elif val == 'black-white':
            hue_range = 0.0, 0.0
            saturation_range = 0.0, 0.0
            value_range = 0.0, 1.0
        elif val == 'white-black':
            hue_range = 0.0, 0.0
            saturation_range = 0.0, 0.0
            value_range = 1.0, 0.0
        lut = self.lut
        lut.trait_set(hue_range=hue_range, saturation_range=saturation_range,
                value_range=value_range, number_of_table_values=256,
                ramp='sqrt')
        lut.force_build()

        self.render()

    def _legend_text_changed(self, val):
        self.scalar_bar.title = val
        self.scalar_bar.modified()
        self.render()

    def _show_scalar_bar_changed(self, val):
        if self.renwin:
            self.scalar_bar_widget.enabled = val
            self.renwin.render()

    def _renwin_changed(self, old, new):
        sbw = self.scalar_bar_widget
        if old:
            sbw.interactor = None
            old.render()
        if new:
            sbw.interactor = new.interactor
            sbw.enabled = self.show_scalar_bar
            new.render()
        super(LUTBase, self)._renwin_changed(old, new)



######################################################################
# `SurfRegular` class.
######################################################################
class SurfRegular(LUTBase):

    def __init__(self, x, y, z, warp=1, scale=[1.0, 1.0, 1.0], f_args=(),
                 f_kwargs=None, **traits):
        super(SurfRegular, self).__init__(**traits)

        if f_kwargs is None:
            f_kwargs = {}

        data, actor = make_surf_actor(x, y, z, warp, scale, *f_args,
                                      **f_kwargs)
        self.data = data
        mapper = actor.mapper
        mapper.lookup_table = self.lut
        self.lut.table_range = mapper.scalar_range

        self.actors.append(actor)


######################################################################
# `SurfRegularC` class.
######################################################################
class SurfRegularC(LUTBase):
    # Number of contours.
    number_of_contours = Int(10, desc='number of contours values')

    # The contour filter.
    contour_filter = Instance(tvtk.ContourFilter, ())

    def __init__(self, x, y, z, warp=1, scale=[1.0, 1.0, 1.0], f_args=(),
                 f_kwargs=None, **traits):
        super(SurfRegularC, self).__init__(**traits)

        if f_kwargs is None:
            f_kwargs = {}

        data, actor = make_surf_actor(x, y, z, warp, scale, *f_args,
                                      **f_kwargs)
        mapper = actor.mapper
        mapper.lookup_table = self.lut
        self.lut.table_range = mapper.scalar_range
        self.data = data

        dr = data.point_data.scalars.range
        cf = self.contour_filter
        configure_input_data(cf, data)
        cf.generate_values(self.number_of_contours, dr[0], dr[1])
        mapper = tvtk.PolyDataMapper(input=cf.output, lookup_table=self.lut)
        cont_actor = _make_actor(mapper=mapper)

        self.actors.extend([actor, cont_actor])

    def _number_of_contours_changed(self, val):
        dr = self.data.point_data.scalars.range
        self.contour_filter.generate_values(val, dr[0], dr[1])
        self.render()


######################################################################
# `TriMesh` class.
######################################################################
class TriMesh(LUTBase):
    # Disables/enables scalar visibility.
    scalar_visibility = Bool(False, desc='show scalar visibility')

    # Representation of the mesh as surface or wireframe.
    surface = Bool(False, desc='show as surface or wireframe')

    # Color of the mesh.
    color = vtk_color_trait((0.5, 1.0, 0.5))

    def __init__(self, triangles, points, scalars=None, **traits):
        """
        Parameters
        ----------

        - triangles : array
          This contains a list of vertex indices forming the triangles.
        - points : array
          Contains the list of points referred to in the triangle list.
        - scalars : array (optional)
          Scalars to associate with the points.
        """
        super(TriMesh, self).__init__(**traits)

        self.pd = make_triangle_polydata(triangles, points, scalars)

        mapper = tvtk.PolyDataMapper(input=self.pd, lookup_table=self.lut,
                                     scalar_visibility=self.scalar_visibility)
        if scalars is not None:
            rs = numpy.ravel(scalars)
            dr = min(rs), max(rs)
            mapper.scalar_range = dr
            self.lut.table_range = dr

        actor = _make_actor(mapper=mapper)
        representation = 'w'
        if self.surface:
            representation = 's'
        if representation == 'w':
            actor.property.trait_set(diffuse=0.0, ambient=1.0, color=self.color,
                               representation=representation)
        else:
            actor.property.trait_set(diffuse=1.0, ambient=0.0, color=self.color,
                               representation=representation)

        self.actors.append(actor)

    def _scalar_visibility_changed(self, val):
        if self.actors:
            mapper = self.actors[0].mapper
            mapper.scalar_visibility = val
        self.render()

    def _surface_changed(self, val):
        if self.actors:
            representation = 'w'
            if val:
                representation = 's'

            actor = self.actors[0]
            if representation == 'w':
                actor.property.trait_set(diffuse=0.0, ambient=1.0,
                                   representation=representation)
            else:
                actor.property.trait_set(diffuse=1.0, ambient=0.0,
                                   representation=representation)
        self.render()

    def _color_changed(self, val):
        if self.actors:
            self.actors[0].property.color = val
        self.render()


######################################################################
# `FancyTriMesh` class.
######################################################################
class FancyTriMesh(LUTBase):
    """Shows a mesh of triangles and draws the edges as tubes and
    points as balls."""
    # Disables/enables scalar visibility.
    scalar_visibility = Bool(False, desc='show scalar visibility')

    # Color of the mesh.
    color = vtk_color_trait((0.5, 1.0, 0.5))

    # The radius of the tubes.
    tube_radius = Float(0.0, desc='radius of the tubes')

    # The radius of the spheres.
    sphere_radius = Float(0.0, desc='radius of the spheres')

    # The TubeFilter used to make the tubes for the edges.
    tube_filter = Instance(tvtk.TubeFilter, (),
                           {'vary_radius':'vary_radius_off',
                            'number_of_sides':6})
    # The sphere source for the points.
    sphere_source = Instance(tvtk.SphereSource, (),
                             {'theta_resolution':12,
                              'phi_resolution':12})

    def __init__(self, triangles, points, scalars=None, **traits):
        """
        Parameters
        ----------

        - triangles : array
          This contains a list of vertex indices forming the triangles.
        - points : array
          Contains the list of points referred to in the triangle list.
        - scalars : array (optional)
          Scalars to associate with the points.
        """
        super(FancyTriMesh, self).__init__(**traits)

        self.points = points
        self.pd = make_triangle_polydata(triangles, points, scalars)

        # Update the radii so the default is computed correctly.
        self._tube_radius_changed(self.tube_radius)
        self._sphere_radius_changed(self.sphere_radius)

        scalar_vis = self.scalar_visibility

        # Extract the edges and show the lines as tubes.
        self.extract_filter = tvtk.ExtractEdges(input=self.pd)
        extract_f = self.extract_filter
        self.tube_filter.trait_set(input=extract_f.output,
                             radius=self.tube_radius)
        edge_mapper = tvtk.PolyDataMapper(input=self.tube_filter.output,
                                          lookup_table=self.lut,
                                          scalar_visibility=scalar_vis)
        edge_actor = _make_actor(mapper=edge_mapper)
        edge_actor.property.color = self.color

        # Create the spheres for the points.
        self.sphere_source.radius = self.sphere_radius
        spheres = tvtk.Glyph3D(scaling=0, source=self.sphere_source.output,
                               input=extract_f.output)
        sphere_mapper = tvtk.PolyDataMapper(input=spheres.output,
                                            lookup_table=self.lut,
                                            scalar_visibility=scalar_vis)
        sphere_actor = _make_actor(mapper=sphere_mapper)
        sphere_actor.property.color = self.color

        if scalars is not None:
            rs = numpy.ravel(scalars)
            dr = min(rs), max(rs)
            self.lut.table_range = dr
            edge_mapper.scalar_range = dr
            sphere_mapper.scalar_range = dr

        self.actors.extend([edge_actor, sphere_actor])

    def _scalar_visibility_changed(self, val):
        if self.actors:
            for i in self.actors:
                i.mapper.scalar_visibility = val
        self.render()

    def _tube_radius_changed(self, val):
        points = self.points
        if val < 1.0e-9:
            val = (max(numpy.ravel(points)) -
                   min(numpy.ravel(points)))/250.0
        self.tube_radius = val
        self.tube_filter.radius = val
        self.render()

    def _sphere_radius_changed(self, val):
        points = self.points
        if val < 1.0e-9:
            val = (max(numpy.ravel(points)) -
                       min(numpy.ravel(points)))/100.0
        self.sphere_radius = val
        self.sphere_source.radius = val
        self.render()

    def _color_changed(self, val):
        if self.actors:
            self.actors[0].property.color = val
        self.render()

######################################################################
# `Mesh` class.
######################################################################
class Mesh(TriMesh):
    def __init__(self, x, y, z, scalars=None, **traits):
        """
        Parameters
        ----------

        - x : array
          A list of x coordinate values formed using numpy.mgrid.
        - y : array
          A list of y coordinate values formed using numpy.mgrid.
        - z : array
          A list of z coordinate values formed using numpy.mgrid.
        - scalars : array (optional)
          Scalars to associate with the points.
        """
        triangles, points = make_triangles_points(x, y, z, scalars)
        super(Mesh, self).__init__(triangles, points, scalars, **traits)


######################################################################
# `FancyMesh` class.
######################################################################
class FancyMesh(FancyTriMesh):
    def __init__(self, x, y, z, scalars=None, **traits):
        """
        Parameters
        ----------

        - x : array
          A list of x coordinate values formed using numpy.mgrid.
        - y : array
          A list of y coordinate values formed using numpy.mgrid.
        - z : array
          A list of z coordinate values formed using numpy.mgrid.
        - scalars : array (optional)
          Scalars to associate with the points.
        """
        triangles, points = make_triangles_points(x, y, z, scalars)
        super(FancyMesh, self).__init__(triangles, points, scalars, **traits)


######################################################################
# `Surf` class.
######################################################################
class Surf(LUTBase):
    # Disables/enables scalar visibility.
    scalar_visibility = Bool(True, desc='show scalar visibility')

    # Color of the mesh.
    color = vtk_color_trait((0.5, 1.0, 0.5))

    def __init__(self, x, y, z, scalars=None, **traits):
        """
        Parameters
        ----------

        - x : array
          A list of x coordinate values formed using numpy.mgrid.
        - y : array
          A list of y coordinate values formed using numpy.mgrid.
        - z : array
          A list of z coordinate values formed using numpy.mgrid.
        - scalars : array (optional)
          Scalars to associate with the points.
        """
        super(Surf, self).__init__(**traits)
        triangles, points = make_triangles_points(x, y, z, scalars)
        self.pd = make_triangle_polydata(triangles, points, scalars)

        mapper = tvtk.PolyDataMapper(input=self.pd, lookup_table=self.lut,
                                     scalar_visibility=self.scalar_visibility)
        if scalars is not None:
            rs = numpy.ravel(scalars)
            dr = min(rs), max(rs)
            mapper.scalar_range = dr
            self.lut.table_range = dr

        actor = _make_actor(mapper=mapper)
        actor.property.trait_set(color=self.color)
        self.actors.append(actor)

    def _scalar_visibility_changed(self, val):
        if self.actors:
            mapper = self.actors[0].mapper
            mapper.scalar_visibility = val
        self.render()

    def _surface_changed(self, val):
        if self.actors:
            representation = 'w'
            if val:
                representation = 's'
            self.actors[0].property.representation = representation
        self.render()

    def _color_changed(self, val):
        if self.actors:
            self.actors[0].property.color = val
        self.render()


######################################################################
# `Contour3` class.
######################################################################
class Contour3(LUTBase):
    # Number of contours.
    number_of_contours = Int(10, desc='number of contours values')

    # The contour filter.
    contour_filter = Instance(tvtk.ContourFilter, ())

    def __init__(self, x, y, z, scalars, **traits):
        """
        Parameters
        ----------

        - x : array
          A list of x coordinate values formed using numpy.mgrid.
        - y : array
          A list of y coordinate values formed using numpy.mgrid.
        - z : array
          A list of z coordinate values formed using numpy.mgrid.
        - scalars : array
          Scalars to associate with the points.
        """
        super(Contour3, self).__init__(**traits)
        triangles, points = make_triangles_points(x, y, z, scalars)
        self.pd = make_triangle_polydata(triangles, points, scalars)

        dr = self.pd.point_data.scalars.range
        self.lut.table_range = dr

        cf = self.contour_filter
        configure_input_data(cf, self.pd)
        cf.generate_values(self.number_of_contours, dr[0], dr[1])
        mapper = tvtk.PolyDataMapper(input=cf.output, lookup_table=self.lut,
                                     scalar_range=dr)
        cont_actor = _make_actor(mapper=mapper)

        self.actors.append(cont_actor)

    def _number_of_contours_changed(self, val):
        dr = self.pd.point_data.scalars.range
        self.contour_filter.generate_values(val, dr[0], dr[1])
        self.render()


######################################################################
# `ImShow` class.
######################################################################
class ImShow(LUTBase):
    """Allows one to view a 2D numpy array as an image.  This works
    best for very large arrays (like 1024x1024 arrays).
    """

    # Interpolate the image or not.
    interpolate = Bool(False, desc='specifies if image should be interpolated')

    def __init__(self, arr, scale=[1.0, 1.0, 1.0], **traits):
        """
        Parameters
        ----------
        - arr : Array to be viewed.

        - scale : Scale the x, y and z axis as per passed values.
          Defaults to [1.0, 1.0, 1.0].
        """
        super(ImShow, self).__init__(**traits)

        assert len(arr.shape) == 2, "Only 2D arrays can be viewed!"

        ny, nx = arr.shape
        dx, dy, junk = numpy.array(scale)*1.0
        xa = numpy.arange(0, nx*scale[0] - 0.1*dx, dx, 'f')
        ya = numpy.arange(0, ny*scale[1] - 0.1*dy, dy, 'f')

        arr_flat = numpy.ravel(arr)
        min_val = min(arr_flat)
        max_val = max(arr_flat)

        sp = _create_structured_points_direct(xa, ya)
        lut = self.lut
        lut.table_range = min_val, max_val
        a = lut.map_scalars(arr_flat, 0, 0)
        sp.point_data.scalars = a
        sp.point_data.scalars.name = 'scalars'
        sp.scalar_type = 'unsigned_char'
        sp.number_of_scalar_components = 4

        ia = tvtk.ImageActor(input=sp, interpolate=self.interpolate)

        self.actors.append(ia)

    def _interpolate_changed(self, val):
        if self.actors:
            ia = self.actors[0]
            ia.interpolate = val
        self.render()


######################################################################
# `Figure` class.
######################################################################
class Figure(HasTraits):
    """A Figure manages varuous MLabBase objects.  Each of these
    objects contains an actor and does something neat."""

    # The various instances of MLabBase that populate this figure.
    objects = List(MLabBase)

    def __init__(self, renwin, **traits):
        super(Figure, self).__init__(**traits)
        self.renwin = renwin

    def add(self, obj):
        """Add an object to the figure.  This adds the actors of the
        object to the renderwindow."""
        self.objects.append(obj)

    def pop(self):
        """Pops out the last object."""
        return self.objects.pop()

    def clear(self):
        """Removes all objects in the figure."""
        self.objects = []

    def _objects_changed(self, new, old):
        self._handle_objects(new, old)

    def _objects_items_changed(self, list_event):
        self._handle_objects(list_event.removed, list_event.added)

    def _handle_objects(self, removed, added):
        for obj in removed:
            obj.renwin = None
        rw = self.renwin
        for obj in added:
            obj.renwin = rw
        rw.reset_zoom()
        rw.render()


def figure(outline=True, browser=True):
    """Simple helper function that returns a usable figure.

    Parameters
    ----------

    - outline : `bool` (default: True)

      If True, create an outline bounding box along with an axes
      marker for the scene.

    - browser : `bool` (default, True)

      If True, creates an IVTK scene with an embedded PipelineBrowser.
      If False, does not create it.
    """
    v = ivtk.viewer(browser)
    f = Figure(v.scene)
    if outline:
        o = Outline()
        f.add(o)
    v.scene.reset_zoom()
    return f


######################################################################
# Test functions.
######################################################################
def test_arrows(fig):
    a = Arrows([[-1,-1,-1],[1,0,0]], [[1,1,1],[0,1,0]], color=(1,0,0))
    fig.add(a)


def test_lines(fig):
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    pi = numpy.pi
    dphi = pi/1000.0
    phi = numpy.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = numpy.cos(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    y = numpy.sin(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    z = numpy.sin(n_long*mu/n_mer)*0.5

    pts = numpy.zeros((len(mu), 3), 'd')
    pts[:,0], pts[:,1], pts[:,2] = x, y, z

    l = Line3(pts, radius=0.05, color=(0.0, 0.0, 0.8))

    fig.add(l)

def test_molecule(fig):
    """Generates and shows a Caffeine molecule."""
    o = [[30, 62, 19],[8, 21, 10]]
    n = [[31, 21, 11], [18, 42, 14], [55, 46, 17], [56, 25, 13]]
    c = [[5, 49, 15], [30, 50, 16], [42, 42, 15], [43, 29, 13], [18, 28, 12],
         [32, 6, 8], [63, 36, 15], [59, 60, 20]]
    h = [[23, 5, 7], [32, 0, 16], [37, 5, 0], [73, 36, 16], [69, 60, 20],
         [54, 62, 28], [57, 66, 12], [6, 59, 16], [1, 44, 22], [0, 49, 6]]

    oxygen = Spheres(o, radius=8, color=(1,0,0))
    nitrogen = Spheres(n, radius=10, color=(0,0,1))
    carbon = Spheres(c, radius=10, color=(0,1,0))
    hydrogen = Spheres(h, radius=5, color=(1,1,1))

    for i in oxygen, nitrogen, carbon, hydrogen:
        fig.add(i)

def test_trimesh(fig):
    """Test for simple triangle mesh."""
    pts = numpy.array([[0.0,0,0], [1.0,0.0,0.0], [1,1,0]], 'd')
    triangles = [[0, 1, 2]]
    t1 = TriMesh(triangles, pts)
    fig.add(t1)
    pts1 = pts.copy()
    pts1[:,2] = 1.0
    t2 = FancyTriMesh(triangles, pts1)
    fig.add(t2)

def test_surf_regular(fig, contour=1):
    """Test Surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        return numpy.sin(x*y)/(x*y)

    x = numpy.arange(-7., 7.05, 0.1)
    y = numpy.arange(-5., 5.05, 0.05)
    if contour:
        s = SurfRegularC(x, y, f)
    else:
        s = SurfRegular(x, y, f)
    fig.add(s)


def test_simple_surf(fig):
    """Test Surf with a simple collection of points."""
    x, y = numpy.mgrid[0:3:1,0:3:1]
    z = x
    s = Surf(x, y, z, numpy.asarray(z, 'd'))
    fig.add(s)

def test_surf(fig):
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

    s = Surf(x, y, z, z)
    fig.add(s)

def test_mesh_sphere(fig):
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
    s = FancyMesh(x, y, z, z, scalar_visibility=True)
    fig.add(s)

def test_mesh(fig):
    """Create a fancy looking mesh (example taken from octaviz)."""
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin
    du, dv = pi/20.0, pi/20.0
    u, v = numpy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
    x = (1- cos(u))*cos(u+2*pi/3) * cos(v + 2*pi/3.0)*0.5
    y = (1- cos(u))*cos(u+2*pi/3) * cos(v - 2*pi/3.0)*0.5
    z = cos(u-2*pi/3.)

    m = FancyMesh(x, y, z, z, scalar_visibility=True)
    fig.add(m)

def test_imshow(fig):
    """Show a large random array."""
    z_large = numpy.random.random((1024, 512))
    i = ImShow(z_large)
    fig.add(i)


def main():
    gui = GUI()
    # Create and open an application window.
    window = ivtk.IVTKWithCrustAndBrowser(size=(800,600))
    window.open()
    f = Figure(window.scene)

    # Create an outline.
    o = Outline()
    f.add(o)

    # Create some pretty pictures.
    #test_lines(f)
    test_surf(f)

    window.scene.reset_zoom()

    # Start the GUI event loop!
    gui.start_event_loop()


if __name__ == '__main__':
    main()
