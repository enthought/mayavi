"""Actions to start various modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.pyface.action.api import Action

# Local imports.
from enthought.mayavi.plugins_e3.script import get_imayavi


######################################################################
# `AxesModule` class.
######################################################################
class AxesModule(Action):
    """ An action that creates an Axes module. """
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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.core.module_manager import ModuleManager
        mm = ModuleManager()
        mv = get_imayavi(self.window)
        mv.add_module(mm)


######################################################################
# `OrientationAxesModule` class.
######################################################################
class OrientationAxesModule(Action):
    """ An action that starts an orientation axes module. """
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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.modules.warp_vector_cut_plane import WarpVectorCutPlane
        m = WarpVectorCutPlane()
        mv = get_imayavi(self.window)        
        mv.add_module(m)
