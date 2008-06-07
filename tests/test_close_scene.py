#!/usr/bin/env mayavi2
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

"""This tests that closing a hidden TVTK scene window does not crash or
raise PyDeadObjectErrors.  The test also shows how it is easy to create
mayavi tests in a manner similar to mayavi example scripts using the
@test decorator.
"""

from common import test

@test
def test_close_scene():
    engine = mayavi.engine
    s1 = mayavi.new_scene()
    s2 = mayavi.new_scene()
    # This should not crash or throw any errors (PyDeadObjects etc.)
    engine.close_scene(s1)
    # Neither should this.
    engine.close_scene(s2)

if __name__ == "__main__":
    test_close_scene()

