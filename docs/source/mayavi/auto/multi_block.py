import os
from mayavi import mlab
from tvtk.api import tvtk


def create_mb_dataset():
    mydir = os.path.dirname(__file__)
    path = os.path.join(mydir, os.pardir, 'data', 'fire_ug.vtu')
    r = tvtk.XMLUnstructuredGridReader(file_name=path)
    r.update()
    ug0 = r.output
    ug1 = tvtk.UnstructuredGrid()
    ug1.deep_copy(ug0)
    pts = ug1.points.to_array()
    pts[:, 2] += 3.0
    ug1.points = pts
    mb = tvtk.MultiBlockDataSet()
    mb.set_block(0, ug0)
    mb.set_block(1, ug1)
    return mb


def main():
    mb = create_mb_dataset()
    src = mlab.pipeline.add_dataset(mb)

    iso = mlab.pipeline.iso_surface(src)
    scp = mlab.pipeline.scalar_cut_plane(src)
    vcp = mlab.pipeline.vector_cut_plane(src)
    vcp.implicit_plane.widget.normal_to_y_axis = True

    mlab.show()


if __name__ == '__main__':
    main()
