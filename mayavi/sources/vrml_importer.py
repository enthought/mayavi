"""An importer for VRML files.

"""
# Author: Prabhu Ramachandran <prabhu at aero dot iitb dot ac dot in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought imports.
from tvtk.api import tvtk
from traits.api import Instance, Str
from traitsui.api import View, Item, FileEditor
from apptools.persistence.file_path import FilePath
from apptools.persistence.state_pickler import set_state

# Local imports
from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo

######################################################################
# `VRMLImporter` class.
######################################################################
class VRMLImporter(Source):

    __version__ = 0

    # The file name.
    file_name = Str('', enter_set=True, auto_set=False,
                    desc='the VRML file name')

    # The VRML importer.
    reader = Instance(tvtk.VRMLImporter, args=(), allow_none=False,
                      record=True)

    output_info = PipelineInfo(datasets=['none'])

    ###############
    # Private traits.

    # Our file path used for persistence
    _file_path = Instance(FilePath, args=())

    # Our View.
    view = View(Item(name='file_name', editor=FileEditor()))

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(VRMLImporter, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('reader', 'file_name'):
            d.pop(name)
        return d

    def __set_pure_state__(self, state):
        # The reader has its own file_name which needs to be fixed.
        fname = state._file_path.abs_pth
        # Now call the parent class to setup everything.
        self.initialize(fname)
        # Setup the rest of the state.
        set_state(self, state, ignore=['_file_path'])

    def initialize(self, file_name):
        self.file_name = file_name

    ######################################################################
    # `PipelineBase` interface.
    ######################################################################
    def add_actors(self):
        """Adds `self.actors` to the scene.
        """
        if not self._actors_added:
            self.reader.render_window = self.scene.render_window
            self._update_reader()
            self._actors_added = True
            if not self.visible:
                self._visible_changed(self.visible)
            self.scene.render()

    def remove_actors(self):
        """Removes `self.actors` from the scene.
        """
        if self._actors_added:
            self.scene.remove_actors(self.actors)
            self._actors_added = False
            self.scene.render()

    def has_output_port(self):
        """ Return True as the reader has output port."""
        return True

    def get_output_object(self):
        """ Return the reader output port."""
        return self.reader.output_port

    ######################################################################
    # Non-public interface
    ######################################################################
    def _file_name_changed(self, value):
        reader = self.reader
        reader.file_name = value
        self._file_path.set(value)
        self._update_reader()
        self.render()
        name = "VRML file (%s)"%basename(self.file_name)
        if '[Hidden]' in self.name:
            name += ' [Hidden]'
        self.name = name

    def _update_reader(self):
        reader = self.reader
        if self.scene is None or reader.file_name is None \
               or len(reader.file_name) == 0:
            return
        actors1 = [x for x in self.scene.renderer.actors]
        reader.read()
        self.scene.render()
        actors2 = [x for x in self.scene.renderer.actors]
        self.actors = [x for x in actors2 if x not in actors1]
        # If these are the first actors on scene reset the view.
        if len(actors1) == 0:
            self.scene.reset_zoom()

    def _scene_changed(self, old, new):
        if self._actors_added:
            old.remove_actors(self.actors)
            reader = self.reader
            reader.render_window = new.render_window
            self._update_reader()

    def _actors_changed(self, old, new):
        if self._actors_added:
            self.scene.remove_actors(old)
            # The actors are added automatically when the importer
            # does a read.
            self.scene.render()

    def _actors_items_changed(self, list_event):
        if self._actors_added:
            self.scene.remove_actors(list_event.removed)
            # The actors are added automatically when the importer
            # does a read.
            self.scene.render()

    def _visible_changed(self, value):
        if value:
            if not self._actors_added:
                self.scene.add_actors(self.actors)
                self._actors_added = True
        super(VRMLImporter, self)._visible_changed(value)

