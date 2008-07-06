
from numpy import column_stack

from enthought.traits.api import HasTraits, Dict, Property, Str, Button, \
    true, Any, false, Enum, Instance, Tuple, HasStrictTraits

from enthought.tvtk.tools import mlab as tvtk_mlab
from enthought.tvtk.api import tvtk

############################################################################
# The DataSourceFactory class
############################################################################
class DataSourceFactory(HasTraits):

    data_sources = Dict

    _data_sources_names = Property(depends_on='data_sources')

    def _get__data_sources_names(self):
        names = self.data_sources.keys()
        names.sort()
        return names


    # Dictionnary mapping the views
    view_mapping = {
            'A set of points, that can be connected by lines':
                    '_set_of_points_view',
            'A set of vectors':
                    '_set_of_vectors_view',
            'Volumetric data':
                    '_volumetric_data_view',
            'A surface':
                    '_surface_view',
            'A planar surface':
                    '_planar_surface_view',
            }


    # The different data source types that we can create
    data_type = Enum(*view_mapping.keys())
    

    # Whether or not the data points should be connected.
    lines = false

    # The scalar data slection
    scalar_data = Str('', help="Select the array that gives the value of the "
                            "scalars plotted.")

    # Whether the position is implicitely inferred from the array indices
    position_implicit = false(help="The positionning of the data points "
                        "can be inferred implicitely from the shape of "
                        "the data array, if it is a three dimensional "
                        "array. In this case the data is assumed to be "
                        "positioned on an orthogonal regular grid")

    x_position = Str(help="Select the array that gives the x "
                        "positon of the data points")
    
    y_position = Str(help="Select the array that gives the y "
                        "positon of the data points")
    
    z_position = Str(help="Select the array that gives the z "
                        "positon of the data points")

    connectivity_implicit = false

    connectivity = Str

    vector_data = false(help="""Do you want to plot vector components?""")

    # A boolean to ask the user if he wants to load scalar data
    scalar_data_option = false

    vector_u = Str

    vector_v = Str

    vector_w =  Str

    #----------------------------------------------------------------------
    # Private traits
    #----------------------------------------------------------------------


    #----------------------------------------------------------------------
    # Public interface
    #----------------------------------------------------------------------

    def build_data_source(self):
        """ This is where we apply the selections made by the user in
            in the wizard to build the data source.
        """
        if self.data_type == 'A surface':
            if self.connectivity_implicit:
                triangles, points = tvtk_mlab.make_triangles_points(
                        self.x_position, self.y_position, self.z_position)
            else:
                points = column_stack( (self.x_position.ravel(), 
                                        self.y_position.ravel(), 
                                        self.z_position.ravel()))
                triangles = self.connectivity
            return False
        elif self.data_type == 'A planar surface':
            return False
        elif self.data_type == 'A set of vectors':
            return False
        elif self.data_type == 'Volumetric data':
            return False
        elif self.data_type == \
                'A set of points, that can be connected by lines':
            return False
        return True
  

