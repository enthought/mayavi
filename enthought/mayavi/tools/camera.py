"""
Controlling the camera.
"""

# Author: Gael Varoquaux 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
try:
    import numpy
except ImportError, e:
    e.message = '''%s\n%s\nPlease check your numpy installation. If you need numpy,
'easy_install numpy' will install it.
http://numpy.scipy.org
        ''' % (e.message, '_'*80)
    e.args = tuple((e.message, ) + e.args[1:])
    raise e
# Enthought library imports.
from enthought.tvtk.api import tvtk

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
    cam = get_engine().current_scene.scene._renderer.active_camera
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

