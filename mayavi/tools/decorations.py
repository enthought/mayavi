"""
Functions for adding decorations (axes, colorbar, outlines..) to the
pipeline in a procedural way.
"""

# Author: Gael Varoquaux
# Copyright (c) 2007-2015 Enthought, Inc.
# License: BSD Style.

import numbers

import numpy as np

# Enthought library imports.
from traits.api import String, CFloat, Instance, HasTraits, \
            Trait, CArray, true, Any, Range, Either
from . import tools
from .figure import draw, gcf

# Mayavi imports
from mayavi.core.utils import DataSetHelper
import mayavi.modules.api as modules
from .pipe_base import make_function
from .modules import ModuleFactory
from .engine_manager import get_engine, engine_manager

#############################################################################
# Colorbar related functions


def _orient_colorbar(lut_mgr, orientation):
    """Orients the given LUTManager (make it horizontal or vertical).
    """
    rep = lut_mgr.scalar_bar_representation
    colorbar = lut_mgr.scalar_bar
    if orientation == "vertical":
        if rep is None:
            # VTK < 5.2
            colorbar.orientation = "vertical"
        else:
            rep.orientation = 1
            rep.position = (0.01, 0.15)
            rep.position2 = (0.1, 0.8)
        colorbar.width = 0.1
        colorbar.height = 0.8
        colorbar.position = (0.01, 0.15)
    elif orientation == "horizontal":
        if rep is None:
            colorbar.orientation = "horizontal"
        else:
            rep.orientation = 0
            rep.position = (0.1, 0.01)
            rep.position2 = (0.8, 0.17)
        colorbar.width = 0.8
        colorbar.height = 0.17
        colorbar.position = (0.1, 0.01)
    else:
        raise ValueError("Unknown orientation: %s" % orientation)
    draw()


def _lut_manager_properties(lut_manager, **props):
    """ Internal function used to apply properties to a colorbar.
    """
    need_redraw = False
    orientation = props.get('orientation', None)
    if orientation is not None:
        _orient_colorbar(lut_manager, orientation)

    colorbar = lut_manager.scalar_bar
    title = props.get('title', None)
    if title is not None:
        colorbar.title = title
        need_redraw = True

    label_fmt = props.get('label_fmt', None)
    if label_fmt is not None:
        colorbar.label_format = label_fmt
        need_redraw = True

    nb_labels = props.get('nb_labels', None)
    if nb_labels is not None:
        colorbar.number_of_labels = nb_labels
        need_redraw = True

    nb_colors = props.get('nb_colors', None)
    if nb_colors is not None:
        colorbar.maximum_number_of_colors = nb_colors
        need_redraw = True

    if need_redraw:
        draw()


def scalarbar(object=None, title=None, orientation=None,
                           nb_labels=None, nb_colors=None,
                           label_fmt=None):
    """Adds a colorbar for the scalar color mapping of the given object.

    If no object is specified, the first object with scalar data in the scene
    is used.

    **Keyword arguments**:

        :object: Optional object to get the scalar color map from

        :title: The title string

        :orientation: Can be 'horizontal' or 'vertical'

        :nb_labels: The number of labels to display on the colorbar.

        :label_fmt: The string formater for the labels. This needs to be
                    a formater for float number, eg '%.1f'.

        :nb_colors: The maximum number of colors displayed on the
                    colorbar.
    """
    module_manager = tools._find_module_manager(object=object,
                                                    data_type="scalar")
    if module_manager is None:
        return
    if not module_manager.scalar_lut_manager.show_scalar_bar:
        if title is None:
            title = ''
        if orientation is None:
            orientation = 'horizontal'
    lut_mgr = module_manager.scalar_lut_manager
    module_manager.scalar_lut_manager.show_scalar_bar = True
    _lut_manager_properties(lut_mgr, title=title, orientation=orientation,
                        nb_labels=nb_labels, nb_colors=nb_colors,
                        label_fmt=label_fmt)
    return lut_mgr


