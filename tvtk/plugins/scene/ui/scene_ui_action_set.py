""" The default action set for the scene UI plugin. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from envisage.ui.action.api import Action, ActionSet, Group, Menu


# This package
PKG = '.'.join(__name__.split('.')[:-1])


#### Groups ###################################################################

scene_group = Group(
    id='TVTKSceneGroup',
    path='MenuBar/File', before='ExitGroup'
)

view_group = Group(
    id='TVTKViewGroup',
    path='MenuBar/Tools', before='PreferencesGroup'
)

#### Menus ####################################################################

new_menu = Menu(
    name='&New',
    path='MenuBar/File', group='TVTKSceneGroup'
)

save_scene_as_menu = Menu(
    id='SaveSceneAs', name="Sa&ve Scene As",
    path='MenuBar/File', group='TVTKSceneGroup', after='New'
)

#### Actions ##################################################################

new_scene = Action(
    class_name = PKG + '.actions.NewScene',
    path       = 'MenuBar/File/New', group='additions'
)

#### Save actions ####

save_scene = Action(
    class_name = PKG + '.actions.SaveScene',
    path       = 'MenuBar/File', group='TVTKSceneGroup', after='SaveSceneAs'
)

save_scene_to_png = Action(
    class_name = PKG + '.actions.SaveSceneToPNG',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_jpeg = Action(
    class_name = PKG + '.actions.SaveSceneToJPEG',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_bmp = Action(
    class_name = PKG + '.actions.SaveSceneToBMP',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_tiff = Action(
    class_name = PKG + '.actions.SaveSceneToTIFF',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_ps = Action(
    class_name = PKG + '.actions.SaveSceneToPS',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_gl2ps = Action(
    class_name = PKG + '.actions.SaveSceneToGL2PS',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_rib = Action(
    class_name = PKG + '.actions.SaveSceneToRIB',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_oogl = Action(
    class_name = PKG + '.actions.SaveSceneToOOGL',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_iv = Action(
    class_name = PKG + '.actions.SaveSceneToIV',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_vrml = Action(
    class_name = PKG + '.actions.SaveSceneToVRML',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_obj = Action(
    class_name = PKG + '.actions.SaveSceneToOBJ',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_pov = Action(
    class_name = PKG + '.actions.SaveSceneToPovray',
    path       = 'MenuBar/File/SaveSceneAs'
)

save_scene_to_x3d = Action(
    class_name = PKG + '.actions.SaveSceneToX3D',
    path       = 'MenuBar/File/SaveSceneAs'
)

#### View actions ####

reset_zoom = Action(
    class_name = PKG + '.actions.ResetZoom',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

isometric_view = Action(
    class_name = PKG + '.actions.IsometricView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

x_plus_view = Action(
    class_name = PKG + '.actions.XPlusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

x_minus_view = Action(
    class_name = PKG + '.actions.XMinusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

y_plus_view = Action(
    class_name = PKG + '.actions.YPlusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

y_minus_view = Action(
    class_name = PKG + '.actions.YMinusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

z_plus_view = Action(
    class_name = PKG + '.actions.ZPlusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)

z_minus_view = Action(
    class_name = PKG + '.actions.ZMinusView',
    path       = 'MenuBar/Tools', group='TVTKViewGroup'
)


class SceneUIActionSet(ActionSet):
    """ The default action set for the scene UI plugin. """

    groups  = [scene_group, view_group]
    menus   = [new_menu, save_scene_as_menu]
    actions = [
        new_scene,

        # Save actions.
        save_scene, save_scene_to_png, save_scene_to_jpeg, save_scene_to_bmp,
        save_scene_to_tiff, save_scene_to_ps, save_scene_to_gl2ps,
        save_scene_to_rib, save_scene_to_oogl, save_scene_to_iv,
        save_scene_to_vrml, save_scene_to_obj, save_scene_to_pov,
        save_scene_to_x3d,

        # Scene actions.
        reset_zoom, isometric_view, x_plus_view, x_minus_view, y_plus_view,
        y_minus_view, z_plus_view, z_minus_view
    ]

#### EOF ######################################################################
