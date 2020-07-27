"""A PLOT3D file reader.  This reader does not support a timeseries of
files.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.


# Standard library imports.
from os.path import basename, isfile, exists, splitext

# Enthought library imports.
from traits.api import Instance, Str, Button
from traitsui.api import View, Group, Item, FileEditor
from tvtk.api import tvtk
from tvtk.tvtk_base import PrefixMap
from apptools.persistence.state_pickler import set_state
from apptools.persistence.file_path import FilePath

# Local imports.
from mayavi.core.source import Source
from mayavi.core.common import handle_children_state, error
from mayavi.core.pipeline_info import PipelineInfo


########################################################################
# `PLOT3DReader` class
########################################################################
class PLOT3DReader(Source):

    """A PLOT3D file reader.  This reader does not support a
    timeseries of files.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # XYZ file name
    xyz_file_name = Str('', desc='the XYZ file')

    # The (optional) Q file.
    q_file_name = Str('', desc='the Q file')

    # The active scalar name.
    scalars_name = PrefixMap({'density': 100,
                              'pressure': 110,
                              'temperature': 120,
                              'enthalpy': 130,
                              'internal energy': 140,
                              'kinetic energy': 144,
                              'velocity magnitude': 153,
                              'stagnation energy': 163,
                              'entropy': 170,
                              'swirl': 184},
                             default_value='density',
                             desc='scalar data attribute to show')
    # The active vector name.
    vectors_name = PrefixMap({'velocity': 200,
                              'vorticity': 201,
                              'momentum': 202,
                              'pressure gradient': 210},
                             default_value='momentum',
                             desc='vector data attribute to show')

    # The VTK data file reader.
    reader = Instance(tvtk.MultiBlockPLOT3DReader, args=(), allow_none=False,
                      record=True)

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['structured_grid'])

    ########################################
    # View related code.

    update_reader = Button('Update Reader')

    # Our view.
    view = View(Group(Item('xyz_file_name', editor=FileEditor()),
                      Item('q_file_name', editor=FileEditor()),
                      Item(name='scalars_name',
                           enabled_when='len(object.q_file_name) > 0'),
                      Item(name='vectors_name',
                           enabled_when='len(object.q_file_name)>0'),
                      Item(name='update_reader'),
                      label='Reader',
                      ),
                Group(Item(name='reader', style='custom',
                           resizable=True),
                      show_labels=False,
                      label='PLOT3DReader'
                      ),
                resizable=True)

    ########################################
    # Private traits.

    # The current file paths.  This is not meant to be touched by the
    # user.
    xyz_file_path = Instance(FilePath, args=(),
                             desc='the current XYZ file path')
    q_file_path = Instance(FilePath, args=(), desc='the current Q file path')

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(PLOT3DReader, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('scalars_name', 'vectors_name', 'xyz_file_name',
                     'q_file_name'):
            d.pop(name, None)

        return d

    def __set_pure_state__(self, state):
        xyz_fn = state.xyz_file_path.abs_pth
        q_fn = state.q_file_path.abs_pth
        if not isfile(xyz_fn):
            msg = 'Could not find file at %s\n' % xyz_fn
            msg += 'Please move the file there and try again.'
            raise IOError(msg)

        # Setup the reader state.
        set_state(self, state, first=['reader'], ignore=['*'])
        # Initialize the files.
        self.initialize(xyz_fn, q_fn, configure=False)
        # Now set the remaining state without touching the children.
        set_state(self, state, ignore=['children', 'xyz_file_path',
                                       'q_file_path'])
        # Setup the children.
        handle_children_state(self.children, state.children)
        # Setup the children's state.
        set_state(self, state, first=['children'], ignore=['*'])

    ######################################################################
    # `FileDataSource` interface
    ######################################################################
    def initialize(self, xyz_file_name, q_file_name='', configure=True):
        """Given an xyz filename and a Q filename which may or may not
        be part of a time series, this initializes the list of files.
        This method need not be called to initialize the data.

        If configure is True, it pops up a UI to configure the
        PLOT3DReader.
        """
        if len(q_file_name) == 0:
            base = splitext(xyz_file_name)[0]
            qf = base + '.q'
            if exists(qf):
                q_file_name = qf

        if configure:
            # First set properties of the reader.  This is useful when
            # the data format has atypical defaults.  Automatic
            # detection can be disastrous sometimes due to VTK related
            # problems.
            self.reader.edit_traits(kind='livemodal')
        self.xyz_file_name = xyz_file_name
        if len(q_file_name) > 0:
            self.q_file_name = q_file_name

    def update(self):
        if len(self.xyz_file_path.get()) == 0:
            return
        self.reader.update()
        self.render()

    def has_output_port(self):
        """ Return True as the reader has output port."""
        return True

    def get_output_object(self):
        """ Return the reader output port."""
        return self.reader.output_port

    ######################################################################
    # Non-public interface
    ######################################################################
    def _xyz_file_name_changed(self, value):
        if len(value) == 0:
            return
        else:
            self.reader.xyz_file_name = value
            self.xyz_file_path.set(value)
            self._update_reader_output()

    def _q_file_name_changed(self, value):
        if len(value) == 0:
            return
        else:
            self.reader.q_file_name = value
            self.q_file_path.set(value)
            self._update_reader_output()

    def _update_reader_output(self):
        r = self.reader
        r.update()

        if r.error_code != 0:
            try:
                self.reader.i_blanking = True
            except AttributeError:
                pass
            else:
                r.update()

        # Try reading file.
        if r.error_code != 0:
            # No output so the file might be an ASCII file.
            try:
                # Turn off IBlanking.
                r.trait_set(i_blanking=False, binary_file=False)
            except AttributeError:
                pass
            else:
                r.update()

        # Try again this time as ascii and with blanking.
        if r.error_code != 0:
            # No output so the file might be an ASCII file.
            try:
                # Turn on IBlanking.
                r.i_blanking = True
            except AttributeError:
                pass
            else:
                r.update()

        # If there still is an error, ask the user.
        if r.error_code != 0:
            r.edit_traits(kind='livemodal')
            r.update()

        # If there still is an error, ask the user to retry.
        if r.error_code != 0:
            msg = 'Unable to read file properly. '\
                  'Please check the settings of the reader '\
                  'on the UI and press the "Update Reader" button '\
                  'when done and try again!'
            error(msg)
            return

        # Now setup the outputs by resetting self.outputs.  Changing
        # the outputs automatically fires a pipeline_changed event.
        self.outputs = [r]

        # Fire data_changed just in case the outputs are not
        # really changed.  This can happen if the dataset is of
        # the same type as before.
        self.data_changed = True

        # Change our name on the tree view
        self.name = self._get_name()

    def _scalars_name_changed(self, value):
        self.reader.scalar_function_number = self.scalars_name_
        self.reader.modified()
        self.update()
        self.data_changed = True

    def _vectors_name_changed(self, value):
        self.reader.vector_function_number = self.vectors_name_
        self.reader.modified()
        self.update()
        self.data_changed = True

    def _update_reader_fired(self):
        self.reader.modified()
        self._update_reader_output()
        self.pipeline_changed = True

    def _get_name(self):
        """ Gets the name to display on the tree view.
        """
        xyz_fname = basename(self.xyz_file_path.get())
        q_fname = basename(self.q_file_path.get())
        if len(self.q_file_name) > 0:
            ret = "PLOT3D:%s, %s" % (xyz_fname, q_fname)
        else:
            ret = "PLOT3D:%s" % (xyz_fname)
        if '[Hidden]' in self.name:
            ret += ' [Hidden]'
        return ret
