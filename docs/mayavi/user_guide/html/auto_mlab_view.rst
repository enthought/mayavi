
view
~~~~

 Sets the view point for the camera.

 view(azimuth=None, elevation=None, distance=None, focalpoint=None)

azimuth: angle in the horizontal plane
elevation: elevation angle of the camera relative to the vertical
distance: distance to the focal point
focalpoint: (x, y, z) position of the focal point.
If some parameters are not passed, they are left unchanged. The
function tries to guess the roll angle appropriate for the view.
see also: roll.
    