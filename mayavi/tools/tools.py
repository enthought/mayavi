"""
The general purpose tools to manipulate the pipeline with the mlab interface.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>,
#         Gael Varoquaux      <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2007-2020 Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import numpy

import vtk

# Enthought library imports.
from tvtk.api import tvtk

# MayaVi related imports.
from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.sources.vtk_object_source import VTKObjectSource
from mayavi.core.module_manager import ModuleManager
from mayavi.core.source import Source
from mayavi.core.filter import Filter

from .engine_manager import get_engine, engine_manager, get_null_engine
from .figure import gcf

######################################################################
# Utility functions.


def _get_engine_from_kwarg(kwargs):
    engine = None
    if 'figure' not in kwargs:
        # No figure has been specified, retrieve the default one.
        gcf()
        engine = get_engine()
    elif kwargs['figure'] is False:
        # Get a null engine that we can use.
        engine = get_null_engine()
    elif kwargs['figure'] is not None:
        figure = kwargs['figure']
        engine = engine_manager.find_figure_engine(figure)
        engine.current_scene = figure

    return engine


def add_dataset(dataset, name='', **kwargs):
    """Add a dataset object to the Mayavi pipeline.

    **Parameters**

    :dataset: a tvtk/vtk dataset/tvtk/VTK Algorithm, or a Mayavi source. The
              dataset added to the Mayavi pipeline

    :figure: a figure identifier number or string, None or False, optional.

            If no `figure` keyword argument is given, the data
            is added to the current figure (a new figure if created if
            necessary).

            If a `figure` keyword argument is given, it should either the name
            the number of the figure the dataset should be added to, or None,
            in which case the data is not added to the pipeline.

            If figure is False, a null engine is created. This null
            engine does not create figures, and is mainly usefull for
            tensting, or using the VTK algorithms without visualization.

    **Returns**

    The corresponding Mayavi source is returned.

    """
    if isinstance(dataset, (tvtk.DataSet, vtk.vtkDataSet)):
        d = VTKDataSource()
        d.data = tvtk.to_tvtk(dataset)
    elif isinstance(dataset, (tvtk.DataObject, vtk.vtkDataObject)):
        d = VTKObjectSource()
        tp = tvtk.TrivialProducer()
        tp.set_output(tvtk.to_tvtk(dataset))
        d.object = tp
    elif isinstance(dataset, (tvtk.Object, vtk.vtkObject)):
        d = VTKObjectSource()
        d.object = tvtk.to_tvtk(dataset)
    elif isinstance(dataset, Source):
        d = dataset
    else:
        raise TypeError(
              "first argument should be either a TVTK object"
              " or a mayavi source")

    if len(name) > 0:
        d.name = name
    engine = _get_engine_from_kwarg(kwargs)
    if engine is None:
        # Return early, as we don't want to add the source to an engine.
        return d
    engine.add_source(d)
    return d


def add_module_manager(object):
    """ Add a module-manager, to control colors and legend bars to the
        given object.
    """
    return get_engine().add_module(ModuleManager(), object)


def _traverse(node):
    """ Generator to traverse a tree accessing the nodes' children
        attribute.

        **Example**

        Here is a simple example printing the names of all the objects in
        the pipeline::

            for obj in mlab.pipeline.traverse(mlab.gcf()):
                print obj.name

    """
    try:
        for leaf in node.children:
            for leaflet in _traverse(leaf):
                yield leaflet
    except AttributeError:
        pass
    yield node


def get_vtk_src(mayavi_object, stop_at_filter=True):
    """ Goes up the Mayavi pipeline to find the data sources of a given
        object.

        **Parameters**

        :object: any Mayavi visualization object

        :stop_at_filter: optional boolean flag: if True, the first object
                         exposing data found going up the pipeline is
                         returned. If False, only the source itself
                         is returned.

        **Returns**

        :sources: List of vtk data sources (vtk data sources, and not
                  Mayavi source objects).

        **Notes**

        This function traverses the Mayavi pipeline. Thus the input
        object 'mayavi_object' should already be added to the pipeline.
    """
    if isinstance(mayavi_object, tvtk.Object):
        if mayavi_object.is_a('vtkDataSet'):
            # We have been passed a tvtk source
            return [mayavi_object]
        elif hasattr(mayavi_object, 'output'):
            return [mayavi_object.output]
    if not (hasattr(mayavi_object, 'parent')
            or isinstance(mayavi_object, Source)):
        raise TypeError('Cannot find data source for given object %s' % (
                                            mayavi_object))
    while True:
        # XXX: If the pipeline is not a DAG, this is an infinite loop
        if isinstance(mayavi_object, Source):
            if stop_at_filter or not isinstance(mayavi_object, Filter):
                get_output = lambda x: x if x.is_a('vtkDataSet') else x.output
                return [get_output(x) for x in mayavi_object.outputs]
        mayavi_object = mayavi_object.parent


def _has_scalar_data(object):
    """Tests if an object has scalar data.
    """
    data_sources = get_vtk_src(object)
    for source in data_sources:
        if source.point_data.scalars is not None:
            return True
        elif source.cell_data.scalars is not None:
            return True
    return False


def _has_vector_data(object):
    """Tests if an object has vector data.
    """
    data_sources = get_vtk_src(object)
    for source in data_sources:
        if source.point_data.vectors is not None:
            return True
        elif source.cell_data.vectors is not None:
            return True
    return False


def _has_tensor_data(object):
    """Tests if an object has tensor data.
    """
    data_sources = get_vtk_src(object)
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
                if data_type == 'scalar':
                    if not _has_scalar_data(object):
                        continue
                    try:
                        if not object.actor.mapper.scalar_visibility:
                            continue
                    except AttributeError:
                        pass
                if data_type == 'vector' and not _has_vector_data(object):
                    continue
                if data_type == 'tensor' and not _has_tensor_data(object):
                    continue
                return object
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


def _typical_distance(data_obj):
    """ Returns a typical distance in a cloud of points.
        This is done by taking the size of the bounding box, and dividing it
        by the cubic root of the number of points.
    """
    x_min, x_max, y_min, y_max, z_min, z_max = data_obj.bounds
    distance = numpy.sqrt(((x_max - x_min) ** 2 + (y_max - y_min) ** 2 +
                           (z_max - z_min) ** 2) / (4 *
                           data_obj.number_of_points ** (0.33)))
    if distance == 0:
        return 1
    else:
        return 0.4 * distance


def _min_distance(x, y, z):
    """ Return the minimum interparticle distance in a cloud of points.
        This is done by brute force calculation of all the distances
        between particle couples.
    """
    distances = numpy.sqrt((x.reshape((-1,)) - x.reshape((1, -1))) ** 2
                           + (y.reshape((-1,)) - y.reshape((1, -1))) ** 2
                           + (z.reshape((-1,)) - z.reshape((1, -1))) ** 2
                          )
    return distances[distances != 0].min()


def _min_axis_distance(x, y, z):
    """ Return the minimum interparticle distance in a cloud of points
        along one of the axis.
        This is done by brute force calculation of all the distances with
        norm infinity between particle couples.
    """
    def axis_min(a):
        a = numpy.abs(a.reshape((-1,)) - a.reshape((-1, 1)))
        a = a[a > 0]
        if a.size == 0:
            return numpy.inf
        return a.min()
    distances = min(axis_min(x), axis_min(y), axis_min(z))
    if distances == numpy.inf:
        return 1
    else:
        return distances


def set_extent(module, extents):
    """ Attempts to set the physical extents of the given module.

        The extents are given as (xmin, xmax, ymin, ymax, zmin, zmax).
        This does not work on an image plane widget, as this module does
        not have an actor.

        Once you use this function on a module, be aware that other
        modules applied on the same data source will not share the same
        scale. Thus for instance an outline module will not respect the
        outline of the actors whose extent you modified. You should pass
        in the same "extents" parameter for this to work.You can have a
        look at the wigner.py example for a heavy use of this
        functionality.

        **Note**

        This function does not work on some specific modules, such as
        Outline, Axes, or ImagePlaneWidget. For Outline and Axes, use the
        extent keyword argument of mlab.pipeline.outline and
        mlab.pipeline.axes.
    """
    if numpy.all(extents == 0.):
        # That the default setting.
        return
    if not hasattr(module, 'actor'):
        print('Cannot set extents for %s' % module)
        return
    xmin, xmax, ymin, ymax, zmin, zmax = extents
    xo = 0.5 * (xmax + xmin)
    yo = 0.5 * (ymax + ymin)
    zo = 0.5 * (zmax + zmin)
    extentx = 0.5 * (xmax - xmin)
    extenty = 0.5 * (ymax - ymin)
    extentz = 0.5 * (zmax - zmin)

    # Extract the actor, checking either module.actor.actor
    # or module.actor as a fallback
    actor = getattr(module.actor, 'actor', module.actor)

    # Now the actual bounds.
    xmin, xmax, ymin, ymax, zmin, zmax = actor.bounds
    # Scale the object
    boundsx = 0.5 * (xmax - xmin)
    boundsy = 0.5 * (ymax - ymin)
    boundsz = 0.5 * (zmax - zmin)
    xs, ys, zs = actor.scale
    if not numpy.allclose(xmin, xmax):
        scalex = xs * extentx / boundsx
    else:
        scalex = 1
    if not numpy.allclose(ymin, ymax):
        scaley = ys * extenty / boundsy
    else:
        scaley = 1
    if not numpy.allclose(zmin, zmax):
        scalez = zs * extentz / boundsz
    else:
        scalez = 1

    actor.scale = (scalex, scaley, scalez)
    ## Remeasure the bounds
    xmin, xmax, ymin, ymax, zmin, zmax = actor.bounds
    xcenter = 0.5 * (xmax + xmin)
    ycenter = 0.5 * (ymax + ymin)
    zcenter = 0.5 * (zmax + zmin)
    # Center the object
    actor.origin = (0.,  0.,  0.)
    xpos, ypos, zpos = actor.position
    actor.position = (xpos + xo - xcenter,
                      ypos + yo - ycenter,
                      zpos + zo - zcenter)


def start_recording(ui=True):
    """Start automatic script recording.  If the `ui` parameter is
    `True`, it creates a recorder with a user interface, if not it
    creates a vanilla recorder without a UI.

    **Returns**
        The `Recorder` instance created.
    """
    from apptools.scripting.api import start_recording as start
    e = get_engine()
    msg = "Current engine, %s, is already being recorded." % (e)
    assert e.recorder is None, msg
    r = start(e, ui=ui)
    return r


def stop_recording(file=None):
    """Stop the automatic script recording.

    **Parameters**

     :file: An open file or a filename or `None`.  If this is `None`,
            nothing is saved.

    """
    from apptools.scripting.api import stop_recording as stop
    e = get_engine()
    r = e.recorder
    if r is not None:
        stop(e, save=False)
        if type(file) is str:
            f = open(file, 'w')
            r.save(f)
            f.close()
        elif hasattr(file, 'write') and hasattr(file, 'flush'):
            r.save(file)
