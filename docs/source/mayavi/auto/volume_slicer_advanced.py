"""
An efficient implementation of the triple-plane view showing 3 cut planes
on volumetric data, and side views showing each cut, with a cursor to
move the other cuts.

This is an example of complex callback interaction. It builds on the
:ref:`example_volume_slicer` but has more complex logic. You should try
to understand the :ref:`example_volume_slicer` first.

In this example, the VolumeSlicer object displays a position attribute
giving the position of the cut in data coordinates. Traits callbacks are
used to move the cut planes when this position attribute is modifed.

In the 3D window, the 3D cuts are displayed using ImagePlaneWidgets
cutting the 3D volumetric data. The data extracted by the
ImagePlaneWidgets for plotting is captured using the TVTK
ImagePlaneWidget's `_get_reslice_output` method. The resulting dataset is
plotted in each side view using another ImagePlaneWidget. As a result the
data is not copied (at the VTK level, there is only one pipeline), and
modifications of the data plotted on the planes in the 3D view (for
instance when these planes are moved) are propagated to the 2D side views
by the VTK pipeline.

A cursor is displayed in each side view using a glyph. The cursor
indicates the position of the cut.

In the side view, when the mouse button is pressed on the planes, it
creates a VTK `InteractionEvent`. When this happens, VTK calls an
callback (observer, it VTK terms), that we use to move the position of
the cut. The Traits callbacks do the rest for the updating.
"""
import numpy as np

from traits.api import HasTraits, Instance, Array, \
    Bool, Dict, on_trait_change
from traitsui.api import View, Item, HGroup, Group

from tvtk.api import tvtk
from tvtk.pyface.scene import Scene

from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MlabSceneModel


