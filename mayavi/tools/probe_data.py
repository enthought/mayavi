"""
A helper function to retrieve the data from Mayavi structures on
arbitrary points.
"""

import numpy as np

from tvtk.api import tvtk
from . import tools
import tvtk.common as tvtk_common

def probe_data(mayavi_object, x, y, z, type='scalars', location='points'):
    """ Retrieve the data from a described by Mayavi visualization object
        at points x, y, z.

        **Parameters**

        :viz_obj: A Mayavi visualization object, or a VTK dataset
                  The object describing the data you are interested in.
        :x: float or ndarray.
            The x position where you want to retrieve the data.
        :y: float or ndarray.
            The y position where you want to retrieve the data.
        :z: float or ndarray
            The z position where you want to retrieve the data.
        :type: 'scalars', 'vectors' or 'tensors', optional
            The type of the data to retrieve.
        :location: 'points' or 'cells', optional
            The location of the data to retrieve.

        **Returns**

        The values of the data at the given point, as an ndarray
        (or multiple arrays, in the case of vectors or tensors) of the
        same shape as x, y, and z.
    """
    dataset = tools.get_vtk_src(mayavi_object)[0]
    assert type in ('scalars', 'vectors', 'cells'), (
        "Invalid value for type: must be 'scalars', 'vectors' or "
        "'cells', but '%s' was given" % type)
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    z = np.atleast_1d(z)
    shape = x.shape
    assert y.shape == z.shape == shape, \
                        'The x, y and z arguments must have the same shape'
    probe_data = mesh = tvtk.PolyData(points=np.c_[x.ravel(),
                                                   y.ravel(),
                                                   z.ravel()])
    shape = list(shape)
    probe = tvtk.ProbeFilter()
    tvtk_common.configure_input_data(probe, probe_data)
    tvtk_common.configure_source_data(probe, dataset)
    probe.update()

    if location == 'points':
        data = probe.output.point_data
    elif location == 'cells':
        data = probe.output.cell_data
    else:
        raise ValueError("Invalid value for data location, must be "
                         "'points' or 'cells', but '%s' was given."
                         % location)

    values = getattr(data, type)
    if values is None:
        raise ValueError("The object given has no %s data of type %s"
                         % (location, type))
    values = values.to_array()
    if type == 'scalars':
        values = np.reshape(values, shape)
    elif type == 'vectors':
        values = np.reshape(values, shape + [3, ])
        values = np.rollaxis(values, -1)
    else:
        values = np.reshape(values, shape + [-1, ])
        values = np.rollaxis(values, -1)
    return values
