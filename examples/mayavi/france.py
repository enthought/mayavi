"""
Using Mlab to display a map of France.

In this example we use Mlab to access directly to the pipeline.
"""
print "This script is numerically intensive and requires a lot of memory."
print "Please be patient"


from numpy import loadtxt, sqrt, r_, c_, ones_like, empty_like, unique
import urllib, zipfile, cStringIO, os
from enthought.mayavi import mlab


############################################################################
# Get the data from the web
def reporthook(*a): print '.',
url = "http://www.ign.fr/telechargement/MPro/produit/BD_ALTI/France_1000.zip"
i = url.rfind('/')
zip_file = url[i+1:]
if not os.path.exists(zip_file):
    print "Retrieving data from %s ..." % url
    urllib.urlretrieve(url, zip_file, reporthook)
    print "Done"

############################################################################
# Load the data
print "Loading the data...",
data_str = cStringIO.StringIO(
                zipfile.ZipFile(zip_file).read('FRANCE_1000.XYZ')
               )
data = loadtxt(data_str)
print "Done"

X = data[:, 0]/100.
Y = data[:, 1]/100.
Z = data[:, 2]/100.
del data_str, data

############################################################################
# Rescale the height for prettier results:
Z = 10*(10*sqrt(Z)+Z)

############################################################################
# Add points on the borders, and put them at negative altitude, with
# this the threshold filter will remove triangles outside the borders
Y_add = c_[unique(Y), unique(Y)]
X_add = empty_like(Y_add)
for i, y in enumerate(unique(Y)):
    row = X[Y==y]
    X_add[i, :] = [row.min()-1, row.max()+1]

X = r_[X, X_add.ravel()]
Y = r_[Y, Y_add.ravel()]
Z = r_[Z,  -10000*ones_like(Y_add).ravel()]

############################################################################
# Do the visualization using the Mlab pipeline
P = mlab.pipeline
mlab.clf()
france_points = P.scalar_scatter(X, Y, Z, Z)
france_elevation = P.elevation_filter( P.quadric_decimation(
                        P.threshold(
                            P.point_to_cell_data(
                                P.delaunay2d(france_points) ),
                        low=0.1)
                        ),
                    low_point  = [0, 0, -0.28*Z.max()],
                    high_point = [0, 0, 0.75*Z.max()],
                    )

france  = P.surface(france_elevation, colormap='gist_earth')
mlab.view(0, 0)
mlab.show()
