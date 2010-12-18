.. _modules:

Modules
~~~~~~~

Modules are the objects that perform the visualization itself: they use
data to create the visual elements on the scene.

Here is a list of the Mayavi modules along with a brief description.

   :Axes:   
         Draws simple axes.

   :ContourGridPlane:
          A contour grid plane module. This module lets one take a
          slice of input grid data and view contours of the data.

   :CustomGridPlane:
          A custom grid plane with a lot more flexibility than
          GridPlane module.

   :Glyph:  
          Displays different types of glyphs oriented and colored
          as per scalar or vector data at the input points.

   :GridPlane:
          A simple grid plane module.

   :HyperStreamline:
          A  module that integrates through a tensor field to generate a
          hyperstreamline. The integration is along the maximum
          eigenvector and the cross section of the hyperstreamline is
          defined by the two other eigenvectors. Thus the shape of the
          hyperstreamline is "tube-like", with the cross  section being
          elliptical. Hyperstreamlines are used to visualize tensor
          fields.

   :ImageActor:
          A simple module to view image data efficiently.

   :ImagePlaneWidget:
          A simple module to view image data along a cut.

   :IsoSurface:
          A module that allows the user to make contours of input
          volumetric data.

   :Labels:
          Allows a user to label the current dataset or the current
          actor of the active module.

   :OrientationAxes:
          Creates small axes on the side that indicates the
          position of the co-ordinate axes and thereby marks the
          orientation of the scene. Requires VTK-4.5 and above.

   :Outline:
          A module that draws an outline for the given data.

   :ScalarCutPlane:
          Takes a cut plane of any input data set along an
          implicit plane and plots the data with optional
          contouring and scalar warping.

   :SliceUnstructuredGrid:
          This module takes a slice of the unstructured grid data
          and shows the cells that intersect or touch the slice.

   :Streamline:
          Allows the user to draw streamlines for given vector
          data. This supports various types of seed objects (line,
          sphere, plane and point seeds). It also allows the user
          to draw ribbons or tubes and further supports different
          types of interactive modes of calculating the
          streamlines.

   :StructuredGridOutline:
          Draws a grid-conforming outline for structured grids.

   :Surface:
          Draws a surface for any input dataset with optional contouring.

   :TensorGlyph:
          Displays tensor glyphs oriented and colored as per scalar or
          vector data at the input points.

   :Text:
          This module allows the user to place text on the screen.

   :VectorCutPlane:
          Takes an arbitrary slice of the input data along an
          implicit cut plane and places glyphs according to the
          vector field data. The glyphs may be colored using
          either the vector magnitude or the scalar attributes.

   :Vectors:
          Displays different types of glyphs oriented and colored
          as per vector data at the input points. This is merely a
          convenience module that is entirely based on the Glyph
          module.

   :Volume:
          The Volume module visualizes scalar fields using
          volumetric visualization techniques.

   :WarpVectorCutPlane:
          Takes an arbitrary slice of the input data using an
          implicit cut plane and warps it according to the vector
          field data. The scalars are displayed on the warped
          surface as colors.


