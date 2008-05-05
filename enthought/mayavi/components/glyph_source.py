"""A component that allows creates the source for the glyphs and
handle transformation.
"""
# Author: KK Rai (kk.rai [at] iitb.ac.in)
#         R. Ambareesha (ambareesha [at] iitb.ac.in)
#         Prabhu Ramachandran <prabhu_r@users.sf.net>

# Enthought library imports.
from enthought.traits.api import Instance, List, Trait, Bool, TraitPrefixList
from enthought.traits.ui.api import View, Group, Item, InstanceEditor
from enthought.tvtk.api import tvtk
from enthought.persistence.state_pickler import set_state

# Local imports.
from enthought.mayavi.core.common import handle_children_state
from enthought.mayavi.core.component import Component


######################################################################
# `GlyphSource` class.
######################################################################
class GlyphSource(Component):

    # The version of this class.  Used for persistence.
    __version__ = 0

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
    # `self._glyph_list` or `self.glyph_dict'.
    glyph_source = Instance(tvtk.Object, allow_none=False)

    # A list of predefined glyph sources that can be used.
    glyph_list = List(tvtk.Object)

    ########################################
    # Private traits.

    # The transformation to use to place glyph appropriately.
    _trfm = Instance(tvtk.TransformFilter, args=())

    # Used for optimization.
    _updating = Bool(False)
    
    ########################################
    # View related traits.            
    view = View(Group(Group(Item(name='glyph_position')),                       
                      Group(Item(name='glyph_source', 
                                 style='custom',
                                 resizable=True,
                                 editor=InstanceEditor(name='glyph_list'),
                               ),
                            label='Glyph Source',
                            show_labels=False)
                     ),
                resizable=True)

    ######################################################################
    # `Base` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(GlyphSource, self).__get_pure_state__()
        for attr in ('_updating'):
            d.pop(attr, None)
        return d

    def __set_pure_state__(self, state):
        # Setup the glyph_list attribute by creating any new ones if
        # needed.
        handle_children_state(self.glyph_list, state.glyph_list)
        # Set their state.
        set_state(self, state, first=['glyph_list'], ignore=['*'])
        glyph_names = [x.__class__.__name__ for x in self.glyph_list]
        g_name = state.glyph_source.__metadata__['class_name']
        # Set the correct glyph_source.
        self.glyph_source = self.glyph_list[glyph_names.index(g_name)]
        set_state(self, state, ignore=['glyph_list'])
        #self._glyph_position_changed(self.glyph_position)

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
        glyphs = [tvtk.GlyphSource2D(glyph_type='arrow', filled=False),
                  tvtk.ArrowSource(),
                  tvtk.ConeSource(height=1.0, radius=0.2, resolution=15),
                  tvtk.CylinderSource(height=1.0, radius=0.15, resolution=10),
                  tvtk.SphereSource(),
                  tvtk.CubeSource(),
                  ]
        self.glyph_list = glyphs
        self.glyph_source = glyphs[0]

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
        if self._updating == True:
            return
        if value not in self.glyph_list:
            classes = [o.__class__ for o in self.glyph_list]
            vc = value.__class__
            if vc in classes:
                self.glyph_list[classes.index(vc)] = value
            else:
                self.glyph_list.append(value)

        # Now change the glyph's source trait.
        self._updating = True
        name = value.__class__.__name__
        if name == 'GlyphSource2D':       
            self.outputs = [value.output]
        else:
            self._trfm.input = value.output
            self.outputs = [self._trfm.output]
        value.on_trait_change(self.render)
        self._updating = False            

        # Now update the glyph position since the transformation might
        # be different.        
        self._glyph_position_changed(self.glyph_position)

    def _glyph_position_changed(self, value):
        if self._updating == True:
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
        # Translate the glyph
        if value == 'tail':
            if name == 'GlyphSource2D':
                g.center = 0.5, 0.0, 0.0
            elif name == 'ArrowSource':
                pass
            elif name == 'CylinderSource':
                g.center = 0,tr_factor, 0.0
            else:
                g.center = tr_factor, 0.0, 0.0
        elif value == 'head':
            if name == 'GlyphSource2D':
                g.center = -0.5, 0.0, 0.0
            elif name == 'ArrowSource':
                tr.translate(-1, 0, 0)
            elif name == 'CylinderSource':
                g.center = 0,-tr_factor, 0.0
            else:
                g.center = -tr_factor, 0.0, 0.0
        else:
            if name == 'GlyphSource2D':
                g.center = 0.0, 0.0, 0.0
            elif name == 'ArrowSource':
                tr.translate(-0.5, 0, 0)
            else:
                g.center = 0.0, 0.0, 0.0

        if name == 'CylinderSource':
            tr.rotate_z(90)

        self._updating = False
        self.render()            
