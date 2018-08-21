"""The Volume module visualizes scalar fields using volumetric
visualization techniques.  This supports ImageData and
UnstructuredGrid data.  It also supports the FixedPointRenderer for
ImageData.  However, the performance is slow so your best bet is
probably with the ImageData based renderers.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006-2018, Enthought, Inc.
# License: BSD Style.

# Standard imports
from math import cos, sqrt, pi
from vtk.util import vtkConstants

# Enthought library imports.
from traits.api import Instance, Property, List, ReadOnly, \
     Str, Button, Tuple, Dict
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk
from tvtk.common import suppress_vtk_warnings
from tvtk.util.gradient_editor import hsva_to_rgba, GradientTable
from tvtk.util.traitsui_gradient_editor import VolumePropertyEditor
from tvtk.util.ctf import save_ctfs, load_ctfs, \
     rescale_ctfs, set_lut, PiecewiseFunction, ColorTransferFunction
from apptools.persistence import state_pickler

# Local imports
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.core.common import error
from mayavi.core.trait_defs import DEnum
from mayavi.core.lut_manager import LUTManager
from mayavi.core.utils import DataSetHelper


######################################################################
# Utility functions.
######################################################################
def is_volume_pro_available():
    """Returns `True` if there is a volume pro card available.
    """
    try:
        map = tvtk.VolumeProMapper()
    except AttributeError:
        return False
    else:
        return map.number_of_boards > 0


def find_volume_mappers():
    res = []
    with suppress_vtk_warnings():
        obj = tvtk.Object()
        obj.global_warning_display = False
        for name in dir(tvtk):
            if 'Volume' in name and 'Mapper' in name:
                try:
                    klass = getattr(tvtk, name)
                    inst = klass()
                except TypeError:
                    pass
                else:
                    res.append(name)
    ignores = ['VolumeTextureMapper3D', 'VolumeProMapper']
    for name in ignores:
        if name in res:
            res.remove(name)
    return res


def default_OTF(x1, x2):
    """Creates a default opacity transfer function.
    """
    maxs = max(x1, x2)
    mins = min(x1, x2)
    otf = PiecewiseFunction()
    otf.add_point(mins, 0.0)
    otf.add_point(maxs, 0.2)
    return otf


def make_CTF(x1, x2, hue_range=(2.0/3.0, 0.0),
             sat_range=(1.0, 1.0), val_range=(1.0, 1.0),
             n=10, mode='sqrt'):
    """Creates a CTF as per given arguments.  Lets one set a hue,
    saturation and value range.  The mode can be one of 'sqrt', or
    'linear'.  The idea of this function is to create a CTF that is
    similar to the LUT being used.  's_curve' is not implemented.
    Patches welcome.
    """
    maxs = max(x1, x2)
    mins = min(x1, x2)
    ds = maxs - mins
    dhue = hue_range[1] - hue_range[0]
    dsat = sat_range[1] - sat_range[0]
    dval = val_range[1] - val_range[0]
    ctf = ColorTransferFunction()
    try:
        ctf.range = (mins, maxs)
    except Exception:
        # VTK versions < 5.2 don't seem to need this.
        pass
    if mode == 'sqrt':
        for i in range(n+1):
            # Generate x in [0, 1]
            x = 0.5*(1.0 + cos((n-i)*pi/n))  # Chebyshev nodes.
            h = hue_range[0] + dhue*x
            s = sat_range[0] + dsat*x
            v = val_range[0] + dval*x
            r, g, b, a = [sqrt(c) for c in hsva_to_rgba(h, s, v, 1.0)]
            ctf.add_rgb_point(mins+x*ds, r, g, b)
    elif mode == 'linear':
        for i in range(n+1):
            # Generate x in [0, 1]
            x = float(i)/n  # Uniform nodes.
            h = hue_range[0] + dhue*x
            s = sat_range[0] + dsat*x
            v = val_range[0] + dval*x
            r, g, b, a = hsva_to_rgba(h, s, v, 1.0)
            ctf.add_rgb_point(mins+x*ds, r, g, b)
    return ctf


def default_CTF(x1, x2):
    """Creates a default RGB color transfer function.  In this case we
    default to a red-blue one with the 'sqrt' mode.
    """
    return make_CTF(x1, x2,
                    hue_range=(2.0/3.0, 0.0),
                    sat_range=(1.0, 1.0),
                    val_range=(1.0, 1.0),
                    n=10,
                    mode='sqrt')


def load_volume_prop_from_grad(grad_file_name, volume_prop,
                               scalar_range=(0, 255)):
    """Load a ``*.grad`` file (*grad_file_name*) and set the given volume
    property (*volume_prop*) given the *scalar_range*.
    """
    gt = GradientTable(300)
    gt.load(grad_file_name)
    gt.store_to_vtk_volume_prop(volume_prop, scalar_range)


def save_volume_prop_to_grad(volume_prop, grad_file_name):
    """Save the given volume property (*volume_prop*) to a ``*.grad`` file
    given as *grad_file_name*.
    """
    gt = GradientTable(300)
    gt.load_from_vtk_volume_prop(volume_prop)
    gt.save(grad_file_name)


######################################################################
# `VolumeLutManager` class.
######################################################################
class VolumeLUTManager(LUTManager):
    """Just has a different view than the LUTManager.
    """
    view = View(Group(Item(name='show_scalar_bar'),
                      Item(name='number_of_labels'),
                      Item(name='shadow'),
                      Item(name='use_default_name'),
                      Item(name='data_name'),
                      label='Scalar Bar',
                      ),
                Group(Item(name='_title_text_property',
                           style='custom',
                           resizable=True),
                      show_labels=False,
                      label='Title'),
                Group(Item(name='_label_text_property',
                           style='custom',
                           resizable=True),
                      show_labels=False,
                      label='Labels'),
                resizable=True
                )


######################################################################
# `Volume` class.
######################################################################
class Volume(Module):
    """The Volume module visualizes scalar fields using volumetric
    visualization techniques.  This supports ImageData and
    UnstructuredGrid data.  It also supports the FixedPointRenderer
    for ImageData.  However, the performance is slow so your best bet
    is probably with the ImageData based renderers.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    volume_mapper_type = DEnum(values_name='_mapper_types',
                               desc='volume mapper to use')

    ray_cast_function_type = DEnum(values_name='_ray_cast_functions',
                                   desc='Ray cast function to use')

    volume = ReadOnly

    volume_mapper = Property(record=True)

    volume_property = Property(record=True)

    ray_cast_function = Property(record=True)

    lut_manager = Instance(VolumeLUTManager, args=(), allow_none=False,
                           record=True)

    input_info = PipelineInfo(datasets=['image_data',
                                        'unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['scalars'])

    ########################################
    # View related code.

    update_ctf = Button('Update CTF')

    view = View(Group(Item(name='_volume_property', style='custom',
                           editor=VolumePropertyEditor,
                           resizable=True),
                      Item(name='update_ctf'),
                      label='CTF',
                      show_labels=False),
                Group(Item(name='volume_mapper_type'),
                      Group(Item(name='_volume_mapper',
                                 style='custom',
                                 resizable=True),
                            show_labels=False
                            ),
                      Item(name='ray_cast_function_type'),
                      Group(Item(name='_ray_cast_function',
                                 enabled_when='len(_ray_cast_functions) > 0',
                                 style='custom',
                                 resizable=True),
                            show_labels=False),
                      label='Mapper',
                      ),
                Group(Item(name='_volume_property', style='custom',
                           resizable=True),
                      label='Property',
                      show_labels=False),
                Group(Item(name='volume', style='custom',
                           editor=InstanceEditor(),
                           resizable=True),
                      label='Volume',
                      show_labels=False),
                Group(Item(name='lut_manager', style='custom',
                           resizable=True),
                      label='Legend',
                      show_labels=False),
                resizable=True
                )

    ########################################
    # Private traits
    _volume_mapper = Instance(tvtk.AbstractVolumeMapper)
    _volume_property = Instance(tvtk.VolumeProperty)
    _ray_cast_function = Instance(tvtk.Object)

    _mapper_types = List(Str, ['TextureMapper2D', 'RayCastMapper', ])

    _available_mapper_types = List(Str)

    _ray_cast_functions = List(Str)

    current_range = Tuple

    # The color transfer function.
    _ctf = Instance(ColorTransferFunction)
    # The opacity values.
    _otf = Instance(PiecewiseFunction)

    # A cache for the mappers, a dict keyed by class.
    _mapper_cache = Dict

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(Volume, self).__get_pure_state__()
        d['ctf_state'] = save_ctfs(self._volume_property)
        for name in ('current_range', '_ctf', '_otf'):
            d.pop(name, None)
        return d

    def __set_pure_state__(self, state):
        self.volume_mapper_type = state['_volume_mapper_type']
        state_pickler.set_state(self, state, ignore=['ctf_state'])
        ctf_state = state['ctf_state']
        ctf, otf = load_ctfs(ctf_state, self._volume_property)
        self._ctf = ctf
        self._otf = otf
        self._update_ctf_fired()

    ######################################################################
    # `Module` interface
    ######################################################################
    def start(self):
        super(Volume, self).start()
        self.lut_manager.start()

    def stop(self):
        super(Volume, self).stop()
        self.lut_manager.stop()

    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.
        """
        v = self.volume = tvtk.Volume()
        vp = self._volume_property = tvtk.VolumeProperty()

        self._ctf = ctf = default_CTF(0, 255)
        self._otf = otf = default_OTF(0, 255)
        vp.set_color(ctf)
        vp.set_scalar_opacity(otf)
        vp.shade = True
        vp.interpolation_type = 'linear'
        v.property = vp

        v.on_trait_change(self.render)
        vp.on_trait_change(self.render)

        available_mappers = find_volume_mappers()
        if is_volume_pro_available():
            self._mapper_types.append('VolumeProMapper')
            available_mappers.append('VolumeProMapper')

        self._available_mapper_types = available_mappers
        if 'FixedPointVolumeRayCastMapper' in available_mappers:
            self._mapper_types.append('FixedPointVolumeRayCastMapper')

        self.actors.append(v)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        dataset = mm.source.get_output_dataset()

        ug = hasattr(tvtk, 'UnstructuredGridVolumeMapper')
        if dataset.is_a('vtkMultiBlockDataSet'):
            if 'MultiBlockVolumeMapper' not in self._available_mapper_types:
                error('Your version of VTK does not support '
                      'Multiblock volume rendering')
                return
        elif dataset.is_a('vtkUniformGridAMR'):
            if 'AMRVolumeMapper' not in self._available_mapper_types:
                error('Your version of VTK does not support '
                      'AMR volume rendering')
                return
        elif ug:
            if not dataset.is_a('vtkImageData') \
                   and not dataset.is_a('vtkUnstructuredGrid'):
                error('Volume rendering only works with '
                      'StructuredPoints/ImageData/UnstructuredGrid datasets')
                return
        elif not dataset.is_a('vtkImageData'):
            error('Volume rendering only works with '
                  'StructuredPoints/ImageData datasets')
            return

        self._setup_mapper_types()
        self._setup_current_range()
        self._volume_mapper_type_changed(self.volume_mapper_type)
        self._update_ctf_fired()
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self._setup_mapper_types()
        self._setup_current_range()
        self._update_ctf_fired()
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _get_image_data_volume_mappers(self):
        check = ('SmartVolumeMapper', 'GPUVolumeRayCastMapper',
                 'OpenGLGPUVolumeRayCastMapper')
        return [x for x in check
                if x in self._available_mapper_types]

    def _setup_mapper_types(self):
        """Sets up the mapper based on input data types.
        """
        dataset = self.module_manager.source.get_output_dataset()
        if dataset.is_a('vtkMultiBlockDataSet'):
            if 'MultiBlockVolumeMapper' in self._available_mapper_types:
                self._mapper_types = ['MultiBlockVolumeMapper']
        elif dataset.is_a('vtkUniformGridAMR'):
            if 'AMRVolumeMapper' not in self._available_mapper_types:
                self._mapper_types = ['AMRVolumeMapper']
        elif dataset.is_a('vtkUnstructuredGrid'):
            if hasattr(tvtk, 'UnstructuredGridVolumeMapper'):
                check = ['UnstructuredGridVolumeZSweepMapper',
                         'UnstructuredGridVolumeRayCastMapper',
                         ]
                mapper_types = []
                for mapper in check:
                    if mapper in self._available_mapper_types:
                        mapper_types.append(mapper)
                if len(mapper_types) == 0:
                    mapper_types = ['']
                self._mapper_types = mapper_types
                return
        else:
            mapper_types = self._get_image_data_volume_mappers()
            if dataset.point_data.scalars.data_type not in \
               [vtkConstants.VTK_UNSIGNED_CHAR,
                vtkConstants.VTK_UNSIGNED_SHORT]:
                if 'FixedPointVolumeRayCastMapper' \
                       in self._available_mapper_types:
                    mapper_types.append('FixedPointVolumeRayCastMapper')
                elif len(mapper_types) == 0:
                    error('Available volume mappers only work with '
                          'unsigned_char or unsigned_short datatypes')
            else:
                check = ['FixedPointVolumeRayCastMapper',
                         'VolumeProMapper', 'TextureMapper2D', 'RayCastMapper',
                         'TextureMapper3D'
                         ]
                for mapper in check:
                    if mapper in self._available_mapper_types:
                        mapper_types.append(mapper)
            self._mapper_types = mapper_types

    def _setup_current_range(self):
        mm = self.module_manager
        # Set the default name and range for our lut.
        lm = self.lut_manager
        slm = mm.scalar_lut_manager
        lm.trait_set(default_data_name=slm.default_data_name,
                     default_data_range=slm.default_data_range)

        # Set the current range.
        dataset = mm.source.get_output_dataset()
        dsh = DataSetHelper(dataset)
        name, rng = dsh.get_range('scalars', 'point')
        if name is None:
            error('No scalars in input data!')
            rng = (0, 255)

        if self.current_range != rng:
            self.current_range = rng

    def _get_volume_mapper(self):
        return self._volume_mapper

    def _get_volume_property(self):
        return self._volume_property

    def _get_ray_cast_function(self):
        return self._ray_cast_function

    def _get_mapper(self, klass):
        """ Return a mapper of the given class. Either from the cache or by
        making a new one.
        """
        result = self._mapper_cache.get(klass)
        if result is None:
            result = klass()
            self._mapper_cache[klass] = result
        return result

    def _volume_mapper_type_changed(self, value):
        mm = self.module_manager
        if mm is None:
            return

        old_vm = self._volume_mapper
        if old_vm is not None:
            old_vm.on_trait_change(self.render, remove=True)
            try:
                old_vm.remove_all_input_connections(0)
            except AttributeError:
                pass

        if value == 'RayCastMapper':
            new_vm = self._get_mapper(tvtk.VolumeRayCastMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['RayCastCompositeFunction',
                                        'RayCastMIPFunction',
                                        'RayCastIsosurfaceFunction']
            new_vm.volume_ray_cast_function = self._get_mapper(
                tvtk.VolumeRayCastCompositeFunction
            )
        elif value == 'MultiBlockVolumeMapper':
            new_vm = self._get_mapper(tvtk.MultiBlockVolumeMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'AMRVolumeMapper':
            new_vm = self._get_mapper(tvtk.AMRVolumeMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'SmartVolumeMapper':
            new_vm = self._get_mapper(tvtk.SmartVolumeMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'GPUVolumeRayCastMapper':
            new_vm = self._get_mapper(tvtk.GPUVolumeRayCastMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'OpenGLGPUVolumeRayCastMapper':
            new_vm = self._get_mapper(tvtk.OpenGLGPUVolumeRayCastMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'TextureMapper2D':
            new_vm = self._get_mapper(tvtk.VolumeTextureMapper2D)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'TextureMapper3D':
            new_vm = self._get_mapper(tvtk.VolumeTextureMapper3D)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'VolumeProMapper':
            new_vm = self._get_mapper(tvtk.VolumeProMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'FixedPointVolumeRayCastMapper':
            new_vm = self._get_mapper(tvtk.FixedPointVolumeRayCastMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'UnstructuredGridVolumeRayCastMapper':
            new_vm = self._get_mapper(tvtk.UnstructuredGridVolumeRayCastMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']
        elif value == 'UnstructuredGridVolumeZSweepMapper':
            new_vm = self._get_mapper(tvtk.UnstructuredGridVolumeZSweepMapper)
            self._volume_mapper = new_vm
            self._ray_cast_functions = ['']

        src = mm.source
        self.configure_input(new_vm, src.outputs[0])
        self.volume.mapper = new_vm
        new_vm.on_trait_change(self.render)

    def _update_ctf_fired(self):
        set_lut(self.lut_manager.lut, self._volume_property)
        self.render()

    def _current_range_changed(self, old, new):
        rescale_ctfs(self._volume_property, new)
        self.render()

    def _ray_cast_function_type_changed(self, old, new):
        rcf = self.ray_cast_function
        if len(old) > 0:
            rcf.on_trait_change(self.render, remove=True)

        if len(new) > 0:
            new_rcf = getattr(tvtk, 'Volume%s' % new)()
            new_rcf.on_trait_change(self.render)
            self._volume_mapper.volume_ray_cast_function = new_rcf
            self._ray_cast_function = new_rcf
        else:
            self._ray_cast_function = None

        self.render()

    def _scene_changed(self, old, new):
        super(Volume, self)._scene_changed(old, new)
        self.lut_manager.scene = new
