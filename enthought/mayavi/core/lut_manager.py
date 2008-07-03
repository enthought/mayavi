"""This manages the lookup table used to map values to colors.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Int, Range, Bool, Trait, Array, \
     Str, Property, List, Enum
from enthought.traits.ui.api import View, Group, Item, FileEditor, \
    ImageEnumEditor
from enthought.tvtk.pyface.api import Scene
from enthought.tvtk.api import tvtk

# Local imports.
from enthought.mayavi.core.base import Base
from enthought.mayavi.core.common import error
from enthought.mayavi.core.lut.pylab_luts import lut_dic as pylab_luts

from enthought.mayavi.core import lut 
import os
lut_image_dir = os.path.dirname(lut.__file__)

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

def check_lut_first_line(line):
    """Check the line to see if this is a valid LUT file."""
    first = line.split()
    if first[0] != "LOOKUP_TABLE":
        errmsg = "Error: The input data file \"%s\"\n"%(file_name)
        errmsg = errmsg+ "is not a proper lookup table file."\
                 " No LOOKUP_TABLE tag in first line. Try again."
        raise IOError, errmsg
    try:
        n_color = first[2]
    except:
        
        raise IOError, "Error: No size for LookupTable specified."
    else:
        return n_color

def parse_lut_file(file_name):
    """Parse the file specified by its name `file_name` for a LUT and
    return the list of parsed values."""
    
    input = open(file_name, "r")

    line = input.readline()
    n_color = check_lut_first_line(line)

    lut = []
    for line in input.readlines():
        entr = line.split()
        if len(entr) != 4:
            errmsg="Error: insufficient or too much data in line "\
                    "-- \"%s\""%(entr)
            raise IOError, errmsg

        tmp = []
        for color in entr:
            try:
                tmp.append(float(color))
            except:
                raise IOError, \
                      "Unknown entry '%s'in lookup table input."%color
        lut.append(tmp)

    return lut


def lut_mode_list():
    """ Function to generate the list of acceptable lut_mode values.
    """
    lut_mode_list = ( ['blue-red', 'black-white', 'file', ] 
                            + [key for key in pylab_luts.keys() if 
                                                    not key[-2:]=='_r' ])
    lut_mode_list.sort()
    return lut_mode_list


######################################################################
# `LUTManager` class.
######################################################################
class LUTManager(Base):
    
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The lookup table.
    lut = Instance(tvtk.LookupTable, ())
    # The scalar bar.
    scalar_bar = Instance(tvtk.ScalarBarActor, ())
    # The scalar_bar_widget
    scalar_bar_widget = Instance(tvtk.ScalarBarWidget, ())

    # The title text property of the axes.
    title_text_property = Property
    
    # The label text property of the axes.
    label_text_property = Property

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

    # The number of labels to use for the scalar bar.
    number_of_labels = Range(0, 64, 8,
                             desc='the number of labels to display')

    # Number of colors for the LUT.
    number_of_colors = Range(2, 2147483647, 256,
                             desc='the number of colors for the LUT')

    # Enable shadowing of the labels and text.
    shadow = Bool(False, desc='if the labels and text have shadows')

    # Use the default data name or the user specified one.
    use_default_name = Bool(True,
                            desc='if the default data name is to be used')

    # The default data name -- set by the module manager.
    default_data_name = Str('data', desc='the default data name')

    # The optionally user specified name of the data.
    data_name = Str('', desc='the title of the legend')

    # Use the default range or user specified one.
    use_default_range = Bool(True,
                             desc='if the default data range is to be used')
    # The default data range -- this is computed and set by the
    # module manager.
    default_data_range = Array(shape=(2,), value=[0.0, 1.0],
                               dtype=float,
                               desc='the default range of the data mapped')

    # The optionally user defined range of the data.
    data_range = Array(shape=(2,), value=[0.0, 1.0],
                       dtype=float,
                       desc='the range of the data mapped')


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
        sc_bar.set(lookup_table=self.lut,
                   title=self.data_name,
                   number_of_labels=self.number_of_labels,
                   orientation='horizontal',
                   width=0.8, height=0.17)
        pc = sc_bar.position_coordinate
        pc.set(coordinate_system='normalized_viewport',
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
        self.scalar_bar_widget.set(scalar_bar_actor=self.scalar_bar,
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
        if value in pylab_luts.keys():
            if reverse:
                value = value + '_r'
            self.load_lut_from_list(pylab_luts[value])
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
        lut.set(hue_range=hue_range, saturation_range=saturation_range,
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
        if self.lut_mode == 'file' or self.lut_mode in pylab_luts.keys():
            return
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
            self.scalar_bar_widget.enabled = value
            self.render()

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
                except IOError, err_msg:
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
