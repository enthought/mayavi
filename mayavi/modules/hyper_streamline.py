""" A module that integrates through a tensor field to generate a
     hyperstreamline. The integration is along the maximum
     eigenvector and the cross section of the hyperstreamline is
     defined by the two other eigenvectors. Thus the shape of the
     hyperstreamline is "tube-like", with the cross section being
     elliptical. Hyperstreamlines are used to visualize tensor fields.
"""
# Authors: KK Rai (kk.rai [at] iitb.ac.in)
#          R. Ambareesha (ambareesha [at] iitb.ac.in)
#          Prabhu Ramachandran <prabhu_r@users.sf.net>

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.actor import Actor

######################################################################
# `HyperStreamline` class.
######################################################################
class HyperStreamline(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The hyper streamline object.
    streamline = Instance(tvtk.HyperStreamline, allow_none=False,
                          record=True)

    # The actor for the streamlines.
    actor = Instance(Actor, allow_none=False, record=True)

    # A point widget
    widget = Instance(tvtk.PointWidget, args=(),
                      kw={'outline': False, 'x_shadows': False,
                      'y_shadows': False, 'z_shadows': False},
                      allow_none=False)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors'])

    # Create the UI for the traits.
    view = View(Group(Item(name='actor', style='custom'),
                      show_labels=False,
                      label='Actor'),
                Group(Item(name='widget', style='custom', resizable=True),
                      show_labels=False,
                      label='PointWidget'),
                Group(Item(name='streamline', style='custom',
                           resizable=True),
                      label='Streamline',
                      show_labels=False),
               resizable=True
               )

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`. Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        self.widget.on_trait_change(self._start_position_changed)

        self.streamline = tvtk.HyperStreamline()
        self.streamline.start_position = self.widget.position
        self.streamline.integrate_minor_eigenvector()
        self.streamline.maximum_propagation_distance = 10.0
        self.streamline.integration_step_length =0.1
        self.streamline.step_length = 0.01
        self.streamline.radius = 0.25
        self.streamline.number_of_sides = 18
        self.streamline.integration_direction = 2 #integrate both direction

        self.streamline.on_trait_change(self.render)
        self.actor = Actor()
        self.widgets.append(self.widget)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return
        src = mm.source.outputs[0]
        self.configure_connection(self.streamline, mm.source)
        w = self.widget
        old_inp = w.input
        self.configure_input_data(w, src)
        if old_inp is None or src != old_inp:
            w.place_widget()
        self.streamline.update()
        self.outputs = [self.streamline]
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _streamline_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)
        mm = self.module_manager
        if mm is not None:
            self.configure_connection(new, mm.source)
        # A default output so there are no pipeline errors.  The
        # update_pipeline call corrects this if needed.
        self.outputs = [new]
        self.update_pipeline()

    def _start_position_changed(self, value):
        self.streamline.start_position = self.widget.position

    def _actor_changed(self, old, new):
        new.scene = self.scene
        new.inputs = [self]
        self._change_components(old, new)