################################################################################
# The object implementing the dialog
class VolumeSlicer(HasTraits):
    # The data to plot
    data = Array

    # The position of the view
    position = Array(shape=(3,))

    # The 4 views displayed
    scene3d = Instance(MlabSceneModel, ())
    scene_x = Instance(MlabSceneModel, ())
    scene_y = Instance(MlabSceneModel, ())
    scene_z = Instance(MlabSceneModel, ())

    # The data source
    data_src = Instance(Source)

    # The image plane widgets of the 3D scene
    ipw_3d_x = Instance(PipelineBase)
    ipw_3d_y = Instance(PipelineBase)
    ipw_3d_z = Instance(PipelineBase)

    # The cursors on each view:
    cursors = Dict()

    disable_render = Bool

    _axis_names = dict(x=0, y=1, z=2)

    #---------------------------------------------------------------------------
    # Object interface
    #---------------------------------------------------------------------------
    def __init__(self, **traits):
        super(VolumeSlicer, self).__init__(**traits)
        # Force the creation of the image_plane_widgets:
        self.ipw_3d_x
        self.ipw_3d_y
        self.ipw_3d_z


    #---------------------------------------------------------------------------
    # Default values
    #---------------------------------------------------------------------------
    def _position_default(self):
        return 0.5*np.array(self.data.shape)

    def _data_src_default(self):
        return mlab.pipeline.scalar_field(self.data,
                            figure=self.scene3d.mayavi_scene,
                            name='Data',)

    def make_ipw_3d(self, axis_name):
        ipw = mlab.pipeline.image_plane_widget(self.data_src,
                        figure=self.scene3d.mayavi_scene,
                        plane_orientation='%s_axes' % axis_name,
                        name='Cut %s' % axis_name)
        return ipw

    def _ipw_3d_x_default(self):
        return self.make_ipw_3d('x')

    def _ipw_3d_y_default(self):
        return self.make_ipw_3d('y')

    def _ipw_3d_z_default(self):
        return self.make_ipw_3d('z')


    #---------------------------------------------------------------------------
    # Scene activation callbacks
    #---------------------------------------------------------------------------
    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        outline = mlab.pipeline.outline(self.data_src,
                        figure=self.scene3d.mayavi_scene,
                        )
        self.scene3d.mlab.view(40, 50)
        # Interaction properties can only be changed after the scene
        # has been created, and thus the interactor exists
        for ipw in (self.ipw_3d_x, self.ipw_3d_y, self.ipw_3d_z):
            ipw.ipw.interaction = 0
        self.scene3d.scene.background = (0, 0, 0)
        # Keep the view always pointing up
        self.scene3d.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleTerrain()
        self.update_position()


    def make_side_view(self, axis_name):
        scene = getattr(self, 'scene_%s' % axis_name)
        scene.scene.parallel_projection = True
        ipw_3d   = getattr(self, 'ipw_3d_%s' % axis_name)

        # We create the image_plane_widgets in the side view using a
        # VTK dataset pointing to the data on the corresponding
        # image_plane_widget in the 3D view (it is returned by
        # ipw_3d._get_reslice_output())
        side_src = ipw_3d.ipw._get_reslice_output()
        ipw = mlab.pipeline.image_plane_widget(
                            side_src,
                            plane_orientation='z_axes',
                            vmin=self.data.min(),
                            vmax=self.data.max(),
                            figure=scene.mayavi_scene,
                            name='Cut view %s' % axis_name,
                            )
        setattr(self, 'ipw_%s' % axis_name, ipw)

        # Extract the spacing of the side_src to convert coordinates
        # into indices
        spacing = side_src.spacing

        # Make left-clicking create a crosshair
        ipw.ipw.left_button_action = 0

        x, y, z = self.position
        cursor = mlab.points3d(x, y, z,
                            mode='axes',
                            color=(0, 0, 0),
                            scale_factor=2*max(self.data.shape),
                            figure=scene.mayavi_scene,
                            name='Cursor view %s' % axis_name,
                        )
        self.cursors[axis_name] = cursor

        # Add a callback on the image plane widget interaction to
        # move the others
        this_axis_number = self._axis_names[axis_name]
        def move_view(obj, evt):
            # Disable rendering on all scene
            position = list(obj.GetCurrentCursorPosition()*spacing)[:2]
            position.insert(this_axis_number, self.position[this_axis_number])
            # We need to special case y, as the view has been rotated.
            if axis_name is 'y':
                position = position[::-1]
            self.position = position

        ipw.ipw.add_observer('InteractionEvent', move_view)
        ipw.ipw.add_observer('StartInteractionEvent', move_view)

        # Center the image plane widget
        ipw.ipw.slice_position = 0.5*self.data.shape[
                                        self._axis_names[axis_name]]

        # 2D interaction: only pan and zoom
        scene.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleImage()
        scene.scene.background = (0, 0, 0)

        # Some text:
        mlab.text(0.01, 0.8, axis_name, width=0.08)

        # Choose a view that makes sens
        views = dict(x=(0, 0), y=(90, 180), z=(0, 0))
        mlab.view(views[axis_name][0],
                  views[axis_name][1],
                  focalpoint=0.5*np.array(self.data.shape),
                  figure=scene.mayavi_scene)
        scene.scene.camera.parallel_scale = 0.52*np.mean(self.data.shape)

    @on_trait_change('scene_x.activated')
    def display_scene_x(self):
        return self.make_side_view('x')

    @on_trait_change('scene_y.activated')
    def display_scene_y(self):
        return self.make_side_view('y')

    @on_trait_change('scene_z.activated')
    def display_scene_z(self):
        return self.make_side_view('z')


    #---------------------------------------------------------------------------
    # Traits callback
    #---------------------------------------------------------------------------
    @on_trait_change('position')
    def update_position(self):
        """ Update the position of the cursors on each side view, as well
            as the image_plane_widgets in the 3D view.
        """
        # First disable rendering in all scenes to avoid unnecessary
        # renderings
        self.disable_render = True

        # For each axis, move image_plane_widget and the cursor in the
        # side view
        for axis_name, axis_number in self._axis_names.items():
            ipw3d = getattr(self, 'ipw_3d_%s' % axis_name)
            ipw3d.ipw.slice_position = self.position[axis_number]

            # Go from the 3D position, to the 2D coordinates in the
            # side view
            position2d = list(self.position)
            position2d.pop(axis_number)
            if axis_name is 'y':
                position2d = position2d[::-1]
            # Move the cursor
            # For the following to work, you need Mayavi 3.4.0, if you
            # have a less recent version, use 'x=[position2d[0]]'
            self.cursors[axis_name].mlab_source.trait_set(
                x=position2d[0], y=position2d[1], z=0)

        # Finally re-enable rendering
        self.disable_render = False

    @on_trait_change('disable_render')
    def _render_enable(self):
        for scene in (self.scene3d, self.scene_x, self.scene_y,
                                                  self.scene_z):
            scene.scene.disable_render = self.disable_render


    #---------------------------------------------------------------------------
    # The layout of the dialog created
    #---------------------------------------------------------------------------
    view = View(HGroup(
                  Group(
                       Item('scene_y',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene_z',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                  Group(
                       Item('scene_x',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene3d',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                ),
                resizable=True,
                title='Volume Slicer',
                )


################################################################################
if __name__ == '__main__':
    # Create some data
    x, y, z = np.ogrid[-5:5:100j, -5:5:100j, -5:5:100j]
    data = np.sin(3*x)/x + 0.05*z**2 + np.cos(3*y)

    m = VolumeSlicer(data=data)
    m.configure_traits()
