
Modules and Filters
--------------------

For each Mayavi module or filter, there is a corresponding
`mlab.pipeline` factory function that takes as an input argument, the
source on which the new module or filter will be added, and returns the 
created module object. The name of the function corresponds to the name
of the module, but with words separated by underscores `_`, rather than
alternating capitals.

The input object, if it is a data source (Mayavi data source or VTK
dataset), does not need to be already present in the figure, it will be
automatically added if necessary.

Factory functions take keyword arguments controlling some properties of
the object added to the pipeline.

For instance, the `ScalarCutPlane` module can be added with the following
function:

.. autofunction:: mayavi.tools.modules.scalar_cut_plane

As the list is long, we shall not enumerate here all the factory function
for adding modules or filters. You are invited to refer to their
docstring for information on the keyword arguments they accept.

