# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.havs_volume_mapper import HAVSVolumeMapper


class OpenGLHAVSVolumeMapper(HAVSVolumeMapper):
    """
    OpenGLHAVSVolumeMapper - Hardware-Assisted
    
    Superclass: HAVSVolumeMapper
    
    HAVSVolumeMapper is a class that renders polygonal data
    (represented as an unstructured grid) using the Hardware-Assisted
    Visibility Sorting (HAVS) algorithm.  First the unique triangles are
    sorted in object space, then they are sorted in image space using a
    fixed size A-buffer implemented on the GPU called the k-buffer.  The
    HAVS algorithm excels at rendering large datasets quickly.  The
    trade-off is that the algorithm may produce some rendering artifacts
    due to an insufficient k size (currently 2 or 6 is supported) or
    read/write race conditions.
    
    A built in level-of-detail (LOD) approach samples the geometry using
    one of two heuristics (field or area).  If LOD is enabled, the amount
    of geometry that is sampled and rendered changes dynamically to stay
    within the target frame rate.  The field sampling method generally
    works best for datasets with cell sizes that don't vary much in size.
     On the contrary, the area sampling approach gives better
    approximations when the volume has a lot of variation in cell size.
    
    The HAVS algorithm uses several advanced features on graphics
    hardware. The k-buffer sorting network is implemented using
    framebuffer objects (FBOs) with multiple render targets (MRTs). 
    Therefore, only cards that support these features can run the
    algorithm (at least an ATI 9500 or an NVidia NV40 (6600)).
    
    Notes:
    
    Several issues had to be addressed to get the HAVS algorithm working
    within the vtk framework.  These additions forced the code to forsake
    speed for the sake of compliance and robustness.
    
    The HAVS algorithm operates on the triangles that compose the mesh.
    Therefore, before rendering, the cells are decomposed into unique
    triangles and stored on the GPU for efficient rendering.  The use of
    GPU data structures is only recommended if the entire geometry can
    fit in graphics memory.  Otherwise this feature should be disabled.
    
    Another new feature is the handling of mixed data types (eg.,
    polygonal data with volume data).  This is handled by reading the
    z-buffer from the current window and copying it into the framebuffer
    object for off-screen rendering.  The depth test is then enabled so
    that the volume only appears over the opaque geometry.  Finally, the
    results of the off-screen rendering are blended into the framebuffer
    as a transparent, view-aligned texture.
    
    Instead of using a preintegrated 3d lookup table for storing the ray
    integral, this implementation uses partial pre-integration.  This
    improves the performance of dynamic transfer function updates by
    avoiding a costly preprocess of the table.
    
    A final change to the original algorithm is the handling of
    non-convexities in the mesh.  Due to read/write hazards that may
    create undesired artifacts with non-convexities when using a
    inside/outside toggle in the fragment program, another approach was
    employed.  To handle non-convexities, the fragment shader determines
    if a ray-gap is larger than the max cell size and kill the fragment
    if so.  This approximation performs rather well in practice but may
    miss small non-convexities.
    
    For more information on the HAVS algorithm see:
    
    
     "Hardware-Assisted Visibility Sorting for Unstructured Volume
    Rendering" by S. P. Callahan, M. Ikits, J. L. D. Comba, and C. T.
    Silva, IEEE Transactions of Visualization and Computer Graphics;
    May/June 2005.
    
    For more information on the Level-of-Detail algorithm, see:
    
    "Interactive Rendering of Large Unstructured Grids Using Dynamic
    Level-of-Detail" by S. P. Callahan, J. L. D. Comba, P. Shirley, and
    C. T. Silva, Proceedings of IEEE Visualization '05, Oct. 2005.
    
    Acknowledgments:
    
    This code was developed by Steven P. Callahan under the supervision
    of Prof. Claudio T. Silva. The code also contains contributions from
    Milan Ikits, Linh Ha, Huy T. Vo, Carlos E. Scheidegger, and Joao L.
    D. Comba.
    
    The work was supported by grants, contracts, and gifts from the
    National Science Foundation, the Department of Energy, the Army
    Research Office, and IBM.
    
    The port of HAVS to VTK and para_view has been primarily supported by
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLHAVSVolumeMapper, obj, update, **traits)
    
    _updateable_traits_ = \
    (('level_of_detail_target_time', 'GetLevelOfDetailTargetTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('gpu_data_structures', 'GetGPUDataStructures'), ('level_of_detail',
    'GetLevelOfDetail'), ('progress_text', 'GetProgressText'),
    ('k_buffer_size', 'GetKBufferSize'), ('debug', 'GetDebug'),
    ('partially_remove_non_convexities',
    'GetPartiallyRemoveNonConvexities'), ('release_data_flag',
    'GetReleaseDataFlag'), ('scalar_mode', 'GetScalarMode'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('level_of_detail_method', 'GetLevelOfDetailMethod'),
    ('abort_execute', 'GetAbortExecute'), ('blend_mode', 'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'k_buffer_size', 'scalar_mode',
    'gpu_data_structures', 'level_of_detail', 'level_of_detail_method',
    'level_of_detail_target_time', 'partially_remove_non_convexities',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLHAVSVolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLHAVSVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['blend_mode', 'k_buffer_size', 'scalar_mode'],
            ['gpu_data_structures', 'level_of_detail', 'level_of_detail_method',
            'level_of_detail_target_time', 'partially_remove_non_convexities']),
            title='Edit OpenGLHAVSVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLHAVSVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

