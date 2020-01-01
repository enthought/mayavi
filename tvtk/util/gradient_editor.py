""" The common code for a gradient editor for `tvtk.LookupTables` and
`tvtk.VolumeProperty` color transfer functions.  Most of the code is
independent of tvtk however.

The toolkit specific code is in toolkit specific files.  This code is
distributed under the conditions of the BSD license.

This code was originally written by Gerald Knizia <cgk.d@gmx.net> and
later modified by Prabhu Ramachandran for tvtk and MayaVi2.

Copyright (c) 2005-2020, Gerald Knizia and Prabhu Ramachandran
"""

from os.path import splitext

from tvtk.api import tvtk


##########################################################################
# Utility functions.
##########################################################################
def lerp(arg0,arg1,f):
    """linearly interpolate between arguments arg0 and arg1.

       The weight f is from [0..1], with f=0 giving arg0 and f=1 giving arg1"""
    return (1-f)*arg0 + f*arg1

def rgba_to_hsva(r,g,b,a):
    """Convert color from RGBA to HSVA.

    input: r,g,b,a are from [0..1]
    output: h,s,v,a are from [0..1] (h will never be 1.0)

    See http://en.wikipedia.org/wiki/HSV_color_space
    Only difference: hue range is [0..1) here, not [0..360)."""
    max_comp = max((r,g,b))
    min_comp = min((r,g,b))
    h = 1.0/6.0 #60.0
    if ( max_comp != min_comp ):
        if ( r >= g) and ( r >= b ):
            h *= 0 + (g-b)/(max_comp-min_comp)
        elif ( g >= b ):
            h *= 2 + (b-r)/(max_comp-min_comp)
        else:
            h *= 4 + (r-g)/(max_comp-min_comp)
    if h < 0:
            h += 1.0
    if h > 1.0:
            h -= 1.0
    if ( max_comp != 0 ):
        s = ( max_comp - min_comp )/max_comp
    else:
        s = 0
    v = max_comp
    return (h,s,v,a)

def hsva_to_rgba(h_,s,v,a):
    """Convert color from HSVA to RGBA.

    input: h,s,v,a are from [0..1]
    output: r,g,b,a are from [0..1]

    See http://en.wikipedia.org/wiki/HSV_color_space
    Only difference: hue range is [0..1) here, not [0..360)."""
    (r,g,b,a) = (v,v,v,a)
    h = h_ * 360.0
    if ( s < 1e-4 ):
        return (r,g,b,a)#zero saturation -> color acromatic
    hue_slice_index = int(h/60.0)
    hue_partial = h/60.0 - hue_slice_index
    p = v * ( 1 - s )
    q = v * ( 1 - hue_partial * s )
    t = v * ( 1 - (1-hue_partial) * s )
    if ( 0 == hue_slice_index ):
        r, g, b = v, t, p
    elif ( 1 == hue_slice_index ):
        r, g, b = q, v, p
    elif ( 2 == hue_slice_index ):
        r, g, b = p, v, t
    elif ( 3 == hue_slice_index ):
        r, g, b = p, q, v
    elif ( 4 == hue_slice_index ):
        r, g, b = t, p, v
    elif ( 5 == hue_slice_index ):
        r, g, b = v, p, q
    return (r,g,b,a)


##########################################################################
# `Color` class.
##########################################################################
class Color:
    """Represents a color and provides means of automatic conversion between
    HSV(A) and RGB(A) color spaces. The color is stored in HSVA space."""
    def __init__(self):
        self.hsva = (0.0, 0.0, 0.5, 1.0)

    def set_rgb(self,r,g,b):
        self.set_rgba(r,g,b,1.0)

    def set_rgba(self,r,g,b,a):
        self.hsva = rgba_to_hsva(r,g,b,a)

    def get_rgb255(self):
        """returns a tuple (r,g,b) of 3 integers in range [0..255] representing
        the color."""
        rgba = self.get_rgba()
        return (int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255) )

    def get_rgba(self):
        h,s,v,a = self.hsva
        return hsva_to_rgba(h,s,v,a)

    def get_hsva(self):
        return self.hsva

    def set_hsva(self,h,s,v,a):
        self.hsva = (h,s,v,a)

    def set_lerp(self, f,A,B):
        """Set self to result of linear interpolation between colors A and
           B in HSVA space.

           The weight f is from [0..1], with f=0 giving A and f=1 giving
           color B."""
        h = lerp(A.hsva[0], B.hsva[0], f)
        s = lerp(A.hsva[1], B.hsva[1], f)
        v = lerp(A.hsva[2], B.hsva[2], f)
        a = lerp(A.hsva[3], B.hsva[3], f)
        self.hsva = (h,s,v,a)


