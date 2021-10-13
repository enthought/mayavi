"""A module that provides VPython like capabilities.  For more
details about VPython, refer the official website.
VPython : http://www.vpython.org/index.html

The API is based on VPython, but instead of using OpenGL and other C
libraries, this is based completly on TVTK, and Traits and Numpy.
All of the demos are also translated from VPython examples.

The implementation is done using object oriented design, and each
visualization capability is implemented as a seperate traits class.
The attributes of each class could be independently edited.

The API is kept as similar to VPython as much as possible.

This module offers the following classes :

 Display actors
 sphere, cylinder, cone, box, arrow, curve, ring, helix, ellipsoid

 Functionality classes
 frame, vector, animator

 Utility functions
 iterator, remove_actor, show

To see examples of classes and functions look at the `test_*`
functions at the end of this file. Here is a quick example
demonstrating how to use visual.

Note: The visual module should be interactively used in ipython only when
--gui=qt is enabled. `visual` will not work properly in an interactive mode
with the vanilla python interpretor.  ::

    $ ipython --gui=qt

    In [1]: from tvtk.tools import visual
    In [2]: visual.test_sphere()
    In [3]: s = visual.sphere() # Create a sphere actor
    In [4]: s.edit_traits() # Edit sphere actor's properties via GUI

"""
# Author: Raashid Baig <raashid@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
#
# License: BSD Style.
# Year : 2007-2016

# Standard library imports.
import sys
import numpy
import time
from math import sin, cos, pi, sqrt, acos

# Enthought library imports.
from traits.api import HasTraits, Trait, Instance, Tuple, Int, \
     Range, Button, Array, Bool, Any, List, Enum
from traitsui.api import View, Item, Group
from tvtk.api import tvtk
from tvtk.tools import ivtk
from tvtk.common import configure_input
from pyface.api import GUI
from pyface.timer.api import Timer
from tvtk.tvtk_base import vtk_color_trait



# Set the global variable to None, for it's future use in function
# get_viewer()
_viewer = None

#################################################################
################       Utility function      ####################
#################################################################

def _create_viewer():
    """Creates and retunrs the ivtk viewer to get_viewer() function"""
    v = ivtk.viewer(browser = False)
    v.scene.background = (0,0,0)
    GUI.process_events()
    return v

def set_viewer(viewer):
    """Set the global viewer.  Handy if you need to use visual from your
    own viewer.  Pass an object that has a `scene` trait containing a
    tvtk scene instance.
    """
    global _viewer
    _viewer = viewer

def get_viewer():
    """ Creates and returns an ivtk viewer. If the fuction is called
    1st time than creates and returns the viewer, otherwise the
    originally created viewer itself is returned. Checking is done
    through the global variable _viewer.
    """
    global _viewer
    if _viewer is None:
        # If no viewer has been created till this point in program
        # _create_viewer() is called and a new ivtk viewer is created
        _viewer = _create_viewer()
    else:
        try:
            _viewer.scene.render()
        except:
            # If the original ivtk window is destroyed when function
            # is called more than once an exception is raised so that
            # a new ivtk browser is created and returned.
            _viewer = _create_viewer()
    return _viewer

def show_actor(*tvtk_actors):
    """ Gets an ivtk viewer from the function get_viewer() and adds
    all the actors given, to the ivtk scene.
    """
    v = get_viewer()
    v.scene.add_actors(tvtk_actors)
    v.scene.reset_zoom()

def remove_actor(*tvtk_actors):
    """ Gets the ivtk viewer from the function get_viewer() and
    removes all the actors given, from the ivtk scene."""
    v = get_viewer()
    for x in tvtk_actors:
        v.scene.remove_actors(x.actor)
        v.scene.reset_zoom()

def show():
    """This function has to be called at the end in a stand alone
    visual program. Note - Don't call this function when running
    visual from ipython iterpretor in an interactive mode
    """
    if '-wthread' in sys.argv or '--gui' in sys.argv:
        pass
    else:
        gui = GUI()
        gui.start_event_loop()

def iterate(millisec, callable, *args, **kwargs):
    """Creates an instance of utility class Animator and returns it,
    used for programs with animations, see examples for demonstration
    """
    return Animator(millisec, callable, *args, **kwargs)

def translate(old, new, points):
    """Translate function takes 3 arguments the old position, new
    position and the points. The function translates all the points to
    the new position and returns the new points"""
    diff = new - old
    points[:] = points + diff
    return points

def translate_points(diff, points):
    """Translate function takes 2 arguments the with which the points
    are required to be translated and the points. The function
    translates all the points to the new position and returns the new
    points"""
    points[:] = points + diff
    return points

def _create_rotation_matrix(axis, angle):
    """Create a rotation matrix given an axis and an angle (in
    degrees) to rotate by.
    """
    axis = numpy.asarray(axis, dtype = float)
    axis /= sqrt(numpy.inner(axis, axis)) #Normalizing the axis
    x = axis[0]
    y = axis[1]
    z = axis[2]
    t = angle*pi/180
    cost = cos(t)
    sint = sin(t)
    rotator = numpy.zeros((3,3), float)
    rotator[0][0] = cost + (1-cost)*(x*x)
    rotator[0][1] = (1-cost)*x*y - (sint)*z
    rotator[0][2] = (1-cost)*x*z + (sint)*y

    rotator[1][0] = (1-cost)*y*x + (sint)*z
    rotator[1][1] = cost + (1-cost)*(y*y)
    rotator[1][2] = (1-cost)*y*z - (sint)*x

    rotator[2][0] = (1-cost)*z*x - (sint)*y
    rotator[2][1] = (1-cost)*z*y + (sint)*x
    rotator[2][2] = cost + (1-cost)*(z*z)
    return rotator

