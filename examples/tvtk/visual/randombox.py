#!/usr/bin/env python

# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

from random import random, randrange
from numpy import arange
from math import pi, cos, sin

from tvtk.tools.visual import curve, box, arrow, \
                                        sphere, cylinder, show

def random_box():
    xx = randrange(-55,54)
    yy = randrange(-55,54)
    zz = randrange(-55,54)
    x = randrange(0,21)
    y = randrange(0,21)
    z = randrange(0,21)
    red = random()
    green = random()
    blue = random()
    box (pos = (xx,yy,zz), length=x, height=y, width=z,
         color=(red,green,blue))

def wirecube(s):
    c = curve(color = (1,1,1), radius=1)
    pts = [(-s, -s, -s),(-s, -s, s), (-s, s, s),
           (-s, s, -s), (-s, -s, -s), (s, -s, -s),
           (s, s, -s), (-s, s, -s), (s, s, -s),
           (s, s, s), (-s, s, s), (s, s, s),
           (s, -s, s), (-s, -s, s), (s, -s, s),(s, -s, -s)]
    for pt in pts:
        c.append(pt)

side = 150.0
cube = box(size = (side,side,side), representation = 'w' )
i = 0
while i < 100:
    random_box()
    i = i + 1

arrow(axis=(0,12,0), radius_shaft=3.5, color = (1,0,0))

ball = sphere(pos=(-side/2.,-side/2.,-side/2.),color=(1,1,0),radius=3)
disk = cylinder(pos=(side/2.,side/2.,-side/2.),color=(.3,.3,1),axis=(1,1,0),radius=5)
xx = arange(0,4*pi,pi/10.)
spring=curve(color=(1,.7,.1), radius=0.4)
for y in xx:
    spring.append([20+cos(2*y), y/2.-30, -20+sin(2*y)+30])

show()