##########################################################################
# `ColorControlPoint` class.
##########################################################################
class ColorControlPoint:
    """A control point represents a fixed position in the gradient
    and its assigned color. A control point can have indifferent
    color channels in hsv space, i.e. channels, on which its
    presence does not impose any effect."""
    def __init__(self, active_channels, fixed=False):
        self.color = Color()
        # position in the gradient table. range: [0..1].
        self.pos = 0.0
        # fixed control points can not be moved to other positions. The
        # control points for the begin and the end of the gradient are usually
        # the only fixed control points.
        self.fixed = fixed

        if ( 'a' != active_channels ):
            self.active_channels = "rgb"
            self.activate_channels(active_channels)
        else:
            self.active_channels = "a"

    def activate_channels(self,new_channels):
        """NewChannels: string consisting of the new color channel names"""
        for c in new_channels:
            if ( not ( c in self.active_channels ) ):
                self.active_channels += c

    def set_pos(self,f):
        self.pos = max(min(f,1.0), 0.0)


##########################################################################
# `GradientTable` class.
##########################################################################
class GradientTable:
    """this class represents a logical gradient table, i.e. an array
    of colors and the means to control it via control points

    This class (unlike the GradientTableOld) does not support scaling
    and uses VTK's ColorTransferFunction and PiecewiseFunction to
    perform the actual interpolation.
    """

    def __init__( self, num_entries ):
        self.size = num_entries
        self.table = tvtk.ColorTransferFunction()
        try:
            self.table.range = (0.0, 1.0)
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass

        self.alpha = tvtk.PiecewiseFunction()
        # These VTK classes perform the interpolation for us.

        # insert the control points for the left and the right end of the
        # gradient. These are fixed (i.e. cannot be moved or deleted) and
        # allow one to set begin and end colors.
        left_control_point = ColorControlPoint(fixed=True, active_channels="hsva")
        left_control_point.set_pos(0.0)
        left_control_point.color.set_rgb(0.0, 0.0, 0.0)
        right_control_point = ColorControlPoint(fixed=True, active_channels="hsva")
        right_control_point.set_pos(1.0)
        right_control_point.color.set_rgb(1.0, 1.0, 1.0)
        self.control_points = [left_control_point, right_control_point]
        # note: The array of control points always has to be sorted by gradient
        # position of the control points.

        # insert another control point. This one has no real function, it
        # is just there to make the gradient editor more colorful initially
        # and suggest to the (first time user) that it is actually possible to
        # place more control points.
        mid_control_point = ColorControlPoint(active_channels="hsv")
        mid_control_point.set_pos(0.4)
        mid_control_point.color.set_rgb(1.0,0.4,0.0)
        self.insert_control_point( mid_control_point )

        # These variables are only for compatibility with GradientTableOld.
        self.scaling_function_string = ""  # will receive the function string if
                                           # set, e.g. "x**(4*a)"

        self.scaling_function_parameter = 0.5 # the parameter a, slider controlled
        self.scaling_function = None      # the actual function object. takes one
                                          # position parameter. None if disabled.

        self.update()

    def get_color_hsva(self, f):
        """return (h,s,v,a) tuple in self.table_hsva for fraction f in
        [0,1]."""
        r, g, b = self.table.get_color(f)
        a = self.alpha.get_value(f)
        return rgba_to_hsva(r, g, b, a)

    def get_color(self, f):
        """return (r,g,b,a) tuple in self.table for fraction f in
        [0,1]."""
        r, g, b = self.table.get_color(f)
        a = self.alpha.get_value(f)
        return r, g, b, a

    def get_pos_color(self,f):
        r"""return a Color object representing the color which is lies at
        position f \in [0..1] in the current gradient"""
        result = Color()
        e = self.get_color_hsva(f)
        result.set_hsva(*e)
        return result

    def get_pos_rgba_color_lerped(self,f):
        r"""return a (r,g,b,a) color representing the color which is lies at
        position f \in [0..1] in the current gradient. if f is outside the
        [0..1] interval, the result will be clamped to this
        interval."""
        return self.get_color(f)

    def insert_control_point(self,new_point):
        """Insert a new control point into the table. Does sort the control
        points, but does NOT update the table."""
        self.control_points += [new_point]
        self.sort_control_points()

    def sort_control_points(self):
        """Sort control points by position. Call this if the position of
        any control point was changed externally. The control point array
        always has to be sorted."""
        self.control_points.sort(key=lambda x: x.pos)

    def update(self):
        """Recalculate the gradient table from the control points. The
        colors are interpolated linearly between each two control
        points in hsva space.
        """
        #self.sort_control_points()

        table = self.table
        alpha = self.alpha
        table.remove_all_points()
        alpha.remove_all_points()
        for point in self.control_points:
            x = point.pos
            h, s, v, a = point.color.get_hsva()
            if point.active_channels != 'a':
                table.add_hsv_point(x, h, s, v)
            if 'a' in point.active_channels:
                alpha.add_point(x, a)

    def store_to_vtk_lookup_table(self, vtk_table, num_entries=256):
        """Store current color table in `vtk_table`, an instance of
        `tvtk.LookupTable`.
        """
        vtk_table.number_of_table_values = num_entries
        for idx in range(num_entries):
            f = float(idx)/(num_entries-1)
            rgba = self.get_color(f)
            vtk_table.set_table_value( idx, rgba )

    def store_to_vtk_volume_prop(self, volume_prop, scalar_range):
        """Given a `tvtk.VolumeProperty` and a scalar range to map
        values into, this sets the CTF based on the current control
        points.
        """
        # FIXME: This method does not support scaling!
        ctf = volume_prop.rgb_transfer_function
        ctf.remove_all_points()
        otf = volume_prop.get_scalar_opacity()
        otf.remove_all_points()
        s1, s2 = scalar_range
        try:
            ctf.range = s1, s2
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass
        size = s2 - s1
        for point in self.control_points:
            x = s1 + point.pos*size
            h, s, v, a = point.color.get_hsva()
            if point.active_channels != 'a':
                ctf.add_hsv_point(x, h, s, v)
            if 'a' in point.active_channels:
                otf.add_point(x, a)

    def load_from_vtk_volume_prop(self, volume_prop):
        """Given a vtkVolumeProperty, this initializes the control
        points of the gradient table.  This works best when a
        ctf.ColorTransferFunction and PiecewiseFunction are used.

        Note that it is not as easy to setup the control points from a
        LUT because the LUT may end up having more than the size of
        the table editor here.  It also usually does not make sense to
        do this with a LUT.
        """
        # FIXME: This method does not support scaling!
        ctf = volume_prop.rgb_transfer_function
        otf = volume_prop.get_scalar_opacity()
        # We need a CTF with at least 2 points.
        size = ctf.size
        assert (size > 1)
        assert (otf.size > 1)
        s1, s2 = ctf.range
        scale = float(s2 - s1)
        ds = scale/(size -1)
        new_ctl_pts = []
        has_nodes = False
        if hasattr(ctf, 'nodes'):
            has_nodes = True
        _ctf_data = [0]*6
        for i in range(size):
            if has_nodes:
                x = ctf.nodes[i]
                r, g, b = ctf.get_color(x)
            else:
                ctf.get_node_value(i, _ctf_data)
                x, r, g, b = _ctf_data[:4]
            a = otf.get_value(x)
            if (i == 0) or (i == (size-1)):
                # First and last points are fixed.
                pt = ColorControlPoint(active_channels="hsva", fixed=True)
            else:
                pt = ColorControlPoint(active_channels="hsv", fixed=False)

            pt.color.set_rgba(r, g, b, a)
            pos = (x - s1)/scale
            pt.set_pos(pos)
            new_ctl_pts.append(pt)

        # The alpha values are indipendent of the hsv ones.
        size = otf.size
        ds = scale/(size -1)
        _otf_data = [0]*4
        has_nodes = False
        if hasattr(ctf, 'nodes'):
            has_nodes = True
        for i in range(1, size-1):
            if has_nodes:
                x = otf.nodes[i]
            else:
                otf.get_node_value(i, _otf_data)
                x, a = _otf_data[:2]
            r, g, b = ctf.get_color(x)
            pt = ColorControlPoint(active_channels="a", fixed=False)
            pt.color.set_rgba(r, g, b, a)
            pos = (x - s1)/scale
            pt.set_pos(pos)
            new_ctl_pts.append(pt)

        self.control_points = new_ctl_pts
        self.sort_control_points()
        self.update()

    def scaling_parameters_changed(self):
        """Recompile the scaling function."""
        raise NotImplementedError

    def set_scaling_function_parameter(self,new_parameter):
        """Set the 'a' parameter of the scaling function"""
        raise NotImplementedError

    def set_scaling_function(self,new_function_string):
        """Set scaling function. new_function_string is a string describing the
        function, e.g. 'x**(4*a)' """
        raise NotImplementedError

    def save(self, file_name):
        """Save control point set into a new file FileName. It is not checked
        whether the file already exists. Further writes out a VTK .lut file
        and a .jpg file showing the gradients."""

        # Ensure that if the input file name had one of the extensions
        # we'll be writing out ourselves, it gets stripped out first.
        path_base,ext = splitext(file_name)
        #print(file_name)
        if ext.lower() in ['.lut','.jpg','.jpeg','.grad']:
            ext = ''
        file_name = path_base  + ext

        # Create the three names for the files we'll be actually
        # writing out.
        file_name_grad = file_name + '.grad'
        file_name_lut = file_name + '.lut'
        file_name_jpg = file_name + '.jpg'

        # write control points set.
        file = open( file_name_grad, "w" )
        file.write( "V 2.0 Color Gradient File\n" )
        file.write( "ScalingFunction: %s\n" % (self.scaling_function_string) )
        file.write( "ScalingParameter: %s\n" % (self.scaling_function_parameter) )
        file.write( "ControlPoints: (pos fixed bindings h s v a)\n" )
        for control_point in self.control_points:
            file.write( "  %s %s %s %s %s %s %s\n" % ( \
                control_point.pos, control_point.fixed, control_point.active_channels,
                control_point.color.get_hsva()[0], control_point.color.get_hsva()[1],
                control_point.color.get_hsva()[2], control_point.color.get_hsva()[3] ) )
        file.close()

        # write vtk lookup table. Unfortunatelly these objects don't seem to
        # have any built in and exposed means of loading or saving them, so
        # we build the vtk file directly
        vtk_table = tvtk.LookupTable()
        self.store_to_vtk_lookup_table(vtk_table)
        file = open( file_name_lut, "w" )
        num_colors = vtk_table.number_of_table_values
        file.write( "LOOKUP_TABLE UnnamedTable %s\n" % ( num_colors ) )
        for idx in range(num_colors):
            entry = vtk_table.get_table_value(idx)
            file.write("%.4f %.4f %.4f %.4f\n" % (entry[0],entry[1],entry[2],entry[3]))
        file.close()

        # if the python image library is aviable, also generate a small .jpg
        # file showing how the gradient looks. Based on code from Arnd Baecker.
        try:
            import Image
        except ImportError:
            pass  # we're ready otherwise. no jpg output tho.
        else:
            Ny=64  # vertical size of the jpeg
            im = Image.new("RGBA",(num_colors,Ny))
            for nx in range(num_colors):
                (r,g,b,a) = vtk_table.get_table_value(nx)
                for ny in range(Ny):
                    im.putpixel((nx,ny),(int(255*r),int(255*g),int(255*b),
                                         int(255*a)))
            im.save(file_name_jpg,"JPEG")
            # it might be better to store the gradient as .png file, as these
            # are actually able to store alpha components (unlike jpg files)
            # and might also lead to a better compression.

    def load(self, file_name):
        """Load control point set from file FileName and recalculate gradient
        table."""
        file = open( file_name, "r" )
        version_tag = file.readline()
        version = float(version_tag.split()[1])+1e-5
        if ( version >= 1.1 ):
            # read in the scaling function and the scaling function parameter
            function_line_split = file.readline().split()
            parameter_line = file.readline()
            if ( len(function_line_split)==2 ):
                self.scaling_function_string = function_line_split[1]
            else:
                self.scaling_function_string = ""
            self.scaling_function_parameter = float(parameter_line.split()[1])
        else:
            self.scaling_function_string = ""
            self.scaling_function_parameter = 0.5
        file.readline()
        new_control_points = []
        while True:
            cur_line = file.readline()
            if len(cur_line) == 0:
                # readline is supposed to return an empty string at EOF
                break
            args = cur_line.split()
            if ( len(args) < 7 ):
                msg = "gradient file format broken at line:\n"
                msg += cur_line
                raise ValueError(msg)
            new_point = ColorControlPoint(active_channels="")
            new_point.set_pos( float( args[0] ) )
            new_point.fixed = "True" == args[1] #bool( args[1] )
            new_point.active_channels = args[2]
            (h,s,v,a) = ( float(args[3]), float(args[4]),
                          float(args[5]), float(args[6]) )
            new_point.color.set_hsva(h,s,v,a)
            new_control_points.append(new_point)
        file.close()
        self.control_points = new_control_points
        self.sort_control_points()
        #self.scaling_parameters_changed()
        self.update()



