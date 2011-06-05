# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports.
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.filters.optional import Optional
from mayavi.filters.collection import Collection
from mayavi.filters.cell_derivatives import CellDerivatives
from mayavi.filters.cell_to_point_data import CellToPointData
from mayavi.filters.extract_vector_norm import ExtractVectorNorm
from mayavi.filters.extract_vector_components import ExtractVectorComponents


################################################################################
# `Vorticity` class.
################################################################################
class Vorticity(Optional):
    """
    This filter computes the vorticity of an input vector field.  For
    convenience, the filter allows one to optionally pass-through the
    given input vector field.  The filter also allows the user to show
    the component of the vorticity along a particular cartesian
    co-ordinate axes.  It produces point data on output which is ready
    to visualize.
    """

    # This is used just for the UI.
    vorticity_component = Instance(Optional, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `object` interface.
    ######################################################################
    def __get_pure_state__(self):
        d = super(Vorticity, self).__get_pure_state__()
        for name in ('vorticity_component'):
            d.pop(name, None)
        return d

    ######################################################################
    # `HasTraits` interface.
    ######################################################################
    def default_traits_view(self):
        view = View(Group(Group(Item(name='enabled',
                               label='Compute Vorticity',
                               )),
                          Group(Item(name='vorticity_component',
                                   style='custom',
                                   resizable=True,
                                   show_label=False),
                              ))
                        )
        return view


    ######################################################################
    # `Filter` interface.
    ######################################################################
    def setup_pipeline(self):
        """Setup our pipeline"""
        cd = CellDerivatives()
        cd.filter.vector_mode = 'compute_vorticity'
        c2d = CellToPointData()
        evn = ExtractVectorNorm()
        evc = ExtractVectorComponents()
        o = Optional(filter=evc, label_text='Extract Component of Vorticity',
                     enabled=False)
        self.vorticity_component = o
        c = Collection(filters=[cd, c2d, evn, o], name='Vorticity')
        self.filter = c

