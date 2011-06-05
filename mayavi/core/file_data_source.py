"""The base file related data source object from which all MayaVi data
sources derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import re
from os.path import split, join, isfile
from glob import glob

# Enthought library imports.
from traits.api import List, Str, Instance, Int, Range
from traitsui.api import Group, Item, FileEditor
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

    files.sort(file_sort)
    return files


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

    base_file_name=Str('', desc="the base name of the file",
                       enter_set=True, auto_set=False,
                       editor=FileEditor())

    # A timestep view group that may be included by subclasses.
    time_step_group = Group(Item(name='file_path', style='readonly'),
                            Item(name='timestep',
                                 defined_when='len(object.file_list) > 1')
                            )

    ##################################################
    # Private traits.
    ##################################################

    # The current file name.  This is not meant to be touched by the
    # user.
    file_path = Instance(FilePath, (), desc='the current file name')

    _min_timestep = Int(0)
    _max_timestep = Int(0)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(FileDataSource, self).__get_pure_state__()
        # These are obtained dynamically, so don't pickle them.
        for x in ['file_list', 'timestep']:
            d.pop(x, None)
        return d

    def __set_pure_state__(self, state):
        # Use the saved path to initialize the file_list and timestep.
        fname = state.file_path.abs_pth
        if not isfile(fname):
            msg = 'Could not find file at %s\n'%fname
            msg += 'Please move the file there and try again.'
            raise IOError, msg

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
        timestep = min(self.timestep, n_files)
        self._max_timestep = max(n_files -1, 0)
        if self.timestep == timestep:
            self._timestep_changed(timestep)
        else:
            self.timestep = timestep

    def _file_list_items_changed(self, list_event):
        self._file_list_changed(self.file_list)

    def _timestep_changed(self, value):
        file_list = self.file_list
        if len(file_list) > 0:
            self.file_path = FilePath(file_list[value])
        else:
            self.file_path = FilePath('')

    def _base_file_name_changed(self,value):
        self.file_list = get_file_list(value)
        if len(self.file_list) == 0:
            self.file_list = [value]
        try:
            self.timestep = self.file_list.index(value)
        except ValueError:
            self.timestep = 0

