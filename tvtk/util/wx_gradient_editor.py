""" A wxPython based color gradient editor for vtkLookupTables and
color transfer functions.

This code is distributed under the conditions of the BSD license.

Based on a Tk version of this widget by Gerald Knizia <cgk.d@gmx.net>
Ported to wxPython by Pete Schmitt <schmitt@colorado.edu>
Cleaned up and enhanced for use with MayaVi2 by Prabhu Ramachandran

Copyright (c) 2005-2020, Gerald Knizia, Pete Schmitt and Prabhu Ramachandran
"""


# Third-party imports
import wx

# Local imports
from tvtk.util.gradient_editor import (
    ColorControlPoint, ChannelBase, FunctionControl, GradientEditorWidget
)

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
class Channel(ChannelBase):
    def paint(self, deviceContext):
        """Paint current channel into Canvas (a canvas of a function control
        object).

        Contents of the canvas are not deleted prior to painting,
        so more than one channel can be painted into the same canvas."""
        dc = deviceContext

        table = self.control.table
        # only control points which are active for the current channel
        # are to be painted. filter them out.
        relevant_control_points = [
            x for x in table.control_points if self.name in x.active_channels
        ]
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
class wxFunctionControl(wx.Panel, FunctionControl):
    """Widget which displays a rectangular regions on which hue, sat, val
    or rgb values can be modified. An function control can have one or more
    attached color channels."""

    # Radius around a control point center in which we'd still count a
    # click as "clicked the control point"
    control_pt_click_tolerance = 4

    ChannelFactory = Channel

    def __init__(self, master, gradient_table, color_space, width, height):
        """Initialize a function control widget on tkframe master.

        Parameters:
        -----------

        master: The master widget.  Note that this widget *must* have
             the methods specified in the `AbstractGradientEditorWidget`
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
        FunctionControl.__init__(self, master, gradient_table, color_space,
                                 width, height)

        wx.Panel.__init__(self, master, size=wx.Size(width, height),
                          name="RGBHSVA Editor")

        self.update()

        wx.EVT_LEFT_DOWN(self, self.on_left_button_down)
        wx.EVT_LEFT_UP(self, self.on_left_button_up)
        wx.EVT_RIGHT_DOWN(self, self.on_right_button_down)
        wx.EVT_RIGHT_UP(self, self.on_right_button_up)
        wx.EVT_MOTION(self, self.on_mouse_move)
        wx.EVT_PAINT(self, self.on_paint)
        wx.EVT_LEAVE_WINDOW(self, self.on_leave_window)

    ######################################################################
    # wxPython event methods.
    ######################################################################
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
# `wxGradientEditorWidget` class.
##########################################################################
class wxGradientEditorWidget(wx.Panel, GradientEditorWidget):
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
        GradientEditorWidget.__init__(self, master, vtk_table,
                                      on_change_color_table, colors)
        wx.Panel.__init__(self, master)

        gradient_preview_width = self.gradient_preview_width
        gradient_preview_height = self.gradient_preview_height
        channel_function_width = self.channel_function_width
        channel_function_height = self.channel_function_height

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
        function_controls = self.function_controls


        editor_data = self.editor_data
        row = 1
        for color in self.colors:
            data = editor_data[color]
            control = wxFunctionControl(self, self.gradient_table, color,
                                        channel_function_width,
                                        channel_function_height)
            txt = data[0] + self.tooltip_text
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
        Open "Save" dialog, write lookuptable to 3 files: ``*.lut``
        (lookuptable) ``*.grad`` (gradient table for use with this program),
        and ``*.jpg`` (image of the gradient)
        """
        dlg = wx.FileDialog(self, "Save LUT to...", style=wx.FD_SAVE)
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
        style = wx.FD_OPEN
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
# Test application.
##########################################################################
def main():
    from tvtk.util.traitsui_gradient_editor import make_test_table
    table, ctf, otf = make_test_table(lut=False)
    # the actual gradient editor code.
    def on_color_table_changed():
        """If we had a vtk window running, update it here"""
        print("Update Render Window")

    app = wx.App(False)
    editor = wxGradientEditor(table,
                              on_color_table_changed,
                              colors=['rgb', 'a', 'h', 's', 'v'],
                              )
    editor.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
