#!/usr/bin/env python
"""A simple example demonstrating the creation of actors and animating
the in a scene using visual modeule."""
# Author: Raashid Baig <raashid@aero.iitb.ac.in>
# License: BSD Style.

from tvtk.tools.visual import box, sphere, vector, iterate, show

def main():
    # Creating parameters for box size
    side = 4.0
    thk = 0.3
    s2 = 2*side - thk
    s3 = 2*side + thk
    # Creating the 6 walls
    wallR = box( pos = (side, 0, 0), size = (thk, s3, s2), color = (1, 0, 0))
    wallL = box( pos = (-side, 0, 0), size = (thk, s3, s2), color = (1, 0, 0))
    wallB = box( pos = (0, -side, 0), size = (s3, thk, s3), color = (0, 0, 1))
    wallT = box( pos = (0, side, 0), size = (s3, thk, s3), color = (0, 0, 1))
    wallBK = box( pos = (0, 0, -side), size = (s2, s2, thk), color = (0.7,0.7,0.7))
    # Creating the ball
    ball = sphere(radius = 0.4, color = (0, 1, 0))
    ball.vector = vector(-0.15, -0.23, 0.27)

    side = side -thk*0.5 - ball.radius

    ball.t = 0.0
    ball.dt = 0.5

    def anim():
        #Creating the animation function which will be called at
        #uniform timeperiod through the iterate function
        ball.t = ball.t + ball.dt
        ball.pos = ball.pos + ball.vector*ball.dt
        if not (side > ball.x > -side):
            ball.vector.x = -ball.vector.x
        if not (side > ball.y > -side):
            ball.vector.y = -ball.vector.y
        if not (side > ball.z > -side):
            ball.vector.z =  -ball.vector.z

    a = iterate(20, anim)
    show()
    return a

if __name__ == '__main__':
    main()
