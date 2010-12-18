"""A simple wrapper around tvtk.tools.mlab suitable for MayaVi2!  This
is meant to be used from the embedded Python interpreter in MayaVi2 or
from IPython with the "-wthread" switch.

There are several test functions at the end of this file that are
illustrative to look at.

"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

#TODO:  * Add optional scalars to plot3d
#       * Make streamline display colors by default
#       * Investigate why the old surf_regular seemed to give more beautiful 
#         surfaces than the current surf. See for instance the difference 
#         between test_surf_lattice and the old test_surf_regular

# Standard library imports.
import scipy

# Enthought library imports.
from enthought.envisage import get_application
from enthought.tvtk.api import tvtk
from enthought.tvtk.tools import mlab
from enthought.mayavi.modules.axes import Axes
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item, Group

# MayaVi related imports.
from enthought.mayavi.services import IMAYAVI
from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi.filters.filter_base import FilterBase
from enthought.mayavi.modules.surface import Surface
from enthought.mayavi.modules.vectors import Vectors
from enthought.mayavi.modules.iso_surface import IsoSurface
from enthought.mayavi.modules.streamline import Streamline
from enthought.mayavi.modules.glyph import Glyph
from enthought.mayavi.modules.text import Text
from enthought.mayavi.app import Mayavi
from enthought.mayavi.core.source import Source
from enthought.mayavi.core.module import Module
from enthought.mayavi.core.module_manager import ModuleManager
from enthought.mayavi.sources.array_source import ArraySource

__all__ = ["scalarscatter", "vectorscatter", "scalarfield",
    "vectorfield", "isosurface", "vectors", "glyph", "streamline",
    "quiver3d", "points3d", "surf", "contour_surf", "imshow", "outline",
    "axes", "figure", "clf", "savefig", "xlabel", "ylabel", "zlabel",
    "title", "scalarbar", "vectorbar"]


######################################################################
# Application and mayavi instances.

application = get_application()
mayavi = None
if application is not None:
    mayavi = application.get_service(IMAYAVI)


######################################################################
# `ImageActor` class

# This should be added as a new MayaVi module.  It is here for testing
# and further improvements.
class ImageActor(Module):

    # An image actor.
    actor = Instance(tvtk.ImageActor, allow_none=False)

    view = View(Group(Item(name='actor', style='custom',
                           resizable=True),
                      show_labels=False),
                width=500,
                height=500,
                resizable=True)

    def setup_pipeline(self):
        self.actor = tvtk.ImageActor()
        
    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.
        """
        mm = self.module_manager
        if mm is None:
            return
        src = mm.source
        self.actor.input = src.outputs[0]
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    def _actor_changed(self, old, new):
        if old is not None:
            self.actors.remove(old)
        self.actors.append(new)

######################################################################
# Utility functions.
def _make_glyph_data(points, vectors=None, scalars=None):
    """Makes the data for glyphs using mlab.
    """
    g = mlab.Glyphs(points, vectors, scalars)
    return g.poly_data

def _make_default_figure():
    """Checks to see if a valid mayavi instance is running.  If not
    creates a new one.
    """
    global mayavi
    if mayavi is None or application.stopped is not None:
        fig = figure()
        mayavi = get_application().get_service(IMAYAVI)
    return mayavi

def _add_data(tvtk_data, name=''):
    """Add a TVTK data object `tvtk_data` to the mayavi pipleine.
    Give the object a name of `name`.
    """
    if isinstance(tvtk_data, tvtk.Object):
        d = VTKDataSource()
        d.data = tvtk_data
    elif isinstance(tvtk_data, Source):
        d = tvtk_data
    else:
        raise TypeError, \
              "first argument should be either a TVTK object"\
              " or a mayavi source"

    if len(name) > 0:
        d.name = name
    _make_default_figure()
    mayavi.add_source(d)
    return d

def _traverse(node):
    """Traverse a tree accessing the nodes children attribute.
    """
    try:
        for leaf in node.children:
            for leaflet in _traverse(leaf):
                yield leaflet
    except AttributeError:
        pass
    yield node

def _find_data(object):
    """Goes up the vtk pipeline to find the data sources of a given
    object.
    """
    if isinstance(object, ModuleManager):
        inputs = [object.source]
    elif hasattr(object, 'module_manager'):
        inputs = [object.module_manager.source]
    elif hasattr(object, 'data') or isinstance(object, ArraySource):
        inputs = [object]
    else:
        raise TypeError, 'Cannot find data source for given object'
    data_sources = []
    try:
        while True:
            input = inputs.pop()
            if hasattr(input, 'inputs'):
                inputs += input.inputs
            elif hasattr(input, 'image_data'):
                data_sources.append(input.image_data)
            else:
                data_sources.append(input.data)
    except IndexError:
        pass
    return data_sources

def _has_scalar_data(object):
    """Tests if an object has scalar data.
    """
    data_sources = _find_data(object)
    for source in data_sources:
        if source.point_data.scalars is not None:
            return True
        elif source.cell_data.scalars is not None:
            return True
    return False

def _has_vector_data(object):
    """Tests if an object has vector data.
    """
    data_sources = _find_data(object)
    for source in data_sources:
        if source.point_data.vectors is not None:
            return True
        elif source.cell_data.vectors is not None:
            return True
    return False

def _has_tensor_data(object):
    """Tests if an object has tensor data.
    """
    data_sources = _find_data(object)
    for source in data_sources:
        if source.point_data.tensors is not None:
            return True
        elif source.cell_data.tensors is not None:
            return True
    return False

def _find_module_manager(object=None, data_type=None):
    """If an object is specified, returns its module_manager, elsewhere finds
    the first module_manager in the scene.
    """
    if object is None:
        for object in _traverse(gcf()):
            if isinstance(object, ModuleManager):
                if ((data_type == 'scalar' and not _has_scalar_data(object))    
                  or (data_type == 'vector' and not _has_vector_data(object))
                  or (data_type == 'tensor' and not _has_tensor_data(object))):
                    continue
                return object
        else:
            print("No object in the scene has a color map")
    else:
        if hasattr(object, 'module_manager'):
            if ((data_type == 'scalar' and _has_scalar_data(object))
               or (data_type == 'vector' and _has_vector_data(object))
               or (data_type == 'tensor' and _has_tensor_data(object))
                or data_type is None):
                return object.module_manager
            else:
                print("This object has no %s data" % data_type)
        else:
            print("This object has no color map")
    return None

