"""
Modules factories and their associated functions for mlab.

Module functions meant to be applied to a data source object or a filter
should take only one positional argument, the input, to be easily used in
helper functions.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Prabhu Ramachandran
# Copyright (c) 2007-2015, Enthought, Inc.
# License: BSD Style.

import numpy

from traits.api import Trait, CArray, Instance, CFloat, \
    Any, false, true, TraitTuple, Range, Bool, Property, CInt, Enum, Either
from traits.trait_errors import TraitError
from tvtk.api import tvtk
from tvtk.common import camel2enthought

from mayavi.core.lut_manager import lut_mode_list
import mayavi.modules.api as modules
from mayavi.core.registry import registry
from . import tools
from .pipe_base import PipeFactory, make_function
from .filters import new_class


# This the list is dynamically populated further down below at the end.
__all__ = ['vectors', 'glyph', 'streamline', 'surface', 'iso_surface',
            'image_actor', 'contour_surface', 'contour_grid_plane',
            'custom_grid_plane', 'image_plane_widget',
            'scalar_cut_plane', 'vector_cut_plane', 'volume',
            ]

##############################################################################
# Abstract module classes
##############################################################################


class ModuleFactory(PipeFactory):
    """ Base class for all the modules factories"""
    color = Trait(None, None,
                TraitTuple(Range(0., 1.), Range(0., 1.), Range(0., 1.)),
                help="""the color of the vtk object. Overides the colormap,
                        if any, when specified. This is specified as a
                        triplet of float ranging from 0 to 1, eg (1, 1,
                        1) for white.""", )

    def _color_changed(self):
        if self.color:
            self._target.actor.property.color = self.color
            if hasattr(self._target.actor.mapper, "scalar_visibility"):
                self._target.actor.mapper.scalar_visibility = False
            if hasattr(self._target, "property"):
                self._target.property.color = self.color

    opacity = CFloat(1.,
                desc="""The overall opacity of the vtk object.""")

    def _opacity_changed(self):
        try:
            self._target.actor.property.opacity = self.opacity
        except AttributeError:
            try:
                self._target.property.opacity = self.opacity
            except AttributeError:
                pass

    line_width = CFloat(2.,
                desc=""" The width of the lines, if any used.""")

    def _line_width_changed(self):
        try:
            self._target.actor.property.line_width = self.line_width
        except (AttributeError, TraitError):
            try:
                self._target.property.line_width = self.line_width
            except (AttributeError, TraitError):
                pass


##############################################################################
class DataModuleFactory(ModuleFactory):
    """ Base class for all the module factories operating on data (ie not
        text and outline) """

    reset_zoom = true(help="""Reset the zoom to accomodate the data newly
                        added to the scene. Defaults to True.""")

    extent = CArray(shape=(6,),
                    help="""[xmin, xmax, ymin, ymax, zmin, zmax]
                            Default is the x, y, z arrays extent. Use
                            this to change the extent of the object
                            created.""", )

    def _extent_changed(self):
        tools.set_extent(self._target, self.extent)

    transparent = false(help="""make the opacity of the actor depend on the
                               scalar.""")

    def _transparent_changed(self):
        if self.transparent:
            data_range = \
                self._target.module_manager.scalar_lut_manager.data_range
            self._target.module_manager.scalar_lut_manager.lut.alpha_range = \
                                                                (0.2, 0.8)
            data_range = (numpy.mean(data_range)
                            + 0.4 * (data_range.max() - data_range.min())
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
                    help="""vmin is used to scale the colormap.
                            If None, the min of the data will be used""")

    vmax = Trait(None, None, CFloat,
                    help="""vmax is used to scale the colormap.
                            If None, the max of the data will be used""")

    def _vmin_changed(self):
        if self.vmin is None and self.vmax is None:
            self._target.module_manager.scalar_lut_manager.use_default_range\
                    = True
            return

        self._target.module_manager.scalar_lut_manager.use_default_range \
                    = False
        vmin, vmax = \
                self._target.module_manager.scalar_lut_manager.data_range
        # This takes care of pathological cases where vmin is changed
        # before vmax is changed, but vmin is greater than data_range[1]
        if self.vmin is not None:
            vmin = self.vmin
            if self.vmax is None:
                vmax = max(vmax, vmin)
        if self.vmax is not None:
            vmax = self.vmax
            if self.vmin is None:
                vmin = min(vmin, vmax)
        self._target.module_manager.scalar_lut_manager.data_range = \
                        (vmin, vmax)

    _vmax_changed = _vmin_changed

    def __init__(self, *args, **kwargs):
        super(DataModuleFactory, self).__init__(*args, **kwargs)
        # We are adding data to the scene, reset the zoom:
        scene = self._scene.scene
        if scene is not None and self.reset_zoom:
            scene.reset_zoom()


class ContourModuleFactory(DataModuleFactory):
    """ Base class for all the module factories with contours """

    contours = Any(5, help="""Integer/list specifying number/list of
                    contours. Specifying a list of values will only
                    give the requested contours asked for.""")

    def _contours_changed(self):
        contour_list = True
        try:
            len(self.contours)
        except TypeError:
            contour_list = False

        if contour_list:
            self._target.contour.auto_contours = False
            self._target.contour.contours = self.contours
        else:
            assert type(self.contours) == int, \
                            "The contours argument must be an integer"
            assert self.contours > 0, "The contours argument must be positive"
            self._target.contour.trait_set(auto_contours=True,
                                number_of_contours=self.contours)
        if hasattr(self._target, 'enable_contours'):
            self._target.enable_contours = True


##############################################################################
class CutPlaneFactory(DataModuleFactory):
    """ Base class for modules with a cut plane.
    """

    plane_orientation = Enum('x_axes', 'y_axes', 'z_axes',
                        desc="""the orientation of the plane""")

    view_controls = Bool(True, adapts='implicit_plane.visible',
                     desc=("Whether or not the controls of the "
                           "cut plane are shown."))

    def _plane_orientation_changed(self):
        choices = dict(x_axes=numpy.array([1.,  0.,  0.]),
                       y_axes=numpy.array([0.,  1.,  0.]),
                       z_axes=numpy.array([0.,  0.,  1.]))
        self._target.implicit_plane.normal = \
                                choices[self.plane_orientation]


##############################################################################
# Concrete module classes
##############################################################################

# The list of possible glyph modes
glyph_mode_dict = {'2darrow': 0, '2dcircle': 0, '2dcross': 0,
                            '2ddash': 0, '2ddiamond': 0,
                            '2dhooked_arrow': 0, '2dsquare': 0,
                            '2dthick_arrow': 0, '2dthick_cross': 0,
                            '2dtriangle': 0, '2dvertex': 0,
                            'arrow': 1, 'cone': 2, 'cylinder': 3,
                            'sphere': 4, 'cube': 5, 'axes': 6, 'point': 7}


##############################################################################
class VectorsFactory(DataModuleFactory):
    """Applies the Vectors mayavi module to the given data object
        source (Mayavi source, or VTK dataset).
    """

    _target = Instance(modules.Vectors, ())

    scale_factor = CFloat(1., adapts='glyph.glyph.scale_factor',
                            desc="""the scaling applied to the glyphs. The
                                    size of the glyph is by default in drawing
                                    units.""")

    scale_mode = Trait('vector', {'none': 'data_scaling_off',
                                'scalar': 'scale_by_scalar',
                                'vector': 'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    resolution = CInt(8, desc="The resolution of the glyph created. For "
                        "spheres, for instance, this is the number of "
                        "divisions along theta and phi.")

    mask_points = Either(None, CInt,
                        desc="If supplied, only one out of 'mask_points' "
                        "data point is displayed. This option is useful "
                        "to reduce the number of points displayed "
                        "on large datasets")

    def _resolution_changed(self):
        glyph = self._target.glyph.glyph_source.glyph_source
        if hasattr(glyph, 'theta_resolution'):
            glyph.theta_resolution = self.resolution
        if hasattr(glyph, 'phi_resolution'):
            glyph.phi_resolution = self.resolution
        if hasattr(glyph, 'resolution'):
            glyph.resolution = self.resolution
        if hasattr(glyph, 'shaft_resolution'):
            glyph.shaft_resolution = self.resolution
        if hasattr(glyph, 'tip_resolution'):
            glyph.tip_resolution = self.resolution

    def _mask_points_changed(self):
        if self.mask_points is not None:
            self._target.glyph.mask_input_points = True
            self._target.glyph.mask_points.on_ratio = self.mask_points

    def _scale_mode_changed(self):
        self._target.glyph.scale_mode = self.scale_mode_

    mode = Trait('2darrow', glyph_mode_dict,
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
    """Applies the Glyph mayavi module to the given VTK data
        source (Mayavi source, or VTK dataset).
    """

    _target = Instance(modules.Glyph, ())

    scale_mode = Trait('scalar', {'none': 'data_scaling_off',
                                'scalar': 'scale_by_scalar',
                                'vector': 'scale_by_vector'},
                            help="""the scaling mode for the glyphs
                            ('vector', 'scalar', or 'none').""")

    mode = Trait('sphere', glyph_mode_dict,
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
            {'sphere': 0, 'line': 1, 'plane': 2, 'point': 3},
            desc="""the widget used as a seed for the streamlines.""")

    seed_visible = Bool(True,
            adapts='seed.widget.enabled',
            desc="Control the visibility of the seed.",
            )

    seed_scale = CFloat(1.,
            desc="Scales the seed around its default center",
            )

    seed_resolution = Either(None, CInt,
            desc='The resolution of the seed. Determines the number of '
                 'seed points')

    integration_direction = Trait('forward', 'backward', 'both',
            adapts='stream_tracer.integration_direction',
            desc="The direction of the integration.",
            )

    def _anytrait_changed(self, name, value):
        if name == 'seed_visible' and self._target.scene is None:
            pass
        else:
            super(StreamlineFactory, self)._anytrait_changed(name, value)

    def _seedtype_changed(self):
        # XXX: this also acts for seed_scale and seed_resolution, but no
        # need to define explicit callbacks, as all the callbacks are
        # being called anyhow.
        self._target.seed.widget = widget = \
                            self._target.seed.widget_list[self.seedtype_]
        scene = self._target.scene

        if not self.seed_scale == 1.:
            if scene is not None:
                widget.enabled = True
            if self.seedtype == 'line':
                p1 = widget.point1
                p2 = widget.point2
                center = (p1 + p2) / 2.
                widget.point1 = center + self.seed_scale * (p1 - center)
                widget.point2 = center + self.seed_scale * (p2 - center)
            elif self.seedtype == 'plane':
                p1 = widget.point1
                p2 = widget.point2
                center = (p1 + p2) / 2.
                o = widget.origin
                widget.point1 = center + self.seed_scale * (p1 - center)
                widget.point2 = center + self.seed_scale * (p2 - center)
                widget.origin = center + self.seed_scale * (o - center)
            elif self.seedtype == 'sphere':
                widget.radius *= self.seed_scale

            # XXX: Very ugly, but this is only way I have found to
            # propagate changes.
            self._target.seed.stop()
            self._target.seed.start()
            if scene is not None:
                widget.enabled = self.seed_visible

        if self.seed_resolution is not None:
            if scene is not None:
                widget.enabled = True
            if self.seedtype in ('plane', 'line'):
                widget.resolution = self.seed_resolution
            elif self.seedtype == 'sphere':
                widget.phi_resolution = widget.theta_resolution = \
                        self.seed_resolution

            # XXX: Very ugly, but this is only way I have found to
            # propagate changes.
            self._target.seed.stop()
            self._target.seed.start()
            if scene is not None:
                widget.enabled = self.seed_visible


streamline = make_function(StreamlineFactory)


##############################################################################
class SurfaceFactory(DataModuleFactory):
    """Applies the Surface mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.Surface, ())

    representation = Trait('surface', 'wireframe', 'points',
                    adapts='actor.property.representation',
                    desc="""the representation type used for the surface.""")


