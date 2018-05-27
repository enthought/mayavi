.. _filters:


Filters
~~~~~~~
Filters transform the data, but do not display it. They are used as an
intermediate between the data sources and the modules.

Here is a list of the Mayavi Filters.

   :CellDerivatives:
          Computes derivatives from input point scalar and vector data
          and produces cell data on the gradients.  Can be used to
          approximately calculate the vorticity for example.

   :CellToPointData:
          Transforms cell attribute data to point data by
          averaging the cell data from the cells at the point.

   :Contour:
          A contour filter that wraps around the Contour component to
          generate iso-surfaces on any input dataset.
    
   :CutPlane:
          This filter represents a cut plane that can be used to slice
          through any dataset.  It also provides a 3D widget interface
          to position and move the slice interactively.

   :DataSetClipper:
	  This filter clips the dataset in an area.  The area can be
	  defined interactively as a box, a sphere...

   :DecimatePro:
          Reduces the number of triangles in a triangular mesh by
          approximating the original mesh.

   :Delaunay2D:
          Performs a 2D Delaunay triangulation.

   :Delaunay3D:
          Performs a 3D Delaunay triangulation.

   :ElevationFilter:
          Creates scalar data corresponding to the elevation of the
          points along a line.

   :ExtractEdges:
          This filter extracts cell edges from any input data.

   :ExtractGrid:
          Allows a user to select a part of a structured grid.

   :ExtractTensorComponents:
          Wraps the TVTK ``ExtractTensorComponents`` filter to extract
          components from a tensor field.

   :ExtractUnstructuredGrid:
          Allows a user to select a part of an unstructured grid.

   :ExtractVectorNorm:
          Computes the norm (Euclidean) of the input vector data
          (with optional scaling between [0, 1]). This is useful
          when the input data has vector input but no scalar data
          for the magnitude of the vectors.
	  
   :ExtractVectorComponents:
	  Wraps the TVTK ExtractVectorComponents filter to extract
	  components of a vector. This is useful for analyzing
	  individual components of a vector data.

   :GaussianSplatter:
          This filter splat points into a volume with an elliptical,
          Gaussian distribution. This is useful to estimate a density
          field from a set of scattered points.

   :GreedyTerrainDecimation:
          Approximates a height field (2D image data) with a triangle mesh,
          keeping the number of triangles minimum.

   :ImageChangeInformation:
          A filter that can be used to change the origin, spacing and
          extents of an input image data dataset without changing the
          data itself.

   :ImageDataProbe:
          A filter that can be used to probe any dataset using a
          Structured Points dataset.  The filter also allows one to
          convert the scalar data to an unsigned short array so that the
          scalars can be used for volume visualization.

   :MaskPoints:
          Selectively passes the input points downstream. This can
          be used to subsample the input points.  Note that this
          does not pass geometry data, this means all grid
          information is lost.

   :PointToCellData:
          Does the inverse of the CellToPointData filter: converts data
          located on the points to data located on the cells.

   :PolyDataNormals:
          Computes normals from input data. This gives meshes a
          smoother appearance. This should work for any input
          dataset. Note: this filter is called "Compute Normals"
          in Mayavi2 GUI (Visualize/Filters/Compute Normals).

   :QuadricDecimation:
          Reduce triangles in a mesh, forming a good approximation of the
          original mesh.

   :SelectOutput:
          A filter that allows a user to select one among several of the
          outputs of a given input.  This is typically very useful for a
          multi-block data source.

   :SetActiveAttribute:
          This filter lets a user set the active data attribute
          (scalars, vectors and tensors) on a VTK dataset.  This is
          particularly useful if you need to do something like compute
          contours of one scalar on the contour of another scalar.

   :Stripper:
	  Create triangle strips and/or poly-lines. Useful for regularizing
	  broken up surfaces, such as those created by the Tube filter.

   :Threshold:
          A simple filter that thresholds on input data.

   :TransformData:
          Performs a linear transformation to input data.

   :Tube:
          Turns lines into tubes.

   :UserDefined:
          This filter lets the user define their own filter
          dynamically/interactively.     

   :Vorticity:
          This filter computes the vorticity of an input vector field.
          For convenience, the filter allows one to optionally
          pass-through the given input vector field.  The filter also
          allows the user to show the component of the vorticity along a
          particular cartesian co-ordinate axes.  It produces point data
          on output which is ready to visualize.
    
   :WarpScalar:
          Warps the input data along a particular direction
          (either the normals or a specified direction) with a
          scale specified by the local scalar value. Useful for
          making carpet plots. The scalar value of a dataset can be, for
          instance, converted in elevation.

   :WarpVector:
          Warps the input data along the point vector attribute
          scaled as per a scale factor.  Useful for showing flow
          profiles or displacements.

