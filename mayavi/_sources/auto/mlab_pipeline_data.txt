

.. currentmodule:: mayavi.tools.pipeline

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Data
====

probe_data
~~~~~~~~~~

.. function:: probe_data(mayavi_object, x, y, z, type='scalars', location='points')

    Retrieve the data from a described by Mayavi visualization object
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
    

    