surface = make_function(SurfaceFactory)


##############################################################################
class IsoSurfaceFactory(ContourModuleFactory):
    """Applies the IsoSurface mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.IsoSurface, ())


iso_surface = make_function(IsoSurfaceFactory)


##############################################################################
class ContourSurfaceFactory(ContourModuleFactory):
    """Applies the Surface mayavi module to the given data
       source (Mayavi source, or VTK dataset) and turns contours on.
    """
    _target = Instance(modules.Surface, ())

    def __init__(self, *args, **kwargs):
        """ Overriding the __init__ to turn contours on."""
        super(ContourSurfaceFactory, self).__init__(*args, **kwargs)
        self._contours_changed()


contour_surface = make_function(ContourSurfaceFactory)


##############################################################################
class ImageActorFactory(DataModuleFactory):
    """Applies the ImageActor mayavi module to the given VTK data object."""
    _target = Instance(modules.ImageActor, ())

    interpolate = Bool(True, adapts='actor.interpolate',
                       desc="""if the pixels in the image are to be
                       interpolated or not.""")

    opacity = Range(0.0, 1.0, 1.0, adapts='actor.opacity',
                    desc="""the opacity of the image.""")


image_actor = make_function(ImageActorFactory)


##############################################################################
class ImagePlaneWidgetFactory(DataModuleFactory):
    """ Applies the ImagePlaneWidget mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.ImagePlaneWidget, ())

    slice_index = CInt(0, adapts='ipw.slice_index',
                        help="""The index along wich the
                                            image is sliced.""")

    plane_opacity = Range(0.0, 1.0, 1.0, adapts='ipw.plane_property.opacity',
                    desc="""the opacity of the plane actor.""")

    plane_orientation = Enum('x_axes', 'y_axes', 'z_axes',
                        adapts='ipw.plane_orientation',
                        desc="""the orientation of the plane""")