def axis_changed(old, new, pos, points):
    """The function takes 4 arguments, the old and the new axis, the
    position and points. All arguments should be given as a numpy
    array, The first 3 can also be given in form of a tuple. The
    function rotates all the points so that they become aligned with
    the new axis"""
    # Creating a working normalized copy of old axis
    o = old/float(sqrt(numpy.inner(old, old)))
    # Creating a working normalized copy of new axis
    n = new/sqrt(numpy.inner(new, new))
    dpdt = numpy.dot(o, n)
    if abs(abs(dpdt) - 1.0) < 1e-10:
        if dpdt < 0:
            #This is a must in the case when the new and the old axis are
            #opposite to each other
            diff = -pos
            points = translate_points(diff, points)
            #Flipping the points to reverse the axis
            points[:] = -points
            diff = pos
            points = translate_points(diff, points)
            return points
        else:
            #This is useful in the case when the new and the old axis are
            #very close to each other
            return points
    alpha = acos(dpdt)# Calculating angle between the old & new axis
    raxis = numpy.cross(o, n)# Calculating the axis about which to rotate
    #Creating the rotation multiplication matrix
    data = _create_rotation_matrix(raxis, 180.0*alpha/pi)

    if (numpy.allclose(pos, 0.0)):
        points[:] = numpy.dot(points, data.T)
        return points
    else:
        diff = -pos
        points = translate_points(diff, points)
        points[:] = numpy.dot(points, data.T)
        diff = pos
        points = translate_points(diff, points)
        return points

def rotate(axis, angle, origin, pos, points, maxis):
    """Rotate function takes 6 arguments the axis about which the
    actor has to be rotated, the angle with which the actor has to be
    rotated, the point (origin) about which actor has to be rotated
    and posistion, points and current axis of the actor. The function
    returns the new position, points and axis of the actor after the
    rotation."""
    data = _create_rotation_matrix(axis, angle)

    if (numpy.allclose(pos, 0.0) and numpy.allclose(origin, 0.0)):
        points[:] = numpy.dot(points, data.T)
        raxis = numpy.dot(maxis, data.T)
        return pos, points, raxis
    else:
        diff = (-1*origin[0], -1*origin[1], -1*origin[2])
        pos = pos - origin
        points = translate_points(diff, points)
        points[:] = numpy.dot(points, data.T)
        pos = numpy.dot(pos, data.T)
        diff = (origin[0], origin[1], origin[2])
        points = translate_points(diff, points)
        pos = pos + origin
        raxis = numpy.dot(maxis, data.T)
        return pos, points, raxis

def rotate_single_point(axis, angle, origin, pos, maxis):
    """Rotate function takes 5 arguments the axis about which the
    actor has to be rotated, the angle with which the actor has to be
    rotated, the point (origin) about which actor has to be rotated
    and posistion, and current axis of the actor. The function returns
    the new position and new axis of the actor after the rotation."""
    axis = numpy.asarray(axis, dtype = float)
    data = _create_rotation_matrix(axis, angle)

    if (numpy.allclose(pos, 0.0)):
        raxis = numpy.dot(maxis, data.T)
        return pos, raxis
    else:
        pos = pos - origin
        pos = numpy.dot(pos, data.T)
        pos = pos + origin
        raxis = pos/sqrt(numpy.inner(pos, pos))
        return pos, raxis

def scale(scale_factor, points, pos):
    """Scale function takes 2 arguments the scaling_factor in a form
    of list, or a tuple giving the scale factor for x,y and z
    axis. The function returns the new points ofthe actor after
    scaling"""
    #Creating the scaling multiplication matrix
    sc = numpy.asarray(scale_factor, dtype=float)
    data = numpy.diag(sc)

    if (numpy.allclose(pos, 0.0)):
        points[:] = numpy.dot(points, data.T)
        return points
    else:
        diff = (-1*pos[0], -1*pos[1], -1*pos[2])
        points = translate_points(diff, points)
        points[:] = numpy.dot(points, data.T)
        diff = (pos[0], pos[1], pos[2])
        points = translate_points(diff, points)
        return points

#################################################################
####################### Functionality classes ###################
#################################################################

class VTimer(Timer):
    def __init__(self, millisecs, callable, *args, **kw_args):
        #Initializing the init method of parent class Timer
        Timer.__init__(self, millisecs, callable, *args, **kw_args)
        self.viewer = get_viewer()
        self.viewer.on_trait_change(self._close, 'closing')

    def _close(self):
        self.Stop()
        print("Stopping iterations since the viewer has been closed.")

    def Notify(self):
        """Overridden to call the given callable.
        """
        try:
            self.callable(*self.args, **self.kw_args)
        except StopIteration:
            self.Stop()
        except:
            self.Stop()
            raise

class Animator(HasTraits):
    #####################################################################
    # Traits definitions

    start_animation = Button('Start Animation')
    stop_animation = Button('Stop Animation')
    time_period = Range(1, 100000, 100,
                      desc='Specifies frequency with which timer is called')

    itimer = Instance(VTimer)

    ######################################################################
    # User interface view

    event_group = Group(Item('start_animation', style = 'simple'),
                         Item('_'),
                         Item('stop_animation', style = 'simple'),
                         Item('_'),
                         show_labels = False,)

    traits_view = View(event_group,
                       Item(name = 'time_period'),
                       title = 'Animation Controler', buttons = ['OK'], width = 250)


    ######################################################################
    # Initialize object
    def __init__(self, millisec, callable, *args, **kwargs):
        self.time_period = millisec
        self.itimer = VTimer(millisec, callable, *args, **kwargs)

    ######################################################################
    # Non-public methods, Event handlers
    def _start_animation_fired(self):
        self.itimer.Start()

    def _stop_animation_fired(self):
        self.itimer.Stop()

    def _time_period_changed(self, value):
        t = self.itimer
        if t is None:
            return
        t.millisec = value
        if t.IsRunning():
            t.Stop()
            t.Start(value)

