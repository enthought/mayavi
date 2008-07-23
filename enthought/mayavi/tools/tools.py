"""
The general purpose tools to manipulate the pipeline with the mlab interface.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import numpy

# Enthought library imports.
from enthought.tvtk.api import tvtk

# MayaVi related imports.
from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi.core.module_manager import ModuleManager
from enthought.mayavi.sources.array_source import ArraySource
from enthought.mayavi.core.source import Source

from engine_manager import get_engine, engine_manager
from figure import gcf

######################################################################
# Utility functions.

def _add_data(tvtk_data, name='', figure=None):
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
    if figure is None:
        gcf()
        engine = get_engine()
    else:
        engine = engine_manager.find_figure_engine(figure)
        engine.current_scene = figure
    engine.add_source(d)
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
    elif ( hasattr(object, 'data') or isinstance(object, ArraySource) 
                or hasattr(object, 'inputs')):
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
    distance = numpy.sqrt(((x_max-x_min)**2 + (y_max-y_min)**2 +
                           (z_max-z_min)**2)/(4*
                           data_obj.number_of_points**(0.33)))
    if distance == 0:
        return 1
    else:
        return 0.4*distance

def _set_extent(module, extents):
    if numpy.all(extents == 0.):
        # That the default setting.
        return
    xmin, xmax, ymin, ymax, zmin, zmax = extents
    xo = 0.5*(xmax + xmin)
    yo = 0.5*(ymax + ymin)
    zo = 0.5*(zmax + zmin)
    extentx = 0.5*(xmax - xmin)
    extenty = 0.5*(ymax - ymin)
    extentz = 0.5*(zmax - zmin)
    # Now the actual bounds.
    xmin, xmax, ymin, ymax, zmin, zmax = module.actor.actor.bounds
    # Scale the object
    boundsx = 0.5*(xmax - xmin)
    boundsy = 0.5*(ymax - ymin)
    boundsz = 0.5*(zmax - zmin)
    xs, ys, zs = module.actor.actor.scale
    if not numpy.allclose(xmin, xmax):
        scalex = xs*extentx/boundsx
    else:
        scalex = 1
    if not numpy.allclose(ymin, ymax):
        scaley = ys*extenty/boundsy
    else:
        scaley = 1
    if not numpy.allclose(zmin, zmax):
        scalez = zs*extentz/boundsz
    else:
        scalez = 1
    
    module.actor.actor.scale = (scalex, scaley, scalez)
    ## Remeasure the bounds
    xmin, xmax, ymin, ymax, zmin, zmax = module.actor.actor.bounds
    xcenter = 0.5*(xmax + xmin)
    ycenter = 0.5*(ymax + ymin)
    zcenter = 0.5*(zmax + zmin)         
    # Center the object                 
    module.actor.actor.origin = (0.,  0.,  0.)
    xpos, ypos, zpos = module.actor.actor.position
    module.actor.actor.position = (xpos + xo -xcenter, ypos + yo - ycenter,
                                            zpos + zo -zcenter)


