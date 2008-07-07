
from numpy import c_, zeros, arange

from enthought.traits.api import HasTraits, \
    false, CArray, Traits, Instance

from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi.sources.array_source import ArraySource
from enthought.mayavi.core.source import Source

from enthought.tvtk.api import tvtk

ArrayOrNone = Traits(None, CArray)

############################################################################
# The DataSourceFactory class
############################################################################
class DataSourceFactory(HasTraits):
    """ Factory for creating data sources. The information about the 
        organisation of the data is given by setting the public traits.
    """

    # Whether the position is implicitely inferred from the array indices
    position_implicit = false

    # Whether the data is on an orthogonal grid
    orthogonal_grid = false

    # The position of the data points
    position_x = ArrayOrNone
    position_y = ArrayOrNone
    position_z = ArrayOrNone

    # Connectivity array. If none, it is implicitely inferred from the array 
    # indices
    connectivity_triangles = ArrayOrNone

    # Whether or not the data points should be connected.
    lines = false

    # The scalar data array
    scalar_data = ArrayOrNone

    # Whether there is vector data
    has_vector_data = false

    # The vector components
    vector_u = ArrayOrNone
    vector_v = ArrayOrNone
    vector_w = ArrayOrNone


    #----------------------------------------------------------------------
    # Private traits
    #----------------------------------------------------------------------
    
    _vtk_source = Instance(tvtk.DataSet)

    _mayavi_source = Instance(Source)


    #----------------------------------------------------------------------
    # Private interface
    #----------------------------------------------------------------------

    def _add_scalar_data(self):
        """ Adds the scalar data to the vtk source.
        """
        if self.scalar_data is not None:
            scalars = self.scalars.ravel()
            self._vtk_source.point_data.scalars = scalars


    def _add_vector_data(self):
        """ Adds the vector data to the vtk source.
        """
        if self.has_vector_data:
            vectors = c_[ self.vector_u.ravel(), 
                          self.vector_v.ravel(),
                          self.vector_w.ravel(),
                        ]
            self._vtk_source.point_data.vectors = vectors

    
    def _mk_polydata(self):
        """ Creates a PolyData vtk data set using the factory's
            attributes.
        """
        points = c_[ self.position_x.ravel(), 
                     self.position_y.ravel(),
                     self.position_z.ravel(),
                   ]
        lines = None
        if self.lines:
            np = len(points) - 1
            lines  = zeros((np, 2), 'l')
            lines[:,0] = arange(0, np-0.5, 1, 'l')
            lines[:,1] = arange(1, np+0.5, 1, 'l')
        self._vtk_source = tvtk.PolyData(points=points, lines=lines)
        if self.connectivity:
            assert self.connectivity.shape[1] == 3, \
                    "The connectivity list must be Nx3."
            self._vtk_source.polys = self.connectivity
        self._mayavi_source = VTKDataSource(self._vtk_source)


    def _mk_image_data(self):
        """ Creates an ImageData VTK data set and the associated ArraySource 
            using the factory's attributes.
        """
        self._mayavi_source = ArraySource(  transpose_input_array=True,
                                            scalar_data=self.scalar_data,
                                            origin=[0., 0., 0],
                                            spacing=[1, 1, 1])
        self._vtk_source = self._mayavi_source.image_data


    def _mk_rectilinear_grid(self):
        """ Creates a RectilinearGrid VTK data set using the factory's 
            attributes.
        """
        rg = tvtk.RectilinearGrid()
        x = self.position_x.squeeze()
        if x.ndim == 3:
            x = x[:, 0, 0]
        y = self.position_y.squeeze()
        if y.ndim == 3:
            y = y[0, :, 0]
        z = self.position_z.squeeze()
        if z.ndim == 3:
            z = z[0, 0, :]
        # FIXME: We should check array size here.
        rg.dimensions = (x.shape, y.shape, z.shape)
        rg.x_coordinates = x
        rg.y_coordinates = y
        rg.z_coordinates = z
        self._vtk_source = rg
        self._mayavi_source = VTKDataSource(self._vtk_source)
        

    def _mk_structured_grid(self):
        """ Creates a StructuredGrid VTK data set using the factory's 
            attributes.
        """
        sg = tvtk.StructuredGrid(dimensions=self.scalar_data.shape)
        sg.points = c_[ self.position_x.ravel(), 
                        self.position_y.ravel(),
                        self.position_z.ravel(),
                      ]
        self._vtk_source = sg
        self._mayavi_source = VTKDataSource(self._vtk_source)
 

    #----------------------------------------------------------------------
    # Public interface
    #----------------------------------------------------------------------

    def build_data_source(self):
        """ Uses all the information given by the user on his data
            structure to figure out the right data structure.
        """
        if self.position_implicit:
            self._mk_image_data()
        elif self.orthogonal_grid:
            self._mk_rectilinear_grid()
        elif self.connectivity is None:
            self._mk_structured_grid()
        else:
            self._mk_polydata()
        self._add_scalar_data()
        self._add_vector_data()
        return self._mayavi_source

