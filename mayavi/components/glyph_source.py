"""A component that allows creates the source for the glyphs and
handle transformation.
"""
# Author: KK Rai (kk.rai [at] iitb.ac.in)
#         R. Ambareesha (ambareesha [at] iitb.ac.in)
#         Prabhu Ramachandran <prabhu_r@users.sf.net>

# Enthought library imports.
from traits.api import (Instance, List, Trait, Bool,
                        TraitPrefixList, Property, Dict)
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk
from tvtk.common import camel2enthought
from apptools.persistence.state_pickler import set_state

# Local imports.
from mayavi.core.common import handle_children_state
from mayavi.core.component import Component


######################################################################
# `GlyphSource` class.
######################################################################
class GlyphSource(Component):

    # The version of this class.  Used for persistence.
    __version__ = 1

    # Glyph position.  This can be one of ['head', 'tail', 'center'],
    # and indicates the position of the glyph with respect to the
    # input point data.  Please note that this will work correctly
    # only if you do not mess with the source glyph's basic size.  For
    # example if you use a ConeSource and set its height != 1, then the
    # 'head' and 'tail' options will not work correctly.
    glyph_position = Trait('center', TraitPrefixList(['head', 'tail',
                                                      'center']),
                           desc='position of glyph w.r.t. data point')

    # The Source to use for the glyph.  This is chosen from
    # `self._glyph_list` or `self.glyph_dict`.
    glyph_source = Instance(tvtk.Object, allow_none=False, record=True)

    # A dict of glyphs to use.
    glyph_dict = Dict(desc='the glyph sources to select from',
                      record=False)

    # A list of predefined glyph sources that can be used.
    glyph_list = Property(List(tvtk.Object), record=False)

    ########################################
    # Private traits.

    # The transformation to use to place glyph appropriately.
    _trfm = Instance(tvtk.TransformFilter, args=())

    # Used for optimization.
    _updating = Bool(False)

    ########################################
    # View related traits.

    view = View(
        Group(
            Group(Item(name='glyph_position')),
            Group(
                Item(
                    name='glyph_source',
                    style='custom',
                    resizable=True,
                    editor=InstanceEditor(name='glyph_list'),
                ),
                label='Glyph Source',
                show_labels=False)),
        resizable=True
    )

    ######################################################################
    # `Base` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(GlyphSource, self).__get_pure_state__()
        for attr in ('_updating', 'glyph_list'):
            d.pop(attr, None)
        return d

    def __set_pure_state__(self, state):
        if 'glyph_dict' in state:
            # Set their state.
            set_state(self, state, first=['glyph_dict'], ignore=['*'])
            ignore = ['glyph_dict']
        else:
            # Set the dict state using the persisted list.
            gd = self.glyph_dict
            gl = self.glyph_list
            handle_children_state(gl, state.glyph_list)
            for g, gs in zip(gl, state.glyph_list):
                name = camel2enthought(g.__class__.__name__)
                if name not in gd:
                    gd[name] = g
                # Set the glyph source's state.
                set_state(g, gs)
            ignore = ['glyph_list']
        g_name = state.glyph_source.__metadata__['class_name']
        name = camel2enthought(g_name)
        # Set the correct glyph_source.
        self.glyph_source = self.glyph_dict[name]
        set_state(self, state, ignore=ignore)

    ######################################################################
    # `Component` interface
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

        self._trfm.transform = tvtk.Transform()
        # Setup the glyphs.
        self.glyph_source = self.glyph_dict['glyph_source2d']

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        self._glyph_position_changed(self.glyph_position)
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self.data_changed = True

    def render(self):
        if not self._updating:
            super(GlyphSource, self).render()

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _glyph_source_changed(self, value):
        if self._updating:
            return

        gd = self.glyph_dict
        value_cls = camel2enthought(value.__class__.__name__)
        if value not in gd.values():
            gd[value_cls] = value

        # Now change the glyph's source trait.
        self._updating = True
        recorder = self.recorder
        if recorder is not None:
            name = recorder.get_script_id(self)
            lhs = '%s.glyph_source' % name
            rhs = '%s.glyph_dict[%r]' % (name, value_cls)
            recorder.record('%s = %s' % (lhs, rhs))

        name = value.__class__.__name__
        if name == 'GlyphSource2D':
            self.outputs = [value]
        else:
            self.configure_input(self._trfm, value)
            self.outputs = [self._trfm]
        value.on_trait_change(self.render)
        self._updating = False

        # Now update the glyph position since the transformation might
        # be different.
        self._glyph_position_changed(self.glyph_position)

    def _glyph_position_changed(self, value):
        if self._updating:
            return

        self._updating = True
        tr = self._trfm.transform
        tr.identity()

        g = self.glyph_source
        name = g.__class__.__name__
        # Compute transformation factor
        if name == 'CubeSource':
            tr_factor = g.x_length/2.0
        elif name == 'CylinderSource':
            tr_factor = -g.height/2.0
        elif name == 'ConeSource':
            tr_factor = g.height/2.0
        elif name == 'SphereSource':
            tr_factor = g.radius
        else:
            tr_factor = 1.
        # Translate the glyph
        if value == 'tail':
            if name == 'GlyphSource2D':
                g.center = 0.5, 0.0, 0.0
            elif name == 'ArrowSource':
                pass
            elif name == 'CylinderSource':
                g.center = 0, tr_factor, 0.0
            elif hasattr(g, 'center'):
                g.center = tr_factor, 0.0, 0.0
        elif value == 'head':
            if name == 'GlyphSource2D':
                g.center = -0.5, 0.0, 0.0
            elif name == 'ArrowSource':
                tr.translate(-1, 0, 0)
            elif name == 'CylinderSource':
                g.center = 0, -tr_factor, 0.0
            else:
                g.center = -tr_factor, 0.0, 0.0
        else:
            if name == 'ArrowSource':
                tr.translate(-0.5, 0, 0)
            elif name != 'Axes':
                g.center = 0.0, 0.0, 0.0

        if name == 'CylinderSource':
            tr.rotate_z(90)

        self._updating = False
        self.render()

    def _get_glyph_list(self):
        # Return the glyph list as per the original order in earlier
        # implementation.
        order = ['glyph_source2d', 'arrow_source', 'cone_source',
                 'cylinder_source', 'sphere_source', 'cube_source',
                 'axes']
        gd = self.glyph_dict
        for key in gd:
            if key not in order:
                order.append(key)
        return [gd[key] for key in order]

    def _glyph_dict_default(self):
        g = {'glyph_source2d': tvtk.GlyphSource2D(glyph_type='arrow',
                                                  filled=False),
             'arrow_source': tvtk.ArrowSource(),
             'cone_source': tvtk.ConeSource(height=1.0, radius=0.2,
                                            resolution=15),
             'cylinder_source': tvtk.CylinderSource(height=1.0, radius=0.15,
                                                    resolution=10),
             'sphere_source': tvtk.SphereSource(),
             'cube_source': tvtk.CubeSource(),
             'axes': tvtk.Axes(symmetric=1)}
        return g
