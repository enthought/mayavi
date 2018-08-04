from tvtk.api import tvtk
from mayavi.core.utils import get_new_output, dsa


def has_attributes(dataset):
    """Returns `True` when the given TVTK `dataset` has any attribute
    arrays in point and cell data and `False` otherwise.
    """
    if dataset is None:
        return False
    obj = dsa.WrapDataObject(tvtk.to_vtk(get_new_output(dataset)))

    if obj.PointData and len(obj.PointData.keys()) > 0:
        return True
    if obj.CellData and len(obj.CellData.keys()) > 0:
        return True

    return False
