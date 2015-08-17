""" A TVTK scene editor. """

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from apptools.preferences.api import get_default_preferences
from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.pyface.api import DecoratedScene
from pyface.workbench.api import Editor
from traits.api import Instance


#### Handy functions ##########################################################

def _id_generator():
    """ Return an ever-increasing number useful for creating unique Ids. """

    n = 1
    while True:
        yield(n)
        n += 1

_id_generator = _id_generator()


class SceneEditor(Editor):
    """ A TVTK scene editor. """

    #### 'SceneEditor' interface ##############################################

    # The TVTK scene object.
    scene = Instance(TVTKScene)

    ###########################################################################
    # 'IWorkbenchPart' interface.
    ###########################################################################

    #### Trait initializers ###################################################

    def _id_default(self):
        """ Trait initializer. """

        return self.name

    def _name_default(self):
        """ Trait initializer. """

        return 'TVTK Scene %d' % (next(_id_generator))

    #### Methods ##############################################################

    def create_control(self, parent):
        """ Create the toolkit-specific control that represents the editor. """

        # We hold a reference to the scene itself to make sure it does not get
        # garbage collected (because we only return the scene's 'control' not
        # the scene itself). The scene is also referenced by the scene manager.
        self.scene = self._create_decorated_scene(parent)
        self.scene.render()

        return self.scene.control

    def destroy_control(self):
        """ Destroy the toolkit-specific control that represents the
        editor.
        """
        if self.scene is not None:
            # Close the scene to cleanly shut it down.
            self.scene.close()

        # Call the parent method.
        return super(SceneEditor, self).destroy_control()

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _create_decorated_scene(self, parent):
        """ Create a new decorated scene. """

        pref = get_default_preferences()
        stereo = eval(pref.get('tvtk.scene.stereo'))

        scene = DecoratedScene(parent, stereo=stereo)

        # Set the scene's traits to preference values.
        scene.magnification = \
                eval(pref.get('tvtk.scene.magnification'))

        fg = eval(pref.get('tvtk.scene.foreground_color'))
        bg = eval(pref.get('tvtk.scene.background_color'))
        scene.foreground = fg
        scene.background = bg
        # FIXME: This seems necessary for some strange reason, if not
        # the actual background of the renderer never gets set even
        # though the renderer and the scene's background are synced.
        scene.renderer.background = scene.background

        return scene

#### EOF ######################################################################
