#!/usr/bin/env python

# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

# Gyroscope hanging from a spring
from math import atan, cos, sin, pi

from tvtk.tools.visual import vector, MVector, Box, Helix, Frame, \
    Cylinder, curve, color, iterate, show


top = vector(0,1.,0) # where top of spring is held
ks = 100. # spring stiffness
Lspring = 1. # unstretched length of spring
Rspring = 0.03 # radius of spring
Dspring = 0.03 # thickness of spring wire
Lshaft = 1. # length of gyroscope shaft
Rshaft = 0.03 # radius of gyroscope shaft
M = 1. # mass of gyroscope (massless shaft)
Rrotor = 0.4 # radius of gyroscope rotor
Drotor = 0.1 # thickness of gyroscope rotor
Dsquare = 1.4*Drotor # thickness of square that turns with rotor
I = 0.5*M*Rrotor**2. # moment of inertia of gyroscope
omega = 40.0 # angular velocity of rotor along axis
g = 9.8
Fgrav = MVector(0,-M*g,0)
precession = M*g*(Lshaft/2.)/(I*abs(omega)) # exact precession angular velocity
phi = atan(precession**2*(Lshaft/2.)/g) # approximate angle of spring to vertical
s = M*g/(ks*cos(phi)) # approximate stretch of spring
# Refine estimate of angle of spring to vertical:
phi = 1./(((I*abs(omega))/(M*Lshaft/2.))**2/(g*Lshaft/2.)-(Lspring+s)/(Lshaft/2.))
# Refine again:
s = M*g/(ks*cos(phi))
phi = 1./( ((I*abs(omega))/(M*Lshaft/2.))**2/(g*Lshaft/2.)-(Lspring+s)/(Lshaft/2.) )
# Momentum required for completely smooth precession:
pprecess = vector(0,0,M*precession*(Lshaft/2.+(Lspring+s)*sin(phi)))
if omega < 0:
    pprecess = -pprecess

support = Box(pos = top+MVector(0,0.01,0), size = (0.2,0.02,0.2), color = (0,1,0))
spring = Helix(pos = top, axis = vector(-0.161579, -0.98686, 0), radius = Rspring, color = (1,0.7,0.2))

gyro1 = Frame(pos = top+spring.axis) # gyro.pos at end of spring
gyro1.axis = MVector(1,0,0)

shaft = Cylinder(pos = gyro1.pos, axis = Lshaft*gyro1.axis, radius =
                 Rshaft, color = (0.85,0.85,0.85), length = 1.0)

rotor = Cylinder(pos = 0.5*gyro1.axis*(Lshaft-Drotor), axis =
                 gyro1.axis*Drotor, radius = Rrotor, color = (0.5,0.5,0.5), length = 0.1)

stripe1 = curve(color = color.green,
                points = [rotor.pos+1.03*rotor.axis+vector(0,Rrotor,0),
                rotor.pos+1.03*rotor.axis-vector(0,Rrotor,0)])
stripe2 = curve(color = color.green,
                points = [rotor.pos-0.03*rotor.axis+vector(0,Rrotor,0),
                rotor.pos-0.03*rotor.axis-vector(0,Rrotor,0)])

gyro = Frame(stripe1, stripe2) # gyro.pos at end of spring
gyro.pos = top+spring.axis # gyro.pos at end of spring
gyro.axis = vector(1,0,0)

gyro.rotate(axis=(0,1,0), angle = 180.0, origin = gyro.pos)

cm = gyro.pos+0.5*Lshaft*gyro.axis # center of mass of shaft
Lrot = I*omega*gyro.axis
p = pprecess
dt = 0.01
t = 0.

c = 0

def anim():
    global Lrot, p, cm, t
    Fspring = -ks*vector.norm(spring.axis)*(vector.mag(spring.axis)-Lspring)
    # Calculate torque about center of mass:
    torque = vector.cross(-0.5*Lshaft*gyro.axis,Fspring)
    Lrot = Lrot+torque*dt
    p = p+(Fgrav+Fspring)*dt
    cm = cm+(p/M)*dt

    # Update positions of shaft, rotor, spring, stripes
    if omega > 0:
        gyro.axis = vector.norm(Lrot)
    else:
        gyro.axis = -vector.norm(Lrot)

    gyro.pos = cm-0.5*Lshaft*gyro.axis # shaft rotated, adjust connection to spring
    spring.axis = gyro.pos - top
    spring.length = vector.mag(spring.axis)
    gyro.rotate(180*omega*dt/(4.0*pi), gyro.axis, gyro.pos) # spin easier to see if slower than actual omega
    shaft.pos = gyro.pos
    shaft.axis = Lshaft*gyro.axis
    rotor.pos = gyro.pos + 0.5*gyro.axis*(Lshaft-Drotor)
    rotor.axis = gyro.axis*Drotor

    t = t+dt

a = iterate(40, anim)
a.edit_traits()
show()
