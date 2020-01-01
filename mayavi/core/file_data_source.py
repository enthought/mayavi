"""The base file related data source object from which all MayaVi data
sources derive.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import re
from os.path import split, join, isfile
from glob import glob

# Enthought library imports.
from traits.api import (Any, Bool, Button, Float, List, Str, Instance, Int,
                        Range)
from traitsui.api import Group, HGroup, Item, FileEditor, RangeEditor
from apptools.persistence.state_pickler import set_state
from apptools.persistence.file_path import FilePath

# Local imports
from mayavi.core.source import Source
from mayavi.core.common import handle_children_state


######################################################################
# Utility functions.
######################################################################
def get_file_list(file_name):
    """ Given a file name, this function treats the file as a part of
    a series of files based on the index of the file and tries to
    determine the list of files in the series.  The file name of a
    file in a time series must be of the form 'some_name[0-9]*.ext'.
    That is the integers at the end of the file determine what part of
    the time series the file belongs to.  The files are then sorted as
    per this index."""

    # The matching is done only for the basename of the file.
    f_dir, f_base = split(file_name)
    # Find the head and tail of the file pattern.
    head = re.sub("[0-9]+[^0-9]*$", "", f_base)
    tail = re.sub("^.*[0-9]+", "", f_base)
    pattern = head+"[0-9]*"+tail
    # Glob the files for the pattern.
    _files = glob(join(f_dir, pattern))

    # A simple function to get the index from the file.
    def _get_index(f, head=head, tail=tail):
        base = split(f)[1]
        result = base.replace(head, '')
        return float(result.replace(tail, ''))

    # Before sorting make sure the files in the globbed series are
    # really part of a timeseries.  This can happen in cases like so:
    # 5_2_1.vtk and 5_2_1s.vtk will be globbed but 5_2_1s.vtk is
    # obviously not a valid time series file.
    files = []
    for x in _files:
        try:
            _get_index(x)
        except ValueError:
            pass
        else:
            files.append(x)

    # Sort the globbed files based on the index value.
    def file_sort(x, y):
        x1 = _get_index(x)
        y1 = _get_index(y)
        if x1 > y1:
            return 1
        elif y1 > x1:
            return -1
        else:
            return 0

    files.sort(key=lambda x:_get_index(x))
    return files


class NoUITimer(object):
    """Dummy timer for case where there is no UI.  This implements the
    pyface.timer.Timer API with the only exception that it does not call Start
    when constructed and start must be called explicitly.

    """

    def __init__(self, millisecs, callable, *args, **kw):
        self.callable = callable
        self.args = args
        self.kw = kw
        self._is_active = False

    def Notify(self):
        try:
            self.callable(*self.args, **self.kw)
        except StopIteration:
            self.Stop()
        except:
            self.Stop()
            raise

    def Start(self):
        self._is_active = True
        while self._is_active:
            self.Notify()

    def Stop(self):
        self._is_active = False

    def IsRunning(self):
        return self._is_active


######################################################################
# `FileDataSource` class.
######################################################################
class FileDataSource(Source):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The list of file names for the timeseries.
    file_list = List(Str, desc='a list of files belonging to a time series')

    # The current time step (starts with 0).  This trait is a dummy
    # and is dynamically changed when the `file_list` trait changes.
    # This is done so the timestep bounds are linked to the number of
    # the files in the file list.
    timestep = Range(value=0,
                     low='_min_timestep',
                     high='_max_timestep',
                     enter_set=True, auto_set=False,
                     desc='the current time step')

    sync_timestep = Bool(False, desc='if all dataset timesteps are synced')

    play = Bool(False, desc='if timesteps are automatically updated')
    play_delay = Float(0.2, desc='the delay between loading files')
    loop = Bool(False, desc='if animation is looped')

    update_files = Button('Rescan files')

    base_file_name=Str('', desc="the base name of the file",
                       enter_set=True, auto_set=False,
                       editor=FileEditor())

    # A timestep view group that may be included by subclasses.
    time_step_group = Group(
                          Item(name='file_path', style='readonly'),
                          Group(
                              Item(name='timestep',
                                   editor=RangeEditor(
                                       low=0, high_name='_max_timestep',
                                       mode='slider'
                                   ),
                              ),
                              Item(name='sync_timestep'),
                              HGroup(
                                  Item(name='play'),
                                  Item(name='play_delay',
                                       label='Delay'),
                                  Item(name='loop'),
                              ),
                              visible_when='len(object.file_list) > 1'
                          ),
                          Item(name='update_files', show_label=False),
                      )

    ##################################################
    # Private traits.
    ##################################################

    # The current file name.  This is not meant to be touched by the
    # user.
    file_path = Instance(FilePath, (), desc='the current file name')

    _min_timestep = Int(0)
    _max_timestep = Int(0)
    _timer = Any
    _in_update_files = Any(False)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(FileDataSource, self).__get_pure_state__()
        # These are obtained dynamically, so don't pickle them.
        for x in ['file_list', 'timestep', 'play']:
            d.pop(x, None)
        return d

    def __set_pure_state__(self, state):
        # Use the saved path to initialize the file_list and timestep.
        fname = state.file_path.abs_pth
        if not isfile(fname):
            msg = 'Could not find file at %s\n'%fname
            msg += 'Please move the file there and try again.'
            raise IOError(msg)

        self.initialize(fname)
        # Now set the remaining state without touching the children.
        set_state(self, state, ignore=['children', 'file_path'])
        # Setup the children.
        handle_children_state(self.children, state.children)
        # Setup the children's state.
        set_state(self, state, first=['children'], ignore=['*'])

    ######################################################################
    # `FileDataSource` interface
    ######################################################################
    def initialize(self, base_file_name):
        """Given a single filename which may or may not be part of a
        time series, this initializes the list of files.  This method
        need not be called to initialize the data.
        """
        self.base_file_name = base_file_name

    ######################################################################
    # Non-public interface
    ######################################################################
    def _file_list_changed(self, value):
        # Change the range of the timestep suitably to reflect new list.
        n_files = len(self.file_list)
        timestep = max(min(self.timestep, n_files-1), 0)
        if self.timestep == timestep:
            self._timestep_changed(timestep)
        else:
            self.timestep = timestep
        self._max_timestep = max(n_files -1, 0)

    def _file_list_items_changed(self, list_event):
        self._file_list_changed(self.file_list)

    def _timestep_changed(self, value):
        file_list = self.file_list
        if len(file_list) > 0:
            self.file_path = FilePath(file_list[value])
        else:
            self.file_path = FilePath('')
        if self.sync_timestep:
            for sibling in self._find_sibling_datasets():
                sibling.timestep = value

    def _base_file_name_changed(self, value):
        self._update_files_fired()
        try:
            self.timestep = self.file_list.index(value)
        except ValueError:
            self.timestep = 0

    def _play_changed(self, value):
        mm = getattr(self.scene, 'movie_maker', None)
        if value:
            if mm is not None:
                mm.animation_start()
            self._timer = self._make_play_timer()
            if not self._timer.IsRunning():
                self._timer.Start()
        else:
            self._timer.Stop()
            self._timer = None
            if mm is not None:
                mm.animation_stop()

    def _loop_changed(self, value):
        if value and self.play:
            self._play_changed(self.play)

    def _play_event(self):
        mm = getattr(self.scene, 'movie_maker', None)
        nf = self._max_timestep
        pc = self.timestep
        pc += 1
        if pc > nf:
            if self.loop:
                pc = 0
            else:
                self._timer.Stop()
                pc = nf
                if mm is not None:
                    mm.animation_stop()
        if pc != self.timestep:
            self.timestep = pc
            if mm is not None:
                mm.animation_step()

    def _play_delay_changed(self):
        if self.play:
            self._timer.Stop()
            self._timer.Start(self.play_delay*1000)

    def _make_play_timer(self):
        scene = self.scene
        if scene is None or scene.off_screen_rendering:
            timer = NoUITimer(self.play_delay*1000, self._play_event)
        else:
            from pyface.timer.api import Timer
            timer = Timer(self.play_delay*1000, self._play_event)
        return timer

    def _find_sibling_datasets(self):
        if self.parent is not None:
            nt = self._max_timestep
            return [x for x in self.parent.children if x._max_timestep == nt]
        else:
            return []

    def _update_files_fired(self):
        # First get all the siblings before we change the current file list.
        if self._in_update_files:
            return
        try:
            self._in_update_files = True
            if self.sync_timestep:
                siblings = self._find_sibling_datasets()
            else:
                siblings = []
            fname = self.base_file_name
            file_list = get_file_list(fname)
            if len(file_list) == 0:
                file_list = [fname]
            self.file_list = file_list
            for sibling in siblings:
                sibling.update_files = True
        finally:
            self._in_update_files = False