class MVector(numpy.ndarray):
    """MVector class gives many of the functionalities given by Vector
    of VPython"""
    def __new__(subtype, x = 0.0, y = 0.0, z = 0.0):
        data = numpy.array((x, y, z), float)
        ret = numpy.ndarray.__new__(subtype, shape = (3,),
                                    buffer = data, dtype=float,
                                    order = False)
        return ret.copy()

    def _get_x(self):
        return self[0]

    def _set_x(self, val):
        self[0] = val

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self[1]

    def _set_y(self, val):
        self[1] = val

    y = property(_get_y, _set_y)

    def _get_z(self):
        return self[2]

    def _set_z(self, val):
        self[2] = val

    z = property(_get_z, _set_z)

    def dot(vec1, vec2):
        """ Function performs the dot vector multiplication of 2
        vector instances and returning a new vector instance equal to
        the dot product of given vectors"""
        i = vec1.x * vec2.x
        j = vec1.y * vec2.y
        k = vec1.z * vec2.z
        dot = i + j + k
        return dot

    def cross(vec1, vec2):
        """ Function performing the cross vector multiplication of 2
        vector instances and returning a new vector instance equal to
        the cross product of given vectors"""
        i = (vec1.y*vec2.z - vec1.z*vec2.y)
        j = (vec1.z*vec2.x - vec1.x*vec2.z)
        k = (vec1.x*vec2.y - vec1.y*vec2.x)
        cross = MVector(i, j, k)
        return cross

    def mag(vec):
        """ Function computes and returns the magnitude of a vector"""
        mag = sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
        return mag

    def norm(vec):
        """ Function computes and returns the normalized form of a
        given vector"""
        norm = vec/sqrt(numpy.inner(vec, vec))
        return norm

class Frame(HasTraits):
    """Frame groups together all the actors given to it into a single
    unit, so that they can be manipulated as a combined entity."""
    #####################################################################
    # Traits definitions

    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the frame axis')
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of frame objects')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of frame objects')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of frame objects')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the frame pos')
    objects = List
    visibility = Bool(True)
    viewer = Any

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'visibility'),
                             label = 'Frame Properties',
                             show_border = True),
                             buttons=['OK'],
                             )

    def __init__(self, *arguments, **traits):
        self.arg = list(arguments)
        HasTraits.__init__(self, **traits)

        self.keys = list(traits.keys())

        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self._x_changed(0.0, self.x)
        self._y_changed(0.0, self.y)
        self._z_changed(0.0, self.z)
        #self._axis_changed(numpy.array([1.0, 0.0, 0.0]), self.axis)

    ######################################################################
    # Non-public methods, Event handlers
    def _pos_changed(self, old, new):
        diff = new - old
        for a in self.arg:
            a.pos = a.pos + diff

    def _x_changed(self, old, new):
        diff = new - old
        for a in self.arg:
            a.x = a.x + diff

    def _y_changed(self, old, new):
        diff = new - old
        for a in self.arg:
            a.y = a.y + diff

    def _z_changed(self, old, new):
        diff = new - old
        for a in self.arg:
            a.z = a.z + diff

    def _axis_changed(self, old, new):
        if (numpy.allclose(old, new)):
            pass
        else:
            o = old/sqrt(numpy.inner(old, old))
            n = new/sqrt(numpy.inner(new, new))
            raxis = numpy.cross(o, n)
            # raxis is the axis about which the rotation of th objects
            # will be performed so that they have the new axis
            alpha = acos(numpy.dot(o, n))
            # alpha is the angle between the old and the new axis
            alpha = 180.0*alpha/pi
            for a in self.arg:
                a.rotate(alpha, raxis, self.pos)

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            for a in self.arg:
                a.actor.visibility = 1
        else:
            for a in self.arg:
                a.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        for a in self.arg:
            a.rotate(angle, axis, origin)
        pts = numpy.array([1.0, 0.0, 0.0])#junk points passed as arguments
        pos, pts, faxis = rotate(axis, angle, origin, self.pos, pts, self.axis)
        self.trait_set(pos=pos, axis = faxis, trait_change_notify = False)


###################################################################
###################### Actor Classes ##############################
###################################################################

