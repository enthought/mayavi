"""
Modules factories and their associated functions for mlab.

Module functions meant to be applied to a data source object or a filter 
should take only one positional argument, the input, to be easily used in
helper functions. 
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

from enthought.traits.api import Trait, CArray, Instance, CFloat, Enum, \
    Any, false, TraitTuple, Range
from pipe_base import PipeFactory, make_function
import enthought.mayavi.modules.api as modules
from enthought.tvtk.api import tvtk
import numpy
from enthought.mayavi.core.lut_manager import lut_mode_list
import tools

__all__ = ( 'vectors', 'glyph', 'streamline', 'volume', 'surface',
                'isosurface', 'contoursurface')

##############################################################################
# Abstract module classes
##############################################################################

class ModuleFactory(PipeFactory):
    """ Base class for all the modules factories"""
    color = Trait(None, None,
                TraitTuple(Range(0., 1.),Range(0., 1.),Range(0., 1.)),
                help="""the color of the vtk object. Overides the colormap,
                        if any, when specified.""", )

    def _color_changed(self):
        if self.color:
            self._target.actor.property.color = self.color
            if hasattr(self._target.actor.mapper, "scalarvisibility"):
                self._target.actor.mapper.scalar_visibility = False
            if hasattr(self._target, "property"):
                self._target.property.color = self.color
    
    opacity = CFloat(1.,
                help="""The overall opactiy of the vtk object.""")

    def _opacity_changed(self):
        try:
            self._target.actor.property.opacity = self.opacity
        except AttributeError:
            try:
                self._target.property.opacity = self.opacity
            except AttributeError:
                pass

##############################################################################
class DataModuleFactory(ModuleFactory):
    """ Base class for all the module factories operating on data (ie not 
        text and outline) """
    
    extent = CArray(shape=(6,),
                    help="""[xmin, xmax, ymin, ymax, zmin, zmax]
                            Default is the x, y, z arrays extents.""", )

    def _extent_changed(self):
        tools._set_extent(self._target, self.extent)

    transparent = false(help="""make the opacity of the actor depend on the 
                               scalar.""")

    def _transparent_changed(self):
        if self.transparent:
            data_range = \
                self._target.module_manager.scalar_lut_manager.data_range
            self._target.module_manager.scalar_lut_manager.lut.alpha_range = \
                                                                (0.2, 0.8)
            data_range = ( numpy.mean(data_range)
                            + 0.4 * ( data_range.max() - data_range.min())
                                * numpy.array([-1, 1]))
            self._target.module_manager.scalar_lut_manager.data_range = \
                data_range

    colormap = Trait('blue-red', lut_mode_list(),
                        help="""type of colormap to use.""")

    def _colormap_changed(self):
        colormap = self.colormap
        if colormap[-2:] == "_r":
            colormap = colormap[:-2]
            self._target.module_manager.scalar_lut_manager.reverse_lut = True
            self._target.module_manager.vector_lut_manager.reverse_lut = True
        self._target.module_manager.scalar_lut_manager.lut_mode = colormap
        self._target.module_manager.vector_lut_manager.lut_mode = colormap
    

    vmin = Trait(None, None, CFloat,
                    help="""vmin is used to scale the colormap
                            If None, the min of the data will be used""")

    vmax = Trait(None, None, CFloat,
                    help="""vmax is used to scale the colormap
                            If None, the max of the data will be used""")

    def _vmin_changed(self):
        if self.vmin == None and self.vmax == None:
            self._target.module_manager.scalar_lut_manager.use_default_range\
                    = True
            return
        
        self._target.module_manager.scalar_lut_manager.use_default_range \
                    = False
        vmin, vmax = \
                self._target.module_manager.scalar_lut_manager.data_range
        if self.vmin is not None:
            vmin = self.vmin
        if self.vmax is not None:
            vmax = self.vmax
        self._target.module_manager.scalar_lut_manager.data_range = \
                        (vmin, vmax)

    _vmax_changed = _vmin_changed

    def __init__(self, *args, **kwargs):
        super(DataModuleFactory, self).__init__(*args, **kwargs)
        # We are adding data to the scene, reset the zoom:
        self._scene.scene.reset_zoom()


class ContourModuleFactory(DataModuleFactory):
    """ Base class for all the module factories with contours """

    contours = Any(5, help="""Integer/list specifying number/list of
                    contours. Specifying 0 shows no contours.
                    Specifying a list of values will only give the
                    requested contours asked for.""")

    def _contours_changed(self):
        contour_list = True
        try:
            len(self.contours)
        except TypeError:
            contour_list = False

        if contour_list:
            self._target.contour.contours = self.contours
        else:
            assert type(self.contours) == int, \
                            "The contours argument must be an integer"
            assert self.contours > 1, "The contours argument must be positiv"
            self._target.contour.set(auto_contours=True,
                                number_of_contours=self.contours)
        if hasattr(self._target, 'enable_contours'):
            self._target.enable_contours = True

 

##############################################################################
# Concrete module classes
##############################################################################

##############################################################################
class VectorsFactory(DataModuleFactory):
    """Applies the Vectors mayavi module to the given VTK data object."""

    _target = Instance(modules.Vectors, ())

    scale_factor = CFloat(1., adapts='glyph.glyph.scale_factor',
                            desc="""the scaling applied to the glyphs. The 
                                    size of the glyph is by default in drawing 
                                    units.""")

    scale_mode = Trait('vector', {'none':'data_scaling_off',
                                'scalar':'scale_by_scalar',
                                'vector':'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    def _scale_mode_changed(self):
        self._target.glyph.glyph.scale_mode = self.scale_mode_

    mode = Trait('2darrow', {'2darrow': 0, '2dcircle':0, '2dcross':0,
                            '2ddash': 0, '2ddiamond':0,
                            '2dhooked_arrow':0, '2dsquare':0,
                            '2dthick_arrow':0, '2dthick_cross':0,
                            '2dtriangle':0, '2dvertex':0,
                            'arrow': 1, 'cone': 2, 'cylinder': 3,
                            'sphere': 4, 'cube': 5, 'point': 6},
                    desc="""the mode of the glyphs.""")

    def _mode_changed(self):
        v = self._target
        # Workaround for different version of VTK:
        if hasattr(v.glyph.glyph_source, 'glyph_source'):
            g = v.glyph.glyph_source
        else:
            g = v.glyph
        if self.mode == 'point':
            g.glyph_source = tvtk.PointSource(radius=0, number_of_points=1)
        else:
            g.glyph_source = g.glyph_list[self.mode_]
        if self.mode_ == 0:
            g.glyph_source.glyph_type = self.mode[2:]


vectors = make_function(VectorsFactory)


##############################################################################
class GlyphFactory(VectorsFactory):
    """Applies the Glyph mayavi module to the given VTK data object."""

    _target = Instance(modules.Glyph, ())

    scale_mode = Trait('scalar', {'none':'data_scaling_off',
                                'scalar':'scale_by_scalar',
                                'vector':'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    mode = Trait('sphere', {'2darrow': 0, '2dcircle':0, '2dcross':0,
                            '2ddash': 0, '2ddiamond':0,
                            '2dhooked_arrow':0, '2dsquare':0,
                            '2dthick_arrow':0, '2dthick_cross':0,
                            '2dtriangle':0, '2dvertex':0,
                            'arrow': 1, 'cone': 2, 'cylinder': 3,
                            'sphere': 4, 'cube': 5, 'point': 6},
                    desc="""the mode of the glyphs.""")


glyph = make_function(GlyphFactory)


##############################################################################
class StreamlineFactory(DataModuleFactory):
    """Applies the Streamline mayavi module to the given VTK data object."""
    _target = Instance(modules.Streamline, ())

    linetype = Trait('line', 'ribbon', 'tube',
            adapts='streamline_type', 
            desc="""the type of line-like object used to display the
                   streamline.""")

    seedtype = Trait('sphere', 
            {'sphere':0, 'line':1, 'plane':2, 'point':3},
            desc="""the widget used as a seed for the streamlines.""")

    def _seedtype_changed(self):
        self._target.seed.widget = \
                            self._target.seed.widget_list[self.seedtype_]


streamline = make_function(StreamlineFactory)

##############################################################################
class VolumeFactory(DataModuleFactory):
    """Applies the Volume mayavi module to the given VTK data object."""

    _target = Instance(modules.Volume, ())

volume = make_function(VolumeFactory)


##############################################################################
class SurfaceFactory(DataModuleFactory):
    """Applies the Surface mayavi module to the given VTK data object."""
    _target = Instance(modules.Surface, ())

    representation = Trait('surface', 'wireframe', 'points',
                    adapts='actor.property.representation',
                    desc="""the representation type used for the surface.""")


surface = make_function(SurfaceFactory)


##############################################################################
class IsoSurfaceFactory(ContourModuleFactory):
    """Applies the IsoSurface mayavi module to the given VTK data object."""
    _target = Instance(modules.IsoSurface, ())


isosurface = make_function(IsoSurfaceFactory)


##############################################################################
class ContourSurfaceFactory(ContourModuleFactory):
    """Applies the Surface mayavi module to the given VTK data object, 
       and turns contours on."""
    _target = Instance(modules.Surface, ())

    def __init__(self, *args, **kwargs):
        """ Overridding the __init__ to turn contours on."""
        super(ContourSurfaceFactory, self).__init__(*args, **kwargs)
        self._contours_changed()


contoursurface = make_function(ContourSurfaceFactory)

