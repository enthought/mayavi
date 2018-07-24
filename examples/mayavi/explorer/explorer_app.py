# This code simulates something the user would like to do.  In this
# case the code allows a user to create a 3D cube of data (a numpy
# array), specify an equation for the scalars and view it using the
# mayavi plugin.  The only "envisage bits" are the code that let one
# grab the running mayavi instance and script it.  The application
# trait is set by Envisage and we use the application to get hold of
# the mayavi engine.  Then we show the data once the mayavi engine has
# started.

# Standard library imports.
import numpy as np

# Enthought library imports
from traits.api import HasTraits, Button, Instance, \
     Any, Str, Array
from traitsui.api import Item, View, TextEditor


######################################################################
# `Explorer3D` class.
######################################################################
class Explorer3D(HasTraits):
    """This class basically allows you to create a 3D cube of data (a
    numpy array), specify an equation for the scalars and view it
    using the mayavi plugin.
    """

    ########################################
    # Traits.

    # Set by envisage when this is offered as a service offer.
    window = Instance('pyface.workbench.api.WorkbenchWindow')

    # The equation that generates the scalar field.
    equation = Str('sin(x*y*z)/(x*y*z)',
                   desc='equation to evaluate (enter to set)',
                   auto_set=False,
                   enter_set=True)

    # Dimensions of the cube of data.
    dimensions = Array(value=(128, 128, 128),
                       dtype=int,
                       shape=(3,),
                       cols=1,
                       labels=['nx', 'ny', 'nz'],
                       desc='the array dimensions')

    # The volume of interest (VOI).
    volume = Array(dtype=float,
                   value=(-5,5,-5,5,-5,5),
                   shape=(6,),
                   cols=2,
                   labels=['xmin','xmax','ymin','ymax','zmin','zmax'],
                   desc='the volume of interest')

    # Clicking this button resets the data with the new dimensions and
    # VOI.
    update_data = Button('Update data')

    ########################################
    # Private traits.
    # Our data source.
    _x = Array
    _y = Array
    _z = Array
    data = Array
    source = Any
    _ipw1 = Any
    _ipw2 = Any
    _ipw3 = Any

    ########################################
    # Our UI view.
    view = View(Item('equation', editor=TextEditor(auto_set=False,
                                                   enter_set=True)),
                Item('dimensions'),
                Item('volume'),
                Item('update_data', show_label=False),
                resizable=True,
                scrollable=True,
                )

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(Explorer3D, self).__init__(**traits)
        # Make some default data.
        if len(self.data) == 0:
            self._make_data()
        # Note: to show the visualization by default we must wait till
        # the mayavi engine has started.  To do this we hook into the
        # mayavi engine's started event and setup our visualization.
        # Now, when this object is constructed (i.e. when this method
        # is invoked), the services are not running yet and our own
        # application instance has not been set.  So we can't even
        # get hold of the mayavi instance.  So, we do the hooking up
        # when our application instance is set by listening for
        # changes to our application trait.

    def get_mayavi(self):
        from mayavi.plugins.script import Script
        return self.window.get_service(Script)

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _make_data(self):
        dims = self.dimensions.tolist()
        np = dims[0]*dims[1]*dims[2]
        xmin, xmax, ymin, ymax, zmin, zmax = self.volume
        x, y, z = np.ogrid[xmin:xmax:dims[0]*1j,
                           ymin:ymax:dims[1]*1j,
                           zmin:zmax:dims[2]*1j]
        self._x = x.astype('f')
        self._y = y.astype('f')
        self._z = z.astype('f')
        self._equation_changed('', self.equation)

    def _show_data(self):
        if self.source is not None:
            return
        mayavi = self.get_mayavi()
        if mayavi.engine.current_scene is None:
            mayavi.new_scene()
        from mayavi.sources.array_source import ArraySource
        vol = self.volume
        origin = vol[::2]
        spacing = (vol[1::2] - origin)/(self.dimensions -1)
        src = ArraySource(transpose_input_array=False,
                          scalar_data=self.data,
                          origin=origin,
                          spacing=spacing)
        self.source = src
        mayavi.add_source(src)

        from mayavi.modules.outline import Outline
        from mayavi.modules.image_plane_widget import ImagePlaneWidget
        from mayavi.modules.axes import Axes
        # Visualize the data.
        o = Outline()
        mayavi.add_module(o)
        a = Axes()
        mayavi.add_module(a)
        self._ipw1 = ipw = ImagePlaneWidget()
        mayavi.add_module(ipw)
        ipw.module_manager.scalar_lut_manager.show_scalar_bar = True

        self._ipw2 = ipw_y = ImagePlaneWidget()
        mayavi.add_module(ipw_y)
        ipw_y.ipw.plane_orientation = 'y_axes'

        self._ipw3 = ipw_z = ImagePlaneWidget()
        mayavi.add_module(ipw_z)
        ipw_z.ipw.plane_orientation = 'z_axes'

    ######################################################################
    # Traits static event handlers.
    ######################################################################
    def _equation_changed(self, old, new):
        try:
            g = np.__dict__
            s = eval(new, g, {'x':self._x,
                              'y':self._y,
                              'z':self._z})
            # The copy makes the data contiguous and the transpose
            # makes it suitable for display via tvtk.
            s = s.transpose().copy()
            # Reshaping the array is needed since the transpose
            # messes up the dimensions of the data.  The scalars
            # themselves are ravel'd and used internally by VTK so the
            # dimension does not matter for the scalars.
            s.shape = s.shape[::-1]
            self.data = s
        except:
            pass

    def _dimensions_changed(self):
        """This does nothing and only changes to update_data do
        anything.
        """
        return

    def _volume_changed(self):
        return

    def _update_data_fired(self):
        self._make_data()
        src = self.source
        if src is not None:
            vol = self.volume
            origin = vol[::2]
            spacing = (vol[1::2] - origin)/(self.dimensions -1)
            # Set the source spacing and origin.
            src.trait_set(spacing=spacing, origin=origin)
            # Update the sources data.
            src.update_image_data = True
            self._reset_ipw()

    def _reset_ipw(self):
        ipw1, ipw2, ipw3 = self._ipw1, self._ipw2, self._ipw3
        if ipw1.running:
            ipw1.ipw.place_widget()
        if ipw2.running:
            ipw2.ipw.place_widget()
            ipw2.ipw.plane_orientation = 'y_axes'
        if ipw3.running:
            ipw3.ipw.place_widget()
            ipw3.ipw.plane_orientation = 'z_axes'
        self.source.render()

    def _data_changed(self, value):
        if self.source is None:
            return
        self.source.scalar_data = value

    def _window_changed(self):
        m = self.get_mayavi()
        if m.engine.running:
            if len(self.data) == 0:
                # Happens since the window may be set on __init__ at
                # which time the data is not created.
                self._make_data()
            self._show_data()
        else:
            # Show the data once the mayavi engine has started.
            m.engine.on_trait_change(self._show_data, 'started')

