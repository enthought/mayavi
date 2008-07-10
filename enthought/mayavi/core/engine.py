"""The Mayavi engine.  This class manages the Mayavi objects at the
highest level.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
# VTK is used to just shut off the warnings temporarily.
import vtk
from os.path import splitext

# Enthought library imports.
from enthought.traits.api import (HasStrictTraits, List, Str, 
        Property, Instance, Event, HasTraits, Callable, Dict,
        Bool, on_trait_change)
from enthought.traits.ui.api import View, Item
from enthought.persistence import state_pickler

# Mayavi imports
from enthought.mayavi.tools.figure_manager import figure_manager

# Local imports.
from enthought.mayavi.core.base import Base
from enthought.mayavi.core.scene import Scene
from enthought.mayavi.core.common import error
from enthought.mayavi.core.registry import registry
from enthought.mayavi.core.adder_node import AdderNode, SceneAdderNode


######################################################################
# Utility functions.
######################################################################
def _scene_id_generator():
    """Returns a sequence of numbers for the title of the scene
    window."""
    n = 1
    while True:
        yield(n)
        n += 1
scene_id_generator = _scene_id_generator()
        

######################################################################
# `Engine` class
######################################################################
class Engine(HasStrictTraits):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The scenes associated with this project.
    scenes = List(Scene)

    # The list to provide to a TreeEditor.  Always add on a AdderNode.
    # TODO: It makes more sense to put the modification of the list 
    #       in some other UI module, and not here.
    children_ui_list = Property

    # Our name.
    name = Str('Mayavi Engine')

    # Current scene.
    current_scene = Property(Instance(Scene))

    # Current object.
    current_object = Property

    # Current selection -- the currently selected object on the tree.
    current_selection = Property

    # Has the Engine started?  Use this event to do something after
    # the engine has been started.
    started = Event

    # An optional callable that will generate a usable new viewer
    # containing a `enthought.tvtk.pyface.TVTKScene` instance. Ideally
    # the viewer should have an interface like
    # `enthought.tvtk.pyface.TVTKWindow` -- basically it must
    # implement the `closing` and `activated` events, however, this is
    # not necessary.  The created viewer is used by the `new_scene`
    # method to create a new Viewer.  This is a mechanism to use a
    # user specified scene with the Engine and have the ability to
    # load saved visualizations using the new scene.  Handy for things
    # like off-screen rendering.
    scene_factory = Callable
   
    # Are we running?
    running = Bool(False)

    ########################################
    # Private traits.
    
    _current_scene = Instance(Scene)
    _current_object = Instance(HasTraits)
    _current_selection = Instance(HasTraits)
    _viewer_ref = Dict

    # View related traits.
    current_selection_view = View(Item(name='_current_selection',
                                       enabled_when='_current_selection is not None',
                                       style='custom', springy=True,
                                       show_label=False,),
                                  resizable=True,
                                  scrollable=True
                                  )
    
    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        super(Engine, self).__init__(**traits)

    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for x in ['_current_scene', '_current_object',
                  '__sync_trait__', '_viewer_ref',
                  '__traits_listener__']:
            d.pop(x, None)
        return d    

    def __set_pure_state__(self, state):
        # Current number of scenes.
        n_scene = len(self.scenes)
        # Number of scenes in saved state.
        n_saved_scene = len(state.scenes)
        # Remove extra ones.
        for i in range(n_scene - n_saved_scene):
            self.close_scene(self.scenes[-1])
        # Add new ones.
        for i in range(n_saved_scene - n_scene):
            self.new_scene()
        # Set the state.
        state_pickler.set_state(self, state)

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        self.__init__()
        state = state_pickler.loads_state(str_state)
        state_pickler.update_state(state)
        self.__set_pure_state__(state)        

    ######################################################################
    # `Engine` interface
    ######################################################################
    def start(self):
        """This is called by the plugin when the plugin actually
        starts."""
        # Notify any listeners that the engine is started.
        self.started = self
        self.running = True
        figure_manager.engines.append(self)

    def stop(self):
        self.running = False
        for index, engine in enumerate(figure_manager.engines):
            if engine == self:
                figure_manager.engines.pop(index)
                break

    def add_source(self, src, scene=None):
        """Adds a source to the pipeline. Uses the current scene unless a
        scene is given in the scene keyword argument."""
        if scene is not None:
            tvtk_scene = scene.scene
            for sc in self.scenes:
                if sc.scene == tvtk_scene:
                    scene = sc
                    break
            else:
                error('This scene is not managed by mayavi')
                return
        else:
            scene = self.current_scene

        # Create a new scene if none is available.
        if scene is None:
            self.new_scene()
            scene = self.current_scene
        scene.add_child(src)
        self.current_object = src

    def add_filter(self, fil, obj=None):
        """Adds a filter to the pipeline at an appropriate point. Adds it 
        to the selected object, or to an object passed as the 
        kwarg `obj`.
        """
        if obj == None:
            obj = self.current_object
        if not isinstance(obj, Base):
            msg = 'No valid current object, '\
                  'please select an active object.'
            error(msg)
            return
        if (obj is not None) and (not isinstance(obj, Scene)):
            if obj.running:
                obj.add_child(fil)
                self.current_object = fil
            else:
                msg = 'Current object is not active, '\
                      'please select an active object.'
                error(msg)
        else:
            if obj is None:
                error('Please create a VTK scene and open some data first.')
            else:
                error('No data: cannot use a Filter/Module/ModuleManager.')

    def add_module(self, mod, obj=None):
        """Adds a module to the pipeline at an appropriate point. Adds it 
        to the selected object, or to an object passed through the 
        kwarg `obj`.
        """
        self.add_filter(mod, obj=obj)

    def save_visualization(self, file_or_fname):
        """Given a file or a file name, this saves the current
        visualization to the file.
        """
        # Save the state of VTK's global warning display.
        o = vtk.vtkObject
        w = o.GetGlobalWarningDisplay()
        o.SetGlobalWarningDisplay(0) # Turn it off.
        try:
            state_pickler.dump(self, file_or_fname)
        finally:
            # Reset the warning state.
            o.SetGlobalWarningDisplay(w)

    def load_visualization(self, file_or_fname):
        """Given a file/file name this loads the visualization."""
        # Save the state of VTK's global warning display.
        o = vtk.vtkObject
        w = o.GetGlobalWarningDisplay()
        o.SetGlobalWarningDisplay(0) # Turn it off.
        try:
            # Get the state from the file.
            state = state_pickler.load_state(file_or_fname)
            state_pickler.update_state(state)
            # Add the new scenes.
            for scene_state in state.scenes:
                self.new_scene()
                scene = self.scenes[-1]
                # Disable rendering initially.
                scene.scene.disable_render = True
                # Update the state.
                state_pickler.update_state(scene_state)
                scene.__set_pure_state__(scene_state)
                # Setting the state will automatically reset the
                # disable_render.                                
                scene.render()
        finally:
            # Reset the warning state.
            o.SetGlobalWarningDisplay(w)

    def open(self, filename):
        """Open a file given a filename if possible.
        """
        base, ext = splitext(filename)
        readers = registry.get_file_reader(ext)
        if len(readers) == 0:
            msg = 'No readers found for the extension %s'%ext
            error(msg)
        else:
            src = None
            cs = self.current_scene
            if cs is None:
                cs = self.new_scene()
            try:
                cs.scene.busy = True
                reader = readers[-1]
                callable = reader.get_callable()
                if reader.factory is None:
                    src = callable()
                    src.initialize(filename)
                else:
                    # Factory functions are passed the filename and a
                    # reference to the engine. 
                    src = callable(filename, self)
                if src is not None:
                    self.add_source(src)
            finally:
                cs.scene.busy = False
            if src is not None:
                return src

    ######################################################################
    # Scene creation/deletion related methods.
    ######################################################################
    def add_scene(self, scene, name=None):
        """Add given `scene` (a `pyface.tvtk.scene.Scene` instance) to
        the mayavi engine so that mayavi can manage the scene.  This
        is used when the user creates a scene.  Note that for the
        `EnvisageEngine` this is automatically taken care of when you
        create a new scene using the TVTK scene plugin.

        Parameters:
        -----------

         scene - `pyface.tvtk.scene.Scene`

          The scene that needs to be managed from mayavi.

         name - `str` 
          The name assigned to the scene.  It tries to determine the
          name of the scene from the passed scene instance.  If this
          is not possible it defaults to 'TVTK Scene'.
          
        """
        if name is None:
            if hasattr(scene, 'name'):
                name = scene.name
            else:
                name = 'TVTK Scene %d'%scene_id_generator.next()
        
        s = Scene(scene=scene, name=name)
        s.start()
        self.scenes.append(s)
        self.current_scene = s

    
    def remove_scene(self, scene):
        """Remove a given `scene` (a `pyface.tvtk.scene.Scene`
        instance) from the mayavi engine if it is already being
        managed by mayavi.  Note that for the `EnvisageEngine` this is
        automatically taken care of when you close a scene started
        using the TVTK scene plugin.

        Parameters:
        -----------

         scene - `pyface.tvtk.scene.Scene`

          The scene that needs to be removed from mayavi.
        """
        s = None
        for x in self.scenes:
            if x.scene is scene:
                s = x
                break
        if s is not None:
            s.stop()
            self.scenes.remove(s)
        # Remove the reference to the viewer if any.
        if scene in self._viewer_ref:
            del self._viewer_ref[scene]
        
    def new_scene(self, viewer=None):
        """Create or manage a new VTK scene window.  If no `viewer`
        argument is provided, the method creates a new viewer using
        `self.scene_factory`.  If `self.scene_factor` is `None` then
        it creates an `ivtk` viewer.  This code requires that the
        `viewer` has a `scene` attribute/trait that is a
        `pyface.tvtk.scene.Scene`.  It also works best if the viewer
        supports `closing` and `activated` events.

        The method returns the created viewer.
        """
        if viewer is None:
            if self.scene_factory is None:
                from enthought.tvtk.tools.ivtk import IVTK
                viewer = IVTK(size=(400, 350))
                if True:
                    # FIXME: Need preferences here
                    viewer.menu_bar_manager = None
                viewer.open()
            else:
                viewer = self.scene_factory()
            
        # Hang on to a reference to this viewer, if not done this will cause a
        # crash with Qt4.  This because the viewer will be closed and gc'd if
        # there isn't a reference to it.  When the viewer is gc'd the scene is
        # also closed and the engine will have a dead scene causing a crash.
        self._viewer_ref[viewer.scene] = viewer

        self.add_scene(viewer.scene)
        if hasattr(viewer, 'on_trait_change'):
            viewer.on_trait_change(self._on_scene_closed, 'closing')
            viewer.on_trait_change(self._on_scene_activated, 'activated')
            if hasattr(viewer, 'title'):
                self.current_scene.sync_trait('name', viewer, 'title')
        return viewer

    def close_scene(self, scene):
        """Given a scene created from new_scene, this method closes it
        and removes the scene from the list of scenes we manage.

        Parameters:
        -----------

         scene - `pyface.tvtk.scene.Scene`
        """
        self.remove_scene(scene.scene)
        if hasattr(scene, 'close'):
            scene.close()
        else:
            scene.scene.close()


    def dialog_view(self):
        """ Default dialog view for Engine objects.
        """
        return None

    ######################################################################
    # Non-public interface
    ######################################################################
    def _on_select(self, object):
        """Called by the EngineTree when an object on the view is
        selected.  This basically sets the current object and current
        scene."""
        self.current_selection = object
        self._current_object = object
        try:
            scene = object.scene
            for s in self.scenes:
                if s.scene == scene:
                    self._current_scene = s
                    break
        except AttributeError:
            pass
            
    def _get_current_scene(self):
        n_scene = len(self.scenes)
        if n_scene == 0:
            return None
        elif n_scene == 1:
            return self.scenes[0]
        elif self._current_scene is not None:
            return self._current_scene
        elif n_scene > 1:
            return self.scenes[-1]
        else:
            return None

    def _set_current_scene(self, scene):
        old = self._current_scene
        self._current_scene = scene
        self.trait_property_changed('current_scene', old, scene)

    def _get_current_object(self):
        if self._current_object is not None:
            return self._current_object
        elif self.current_scene is not None:
            return self.current_scene
        else:
            return None

    def _set_current_object(self, object):
        old = self._current_object
        self._current_object = object
        self.trait_property_changed('current_object', old, object)

    def _get_current_selection(self):
        return self._current_selection

    def _set_current_selection(self, object):
        old = self._current_selection
        if not isinstance(object, (Base, AdderNode)):
            object = None
        self._current_selection = object
        self.trait_property_changed('current_selection', old, object)

    def _on_scene_closed(self, obj, name, old, new):
        self.remove_scene(obj.scene)

    def _on_scene_activated(self, obj, name, old, new):
        for scene in self.scenes:
            if scene.scene is obj.scene:
                self.current_scene = scene
                break

    def _get_children_ui_list(self):
        """ Trait getter for children_ui_list Property.
        """
        node = SceneAdderNode(label='Add a new scene', object=self)
        return [node] + self.scenes

    @on_trait_change('scenes[]')
    def _trigger_children_ui_list(self, old, new):
        """ Trigger a children_ui_list change when scenes changed.
        """
        self.trait_property_changed('children_ui_list', old, new)

    
