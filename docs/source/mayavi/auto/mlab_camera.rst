

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

    Sets/Gets the view point for the camera.
    
     view(azimuth=None, elevation=None, distance=None, focalpoint=None)
    
    If called with no arguments this returns the current view of the
    camera.  To understand how this function works imagine the surface
    of a sphere centered around the visualization.  The `azimuth`
    argument specifies the the angle "phi" on the x-y plane which varies
    from 0-360 degrees.  The `elevation` argument specifies the angle
    "theta" from the z axis and varies from 0-180 degrees.  The
    `distance` argument is the radius of the sphere and the
    `focalpoint`, the center of the sphere.
    
    Note that if the `elevation` is close to zero or 180, then the
    `azimuth` angle refers to the amount of rotation of a standard x-y
    plot with respect to the x-axis.  Thus, specifying ``view(0,0)``
    will give you a typical x-y plot with x varying from left to right
    and y from bottom to top.
    
    **Keyword arguments**:
    
     :azimuth: float, optional. The azimuthal angle (in degrees, 0-360),
        i.e. the angle subtended by the position vector on a sphere
        projected on to the x-y plane with the x-axis.
    
     :elevation: float, optional. The zenith angle (in degrees, 0-180),
        i.e. the angle subtended by the position vector and the z-axis.
    
     :distance: float, optional. A positive floating point number
        representing the distance from the focal point to place the
        camera.
    
     :focalpoint: array_like, optional.  An array of 3 floating point
        numbers representing the focal point of the camera.
    
    
    **Returns**:
    
    If no arguments are supplied it returns a tuple of 4 values
    ``(azimuth, elevation, distance, focalpoint)``, representing the
    current view.  Note that these can be used later on to set the view.
    
    If arguments are supplied it returns `None`.
    
    **Examples**:
    
    Get the current view::
    
      >>> v = view()
      >>> v
     (45.0, 45.0, 25.02794981, array([ 0.01118028,  0.        ,  4.00558996]))
    
    Set the view in different ways::
    
      >>> view(45, 45)
      >>> view(240, 120)
      >>> view(distance=20)
      >>> view(focalpoint=(0,0,9))
    
    Set the view to that saved in `v` above::
    
      >>> view(*v)
    

    

