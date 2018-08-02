from traits.api import Bool, Instance, Int
from traitsui.api import Item, Group, View

import vtk
from tvtk.common import camel2enthought
from tvtk.api import tvtk
from tvtk import messenger
from tvtk.pipeline.browser import PipelineBrowser

from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo


def _create_dataset_name_map():
    names = ['vtkImageData', 'vtkPolyData',
             'vtkRectilinearGrid', 'vtkStructuredGrid',
             'vtkUnstructuredGrid']
    mapping = {x: camel2enthought(x)[4:] for x in names}
    mapping['vtkStructuredPoints'] = 'image_data'
    mapping['vtkDataSet'] = 'any'
    return mapping


_dataset_name_map = _create_dataset_name_map()


def tvtk_dataset_name(name):
    return _dataset_name_map.get(name, 'none')


def get_tvtk_dataset_name(obj):
    v = tvtk.to_vtk(obj)
    obj = v.GetOutputInformation(0).Get(vtk.vtkDataObject.DATA_OBJECT())
    if obj is not None:
        name = obj.GetClassName()
    else:
        name = v.GetOutputPortInformation(0).Get(
            vtk.vtkDataObject.DATA_TYPE_NAME()
        )
        if name is None:
            # Try again after calling update
            v.Update()
            return get_tvtk_dataset_name(v)
    return [tvtk_dataset_name(name)]


class VTKObjectSource(Source):

    """A simple wrapper to allow us to be able to add an arbitrary VTK object as a
    source into the Mayavi pipeline. This is convenient when one wishes to use
    an existing VTK object which produces some output.

    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The VTK algorithm to manage.
    object = Instance(tvtk.Algorithm, allow_none=False)

    browser = Instance(PipelineBrowser)

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    view = View(
        Group(
            Item(
                name='browser', show_label=False,
                style='custom', resizable=True
            )
        )
    )

    # The ID of the observer for the data.
    _observer_id = Int(-1)

    # ## Private protocol #############################################

    def _object_changed(self, old, new):
        self.outputs = [new]

        self.browser.root_object = [new]

        self.output_info.datasets = get_tvtk_dataset_name(new)

        if old is not None:
            old.remove_observer(self._observer_id)
        self._observer_id = new.add_observer(
            'ModifiedEvent', messenger.send
        )
        new_vtk = tvtk.to_vtk(new)
        messenger.connect(new_vtk, 'ModifiedEvent', self._fire_data_changed)

        self.name = self._get_name()

    def _fire_data_changed(self, *args):
        self.data_changed = True

    def _get_name(self):
        result = 'VTK (uninitialized)'
        if self.object is not None:
            typ = self.object.__class__.__name__
            result = "VTK (%s)" % typ
        if '[Hidden]' in self.name:
            result += ' [Hidden]'
        return result

    def _browser_default(self):
        b = PipelineBrowser()
        b.on_trait_change(self._fire_data_changed, 'object_edited')
        return b
