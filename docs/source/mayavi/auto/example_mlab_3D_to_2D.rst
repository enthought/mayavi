

.. _example_mlab_3D_to_2D:

Mlab 3D to 2D example
--------------------------------------------


A script to calculate the projection of 3D world coordinates to
2D display coordinates (pixel coordinates) for a given scene.

The 2D pixel locations of objects in the image plane are related to their
3D world coordinates by a series of linear transformations. The specific
transformations fall under the group known as projective transformations.
This set includes pure projectivities, affine transformations,
perspective transformations, and euclidean transformations. In the case
of mlab (and most other computer visualization software), we deal with
only the perspective and euclidean cases. An overview of Projective space
can be found here: http://en.wikipedia.org/wiki/Projective_space and a
thorough treatment of projective geometry can be had in the book
"Multiple View Geometry in Computer Vision" by Richard Hartley.

The essential thing to know for this example is that points in 3-space
are related to points in 2-space through a series of multiplications of
4x4 matrices which are the perspective and euclidean transformations. The
4x4 matrices predicate the use of length 4 vectors to represent points.
This representation is known as homogeneous coordinates, and while they
appear foriegn at first, they truly simplify all the mathematics
involved. In short, homogeneous coordinates are your friend, and you
should read about them here:
http://en.wikipedia.org/wiki/Homogeneous_coordinates

In the normal pinhole camera model (the ideal real world model), 3D world
points are related to 2D image points by the matrix termed the
'essential' matrix which is a combination of a perspective transformation
and a euclidean transformation. The perspective transformation is defined
by the camera intrinsics (focal length, imaging sensor offset, etc...)
and the euclidean transformation is defined by the cameras position and
orientation. In computer graphics, things are not so simple. This is
because computer graphics have the benefit of being able to do things
which are not possible in the real world: adding clipping planes, offset
projection centers, arbitrary distortions, etc... Thus, a slightly
different model is used.

What follows is the camera/view model for OpenGL and thus, VTK. I can not
guarantee that other packages follow this model.

There are 4 different transformations that are applied 3D world
coordinates to map them to 2D pixel coordinates. They are: the model
transform, the view transform, the perspective transform, and the
viewport or display transform.

In OpenGL the first two transformations are concatenated to yield the
modelview transform (called simply the view transform in VTK). The
modelview transformation applies arbitrary scaling and distortions to the
model (if they are specified) and transforms them so that the orientation
is the equivalent of looking down the negative Z axis. Imagine its as if
you relocate your camera to look down the negative Z axis, and then move
everything in the world so that you see it now as you did before you
moved the camera. The resulting coordinates are termed "eye" coordinates
in OpenGL (I don't know that they have a name in VTK).

The perspective transformation applies the camera perspective to the eye
coordinates. This transform is what makes objects in the foreground look
bigger than equivalent objects in the background. In the pinhole camera
model, this transform is determined uniquely by the focal length of the
camera and its position in 3-space. In Vtk/OpenGL it is determined by the
frustum. A frustum is simply a pyramid with the top lopped off. The top
of the pyramid (a point) is the camera location, the base of the pyramid
is a plane (the far clipping plane) defined as normal to principle camera
ray at distance termed the far clipping distance, the top of the frustum
(where it's lopped off) is the near clipping plane, with a definition
similar to that of the far clipping plane. The sides of the frustum are
determined by the aspect ratio of the camera (width/height) and its
field-of-view. Any points not lying within the frustum are not mapped to
the screen (as they would lie outside the viewable area). The
perspective transformation has the effect of scaling everything within
the frustum to fit within a cube defined in the range (-1,1)(-1,1)(-1,1)
as represented by homogeneous coordinates. The last phrase there is
important, the first 3 coordinates will not, in general, be within the
unity range until we divide through by the last coordinate (See the
wikipedia on homogeneous coordinates if this is confusing). The resulting
coordinates are termed (appropriately enough) normalized view
coordinates.

The last transformation (the viewport transformation) takes us from
normalized view coordinates to display coordinates. At this point, you
may be asking yourself 'why not just go directly to display coordinates,
why need normalized view coordinates at all?', the answer is that we may
want to embed more than one view in a particular window, there will
therefore be different transformations to take each view to an
appropriate position an size in the window. The normalized view
coordinates provide a nice common ground so-to-speak. At any rate, the
viewport transformation simply scales and translates the X and Y
coordinates of the normalized view coordinates to the appropriate pixel
coordinates. We don't use the Z value in our example because we don't
care about it. It is used for other various things however.

That's all there is to it, pretty simple right? Right. Here is an overview:

Given a set of 3D world coordinates:
 - Apply the modelview transformation (view transform in VTK) to get eye
   coordinates
 - Apply the perspective transformation to get normalized view coordinates
 - Apply the viewport transformation to get display coordinates

VTK provides a nice method to retrieve a 4x4 matrix that combines the
first two operations. As far as I can tell, VTK does not export a method
to retrieve the 4x4 matrix representing the viewport transformation, so
we are on our there to create one (no worries though, its not hard, as
you will see).

Now that the prelimenaries are out of the way, lets get started.



**Python source code:** :download:`mlab_3D_to_2D.py`

.. literalinclude:: mlab_3D_to_2D.py
    :lines: 109-


    