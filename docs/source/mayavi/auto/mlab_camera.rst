

.. currentmodule:: mayavi.mlab

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Camera handling functions
=========================

move
~~~~

.. function:: move(forward=None, right=None, up=None)

    Translates the camera and focal point together.
    
    The arguments specify the relative distance to translate the
    camera and focal point, so as to produce the appearance of
    moving the camera without changing the effective field of view.
    If called with no arguments, the function returns the absolute
    position of the camera and focal point on a cartesian coordinate
    system.
    
    Note that the arguments specify relative motion, although the
    return value with no arguments is in an absolute coordinate system.
    
    **Keyword arguments**:
    
    :forward: float, optional. The distance in space to translate the
        camera forward (if positive) or backward (if negative)
    
    :right: float, optional.  The distance in space to translate the
        camera to the right (if positive) or left (if negative)
    
    :up: float, optional. The distance in space to translate the
        camera up (if positive) or down (if negative)
    
    
    **Returns**:
    
    If no arguments are supplied (or all are None), returns a
    tuple (camera_position, focal_point_position)
    
    otherwise, returns None
    
    **Examples**:
    
    Get the current camera position::
    
      >>> cam,foc = move()
      >>> cam
      array([-0.06317079, -0.52849738, -1.68316389])
      >>> foc
      array([ 1.25909623,  0.15692708, -0.37576693])
    
    Translate the camera::
    
      >>> move(3,-1,-1.2)
      >>> move()
      (array([ 2.93682921, -1.52849738, -2.88316389]),
       array([ 4.25909623, -0.84307292, -1.57576693]))
    
    Return to the starting position::
    
      >>> move(-3,1,1.2)
      >>> move()
      (array([-0.06317079, -0.52849738, -1.68316389]),
       array([ 1.25909623,  0.15692708, -0.37576693]))
    
    **See also**
    
    :mlab.yaw: yaw the camera (tilt left-right)
    :mlab.pitch: pitch the camera (tilt up-down)
    :mlab.roll: control the absolute roll angle of the camera
    :mlab.view: set the camera position relative to the focal point instead
                of in absolute space
    
    

    


pitch
~~~~~

.. function:: pitch(degrees)

    Rotates the camera about the  axis corresponding to the
    "right" direction of the current view. Note that this will
    change the location of the focal point (although not the
    camera location).
    
    This angle is relative to the current direction - the
    angle is NOT an absolute angle in a fixed coordinate
    system.
    
    **See also**
    
    :mlab.yaw: relative rotation about the "up" direction
    :mlab.roll: absolute roll angle (i.e. "up" direction)
    :mlab.move: relative  translation of the camera and focal
                point
    

    


roll
~~~~

.. function:: roll(roll=None, figure=None)

    Sets or returns the absolute roll angle of the camera.
    
    **See also**
    
    :mlab.view: control the position and direction of the camera
    

    


view
~~~~

.. function:: view(azimuth=None, elevation=None, distance=None, focalpoint=None, roll=None, reset_roll=True, figure=None)

    Sets/Gets the view point for the camera::
    
     view(azimuth=None, elevation=None, distance=None, focalpoint=None,
          roll=None, reset_roll=True, figure=None)
    
    If called with no arguments this returns the current view of the
    camera.  To understand how this function works imagine the surface
    of a sphere centered around the visualization.  The `azimuth`
    argument specifies the angle "phi" on the x-y plane which varies
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
    
     :distance: float or 'auto', optional.
        A positive floating point number representing the distance from
        the focal point to place the camera. New in Mayavi 3.4.0: if
        'auto' is passed, the distance is computed to have a best fit of
        objects in the frame.
    
     :focalpoint: array_like or 'auto', optional.
        An array of 3 floating point numbers representing the focal point
        of the camera. New in Mayavi 3.4.0: if 'auto' is passed, the
        focal point is positioned at the center of all objects in the
        scene.
    
     :roll: float, optional
        Controls the roll, ie the rotation of the camera around its axis.
    
     :reset_roll: boolean, optional.
        If True, and 'roll' is not specified, the roll orientation of the
        camera is reset.
    
     :figure: The Mayavi figure to operate on. If None is passed, the
        current one is used.
    
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
    
    **See also**
    
    :mlab.roll: control the roll angle of the camera, ie the direction
               pointing up
    

    


yaw
~~~

.. function:: yaw(degrees)

    Rotates the camera about the  axis corresponding to the
    "up" direction of the current view. Note that this will
    change the location of the focal point (although not the
    camera location).
    
    This angle is relative to the current direction - the
    angle is NOT an absolute angle in a fixed coordinate
    system.
    
    **See also**
    
    :mlab.pitch: relative rotation about the "right" direction
    :mlab.roll: absolute roll angle (i.e. "up" direction)
    :mlab.move: relative translation of the camera and focal
                point
    

    

