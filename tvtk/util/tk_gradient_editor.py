""" Defines the UI for a gradient editor for vtkLookupTables and color
transfer functions.

This code is distributed under the conditions of the BSD license.

This code was originally written by Gerald Knizia <cgk.d@gmx.net> and
later modified by Prabhu Ramachandran

Copyright (c) 2005-2015, Gerald Knizia and Prabhu Ramachandran
"""

try:
    import Tkinter as tk
    import tkFileDialog
except ImportError:
    import tkinter as tk
    import tkinter.filedialog as tkFileDialog

from .gradient_editor import GradientTable, ColorControlPoint

##########################################################################
# `GradientControl` class.
##########################################################################
class GradientControl(tk.Frame):
    """Widget which displays the gradient represented by an GradientTable
    object (and does nothing beyond that)"""
    def __init__(self, master, gradient_table, width, height ):
        """master: frame in which to place the control. GradientTable is the
        Table to which to attach."""
        tk.Frame.__init__(self, master, borderwidth=2, relief='groove')
        self.width = width
        self.height = height
        self.gradient_table = gradient_table
        assert( gradient_table.size == width )
        # ^- currently only able to use gradient tables in the same
        # size as the canvas width
        self.canvas = tk.Canvas(self, background="white", width=width,
                height=height)
        self.canvas.pack()
        self.update()

    def update(self):
        """Repaint the control."""
        self.canvas.delete(tk.ALL) # clears all lines contained.

        # a look around the web (http://wiki.tcl.tk/11868) told me that
        # using the PhotoImage tk-control would not be a good idea and
        # that line objects work faster. While I doubt this is an optimal
        # solution it currently works fast enought.

        xform = self.gradient_table.scaling_function
        start_y = 0
        end_y = self.height
        if xform:
            # if a scaling transformation is provided, paint the original
            # gradient under the scaled gradient.
            start_y = self.height/2

        # paint the original gradient as it stands in the table.
        width = self.width
        for x in range(width):
            (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(float(x)/(width-1))
            self.canvas.create_line(x,start_y,x,end_y, \
                    fill="#%02x%02x%02x" % (int(255*r),int(255*g),int(255*b)))
        if xform:
            # paint the scaled gradient below
            end_y = start_y
            start_y = 0
            for x in range(self.width):
                f = float(x)/(self.width-1)
                (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(xform(f))
                self.canvas.create_line(x,start_y,x,end_y, \
                        fill="#%02x%02x%02x" % (int(255*r),int(255*g),int(255*b)))

##########################################################################
# `FunctionControl` class.
##########################################################################
class FunctionControl(tk.Frame):
    """Widget which displays a rectangular regions on which hue, sat, val
    or rgb values can be modified. An function control can have one or more
    attached color channels."""

    # Radius around a control point center in which we'd still count a
    # click as "clicked the control point"
    control_pt_click_tolerance = 4

    class Channel:
        def __init__(self, function_control, name, color_string,
                channel_index, channel_mode):
            """arguments documented in function body"""
            self.control = function_control  #owning function control
            self.name = name #'r','g','b','h','s','v' or 'a'
            self.color_string = color_string
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
            return min(1.0, max(0.0, 1.0 - float(y-1)/(self.control.height-1)))

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
            y will be set to the color channel of Color that ``*self`` represents."""
            self.set_value( color, self.get_index_value(y) )

        def get_pos_index(self,f):
            """Return x-index for gradient position f in [0..1]"""
            return int(f*(self.control.width-1))

        def get_index_pos(self,idx):
            """Return gradient position f in [0..1] for x-index Idx in
            [0..ControlWidth-1]"""
            return (1.0*idx)/(self.control.width-1)

        def paint(self, canvas):
            """Paint current channel into Canvas (a canvas of a function control
            object).

            Contents of the canvas are not deleted prior to painting,
            so more than one channel can be painted into the same canvas."""
            table = self.control.table
            # only control points which are active for the current channel
            # are to be painted. filter them out.
            relevant_control_points = [
                x for x in table.control_points \
                if self.name in x.active_channels
            ]
            # lines between control points
            for k in range( len(relevant_control_points) - 1 ):
                cur_point = relevant_control_points[k]
                next_point = relevant_control_points[1+k]

                canvas.create_line( self.get_pos_index(cur_point.pos),
                        self.get_value_index(cur_point.color),
                        self.get_pos_index(next_point.pos),
                        self.get_value_index(next_point.color),
                        fill = self.color_string  )
            # control points themself.
            for control_point in relevant_control_points:
                x = self.get_pos_index( control_point.pos )
                y = self.get_value_index( control_point.color )
                radius = 3
                canvas.create_rectangle( x - radius, y - radius, x + radius,
                    y + radius, outline = '#000000' )

    def __init__(self, master, gradient_table, color_space, width, height,
            on_table_changed = None ):
        tk.Frame.__init__(self, master, borderwidth=2, relief='groove')
        """Initialize a function control widget on tkframe master.

        input:
        OnTableChanged: Callback function taking a bool argument of meaning
            'FinalUpdate'. FinalUpdate is true if a control point is dropped,
            created or removed and false if the update is due to a control point
            currently beeing dragged (but not yet dropped)
        ColorSpace: String which specifies the channels painted on this control.
             May be any combination of h,s,v,r,g,b,a in which each channel
             occurs only once."""
        self.on_table_changed = on_table_changed
        self.table = gradient_table
        self.width = width
        self.height = height

        self.gradient_table = gradient_table
        self.canvas = tk.Canvas(self, background="white", \
            width=self.width, height=self.height)
        self.canvas.pack()
        self.channels = []

        # add the channels
        Channel = FunctionControl.Channel
        for c in color_space:
            if c == 'r':
                self.channels += [Channel(self, "r", "red", 0, 'rgb' )]
            elif c == 'g':
                self.channels += [Channel(self, "g", "green", 1, 'rgb' )]
            elif c == 'b':
                self.channels += [Channel(self, "b", "blue", 2, 'rgb' )]
            elif c == 'v':
                self.channels += [Channel(self, "v", "#7f7f7f", 2, 'hsv' )]
            elif c == 'h':
                self.channels += [Channel(self, "h", "#ff0000", 0, 'hsv' )]
            elif c == 's':
                self.channels += [Channel(self, "s", "#ffafaf", 1, 'hsv' )]
            elif c == 'a':
                self.channels += [Channel(self, "a", "#000000", 3, 'hsv' )]

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

        self.canvas.bind( "<ButtonRelease-1>", self.on_left_button_up )
        self.canvas.bind( "<Button-1>", self.on_left_button_down )
        self.canvas.bind( "<ButtonRelease-3>", self.on_right_button_up )
        self.canvas.bind( "<Button-3>", self.on_right_button_down )
        self.canvas.bind( "<Motion>", self.on_mouse_move )

        self.cur_drag = None #<- [channel,control_point] while something is dragged.

    def update(self):
        """Repaint the control."""
        canvas = self.canvas # shortcut...
        canvas.delete(tk.ALL)

        for channel in self.channels:
            channel.paint(self.canvas)

    def find_control_point(self, x, y):
        """Check if a control point lies near (x,y) or near x if y is None.
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
                if ( y_ is None ):
                    y_ = point_y
                if ( (point_x-x)**2 + (point_y-y_)**2 <= self.control_pt_click_tolerance**2 ):
                    return [channel, control_point]
        return None

    def on_left_button_down(self, event):
        self.cur_drag = self.find_control_point( event.x, event.y )

    def on_left_button_up(self, event):
        if self.cur_drag:
            self.table_config_changed( final_update = True )
            self.cur_drag = None

    def on_right_button_down(self, event):
        pass

    def table_config_changed(self, final_update):
        """Called internally in the control if the configuration of the attached
        gradient table has changed due to actions of this control.

        Forwards the update/change notice."""
        self.table.update()
        if self.on_table_changed:
            self.on_table_changed(final_update)
        else:
            self.update()

    def on_right_button_up(self, event):
        # toggle control point. check if there is a control point
        # under the mouse. If yes, delete it, if not, create one
        # at that point.
        cur_control_point = self.find_control_point(event.x, None)
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
            new_control_point.set_pos(self.channels[0].get_index_pos(event.x))

            # set new control point color to the color currently present
            # at its designated position
            new_control_point.color = self.table.get_pos_color(new_control_point.pos)

            self.table.insert_control_point( new_control_point )
            self.table_config_changed( final_update = True )

    def on_mouse_move(self, event):
        # currently dragging a control point?
        if self.cur_drag:
            channel = self.cur_drag[0]
            point = self.cur_drag[1]
            if ( not point.fixed ):
                point.set_pos( channel.get_index_pos(event.x) )
                point.activate_channels( self.active_channels_string )
                self.table.sort_control_points()
            channel.set_value_index( point.color, event.y )
            self.table_config_changed( final_update = False )


##########################################################################
# `GradientEditor` class.
##########################################################################
class GradientEditor(tk.Toplevel):
    """The gradient editor window, i.e. the thing that contains the gradient
    display, the function controls and the buttons."""
    def __init__(self, master, vtk_table, on_change_color_table = None):
        """Initialize the gradient editor window.

        Parameters
        ----------
        master
            Owning widget, for example a tk root object.
        VtkTable
            Instance of vtkLookupTable, designating the table which is
            to be edited.
        OnChangeColorTable
            Callback function taking no arguments. Called
            when the color table was changed and rendering is requested."""

        # Inner dimensions of the color control gui-elements in pixels.
        gradient_preview_width = 300
        gradient_preview_height = 50
        channel_function_width = gradient_preview_width
        channel_function_height = 80

        tk.Toplevel.__init__(self, master)
        self.title("Color Gradient Editor")
        self.minsize( gradient_preview_width+4, gradient_preview_height + 5 * \
                      channel_function_height + 50 )

        self.gradient_table = GradientTable(gradient_preview_width)
        self.vtk_color_table = vtk_table

        # create controls.
        self.gradient_control = GradientControl(self, self.gradient_table,
                                                gradient_preview_width,
                                                gradient_preview_height )
        self.gradient_control.grid(row=0,column=1,sticky="we")

        def on_gradient_table_changed( final_update ):
            # update all function controls.
            self.function_control_rgb.update()
            for control in self.function_controls_hsv:
                control.update()
            # repaint the gradient display or the external windows only
            # when the instant*** options are set or when the update was final.
            if final_update or ( 1 == self.show_instant_gradients.get() ):
                self.gradient_control.update()

            if final_update or ( 1 == self.show_instant_feedback.get() ):
                self.gradient_table.store_to_vtk_lookup_table( self.vtk_color_table )
                on_change_color_table()
        self.on_gradient_table_changed = on_gradient_table_changed

        self.function_control_rgb = FunctionControl(self, self.gradient_table,
                "rgb", channel_function_width, channel_function_height,
                on_gradient_table_changed)
        label = tk.Label( self, text = "rgb" )
        label.grid(row=1, column=0)
        self.function_control_rgb.grid(row=1,column=1,sticky="we")
        self.function_controls_hsv = []
        for it in [("hue",2), ("sat",3), ("val",4), ("alp", 5) ]:
            control = FunctionControl(self, self.gradient_table,
                it[0][0], channel_function_width, channel_function_height,
                on_gradient_table_changed )
            control.grid(row=it[1],column=1,sticky="we")
            self.function_controls_hsv.append(control)

            label = tk.Label( self, text = it[0] )
            label.grid(row=it[1], column=0)

        # buttons and the instruction label get into an own subframe for
        # easier control.
        button_frame = tk.Frame(self)
        button_frame.grid(row=6,column=0,columnspan=2)

        ok_button = tk.Button(button_frame, text="ok", command=self.ok)
        ok_button.grid(row=0,column=1)
        #CancelButton = tk.Button(ButtonFrame, text="cancel", command=self.Cancel)
        #CancelButton.grid(row=0,column=2)
        spacer = tk.Frame(button_frame, width=10 )
        spacer.grid(row=0,column=3)
        save_button = tk.Button(button_frame, text="save", command=self.save_gradient)
        save_button.grid(row=0,column=4)
        load_button = tk.Button(button_frame, text="load", command=self.load_gradient)
        load_button.grid(row=0,column=5)
        spacer = tk.Frame(button_frame, width=10 )
        spacer.grid(row=0,column=6)
        label = tk.Label(button_frame,text="instant:")
        label.grid(row=0,column=7)

        # these two buttons control whether gradient and render target
        # updates are executed during movement of control points or
        # only at the end of such changes.
        self.show_instant_gradients = tk.IntVar()
        self.show_instant_gradients.set(1) # enable instant gradients by default
        self.show_instant_feedback = tk.IntVar()
        self.show_instant_feedback.set(0) # disable instant feedback by default
        instant_gradient_button = tk.Checkbutton(button_frame, text="grad")
        instant_gradient_button.grid(row=0,column=8)
        instant_gradient_button.configure(variable=self.show_instant_gradients)
        instant_feedback_button = tk.Checkbutton(button_frame, text="feed")
        instant_feedback_button.grid(row=0,column=9)
        instant_feedback_button.configure(variable=self.show_instant_feedback)

        instruction_label = tk.Label(button_frame,
                text="left button: move point; right click: toggle point")
        instruction_label.grid(column=0,columnspan=9,row=1)

        # insert a ratio button which decides whether the controls for nonlinear
        # scaling of the gradient are shown and activated.
        self.nonlinear_scaling_enabled = tk.IntVar()
        self.nonlinear_scaling_enabled.set(0)
        nonlinear_enabled_button = tk.Checkbutton(button_frame, text="nonlin")
        nonlinear_enabled_button.grid(column=9,row=1)
        nonlinear_enabled_button.configure(variable=self.nonlinear_scaling_enabled,
            command=self.nonlinear_scaling_option_changed)

        # the controls for the nonlinear scaling also get into an own frame.
        # this one can be shown or hidden when the "nonlin"-button is pressed
        nonlin_frame = tk.Frame(self)
        self.nonlin_frame = nonlin_frame

        label = tk.Label(nonlin_frame, text="f(x) =")
        label.grid(row=0, column=0)
        self.nonlinear_function_string = tk.StringVar()
        self.nonlinear_function_string.set( "x**(4*a)" )
        function_edit = tk.Entry(nonlin_frame, width=35,
            textvariable=self.nonlinear_function_string)
        function_edit.bind("<Return>", self.nonlinear_function_string_changed )
        function_edit.grid(row=0, column=1)

        label = tk.Label(nonlin_frame, text="param a:")
        label.grid(row=1, column=0)
        self.parameter_scale = tk.Scale(nonlin_frame, from_=0.0, to=1.0,
            resolution=0.001, length=250, orient="horizontal")
        self.parameter_scale.bind("<ButtonRelease>",
            lambda event: self.nonlinear_parameter_scale_changed(final_update=True))
        self.parameter_scale.bind("<Motion>",
            lambda event:self.nonlinear_parameter_scale_changed(final_update=False))
        self.parameter_scale.set(0.5)
        self.parameter_scale.grid(row=1, column=1)
        label = tk.Label(nonlin_frame, text= \
                "f(x) should map [0..1] to [0..1]. It rescales the gradient.")
        label.grid(column=0,columnspan=2,row=2)

        # finally, write the current gradient out into main program
        on_gradient_table_changed(final_update = True)

    def nonlinear_scaling_option_changed(self):
        """called when the 'nonlin'-button is pressed to toggle if nonlinear-
        scaling is activated and the corresponding controls are shown"""
        if ( 1 == self.nonlinear_scaling_enabled.get() ):
            # activate the nonlinear scaling controls
            self.nonlin_frame.grid(row=7,column=0,columnspan=2)
            self.nonlinear_parameter_scale_changed(final_update=False)
            self.nonlinear_function_string_changed(None)
        else:
            # disable the nonlinear scaling controls (and the scaling)
            self.nonlin_frame.pack(side=tk.LEFT, anchor=tk.NW)
            self.nonlin_frame.pack_forget()
            self.gradient_table.set_scaling_function("")
            self.on_gradient_table_changed(final_update=True)

    def nonlinear_parameter_scale_changed(self,final_update):
        """Event Handler for the nonlinear-parameter scaling bar. FinalUpdate
        is true on ButtonRelease and False on Motion"""
        self.gradient_table.set_scaling_function_parameter(self.parameter_scale.get())
        self.on_gradient_table_changed(final_update = final_update)

    def nonlinear_function_string_changed(self,event):
        """Invoked when Return is pressed in the nonlinear-function edit"""
        self.gradient_table.set_scaling_function(self.nonlinear_function_string.get())
        self.on_gradient_table_changed(final_update = True)

    def ok(self):
        self.destroy()

    def save_gradient(self):
        filetypes = [("Gradient Files","*.grad"),("All Files","*")]
        file_name = tkFileDialog.asksaveasfilename(defaultextension=".grad",
                                                   filetypes=filetypes)
        if file_name:
            # there is probably a way to find out which file type the user
            # actually selected. But since I don't know it and also don't really
            # know how to find it out, i rely on this error prone method...
            if ( ".lut" == file_name[len(file_name)-4:] ):
                self.gradient_table.save(file_name)
            self.gradient_table.save(file_name)

    def load_gradient(self):
        filetypes = [("Gradient Files","*.grad"), ("All Files","*")]
        file_name = tkFileDialog.askopenfilename(defaultextension=".grad",
                                                 filetypes=filetypes)
        if file_name:
            self.gradient_table.load(file_name)
            self.on_gradient_table_changed(final_update = True)
            if self.gradient_table.scaling_function:
                self.parameter_scale.set(self.gradient_table.scaling_function_parameter)
                self.nonlinear_function_string.set(self.gradient_table.scaling_function_string)
                self.nonlinear_scaling_enabled.set(1)
                self.nonlinear_scaling_option_changed()
            else:
                self.nonlinear_scaling_enabled.set(0)
                self.nonlinear_scaling_option_changed()



if __name__ == "__main__":
    # prepare a vtk window with an actor for visible feedback. Don't be
    # be scared, the actual gradient editor code is only 3 lines long,
    # the rest is setup of the scene.
    from tvtk.api import tvtk
    import vtk
    from vtk.tk import vtkTkRenderWidget
    from math import cos
    root = tk.Tk()
    root.minsize(520,520)
    render_frame = tk.Frame(root)
    render_frame.pack()
    render_widget = vtkTkRenderWidget.vtkTkRenderWidget(render_frame,
                                                        width=512, height=512 )
    render_widget.pack(side=tk.BOTTOM,expand='true',fill='both')
    render_window = render_widget.GetRenderWindow()
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.2,0.2,0.4)
    render_window.AddRenderer(renderer)

    image_data = vtk.vtkImageData()
    N = 72
    image_data.SetDimensions(N,N,1)
    try:
        method = image_data.SetScalarComponentFromFloat
    except AttributeError:
        method = image_data.SetScalarComponentFromDouble
    for i in range(N):
        for j in range(N):
            a = float(i)/N
            b = float(j)/N
            v = 0.5 + 0.5*cos(13*a)*cos(8*b+3*a*a)
            v = v**2
            method(i,j,0,0,v)
    geometry_filter = vtk.vtkImageDataGeometryFilter()
    geometry_filter.SetInput(image_data)
    warp = vtk.vtkWarpScalar()
    warp.SetInput(geometry_filter.GetOutput())
    warp.SetScaleFactor(8.1)
    normal_filter = vtk.vtkPolyDataNormals()
    normal_filter.SetInput(warp.GetOutput())
    data_mapper = vtk.vtkDataSetMapper()
    data_mapper.SetInput(normal_filter.GetOutput())
    data_actor = vtk.vtkActor()
    data_actor.SetMapper(data_mapper)
    renderer.AddActor(data_actor)

    table = vtk.vtkLookupTable()
    data_mapper.SetLookupTable(table)

    # the actual gradient editor code.
    def on_color_table_changed():
        render_window.Render()

    # Gradient editor only works with tvtk objects, so convert the lut
    # to a tvtk version.
    tvtk_table = tvtk.to_tvtk(table)
    editor = GradientEditor(root, tvtk_table, on_color_table_changed)

    root.mainloop()
