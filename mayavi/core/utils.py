import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

from tvtk.api import tvtk


def get_new_output(input, update=True):
    if update and hasattr(input, 'update'):
        input.update()
    if input.is_a('vtkDataObject'):
        return input
    elif input.is_a('vtkAlgorithmOutput'):
        return input.producer
    else:
        if hasattr(input, 'output') and input.output is not None:
            result = input.output
        elif hasattr(input, 'get_output_information'):
            obj = input.get_output_information(0).get(
                vtk.vtkDataSet.DATA_OBJECT()
            )
            result = obj
        else:
            result = None
        return result


class DataSetHelper(object):
    def __init__(self, input):
        self.dataset = dsa.WrapDataObject(
            tvtk.to_vtk(get_new_output(input, update=True))
        )
        self._composite = isinstance(self.dataset, dsa.CompositeDataSet)
        self._scalars = None
        self._vectors = None

    def _find_attr_name_for_composite_data(self, attr, mode):
        prop = 'PointData' if mode == 'point' else 'CellData'
        for obj in self.dataset:
            da = getattr(obj, prop)
            if attr == 'scalars':
                s = da.GetScalars()
            else:
                s = da.GetVectors()
            if s is not None:
                return s.GetName()

    def _get_attr(self, da, attr, mode):
        if self._composite:
            name = self._find_attr_name_for_composite_data(attr, mode)
            return name,  da[name]
        else:
            if attr == 'scalars':
                s = da.GetScalars()
            else:
                s = da.GetVectors()
            if s is not None:
                name = s.GetName()
                if name is None or len(name) == 0:
                    s.SetName(mode + '_' + attr)
                return name, da[name]

    def get_range(self, attr='scalars', mode='point'):
        assert mode in ('point', 'cell')
        assert attr in ('scalars', 'vectors')
        dataset = self.dataset
        da = dataset.PointData if mode == 'point' else dataset.CellData
        x = self._get_attr(da, attr, mode)
        if x is None:
            return None, [0.0, 1.0]
        name, x = x
        if isinstance(x, dsa.VTKNoneArray):
            res = [0.0, 1.0]
        elif self._composite:
            # Don't bother with Nans for composite data for now.
            if attr == 'scalars':
                res = [algs.min(x), algs.max(x)]
            else:
                max_norm = np.sqrt(algs.max(algs.sum(x*x, axis=1)))
                res = [0.0, max_norm]
        else:
            has_nan = np.isnan(x).any()
            if attr == 'scalars':
                if has_nan:
                    res = [float(np.nanmin(x)), float(np.nanmax(x))]
                else:
                    res = list(x.GetRange())
            else:
                if has_nan:
                    d_mag = np.sqrt((x*x).sum(axis=1))
                    res = [float(np.nanmin(d_mag)),
                           float(np.nanmax(d_mag))]
                else:
                    res = [0.0, x.GetMaxNorm()]
        return name, res

    def get_center(self):
        """Return the center of the data.
        """
        if self._composite:
            return algs.mean(self.dataset.Points, axis=0)
        else:
            return self.dataset.GetCenter()

    def get_bounds(self):
        """Return the bounds of the data.
        """
        if self._composite:
            c1 = algs.min(self.dataset.Points, axis=0)
            c2 = algs.max(self.dataset.Points, axis=0)
            result = np.zeros(6)
            result[::2] = c1
            result[1::2] = c2
            return result
        else:
            return self.dataset.GetBounds()


def get_tvtk_dataset_name(dataset):
    """Given a TVTK dataset `dataset` return the string dataset type of
    the dataset.
    """
    result = 'none'
    if not hasattr(dataset, 'is_a'):
        return result
    dataset = get_new_output(dataset)
    if dataset is None:
        return result
    if dataset.is_a('vtkStructuredPoints') or dataset.is_a('vtkImageData'):
        result = 'image_data'
    elif dataset.is_a('vtkRectilinearGrid'):
        result = 'rectilinear_grid'
    elif dataset.is_a('vtkPolyData'):
        result = 'poly_data'
    elif dataset.is_a('vtkStructuredGrid'):
        result = 'structured_grid'
    elif dataset.is_a('vtkUnstructuredGrid'):
        result = 'unstructured_grid'
    elif dataset.is_a('vtkCompositeDataSet'):
        result = 'any'
    else:
        result = 'none'
    return result
