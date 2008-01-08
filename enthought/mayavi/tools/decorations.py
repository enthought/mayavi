"""
Functions for adding decorations (axes, colorbar, outlines..) to the
pipeline in a procedural way.
"""

# Author: Gael Varoquaux 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import numpy

# Enthought library imports.
import enthought.mayavi.modules.api as modules
from enthought.traits.api import String, CFloat, Instance, HasTraits, \
            Trait, CArray
import tools
from figure import draw, gcf
import types

# Mayavi imports
from pipe_base import make_function
from modules import ModuleFactory
from config import get_engine

#############################################################################
# Colorbar related functions

def _orient_colorbar(colorbar, orientation):
    """Orients the given colorbar (make it horizontal or vertical).
    """
    if orientation == "vertical":
        colorbar.orientation = "vertical"
        colorbar.width = 0.1
        colorbar.height = 0.8
        colorbar.position = (0.01, 0.15)
    elif orientation == "horizontal":
        colorbar.orientation = "horizontal"
        colorbar.width = 0.8
        colorbar.height = 0.17
        colorbar.position = (0.1, 0.01)
    else:
        print "Unknown orientation"
    draw()

def scalarbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the scalar color mapping of the given object.

    If no object is specified, the first object with scalar data in the scene 
    is used.

    Keyword arguments
    -----------------
    
        title -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
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
    colorbar = module_manager.scalar_lut_manager.scalar_bar
    if orientation is not None:
        _orient_colorbar(colorbar, orientation)
    module_manager.scalar_lut_manager.show_scalar_bar = True
    if title is not None:
        colorbar.title = title
        draw()
    return colorbar

def vectorbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the vector color mapping of the given object.

    If no object is specified, the first object with vector data in the scene 
    is used.

    Keyword arguments
    -----------------

        object -- Optional object to get the vector lut from
    
        title -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
    """
    module_manager = tools._find_module_manager(object=object, 
                                                    data_type="vector")
    if module_manager is None:
        return
    if not module_manager.vector_lut_manager.show_scalar_bar:
        if title is None:
            title = ''
        orientation = 'horizontal'
    colorbar = module_manager.vector_lut_manager.scalar_bar
    module_manager.vector_lut_manager.show_scalar_bar = True
    if orientation is not None:
        _orient_colorbar(colorbar, orientation)
    if title is not None:
        colorbar.title = title
        draw()
    return colorbar

def colorbar(object=None, title=None, orientation=None):
    """Adds a colorbar for the color mapping of the given object. 
    
    If the object has scalar data, the scalar color mapping is 
    represented. Elsewhere the vector color mapping is represented, if 
    available.
    If no object is specified, the first object with a color map in the scene 
    is used.

    Keyword arguments
    -----------------

        object -- Optional object to get the vector lut from
    
        title       -- The title string 

        orientation -- Can be 'horizontal' or 'vertical'
    """
    colorbar = scalarbar(object=object, title=title, orientation=orientation)
    if colorbar is None:
        colorbar = vectorbar(object=object, title=title, orientation=orientation)
    return colorbar

#############################################################################
class SingletonModuleFactory(ModuleFactory):
    """ Base classe for factories that can find an existing object
    matching certain criteria instead of building a new one"""

    def __init__(self, *args, **kwargs):
        """ Try to find an module actor with the same name, on the given 
        parent (if any) and use it rather than building a new module."""
        # Call the HasTraits constructor, but not the PipeBase one.
        HasTraits.__init__(self)
        self._scene = gcf()
        self._engine = get_engine() 
        self._scene.scene.disable_render = True
        # Process the arguments
        if len(args)==1:
            (parent, ) = args
        elif len(args)==0:
            parent = None
        else:
            raise ValueError, "Wrong number of arguments"

        # Try to find an existing module, if not add one to the pipeline
        if parent == None:
            target = self._scene
        else:
            target = parent
        
        klass = self._target.__class__

        for obj in tools._traverse(target):
            if ( isinstance(obj, klass)
                        and obj.name == self.name ):
                self._target = obj
                break
        else:
            self._engine.add_module(self._target, obj=parent)

        # Now calling the traits setter, so that traits handlers are
        # called
        self.set(**kwargs)
        #self._scene.scene.reset_zoom()
        self._scene.scene.disable_render = False


#############################################################################
class AxesLikeModuleFactory(SingletonModuleFactory):
    """ Base class for axes and outline"""

    extent = CArray(shape=(6,),
                    help="""[xmin, xmax, ymin, ymax, zmin, zmax]
                            Default is the object's extents.""", )

    def _extent_changed(self):
        tools._set_extent(self._target, self.extent)


#############################################################################
class Outline(AxesLikeModuleFactory):
    """ Creates an outline for the current (or given) object."""

    _target = Instance(modules.Outline, ())

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

    _target = Instance(modules.Axes, ())


axes = make_function(Axes)


def xlabel(text, object=None):
    """ 
    Creates a set of axes if there isn't already one, and sets the x label

    Keyword arguments
    -----------------
    
        object --  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, xlabel=text)


def ylabel(text, object=None):
    """ 
    Creates a set of axes if there isn't already one, and sets the y label

    Keyword arguments
    -----------------
    
        object --  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, ylabel=text)


def zlabel(text, object=None):
    """ 
    Creates a set of axes if there isn't already one, and sets the z label

    Keyword arguments
    -----------------
    
        object --  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    """
    return axes(object, zlabel=text)


###############################################################################
class Text(ModuleFactory):
    """ Adds a text on the figure.
    
        signature: text(x, y, text, ...) 
        x, and y are the position of the origin of
        the text on the 2D projection of the figure.
        """

    width = Trait(None, None, CFloat, adapts='width',
                        help="""width of the text.""")

    _target = Instance(modules.Text, ())

    def __init__(self, x, y, text, **kwargs):
        """ Override init as for diffreent positional arguments."""
        super(Text, self).__init__(None, **kwargs)
        self._target.text       = text
        self._target.x_position = x
        self._target.y_position = y

text = make_function(Text)


#############################################################################
class Title(SingletonModuleFactory):
    """Creates a title for the figure.

    signature: title(text, ...)
    """

    size = CFloat(1, help="the size of the title")

    height = CFloat(0.8, adapts='y_position',
                         help="""height of the title, in portion of the 
                                 figure height""")

    def _size_changed(self):
        self._target.width = min(0.05*self.size*len(self._text), 1)
        self._target.x_position = 0.5*(1 - self._target.width)

    _target = Instance(modules.Text)

    def __target_default(self):
        """ This is called only if no existing title is found."""
        width = min(0.05*self.size*len(self._text), 1)
        text= modules.Text(text=self._text, 
                            y_position=self.height,
                            x_position=0.5*(1 - width),)
        text.width =width
        return text

    def __init__(self, text, **kwargs):
        self._text = text # This will be used by _size_changed 
        super(Title, self).__init__(**kwargs)
        self._target.text = self._text

title = make_function(Title)

