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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class DiagonalMatrixSource(ArrayDataAlgorithm):
    """
    DiagonalMatrixSource - generates a sparse or dense square matrix
    
    Superclass: ArrayDataAlgorithm
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiagonalMatrixSource, obj, update, **traits)
    
    sub_diagonal = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to subdiagonal elements
        (default: 0)
        """
    )
    def _sub_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubDiagonal,
                        self.sub_diagonal)

    diagonal = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to diagonal elements
        (default: 1)
        """
    )
    def _diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiagonal,
                        self.diagonal)

    row_label = traits.String(r"rows", enter_set=True, auto_set=False, help=\
        """
        Controls the output matrix row dimension label. Default: "rows"
        """
    )
    def _row_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRowLabel,
                        self.row_label)

    array_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _array_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayType,
                        self.array_type)

    super_diagonal = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to superdiagonal elements
        (default: 0)
        """
    )
    def _super_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSuperDiagonal,
                        self.super_diagonal)

    extents = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Stores the extents of the output matrix (which is square)
        """
    )
    def _extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtents,
                        self.extents)

    column_label = traits.String(r"columns", enter_set=True, auto_set=False, help=\
        """
        Controls the output matrix column dimension label. Default:
        "columns"
        """
    )
    def _column_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColumnLabel,
                        self.column_label)

    _updateable_traits_ = \
    (('extents', 'GetExtents'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('diagonal', 'GetDiagonal'), ('column_label',
    'GetColumnLabel'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('array_type', 'GetArrayType'), ('row_label', 'GetRowLabel'),
    ('sub_diagonal', 'GetSubDiagonal'), ('super_diagonal',
    'GetSuperDiagonal'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_type', 'column_label', 'diagonal',
    'extents', 'progress_text', 'row_label', 'sub_diagonal',
    'super_diagonal'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiagonalMatrixSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['array_type', 'column_label', 'diagonal',
            'extents', 'row_label', 'sub_diagonal', 'super_diagonal']),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

