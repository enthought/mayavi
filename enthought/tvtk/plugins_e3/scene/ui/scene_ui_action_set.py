""" The default action set for the scene UI plugin. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.envisage.ui.action.api import Action, ActionSet, Group, Menu


# The base package.
ID = 'enthought.tvtk.plugins_e3.scene.ui'


#### Menus ####################################################################

new_menu = Menu(
    name='&New', path='MenuBar/File', group='additions'
)

save_scene_as_menu = Menu(
    name="Sa&ve Scene As", path='MenuBar/File', group='additions', after='New'
)

#### Actions ##################################################################

new_scene = Action(
    class_name = ID + '.actions.NewScene',
    path       = 'MenuBar/File/New',
    group      = 'additions'
)

#### Save actions ####

save_scene = Action(
    class_name = ID + '.actions.SaveScene',
    path       = 'MenuBar/File',
    group      = 'additions',
    #after      = 'Save Scene As'
)

save_scene_to_png = Action(
    class_name = ID + '.actions.SaveSceneToPNG',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_jpeg = Action(
    class_name = ID + '.actions.SaveSceneToJPEG',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_bmp = Action(
    class_name = ID + '.actions.SaveSceneToBMP',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_tiff = Action(
    class_name = ID + '.actions.SaveSceneToTIFF',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_ps = Action(
    class_name = ID + '.actions.SaveSceneToPS',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_gl2ps = Action(
    class_name = ID + '.actions.SaveSceneToGL2PS',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_rib = Action(
    class_name = ID + '.actions.SaveSceneToRIB',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_oogl = Action(
    class_name = ID + '.actions.SaveSceneToOOGL',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_iv = Action(
    class_name = ID + '.actions.SaveSceneToIV',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_vrml = Action(
    class_name = ID + '.actions.SaveSceneToVRML',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

save_scene_to_obj = Action(
    class_name = ID + '.actions.SaveSceneToOBJ',
    path       = 'MenuBar/File/SaveSceneAs',
    group      = 'additions'
)

#### View actions ####

reset_zoom = Action(
    class_name = ID + '.actions.ResetZoom',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

isometric_view = Action(
    class_name = ID + '.actions.IsometricView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

x_plus_view = Action(
    class_name = ID + '.actions.XPlusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

x_minus_view = Action(
    class_name = ID + '.actions.XMinusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

y_plus_view = Action(
    class_name = ID + '.actions.YPlusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

y_minus_view = Action(
    class_name = ID + '.actions.YMinusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

z_plus_view = Action(
    class_name = ID + '.actions.ZPlusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)

z_minus_view = Action(
    class_name = ID + '.actions.ZMinusView',
    path       = 'MenuBar/ViewMenu',
    group      = 'additions'
)


class SceneUIActionSet(ActionSet):
    """ The default action set for the scene UI plugin. """

    id      = ID + '.action_set',
    name    = 'SceneActionSet',
    menus   = [new_menu, save_scene_as_menu]
    actions = [
        new_scene,

        # Save actions.
        save_scene, save_scene_to_png, save_scene_to_jpeg, save_scene_to_bmp,
        save_scene_to_tiff, save_scene_to_ps, save_scene_to_gl2ps,
        save_scene_to_rib, save_scene_to_oogl, save_scene_to_iv,
        save_scene_to_vrml, save_scene_to_obj,

        # Scene actions.
        reset_zoom, isometric_view, x_plus_view, x_minus_view, y_plus_view,
        y_minus_view, z_plus_view, z_minus_view
    ]

#### EOF ######################################################################
