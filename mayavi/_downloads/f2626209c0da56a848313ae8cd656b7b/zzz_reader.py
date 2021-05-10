"""This is a simple example that shows how to create a reader factory
and register that reader with mayavi.

To use this:

    - put this in ~/.mayavi2/
    - then import this module in your ~/.mayavi2/user_mayavi.py.

that's it.

What you should get:

    - Options to open .zzz files from the file->open menu.
    - Open .zzz files via right click.
    - Open .zzz files from the engine or mlab (via open)
    - do mayavi2 -d foo.zzz.

"""

from mayavi.core.api import registry, SourceMetadata, PipelineInfo

def zzz_reader(fname, engine):
    """Reader for .zzz files.

    Parameters:
    -----------

    fname -- Filename to be read.

    engine -- The engine the source will be associated with.
    """
    from tvtk.api import tvtk
    from mayavi.sources.vtk_data_source import VTKDataSource
    # Do your own reader stuff here, I'm just reading a VTK file with a
    # different extension here.
    r = tvtk.StructuredPointsReader(file_name=fname)
    r.update()

    src = VTKDataSource(data=r.output)
    return src

zzz_reader_info = SourceMetadata(
    id            = "ZZZReader",
    factory = 'zzz_reader.zzz_reader',
    tooltip       = "Load a ZZZ file",
    desc   = "Load a ZZZ file",
    help   = "Load a ZZZ file",
    menu_name        = "&ZZZ file",
    extensions = ['zzz'],
    wildcard = 'ZZZ files (*.zzz)|*.zzz',
    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)
# Inject this information in the mayavi registry
registry.sources.append(zzz_reader_info)

if __name__ == '__main__':
    import sys
    print("*"*80)
    print("ERROR: This script isn't supposed to be executed.")
    print(__doc__)
    print("*"*80)
    sys.exit(1)
