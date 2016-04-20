from __future__ import print_function

import os
from mayavi import mlab
from pyface.api import GUI

def close():
    """Close the scene."""
    f = mlab.gcf()
    e = mlab.get_engine()
    e.window.workbench.prompt_on_exit = False
    e.window.close()
    mlab.options.backend = 'auto'
    # Hack: on Linux the splash screen does not go away so we force it.
    GUI.invoke_after(500, e.window.workbench.application.gui.stop_event_loop)

def test_mlab_envisage():
    "Test if mlab runs correctly when the backend is set to 'envisage'."
    @mlab.show
    def f():
        from mayavi.preferences.api import preference_manager
        preference_manager.root.show_splash_screen = False
        mlab.options.backend = 'envisage'
        mlab.test_contour3d()
        GUI.invoke_after(3000, close)

    f()

if __name__ == '__main__':
    from traits.etsconfig.api import ETSConfig

    if os.environ.get("TRAVIS", False) and ETSConfig.toolkit == "qt4":
        print("Virtual buffer on Travis leads to seg fault with Qt as "
              "has_focus, active_view are undefined.  Skip.")
    else:
        test_mlab_envisage()
