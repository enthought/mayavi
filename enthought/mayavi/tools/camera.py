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

def _xyz2rthetaphi(vec):
    """ Returns an r, theta, phi vector for an yxz one (! angles in
    degrees, x and y swapped compared to cylindrical coords)"""
    pi = numpy.pi
    r = numpy.sqrt(numpy.square(vec).sum())
    if r < 1.0e-24:
        vec = numpy.ones_like(vec)*numpy.nan
    else:
        vec = vec / r
    theta = numpy.arccos(vec[2])*180/pi
    xy_mag = numpy.sqrt(numpy.dot(vec[0:2], vec[0:2]))
    if xy_mag < 1.0e-24:
        xy = numpy.ones_like(vec)*numpy.nan
    else:
        xy = vec[0:2] / xy_mag
    phi = numpy.arccos(xy[1])*180/pi
    if numpy.isnan(phi):
        phi=0
    return numpy.array([r, theta, phi])

def _rthetaphi2xyz(vec):
    """ Returns an xyz vector from an r, theta, phi one (! angles in
    degrees, x and y swapped compared to cylindrical coords)"""
    r, theta, phi = vec
    pi = numpy.pi
    cos = numpy.cos
    sin = numpy.sin
    return r*numpy.array([ sin(theta*pi/180.)*sin(phi*pi/180.),
                        sin(theta*pi/180.)*cos(phi*pi/180.),
                        cos(theta*pi/180.)])

def _constraint_thetaphi(theta, phi):
    """ Constraint theta, phi to [0, 180] x [-180, 180] """
    n_theta = numpy.floor(theta/180.)
    theta = abs((theta +180) % 360 - 180)
    phi = ((n_theta*180 + phi + 180) % 360) - 180
    return theta, phi

def guess_roll(phi, theta):
    """ Tries to get the roll angle right to make the picture look good.
        See also: roll"""
    # This is really magic fudge ! Before modifying this, spend a long
    # time understanding the problem. There must be a rigorous way of
    # doing this, but I couldn't find any, and the net didn't help.
    #
    # The functions here where found by considering special lines
    # (along the equator, on the principal meridian, near the pole),
    # finding the right value for "roll" on these lines, and finding an
    # extrapolation on the complete globe. Of course there is a singular
    # point. This is unovaidable (hairy ball theorem)
    # 
    # theta, phi in [0, 180] x [-180, 180]
    if theta==0:
        return phi
    elif theta==90:
        if phi in (-180, 180):
            return 0
        return -numpy.sign(phi)*90
    pi = numpy.pi
    remainer = 0.
    if theta > 90:
        theta = 180. - theta
        remainer = 180.
    if phi > 90:
        phi = 180 -phi
    elif phi < -90:
        phi = -180 -phi
    rr = lambda p, t: numpy.sign(p)*90*pow(abs(p)/90., (90-t)/90.)
    rr = lambda p, t: numpy.sign(p)*90*pow(abs(p)/90., numpy.sqrt((90-t)/90.))
    roll = remainer -rr(phi, theta)
    return roll

def view(azimuth=None, elevation=None, distance=None, focalpoint=None):
    """ Sets the view point for the camera. 
    
     view(azimuth=None, elevation=None, distance=None, focalpoint=None)

    azimuth: angle in the horizontal plane
    elevation: elevation angle of the camera relative to the vertical
    distance: distance to the focal point
    focalpoint: (x, y, z) position of the focal point.
    If some parameters are not passed, they are left unchanged. The
    function tries to guess the roll angle appropriate for the view.
    see also: roll."""
    # XXX: It might be more sensible to have elevation = 90+theta
    # Currently theta = - elevation
    scene = get_engine().current_scene.scene
    if scene is None:
        return
    cam = scene._renderer.active_camera
    if focalpoint is not None:
        cam.focal_point = focalpoint
    vec = cam.position - cam.focal_point
    r, theta, phi = _xyz2rthetaphi(vec)
    if azimuth is not None:
        phi = azimuth
    if elevation is not None:
        theta = -elevation
    theta, phi = _constraint_thetaphi(theta, phi)
    if distance is not None:
        r = distance
    if not (      azimuth is None
             and  elevation is None
             and  distance is None
             and  focalpoint is None ):
        vec = _rthetaphi2xyz([r, theta, phi])
        cam.position = cam.focal_point + numpy.array(vec)
        cam.orthogonalize_view_up()
        roll = guess_roll(phi, theta)
        cam.set_roll(roll)
        # FIXME: vtk knows how to calculate that. Need to find out.
        cam.clipping_range = r*numpy.array([0.2, 1.5])
        get_engine().current_scene.render()
    return phi, -theta, r

def roll(roll=None):
    """ Sets or returns the absolute roll angle of the camera """
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

    Parameters
    -----------

    azimuth : float, optional
        The azimuthal angle (in degrees, 0-360), i.e. the angle
        subtended by the position vector on a sphere projected on to the
        x-y plane with the x-axis.

    elevation : float, optional
        The zenith angle (in degrees, 0-180), i.e. the angle subtended
        by the position vector and the z-axis. 

    distance : float, optional
        A positive floating point number representing the distance from
        the focal point to place the camera

    focalpoint : array_like, optional
        An array of 3 floating point numbers representing the focal
        point of the camera. 


    Returns
    --------

    If no arguments are supplied it returns a tuple of 4 values
    ``(azimuth, elevation, distance, focalpoint)``, representing the
    current view.  Note that these can be used later on to set the view.
    
    If arguments are supplied it returns `None`.

    Examples
    ---------

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
    """

    f = get_engine().current_scene
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