def vectorbar(object=None, title=None, orientation=None,
                           nb_labels=None, nb_colors=None,
                           label_fmt=None):
    """Adds a colorbar for the vector color mapping of the given object.

    If no object is specified, the first object with vector data in the scene
    is used.

    **Keyword arguments**

        :object: Optional object to get the vector color map from

        :title: The title string

        :orientation: Can be 'horizontal' or 'vertical'

        :nb_labels: The number of labels to display on the colorbar.

        :label_fmt: The string formater for the labels. This needs to be
                    a formater for float number, eg '%.1f'.

        :nb_colors: The maximum number of colors displayed on the
                    colorbar.
    """
    module_manager = tools._find_module_manager(object=object,
                                                    data_type="vector")
    if module_manager is None:
        return
    if not module_manager.vector_lut_manager.show_scalar_bar:
        if title is None:
            title = ''
        orientation = 'horizontal'
    lut_mgr = module_manager.vector_lut_manager
    lut_mgr.show_scalar_bar = True
    _lut_manager_properties(lut_mgr, title=title, orientation=orientation,
                        nb_labels=nb_labels, nb_colors=nb_colors,
                        label_fmt=label_fmt)
    return lut_mgr


def colorbar(object=None, title=None, orientation=None,
                           nb_labels=None, nb_colors=None,
                           label_fmt=None):
    """Adds a colorbar for the color mapping of the given object.

    If the object has scalar data, the scalar color mapping is
    represented. Elsewhere the vector color mapping is represented, if
    available.
    If no object is specified, the first object with a color map in the scene
    is used.

    **Keyword arguments**:

        :object: Optional object to get the color map from

        :title: The title string

        :orientation: Can be 'horizontal' or 'vertical'

        :nb_labels: The number of labels to display on the colorbar.

        :label_fmt: The string formater for the labels. This needs to be
                    a formater for float number, eg '%.1f'.

        :nb_colors: The maximum number of colors displayed on the
                    colorbar.
    """
    colorbar = scalarbar(object=object, title=title, orientation=orientation,
                            nb_labels=nb_labels, nb_colors=nb_colors,
                            label_fmt=label_fmt)
    if colorbar is None:
        colorbar = vectorbar(object=object, title=title,
                                orientation=orientation,
                                nb_labels=nb_labels, nb_colors=nb_colors,
                                label_fmt=label_fmt)
    return colorbar


#############################################################################
class SingletonModuleFactory(ModuleFactory):
    """ Base classe for factories that can find an existing object
    matching certain criteria instead of building a new one"""

    # The parent object on which this module is going to be added.
    _parent = Any

    def __init__(self, *args, **kwargs):
        """ Try to find an module actor with the same name, on the given
        parent (if any) and use it rather than building a new module."""
        # Call the HasTraits constructor, but not the PipeBase one.
        HasTraits.__init__(self)
        self._scene = gcf()
        if not 'figure' in kwargs:
            self._engine = get_engine()
        else:
            figure = kwargs['figure']
            self._engine = engine_manager.find_figure_engine(figure)
            self._engine.current_scene = figure
            kwargs.pop('figure')
        if self._scene.scene is not None:
            self._scene.scene.disable_render = True
        # Process the arguments
        if len(args) == 1:
            (parent, ) = args
        elif len(args) == 0:
            parent = self._engine.current_object
        else:
            raise ValueError("Wrong number of arguments")

        # Try to find an existing module, if not add one to the pipeline
        if parent is None:
            target = self._scene
        else:
            target = parent

        klass = self._target.__class__

        for obj in tools._traverse(target):
            if (isinstance(obj, klass)
                        and obj.name == self.name):
                self._target = obj
                break
        else:
            # Keep a reference to the parent
            self._parent = parent
            self._engine.add_module(self._target, obj=parent)

        # Now calling the traits setter, so that traits handlers are
        # called
        self.trait_set(**kwargs)
        if self._scene.scene is not None:
            self._scene.scene.disable_render = False


