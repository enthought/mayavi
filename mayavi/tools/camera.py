"""
Controlling the camera.
"""

# Author: Gael Varoquaux and Prabhu Ramachandran
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys

try:
    import numpy as np
except ImportError as m:
    msg = '''%s\n%s\nPlease check your numpy installation. If you need numpy,
'easy_install numpy' will install it.
http://numpy.scipy.org
        ''' % (m, '_' * 80)
    raise ImportError(msg)
from numpy import pi

# We can't use gcf, as it creates a circular import in camera management
# routines.
from .engine_manager import get_engine


def world_to_display(x, y, z, figure=None):
    """ Converts 3D world coordinates to screenshot pixel coordinates.

        **Parameters**

        :x: float
            World x coordinate
        :y: float
            World y coordinate
        :z: float
            World z coordinate
        :figure: Mayavi figure or None
            The figure to use for the conversion. If None, the
            current one is used.

        **Output**
        :x: float
            Screenshot x coordinate
        :y: float
            Screenshot y coordinate
    """
    if figure is None:
        f = get_engine().current_scene
    else:
        f = figure
    if f is None or f.scene is None:
        return 0, 0

    f.scene._renderer.world_point = [x, y, z, 1]
    f.scene._renderer.world_to_display()
    x, y, _ = f.scene._renderer.display_point
    return x, y


def roll(roll=None, figure=None):
    """ Sets or returns the absolute roll angle of the camera.

    **See also**

    :mlab.view: control the position and direction of the camera
    """
    if figure is None:
        f = get_engine().current_scene
    else:
        f = figure
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return
    cam = scene.camera

    if roll is not None:
        cam.set_roll(roll)
        if not scene.disable_render:
            scene.render()
    return cam.get_roll()


# This is needed for usage inside the view function, where roll is a
# local variable
_roll = roll


def rad2deg(rad):
    """Converts radians to degrees."""
    return rad * 180. / pi


def deg2rad(deg):
    """Converts degrees to radians."""
    return deg * pi / 180.


def get_camera_direction(cam):
    """ Return the polar coordinates for the camera position:
        r, theta, phi, as well as the focal point.
    """
    fp = cam.focal_point
    pos = cam.position
    x, y, z = pos - fp
    r = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi, fp


def get_outline_bounds(figure=None):
    """ Return the pixel bounds of the objects visible on the figure.
    """
    if figure is None:
        f = get_engine().current_scene
    else:
        f = figure
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return 1, 1, 1, 1

    # Lazy import, to avoid circular imports
    from .figure import screenshot
    red, green, blue = scene.background

    # Use mode='rgba' to have float values, as with fig.scene.background
    outline = screenshot(mode='rgba')
    outline = (
        (outline[..., 0] != red) + (outline[..., 1] != green)
        + (outline[..., 2] != blue)
    )
    outline_x = outline.sum(axis=0)
    outline_y = outline.sum(axis=1)
    height, width = outline.shape
    width = float(width)
    height = float(height)

    outline_x = np.where(outline_x)[0]
    outline_y = np.where(outline_y)[0]

    if len(outline_x) == 0:
        x_min = x_max = .5 * width
    else:
        x_min = outline_x.min()
        x_max = outline_x.max()
    if len(outline_y) == 0:
        y_min = y_max = .5 * height
    else:
        y_min = outline_y.min()
        y_max = outline_y.max()
    return x_min, x_max, y_min, y_max, width, height


def view(azimuth=None, elevation=None, distance=None, focalpoint=None,
         roll=None, reset_roll=True, figure=None):
    """ Sets/Gets the view point for the camera::

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
    """
    if figure is None:
        f = get_engine().current_scene
    else:
        f = figure
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return

    ren = scene.renderer
    cam = scene.camera
    cos = np.cos
    sin = np.sin

    # First compute the current state of the camera.
    r, theta, phi, fp = get_camera_direction(cam)

    # If no arguments were specified, just return the current view.
    if azimuth is None and elevation is None and distance is None \
            and focalpoint is None and roll is None:
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
    bounds = np.array(ren.compute_visible_prop_bounds())
    if distance is not None and not (
            isinstance(distance, str) and distance == 'auto'):
        r = distance
    else:
        r = max(bounds[1::2] - bounds[::2]) * 2.0

    cen = (bounds[1::2] + bounds[::2]) * 0.5
    if focalpoint is not None and not (
            isinstance(focalpoint, str) and focalpoint == 'auto'):
        cen = np.asarray(focalpoint)

    # Find camera position.
    x = r * cos(phi) * sin(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(theta)

    # Now setup the view.
    cam.focal_point = cen
    cam.position = cen + [x, y, z]
    cam.compute_view_plane_normal()
    ren.reset_camera_clipping_range()

    if roll is not None:
        _roll(roll)
    elif reset_roll:
        # Now calculate the view_up vector of the camera.  If the view up is
        # close to the 'z' axis, the view plane normal is parallel to the
        # camera which is unacceptable, so we use a different view up.
        view_up = [0, 0, 1]
        if abs(elevation) < 5. or abs(elevation) > 175.:
            view_up = [sin(phi), cos(phi), 0]
        cam.view_up = view_up

    if distance == 'auto':
        # Reset the zoom, to have the full extents:
        scene.reset_zoom()
        x_min, x_max, y_min, y_max, w, h = get_outline_bounds(figure=figure)
        x_focus, y_focus = world_to_display(cen[0], cen[1], cen[2],
                                            figure=figure)

        ratio = 1.1 * max((x_focus - x_min) / x_focus,
                          (x_max - x_focus) / (w - x_focus),
                          (y_focus - y_min) / y_focus,
                          (y_max - y_focus) / (h - y_focus))

        distance = get_camera_direction(cam)[0]
        r = distance * ratio
        # Reset the camera position.
        x = r * cos(phi) * sin(theta)
        y = r * sin(phi) * sin(theta)
        z = r * cos(theta)

        # Now setup the view.
        cam.position = cen + [x, y, z]
        cam.compute_view_plane_normal()
        ren.reset_camera_clipping_range()

    if not scene.disable_render:
        scene.render()
    return rad2deg(phi), rad2deg(theta), r, fp


def move(forward=None, right=None, up=None):
    """ Translates the camera and focal point together.

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

    """

    f = get_engine().current_scene
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return

    ren = scene.renderer
    cam = scene.camera

    if forward is None and right is None and up is None:
        return cam.position, cam.focal_point

    # vector to offset the camera loc and focal point
    v = np.zeros(3)

    # view plane vetor points behind viewing direction, so we invert it
    yhat = -1. * np.array(cam.view_plane_normal)
    zhat = cam.view_up
    xhat = np.cross(yhat, zhat)

    if forward is not None:
        v += forward * yhat

    if right is not None:
        v += right * xhat

    if up is not None:
        v += up * zhat

    # Apply the offset and setup the view.
    cam.position = cam.position + v
    cam.focal_point = cam.focal_point + v
    ren.reset_camera_clipping_range()
    scene.render()


def yaw(degrees):
    """ Rotates the camera about the  axis corresponding to the
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
    """

    f = get_engine().current_scene
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return

    ren = scene.renderer
    cam = scene.camera

    cam.yaw(degrees)

    ren.reset_camera_clipping_range()
    scene.render()


def pitch(degrees):
    """ Rotates the camera about the  axis corresponding to the
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
    """

    f = get_engine().current_scene
    if f is None:
        return
    scene = f.scene
    if scene is None:
        return

    ren = scene.renderer
    cam = scene.camera

    cam.pitch(degrees)

    ren.reset_camera_clipping_range()
    scene.render()
