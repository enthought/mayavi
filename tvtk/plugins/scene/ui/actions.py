""" The various actions for the Scene plugin. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from pyface.api import FileDialog, OK
from pyface.tasks.action.api import TaskAction
from traits.api import Instance, Property, Str

from pyface.tasks.api import Task

from mayavi.plugins.mayavi_tasks_application import MayaviTasksApplication


class BetterLazyTaskAction(TaskAction):

    """ A TaskAction that resolves the task lazily given its ID.
    The task for the dock pane is resolved lazily from an application. This
    allows, for example, to contribute an action in a plugin that refers to
    a task from another plugin, even if the task has not been created yet.
    """

    task = Property(depends_on='application')
    _task = Instance(Task)

    #### 'TaskAction' protocol ################################################
    def _get_task(self):
        if self.application.windows:
            task = self.application.get_task(self.task_id)
            return task
        

    def _set_task(self, task):
        old = None
        if self._task:
            old = self._task
        if old != task:
            self.trait_property_changed("task", old, task)
    
    #### 'LazyTaskAction' protocol ############################################

    task_id = Str("mayavi.task")

    application = Instance(MayaviTasksApplication)


class LazyTaskAction(TaskAction):
    """ A TaskAction that resolves the task lazily given its ID.
    The task for the dock pane is resolved lazily from an application. This
    allows, for example, to contribute an action in a plugin that refers to
    a task from another plugin, even if the task has not been created yet.
    """

    #### 'TaskAction' protocol ################################################
    def _task_default(self):
        task = self.application.get_task(self.task_id)
        return task

    #### 'LazyTaskAction' protocol ############################################

    task_id = Str("mayavi.task")

    application = Instance(MayaviTasksApplication)


class SceneAction(BetterLazyTaskAction):
    """ Base class for actions that require a scene manager. """

    #### 'SceneAction' interface ##############################################

    # The scene manager.
    scene_manager = Property(Instance(
        'tvtk.plugins.scene.i_scene_manager import ISceneManager'
    ))

    def _get_scene_manager(self):
        """ Trait property getter. """

        return self.task.scene_manager


class NewScene(BetterLazyTaskAction):
    """ An action that creates a new TVTK scene. """

    #### 'Action' interface ###################################################

    name = 'Scene'

    def perform(self, event):
        """ Performs the action. """
        print('EVENT: ', event)
        from tvtk.plugins.scene.scene_editor import SceneEditor
        editor = self.task.window.central_pane.edit(object(), factory=SceneEditor)

        return editor


class SaveScene(SceneAction):
    """ An action that saves a scene to an image. """

    #### 'Action' interface ###################################################

    name = 'Save Scene'

    def perform(self, event):
        """ Performs the action. """

        extensions = [
            '*.png', '*.jpg', '*.jpeg', '*.tiff', '*.bmp', '*.ps', '*.eps',
            '*.tex', '*.rib', '*.wrl', '*.oogl', '*.pdf', '*.vrml', '*.obj',
            '*.iv', '*.pov', '*x3d'
        ]

        descriptions = [
            'PNG', 'JPG', 'JPEG', 'TIFF', 'Bitmap', 'PostScript', 'EPS',
            'TeX', 'RIB', 'WRL', 'Geomview', 'PDF', 'VRML', 'Wavefront',
	    'Povray', 'X3D'
        ]

        wildcard = ''

        for description, extension in zip(descriptions, extensions):
            wildcard += '{} ({})|{}|'.format(description, extension, extension)
        
        wildcard += 'Determine by extension (*.*)|(*.*)'

        dialog = FileDialog(
            parent   = self.task.window.control,
            title    = 'Save scene to image',
            action   = 'save as',
            wildcard = wildcard
        )
        if dialog.open() == OK:
            scene = self.scene_manager.current_scene
            if scene is not None:
                scene.save(dialog.path)

        return


class SaveSceneToImage(SceneAction):
    """ An action that saves a scene to an image. """

    #### 'Action' interface ###################################################

    # Name of the action.
    name = 'Image'

    #### 'SaveSceneToImage' interface #########################################

    # The save method name.
    save_method = Str('save')

    # The wildcard for the file dialog.
    wildcard = Str("All files (*.*)|*.*")

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Perform the action. """

        dialog = FileDialog(
            parent   = self.task.window.control,
            title    = 'Save scene to %s' % self.name,
            action   = 'save as',
            wildcard = self.wildcard
        )
        if dialog.open() == OK:
            scene = self.scene_manager.current_scene
            if scene is not None:
                method = getattr(scene, self.save_method)
                method(dialog.path)

        return


