""" The default action set for the scene UI plugin. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.envisage.ui.action.api import Action, ActionSet, Group, Menu


# The base package.
PKG = 'enthought.tvtk.plugins_e3.scene.ui'


#### Menus ####################################################################

new_menu = Menu(
    name='&New', path='MenuBar/File', group='additions'
)

save_scene_as_menu = Menu(
    name="Sa&ve Scene As", path='MenuBar/File', group='additions', after='New'
)

#### Actions ##################################################################

new_scene = Action(
    class_name = PKG + '.actions.NewScene',
    path       = 'MenuBar/File/New',
    group      = 'additions'
)

save_scene = Action(
    class_name = PKG + ".actions.SaveScene",
    path       = 'MenuBar/File',
    group      = 'additions',
    #after      = 'Save Scene As'
)

class SceneUIActionSet(ActionSet):
    """ The default action set for the scene UI plugin. """

    menus   = [new_menu, save_scene_as_menu]

    actions = [
        new_scene, save_scene,
    ]


## save_scene = Action(
##     id            = "SaveScene",
##     class_name    = ID + ".actions.SaveScene",
##     name          = "S&ave Scene",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to an image",
##     description   = "Save rendered scene to an image",
##     locations = [Location(path="MenuBar/FileMenu/additions",
##                           after="SaveSceneAs")]
## )

## save_scene_to_png = Action(
##     id            = "SaveSceneToPNG",
##     class_name    = ID + ".actions.SaveSceneToPNG",
##     name          = "&PNG Image",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to a PNG image",
##     description   = "Save rendered scene to a PNG image",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_jpeg = Action(
##     id            = "SaveSceneToJPEG",
##     class_name    = ID + ".actions.SaveSceneToJPEG",
##     name          = "&JPEG Image",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to a JPEG image",
##     description   = "Save rendered scene to a JPEG image",
##     locations     = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions",
##                               after="SaveSceneToPNG")]
##     )

## save_scene_to_bmp = Action(
##     id            = "SaveSceneToBMP",
##     class_name    = ID + ".actions.SaveSceneToBMP",
##     name          = "&BMP Image",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to a BMP image",
##     description   = "Save rendered scene to a BMP image",
##     locations     = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions",
##                               after="SaveSceneToJPEG")]
## )

## save_scene_to_tiff = Action(
##     id            = "SaveSceneToTIFF",
##     class_name    = ID + ".actions.SaveSceneToTIFF",
##     name          = "&TIFF Image",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to a TIFF image",
##     description   = "Save rendered scene to a TIFF image",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_ps = Action(
##     id            = "SaveSceneToPS",
##     class_name    = ID + ".actions.SaveSceneToPS",
##     name          = "Post&Script bitmap image",
##     image         = "images/save_scene.png",
##     tooltip       = "Save rendered scene to a PostScript bitmap image",
##     description   = "Save rendered scene to a PostScript bitmap image",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_gl2ps = Action(
##     id            = "SaveSceneToGL2PS",
##     class_name    = ID + ".actions.SaveSceneToGL2PS",
##     name          = "V&ector PS/EPS/PDF/TeX (GL2PS)",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to vector PS/EPS/PDF/TeX",
##     description   = "Export rendered scene to vector PS/EPS/PDF/TeX",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_rib = Action(
##     id            = "SaveSceneToRIB",
##     class_name    = ID + ".actions.SaveSceneToRIB",
##     name          = "&RenderMan RIB file",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to a RenderMan RIB file",
##     description   = "Export rendered scene to a RenderMan RIB file",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_oogl = Action(
##     id            = "SaveSceneToOOGL",
##     class_name    = ID + ".actions.SaveSceneToOOGL",
##     name          = "&GeomView OOGL file",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to a GeomView OOGL file",
##     description   = "Export rendered scene to a GeomView OOGL file",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_iv = Action(
##     id            = "SaveSceneToIV",
##     class_name    = ID + ".actions.SaveSceneToIV",
##     name          = "&OpenInventor file",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to an OpenInventor file",
##     description   = "Export rendered scene to an OpenInventor file",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_vrml = Action(
##     id            = "SaveSceneToVRML",
##     class_name    = ID + ".actions.SaveSceneToVRML",
##     name          = "&VRML file",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to a VRML file",
##     description   = "Export rendered scene to a VRML file",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## save_scene_to_obj = Action(
##     id            = "SaveSceneToOBJ",
##     class_name    = ID + ".actions.SaveSceneToOBJ",
##     name          = "&Wavefront OBJ file",
##     image         = "images/save_scene.png",
##     tooltip       = "Export rendered scene to a Wavefront OBJ file",
##     description   = "Export rendered scene to a Wavefront OBJ file",
##     locations = [Location(path="MenuBar/FileMenu/SaveSceneAs/additions")]
## )

## reset_zoom = Action(
##     id            = "ResetZoom",
##     class_name    = ID + ".actions.ResetZoom",
##     name          = "&Reset Zoom",
##     image         = "",
##     tooltip       = "Reset zoom so everything fits in view",
##     description   = "Reset zoom so everything fits in view",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## isometric_view = Action(
##     id            = "IsometricView",
##     class_name    = ID + ".actions.IsometricView",
##     name          = "&Isometric",
##     image         = "",
##     tooltip       = "Set the view to isometric",
##     description   = "Set the view to isometric",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## x_plus_view = Action(
##     id            = "XPlusView",
##     class_name    = ID + ".actions.XPlusView",
##     name          = "&X positive",
##     image         = "",
##     tooltip       = "View scene along the positive X-axis",
##     description   = "View scene along the positive X-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## x_minus_view = Action(
##     id            = "XMinusView",
##     class_name    = ID + ".actions.XMinusView",
##     name          = "X negative",
##     image         = "",
##     tooltip       = "View scene along the negative X-axis",
##     description   = "View scene along the negative X-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## y_plus_view = Action(
##     id            = "YPlusView",
##     class_name    = ID + ".actions.YPlusView",
##     name          = "&Y positive",
##     image         = "",
##     tooltip       = "View scene along the positive Y-axis",
##     description   = "View scene along the positive Y-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## y_minus_view = Action(
##     id            = "YMinusView",
##     class_name    = ID + ".actions.YMinusView",
##     name          = "Y negative",
##     image         = "",
##     tooltip       = "View scene along the negative Y-axis",
##     description   = "View scene along the negative Y-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## z_plus_view = Action(
##     id            = "ZPlusView",
##     class_name    = ID + ".actions.ZPlusView",
##     name          = "&Z positive",
##     image         = "",
##     tooltip       = "View scene along the positive Z-axis",
##     description   = "View scene along the positive Z-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## z_minus_view = Action(
##     id            = "ZMinusView",
##     class_name    = ID + ".actions.ZMinusView",
##     name          = "Z negative",
##     image         = "",
##     tooltip       = "View scene along the negative Z-axis",
##     description   = "View scene along the negative Z-axis",
##     locations = [Location(path="MenuBar/ViewMenu/additions")]
## )

## action_set = WorkbenchActionSet(
##     id = ID + '.action_set',
##     name = 'SceneActionSet',
##     menus = [new_menu, save_scene_as_menu],

##     actions = [
##         new_scene, save_scene, save_scene_to_png, save_scene_to_jpeg,
##         save_scene_to_bmp, save_scene_to_tiff, save_scene_to_ps,
##         save_scene_to_gl2ps, save_scene_to_rib, save_scene_to_oogl,
##         save_scene_to_iv, save_scene_to_vrml, save_scene_to_obj,
##         reset_zoom, isometric_view,
##         x_plus_view, x_minus_view, y_plus_view, y_minus_view,
##         z_plus_view, z_minus_view,
##     ]
## )

#### EOF ######################################################################
