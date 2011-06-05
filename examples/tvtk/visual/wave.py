#!/usr/bin/env python

# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

from math import sin, pi

from numpy import zeros, float, arange

from tvtk.tools.visual import show, Curve, iterate, MVector


def main():
    dt = 0.1

    x = arange(-50,50)
    wpoints1 = zeros((100,3), float)
    wpoints2 = zeros((100,3), float)
    wpoints3 = zeros((100,3), float)
    wpoints4 = zeros((100,3), float)

    for i in range (0,100,1):
        wpoints1[i] = [x[i], -30, 0]
        wpoints2[i] = [x[i], -15, 0]
        wpoints3[i] = [x[i], 0, 0]
        wpoints4[i] = [x[i], 15, 0]

    band1 = Curve(points = wpoints1, k = 6.0, color = (1,0,0),
                  mass = 2.0, radius = 0.5, momentum = zeros((100, 3), float))

    band2 = Curve(points = wpoints2, k = 6.0, color = (1,1,0),
                  mass = 2.0, radius = 0.5, momentum = zeros((100, 3), float))

    band3 = Curve(points = wpoints3, k = 6.0, color = (0,1,0),
                  mass = 2.0, radius = 0.5, momentum = zeros((100, 3), float))

    band4 = Curve(points = wpoints4, k = 6.0, color = (0,0,1),
                  mass = 2.0, radius = 0.5, momentum = zeros((100, 3), float))

    for i in range(0,25,1):
        band1.momentum[i,1] = sin(x[i]*pi/25.0)*3   # half-wave pulse

    for i in range(0,25,1):
        band2.momentum[i,1] = sin(x[i]*2*pi/25.0)*5   # full-wave pulse

    for i in range(0,25,1):
        band3.momentum[i,0] = sin(x[i]*pi/25.0)*5   # compresion pulse

    for i in range(0,100,1):
        band4.momentum[i,1] = sin(x[i]*4*pi/100.0)*2   # standing wave

    def anim():
        band1.momentum[0] = band1.momentum[-1] = MVector(0,0,0)
        band2.momentum[0] = band2.momentum[-1] = MVector(0,0,0)
        band3.momentum[0] = band3.momentum[-1] = MVector(0,0,0)
        band4.momentum[0] = band4.momentum[-1] = MVector(0,0,0)

        band1.points = band1.points + (band1.momentum/band1.mass*dt)
        band2.points = band2.points + (band2.momentum/band2.mass*dt)
        band3.points = band3.points + (band3.momentum/band3.mass*dt)
        band4.points = band4.points + (band4.momentum/band4.mass*dt)

        force1 = band1.k * (band1.points[1:] - band1.points[:-1])
        force2 = band2.k * (band2.points[1:] - band2.points[:-1])
        force3 = band3.k * (band3.points[1:] - band3.points[:-1])
        force4 = band4.k * (band4.points[1:] - band4.points[:-1])

        band1.momentum[:-1] = band1.momentum[:-1] + force1 * dt
        band2.momentum[:-1] = band2.momentum[:-1] + force2 * dt
        band3.momentum[:-1] = band3.momentum[:-1] + force3 * dt
        band4.momentum[:-1] = band4.momentum[:-1] + force4 * dt

        band1.momentum[1:] = band1.momentum[1:] - force1 * dt
        band2.momentum[1:] = band2.momentum[1:] - force2 * dt
        band3.momentum[1:] = band3.momentum[1:] - force3 * dt
        band4.momentum[1:] = band4.momentum[1:] - force4 * dt

    a = iterate(20, anim)
    show()
    return a

if __name__ == '__main__':
    main()