class Curve(HasTraits):
    """Curve class creates a polydata source using point and
    connectivity arrays given by the user, which inturn is used to
    create a polydata actor"""
    #####################################################################
    # Traits definitions

    points = Array(dtype=float, shape=(None,3), desc='the points of the curve')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the curve pos')
    radius = Range(0.0, 1.0e299, value = 0.01, desc = 'the radius of curve tube')
    axis = Array(value=(1.0, 0.0, 0.0), desc = 'the curve axis')
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of curve')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of curve')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of curve')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)

    polydata = Instance(tvtk.PolyData, args=())
    property = Instance(tvtk.Property)
    stripper = Instance(tvtk.Stripper, args=())
    tube = Instance(tvtk.TubeFilter, args=())
    actor = Instance(tvtk.Actor, args=()) # tvtk Actor, for the usual pipeline architecture.

    viewer = Any

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'radius'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'representation'),
                             label = 'Curve Properties',
                             show_border = True),
                             buttons=['OK'],
                             )

    def __init__(self, **traits):
        self.property = self.actor.property

        configure_input(self.stripper, self.polydata)
        configure_input(self.tube, self.stripper)
        self.tube.number_of_sides = 4
        self.tube.capping = 1

        m = tvtk.PolyDataMapper()
        configure_input(m, self.tube)
        self.actor.mapper = m
        self.stripper.update()
        self.tube.update()
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor)
        self.viewer = get_viewer()

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)
        self.tube.on_trait_change(self.viewer.scene.render)

        axis = traits.pop('axis', None)
        HasTraits.__init__(self, **traits)

        self._points_changed(self.points)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._radius_changed(self.radius)
        if axis is not None:
            self._axis_changed(numpy.array((1.0, 0.0, 0.0)),
                               numpy.asarray(axis, dtype=float))


    ######################################################################
    # Object's public methods
    def append(self, pnt):
        """Function appeneds new points given as arguments to the
        current points"""
        self.extend([pnt])

    def extend(self, pts):
        if self.points is None:
            p = pts
        else:
            n = self.points.shape[0]
            p = numpy.resize(self.points, (n+len(pts), 3))
            p[:n] = self.points
            p[n:] = pts
        self.points = p
        self.update()

    def update(self):
        self.polydata.modified()
        self.stripper.update()
        self.tube.update()
        self.viewer.scene.render()

    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, numpy.array([0.0, 0.0, 0.0]))
        self.trait_set(pos = p, trait_change_notify = False)
        self.trait_set(points = pi, trait_change_notify = False)
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.stripper.update()
        self.tube.update()
        self.render()

    def render(self):
        """Function redraws/refreshs the ivtk viewer's scene"""
        v = self.viewer
        if v is not None:
            v.scene.render()

    ######################################################################
    # Non-public methods, Event handlers
    def _points_changed(self, value):
        self.polydata.lines = None
        self.polydata.points = value
        if value is None:
            np = 0
            lines = None
        else:
            np = len(self.points) - 1
            lines = numpy.zeros((np, 2), 'l')
            lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
            lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
        self.polydata.lines = lines
        self.polydata.modified()
        self.stripper.update()
        self.tube.update()
        v = self.viewer
        if v is not None:
            v.scene.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        p = translate(old, new, self.points)
        self.trait_set(points = p, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.stripper.update()
        self.tube.update()
        self.render()

    def _axis_changed(self, old, new):
        pts = axis_changed(old, new, self.pos, self.points)
        self.points = pts.copy()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _radius_changed(self, value):
        self.tube.radius = self.radius

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

class Ring(HasTraits):
    """Ring class creates a Ring form tvtk polydata, follows
    the usual VTK pipeline and creates a ring actor."""
    #####################################################################
    # Traits definitions

    points = Array('d', shape = (360,3))
    radius = Range(-1e299, 1e299, value = 0.5, desc = 'the ring radius')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the ring pos')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the ring axis')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of ring center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of ring center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of ring center')
    representation = Enum('s', 'w', 'p')
    thickness = Range(0, 1e299, value = 0.01, desc = 'the ring thickness')
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    property = Instance(tvtk.Property)
    tube = Instance(tvtk.TubeFilter, ())
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    normals = Instance(tvtk.PolyDataNormals(), ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius'),
                             Item(name = 'thickness'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Ring Properties',
                             show_border = True),
                             buttons=['OK'],
                        )

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        configure_input(self.tube, self.normals)
        self.normals.update()
        self.tube.update()
        self.tube.number_of_sides = 4
        self.tube.capping = 1

        m = tvtk.PolyDataMapper()
        configure_input(m, self.tube)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation

        self.viewer = get_viewer()
        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)
        self.tube.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points()
        self._pos_changed([0.0, 0.0, 0.0], self.pos)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._thickness_changed(self.thickness)
        self._axis_changed(numpy.array((1.0, 0.0, 0.0)), self.axis)

        show_actor(self.actor)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self):
        for i in range(0,360,1):
            theta = i*pi/180
            self.points[i][0] = 0.0
            self.points[i][1] = self.radius*sin(theta)
            self.points[i][2] = self.radius*cos(theta)

        np = len(self.points) - 1
        lines = numpy.zeros((np, 2), 'l')
        lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
        lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
        self.polydata.points = self.points
        self.polydata.lines = lines
        v = self.viewer
        if v is not None:
            v.scene.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _radius_changed(self, old, new):
        factor = new/old

        if (numpy.allclose(self.pos, 0.0)):
            self.points[:] = factor*self.points[:]
            self.polydata.modified()
            self.normals.update()
            self.tube.update()
            self.render()
        else:
            c = self.pos
            diff = (0.0, 0.0, 0.0) - c
            self.points = translate_points(diff, self.points)
            self.points[:] = factor*self.points[:]
            diff = c
            self.points = translate_points(diff, self.points)
            self.polydata.points = self.points
            self.polydata.modified()
            self.normals.update()
            self.tube.update()
            self.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        self.points = translate(old, new, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        self.actor.visibility = value

    def _thickness_changed(self, value):
        self.tube.radius = value

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: angle with which to
        rotate the actor, and the axis about which to rotate the
        actor, the 3rd agrument is origin i.e. the point about which
        to rotate the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()


class Cone(HasTraits):
    """Cone class creates Cone from polydata obtained from tvtk
    ConeSource, follows the usual VTK pipeline and creates a Cone
    actor, which is passed to the show_actor() function as an
    argument.
    """
    #####################################################################
    # Traits definitions

    points = Array('d', shape = (7,3))
    radius = Range(0.0, 100.0, value = 0.5, desc = 'the cone radius')
    height = Range(0.0, 100.0, value = 1.0, desc = 'the cone height')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the cone pos')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the cone axis')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of cone center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of cone center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of cone center')
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    property = Instance(tvtk.Property)
    actor = Instance(tvtk.Actor, ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius'),
                             Item(name = 'height'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Cone Properties',
                             show_border = True),
                             buttons=['OK'],
                             )

    def __init__(self, **traits):
        self.property = self.actor.property

        m = tvtk.PolyDataMapper()
        configure_input(m, self.polydata)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation

        self.viewer = get_viewer() # getting the ivtk viewer
        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points(self.radius, self.height, self.pos, self.axis)
        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self._color_changed(self.color)

        show_actor(self.actor) # passing the actors function for rendering

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, r, h, c, d):
        cs = tvtk.ConeSource(radius=r, height=h, center=tuple(c),
                             direction=tuple(d))
        cs.update()
        ps = cs.output

        points = ps.points.to_array()
        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _color_changed(self, value):
        self.actor.property.color = value

    def _radius_changed(self):
        points, lines = self._create_points(self.radius, self.height, self.pos, self.axis)
        self.polydata.points = points
        self.polydata.modified()
        self.render()

    def _height_changed(self):
        points, lines = self._create_points(self.radius, self.height, self.pos, self.axis)
        self.polydata.points = points
        self.polydata.modified()
        self.render()

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        points, lines = self._create_points(self.radius, self.height, self.pos, self.axis)
        self.points = points
        self.polydata.modified()
        self.render()

    def _axis_changed(self):
        points, lines = self._create_points(self.radius, self.height, self.pos, self.axis)
        self.polydata.points = points
        self.polydata.modified()
        self.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

