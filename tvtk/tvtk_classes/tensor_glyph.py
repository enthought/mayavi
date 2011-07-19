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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class TensorGlyph(PolyDataAlgorithm):
    """
    TensorGlyph - scale and orient glyph(s) according to tensor
    eigenvalues and eigenvectors
    
    Superclass: PolyDataAlgorithm
    
    TensorGlyph is a filter that copies a geometric representation
    (specified as polygonal data) to every input point. The geometric
    representation, or glyph, can be scaled and/or rotated according to
    the tensor at the input point. Scaling and rotation is controlled by
    the eigenvalues/eigenvectors of the tensor as follows. For each
    tensor, the eigenvalues (and associated eigenvectors) are sorted to
    determine the major, medium, and minor eigenvalues/eigenvectors.
    
    If the boolean variable three_glyphs is not set the major eigenvalue
    scales the glyph in the x-direction, the medium in the y-direction,
    and the minor in the  z-direction. Then, the glyph is rotated so that
    the glyph's local x-axis lies along the major eigenvector, y-axis
    along the medium eigenvector, and z-axis along the minor.
    
    If the boolean variable three_glyphs is set three glyphs are produced,
    each of them oriented along an eigenvector and scaled according to
    the corresponding eigenvector.
    
    If the boolean variable Symmetric is set each glyph is mirrored (2 or
    6 glyphs will be produced)
    
    The x-axis of the source glyph will correspond to the eigenvector on
    output. Point (0,0,0) in the source will be placed in the data point.
    Variable Length will normally correspond to the distance from the
    origin to the tip of the source glyph along the x-axis, but can be
    changed to produce other results when Symmetric is on, e.g. glyphs
    that do not touch or that overlap.
    
    Please note that when Symmetric is false it will generally be better
    to place the source glyph from (-0.5,0,0) to (0.5,0,0), i.e. centred
    at the origin. When symmetric is true the placement from (0,0,0) to
    (1,0,0) will generally be more convenient.
    
    A scale factor is provided to control the amount of scaling. Also,
    you can turn off scaling completely if desired. The boolean variable
    clamp_scaling controls the maximum scaling (in conjunction with
    max_scale_factor.) This is useful in certain applications where
    singularities or large order of magnitude differences exist in the
    eigenvalues.
    
    If the boolean variable color_glyphs is set to true the glyphs are
    colored.  The glyphs can be colored using the input scalars
    (_set_color_mode_to_scalars), which is the default, or colored using the
    eigenvalues (_set_color_mode_to_eigenvalues).
    
    Another instance variable, extract_eigenvalues, has been provided to
    control extraction of eigenvalues/eigenvectors. If this boolean is
    false, then eigenvalues/eigenvectors are not extracted, and the
    columns of the tensor are taken as the eigenvectors (the norm of
    column, always positive, is the eigenvalue).  This allows additional
    capability over the Glyph3D object. That is, the glyph can be
    oriented in three directions instead of one.
    
    See Also:
    
    Glyph3D PointLoad HyperStreamline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTensorGlyph, obj, update, **traits)
    
    symmetric = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off drawing a mirror of each glyph
        """
    )
    def _symmetric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSymmetric,
                        self.symmetric_)

    color_glyphs = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off coloring of glyph with input scalar data or
        eigenvalues. If false, or input scalar data not present, then the
        scalars from the source object are passed through the filter.
        """
    )
    def _color_glyphs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorGlyphs,
                        self.color_glyphs_)

    scaling = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off scaling of glyph with eigenvalues.
        """
    )
    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    clamp_scaling = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off scalar clamping. If scalar clamping is on, the ivar
        max_scale_factor is used to control the maximum scale factor. (This
        is useful to prevent uncontrolled scaling near singularities.)
        """
    )
    def _clamp_scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClampScaling,
                        self.clamp_scaling_)

    extract_eigenvalues = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off extraction of eigenvalues from tensor.
        """
    )
    def _extract_eigenvalues_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractEigenvalues,
                        self.extract_eigenvalues_)

    three_glyphs = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off drawing three glyphs
        """
    )
    def _three_glyphs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeGlyphs,
                        self.three_glyphs_)

    color_mode = traits.Trait('scalars',
    tvtk_base.TraitRevPrefixMap({'scalars': 0, 'eigenvalues': 1}), help=\
        """
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If three_glyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Specify the geometry to copy to each point. Old style. See
        set_source_connection.
        """
    )

    length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance, along x, from the origin to the end of the
        source glyph. It is used to draw the symmetric glyphs.
        """
    )
    def _length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLength,
                        self.length)

    max_scale_factor = traits.Float(100.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum allowable scale factor. This value is
        compared to the combination of the scale factor times the
        eigenvalue. If less, the scale factor is reset to the
        max_scale_factor. The boolean clamp_scaling has to be "on" for this
        to work.
        """
    )
    def _max_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxScaleFactor,
                        self.max_scale_factor)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify scale factor to scale object by. (Scale factor always
        affects output even if scaling is off.)
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    def set_source_connection(self, *args):
        """
        V.set_source_connection(int, AlgorithmOutput)
        C++: void SetSourceConnection(int id,
            AlgorithmOutput *algOutput)
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify a source object at a specified table location. New style.
        Source connection is stored in port 1. This method is equivalent
        to set_input_connection(_1, id, output_port).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('scale_factor', 'GetScaleFactor'), ('max_scale_factor',
    'GetMaxScaleFactor'), ('scaling', 'GetScaling'), ('debug',
    'GetDebug'), ('extract_eigenvalues', 'GetExtractEigenvalues'),
    ('color_mode', 'GetColorMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_glyphs', 'GetColorGlyphs'),
    ('clamp_scaling', 'GetClampScaling'), ('progress_text',
    'GetProgressText'), ('symmetric', 'GetSymmetric'), ('length',
    'GetLength'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('three_glyphs',
    'GetThreeGlyphs'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamp_scaling', 'color_glyphs', 'debug',
    'extract_eigenvalues', 'global_warning_display', 'release_data_flag',
    'scaling', 'symmetric', 'three_glyphs', 'color_mode', 'length',
    'max_scale_factor', 'progress_text', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TensorGlyph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TensorGlyph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamp_scaling', 'color_glyphs',
            'extract_eigenvalues', 'scaling', 'symmetric', 'three_glyphs'],
            ['color_mode'], ['length', 'max_scale_factor', 'scale_factor']),
            title='Edit TensorGlyph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TensorGlyph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

