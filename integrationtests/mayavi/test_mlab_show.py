"""Test for the mlab.show function/decorator."""

from inspect import getmembers
from enthought.mayavi import mlab
from enthought.pyface.api import GUI

def do_mlab():
    ############################################################
    # run all the "test_foobar" functions in the mlab module.
    for name, func in getmembers(mlab):
        if not callable(func) or not name[:4] in ('test', 'Test'):
            continue
        mlab.clf()
        func()

def close():
    """Close the scene."""
    f = mlab.gcf()
    e = mlab.get_engine()
    v = e.get_viewer(f)
    v.close()

def test_mlab_show():
    """Test mlab.show()"""
    do_mlab()
    # Automatically close window in 2500 msecs.
    GUI.invoke_after(2500, close)
    mlab.show()

def test_show_decorator():
    """Test the @mlab.show decorator"""
    @mlab.show
    def f():
        do_mlab()
        # Automatically close window in 2500 msecs.
        GUI.invoke_after(2500, close)
    f()

if __name__ == '__main__':
    test_mlab_show()
    test_show_decorator()
