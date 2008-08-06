

.. currentmodule:: enthought.mayavi.mlab

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Camera handling functions
=========================

roll
~~~~

.. function:: roll(roll=None)

    Sets or returns the absolute roll angle of the camera
    

    


view
~~~~

.. function:: view(azimuth=None, elevation=None, distance=None, focalpoint=None)

    Sets the view point for the camera.
    
     view(azimuth=None, elevation=None, distance=None, focalpoint=None)
    
    azimuth: angle in the horizontal plane
    elevation: elevation angle of the camera relative to the vertical
    distance: distance to the focal point
    focalpoint: (x, y, z) position of the focal point.
    If some parameters are not passed, they are left unchanged. The
    function tries to guess the roll angle appropriate for the view.
    see also: roll.

    

