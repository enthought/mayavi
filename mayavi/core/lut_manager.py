"""This manages the lookup table used to map values to colors.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

import os.path
import sys
import subprocess
import warnings

# Enthought library imports.
from traits.api import Instance, Range, Bool, Array, \
     Str, Property, Enum, Button
from traits.etsconfig.api import ETSConfig
from traitsui.api import FileEditor, auto_close_message
from apptools.persistence import state_pickler
from tvtk.api import tvtk

# Local imports.
from mayavi.core.base import Base
from mayavi.core.common import error

from mayavi.core import lut


# The directory that contains the pickled files for colormap
lut_image_dir = os.path.dirname(lut.__file__)
pylab_luts_file = os.path.join(lut_image_dir, 'pylab_luts.pkl')

try:
    pylab_luts = state_pickler.load_state(pylab_luts_file)
except (IOError, ValueError) as exception:
    # IOError: failed to open file
    # ValueError: pickled file is built from an OS w/ different
    #             architecture, or with an incompatible protocol
    message = ("Failed to load pylab colormaps from file:\n"
               "{filepath}\n"
               "Last error: {err_type} {err_message}\n"
               "Some colormaps will not be available. "
               "You may rebuild this file using the script provided "
               "in the mayavi source code: scripts/cm2lut.py")
    warnings.warn(message.format(filepath=pylab_luts_file,
                                 err_type=type(exception).__name__,
                                 err_message=str(exception)))
    pylab_luts = {}


#################################################################
# Utility functions.
#################################################################
def set_lut(vtk_lut, lut_lst):
    """Setup the tvtk.LookupTable (`vtk_lut`) using the passed list of
    lut values."""
    n_col = len(lut_lst)
    vtk_lut.number_of_colors = n_col
    vtk_lut.build()
    for i in range(0, n_col):
        lt = lut_lst[i]
        vtk_lut.set_table_value(i, lt[0], lt[1], lt[2], lt[3])

    return vtk_lut

def check_lut_first_line(line, file_name=''):
    """Check the line to see if this is a valid LUT file."""
    first = line.split()
    if first[0] != "LOOKUP_TABLE":
        errmsg = "Error: The input data file \"%s\"\n"%(file_name)
        errmsg = errmsg+ "is not a proper lookup table file."\
                 " No LOOKUP_TABLE tag in first line. Try again."
        raise IOError(errmsg)
    try:
        n_color = first[2]
    except:

        raise IOError("Error: No size for LookupTable specified.")
    else:
        return n_color

def parse_lut_file(file_name):
    """Parse the file specified by its name `file_name` for a LUT and
    return the list of parsed values."""

    input = open(file_name, "r")

    line = input.readline()
    n_color = check_lut_first_line(line, file_name)

    lut = []
    for line in input.readlines():
        entr = line.split()
        if len(entr) != 4:
            errmsg="Error: insufficient or too much data in line "\
                    "-- \"%s\""%(entr)
            raise IOError(errmsg)

        tmp = []
        for color in entr:
            try:
                tmp.append(float(color))
            except:
                raise IOError(
                    "Unknown entry '%s'in lookup table input."%color
                )
        lut.append(tmp)

    return lut


def lut_mode_list():
    """ Function to generate the list of acceptable lut_mode values.
    """
    lut_mode_list = ( ['blue-red', 'black-white', 'file', ]
                            + list(pylab_luts.keys()) )
    lut_mode_list.sort()
    return lut_mode_list


######################################################################
# `LUTManager` class.
######################################################################
class LUTManager(Base):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The lookup table.
    lut = Instance(tvtk.LookupTable, (), record=False)
    # The scalar bar.
    scalar_bar = Instance(tvtk.ScalarBarActor, (), record=True)
    # The scalar_bar_widget
    scalar_bar_widget = Instance(tvtk.ScalarBarWidget, ())

    # The representation associated with the scalar_bar_widget.  This
    # only exists in VTK versions about around 5.2.
    scalar_bar_representation = Instance(tvtk.Object, allow_none=True,
                                         record=True)

    # The title text property of the axes.
    title_text_property = Property(record=True)

    # The label text property of the axes.
    label_text_property = Property(record=True)

    # The current mode of the LUT.
    lut_mode = Enum('blue-red', lut_mode_list(),
                     desc='the type of the lookup table')

    # File name of the LUT file to use.
    file_name = Str('', editor=FileEditor,
                    desc='the filename containing the LUT')

    # Reverse the colors of the LUT.
    reverse_lut = Bool(False, desc='if the lut is to be reversed')

    # Turn on/off the visibility of the scalar bar.
    show_scalar_bar = Bool(False,
                           desc='if scalar bar is shown or not')

    # This is an alias for show_scalar_bar.
    show_legend = Property(Bool, desc='if legend is shown or not')

    # The number of labels to use for the scalar bar.
    number_of_labels = Range(0, 64, 8, enter_set=True, auto_set=False,
                             desc='the number of labels to display')

    # Number of colors for the LUT.
    number_of_colors = Range(2, 2147483647, 256, enter_set=True,
                             auto_set=False,
                             desc='the number of colors for the LUT')

    # Enable shadowing of the labels and text.
    shadow = Bool(False, desc='if the labels and text have shadows')

    # Use the default data name or the user specified one.
    use_default_name = Bool(True,
                            desc='if the default data name is to be used')

    # The default data name -- set by the module manager.
    default_data_name = Str('data', enter_set=True, auto_set=False,
                            desc='the default data name')

    # The optionally user specified name of the data.
    data_name = Str('', enter_set=True, auto_set=False,
                    desc='the title of the legend')

    # Use the default range or user specified one.
    use_default_range = Bool(True,
                             desc='if the default data range is to be used')
    # The default data range -- this is computed and set by the
    # module manager.
    default_data_range = Array(shape=(2,), value=[0.0, 1.0],
                               dtype=float, enter_set=True, auto_set=False,
                               desc='the default range of the data mapped')

    # The optionally user defined range of the data.
    data_range = Array(shape=(2,), value=[0.0, 1.0],
                       dtype=float, enter_set=True, auto_set=False,
                       desc='the range of the data mapped')

    # Create a new LUT.
    create_lut = Button('Launch LUT editor',
                        desc='if we launch a Lookup table editor in'
                             ' a separate process')

    ########################################
    ## Private traits.
    # The original range of the data.
    _orig_data_range = Array(shape=(2,), value=[0.0, 1.0], dtype=float)
    _title_text_property = Instance(tvtk.TextProperty)
    _label_text_property = Instance(tvtk.TextProperty)

    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        super(LUTManager, self).__init__(**traits)

        # Initialize the scalar bar.
        sc_bar = self.scalar_bar
        sc_bar.trait_set(lookup_table=self.lut,
                         title=self.data_name,
                         number_of_labels=self.number_of_labels,
                         orientation='horizontal',
                         width=0.8, height=0.17)
        pc = sc_bar.position_coordinate
        pc.trait_set(coordinate_system='normalized_viewport',
                     value=(0.1, 0.01, 0.0))
        self._shadow_changed(self.shadow)

        # Initialize the lut.
        self._lut_mode_changed(self.lut_mode)

        # Set the private traits.
        ttp = self._title_text_property = sc_bar.title_text_property
        ltp = self._label_text_property = sc_bar.label_text_property

        # Call render when the text properties are changed.
        ttp.on_trait_change(self.render)
        ltp.on_trait_change(self.render)

        # Initialize the scalar_bar_widget
        self.scalar_bar_widget.trait_set(scalar_bar_actor=self.scalar_bar,
                                         key_press_activation=False)
        self._number_of_colors_changed(self.number_of_colors)


    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.
        """
        # Do nothing if we are already running.
        if self.running:
            return

        # Show the legend if necessary.
        self._show_scalar_bar_changed(self.show_scalar_bar)

        # Call parent method to set the running state.
        super(LUTManager, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Hide the scalar bar.
        sbw = self.scalar_bar_widget
        if sbw.interactor is not None:
            sbw.off()

        # Call parent method to set the running state.
        super(LUTManager, self).stop()

    ######################################################################
    # Non-public interface
    ######################################################################
    def _lut_mode_changed(self, value):

        if value == 'file':
            if self.file_name:
                self.load_lut_from_file(self.file_name)
            #self.lut.force_build()
            return

        reverse = self.reverse_lut
        if value in pylab_luts:
            lut = pylab_luts[value]
            if reverse:
                lut = lut[::-1, :]
            n_total = len(lut)
            n_color = self.number_of_colors
            if not n_color >= n_total:
                lut = lut[::int(round(n_total/float(n_color)))]
            self.load_lut_from_list(lut.tolist())
            #self.lut.force_build()
            return
        elif value == 'blue-red':
            if reverse:
                hue_range = 0.0, 0.6667
                saturation_range = 1.0, 1.0
                value_range = 1.0, 1.0
            else:
                hue_range = 0.6667, 0.0
                saturation_range = 1.0, 1.0
                value_range = 1.0, 1.0
        elif value == 'black-white':
            if reverse:
                hue_range = 0.0, 0.0
                saturation_range = 0.0, 0.0
                value_range = 1.0, 0.0
            else:
                hue_range = 0.0, 0.0
                saturation_range = 0.0, 0.0
                value_range = 0.0, 1.0
        lut = self.lut
        lut.trait_set(hue_range=hue_range, saturation_range=saturation_range,
                      value_range=value_range,
                      number_of_table_values=self.number_of_colors,
                      ramp='sqrt')
        lut.modified()
        lut.force_build()

        self.render()

    def _scene_changed(self, value):
        sbw = self.scalar_bar_widget
        if value is None:
            return
        if sbw.interactor is not None:
            sbw.off()
        value.add_widgets(sbw, enabled=False)
        if self.show_scalar_bar:
            sbw.on()
        self._foreground_changed_for_scene(None, value.foreground)

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the text.
        self.title_text_property.color = new
        self.label_text_property.color = new
        self.render()

    def _number_of_colors_changed(self, value):
        if self.lut_mode == 'file':
            return
        elif self.lut_mode in pylab_luts:
            # We can't interpolate these LUTs, as they are defined from a
            # table. We hack around this limitation
            reverse = self.reverse_lut
            lut = pylab_luts[self.lut_mode]
            if reverse:
                lut = lut[::-1, :]
            n_total = len(lut)
            if value > n_total:
                return
            lut = lut[::int(round(n_total/float(value)))]
            self.load_lut_from_list(lut.tolist())
        else:
            lut = self.lut
            lut.number_of_table_values = value
            lut.modified()
            lut.build()
            self.render() # necessary to flush.
        sc_bar = self.scalar_bar
        sc_bar.maximum_number_of_colors = value
        sc_bar.modified()
        self.render()

    def _number_of_labels_changed(self, value):
        sc_bar = self.scalar_bar
        sc_bar.number_of_labels = value
        sc_bar.modified()
        self.render()

    def _file_name_changed(self, value):
        if self.lut_mode == 'file':
            self.load_lut_from_file(value)
        else:
            # This will automagically load the LUT from the file.
            self.lut_mode = 'file'

    def _reverse_lut_changed(self, value):
        # This will do the needful.
        self._lut_mode_changed(self.lut_mode)

    def _show_scalar_bar_changed(self, value):
        if self.scene is not None:
            # Without a title for scalar bar actor, vtkOpenGLTexture logs this:
            # Error: No scalar values found for texture input!
            if self.scalar_bar.title == '':
                self.scalar_bar.title = ' '
            self.scalar_bar_widget.enabled = value
            self.render()

    def _get_show_legend(self):
        return self.show_scalar_bar

    def _set_show_legend(self, value):
        old = self.show_scalar_bar
        if value != old:
            self.show_scalar_bar = value
            self.trait_property_changed('show_legend', old, value)

    def _shadow_changed(self, value):
        sc_bar = self.scalar_bar
        sc_bar.title_text_property.shadow = self.shadow
        sc_bar.label_text_property.shadow = self.shadow
        self.render()

    def _use_default_name_changed(self, value):
        self._default_data_name_changed(self.default_data_name)

    def _data_name_changed(self, value):
        sc_bar = self.scalar_bar
        sc_bar.title = value
        sc_bar.modified()
        self.render()

    def _default_data_name_changed(self, value):
        if self.use_default_name:
            self.data_name = value

    def _use_default_range_changed(self, value):
        self._default_data_range_changed(self.default_data_range)

    def _data_range_changed(self, value):
        # should be guaranteed by callers, otherwise VTK will print an error
        assert value[0] <= value[1]
        try:
            self.lut.set_range(value[0], value[1])
        except TypeError:
            self.lut.set_range((value[0], value[1]))
        except AttributeError:
            self.lut.range = value
        self.scalar_bar.modified()
        self.render()

    def _default_data_range_changed(self, value):
        if self.use_default_range:
            self.data_range = value

    def _visible_changed(self, value):
        state = self.show_scalar_bar and value
        self._show_scalar_bar_changed(state)
        super(LUTManager, self)._visible_changed(value)

    def load_lut_from_file(self, file_name):
        lut_list = []
        if len(file_name) > 0:
            try:
                f = open(file_name, 'r')
            except IOError:
                msg = "Cannot open Lookup Table file: %s\n"%file_name
                error(msg)
            else:
                f.close()
                try:
                    lut_list = parse_lut_file(file_name)
                except IOError as err_msg:
                    msg = "Sorry could not parse LUT file: %s\n"%file_name
                    msg += err_msg
                    error(msg)
                else:
                    if self.reverse_lut:
                        lut_list.reverse()
                    self.lut = set_lut(self.lut, lut_list)
                    self.render()

    def load_lut_from_list(self, list):
        self.lut = set_lut(self.lut, list)
        self.render()

    def _get_title_text_property(self):
        return self._title_text_property

    def _get_label_text_property(self):
        return self._label_text_property

    def _create_lut_fired(self):
        from tvtk import util
        tk = 'wx' if ETSConfig.toolkit.lower().startswith('wx') else 'qt'
        script = os.path.join(os.path.dirname(util.__file__),
                              tk + '_gradient_editor.py')
        subprocess.Popen([sys.executable, script])
        auto_close_message('Launching LUT editor in separate process ...')

    def _scalar_bar_representation_default(self):
        w = self.scalar_bar_widget
        if hasattr(w, 'representation'):
            r = w.representation
            r.on_trait_change(self.render)
            return r
        else:
            return None