#############################################################################
class AxesLikeModuleFactory(SingletonModuleFactory):
    """ Base class for axes and outline"""

    extent = CArray(shape=(6,),
                    help="""[xmin, xmax, ymin, ymax, zmin, zmax]
                            Default is the object's extents.""", )

    def _extent_changed(self):
        """ There is no universal way of setting extents for decoration
            objects. This should be implemented in subclasses
        """
        pass

    # Override the color and opacity handlers: axes and outlines do not
    # behave like other modules

    def _color_changed(self):
        if self.color:
            try:
                self._target.property.color = self.color
            except AttributeError:
                try:
                    self._target.actor.property.color = self.color
                except AttributeError:
                    pass

    def _opacity_changed(self):
        try:
            self._target.property.opacity = self.opacity
        except AttributeError:
            try:
                self._target.actor.property.opacity = self.opacity
            except AttributeError:
                pass

    def __init__(self, *args, **kwargs):
        """ Overide the call method to be able to catch the extents of
            the object, if any.
        """
        SingletonModuleFactory.__init__(self, *args, **kwargs)
        if not 'extent' in kwargs:
            try:
                # XXX: Do not use tools.set_extent, as it does not work
                # on axes.
                self.extent = self._parent.actor.actor.bounds
            except AttributeError:
                """ Either this is not a module, or it has no actors"""


#############################################################################
class Outline(AxesLikeModuleFactory):
    """ Creates an outline for the current (or given) object."""

    _target = Instance(modules.Outline, ())

    def _extent_changed(self):
        self._target.manual_bounds = True
        self._target.bounds = self.extent


outline = make_function(Outline)


#############################################################################
class Axes(AxesLikeModuleFactory):
    """ Creates axes for the current (or given) object."""

    xlabel = String(None, adapts='axes.x_label',
                help='the label of the x axis')

    ylabel = String(None, adapts='axes.y_label',
                help='the label of the y axis')

    zlabel = String(None, adapts='axes.z_label',
                help='the label of the z axis')

    nb_labels = Range(0, 50, 2, adapts='axes.number_of_labels',
                desc='The number of labels along each direction')

    ranges = Trait(None, None, CArray(shape=(6,)),
                    help="""[xmin, xmax, ymin, ymax, zmin, zmax]
                            Ranges of the labels displayed on the axes.
                            Default is the object's extents.""", )

    x_axis_visibility = true(adapts='axes.x_axis_visibility',
                help="Whether or not the x axis is visible (boolean)")

    y_axis_visibility = true(adapts='axes.y_axis_visibility',
                help="Whether or not the y axis is visible (boolean)")

    z_axis_visibility = true(adapts='axes.z_axis_visibility',
                help="Whether or not the z axis is visible (boolean)")

    _target = Instance(modules.Axes, ())

    def _extent_changed(self):
        """ Code to modify the extents for
        """
        axes = self._target
        axes.axes.use_data_bounds = False
        axes.axes.bounds = self.extent
        if self.ranges is None:
            dsh = DataSetHelper(axes.module_manager.source.outputs[0])
            axes.axes.ranges = dsh.get_bounds()

    def _ranges_changed(self):
        if self.ranges is not None:
            self._target.axes.ranges = self.ranges
            self._target.axes.use_ranges = True

axes = make_function(Axes)


def xlabel(text, object=None):
    """
    Creates a set of axes if there isn't already one, and sets the x label

    **Keyword arguments**:

        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, xlabel=text)


def ylabel(text, object=None):
    """
    Creates a set of axes if there isn't already one, and sets the y label

    **Keyword arguments**:


        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, ylabel=text)