# These are all specific subclasses that save particular images.
class SaveSceneToPNG(SaveSceneToImage):
    name        = 'PNG Image'
    save_method = 'save_png'
    wildcard    = 'PNG images (*.png)|*.png|' \
                  'All files (*.*)|*.*'

class SaveSceneToJPEG(SaveSceneToImage):
    name        = 'JPEG Image'
    save_method = 'save_jpg'
    wildcard    = 'JPEG images (*.jpg)|*.jpg|' \
                  'JPEG images (*.jpeg)|*.jpeg|' \
                  'All files (*.*)|*.*'

class SaveSceneToBMP(SaveSceneToImage):
    name        = 'BMP Image'
    save_method = 'save_bmp'
    wildcard    = 'BMP images (*.bmp)|*.bmp|' \
                  'All files (*.*)|*.*'

class SaveSceneToTIFF(SaveSceneToImage):
    name        = 'TIFF Image'
    save_method = 'save_tiff'
    wildcard    = 'TIFF images (*.tif)|*.tif|' \
                  'TIFF images (*.tiff)|*.tiff|' \
                  'All files (*.*)|*.*'

class SaveSceneToPS(SaveSceneToImage):
    name        = 'PostScript bitmap Image'
    save_method = 'save_ps'
    wildcard    = 'PostScript bitmap images (*.ps)|*.ps|' \
                  'All files (*.*)|*.*'

class SaveSceneToGL2PS(SaveSceneToImage):
    name        = 'Vector PS/EPS/PDF/TeX'
    save_method = 'save_gl2ps'
    wildcard    = 'All files (*.*)|*.*|' \
                  'EPS files (*.eps)|*.eps|' \
                  'PS files (*.ps)|*.ps|' \
                  'PDF files (*.pdf)|*.pdf|' \
                  'TeX files (*.tex)|*.tex'

class SaveSceneToRIB(SaveSceneToImage):
    name        = 'RenderMan RIB file'
    save_method = 'save_rib'
    wildcard    = 'RIB files (*.rib)|*.rib|' \
                  'All files (*.*)|*.*'

class SaveSceneToOOGL(SaveSceneToImage):
    name        = 'GeomView OOGL file'
    save_method = 'save_oogl'
    wildcard    = 'OOGL files (*.oogl)|*.oogl|' \
                  'All files (*.*)|*.*'

class SaveSceneToIV(SaveSceneToImage):
    name        = 'OpenInventor file'
    save_method = 'save_iv'
    wildcard    = 'OpenInventor files (*.iv)|*.iv|' \
                  'All files (*.*)|*.*'

class SaveSceneToVRML(SaveSceneToImage):
    name        = 'VRML file'
    save_method = 'save_vrml'
    wildcard    = 'VRML files (*.wrl)|*.wrl|' \
                  'All files (*.*)|*.*'

class SaveSceneToOBJ(SaveSceneToImage):
    name        = 'Wavefront OBJ file'
    save_method = 'save_wavefront'
    wildcard    = 'OBJ files (*.obj)|*.obj|' \
                  'All files (*.*)|*.*'

class SaveSceneToPovray(SaveSceneToImage):
    name	= 'Povray File'
    save_method = 'save_povray'
    wildcard	= 'Povray (*.pov)|*.pov|' \
    		  'All files (*.*)|*.*'

class SaveSceneToX3D(SaveSceneToImage):
    name	= 'X3D File'
    save_method	= 'save_x3d'
    wildcard	= 'X3D (*.x3d)|*.pov|' \
		  'All files (*.*)|*.*'

class SetView(SceneAction):
    """ An action that sets the current scene to a particular view."""

    #### 'SetView' interface ##################################################

    # The method to invoke on the scene that will set the view.
    view_method = Str

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Perform the action. """

        scene = self.scene_manager.current_scene
        if scene is not None:
            method = getattr(scene, self.view_method)
            method()

        return

# These are all specific subclasses that invoke particular views.
class ResetZoom(SetView):
    name = '&Reset Zoom'
    view_method = 'reset_zoom'

class IsometricView(SetView):
    name = '&Isometric View'
    view_method = 'isometric_view'

class XPlusView(SetView):
    name = '&X+ View'
    view_method = 'x_plus_view'

class XMinusView(SetView):
    name = '&X- View'
    view_method = 'x_minus_view'

class YPlusView(SetView):
    name = '&Y+ View'
    view_method = 'y_plus_view'

class YMinusView(SetView):
    name = '&Y- View'
    view_method = 'y_minus_view'

class ZPlusView(SetView):
    name = '&Z+ View'
    view_method = 'z_plus_view'

class ZMinusView(SetView):
    name = '&Z- View'
    view_method = 'z_minus_view'

#### EOF ######################################################################
