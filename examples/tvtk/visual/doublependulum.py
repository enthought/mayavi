#!/usr/bin/env python

"""A simple example demonstrating the creation of actors and animating
the in a scene using visual modeule."""

# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

# Double pendulum

#The analysis is in terms of Lagrangian mechanics. The Lagrangian
#variables are angle of upper bar, angle of lower bar,measured from
#the vertical.

from tvtk.tools.visual import box, vector, frame, iterate, show
from math import pi, sin

g = 9.8
M1 = 2.0
M2 = 1.0
d = 0.05 # thickness of each bar
gap = 2.*d # distance between two parts of upper, U-shaped assembly
L1 = 0.5 # physical length of upper assembly; distance between axles
L1display = L1+d # show upper assembly a bit longer than physical, to overlap axle
L2 = 1.0 # physical length of lower bar
L2display = L2+d/2. # show lower bar a bit longer than physical, to overlap axle
# Coefficients used in Lagrangian calculation
A = (1./4.)*M1*L1**2+(1./12.)*M1*L1**2+M2*L1**2
B = (1./2.)*M2*L1*L2
C = g*L1*(M1/2.+M2)
D = M2*L1*L2/2.
E = (1./12.)*M2*L2**2+(1./4.)*M2*L2**2
F = g*L2*M2/2.

hpedestal = 1.3*(L1+L2) # height of pedestal
wpedestal = 0.1 # width of pedestal
tbase = 0.05 # thickness of base
wbase = 8.*gap # width of base
offset = 2.*gap # from center of pedestal to center of U-shaped upper assembly
top = vector(0,0,0) # top of inner bar of U-shaped upper assembly

theta1 = 1.3*pi/2. # initial upper angle (from vertical)
theta1dot = 0 # initial rate of change of theta1
theta2 = 0 # initial lower angle (from vertical)
theta2dot = 0 # initial rate of change of theta2

pedestal = box(pos = (top - vector(0, hpedestal/2.0, offset)),size = (wpedestal, 1.1*hpedestal, wpedestal), color = (0.4,0.4,0.5))

base = box(pos = (top - vector(0,hpedestal + tbase/2.0, offset)),size=(wbase, tbase, wbase),color = (0.4,0.4,0.5))

bar1 = box(pos=(L1display/2.0 - d/2.0, 0, -(gap+d)/2.0), size=(L1display, d, d), color=(1,0,0))
bar1b = box(pos=(L1display/2.0 - d/2.0, 0, (gap+d)/2.0), size=(L1display, d, d), color=(1,0,0))

frame1 = frame(bar1, bar1b)
frame1.pos = (0.0, 0.0, 0.0)
frame1.axis = (0.0, -1.0, 0.0)
frame1.rotate(axis=(0,0,1), angle = 180.0*theta1/pi)

bar2 = box(pos = (L2display/2.0 - d/2.0, 0, 0), size = (L2display, d, d), color = (0,1,0))

frame2 = frame(bar2)
frame2.pos = (0.0, -1.0*L1, 0.0)
frame2.axis = (0.0, -1.0, 0.0)
frame2.rotate(axis = (0,0,1), angle = 180.0*theta2/pi)

dt = 0.001

def anim():
    global theta1, theta2, theta1dot, theta2dot
    atheta1 = ((E*C/B)*sin(theta1)-F*sin(theta2))/(D-E*A/B)
    atheta2 = -(A*atheta1+C*sin(theta1))/B

    theta1dot = theta1dot + atheta1*dt
    theta2dot = theta2dot + atheta2*dt

    dtheta1 = theta1dot*dt
    dtheta2 = theta2dot*dt
    theta1 = theta1 + dtheta1
    theta2 = theta2 + dtheta2

    frame1.rotate(axis = (0,0,1), angle = 180.0*dtheta1/pi)

    frame2.pos = top + frame1.axis*L1
    frame2.rotate(axis = (0,0,1), angle = 180*dtheta2/pi)

a = iterate(20, anim)
a.edit_traits()
show()