##########################################################################
# `ChannelBase` class.
##########################################################################
class ChannelBase(object):
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

    def paint(self, painter):
        """Paint current channel into Canvas (a canvas of a function control
        object).

        This should be overridden to do the actual painting.

        """
        raise NotImplementedError

##########################################################################
# `FunctionControl` class.
##########################################################################
class FunctionControl(object):
    """Widget which displays a rectangular regions on which hue, sat, val
    or rgb values can be modified. An function control can have one or more
    attached color channels."""

    # Radius around a control point center in which we'd still count a
    # click as "clicked the control point"
    control_pt_click_tolerance = 4

    ChannelFactory = ChannelBase

    def __init__(self, master=None, gradient_table=None, color_space=None,
                 width=100, height=100):
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
        self.text_map = {'r': 'RED', 'g': 'GREEN', 'b': 'BLUE',
                         'h': 'HUE', 's': 'SATURATION', 'v': 'VALUE',
                         'a': 'ALPHA'}
        self.master = master
        self.table = gradient_table
        self.gradient_table = gradient_table
        self.width = width
        self.height = height

        self.channels = []

        # add the channels
        Channel = self.ChannelFactory
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
        # explicitly means that h, s and v all have to be fixed.
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

        # need to set to "None" initially or event handlers get confused.
        self.cur_drag = None #<- [channel,control_point] while something is dragged.

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

    def table_config_changed(self, final_update):
        """Called internally in the control if the configuration of the attached
        gradient table has changed due to actions of this control.

        Forwards the update/change notice."""
        self.table.update()
        self.master.on_gradient_table_changed(final_update)

    ######################################################################
    # Toolkit specific event methods.
    # Look at wx_gradient_editor.py and qt_gradient_editor.py to see
    # the methods that are necessary.
    ######################################################################