class Sphere(HasTraits):
    """Sphere class creates Sphere from tvtk SphereSource, follows the
    usual VTK pipeline and creates a Sphere actor, which is passed to
    the show_actor() function as an argument.
    """
    #####################################################################
    # Traits definitions

    radius = Range(0.0, 1e299, value = 0.5, desc = 'the sphere radius')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the sphere pos')
    axis = Array(value = (1.0, 0.0, 0.0), desc= 'the sphere axis')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of sphere center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of sphere center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of sphere center')
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    property = Instance(tvtk.Property)
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    normals = Instance(tvtk.PolyDataNormals, ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius', style = 'simple'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Sphere Properties',
                             show_border = True),
                             buttons=['OK'],
                             )

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        self.normals.update()
        m = tvtk.PolyDataMapper() # the usual vtk pipleine countinuation
        configure_input(m, self.normals)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor) # passing the actors function for rendering
        self.viewer = get_viewer() # getting the ivtk viewer

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points(self.radius, self.pos)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)


    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, r, c):
        sp = tvtk.SphereSource(radius = r, center = tuple(c),
                               phi_resolution = 20,
                               theta_resolution = 20)
        sp.update()
        ps = sp.output

        points = ps.points.to_array()
        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _radius_changed(self, value):
        points, polys = self._create_points(self.radius, self.pos)
        self.polydata.points = points
        self.polydata.modified()
        self.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        points, lines = self._create_points(self.radius, self.pos)
        self.polydata.points = points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()

