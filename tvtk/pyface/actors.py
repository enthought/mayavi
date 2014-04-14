#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
"""Helper functions to make a bunch of simple actors.  This is useful
when writing demo/example code.

"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

from tvtk.api import tvtk
from vtk.util import colors
from tvtk.common import configure_input_data

def axes_actor(origin=(0, 0, 0), scale_factor=1.0, radius=0.02,
               sides=12):
    """Creates a simple axes actor and returns a tvtk.Actor object."""
    axes = tvtk.Axes(origin=origin, scale_factor=scale_factor, symmetric=1)
    tube = tvtk.TubeFilter(radius=radius, number_of_sides=sides,
                           vary_radius='vary_radius_off')
    configure_input_data(tube, axes.output)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, tube.output)
    actor = tvtk.Actor(mapper=mapper)
    axes.update()
    return actor


def cone_actor(center=(0, 0, 0), height=1.0, radius=0.5,
               direction=(1, 0, 0), resolution=100, color=colors.red,
               opacity=1.0):
    """ Sets up a cone actor and returns the tvtk.Actor object."""
    source = tvtk.ConeSource(center=center, height=height,
                             radius=radius, direction=direction,
                             resolution=resolution)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    p = tvtk.Property(opacity=opacity, color=color)
    actor = tvtk.Actor(mapper=mapper, property=p)
    source.update()
    return actor


def cube_actor(center=(0, 0, 0), color=colors.blue, opacity=1.0):
    """ Creates a cube and returns the tvtk.Actor. """

    source = tvtk.CubeSource(center=center)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    p = tvtk.Property(opacity=opacity, color=color)
    actor = tvtk.Actor(mapper=mapper, property=p)
    source.update()
    return actor


def cylinder_actor(center=(0, 0, 0), radius=0.5, resolution=64,
                   color=colors.green, opacity=1.0):
    """ Creates a cylinder and returns a tvtk.Actor. """
    source = tvtk.CylinderSource(center=center, radius=radius,
                                 resolution=resolution)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    prop = tvtk.Property(opacity=opacity, color=color)
    actor = tvtk.Actor(mapper=mapper, property=prop)
    source.update()
    return actor


def earth_actor(radius=0.5, opacity=1.0):
    """ Creates an earth source and returns the actor. """
    source = tvtk.EarthSource(radius=radius, on_ratio=16, outline=0)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    prop = tvtk.Property(opacity=opacity)
    actor = tvtk.Actor(mapper=mapper, property=prop)
    source.update()
    return actor


def sphere_actor(center=(0, 0, 0), radius=0.5, resolution=32,
                 color=colors.purple, opacity=1.0):
    """ Creates a sphere and returns the actor. """
    source = tvtk.SphereSource(center=center, radius=radius,
                               theta_resolution=resolution,
                               phi_resolution=resolution)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    prop = tvtk.Property(opacity=opacity, color=color)
    actor = tvtk.Actor(mapper=mapper, property=prop)
    source.update()
    return actor


def arrow_actor(color=colors.peacock, opacity=1.0, resolution=24):
    """ Creates a 3D Arrow and returns an actor. """
    source = tvtk.ArrowSource(tip_resolution=resolution,
                              shaft_resolution=resolution)
    mapper = tvtk.PolyDataMapper()
    configure_input_data(mapper, source.output)
    prop = tvtk.Property(opacity=opacity, color=color)
    actor = tvtk.Actor(mapper=mapper, property=prop)
    source.update()
    return actor

