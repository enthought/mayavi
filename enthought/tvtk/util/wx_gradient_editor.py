""" A wxPython based color gradient editor for vtkLookupTables and
color transfer functions.

This code is distributed under the conditions of the BSD license.

Based on a Tk version of this widget by Gerald Knizia <cgk.d@gmx.net>
Ported to wxPython by Pete Schmitt <schmitt@colorado.edu>
Cleaned up and enhanced for use with MayaVi2 by Prabhu Ramachandran

Copyright (c) 2005-2006, Gerald Knizia, Pete Schmitt and Prabhu Ramachandran
"""
##########################################################################
# TODO:
#
# * Support for resizing the widget.
#
##########################################################################


# Third-party imports
import wx

# Enthought library imports
from enthought.tvtk.api import tvtk

# Local imports
from gradient_editor import GradientTable, ColorControlPoint

##########################################################################
# `wxGradientControl` class.
##########################################################################
class wxGradientControl(wx.Panel):
    """Widget which displays the gradient represented by an GradientTable
    object (and does nothing beyond that)"""
    def __init__(self, masterPanel, gradient_table, width, height ):
        """master: panel in which to place the control. GradientTable is the
        Table to which to attach."""
        wx.Panel.__init__(self, masterPanel, size=wx.Size(width, height),
                          style=wx.RAISED_BORDER,
                          name="Colormap Panel")
                          
        self.SetBackgroundColour(wx.Colour(255,255,255))    
        self.width = width
        self.height = height
        self.gradient_table = gradient_table
        assert( gradient_table.size == width )
        # ^- currently only able to use gradient tables in the same size as the canvas width

        # bind paint event to redraw  when resizing/creating window...
        wx.EVT_PAINT(self, self.OnPaint)

    def OnPaint(self, event):
        """ Paint event handler for when the window is resized and
        whatnot."""
        dc = wx.PaintDC(self)
        self.update()
        
    def update(self):
        """Repaint the control."""
        #self.canvas.delete(tk.ALL) # clears all lines contained.
        dc = wx.ClientDC(self)
        dc.SetBackground(wx.Brush(wx.Colour(0,0,0), wx.SOLID))
        dc.Clear()

        width, height = self.GetSize()

        # From the old tk GradientEditor:
        #     a look around the web (http://wiki.tcl.tk/11868) told me that
        #     using the PhotoImage tk-control would not be a good idea and
        #     that line objects work faster. While I doubt this is an optimal
        #     solution it currently works fast enought.
        # So... let's do the same thing for the new and improved (?) wxPython GradientEditor.

        xform = self.gradient_table.scaling_function
        start_y = 0
        end_y = height
        if xform:
            # if a scaling transformation is provided, paint the original
            # gradient under the scaled gradient.
            start_y = height/2
        
        # paint the original gradient as it stands in the table.
        dc.BeginDrawing()
        for x in range(width):
            (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(float(x)/(width-1))
            dc.SetPen(wx.Pen(wx.Colour(int(255*r),int(255*g),int(255*b))))
            dc.SetBrush(wx.Brush((int(255*r),int(255*g),int(255*b)), wx.SOLID))
            dc.DrawLine(x, start_y, x, end_y)
        if xform:
            # paint the scaled gradient below
            end_y = start_y
            start_y = 0
            for x in range(width):
                f = float(x)/(width-1)
                (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(xform(f))
                dc.SetBrush(wx.Brush((int(255*r),int(255*g),int(255*b)), wx.SOLID))
                dc.DrawLine(x, start_y, x, end_y)
        dc.EndDrawing()


##########################################################################
# `Channel` class.
##########################################################################
class Channel:
    def __init__(self, function_control, name, rgb_color,
                 channel_index, channel_mode):
        """arguments documented in function body"""
        self.control = function_control  #owning function control
        self.name = name #'r','g','b','h','s','v' or 'a'
        self.rgb_color = rgb_color
        # ^-- string containing a tk color value with which to
        # paint this channel
        self.index = channel_index #0: r or h, 1: g or s, 2: b or v, 3: a
        self.mode = channel_mode #'hsv' or 'rgb'

    def get_value(self, color):
        """Return height value of the current channel for the given color. 
        Range: 0..1"""
        if ( self.mode == 'hsv' ):
            return color.get_hsva()[self.index]
        else:
            return color.get_rgba()[self.index]

    def get_value_index(self, color):
        """Return height index of channel value of Color. 
        Range: [1..ControlHeight]"""
        return int( 1+(self.control.height-1)*(1.0 - self.get_value(color)) )

    def get_index_value(self, y):
        """Get value in [0..1] of height index y"""
        return min(1.0, max(0.0, 1.0 - float(y)/(self.control.height-1)))

    def set_value( self, color, new_value_on_this_channel ):
        """Color will be modified: NewValue.. will be set to the color
        channel that ``*self`` represents."""
        if ( self.mode == 'hsv' ):
            hsva = [color.get_hsva()[0], color.get_hsva()[1],
                    color.get_hsva()[2], color.get_hsva()[3] ]
            hsva[self.index] = new_value_on_this_channel
            if ( hsva[0] >= 1.0 - 1e-5 ):
                # hack to make sure hue does not jump back to 0.0
                # when it should be at 1.0 (rgb <-> hsv xform not
                # invertible there)
                hsva[0] = 1.0 - 1e-5
            color.set_hsva(hsva[0],hsva[1],hsva[2],hsva[3])
        else:
            rgba = [color.get_rgba()[0], color.get_rgba()[1],
                    color.get_rgba()[2], color.get_rgba()[3] ]
            rgba[self.index] = new_value_on_this_channel
            color.set_rgba(rgba[0],rgba[1],rgba[2],rgba[3])

    def set_value_index( self, color, y ):
        """Color will be modified: the value assigned to the height index 
        y will be set to the color channel of Color ``*self`` represents."""
        self.set_value( color, self.get_index_value(y) )

    def get_pos_index(self,f):
        """Return x-index for gradient position f in [0..1]"""
        return int(f*(self.control.width-1))

    def get_index_pos(self,idx):
        """Return gradient position f in [0..1] for x-index Idx in 
        [0..ControlWidth-1]"""
        return (1.0*idx)/(self.control.width-1)

    def paint(self, deviceContext):
        """Paint current channel into Canvas (a canvas of a function control
        object). 

        Contents of the canvas are not deleted prior to painting,
        so more than one channel can be painted into the same canvas."""
        dc = deviceContext

        table = self.control.table
        # only control points which are active for the current channel
        # are to be painted. filter them out.
        relevant_control_points = filter( \
            lambda x: self.name in x.active_channels,
            table.control_points )
        dc.BeginDrawing()
        # lines between control points
        dc.SetPen(wx.Pen(self.rgb_color,1))
        #dc.SetBrush(wx.Brush((255,255,255), wx.SOLID))
        dc.SetBrush(wx.Brush((255,255,255), wx.SOLID))
        for k in range( len(relevant_control_points) - 1 ):
            cur_point = relevant_control_points[k]
            next_point = relevant_control_points[1+k]

            dc.DrawLine( self.get_pos_index(cur_point.pos),
                    self.get_value_index(cur_point.color),
                    self.get_pos_index(next_point.pos),
                    self.get_value_index(next_point.color))

        # control points themself.
        dc.SetPen(wx.Pen("BLACK",1))
        dc.SetBrush(wx.Brush((255,255,255), wx.SOLID))
        for control_point in relevant_control_points:
            x = self.get_pos_index( control_point.pos )
            y = self.get_value_index( control_point.color )
            radius=6
            #print(x,y)
            dc.DrawRectangle(x-(radius/2.0), y-(radius/2.0),radius,radius)
            dc.DrawRectangle(100,80,6,6)
        dc.EndDrawing()


##########################################################################
# `wxFunctionControl` class.
##########################################################################
class wxFunctionControl(wx.Panel):
    """Widget which displays a rectangular regions on which hue, sat, val
    or rgb values can be modified. An function control can have one or more
    attached color channels."""

    # Radius around a control point center in which we'd still count a
    # click as "clicked the control point"
    control_pt_click_tolerance = 4     

    def __init__(self, master, gradient_table, color_space, width, height):
        """Initialize a function control widget on tkframe master.
        
        Parameters:
        -----------

        master: The master widget.  Note that this widget *must* have
             the methods specified in the `AbstractGradEditorWidget`
             interface.
        
        on_table_changed: Callback function taking a bool argument of meaning 
            'FinalUpdate'. FinalUpdate is true if a control point is dropped,
            created or removed and false if the update is due to a control point
            currently beeing dragged (but not yet dropped)

        color_space: String which specifies the channels painted on this control.
             May be any combination of h,s,v,r,g,b,a in which each channel
             occurs only once.

        set_status_text: a callback used to set the status text
             when using the editor.
        """
        self.text_map = {'r': 'RED', 'g': 'GREEN', 'b': 'BLUE',
                         'h': 'HUE', 's': 'SATURATION', 'v': 'VALUE',
                         'a': 'ALPHA'}
        self.master = master
        self.table = gradient_table
        self.gradient_table = gradient_table
        self.width = width
        self.height = height

        wx.Panel.__init__(self, master, size=wx.Size(width, height),
                          name="RGBHSVA Editor")
        # You can pass style=wx.RAISED_BORDER into wx.Panel() to make a border, but....
        # then a few pixels on each side are chopped off...
        
        #self.SetBackgroundColour(wx.Colour(255,0,0))
        self.channels = []
        
        # add the channels
        for c in color_space:
            if c == 'r':
                self.channels += [Channel(self, "r", (255,0,0), 0, 'rgb' )]
            elif c == 'g':
                self.channels += [Channel(self, "g", (0,255,0), 1, 'rgb' )]
            elif c == 'b':
                self.channels += [Channel(self, "b", (0,0,255), 2, 'rgb' )]
            elif c == 'h':
                self.channels += [Channel(self, "h", (255,0,0), 0, 'hsv' )]
            elif c == 's':
                self.channels += [Channel(self, "s", (0,255,0), 1, 'hsv' )]
            elif c == 'v':
                self.channels += [Channel(self, "v", (0,0,255), 2, 'hsv' )]
            elif c == 'a':
                self.channels += [Channel(self, "a", (0,0,0), 3, 'hsv' )]

        # generate a list of channels on which markers should
        # be bound if moved on the current channel. since we interpolate
        # the colors in hsv space, changing the r, g or b coordinates
        # explicitely means that h, s and v all have to be fixed.
        self.active_channels_string = ""
        for channel in self.channels:
            self.active_channels_string += channel.name
        if ( ( 'r' in color_space ) or ( 'g' in color_space ) or ( 'b' in color_space ) ):
            for c in "hsv":
                if ( not ( c in self.active_channels_string ) ):
                    self.active_channels_string += c
        if ( color_space == 'a' ):
            # alpha channels actually independent of all other channels.
            self.active_channels_string = 'a'

        self.update()

        wx.EVT_LEFT_DOWN(self, self.on_left_button_down)
        wx.EVT_LEFT_UP(self, self.on_left_button_up)
        wx.EVT_RIGHT_DOWN(self, self.on_right_button_down)
        wx.EVT_RIGHT_UP(self, self.on_right_button_up)
        wx.EVT_MOTION(self, self.on_mouse_move)
        wx.EVT_PAINT(self, self.on_paint)
        wx.EVT_LEAVE_WINDOW(self, self.on_leave_window)
        
        # need to set to "None" initially or event handlers get confused.
        self.cur_drag = None #<- [channel,control_point] while something is dragged.
        
    def find_control_point(self, x, y):
        """Check if a control point lies near (x,y) or near x if y == None. 
        returns [channel, control point] if found, None otherwise"""
        for channel in self.channels:
            for control_point in self.table.control_points:
                # take into account only control points which are
                # actually active for the current channel
                if ( not ( channel.name in control_point.active_channels ) ):
                    continue
                point_x = channel.get_pos_index( control_point.pos )
                point_y = channel.get_value_index( control_point.color )
                y_ = y
                if ( None == y_ ):
                    y_ = point_y
                if ( (point_x-x)**2 + (point_y-y_)**2 <= self.control_pt_click_tolerance**2 ):
                    return [channel, control_point]
        return None
        
    def table_config_changed(self, final_update):
        """Called internally in the control if the configuration of the attached
        gradient table has changed due to actions of this control.
        
        Forwards the update/change notice."""
        self.table.update()
        self.master.on_gradient_table_changed(final_update)

    def update(self, event = None):
        """Repaint the control."""
        dc = wx.ClientDC(self)
        #if we have a custom background, we *must* set the background brush *BEFORE* clearing...
        dc.SetBackground(wx.Brush(wx.Colour(255,255,255), wx.SOLID))
        dc.Clear()

        for channel in self.channels:
            channel.paint(dc)

    def on_paint(self, event=None):
        dc = wx.PaintDC(self)
        self.update()

    def on_left_button_down(self, event):
        self.cur_drag = self.find_control_point( event.GetX(), event.GetY() )
        
    def on_left_button_up(self, event):
        if self.cur_drag:
            self.table_config_changed( final_update = True )
            self.cur_drag = None

    def on_leave_window(self, event):
        self.on_left_button_up(event)
        
    def on_right_button_down(self, event):
        pass
        
    def on_right_button_up(self, event):
        # toggle control point. check if there is a control point
        # under the mouse. If yes, delete it, if not, create one
        # at that point.
        cur_control_point = self.find_control_point(event.GetX(), None)
        if cur_control_point:
            # found a marker at the click position. delete it and return,
            # unless it is a fixed marker (at pos 0 or 1)..
            if ( cur_control_point[1].fixed ):
                # in this case do nothing. Fixed markers cannot be deleted.
                return
            self.table.control_points.remove(cur_control_point[1])
            self.table_config_changed(final_update=True)
        else:
            # since there was no marker to remove at the point, we assume
            # that we should place one there
            new_control_point = ColorControlPoint(active_channels = self.active_channels_string)
            new_control_point.set_pos(self.channels[0].get_index_pos(event.GetX()))
    
            # set new control point color to the color currently present
            # at its designated position
            new_control_point.color = self.table.get_pos_color(new_control_point.pos)
    
            self.table.insert_control_point( new_control_point )
            self.table_config_changed( final_update = True )
        
    def on_mouse_move(self, event):
        # currently dragging a control point?
        channel = None
        point = None
        if self.cur_drag:
            channel = self.cur_drag[0]
            point = self.cur_drag[1]
            if ( not point.fixed ):
                point.set_pos( channel.get_index_pos(event.GetX()) )
                point.activate_channels( self.active_channels_string )
                self.table.sort_control_points()
            channel.set_value_index( point.color, event.GetY() )
            self.table_config_changed( final_update = False )

        screenX = event.GetX()
        screenY = event.GetY()
        width, height = self.GetSize()
        master = self.master
        s1, s2 = master.get_table_range()
        if channel is not None:
            name = self.text_map[channel.name]
            pos = s1 + (s2 - s1)*point.pos
            val = channel.get_value(point.color)
            txt = '%s: (%.3f, %.3f)'%(name, pos, val)
        else:
            x = s1 + (s2 - s1)*float(screenX)/(width-1)
            y = 1.0 - float(screenY)/(height-1)
            txt = "position: (%.3f, %.3f)"%(x, y)

        self.master.set_status_text(txt)

##########################################################################
# `AbstractGradEditor` interface.
##########################################################################
class AbstractGradEditor(object):
    def on_gradient_table_changed(self, final_update):
        """ Update the gradient table and vtk lookuptable."""
        raise NotImplementedError
    
    def set_status_text(self, msg):
        """Set the status on the status widget if you have one."""
        raise NotImplementedError

    def get_table_range(self):
        """Return the CTF or LUT's scalar range."""
        raise NotImplementedError
    

##########################################################################
# `wxGradientEditorWidget` class.
##########################################################################
class wxGradientEditorWidget(wx.Panel, AbstractGradEditor):
    """A Gradient Editor widget that can be used anywhere.
    """
    def __init__(self, master, vtk_table, on_change_color_table=None,
                 colors=None):
        """

        Parameters:
        -----------
        
        vtk_table : the `tvtk.LookupTable` or `tvtk.VolumeProperty` object
                    to set.
        
        on_change_color_table : A callback called when the color table
                                changes.
        
        colors : list of 'rgb', 'hsv', 'h', 's', 'v', 'a'
                 (Default : ['rgb', 'hsv', 'a'])

                 'rgb' creates one panel to edit Red, Green and Blue
                 colors.

                 'hsv' creates one panel to edit Hue, Saturation and
                 Value.

                 'h', 's', 'v', 'r', 'g', 'b', 'a' separately
                 specified creates different panels for each.
        """
        wx.Panel.__init__(self, master)

        if colors is None:
            colors = ['rgb', 'hsv', 'a']
        
        gradient_preview_width = 300
        gradient_preview_height = 50
        channel_function_width = gradient_preview_width
        channel_function_height = 80
        self.gradient_table = GradientTable(gradient_preview_width)
        self.vtk_color_table = vtk_table
        if isinstance(vtk_table, tvtk.LookupTable):
            self.vtk_table_is_lut = True
        else:
            # This is a tvtk.VolumeProperty
            self.vtk_table_is_lut = False
            # Initialize the editor with the volume property. 
            self.gradient_table.load_from_vtk_volume_prop(vtk_table)

        self.on_change_color_table = on_change_color_table

        # set up all the panels in a gridbagsizer (i.e. a big grid)
        # 6x2 size:  6 rows, 2 columns...
        sizer = wx.GridBagSizer(2, 2)

        # "Gradient Viewer" panel, in position (0,1) for sizer
        self.gradient_control = wxGradientControl(self,
                                                  self.gradient_table,
                                                  gradient_preview_width,
                                                  gradient_preview_height)
        tt = wx.ToolTip('Right click for menu')
        self.gradient_control.Bind(wx.EVT_CONTEXT_MENU, self.on_gradient_menu)
        self.gradient_control.SetToolTip(tt)
        sizer.Add(self.gradient_control, pos=(0,1))

        
        # Add the function controls:
        function_controls = []
        self.function_controls = function_controls

        tooltip_text = 'Left click: move control points\n'\
                       'Right click: add/remove control points'
        editor_data = {'rgb': ('', 'RGB'),
                       'hsv': ('Hue: Red; Saturation: Green; '\
                               'Value: Blue\n',                   
                               'HSV'
                               ),
                       'h': ('', 'HUE'),
                       's': ('', 'SAT'),
                       'v': ('', 'VAL'),
                       'r': ('', 'RED'),
                       'g': ('', 'GREEN'),
                       'b': ('', 'BLUE'),
                       'a': ('', 'ALPHA'),
                       }
        row = 1
        for color in colors:
            data = editor_data[color]
            control = wxFunctionControl(self, self.gradient_table, color,
                                        channel_function_width,
                                        channel_function_height)
            txt = data[0] + tooltip_text
            control.SetToolTip(wx.ToolTip(txt))
            # Add name of editor (to left side of editor)
            sizer.Add(wx.StaticText(self, -1, data[1]), pos=(row, 0),
                      flag=wx.ALIGN_CENTER|wx.ALL)
            # Add the "RGB" control point editor
            sizer.Add(control, pos=(row, 1))
            function_controls.append(control)
            row += 1

        # The status text.
        self.text = wx.StaticText(self, -1, 'status')
        sizer.Add(self.text, (row,0), (row,2))
        row += 1

        # set the appropriate sizer.
        sizer.SetSizeHints(self)
        self.SetSizerAndFit(sizer)

    ######################################################################
    # `wxGradientEditorWidget` interface.
    ######################################################################
    def set_status_text(self, msg):
        t = self.text
        t.SetLabel(msg)
        t.Refresh()
        t.Update()

    def on_gradient_table_changed(self, final_update ):
        """ Update the gradient table and vtk lookuptable..."""
        # update all function controls.
        for control in self.function_controls:
            control.update()
        # repaint the gradient display or the external windows only
        # when the instant*** options are set or when the update was final.
        #if final_update or ( 1 == self.show_instant_gradients.get() ):
        if True:
            self.gradient_control.update()

        #if final_update or ( 1 == self.show_instant_feedback.get() ):
        if final_update:
            vtk_table = self.vtk_color_table
            if self.vtk_table_is_lut:
                self.gradient_table.store_to_vtk_lookup_table(vtk_table)
            else:
                rng = self.get_table_range()
                self.gradient_table.store_to_vtk_volume_prop(vtk_table, rng)
                
            cb = self.on_change_color_table
            if cb is not None:
                cb()

    def get_table_range(self):
        vtk_table = self.vtk_color_table
        if self.vtk_table_is_lut:
            return vtk_table.table_range
        else:
            return vtk_table.get_scalar_opacity().range

    def load(self, file_name):
        """Set the state of the color table using the given file.
        """
        if len(file_name) == 0:
            return
        self.gradient_table.load(file_name)
        self.on_gradient_table_changed(final_update = True)

    def save(self, file_name):
        """Store the color table to the given file.  This actually
        generates 3 files, a '.grad', a '.lut' file and a '.jpg' file.
        The .lut file can be used to setup a lookup table.  The .grad
        file is used to set the state of the gradient table and the
        JPG file is an image of the how the lut will look.
        """
        if len(file_name) == 0:
            return
        self.gradient_table.save(file_name)          

    ######################################################################
    # wxPython event methods.
    ######################################################################
    def on_gradient_menu(self, event):
        if not hasattr(self, 'save_menuid'):
            # Do this only the first time.
            self.save_menuid = wx.NewId()
            self.load_menuid = wx.NewId()
            self.Bind(wx.EVT_MENU, self.on_save, id=self.save_menuid)
            self.Bind(wx.EVT_MENU, self.on_load, id=self.load_menuid)
        
        menu = wx.Menu()
        menu.Append(self.save_menuid, "Save as")
        menu.Append(self.load_menuid, "Load")
        self.PopupMenu(menu)
        menu.Destroy()

    def on_save(self, event):
        """
        Open "Save" dialog, write lookuptable to 3 files: ``*.lut`` (lookuptable) ``*.grad``
        (gradient table for use with this program), and ``*.jpg`` (image of the
        gradient)
        """
        dlg = wx.FileDialog(self, "Save LUT to...", style=wx.SAVE)
        wildcard = "Gradient Files (.grad)|*.grad|"   \
                   "All files (*.*)|*.*"
        dlg.SetWildcard(wildcard)
        if (dlg.ShowModal() == wx.ID_OK):
            file_name = dlg.GetPath()
            if file_name:
                self.save(file_name)

    def on_load(self, event):
        """
        Load a ``*.grad`` lookuptable file using wxpython dialog
        """
        style = wx.OPEN | wx.HIDE_READONLY
        dlg = wx.FileDialog(self, "Open a file", style=style)
        wildcard = "Gradient Files (.grad)|*.grad|"   \
                   "All files (*.*)|*.*"
        dlg.SetWildcard(wildcard)
        if (dlg.ShowModal() == wx.ID_OK):
            file_name = dlg.GetPath()        
            if file_name:
                self.load(file_name)


##########################################################################
# `wxGradientEditor` class.
##########################################################################
class wxGradientEditor(wx.Frame):
    """ wxPython frame that displays the gradient editor window,
    i.e. the thing that contains the gradient display, the function
    controls and the buttons.
    """
    def __init__(self, vtk_table, on_change_color_table = None, colors=None):
        """Initialize the gradient editor window.
        
        Parameters
        ----------
        vtk_table: Instance of vtkLookupTable, designating the table which is
            to be edited.
        on_change_color_table: Callback function taking no arguments. Called
            when the color table was changed and rendering is
            requested.
        """

        wx.Frame.__init__(self, None, -1, "Color Gradient Editor",
                          wx.DefaultPosition, [350, 400])

        self.widget = wxGradientEditorWidget(self, vtk_table, 
                                             on_change_color_table,
                                             colors)
        
        # draw the rest of the GUI (i.e. statusbar, menubar, etc.
        self.SetupMenuBar()
        self.CreateStatusBar()                      

    def SetupMenuBar(self):
        """
        Create menus (i.e. Create Filemenu and submenus, help menu, ...)
        """
        ## Set up the MenuBar
        MenuBar = wx.MenuBar()

        #FILE Menu....
        file_menu = wx.Menu()
        item = file_menu.Append(-1, "&Save","Save CTF")
        self.Bind(wx.EVT_MENU, self.widget.on_save, item)
        item = file_menu.Append(-1, "&Load","Load CTF")
        self.Bind(wx.EVT_MENU, self.widget.on_load, item)
        item = file_menu.Append(-1, "&Close","Close this frame")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)
        MenuBar.Append(file_menu, "&File")

        help_menu = wx.Menu()
        item = help_menu.Append(-1, "&Help", "Help")
        self.Bind(wx.EVT_MENU, self.OnHelp, item)
        item = help_menu.Append(-1, "&About", "About")
        self.Bind(wx.EVT_MENU, self.OnAbout, item)
        MenuBar.Append(help_menu, "&Help")        
            
        self.SetMenuBar(MenuBar)

    def OnQuit(self, event):
        self.Close()

    def OnHelp(self, event):
        """ Help defining the mouse interactions """
        message = "Right click to add control points.  Left click to move control points"
        dlg = wx.MessageDialog(self, message,
                               'About wxGradientEditor',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

    def OnAbout(self, event):
        """ Who wrote the program?"""
        message = 'tk Gradient Editor for MayaVi1: Gerald Knizia (cgk.d@gmx.net)\n'\
                  'wxPython port: Pete Schmitt (schmitt@colorado.edu)\n'\
                  'Enhanced for MayaVi2: Prabhu Ramachandran'
        dlg = wx.MessageDialog(self, message,
                               'About wxGradientEditor',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()


##########################################################################
# Traits UI factory functions.
##########################################################################
def gradient_editor_factory(wx_parent, trait_editor):
    """This is a factory function for
    `enthought.traits.ui.CustomEditor` and allows us to use the
    `wxGradientEditorWidget` as a traits UI editor.  This currently
    assumes that the user is using TVTK.  The `wxGradientEditorWidget`
    works with VTK directly.
    """
    tvtk_obj = getattr(trait_editor.object, trait_editor.name)
    widget = wxGradientEditorWidget(wx_parent, tvtk_obj)
    return widget


##########################################################################
# Test case related code.
##########################################################################
def make_test_table(lut=False):
    from ctf import ColorTransferFunction, PiecewiseFunction
    if lut:
        table = tvtk.LookupTable()
        table.table_range = (255, 355)
        return table, None, None
    else:
        table = tvtk.VolumeProperty()
        ctf = ColorTransferFunction()
        mins, maxs = 255, 355
        ds = (maxs-mins)/4.0
        try:
            ctf.range = (mins, maxs)
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass
        ctf.add_rgb_point(mins,      0.00, 0.0, 1.00)
        ctf.add_rgb_point(mins+ds,   0.25, 0.5, 0.75)
        ctf.add_rgb_point(mins+2*ds, 0.50, 1.0, 0.50)
        ctf.add_rgb_point(mins+3*ds, 0.75, 0.5, 0.25)
        ctf.add_rgb_point(maxs,      1.00, 0.0, 0.00)
        otf = PiecewiseFunction()
        otf.add_point(255, 0.0)
        otf.add_point(355, 0.2)
        table.set_color(ctf)
        table.set_scalar_opacity(otf)
        return table, ctf, otf


def test_trait_ui():
    from enthought.traits.api import HasTraits, Instance, Button
    from enthought.traits.ui.api import View, Item, CustomEditor

    class Test(HasTraits):
        p = Instance(tvtk.VolumeProperty, ())
        b = Button('Click me')

        view = View(Item(name='p', style='custom',
                         resizable=True,
                         editor=CustomEditor(gradient_editor_factory)),
                    Item('b')
                    )

    table, otf, ctf = make_test_table(False)
    t = Test(p=table)
    # We need to hang on to these so these don't go out of scope.
    t.otf = otf
    t.ctf = ctf
    return t

def main():
    table, ctf, otf = make_test_table(lut=False)
    # the actual gradient editor code.
    def on_color_table_changed():
        """If we had a vtk window running, update it here"""
        print("Update Render Window")
    
    app = wx.PySimpleApp()
    editor = wxGradientEditor(table,
                              on_color_table_changed,
                              #colors=['rgb', 'a', 'h', 's', 'v'],
                              )
    editor.Show()
    app.MainLoop()
        

##########################################################################
# Test application.
##########################################################################
if __name__ == "__main__":
    #t = test_trait_ui()
    #t.configure_traits()
    main()