class Cylinder(HasTraits):
    """Cylinder class creates Cylinder from tvtk CylinderSource,
    follows the usual VTK pipeline and creates a Sphere actor, which
    is passed to the show_actor() function as an argument.
    """
    #####################################################################
    # Traits definitions

    # XXX: These should really not be ranges, but positive numbers.
    radius = Range(0.0, 1e299, value = 1.0, desc = 'the cylinder radius')
    length = Range(0.0, 1e299, value = 1.0, desc = 'the cylinder length')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the cylinder pos')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the cylinder axis')
    points = Array('d', shape = (60,3))
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of cylinder center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of cylinder center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of cylinder center')
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    property = Instance(tvtk.Property)
    normals = Instance(tvtk.PolyDataNormals(), ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius', style = 'simple'),
                             Item(name = 'length', style = 'simple'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Cylinder Properties',
                             show_border = True),
                             buttons=['OK'],
                             )

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        m = tvtk.PolyDataMapper() # the usual vtk pipleine countinuation
        configure_input(m, self.normals)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor) # passing the actors function for rendering
        self.viewer = get_viewer() # getting the ivtk viewer

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points(self.radius, self.pos, self.length)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._axis_changed(numpy.array([1.0, 0.0, 0.0]), self.axis)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, r, c, h):
        cp = tvtk.CylinderSource(radius = r, height = h, resolution = 15)
        cp.update()
        ps = cp.output
        points = ps.points.to_array()
        l = len(points)
        for i in range(0, l, 1):
            points[i][1] = points[i][1] + h/2.0
        points = axis_changed(numpy.array([0.0,1.0,0.0]),numpy.array([1.0,0.0,0.0]),numpy.array([0.0, 0.0, 0.0]), points)
        points = translate(numpy.array([0.0, 0.0, 0.0]), self.pos, points)
        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _radius_changed(self, old, new):
        self.points, polys = self._create_points(self.radius, self.pos, self.length)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _length_changed(self, value):
        self.points, polys = self._create_points(self.radius, self.pos, self.length)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        self.points = translate(old, new, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

class Box(HasTraits):
    """Box class creates Box from tvtk CubeSource, follows the usual
    VTK pipeline and creates a Cube actor, which is passed to the
    show_actor() function as an argument.
    """
    #####################################################################
    # Traits definitions

    size = Tuple((1.0, 1.0, 1.0), desc = 'the box size')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the Box pos')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of box center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of box center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of box center')
    representation = Enum('s', 'w', 'p')
    length = Range(0, 1e299, 1.0, desc = 'the box length')
    height = Range(0, 1e299, 1.0, desc = 'the box height')
    width = Range(0, 1e299, 1.0, desc = 'the box width')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the box axis')
    points = Array('d', shape = (24,3))
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    property = Instance(tvtk.Property)

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'length'),
                             Item(name = 'height'),
                             Item(name = 'width'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Box Properties',
                             show_border = True),
                             buttons = ['OK'],
                             )

    def __init__(self, **traits):
        self.property = self.actor.property

        m = tvtk.PolyDataMapper() # the usual vtk pipleine countinuation
        configure_input(m, self.polydata)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor) # passing the actors function for rendering
        self.viewer = get_viewer() # getting the ivtk viewer

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points(self.size, self.pos)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._axis_changed(numpy.array([1.0, 0.0, 0.0]), self.axis)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)
        self._length_changed(self.length)
        self._height_changed(self.height)
        self._width_changed(self.width)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, s, c):
        cp = tvtk.CubeSource(x_length = s[0], y_length = s[1], z_length = s[2], center = tuple(c))
        cp.update()
        ps = cp.output
        points = ps.points.to_array()

        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _size_changed(self, old, new):
        self.trait_set(length = new[0], trait_change_notify = False)
        self.trait_set(height = new[1], trait_change_notify = False)
        self.trait_set(width = new[2], trait_change_notify = False)
        self.points, lines = self._create_points(self.size, self.pos)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        self.points = translate(old, new, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _length_changed(self, value):
        self.size = (self.length, self.size[1],self.size[2])

    def _height_changed(self, value):
        self.size = (self.size[0], self.height, self.size[2])

    def _width_changed(self, value):
        self.size = (self.size[0], self.size[1], self.width)

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        #self.connectivity.points = self.points
        self.polydata.modified()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

class Arrow(HasTraits):
    """Arrow class creates Arrow from tvtk ArrowSource, follows the
    usual VTK pipeline and creates a Arrow actor, which is passed to
    the show_actor() function as an argument.
    """
    #####################################################################
    # Traits definitions

    points = Array('d', shape = (31 ,3))
    radius_cone = Range(0.0, 10.0, value = 0.08, desc = 'the radius of cone portion of arrow')
    radius_shaft = Range(0.0, 5.0, value = 0.03, desc = 'the radius of shaft portion of arrow')
    length_cone = Range(0.0, 1.0, value = 0.35, desc = 'shaft length of arrow')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the arrow axis')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the Arrow pos')
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of arrow center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of arrow center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of arrow center')
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)
    viewer = Any

    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    property = Instance(tvtk.Property)
    polydata = Instance(tvtk.PolyData, ())
    normals = Instance(tvtk.PolyDataNormals(), ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius_cone'),
                             Item(name = 'length_cone'),
                             Item(name = 'radius_shaft'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Arrow Properties',
                             show_border = True), buttons=['OK'])

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        self.normals.update()
        m = tvtk.PolyDataMapper() # the usual vtk pipleine countinuation
        configure_input(m, self.normals)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor) # passing the actors function for rendering
        self.viewer = get_viewer() # getting the ivtk viewer

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points(self.radius_cone, self.length_cone, self.radius_shaft, self.pos)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)
        self._axis_changed(numpy.array((1.0, 0.0, 0.0)), self.axis)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, rc, lc, rs, ps):
        asrc = tvtk.ArrowSource(tip_radius=rc, tip_length=lc, shaft_radius=rs)
        asrc.update()
        ps = asrc.output
        points = ps.points.to_array()
        points = translate(numpy.array([0.0, 0.0, 0.0]), self.pos, points)
        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _radius_cone_changed(self, old, new):
        self.points, polys = self._create_points(self.radius_cone, self.length_cone, self.radius_shaft, self.pos)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _length_cone_changed(self, old, new):
        self.points, polys = self._create_points(self.radius_cone, self.length_cone, self.radius_shaft, self.pos)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _radius_shaft_changed(self, old, new):
        self.points, polys = self._create_points(self.radius_cone, self.length_cone, self.radius_shaft, self.pos)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        self.points = translate(old, new, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

class Helix(HasTraits):
    """Helix class creates Helix/Spring from tvtk polydata, follows the
    usual VTK pipeline and creates an Helix actor, which is passed to
    the show_actor() function as an argument.
    """
    #####################################################################
    # Traits definitions

    coils = Int(5)
    points = Array('d', shape = (None, 3))
    radius = Range(0.01, 1e299, value = 0.2, desc = 'the helix radius')
    length = Range(0.01, 1e299, value = 1.0, desc = 'the helix length')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'the helix position')
    axis = Array(value = (1.0, 0.0, 0.0), desc = 'the helix axis')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    x = Range(-1e299, 1e299, 0.0, desc = 'the X coordinate of helix center')
    y = Range(-1e299, 1e299, 0.0, desc = 'the Y coordinate of helix center')
    z = Range(-1e299, 1e299, 0.0, desc = 'the Z coordinate of helix center')
    representation = Enum('s', 'w', 'p')
    thickness = Range(0, 1e299, value = 0.01, desc = 'the helix thickness')

    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    property = Instance(tvtk.Property)
    tube = Instance(tvtk.TubeFilter, ())
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    normals = Instance(tvtk.PolyDataNormals(), ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius'),
                             Item(name = 'length'),
                             Item(name = 'thickness'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Helix Properties',
                             show_border = True), buttons=['OK'])

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        configure_input(self.tube, self.normals)
        self.tube.number_of_sides = 4
        self.tube.capping = 1

        m = tvtk.PolyDataMapper()
        configure_input(m, self.tube)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation
        show_actor(self.actor)
        self.viewer = get_viewer()

        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)
        self.tube.on_trait_change(self.viewer.scene.render)

        HasTraits.__init__(self, **traits)

        self._create_points()
        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._thickness_changed(self.thickness)
        self._axis_changed(numpy.array((1.0, 0.0, 0.0)), self.axis)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self):
        h = self.length/(self.coils*10)
        cons = self.length/(self.coils*10)
        j = 0
        self.points = numpy.resize(self.points, (self.coils*10, 3))
        for i in range(0,self.coils*360,36):
            theta = i*pi/180
            self.points[j][0] = h
            self.points[j][1] = self.radius*sin(theta)
            self.points[j][2] = self.radius*cos(theta)
            j = j+1
            h = h + cons

        np = len(self.points) - 1
        lines = numpy.zeros((np, 2), 'l')
        lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
        lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
        self.polydata.points = self.points
        self.polydata.lines = lines
        self.normals.update()
        self.tube.update()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _radius_changed(self, old, new):
        self._create_points()
        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self.change_axis(numpy.array((1.0, 0.0, 0.0)), self.axis)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _coils_changed(self, old, new):
        p = numpy.arange(self.coils*10*3, dtype = float)
        p = p.reshape(self.coils*10,3)
        h = self.length/(self.coils*10)
        cons = self.length/(self.coils*10)
        j = 0
        for i in range(0,self.coils*360,36):
            theta = i*pi/180
            p[j][0] = h
            p[j][1] = self.radius*sin(theta)
            p[j][2] = self.radius*cos(theta)
            j = j+1
            h = h + cons

        np = len(p) - 1
        lines = numpy.zeros((np, 2), 'l')
        lines[:,0] = numpy.arange(0, np-0.5, 1, 'l')
        lines[:,1] = numpy.arange(1, np+0.5, 1, 'l')
        self.polydata.points = p
        self.polydata.lines = lines
        self.points = p
        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self.change_axis(numpy.array((1.0, 0.0, 0.0)), self.axis)
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        self.points = translate(old, new, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _axis_changed(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def change_axis(self, old, new):
        self.points = axis_changed(old, new, self.pos, self.points)
        self.polydata.points = self.points

    def _length_changed(self, old, new):
        self._create_points()
        v = self.viewer
        if v:
            v.scene.disable_render = True
        self._pos_changed(numpy.array([0.0, 0.0, 0.0]), self.pos)
        self.change_axis(numpy.array((1.0, 0.0, 0.0)), self.axis)
        if v:
            v.scene.disable_render = False
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    def _thickness_changed(self, value):
        self.tube.radius = value

    ######################################################################
    # Object's public methods
    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.tube.update()
        self.render()

    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

class Ellipsoid(HasTraits):
    """Ellipsoid class creates Ellipsoid from tvtk SphereSource by
    suitably scaling it, follows the usual VTK pipeline and creates a
    Ellipsoid actor, which is passed to the show_actor() function as
    an argument.
    """
    #####################################################################
    # Traits definitions

    radius = Range(0.0, 1e299, value = 0.5, desc = 'Undistorted ellipsoid radius')
    pos = Array(value = (0.0, 0.0, 0.0), desc = 'Ellipsoid pos')
    color = vtk_color_trait((1.0, 1.0, 1.0))
    axis = Array(value = (1.0, 0.0, 0.0), desc= 'Ellipsoid axis')
    size = Array(value = (1.0, 0.5, 1.0), desc= 'Ellipsoid size_factor')
    length = Range(0.0, 1e299, 1.0, desc = 'Scaling factor in X direction')
    height = Range(0.0, 1e299, 0.5, desc = 'Sscaling factor in Y direction')
    width = Range(0.0, 1e299, 1.0, desc = 'Scaling factor in Z direction')
    x = Range(-1e299, 1e299, 0.0, desc = 'X coordinate of ellipsoid center')
    y = Range(-1e299, 1e299, 0.0, desc = 'Y coordinate of ellipsoid center')
    z = Range(-1e299, 1e299, 0.0, desc = 'Z coordinate of ellipsoid center')
    representation = Enum('s', 'w', 'p')
    visibility = Bool(True)
    viewer = Any

    polydata = Instance(tvtk.PolyData, ())
    property = Instance(tvtk.Property)
    actor = Instance(tvtk.Actor, ()) # tvtk Actor, for the usual pipeline architecture.
    normals = Instance(tvtk.PolyDataNormals(), ())

    ######################################################################
    # User interface view

    traits_view = View(Group(Item(name = 'radius', style = 'simple'),
                             Item(name = 'x', label = 'Pos X'),
                             Item(name = 'y', label = 'Pos Y'),
                             Item(name = 'z', label = 'Pos Z'),
                             Item(name = 'length', label = 'Length'),
                             Item(name = 'height', label = 'Height'),
                             Item(name = 'width', label = 'Width'),
                             Item(name = 'color'),
                             Item(name = 'visibility'),
                             Item(name = 'representation'),
                             label = 'Ellipsoid Properties',
                             show_border = True), buttons=['OK'])

    def __init__(self, **traits):
        self.property = self.actor.property

        self.normals = tvtk.PolyDataNormals()
        configure_input(self.normals, self.polydata)
        m = tvtk.PolyDataMapper()
        configure_input(m, self.normals)
        self.actor.mapper = m
        self.property = self.actor.property
        self.property.representation = self.representation

        HasTraits.__init__(self, **traits)

        self._create_points(self.radius, self.pos)
        self._color_changed(self.color)
        self._visibility_changed(self.visibility)
        self._x_changed(self.x)
        self._y_changed(self.y)
        self._z_changed(self.z)
        self._axis_changed(numpy.array((1.0, 0.0, 0.0)), self.axis)

        show_actor(self.actor) # passing the actors function for rendering
        self.viewer = get_viewer() # getting the ivtk viewer
        self.property.on_trait_change(self.viewer.scene.render)
        self.actor.on_trait_change(self.viewer.scene.render)

    ######################################################################
    # Non-public methods, Event handlers
    def _create_points(self, r, c):
        sp = tvtk.SphereSource(radius=r, center=tuple(c),
                               phi_resolution=20, theta_resolution=20)
        sp.update()
        ps = sp.output

        points = ps.points.to_array()
        points = scale(self.size, points, self.pos)
        self.points = points
        self.polydata.points = self.points
        self.polydata.polys = ps.polys
        return points, ps.polys

    def _radius_changed(self, value):
        points, polys = self._create_points(self.radius, self.pos)
        self.polydata.points = points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _size_changed(self, value):
        points, polys = self._create_points(self.radius, self.pos)
        self.trait_set(length=value[0], height=value[1],  width=value[2],
                 trait_change_notify=False)
        self.polydata.points = points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _color_changed(self, value):
        self.actor.property.color = value

    def _pos_changed(self, old, new):
        self.trait_set(x = new[0], trait_change_notify = False)
        self.trait_set(y = new[1], trait_change_notify = False)
        self.trait_set(z = new[2], trait_change_notify = False)
        points, lines = self._create_points(self.radius, self.pos)
        self.polydata.points = points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _axis_changed(self, old, new):
        points = axis_changed(old, new, self.pos, self.points)
        self.points = points
        self.polydata.points = self.points
        self.polydata.modified()
        self.normals.update()
        self.render()

    def _x_changed(self, value):
        self.x = value
        self.pos = (self.x, self.pos[1],self.pos[2])

    def _y_changed(self, value):
        self.y = value
        self.pos = (self.pos[0], self.y, self.pos[2])

    def _z_changed(self, value):
        self.z = value
        self.pos = (self.pos[0], self.pos[1], self.z)

    def _representation_changed(self, value):
        self.property.representation = self.representation
        self.property.modified()
        self.render()

    def _length_changed(self, value):
        self.x_scale = value
        self.size = (self.length, self.size[1], self.size[2])

    def _height_changed(self, value):
        self.y_scale = value
        self.size = (self.size[0], self.height, self.size[2])

    def _width_changed(self, value):
        self.z_scale = value
        self.size = (self.size[0], self.size[1], self.width)

    def _visibility_changed(self, value):
        val = int(value)
        if (val == 1):
            self.actor.visibility = 1
        else:
            self.actor.visibility = 0

    ######################################################################
    # Object's public methods
    def render(self):
        v = self.viewer
        if v is not None:
            v.scene.render()

    def rotate(self, angle, axis, origin = numpy.array([0.0, 0.0, 0.0])):
        """Function takes atleast 2 arguments: axis about which to
        rotate the actor and angle with which to rotate the actor, the
        3rd agrument is origin i.e. the point about which to rotate
        the actor, by default it is set to the global origin"""
        p, pi, ax = rotate(axis, angle, origin, self.pos, self.points, self.axis)
        self.trait_set(pos = p, trait_change_notify = False)
        self.points = pi
        self.trait_set(axis = ax, trait_change_notify = False)
        self.polydata.points = self.points
        self.polydata.modified()
        self.render()


###########################################################
################### Compatibility layer ###################
###########################################################

sphere = Sphere
vector = MVector
frame = Frame
curve = Curve
ring = Ring
cone = Cone
cylinder = Cylinder
box = Box
arrow = Arrow
helix = Helix
ellipsoid = Ellipsoid
mag = numpy.linalg.norm

def rate(arg):
    msg = """Do not use rate, instead use the iterate() function.
    Iterate should be called with a callback.  This callback will be
    periodically called via a timer.  This will make your script's UI
    completely interactive.
    """
    print('*'*80)
    print(msg)
    print('*'*80)


############################################################
# Some examples.

def test_remove_actors():
    """Test fuction for testing integrity of remove function for
    actors"""
    s = sphere(radius = 1.5, pos = (0, 0, 0), color = (1, 0, 0))
    b = box(center = (1, 0, 0), size = (2, 1, 1), color = (0.5, 0.5, 1.0))
    co = cone(resolution = 100, pos = (2, 0, 0), color = (0, 1, 0))
    cy = cylinder(resolution = 100, pos = (3, 0, 0), color = (0, 0, 1))

    time.sleep(3)
    print("Removed sphere from scene")
    remove_actor(s)

    time.sleep(3)
    print("Removed cone from cone")
    remove_actor(co)

def test_frame():
    c1 = cone(pos = (3.0, 0.0, 0.0))
    r1 = ring()
    f = frame(r1,c1)
    f.edit_traits()
    return f

def rotate_frame():
    """Test fuction for testing integrity of rotation function of
    frame"""
    r1 = ring(pos = (1,0,0))
    h1 = helix(pos = (1,0,0))
    f = frame(r1,h1)
    f.pos = (2,0,0)
    f.axis = (1,1,1)
    j = 1
    def anim():
        f.rotate(j, [0.0, 1.0, 0.0])
    ti = iterate(200, anim)
    ti.edit_traits()
    return ti

def test_rotate():
    """Test fuction for testing integrity of rotation function of
    actors"""
    r = ring()
    r.pos = (3,0,0)
    r2 = ring(pos = (3,0,0))
    points1 = r2.points
    r.rotate(90, [0,1,0], [1,0,0])
    r.rotate(-90, [0,1,0], [1,0,0])
    points2 = r.points
    if (numpy.allclose(points1, points2)):
        print("All clear")
    else:
        print("Test failed")
    return r

def test_translate():
    """This is a basic examples function demonstrating the creating
    simple animation from visual actors.  Note the show function has
    to be called in stand alone programs."""
    b = box()
    xlen = 10
    s = sphere(pos = (xlen, 0, 0))
    s.velocity = (-1,0,0)

    def anim():
        x = s.x
        if (x < 1):
            s.velocity = (1, 0, 0)
        elif (x > xlen):
            s.velocity = (-1, 0, 0)
        s.x = x + s.velocity[0]

    ti = iterate(50, anim)
    ti.edit_traits()

def test_bounce():
    """This is a basic example function, extending the previous
    example."""
    xlen = 10
    b1 = box(size = (1, 4, 4), color = (0,1,0))
    b2 = box(size = (1, 4, 4), color = (0,1,0), pos = (xlen, 0, 0))
    s = sphere(radius = 0.5, pos = (xlen, 0, 0), color = (1, 0, 0))
    s.velocity = (-1, 0, 0)

    def anim():
        x = s.x
        if (x == 1):
            s.velocity = (1, 0, 0)
        elif (x == (xlen-1)):
            s.velocity = (-1, 0, 0)
        s.x = x + s.velocity[0]

    t = iterate(60, anim)
    t.edit_traits()
    return t
