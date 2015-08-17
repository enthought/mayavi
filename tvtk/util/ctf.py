"""Color transfer function related code.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006-2015, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import List
from tvtk.api import tvtk


##########################################################################
# Color transfer function related utility code from MayaVi1.
##########################################################################
def _err_msg(obj, cls_name):
    return '%s %s does not have either a "nodes" attribute or a '\
           '"get_node_value" method'%(cls_name, str(obj))

def save_ctfs(volume_property):
    """Given a `tvtk.VolumeProperty` it saves the state of the RGB and
    opacity CTF to a dictionary and returns that.

    The 'rgb' key stores a list of (x, r, g, b) and the 'alpha' a list
    of (x, a) values.
    """
    vp = volume_property
    ctf = vp.rgb_transfer_function
    otf = vp.get_scalar_opacity()
    s1, s2 = ctf.range
    # The RGB values.
    nc = ctf.size
    rgb = []
    if hasattr(ctf, 'nodes'):
        for i in range(nc):
            x = ctf.nodes[i]
            r, g, b = ctf.get_color(x)
            rgb.append([x, r, g, b])
    elif hasattr(ctf, 'get_node_value'):
        val = [0]*6
        for i in range(nc):
            ctf.get_node_value(i, val)
            rgb.append(val[:4])
    else:
        raise TypeError(_err_msg(ctf, 'ColorTransferFunction'))

    # The Alpha values.
    na = otf.size
    a = []
    if hasattr(otf, 'nodes'):
        for i in range(na):
            x = otf.nodes[i]
            val = otf.get_value(x)
            a.append([x, val])
    elif hasattr(otf, 'get_node_value'):
        val = [0]*4
        for i in range(na):
            otf.get_node_value(i, val)
            a.append(val[:2])
    else:
        raise TypeError(_err_msg(otf, 'PiecewiseFunction'))

    return {'range': (s1, s2), 'rgb':rgb, 'alpha':a}

def load_ctfs(saved_data, volume_property):
    """ Given the saved data produced via `save_ctfs`, this sets the
    state of the passed volume_property appropriately.

    It returns the new color transfer function and piecewise function.
    """
    rgb = saved_data['rgb']
    a = saved_data['alpha']

    # The new_ctf/otf shenanigans are necessary because if the ctf/otf
    # go out of scope we loose the node information.  This is because
    # the tvtk object is really a dynamically generated wrapper.

    # First do the RGB values ...
    new_ctf = True
    ctf = volume_property.rgb_transfer_function
    if isinstance(ctf, ColorTransferFunction):
        new_ctf = False
        ctf.remove_all_points()
    else:
        ctf = ColorTransferFunction()
    nc = len(rgb)
    for i in range(nc):
        ctf.add_rgb_point(rgb[i][0], *(rgb[i][1:]))
    if new_ctf:
        volume_property.set_color(ctf)
    try:
        ctf.range = saved_data['range']
    except Exception:
        # VTK versions < 5.2 don't seem to need this.
        pass
    # and then the alpha values.
    na = len(a)
    new_otf = True
    otf = volume_property.get_scalar_opacity()
    if isinstance(otf, PiecewiseFunction):
        new_otf = False
        otf.remove_all_points()
    else:
        otf = PiecewiseFunction()
    for i in range(na):
        otf.add_point(a[i][0], a[i][1])
    if new_otf:
        volume_property.set_scalar_opacity(otf)
    return ctf, otf

def rescale_ctfs(volume_property, new_range):
    """ Given the volume_property with a new_range for the data while
    using the same transfer functions, this function rescales the
    CTF's so that everything works OK.

    It returns the CTF and OTF.
    """
    ctf = volume_property.rgb_transfer_function
    otf = volume_property.get_scalar_opacity()
    old_range = ctf.range
    def _rescale_value(x, old, new):
        nx = (x - old[0])/(old[1] - old[0])
        return new[0] + nx*(new[1] - new[0])
    if new_range[0] != old_range[0] and new_range[1] != old_range[1]:
        s_d = save_ctfs(volume_property)
        # Set the new range making sure that they are in the right order.
        s1, s2 = new_range
        if s1 > s2:
            s_d['range'] = (s2, s1)
        else:
            s_d['range'] = (s1, s2)
        # Rescale the RGB values.
        rgb = s_d['rgb']
        for v in rgb:
            v[0] = _rescale_value(v[0], old_range, new_range)
        # Rescale the alpha values.
        alpha = s_d['alpha']
        for v in alpha:
            v[0] = _rescale_value(v[0], old_range, new_range)
        # Now load the rescaled values.
        ctf, otf = load_ctfs(s_d, volume_property)
    return ctf, otf

def set_lut(lut, volume_property):
    """Given a `tvtk.LookupTable` and a `tvtk.VolumeProperty` it saves
    the state of the RGB and opacity CTF from the volume property to
    the LUT.  The number of colors to use is obtained from the LUT and
    not the CTF.
    """
    vp = volume_property
    ctf = vp.rgb_transfer_function
    otf = vp.get_scalar_opacity()
    s1, s2 = ctf.range
    nc = lut.number_of_colors
    ds = float(s2-s1)/(nc - 1)
    for i in range(nc):
        r, g, b = ctf.get_color(s1 + i*ds)
        a = otf.get_value(s1 + i*ds)
        lut.set_table_value(i, r, g, b, a)

def set_ctf_from_lut(lut, volume_property):
    """Given a `tvtk.LookupTable` and a `tvtk.VolumeProperty` it loads
    the state of the RGB and opacity CTF from the lookup table to the
    CTF.  The CTF range is obtained from the volume property and the
    number of colors to use is obtained from the LUT.
    """
    vp = volume_property
    ctf = vp.rgb_transfer_function
    s1, s2 = ctf.range
    nc = lut.number_of_colors
    ds = float(s2-s1)/(nc - 1)
    ctf = ColorTransferFunction()
    otf = PiecewiseFunction()
    for i in range(nc):
        v = s1 + i*ds
        r, g, b, a = lut.get_table_value(i)
        ctf.add_rgb_point(v, r, g, b)
        otf.add_point(v, a)
    volume_property.set_color(ctf)
    volume_property.set_scalar_opacity(otf)


##########################################################################
# `ColorTransferFunction` class.
##########################################################################
class ColorTransferFunction(tvtk.ColorTransferFunction):
    """Overrides a few important methods that allow us to glean node
    information.  This is useful in cases where the super class does
    not have methods to get the nodes.
    """

    # Stores the nodes used by the CTF.  Note that this is not a
    # proper trait and modifying this will not change the underlying
    # VTK object.
    nodes = List

    def add_rgb_point(self, *args):
        """V.add_rgb_point(float, float, float, float) -> int
        V.add_rgb_point(float, float, float, float, float, float) -> int

        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error.

        Wrapper around parent class functionality to store node
        information.

        """
        ret = super(ColorTransferFunction, self).add_rgb_point(*args)
        self.nodes.append(args[0])
        self.nodes.sort()
        return ret

    def add_hsv_point(self, *args):
        """V.add_hsv_point(float, float, float, float) -> int
        V.add_hsv_point(float, float, float, float, float, float) -> int

        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error.

        Wrapper around parent class functionality to store node
        information.

        """
        ret = super(ColorTransferFunction, self).add_hsv_point(*args)
        self.nodes.append(args[0])
        self.nodes.sort()
        return ret

    def remove_all_points(self):
        """Remove all the points.
        """
        super(ColorTransferFunction, self).remove_all_points()
        self.nodes = []


##########################################################################
# `PiecewiseFunction` class.
##########################################################################
class PiecewiseFunction(tvtk.PiecewiseFunction):
    """Overrides a few important methods that allow us to glean node
    information.  This is useful in cases where the super class does
    not have methods to get the nodes.
    """

    # Stores the nodes used by the function.  Note that this is not a
    # proper trait and modifying this will not change the underlying
    # VTK object.
    nodes = List

    def initialize(self):
        """V.initialize()

        Clears out the current function. A newly created
        PiecewiseFunction is alreay initialized, so there is no need
        to call this method which in turn simply calls
        remove_all_points()
        """
        super(PiecewiseFunction, self).initialize()
        self.nodes = []

    def add_point(self, x, val):
        """V.add_point(float, float) -> int
        V.add_point(float, float, float, float) -> int

        Add/Remove points to/from the function. If a duplicate point
        is added then the function value is changed at that location.
        Return the index of the point (0 based), or -1 on error.
        """
        ret = super(PiecewiseFunction, self).add_point(x, val)
        self.nodes.append(x)
        self.nodes.sort()
        return ret

    def remove_point(self, x):
        """V.remove_point(float) -> int

        Add/Remove points to/from the function. If a duplicate point
        is added then the function value is changed at that location.
        Return the index of the point (0 based), or -1 on error.
        """
        ret = super(PiecewiseFunction, self).remove_point(x)
        self.nodes.remove(x)
        self.nodes.sort()
        return ret

    def remove_all_points(self):
        """Remove all the points.
        """
        super(PiecewiseFunction, self).remove_all_points()
        self.nodes = []
