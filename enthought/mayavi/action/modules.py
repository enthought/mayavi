"""Actions to start various modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.pyface.action.api import Action

# Local imports.
from enthought.mayavi.plugins.script import get_imayavi


######################################################################
# `AxesModule` class.
######################################################################
class AxesModule(Action):
    """ An action that creates an Axes module. """

    tooltip       = "Draw axes on the outline of input data"

    description   = "Draw cubical axes on the outline for given input"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.axes import Axes
        a = Axes()
        mv = get_imayavi(self.window)        
        mv.add_module(a)


######################################################################
# `ContourGridPlaneModule` class.
######################################################################
class ContourGridPlaneModule(Action):
    """ An action that creates a ContourGridPlane module. """

    tooltip       = "Shows a contour grid plane for the given input"

    description   = "Shows a contour grid plane for the given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.contour_grid_plane import ContourGridPlane
        m = ContourGridPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(m)


######################################################################
# `CustomGridPlaneModule` class.
######################################################################
class CustomGridPlaneModule(Action):
    """ An action that creates a CustomGridPlane module. """

    tooltip       = "Creates a highly customizable grid plane for given input"

    description   = "Creates a highly customizable grid plane for given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.custom_grid_plane import CustomGridPlane
        m = CustomGridPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(m)

######################################################################
# `GlyphModule` class.
######################################################################
class GlyphModule(Action):
    """ An action that creates a Glyph module. """

    tooltip       = "Creates colored and scaled glyphs at at input points"

    description   = "Creates colored and scaled glyphs at at input points"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.glyph import Glyph
        m = Glyph()
        mv = get_imayavi(self.window)        
        mv.add_module(m)

######################################################################
# `GridPlaneModule` class.
######################################################################
class GridPlaneModule(Action):
    """ An action that creates a GridPlane module. """

    tooltip       = "Shows a grid plane for the given input"

    description   = "Shows a grid plane for the given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.grid_plane import GridPlane
        gp = GridPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(gp)
        
######################################################################
# `HyperStreamlineModule` class.
######################################################################
class HyperStreamlineModule(Action):
    """ An action that creates a HyperStreamline module. """

    tooltip       = "Shows hyper streamlines for tensor data"

    description   = "Shows hyper streamlines for tensor data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.hyper_streamline import HyperStreamline
        h = HyperStreamline()
        mv = get_imayavi(self.window)        
        mv.add_module(h)


######################################################################
# `ImageActorModule` class.
######################################################################
class ImageActorModule(Action):
    """ An action that creates an ImageActor module. """

    tooltip       = "Shows an image actor for image data"

    description   = "Shows an image actor for image data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.image_actor import ImageActor
        i = ImageActor()
        mv = get_imayavi(self.window)        
        mv.add_module(i)

 
######################################################################
# `ImagePlaneWidgetModule` class.
######################################################################
class ImagePlaneWidgetModule(Action):
    """ An action that creates an ImagePlaneWidget module. """

    tooltip       = "Shows an image plane widget for image data"

    description   = "Shows an image plane widget for image data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.image_plane_widget import ImagePlaneWidget
        ipw = ImagePlaneWidget()
        mv = get_imayavi(self.window)        
        mv.add_module(ipw)


######################################################################
# `IsoSurfaceModule` class.
######################################################################
class IsoSurfaceModule(Action):
    """ An action that creates a IsoSurface module. """

    tooltip       = "Creates an iso-surface for the given input"

    description   = "Creates an iso-surface for the given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.iso_surface import IsoSurface
        iso = IsoSurface()
        mv = get_imayavi(self.window)        
        mv.add_module(iso)


######################################################################
# `AddModuleManager` class.
######################################################################
class AddModuleManager(Action):
    """ An action that adds a ModuleManager to the tree. """

    tooltip       = "Add a ModuleManager to the current source/filter"

    description   = "Add a ModuleManager to the current source/filter"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.core.module_manager import ModuleManager
        mm = ModuleManager()
        mv = get_imayavi(self.window)
        mv.add_module(mm)

######################################################################
# `LabelsModule` class.
######################################################################
class LabelsModule(Action):

    tooltip       = "Display labels for active dataset or active module"

    description   = "Display labels for active dataset or active module"
    
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.labels import Labels
        mv = get_imayavi(self.window)
        object = mv.current_object
        m = Labels(object=object)
        mv.add_module(m)


######################################################################
# `OrientationAxesModule` class.
######################################################################
class OrientationAxesModule(Action):
    """ An action that starts an orientation axes module. """

    tooltip       = "Show an axes indicating the current orientation"

    description   = "Show an axes indicating the current orientation"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.orientation_axes import OrientationAxes
        o = OrientationAxes()
        mv = get_imayavi(self.window)        
        mv.add_module(o)


######################################################################
# `OutlineModule` class.
######################################################################
class OutlineModule(Action):
    """ An action that starts an outline module. """

    tooltip       = "Draw an outline for given input"

    description   = "Draw an outline for given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.outline import Outline
        o = Outline()
        mv = get_imayavi(self.window)        
        mv.add_module(o)


######################################################################
# `ScalarCutPlaneModule` class.
######################################################################
class ScalarCutPlaneModule(Action):
    """ An action that creates a scalar cut plane module. """

    tooltip       = "Slice through the data with optional contours"

    description   = "Slice through the data with optional contours"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.scalar_cut_plane import ScalarCutPlane
        s = ScalarCutPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(s)


######################################################################
# `SliceUnstructuredGridModule` class.
######################################################################
class SliceUnstructuredGridModule(Action):
    """ An action that creates a scalar cut plane module. """

    tooltip       = "Slice an unstructured grid to show cells"

    description   = "Slice an unstructured grid to show cells"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.slice_unstructured_grid import SliceUnstructuredGrid
        s = SliceUnstructuredGrid()
        mv = get_imayavi(self.window)        
        mv.add_module(s)


######################################################################
# `StreamlineModule` class.
######################################################################
class StreamlineModule(Action):
    """ An action that starts a streamline module. """

    tooltip       = "Generate streamlines for the vectors"

    description   = "Generate streamlines for the vectors"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.streamline import Streamline
        s = Streamline()
        mv = get_imayavi(self.window)        
        mv.add_module(s)


######################################################################
# `StructuredGridOutlineModule` class.
######################################################################
class StructuredGridOutlineModule(Action):
    """ An action that starts a streamline module. """

    tooltip       = "Draw a grid-conforming outline for structured grids"

    description   = "Draw a grid-conforming outline for structured grids"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.structured_grid_outline \
             import StructuredGridOutline
        s = StructuredGridOutline()
        mv = get_imayavi(self.window)        
        mv.add_module(s)


######################################################################
# `SurfaceModule` class.
######################################################################
class SurfaceModule(Action):
    """ An action that starts an outline module. """

    tooltip       = "Creates a surface for the given input"

    description   = "Creates a surface for the given input"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.surface import Surface
        s = Surface()
        mv = get_imayavi(self.window)        
        mv.add_module(s)

######################################################################
# `TensorGlyphModule` class.
######################################################################
class TensorGlyphModule(Action):
    """ An action that creates a TensorGlyph module. """

    tooltip       = "Displays glyphs scaled and oriented as per tensor data"

    description   = "Displays glyphs scaled and oriented as per tensor data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.tensor_glyph import TensorGlyph
        h = TensorGlyph()
        mv = get_imayavi(self.window)        
        mv.add_module(h)
 
######################################################################
# `TextModule` class.
######################################################################
class TextModule(Action):
    """ An action that starts a text module. """

    tooltip       = "Displays text on screen"

    description   = "Displays user specified text on screen"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.text import Text
        t = Text()
        mv = get_imayavi(self.window)        
        mv.add_module(t)

######################################################################
# `VectorCutPlaneModule` class.
######################################################################
class VectorCutPlaneModule(Action):
    """ An action that creates a VecturCutPlane module. """

    tooltip       = "Display vectors along a cut plane"

    description   = "Display vectors along a cut plane"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.vector_cut_plane import VectorCutPlane
        m = VectorCutPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(m)

######################################################################
# `Vectors` class.
######################################################################
class VectorsModule(Action):
    """ An action that creates a Vectors module. """

    tooltip       = "Display input vectors using arrows or other glyphs"

    description   = "Display input vectors using arrows or other glyphs"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.vectors import Vectors
        m = Vectors()
        mv = get_imayavi(self.window)        
        mv.add_module(m)

######################################################################
# `VolumeModule` class.
######################################################################
class VolumeModule(Action):
    """ An action that creates a Volume module. """

    tooltip       = "Use volume rendering to view the scalar field"

    description   = "Use volume rendering to view the scalar field"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.volume import Volume
        m = Volume()
        mv = get_imayavi(self.window)        
        mv.add_module(m)

######################################################################
# `WarpVectorCutPlaneModule` class.
######################################################################
class WarpVectorCutPlaneModule(Action):
    """ An action that creates a WarpVectorCutPlane module. """

    tooltip       = "Warp cut plane along scaled input vectors"

    description   = "Warp cut plane along scaled input vectors"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.warp_vector_cut_plane import WarpVectorCutPlane
        m = WarpVectorCutPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(m)
