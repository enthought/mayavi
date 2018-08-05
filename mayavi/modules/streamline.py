"""Allows the user to draw streamlines for given vector data.  This
supports various types of seed objects (line, sphere, plane and point
seeds).  It also allows the user to draw ribbons or tubes and further
supports different types of interactive modes of calculating the
streamlines.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from math import sqrt

# Enthought library imports.
from traits.api import Instance, Bool, TraitPrefixList, Trait, \
                             Delegate, Button
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.actor import Actor
from mayavi.components.source_widget import SourceWidget
from mayavi.core.utils import DataSetHelper

######################################################################
# `Streamline` class.
######################################################################
class Streamline(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The streamline generator.
    stream_tracer = Instance(tvtk.StreamTracer, allow_none=False,
                             record=True)

    # The seed for the streamlines.
    seed = Instance(SourceWidget, allow_none=False, record=True)

    # The update mode of the seed -- this is delegated to the
    # SourceWidget.
    update_mode = Delegate('seed', modify=True)

    # Determines if the streamlines are shown as lines or ribbons or
    # tubes.
    streamline_type = Trait('line', TraitPrefixList(['line', 'ribbon',
                                                      'tube']),
                            desc='draw streamlines as lines/ribbons/tubes')

    # The ribbon filter.
    ribbon_filter = Instance(tvtk.RibbonFilter, allow_none=False,
                             record=True)

    # The tube filter.
    tube_filter = Instance(tvtk.TubeFilter, allow_none=False,
                           record=True)

    # The clean poly data filter
    clean_filter = Instance(tvtk.CleanPolyData, allow_none=False,
                           record=True)

    # The actor component that represents the visualization.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    ########################################
    # Private traits.

    _first = Bool(True)

    ########################################
    # View related code.

    # A button to update the streamlines.
    update_streamlines = Button('Update Streamlines')

    _tube_group = Group(Item(name='capping'),
                        Item(name='sides_share_vertices'),
                        Item(name='vary_radius'),
                        Item(name='number_of_sides'),
                        Item(name='radius'),
                        Item(name='radius_factor'),
                        Item(name='offset'),
                        Item(name='on_ratio')
                        )

    _ribbon_group = Group(Item(name='vary_width'),
                          Item(name='width'),
                          Item(name='width_factor'),
                          Item(name='angle')
                          )

    view = View(Group(Group(Item(name='update_mode'),
                            ),
                      Group(Item(name='update_streamlines'),
                            show_labels=False,
                            ),
                      Group(Item(name='streamline_type'),
                            Item(name='ribbon_filter', style='custom',
                                 visible_when='object.streamline_type == "ribbon"',
                                 editor=InstanceEditor(view=View(_ribbon_group))),
                            Item(name='tube_filter', style='custom',
                                 visible_when='object.streamline_type == "tube"',
                                 editor=InstanceEditor(view=View(_tube_group))),
                            show_labels=False,
                            label='Streamline'
                            ),
                      label='Streamline'
                      ),
                Group(Item(name='seed', style='custom', resizable=True),
                      label='Seed',
                      show_labels=False),
                Group(Item(name='stream_tracer', style='custom', resizable=True),
                      label='StreamTracer',
                      show_labels=False),
                Group(Item(name='actor', style='custom'),
                      label='Actor',
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
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        # Create and setup the default objects.
        self.seed = SourceWidget()
        self.stream_tracer = tvtk.StreamTracer(maximum_propagation=50,
                                               integration_direction='forward',
                                               compute_vorticity=True,
                                               integrator_type='runge_kutta4',
                                               )
        self.ribbon_filter = tvtk.RibbonFilter()
        self.tube_filter = tvtk.TubeFilter()
        self.clean_filter = tvtk.CleanPolyData()

        self.actor = Actor()
        # Setup the actor suitably for this module.
        self.actor.property.line_width = 2.0

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        src = mm.source
        self.configure_connection(self.stream_tracer, src.outputs[0])
        self.seed.inputs = [src]

        # Setup the radius/width of the tube/ribbon filters based on
        # given input.
        if self._first:
            dsh = DataSetHelper(src.outputs[0])
            b = dsh.get_bounds()
            l = [(b[1]-b[0]), (b[3]-b[2]), (b[5]-b[4])]
            length = sqrt(l[0]*l[0] + l[1]*l[1] + l[2]*l[2])
            self.ribbon_filter.width = length*0.0075
            self.tube_filter.radius = length*0.0075
            self._first = False

        self._streamline_type_changed(self.streamline_type)
        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the components should do the rest if
        # they are connected.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _streamline_type_changed(self, value):
        if self.module_manager is None:
            return
        st = self.stream_tracer
        rf = self.ribbon_filter
        tf = self.tube_filter
        if value == 'line':
            self.outputs = [st]
        elif value == 'ribbon':
            self.configure_connection(rf, st)
            self.outputs = [rf]
        elif value == 'tube':
            # Without a clean poly data filter, tube filter will throw could
            # not generate normals warning
            cf = self.clean_filter
            self.configure_connection(cf, st)
            self.configure_connection(tf, cf)
            self.outputs = [tf]
        self.render()

    def _update_streamlines_fired(self):
        self.seed.update_poly_data()
        self.stream_tracer.update()
        self.render()

    def _stream_tracer_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        seed = self.seed
        if seed is not None:
            self.configure_source_data(new, seed.poly_data)
        new.on_trait_change(self.render)
        mm = self.module_manager
        if mm is not None:
            src = mm.source
            self.configure_connection(new, src.outputs[0])

        # A default output so there are no pipeline errors.  The
        # update_pipeline call corrects this if needed.
        self.outputs = [new]

        self.update_pipeline()

    def _seed_changed(self, old, new):
        st = self.stream_tracer
        if st is not None:
            self.configure_source_data(st, new.poly_data)
        self._change_components(old, new)

    def _ribbon_filter_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)
        self._streamline_type_changed(self.streamline_type)

    def _tube_filter_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)
        self._streamline_type_changed(self.streamline_type)

    def _actor_changed(self, old, new):
        new.scene = self.scene
        new.inputs = [self]
        self._change_components(old, new)