##########################################################################
# `AbstractGradientEditor` interface.
##########################################################################
class AbstractGradientEditor(object):
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
# `GradientEditorWidget` interface.
##########################################################################
class GradientEditorWidget(AbstractGradientEditor):
    """A Gradient Editor widget that can be used anywhere.
    """
    def __init__(self, master=None, vtk_table=None,
                 on_change_color_table=None, colors=None):
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
        if colors is None:
            colors = ['rgb', 'hsv', 'a']
        self.colors = colors
        self.gradient_preview_width = 300
        self.gradient_preview_height = 50
        self.channel_function_width = self.gradient_preview_width
        self.channel_function_height = 80
        self.gradient_table = GradientTable(self.gradient_preview_width)
        self.vtk_color_table = vtk_table
        if isinstance(vtk_table, tvtk.LookupTable):
            self.vtk_table_is_lut = True
        else:
            # This is a tvtk.VolumeProperty
            self.vtk_table_is_lut = False
            # Initialize the editor with the volume property.
            self.gradient_table.load_from_vtk_volume_prop(vtk_table)

        self.on_change_color_table = on_change_color_table

        # Add the function controls:
        self.function_controls = []

        self.tooltip_text = 'Left click: move control points\n'\
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
        self.editor_data = editor_data

    ######################################################################
    # `GradientEditorWidget` interface.
    ######################################################################
    def set_status_text(self, msg):
        raise NotImplementedError

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