def _orient_colorbar(colorbar, orientation):
    """Orients the given colorbar (make it horizontal or vertical).
    """
    if orientation == "vertical":
        colorbar.orientation = "vertical"
        colorbar.width = 0.1
        colorbar.height = 0.8
        colorbar.position = (0.01, 0.15)
    elif orientation == "horizontal":
        colorbar.orientation = "horizontal"
        colorbar.width = 0.8
        colorbar.height = 0.17
        colorbar.position = (0.1, 0.01)
    else:
        print "Unknown orientation"
    gcf().render()

def _typical_distance(data_obj):
    """ Returns a typical distance in a cloud of points.
        This is done by taking the size of the bounding box, and dividing it
        by the cubic root of the number of points.
    """
    x_min, x_max, y_min, y_max, z_min, z_max = data_obj.bounds
    distance = scipy.sqrt(((x_max-x_min)**2 + (y_max-y_min)**2 +
                           (z_max-z_min)**2)/(4*
                           data_obj.number_of_points**(0.33)))
    if distance == 0:
        return 1
    else:
        return 0.4*distance

######################################################################
# Data creation

def scalarscatter(*args, **kwargs):
    """
    Creates scattered scalar data.

    Function signatures
    -------------------

        scalarscatter(s, ...)
        scalarscatter(x, y, z, s, ...)
        scalarscatter(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.

    Arguments
    ---------
 
        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- z coordinates of the points of the mesh (optional).
        
        s -- scalar value

        f -- callable that is used to build the scalar data (only if 4 
             positional arguments are passed).

    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Scattered scalars'

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

    """
    if len(args)==1:
        s = args[0]
        x, y, z = scipy.indices(s.shape)
    elif len(args)==4:
        x, y, z, s = args
        if callable(s):
            s = f(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"
    
    assert ( x.shape == y.shape and
             y.shape == z.shape and
             s.shape == z.shape ), "argument shape are not equal"

    if 'extent' in kwargs:
        xmin, xmax, ymin, ymax, zmin, zmax = kwargs.pop('extent')
        x = xmin + x*(xmax - xmin)/float(x.max() - x.min()) -x.min()
        y = ymin + y*(ymax - ymin)/float(y.max() - y.min()) -y.min()
        z = zmin + z*(zmax - zmin)/float(z.max() - z.min()) -z.min()

    points = scipy.c_[x.ravel(), y.ravel(), z.ravel()]
    scalars = s.ravel()
    name = kwargs.pop('name', 'Scattered scalars')

    data = _make_glyph_data(points, None, scalars)
    data_obj = _add_data(data, name)
    return data_obj

def vectorscatter(*args, **kwargs):
    """
    Creates scattered vector data.

    Function signatures
    -------------------

        vectorscatter(u, v, w, ...)
        vectorscatter(x, y, z, u, v, w, ...)
        vectorscatter(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors.

    Arguments
    ---------
 
        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- z coordinates of the points of the mesh (optional).
        
        u -- x coordinnate of the vector field

        v -- y coordinnate of the vector field

        w -- z coordinnate of the vector field

        f -- callable that is used to build the vector field (only if 4 
             positional arguments are passed).

    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Scattered vector'

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

        scalars -- The scalars associated to the vectors. Defaults to none. 

    """
    if len(args)==3:
        u, v, w = args
        x, y, z = scipy.indices(u.shape)
    elif len(args)==6:
        x, y, z, u, v, w = args
    elif len(args)==4:
        x, y, z, f = args
        assert callable(f), "when used with 4 arguments last argument must be callable"
        u, v, w = f(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"
    
    assert ( x.shape == y.shape and
             y.shape == z.shape and
             z.shape == u.shape and
             u.shape == v.shape and
             v.shape == w.shape ), "argument shape are not equal"

    if 'extent' in kwargs:
        xmin, xmax, ymin, ymax, zmin, zmax = kwargs.pop('extent')
        x = xmin + x*(xmax - xmin)/float(x.max() - x.min()) -x.min()
        y = ymin + y*(ymax - ymin)/float(y.max() - y.min()) -y.min()
        z = zmin + z*(zmax - zmin)/float(z.max() - z.min()) -z.min()

    points = scipy.c_[x.ravel(), y.ravel(), z.ravel()]
    vectors = scipy.c_[u.ravel(), v.ravel(), w.ravel()]
    if 'scalars' in kwargs:
        scalars = kwargs['scalars'].ravel()
    else:
        scalars = None
    name = kwargs.pop('name', 'Scattered vectors')

    data = _make_glyph_data(points, vectors, scalars)
    data_obj = _add_data(data, name)
    return data_obj

def scalarfield(*args, **kwargs):
    """
    Creates a scalar field data.

    Function signatures
    -------------------

        scalarfield(s, ...)
        scalarfield(x, y, z, s, ...)
        scalarfield(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to
    be made from the indices of the s array.

    If the x, y and z arrays are passed they are supposed to have been
    generated by  `numpy.mgrid`.  The function builds a scalar field assuming 
    the points are regularly spaced.

    Arguments
    ---------
 
        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- z coordinates of the points of the mesh (optional).
        
        s -- scalar values.

        f -- callable that is used to build the scalar field (only if 4 
             positional arguments are passed).

    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Scalar field'

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.
    """

    # Get the keyword args.
    name = kwargs.get('name', 'Scalar field')

    if len(args)==1:
        s = args[0]
        x, y, z = scipy.indices(s.shape)
    elif len(args)==4:
        x, y, z, s = args
        if callable(s):
            s = f(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"
    
    assert ( x.shape == y.shape and
             y.shape == z.shape and
             s.shape == z.shape ), "argument shape are not equal"

    if 'extent' in kwargs:
        xmin, xmax, ymin, ymax, zmin, zmax = kwargs.pop('extent')
        x = xmin + x*(xmax - xmin)/float(x.max() - x.min()) -x.min()
        y = ymin + y*(ymax - ymin)/float(y.max() - y.min()) -y.min()
        z = zmin + z*(zmax - zmin)/float(z.max() - z.min()) -z.min()

    points = scipy.c_[x.ravel(), y.ravel(), z.ravel()]
    dx = x[1, 0, 0] - x[0, 0, 0]
    dy = y[0, 1, 0] - y[0, 0, 0]
    dz = z[0, 0, 1] - z[0, 0, 0]

    data = ArraySource(scalar_data=s,
                      origin=[points[0, 0], points[0, 1], points[0, 2]],
                      spacing=[dx, dy, dz])
    data_obj = _add_data(data, name)
    return data_obj

def vectorfield(*args, **kwargs):
    """
    Creates a vector field data.

    Function signatures
    -------------------

        vectorfield(u, v, w, ...)
        vectorfield(x, y, z, u, v, w, ...)
        vectorfield(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to
    be made from the indices of the u, v, w arrays.
        
    If the x, y and z arrays are passed they are supposed to have been
    generated by  `numpy.mgrid`.  The function builds a vector field assuming 
    the points are regularly spaced.

    Arguments
    ---------
 
        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- z coordinates of the points of the mesh (optional).
        
        u -- x coordinnate of the vector field

        v -- y coordinnate of the vector field

        w -- z coordinnate of the vector field

        f -- callable that is used to build the vector field (only if 4 
             positional arguments are passed).

    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Vector field'

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

        scalars -- The scalars associated to the vectors. Defaults to none. 

        transpose_vectors -- If the additional argument
                             transpose_vectors is passed, then the
                             input vectors array is suitably
                             transposed.  By default transpose_vectors
                             is True so that the array is in the
                             correct format that VTK expects.
                             However, a transposed array is not
                             contiguous and thus a copy is made, this
                             also means that any changes to the users
                             input array will will not be reflected in
                             the renderered object (provided you know
                             how to do this).  Thus, sometimes users
                             might want to provide already transposed
                             data suitably formatted.  In these cases
                             one should set transpose_vectors to
                             False.
                             Default value: True
    """
    # Get the keyword args.
    transpose_vectors = kwargs.get('transpose_vectors', True)

    if len(args)==3:
        u, v, w = args
        x, y, z = scipy.indices(u.shape)
    elif len(args)==6:
        x, y, z, u, v, w = args
    elif len(args)==4:
        x, y, z, f = args
        assert callable(f), "when used with 4 arguments last argument must be callable"
        u, v, w = f(x, y, z)
    else:
        raise ValueError, "wrong number of arguments"
    
    assert ( x.shape == y.shape and
             y.shape == z.shape and
             z.shape == u.shape and
             u.shape == v.shape and
             v.shape == w.shape ), "argument shape are not equal"

    if 'extent' in kwargs:
        xmin, xmax, ymin, ymax, zmin, zmax = kwargs.pop('extent')
        x = xmin + x*(xmax - xmin)/float(x.max() - x.min()) -x.min()
        y = ymin + y*(ymax - ymin)/float(y.max() - y.min()) -y.min()
        z = zmin + z*(zmax - zmin)/float(z.max() - z.min()) -z.min()

    points = scipy.c_[x.ravel(), y.ravel(), z.ravel()]
    vectors = scipy.concatenate([u[..., scipy.newaxis], 
                                 v[..., scipy.newaxis],
                                 w[..., scipy.newaxis] ],
                                 axis=3)
    if 'scalars' in kwargs:
        scalars = kwargs['scalars']
    else:
        scalars = None
    name = kwargs.pop('name', 'Vector field')
    dx = x[1, 0, 0] - x[0, 0, 0]
    dy = y[0, 1, 0] - y[0, 0, 0]
    dz = z[0, 0, 1] - z[0, 0, 0]

    if not transpose_vectors:
        vectors.shape = vectors.shape[::-1]
    data = ArraySource(transpose_input_array=transpose_vectors,
                      vector_data=vectors,
                      scalar_data=scalars,
                      origin=[points[0, 0], points[0, 1], points[0, 2]],
                      spacing=[dx, dy, dz])
    data_obj = _add_data(data, name)
    return data_obj

######################################################################
# Module creation

def isosurface(data_obj, name='IsoSurface', transparent=True,
                    contours=5):
    """ Applies the Iso-Surface mayavi module to the given VTK data object.
    """
    iso = IsoSurface()

    # Check what type the 'contours' are and do whatever is needed.
    contour_list = True
    try:
        len(contours)
    except TypeError:
        contour_list = False

    if contour_list:
        iso.contour.contours = contours
    else: 
        assert type(contours) == int, "The contours argument must be an integer"
        assert contours > 1, "The contours argument must be positivee"
        iso.contour.set(auto_contours=True,
                            number_of_contours=contours)

    mayavi.add_module(iso, obj=data_obj)

    if transparent:
        data_range = iso.module_manager.scalar_lut_manager.data_range
        iso.module_manager.scalar_lut_manager.lut.alpha_range = \
                (0.2, 0.8)
        data_range = ( scipy.mean(data_range)
                        + 0.4 * ( data_range.max() - data_range.min()) 
                               * scipy.array([-1, 1])) 
        iso.scene.render()

    return iso

def vectors(data_obj, color=None,  name='Vectors', mode='2d',
                scale_factor=1.):
    """ Applies the Vectors mayavi module to the given VTK data object.
    """
    v = Vectors(name=name)
    mayavi.add_module(v, obj=data_obj)
    mode_map = {'2d': 0, 'arrow': 1, 'cone': 2, 'cylinder': 3,
                'sphere': 4, 'cube': 5, 'point': 6}
    if mode == 'point':
        v.glyph.glyph_source = tvtk.PointSource(radius=0,
                                                number_of_points=1)
    else:
         v.glyph.glyph_source = v.glyph.glyph_list[mode_map[mode]]
    if color:
        v.glyph.color_mode = 'no_coloring'
        v.actor.property.color = color
    elif _has_scalar_data(data_obj) :
        v.glyph.color_mode = 'color_by_scalar'
    else:
        v.glyph.color_mode = 'color_by_vector'
    v.glyph.glyph.scale_factor = scale_factor
    return v

def glyph(data_obj, color=None, name='Glyph', mode='sphere',
            scale_factor=1.):
    """ Applies the Glyph mayavi module to the given VTK data object.
    """
    g = Glyph(name=name)
    mayavi.add_module(g, obj=data_obj)
    mode_map = {'2d': 0, 'arrow': 1, 'cone': 2, 'cylinder': 3,
                'sphere': 4, 'cube': 5, 'point': 6}
    if mode == 'point':
        g.glyph.glyph_source = tvtk.PointSource(radius=0,
                                                number_of_points=1)
    else:
         g.glyph.glyph_source = g.glyph.glyph_list[mode_map[mode]]
    if color:
        g.actor.property.color = color
    if _has_scalar_data(data_obj) :
        g.glyph.color_mode = 'color_by_scalar'
        g.glyph.scale_mode = 'scale_by_scalar'
    g.glyph.glyph.scale_factor = scale_factor
    return g

#FIXME : just started this procedure !! Need to modify the color so that if
# none it warps a scalar. Need to add a kwarg for the source.
def streamline(data_obj, color=None,  name='Streamline', ):
    """ Applies the Streamline mayavi module to the given VTK data object.
    """
    st = Streamline()
    mayavi.add_module(st, obj=data_obj)
    if color:
        st.actor.property.color = color
    elif _has_scalar_data(data_obj) :
        st.actor.mapper.scalar_visibility = True
    else:
        st.actor.mapper.interpolate_scalars_before_mapping = True
        st.actor.mapper.scalar_visibility = True
    return st

######################################################################
# Helper functions

def quiver3d(*args, **kwargs):
    """
    Plots glyphs (like arrows) indicating the direction of the vectors
    for a 3D volume of data supplied as arguments.

    Function signatures
    -------------------

        quiver3d(vectordata, ...)
        quiver3d(u, v, w, ...)
        quiver3d(x, y, z, u, v, w, ...)
        quiver3d(x, y, z, f, ...)

    If only one positional argument is passed, it should be VTK data
    object with vector data.

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be a callable, f, 
    that returns vectors.

    Arguments
    ---------
        
        vectordata -- VTK data object with vector data, such as created
                      by vectorscatter of vectorfield.

        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- z coordinates of the points of the mesh (optional).
        
        u -- x coordinnate of the vector field

        v -- y coordinnate of the vector field

        w -- z coordinnate of the vector field

        f -- callable that is used to build the vector field (only if 4 
             positional arguments are passed).

    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Quiver3D'

        mode -- This should be one of ['2d' (2d arrows),
                'arrow', 'cone', 'cylinder', 'sphere', 'cube',
                'point'] and depending on what is passed shows an
                appropriate glyph.  It defaults to a 3d arrow.

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

        scalars -- The scalars used to display the color of the glyphs. 
                  Defaults to the norm of the vectors.

        color -- The color of the glyphs in the absence of scalars. 
                 Default: (1., 0., 0.)

        autoscale -- Autoscale the size of the glyph.
                     Default: True

        scale_factor -- Default 1
    """
    if len(args)==1:
        data_obj = args[0]
    else:
        data_kwargs = kwargs.copy()
        data_kwargs.pop('name','')
        if len(args)==6:
            data_obj = vectorscatter(*args, **data_kwargs)
        else:
            data_obj = vectorfield(*args, **data_kwargs)
    
    if not 'name' in kwargs:
            kwargs['name'] = 'Quiver3D'

    if not 'mode' in kwargs:
            kwargs['mode'] = 'arrow'

    if not 'autoscale' in kwargs or kwargs['autoscale']:
        scale_factor = kwargs.get('scale_factor', 1.)
        kwargs['scale_factor'] = (scale_factor * 
                        _typical_distance(_find_data(data_obj)[0]) )
    kwargs.pop('autoscale', '')

    return vectors(data_obj, **kwargs)

def points3d(*args, **kwargs):
    """
    Plots glyphs (like points) at the position of the supplied data.

    Function signatures
    -------------------

        points3d(scalardata, ...)
        points3d(x, y, z...)
        points3d(x, y, z, s, ...)
        points3d(x, y, z, f, ...)

    If only one positional argument is passed, it should be VTK data
    object with scalar data.

    If only 3 arrays x, y, z all the points are drawn with the same size
    and color

    If 4 positional arguments are passed the last one can be an array s
    or a callable f that gives the size and color of the glyph.

    Arguments
    ---------
        
        scalardata -- VTK data object with scalar data, such as created
                      by scalarscatter.

        x -- x coordinates of the points.

        y -- y coordinates of the points.

        z -- z coordinates of the points.
        
        s -- array giving the color and size of the glyphs (optional).

        f -- callable that returns the scalar associated with the points
             as a function of position.
    
    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Points3D'

        mode -- This should be one of ['2d' (2d arrows),
                'arrow', 'cone', 'cylinder', 'sphere', 'cube',
                'point'] and depending on what is passed shows an
                appropriate glyph.  It defaults to a sphere.

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

        scalars -- The scalars used to display the color of the glyphs. 

        color -- The color of the glyphs. Overrides the scalar array. 
                 Default: (1., 0., 0.). 

        autoscale -- Autoscale the size of the glyph.
                     Default: True

        scale_factor -- Default 1
    """
    if len(args)==1:
        data_obj = args[0]
    else:
        data_kwargs = kwargs.copy()
        data_kwargs.pop('name','')
        if len(args)==4:
            x, y, z, s = args
            if callable(s):
                s = s(x, y, z)
        else:
            x, y, z = args
            s = scipy.ones(x.shape)
        data_obj = scalarscatter(x, y, z, s, **data_kwargs)
    
    if not 'name' in kwargs:
            kwargs['name'] = 'Points3D'

    if not 'mode' in kwargs:
            kwargs['mode'] = 'sphere'

    if not 'autoscale' in kwargs or kwargs['autoscale']:
        scale_factor = kwargs.get('scale_factor', 1.)
        kwargs['scale_factor'] = (0.6* scale_factor * 
                        _typical_distance(_find_data(data_obj)[0]) )
    kwargs.pop('autoscale', '')

    g = glyph(data_obj, **kwargs)
    if len(args)==3:
        g.glyph.scale_mode = 'data_scaling_off'
    if 'color' in kwargs:
        g.glyph.color_mode = 'no_coloring'
    return g

def contour3d(*args, **kwargs):
    """
    Plots iso-surfaces for a 3D volume of data suplied as arguments.

    Function signatures
    -------------------

        contour3d(scalars, ...)
        contour3d(scalarfield, ...)

    Arguments
    ---------
 
        scalars -- A 3D array giving the value of the scalar on a grid.
        
        scalarfield -- VTK data object with scalar field data, such as
                       created by scalarfield.


    Keyword arguments
    -----------------

        name -- The name of the vtk object created. Default: 'Contour3D'

        transpose_scalars -- If the additional argument
                             transpose_scalars is passed, then the
                             input scalar array is suitably
                             transposed.  By default transpose_scalars
                             is True so that the array is in the
                             correct format that VTK expects.
                             However, a transposed array is not
                             contiguous and thus a copy is made, this
                             also means that any changes to the users
                             input array will will not be reflected in
                             the renderered object (provided you know
                             how to do this).  Thus, sometimes users
                             might want to provide already transposed
                             data suitably formatted.  In these cases
                             one should set transpose_scalars to
                             False.
                             Default value: True

        contours -- Integer/list specifying number/list of
                    iso-surfaces. Specifying 0 shows no contours.
                    Specifying a list of values will only give the
                    requested contours asked for.  Default: 3

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the shape of the scalars

        transparent -- Boolean to make the opacity of the isosurfaces depend
                       on the scalar.  Default: True
    """
    if len(args)==1:
        if hasattr(args[0], 'shape'):
            scalars = args[0]
            assert len(scalars.shape) == 3, 'Only 3D arrays are supported.'
            data_kwargs = kwargs.copy()
            data_kwargs.pop('contours', '')
            data_kwargs.pop('transparent', '')
            if not 'name' in kwargs:
                data_kwargs['name'] = 'Contour3D'
            data_obj = scalarfield(scalars, **data_kwargs)
        else:
            data_obj = args[0]
    else:
        raise TypeError, "contour3d takes only one argument"

    # Remove extra kwargs that are not needed for the iso-surface.
    kwargs.pop('extent', '')
    kwargs.pop('name', '')

    return isosurface(data_obj, **kwargs)

######################################################################
# The mlab functionality.

def plot3d(x, y, z, radius=0.01, use_tubes=True, color=(1., 0., 0.) ,
          name='Plot3D'):
    """Draws lines between points.

    Arguments
    ---------

    x -- x coordinates of the points of the line

    y -- y coordinates of the points of the line

    z -- z coordinates of the points of the line

    Keyword arguments
    -----------------

    color -- color of the line. Default: (1., 0., 0.)

    use_tubes -- Enables the drawing of the lines as tubes. Default: True

    radius -- radius of the tubes created. Default: 0.01

    name -- The name of the vtk object created. Default: 'Plot3D'

    """
    assert ( x.shape == y.shape and
             y.shape == z.shape ), "argument shape are not equal"

    points = scipy.c_[x, y, z]
    np = len(points) - 1
    lines = scipy.zeros((np, 2), 'l')
    lines[:,0] = scipy.arange(0, np-0.5, 1, 'l')
    lines[:,1] = scipy.arange(1, np+0.5, 1, 'l')
    pd = tvtk.PolyData(points=points, lines=lines)
    _add_data(pd, name)
    if use_tubes:
        filter = tvtk.TubeFilter(number_of_sides=6)
        filter.radius = radius
        f = FilterBase(filter=filter, name='TubeFilter')
        mayavi.add_filter(f)
    s = Surface()
    s.actor.mapper.scalar_visibility = False
    mayavi.add_module(s)
    s.actor.property.color = color
    return s

def surf(*args, **kwargs):
    """
    Plots a surface using grid spaced data supplied as 2D arrays.

    Function signatures
    -------------------

        surf(z, scalars=z, ...)
        surf(x, y, z, scalars=z, ...)
        
    If only one array z is passed the x and y arrays are assumed to be made 
    of the indices of z.
    z is the elevation matrix. If no `scalars` argument is passed the color 
    of the surface also represents the z matrix. Setting the `scalars` argument
    to None prevents this.

    Arguments
    ---------
 
        x -- x coordinates of the points of the mesh (optional).

        y -- y coordinates of the points of the mesh (optional).

        z -- A 2D array giving the elevation of the mesh.
             Also will work if z is a callable which supports x and y arrays 
             as the arguments, but x and y must then be supplied.

    Keyword arguments
    -----------------

        extent --  [xmin, xmax, ymin, ymax, zmin, zmax] 
                   Default is the x, y, z arrays extent.

        scalars -- An array of the same shape as z that gives the color of the
                   surface. This can also be a function that takes x and
                   y as arguments.

        represention -- can be 'surface', 'wireframe', 'points', or 'mesh'
                        Default is 'surface'

        color -- The color of the mesh in the absence of scalars.

        name -- The name of the vtk object created. Default is "Surf"
    """
    if len(args)==1:
        z = args[0]
        x, y = scipy.indices(z.shape)
    else:
        x, y, z = args
    if callable(z):
        z = z(x, y)
    if not 'scalars' in kwargs:
        kwargs['scalars'] = z
    if callable(kwargs['scalars']):
        kwargs['scalars'] = kwargs['scalars'](x, y)
    if 'color' in kwargs and kwargs['color']:
        kwargs['scalar_visibility'] = False
    if 'extent' in kwargs:
        xmin, xmax, ymin, ymax, zmin, zmax = kwargs.pop('extent')
        x = xmin + x*(xmax - xmin)/float(x.max() - x.min()) -x.min()
        y = ymin + y*(ymax - ymin)/float(y.max() - y.min()) -y.min()
        z = zmin + z*(zmax - zmin)/float(z.max() - z.min()) -z.min()
    return _surf(x, y, z, **kwargs)

def _surf(x, y, z, scalars=None, scalar_visibility=True,
          color=(0.5, 1.0, 0.5), name='Surf', representation='surface',
          tube_radius=0.05, sphere_radius=0.05, ):
    """ Functions that does the work for "surf". It is called with the right 
        number of arguments after the "surf" fonction does the magic to 
        translate the user-supplied arguments into something this function
        understands. """
    triangles, points = mlab.make_triangles_points(x, y, z, scalars)
    data = mlab.make_triangle_polydata(triangles, points, scalars)
    _add_data(data, name)
    
    if representation == 'mesh':
        # Extract the edges.
        ef = tvtk.ExtractEdges()
        extract_edges = FilterBase(filter=ef, name='ExtractEdges')
        mayavi.add_filter(extract_edges)

        # Now show the lines with tubes.
        tf = tvtk.TubeFilter(radius=tube_radius)
        tube = FilterBase(filter=tf, name='TubeFilter')
        mayavi.add_filter(tube)
        s = Surface(name='Tubes')
        s.actor.mapper.scalar_visibility = scalar_visibility
        mayavi.add_module(s)
        s.actor.property.color = color

        # Show the points with glyphs.
        g = Glyph(name='Spheres')
        g.glyph.glyph_source = g.glyph.glyph_list[4]
        g.glyph.glyph_source.radius = sphere_radius
        extract_edges.add_child(g)
        g.glyph.scale_mode = 'data_scaling_off'
        g.actor.mapper.scalar_visibility=scalar_visibility
        g.actor.property.color = color
        return s, g

    s = Surface()
    s.actor.mapper.scalar_visibility = scalar_visibility
    mayavi.add_module(s)
    s.actor.property.color = color
    s.actor.property.representation = representation
    return s

def contour_surf(*args, **kwargs):
    """ Plots the contours of a surface using grid spaced data supplied as 
    2D arrays.

    Function signatures::
    
        contour_surf(z, scalars=z, ...)
        contour_surf(surf_object, ...)
        contour_surf(x, y, z, scalars=z, ...)
        
    If only one array z is passed the x and y arrays are assumed to be made 
    of the indices of z.
    z is the elevation matrix. If no `scalars` argument is passed the
    contours are contour lines of the elevation, elsewhere they are
    contour lines of the scalar array.
    A surf object can also be passed in which case the function adds contours 
    to the existing surf.

    Arguments
    ---------

    x 
        x coordinates of the points of the mesh (optional).
    y 
        y coordinates of the points of the mesh (optional).
    z
        A 2D array giving the elevation of the mesh.
        Also will work if z is a callable which supports x and y arrays 
        as the arguments, but x and y must then be supplied.
    
    Keyword arguments
    -----------------

    extent :  [xmin, xmax, ymin, ymax, zmin, zmax] 
        Default is the x, y, z arrays extent.
    contours 
        Integer/list specifying number/list of
        iso-surfaces. Specifying 0 shows no contours.
        Specifying a list of values will only give the
        requested contours asked for.  Default: 10
    scalars 
        An array of the same shape as z that gives the scalar
        data to plot the contours of. This can also be a function 
        that takes x and y as arguments.
    color 
        The color of the contour lines. If None, this is given by
        the scalars.
    contour_z 
        If this argument is given the contours are drawn on a 
        plane at the altitude specified by this argument instead
        of on the surface. Currently this cannot be used when a 
        surf_object is passed as an argument.
    name 
        The name of the vtk object created. Default is "Contour Surf"
        
    """
    
    contours = kwargs.pop('contours', 10)
    if len(args) == 1 and isinstance(args[0], Surface):
        if 'contour_z' in kwargs:
            raise TypeError, 'contour_z cannot be used when passing a surf_object'
        data_object = _find_module_manager(args[0]).source
        mm = ModuleManager()
        mayavi.add_module(mm, obj=data_object)
        s = Surface(name=kwargs.get('name', 'Contours'))
        mm.add_child(s)
    else:
        if 'contour_z' in kwargs:
            if not 'scalars' in kwargs:
                kwargs['scalars'] = args[-1]
            contour_z = kwargs.pop('contour_z')
            args = list(args)
            args[-1] = scipy.zeros_like(args[0])
        if not 'name' in kwargs:
            kwargs['name'] = "Contour Surf"
        s = surf(*args, **kwargs)
    s.enable_contours = True
    
    # Check what type the 'contours' are and do whatever is needed.
    contour_list = True
    try:
        len(contours)
    except TypeError:
        contour_list = False

    if contour_list:
        s.contour.contours = contours
        s.contour.set(auto_contours=False)
    else: 
        assert type(contours) == int, "The contours argument must be an integer"
        assert contours > 1, "The contours argument must be positive"
        s.contour.set(auto_contours=True,
                            number_of_contours=contours)

    return s

def imshow(arr, extent=None, interpolate=False,
           lut_mode='blue-red', file_name='',
           name='ImShow'):
    """Allows one to view a 2D Numeric array as an image.  This works
    best for very large arrays (like 1024x1024 arrays).

    Arguments
    ---------
    
    arr -- Array to be viewed.

    Keyword arguments
    -----------------

    scale -- Scale the x, y and z axis as per passed values.
             Defaults to [1.0, 1.0, 1.0].

    extent --  [xmin, xmax, ymin, ymax] 
                   Default is the x, y arrays extent

    interpolate -- Boolean to interpolate the data in the image.
    """
    # FIXME
    assert len(arr.shape) == 2, "Only 2D arrays can be viewed!"

    ny, nx = arr.shape
    if extent:
        xmin, xmax, ymin, ymax = extent
    else:
        xmin = 0.
        xmax = nx
        ymin = 0.
        ymax = ny

    xa = scipy.linspace(xmin, xmax, nx, 'f')
    ya = scipy.linspace(ymin, ymax, ny, 'f')

    arr_flat = scipy.ravel(arr)
    min_val = min(arr_flat)
    max_val = max(arr_flat)

    sp = mlab._create_structured_points_direct(xa, ya)

    from enthought.mayavi.core.lut_manager import LUTManager
    lut = LUTManager(lut_mode=lut_mode, file_name=file_name)    
    lut.data_range = min_val, max_val
    a = lut.lut.map_scalars(arr_flat, 0, 0)
    a.name = 'scalars'
    sp.point_data.scalars = a
    sp.scalar_type = 'unsigned_char'
    sp.number_of_scalar_components = 4
    d = _add_data(sp, name)

    ia = ImageActor()
    ia.actor.interpolate = interpolate
    mayavi.add_module(ia)
    return ia

######################################################################
# Non data-related drawing elements
def outline(object=None, color=None, name='Outline'):
    """Creates an outline for the current data.

    Keyword arguments
    -----------------
    
        object -- the object for which we create the outline
                       (default None).

        color -- The color triplet, eg: ( 1., 0., 0.)
    """
    from enthought.mayavi.modules.outline import Outline
    mayavi = _make_default_figure()
    scene = gcf()
    for obj in _traverse(scene):
        if isinstance(obj, Outline) and obj.name == name:
            o = obj
            break
    else:
        o = Outline(name=name)
        if object is not None:
            object.add_child(o)
        else:
            mayavi.add_module(o)
        if color is None:
            color = scene.scene.foreground
    if not color is None:
        o.actor.property.color = color
    return o

def axes(color=None, xlabel=None, ylabel=None, zlabel=None,
         object=None, name='Axes'):
    """Creates an axes for the current data.

    Keyword arguments
    -----------------
    
        color -- The color triplet, eg: (1., 0., 0.)

        xlabel -- the label of the x axis, default: ''

        ylabel -- the label of the y axis, default: ''

        zlabel -- the label of the z axis, default: ''

        object -- the object for which we create the axes.
    """
    mayavi = _make_default_figure()
    scene = gcf()
    new = False
    if object is not None:
        a = Axes(name=name)
        object.add_child(a)
        new = True
    else:
        for obj in _traverse(scene):
            if isinstance(obj, Axes) and obj.name == name:
                a = obj
                break
        else:
            a = Axes(name=name)
            mayavi.add_module(a)
            new = True
    if new:
        if color is None:
            color = scene.scene.foreground
        if xlabel is None:
            xlabel = ''
        if ylabel is None:
            ylabel = ''
        if zlabel is None:
            zlabel = ''
    if color is not None:
        a.property.color = color
    if xlabel is not None:
        a.axes.x_label = xlabel
    if ylabel is not None:
        a.axes.y_label = ylabel
    if zlabel is not None:
        a.axes.z_label = zlabel
    return a

def figure():
    """If you are running from IPython this will start up mayavi for
    you!  This returns the current running MayaVi script instance.
    """
    global mayavi, application
    if mayavi is not None and application.stopped is None:
        mayavi.new_scene()
        return mayavi.engine.current_scene
    m = Mayavi()
    m.main()
    m.script.new_scene()
    engine = m.script.engine
    mayavi = m.script
    application = m.application
    return mayavi.engine.current_scene

def gcf():
    """Return a handle to the current figure.
    """
    return mayavi.engine.current_scene

def clf():
    """Clear the current figure.
    """
    try:
        scene = gcf()
        scene.children[:] = []
    except AttributeError:
        pass

def savefig(filename, size=None, **kwargs):
    """ Save the current scene.
        The output format are deduced by the extension to filename.
        Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
        oogl (geomview), iv (OpenInventor), vrml, obj (wavefront)

        If an additional size (2-tuple) argument is passed the window
        is resized to the specified size in order to produce a
        suitably sized output image.  Please note that when the window
        is resized, the window may be obscured by other widgets and
        the camera zoom is not reset which is likely to produce an
        image that does not reflect what is seen on screen.

        Any extra keyword arguments are passed along to the respective
        image format's save method.
    """
    gcf().scene.save(filename, size=size, **kwargs)

def xlabel(text):
    """Creates a set of axes if there isn't already one, and sets the x label
    """
    return axes(xlabel=text)

def ylabel(text):
    """Creates a set of axes if there isn't already one, and sets the y label
    """
    return axes(ylabel=text)

def zlabel(text):
    """ Creates a set of axes if there isn't already one, and sets the z label
    """
    return axes(zlabel=text)

def title(text=None, color=None, size=None, name='Title'):
    """Creates a title for the figure.

    Keyword arguments
    -----------------

        text -- The text of the title, default: ''
    
        color -- The color triplet, eg: ( 1., 0., 0.)

        size -- The size, default: 1
    """
    scene = gcf()
    for object in _traverse(scene):
        if isinstance(object, Text) and object.name==name:
            t = object
            break
    else:
        t = Text(name=name)
        mayavi.add_module(t)
        if color is None:
            color = scene.scene.foreground
        if text is None:
            text = 'title'
    if color is not None:
        t.property.color = color
    if text is not None:
        t.text = text
    if text is not None or size is not None:
        t.width = min(0.05*size*len(t.text), 1)
        t.x_position = 0.5*(1 - t.width)
        t.y_position = 0.8
    return t

def text(x=0, y=0, text='', color=None, size=None, name='Text'):
    """Adds a text on the figure.

    Keyword arguments
    -----------------
        x -- x position on the screen of the origin of the text, default: 0

        y -- y position on the screen of the origin of the text, default: 0

        text -- The text, default: ''
    
        color -- The color triplet, eg: ( 1., 0., 0.)

        size -- The size, default: 1
    """
    scene = gcf()
    t = Text(name=name)
    mayavi.add_module(t)
    if color is None:
        color = scene.scene.foreground
    else:
        t.property.color = color
    t.text = text
    t.x_position = x
    t.y_position = y
    return t


def scalarbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the scalar color mapping of the given object.

    If no object is specified, the first object with scalar data in the scene 
    is used.

    Keyword arguments
    -----------------
    
        title -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
    """
    module_manager = _find_module_manager(object=object, data_type="scalar")
    if module_manager is None:
        return
    if not module_manager.scalar_lut_manager.show_scalar_bar:
        if title is None:
            title = ''
        if orientation is None:
            orientation = 'horizontal'
    colorbar = module_manager.scalar_lut_manager.scalar_bar
    if title is not None:
        colorbar.title = title
    if orientation is not None:
        _orient_colorbar(colorbar, orientation)
    module_manager.scalar_lut_manager.show_scalar_bar = True
    return colorbar

def vectorbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the vector color mapping of the given object.

    If no object is specified, the first object with vector data in the scene 
    is used.

    Keyword arguments
    -----------------

        object -- Optional object to get the vector lut from
    
        title -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
    """
    module_manager = _find_module_manager(object=object, data_type="vector")
    if module_manager is None:
        return
    if not module_manager.vector_lut_manager.show_scalar_bar:
        title = ''
        orientation = 'horizontal'
    colorbar = module_manager.vector_lut_manager.scalar_bar
    if title is not None:
        colorbar.title = title
    if orientation is not None:
        _orient_colorbar(colorbar, orientation)
    module_manager.vector_lut_manager.show_scalar_bar = True
    return colorbar

def colorbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the color mapping of the given object. 
    
    If the object has scalar data, the scalar color mapping is 
    represented. Elsewhere the vector color mapping is represented, if 
    available.
    If no object is specified, the first object with a color map in the scene 
    is used.

    Keyword arguments
    -----------------

        object -- Optional object to get the vector lut from
    
        title       -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
    """
    colorbar = scalarbar(object=object, title=title, orientation=orientation)
    if colorbar is None:
        colorbar = vectorbar(object=object, title=title, orientation=orientation)
    return colorbar


######################################################################
# Test functions.
######################################################################
def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    pi = scipy.pi
    dphi = pi/1000.0
    phi = scipy.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = scipy.cos(mu)*(1+scipy.cos(n_long*mu/n_mer)*0.5)
    y = scipy.sin(mu)*(1+scipy.cos(n_long*mu/n_mer)*0.5)
    z = scipy.sin(n_long*mu/n_mer)*0.5

    l = plot3d(x, y, z, radius=0.05, color=(0.0, 0.0, 0.8))
    return l

def test_molecule():
    """Generates and shows a Caffeine molecule."""
    o = [[30, 62, 19],[8, 21, 10]]
    ox, oy, oz = map(scipy.array, zip(*o))
    n = [[31, 21, 11], [18, 42, 14], [55, 46, 17], [56, 25, 13]]
    nx, ny, nz = map(scipy.array, zip(*n))
    c = [[5, 49, 15], [30, 50, 16], [42, 42, 15], [43, 29, 13], [18, 28, 12],
         [32, 6, 8], [63, 36, 15], [59, 60, 20]]
    cx, cy, cz = map(scipy.array, zip(*c))
    h = [[23, 5, 7], [32, 0, 16], [37, 5, 0], [73, 36, 16], [69, 60, 20],
         [54, 62, 28], [57, 66, 12], [6, 59, 16], [1, 44, 22], [0, 49, 6]]
    hx, hy, hz = map(scipy.array, zip(*h))

    oxygen = points3d(ox, oy, oz, scale_factor=8, autoscale=False, 
                                        color=(1,0,0), name='Oxygen')
    nitrogen = points3d(nx, ny, nz, scale_factor=10, autoscale=False,
                                        color=(0,0,1), name='Nitrogen')
    carbon = points3d(cx, cy, cz, scale_factor=10, autoscale=False,
                                        color=(0,1,0), name='Carbon')
    hydrogen = points3d(hx, hy, hz, scale_factor=5, autoscale=False,
                                        color=(1,1,1), name='Hydrogen')

def test_surf_lattice():
    """Test Surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = scipy.sin, scipy.cos
        return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
        #return scipy.sin(x*y)/(x*y)

    x, y = scipy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = surf(x, y, f)
    cs = contour_surf(x, y, f, contour_z=0)
    return s

def test_simple_surf():
    """Test Surf with a simple collection of points."""
    x, y = scipy.mgrid[0:3:1,0:3:1]
    return surf(x, y, scipy.asarray(x, 'd'))

def test_surf():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = scipy.pi
    cos = scipy.cos
    sin = scipy.sin
    dphi, dtheta = pi/250.0, pi/250.0
    [phi,theta] = scipy.mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta] 
    m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
    r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
    x = r*sin(phi)*cos(theta)
    y = r*cos(phi)
    z = r*sin(phi)*sin(theta);

    return surf(x, y, z)

def test_mesh_sphere():
    """Create a simple sphere and test the mesh."""
    pi = scipy.pi
    cos = scipy.cos
    sin = scipy.sin    
    du, dv = pi/20.0, pi/20.0
    phi, theta = scipy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
    r = 1.0
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)
    s = surf(x, y, z, representation='mesh',
                   tube_radius=0.01, sphere_radius=0.025)

def test_mesh():
    """Create a fancy looking mesh (example taken from octaviz)."""
    pi = scipy.pi
    cos = scipy.cos
    sin = scipy.sin
    du, dv = pi/20.0, pi/20.0
    u, v = scipy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
    x = (1- cos(u))*cos(u+2*pi/3) * cos(v + 2*pi/3.0)*0.5
    y = (1- cos(u))*cos(u+2*pi/3) * cos(v - 2*pi/3.0)*0.5
    z = cos(u-2*pi/3.)

    m = surf(x, y, z, scalar_visibility=True, representation='mesh',
                   tube_radius=0.0075, sphere_radius=0.02)

def test_imshow():
    """Show a large random array."""
    z_large = scipy.random.random((1024, 512))
    i = imshow(z_large, extent=[0., 1., 0., 1.])

def test_contour3d():
    dims = [64, 64, 64]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = scipy.ogrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = scipy.sin
    scalars = x*x*0.5 + y*y + z*z*2.0

    contour3d(scalars, contours=4)

    # Show an outline and zoom appropriately.
    outline()
    mayavi.engine.current_scene.scene.isometric_view()
    
def test_quiver3d():
    dims = [16, 16, 16]
    xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
    x, y, z = scipy.mgrid[xmin:xmax:dims[0]*1j,
                          ymin:ymax:dims[1]*1j,
                          zmin:zmax:dims[2]*1j]
    x = x.astype('f')
    y = y.astype('f')
    z = z.astype('f')

    sin = scipy.sin
    cos = scipy.cos
    u = cos(x)
    v = sin(y)
    w = sin(x*z)
    
    # All these work!
    #quiver3d(u, v, w)
    quiver3d(x, y, z, u, v, w)

    # Show an outline and zoom appropriately.
    outline()
    mayavi.engine.current_scene.scene.isometric_view()

def test_quiver3d_2d_data():
    dims = [32, 32]
    xmin, xmax, ymin, ymax = [-5,5,-5,5]
    x, y = scipy.mgrid[xmin:xmax:dims[0]*1j,
                       ymin:ymax:dims[1]*1j]
    x = x.astype('f')
    y = y.astype('f')

    sin = scipy.sin
    cos = scipy.cos
    u = cos(x)
    v = sin(y)
    w = scipy.zeros_like(x)
    
    quiver3d(x, y, w, u, v, w)

    # Show an outline and zoom appropriately.
    outline()
    mayavi.engine.current_scene.scene.isometric_view()
