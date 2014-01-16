"""Test for the mlab.show function/decorator."""

from mayavi import mlab
from pyface.api import GUI

from test_mlab import run_mlab_examples

def close():
    """Close the scene."""
    f = mlab.gcf()
    e = mlab.get_engine()
    v = e.get_viewer(f)
    v.close()

def test_mlab_show():
    """Test mlab.show()"""
    run_mlab_examples()
    # Automatically close window in 100 msecs.
    GUI.invoke_after(100, close)
    mlab.show()

def test_show_decorator():
    """Test the @mlab.show decorator"""
    @mlab.show
    def f():
        run_mlab_examples()
        # Automatically close window in 100 msecs.
        GUI.invoke_after(100, close)
    f()

if __name__ == '__main__':
    test_mlab_show()
    test_show_decorator()
