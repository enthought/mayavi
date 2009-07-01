"""
Controlling the camera.
"""

# Author: Gael Varoquaux and Prabhu Ramachandran 
# Copyright (c) 2007-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
try:
    import numpy
except ImportError, m:
    msg = '''%s\n%s\nPlease check your numpy installation. If you need numpy,
'easy_install numpy' will install it.
http://numpy.scipy.org
        ''' % (m, '_'*80)
    raise ImportError(msg)

from numpy import pi

# We can't use gcf, as it creates a circular import in camera management
# routines.
from engine_manager import get_engine

def roll(roll=None):
    """ Sets or returns the absolute roll angle of the camera.
    
    **See also**

    :mlab.view: control the position and direction of the camera
    """
    cam = get_engine().current_scene.scene._renderer.active_camera
    if roll is not None:
        cam.set_roll(roll)
        get_engine().current_scene.render()
    return cam.get_roll()

def rad2deg(rad):
    """Converts radians to degrees."""
    return rad*180./pi

def deg2rad(deg):
    """Converts degrees to radians."""
    return deg*pi/180.

def view(azimuth=None, elevation=None, distance=None, focalpoint=None):
    """ Sets/Gets the view point for the camera. 
    
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
    
    **See also**

    :mlab.roll: control the roll angle of the camera, ie the direction
               pointing up
    """

    f = get_engine().current_scene
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return

    ren = scene.renderer
    cam = scene.camera
    cos = numpy.cos
    sin = numpy.sin

    # First compute the current state of the camera.
    fp = cam.focal_point
    pos = cam.position
    x, y, z = pos - fp
    r = numpy.sqrt(x*x + y*y + z*z)
    theta = numpy.arccos(z/r)
    phi = numpy.arctan2(y, x)

    # If no arguments were specified, just return the current view.
    if azimuth is None and elevation is None and distance is None \
            and focalpoint is None:
        return rad2deg(phi), rad2deg(theta), r, fp

    # Convert radians to 
    if azimuth is None:
        azimuth = rad2deg(phi)
    else:
        phi = deg2rad(azimuth)
    if elevation is None:
        elevation = rad2deg(theta)
    else:
        theta = deg2rad(elevation)

    # We compute the position of the camera on the surface of a sphere
    # centered at the center of the bounds, with radius chosen from the
    # bounds.
    bounds = numpy.array(ren.compute_visible_prop_bounds())
    if distance is not None:
        r = distance
    else:
        r = max(bounds[1::2] - bounds[::2])*2.0

    cen = (bounds[1::2] + bounds[::2])*0.5
    if focalpoint is not None:
        cen = numpy.asarray(focalpoint)

    # Now calculate the view_up vector of the camera.  If the view up is
    # close to the 'z' axis, the view plane normal is parallel to the
    # camera which is unacceptable, so we use a different view up.
    view_up = [0, 0, 1]
    if abs(elevation) < 5. or abs(elevation) > 175.:
        view_up = [sin(phi), cos(phi), 0]

    # Find camera position.
    x = r*cos(phi)*sin(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(theta)

    # Now setup the view.
    cam.focal_point = cen
    cam.view_up = view_up
    cam.position = cen + [x,y,z]
    cam.compute_view_plane_normal()
    ren.reset_camera_clipping_range()
    scene.render()
