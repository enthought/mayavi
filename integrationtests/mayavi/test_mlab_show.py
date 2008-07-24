"""NOTE: This test requires user intervention.  Just close the scene
window after it stops doing anything."""

from inspect import getmembers
from enthought.mayavi import mlab

def do_mlab():
    ############################################################
    # run all the "test_foobar" functions in the mlab module.
    for name, func in getmembers(mlab):
        if not callable(func) or not name[:4] in ('test', 'Test'):
            continue
        mlab.clf()
        func()

def test_mlab_show():
    """Test mlab.show()"""
    do_mlab()
    mlab.show()

def test_show_decorator():
    """Test the @mlab.show decorator"""
    @mlab.show
    def f():
        do_mlab()
    f()

if __name__ == '__main__':
    test_mlab_show()
    test_show_decorator()
