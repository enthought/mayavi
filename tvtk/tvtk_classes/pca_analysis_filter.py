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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class PCAAnalysisFilter(PointSetAlgorithm):
    """
    PCAAnalysisFilter - Performs principal component analysis of a set
    of aligned pointsets
    
    Superclass: PointSetAlgorithm
    
    PCAAnalysisFilter is a filter that takes as input a set of aligned
    pointsets (any object derived from PointSet) and performs a
    principal component analysis of the coordinates. This can be used to
    visualise the major or minor modes of variation seen in a set of
    similar biological objects with corresponding landmarks.
    PCAAnalysisFilter is designed to work with the output from the
    ProcrustesAnalysisFilter
    
    Call set_number_of_inputs(n) before calling set_input(_0) ...
    set_input(n-_1). Retrieve the outputs using get_output(_0) ...
    get_output(n-_1).
    
    PCAAnalysisFilter is an implementation of (for example):
    
    T. Cootes et al. : Active Shape Models - their training and
    application. Computer Vision and Image Understanding, 61(1):38-59,
    1995.
    
    The material can also be found in Tim Cootes' ever-changing online
    report published at his website: http://www.isbe.man.ac.uk/~bim/
    
    Caveats:
    
    All of the input pointsets must have the same number of points.
    
    Thanks:
    
    Rasmus Paulsen and Tim Hutton who developed and contributed this
    class
    
    See Also:
    
    ProcrustesAlignmentFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPCAAnalysisFilter, obj, update, **traits)
    
    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> PointSet
        C++: PointSet *GetInput(int idx)
        Retrieve the input with index idx (usually only used for pipeline
        tracing).
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(int, PointSet)
        C++: void SetInput(int idx, PointSet *p)
        V.set_input(int, DataObject)
        C++: void SetInput(int idx, DataObject *input)
        Specify the input pointset with index idx. Call set_number_of_inputs
        before calling this function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def _get_evals(self):
        return wrap_vtk(self._vtk_obj.GetEvals())
    evals = traits.Property(_get_evals, help=\
        """
        Get the vector of eigenvalues sorted in descending order
        """
    )

    def get_modes_required_for(self, *args):
        """
        V.get_modes_required_for(float) -> int
        C++: int GetModesRequiredFor(double proportion)
        Retrieve how many modes are necessary to model the given
        proportion of the variation. proportion should be between 0 and 1
        """
        ret = self._wrap_call(self._vtk_obj.GetModesRequiredFor, *args)
        return ret

    def get_parameterised_shape(self, *args):
        """
        V.get_parameterised_shape(FloatArray, PointSet)
        C++: void GetParameterisedShape(FloatArray *b,
            PointSet *shape)
        Fills the shape with:
        
        mean + b[0] * sqrt(eigenvalue[0]) * eigenvector[0]
             + b[1] * sqrt(eigenvalue[1]) * eigenvector[1] ...
             + b[sizeb-1] * sqrt(eigenvalue[bsize-1]) *
        eigenvector[bsize-1]
        
        here b are the parameters expressed in standard deviations bsize
        is the number of parameters in the b vector This function assumes
        that shape is allready allocated with the right size, it just
        moves the points.
        """
        my_args = deref_array(args, [('vtkFloatArray', 'vtkPointSet')])
        ret = self._wrap_call(self._vtk_obj.GetParameterisedShape, *my_args)
        return ret

    def get_shape_parameters(self, *args):
        """
        V.get_shape_parameters(PointSet, FloatArray, int)
        C++: void GetShapeParameters(PointSet *shape, FloatArray *b,
             int bsize)
        Return the bsize parameters b that best model the given shape (in
        standard deviations). That is that the given shape will be
        approximated by:
        
        shape ~ mean + b[0] * sqrt(eigenvalue[0]) * eigenvector[0]
                     + b[1] * sqrt(eigenvalue[1]) * eigenvector[1]
                ...
                     + b[bsize-1] * sqrt(eigenvalue[bsize-1]) *
        eigenvector[bsize-1]
        """
        my_args = deref_array(args, [('vtkPointSet', 'vtkFloatArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.GetShapeParameters, *my_args)
        return ret

    def set_number_of_inputs(self, *args):
        """
        V.set_number_of_inputs(int)
        C++: void SetNumberOfInputs(int n)
        Specify how many pointsets are going to be given as input.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfInputs, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PCAAnalysisFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