image_plane_widget = make_function(ImagePlaneWidgetFactory)


##############################################################################
class ScalarCutPlaneFactory(CutPlaneFactory):
    """ Applies the ScalarCutPlane mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.ScalarCutPlane, ())

scalar_cut_plane = make_function(ScalarCutPlaneFactory)


##############################################################################
class VectorCutPlaneFactory(CutPlaneFactory, VectorsFactory):
    """ Applies the VectorCutPlane mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.VectorCutPlane, ())

vector_cut_plane = make_function(VectorCutPlaneFactory)


##############################################################################
class ContourGridPlaneFactory(ContourModuleFactory):
    """ Applies the ContourGridPlane mayavi module to the given data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.ContourGridPlane, ())

contour_grid_plane = make_function(ContourGridPlaneFactory)


##############################################################################
class CustomGridPlaneFactory(ContourModuleFactory):
    """ Applies the CustomGridPlane mayavi module to the given VTK data
        source (Mayavi source, or VTK dataset).
    """
    _target = Instance(modules.CustomGridPlane, ())

custom_grid_plane = make_function(CustomGridPlaneFactory)


##############################################################################
class VolumeFactory(PipeFactory):
    """ Applies the Volume mayavi module to the given VTK data
        source (Mayavi source, or VTK dataset).

        **Note**

        The range of the colormap can be changed simply using the
        vmin/vmax parameters (see below). For more complex modifications of
        the colormap, here is some pseudo code to change the ctf (color
        transfer function), or the otf (opacity transfer function)::

            vol = mlab.pipeline.volume(src)

            # Changing the ctf:
            from tvtk.util.ctf import ColorTransferFunction
            ctf = ColorTransferFunction()
            ctf.add_rgb_point(value, r, g, b)  # r, g, and b are float
                                               # between 0 and 1
            ctf.add_hsv_point(value, h, s, v)
            # ...
            vol._volume_property.set_color(ctf)
            vol._ctf = ctf
            vol.update_ctf = True

            # Changing the otf:
            from tvtk.util.ctf import PiecewiseFunction
            otf = PiecewiseFunction()
            otf.add_point(value, opacity)
            vol._otf = otf
            vol._volume_property.set_scalar_opacity(otf)

        Also, it might be useful to change the range of the ctf::

            ctf.range = [0, 1]
    """

    color = Trait(None, None,
                TraitTuple(Range(0., 1.), Range(0., 1.), Range(0., 1.)),
                help="""the color of the vtk object. Overides the colormap,
                        if any, when specified. This is specified as a
                        triplet of float ranging from 0 to 1, eg (1, 1,
                        1) for white.""", )

    vmin = Trait(None, None, CFloat,
                    help="""vmin is used to scale the transparency
                            gradient. If None, the min of the data will be
                            used""")

    vmax = Trait(None, None, CFloat,
                    help="""vmax is used to scale the transparency
                            gradient. If None, the max of the data will be
                            used""")

    _target = Instance(modules.Volume, ())

    __last_vrange = Any(None)

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _color_changed(self):
        if not self.color:
            return
        range_min, range_max = self._target.current_range
        from tvtk.util.ctf import ColorTransferFunction
        ctf = ColorTransferFunction()
        try:
            ctf.range = (range_min, range_max)
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass

        r, g, b = self.color
        ctf.add_rgb_point(range_min, r, g, b)
        ctf.add_rgb_point(range_max, r, g, b)

        self._target._ctf = ctf
        self._target._volume_property.set_color(ctf)
        self._target.update_ctf = True

    def _vmin_changed(self):
        vmin = self.vmin
        vmax = self.vmax
        range_min, range_max = self._target.current_range
        if vmin is None:
            vmin = range_min
        if vmax is None:
            vmax = range_max

        # Change the opacity function
        from tvtk.util.ctf import PiecewiseFunction, save_ctfs

        otf = PiecewiseFunction()
        if range_min < vmin:
            otf.add_point(range_min, 0.)
        if range_max > vmax:
            otf.add_point(range_max, 0.2)
        otf.add_point(vmin, 0.)
        otf.add_point(vmax, 0.2)
        self._target._otf = otf
        self._target._volume_property.set_scalar_opacity(otf)
        if self.color is None and \
           ((self.vmin is not None) or (self.vmax is not None)):
            # FIXME: We don't use 'rescale_ctfs' because it screws up the
            # nodes, this is because, the values are actually scaled between
            # the specified vmin/vmax and NOT the full range of values
            # specified in the CTF or in the volume object.
            if self.__last_vrange:
                last_min, last_max = self.__last_vrange
            else:
                last_min, last_max = range_min, range_max

            def _rescale_value(x):
                nx = (x - last_min) / (last_max - last_min)
                return vmin + nx * (vmax - vmin)

            # For some reason on older versions of VTK (< 8.1 at least),
            # The range trait is not updated correctly when the rgb points
            # are added, this causes problems so we explicitly update them.
            self._target._ctf.update_traits()
            scale_min, scale_max = self._target._ctf.range

            def _rescale_node(x):
                nx = (x - scale_min) / (scale_max - scale_min)
                return range_min + nx * (range_max - range_min)

            if hasattr(self._target._ctf, 'nodes'):
                rgb = list()
                for value in self._target._ctf.nodes:
                    r, g, b = \
                            self._target._ctf.get_color(value)
                    rgb.append((_rescale_node(value), r, g, b))
            else:
                rgb = save_ctfs(self._target.volume_property)['rgb']

            from tvtk.util.ctf import ColorTransferFunction
            ctf = ColorTransferFunction()
            try:
                ctf.range = (range_min, range_max)
            except Exception:
                # VTK versions < 5.2 don't seem to need this.
                pass
            rgb.sort()
            v = rgb[0]
            ctf.add_rgb_point(range_min, v[1], v[2], v[3])
            for v in rgb:
                ctf.add_rgb_point(_rescale_value(v[0]), v[1], v[2], v[3])
            ctf.add_rgb_point(range_max, v[1], v[2], v[3])

            self._target._ctf = ctf
            self._target._volume_property.set_color(ctf)
            self.__last_vrange = vmin, vmax

        self._target.update_ctf = True

    # This is not necessary: the job is already done by _vmin_changed
    _vmax_changed = _vmin_changed

volume = make_function(VolumeFactory)


############################################################################
# Automatically generated modules from registry.
############################################################################
class _AutomaticModuleFactory(DataModuleFactory):
    """The base class for any auto-generated factory classes.

    NOTE: This class requires the `_metadata` trait be set to
    the metadata object for the object for which this is a factory.
    """

    # The target.
    _target = Property

    # The saved target that is created once and then always returned.
    _saved_target = Any(None)

    def _get__target(self):
        """Getter for the _target trait."""
        if self._saved_target is None:
            self._saved_target = self._metadata.get_callable()()

        return self._saved_target


def _make_functions(namespace):
    """Make the functions for adding modules and add them to the
    namespace automatically.
    """
    # Ignore these since they are already provided.
    ignore = ['axes', 'text', 'orientation_axes']
    for mod in registry.modules:
        func_name = camel2enthought(mod.id)
        class_name = mod.id
        if func_name.endswith('_module'):
            func_name = func_name[:-7]
            class_name = class_name[:-6]
        class_name = class_name + 'Factory'

        # Don't create any that are already defined or ignored.
        if class_name in namespace or func_name in ignore:
            continue

        # The class to wrap.
        klass = new_class(
            class_name, (_AutomaticModuleFactory,), {'__doc__': mod.help, }
        )
        klass._metadata = mod
        # The mlab helper function.
        func = make_function(klass)

        # Inject class/function into the namespace and __all__.
        namespace[class_name] = klass
        namespace[func_name] = func
        __all__.append(func_name)

# Create the module related functions.
_make_functions(locals())