def zlabel(text, object=None):
    """
    Creates a set of axes if there isn't already one, and sets the z label

    **Keyword arguments**

        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, zlabel=text)


##############################################################################
class OrientationAxesFactory(SingletonModuleFactory):
    """Applies the OrientationAxes mayavi module to the given VTK data object.
    """

    xlabel = String(None, adapts='axes.x_axis_label_text',
                help='the label of the x axis')

    ylabel = String(None, adapts='axes.y_axis_label_text',
                help='the label of the y axis')

    zlabel = String(None, adapts='axes.z_axis_label_text',
                help='the label of the z axis')

    _target = Instance(modules.OrientationAxes, ())

orientation_axes = make_function(OrientationAxesFactory)


###############################################################################
class Text(ModuleFactory):
    """ Adds a text on the figure.

        **Function signature**::

            text(x, y, text, ...)

        x, and y are the position of the origin of the text. If no z
        keyword argument is given, x and y are the 2D projection of the
        figure, they belong to [0, 1]. If a z keyword  argument is given, the
        text is positionned in 3D, in figure coordinnates.
        """

    width = Trait(None, None, CFloat, adapts='width',
                        help="""width of the text.""")

    z = Trait(None, None, CFloat,
              help="""Optional z position. When specified, the
                      text is positioned in 3D""")

    _target = Instance(modules.Text, ())

    opacity = CFloat(1, adapts="property.opacity",
                        help="""The opacity of the text.""")

    def __init__(self, x, y, text, **kwargs):
        """ Override init as for different positional arguments."""
        if 'z' in kwargs and kwargs['z'] is not None:
            self._target.z_position = kwargs['z']
            self._target.position_in_3d = True
        elif not (x <= 1. and x >= 0. and y >= 0. and y <= 1.):
            raise ValueError('Text positions should be in [0, 1] if no z'
                'position is given')
        super(Text, self).__init__(None, **kwargs)
        self._target.text = text
        self._target.x_position = x
        self._target.y_position = y


text = make_function(Text)


###############################################################################
class Text3D(ModuleFactory):
    """ Positions text at a 3D location in the scene.

        **Function signature**::

            text3d(x, y, z, text, ...)

        x, y, and z are the position of the origin of the text. The
        text is positionned in 3D, in figure coordinnates.
        """

    _target = Instance(modules.Text3D, ())

    scale = Either(CFloat(1), CArray(shape=(3,)),
                        help="""The scale of the text, in figure units.
                                Either a float, or 3-tuple of floats.""")

    orientation = CArray(shape=(3,), adapts='orientation',
                        desc="""the angles giving the orientation of the
                        text. If the text is oriented to the camera,
                        these angles are referenced to the axis of the
                        camera. If not, these angles are referenced to
                        the z axis.""")

    orient_to_camera = true(adapts='orient_to_camera',
                        desc="""if the text is kept oriented to the
                        camera, or is pointing in a specific direction,
                        regardless of the camera position.""")

    def __init__(self, x, y, z, text, **kwargs):
        """ Override init as for different positional arguments."""
        if not 'scale' in kwargs:
            kwargs['scale'] = 1
        super(Text3D, self).__init__(None, **kwargs)
        self._target.text = text
        self._target.position = (x, y, z)

    def _scale_changed(self):
        scale = self.scale
        if isinstance(scale, numbers.Number):
            scale = scale * np.ones((3,))
        self._target.scale = scale

text3d = make_function(Text3D)


#############################################################################
class Title(SingletonModuleFactory):
    """Creates a title for the figure.

    **Function signature**::

        title(text, ...)

    """

    size = CFloat(1, help="the size of the title")

    height = CFloat(0.8, adapts='y_position',
                         help="""height of the title, in portion of the
                                 figure height""")

    def _size_changed(self):
        self._target.width = min(0.05 * self.size * len(self._text), 1)
        self._target.x_position = 0.5 * (1 - self._target.width)

    _target = Instance(modules.Text)

    def __target_default(self):
        """ This is called only if no existing title is found."""
        width = min(0.05 * self.size * len(self._text), 1)
        text = modules.Text(text=self._text,
                            y_position=self.height,
                            x_position=0.5 * (1 - width),)
        text.width = width
        return text

    def __init__(self, text, **kwargs):
        self._text = text  # This will be used by _size_changed
        if not 'name' in kwargs:
            # The name is used as au unique marker to identify the
            # title. We need to set it ASAP.
            self.name = kwargs['name'] = 'Title'
        super(Title, self).__init__(**kwargs)
        self._target.text = self._text
        # We need to set position after Text is initiated, as text will
        # override these positions
        self._target.y_position = self.height
        self._size_changed()


title = make_function(Title)
