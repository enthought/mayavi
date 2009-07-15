from enthought.mayavi import mlab
from enthought.pyface.api import GUI

def close():
    """Close the scene."""
    f = mlab.gcf()
    e = mlab.get_engine()
    e.window.close()

def test_mlab_envisage():
    """Test if mlab runs correctly when the backend is set to
    'envisage'."""
    @mlab.show
    def f():
        mlab.options.backend = 'envisage'
        mlab.test_contour3d()
        GUI.invoke_after(3000, close)

    f()

if __name__ == '__main__':
    test_mlab_envisage()

