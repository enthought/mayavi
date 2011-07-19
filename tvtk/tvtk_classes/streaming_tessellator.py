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

from tvtk.tvtk_classes.object import Object


class StreamingTessellator(Object):
    """
    StreamingTessellator - An algorithm that refines an initial
    simplicial tessellation using edge subdivision
    
    Superclass: Object
    
    This class is a simple algorithm that takes a single starting simplex
    -- a tetrahedron, triangle, or line segment -- and calls a function
    you pass it with (possibly many times) tetrahedra, triangles, or
    lines adaptively sampled from the one you specified. It uses an
    algorithm you specify to control the level of adaptivity.
    
    This class does not create UnstructuredGrid output because it is
    intended for use in mappers as well as filters. Instead, it calls the
    registered function with simplices as they are created.
    
    The subdivision algorithm should change the vertex coordinates (it
    must change both geometric and, if desired, parametric coordinates)
    of the midpoint. These coordinates need not be changed unless the
    evaluate_edge() member returns true. The StreamingTessellator
    itself has no way of creating a more accurate midpoint vertex.
    
    Here's how to use this class:
    - Call adaptively_sample1_facet, adaptively_sample2_facet, or
      adaptively_sample3_facet, with an edge, triangle, or tetrahedron you
      want tessellated.
    - The adaptive tessellator classifies each edge by passing the
      midpoint values to the EdgeSubdivisionCriterion.
    - After each edge is classified, the tessellator subdivides edges as
      required until the subdivision criterion is satisfied or the
      maximum subdivision depth has been reached.
    - Edges, triangles, or tetrahedra connecting the vertices generated
      by the subdivision algorithm are processed by calling the
      user-defined callback functions (set with set_tetrahedron_callback(),
    set_triangle_callback(), or set_edge_callback() ).
    
    Warning:
    
    Note that the vertices passed to adaptively_sample3_facet,
    adaptively_sample2_facet, or adaptively_sample1_facet must be at least 6,
    5, or 4 entries long, respectively! This is because the
    &lt;r,s,t&gt;, &lt;r,s&gt;, or &lt;r&gt; parametric coordinates of
    the vertices are maintained as the facet is subdivided. This
    information is often required by the subdivision algorithm in order
    to compute an error metric. You may change the number of parametric
    coordinates associated with each vertex using
    StreamingTessellator::SetEmbeddingDimension().
    
    Interpolating Field Values:
    
    If you wish, you may also use StreamingTessellator to interpolate
    field values at newly created vertices. Interpolated field values are
    stored just beyond the parametric coordinates associated with a
    vertex. They will always be double values; it does not make sense to
    interpolate a boolean or string value and your output and subdivision
    subroutines may always cast to a float or use floor() to truncate an
    interpolated value to an integer.
    
    See Also:
    
    EdgeSubdivisionCriterion
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamingTessellator, obj, update, **traits)
    
    def _get_const_private_data(self):
        return self._vtk_obj.GetConstPrivateData()
    def _set_const_private_data(self, arg):
        old_val = self._get_const_private_data()
        self._wrap_call(self._vtk_obj.SetConstPrivateData,
                        arg)
        self.trait_property_changed('const_private_data', old_val, arg)
    const_private_data = traits.Property(_get_const_private_data, _set_const_private_data, help=\
        """
        Get/Set a constant void pointer passed to the simplex output
        functions.
        """
    )

    def get_field_size(self, *args):
        """
        V.get_field_size(int) -> int
        C++: int GetFieldSize(int k)
        Get/Set the number of field value coordinates associated with
        each input and output point. The default is 0; no field values
        are interpolated. You may specify a different size, s, for each
        type of k -facet to be processed. For example, set_field_size( 2, 3
        ) would associate 3 field value coordinates with each input and
        output point of an adaptively_sample2_facet call, but does not say
        anything about input or output points of adaptively_sample1_facet.
        Call set_field_size( -1, s ) to specify the same dimension for all
        possible k values.s may not exceed
        StreamingTessellator::MaxFieldSize. This is a compile-time
        constant that defaults to 18, which is large enough for a scalar,
        vector, tensor, normal, and texture coordinate to be included at
        each point.
        
        Normally, you will not call set_field_size() directly; instead,
        subclasses of EdgeSubdivisionCriterion, such as
        ShoeMeshSubdivisionAlgorithm, will call it for you.
        
        In any event, setting field_size to a non-zero value means you
        must pass field values to the adaptively_samplek_facet routines;
        For example,
            StreamingTessellator* t = StreamingTessellator::New();
            t->_set_field_size( 1, 3 );
            t->_set_embedding_dimension( 1, 1 ); // not really required, this is the default
            double p0[3+1+3] = { x0, y0, z0, r0, fx0, fy0, fz0 };
            double p1[3+1+3] = { x1, y1, z1, r1, fx1, fy1, fz1 };
            t->_adaptively_sample1_facet( p0, p1 );
          This would adaptively sample an curve (1-facet) with geometry
        and a vector field at every output point on the curve.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldSize, *args)
        return ret

    def set_field_size(self, *args):
        """
        V.set_field_size(int, int)
        C++: virtual void SetFieldSize(int k, int s)
        Get/Set the number of field value coordinates associated with
        each input and output point. The default is 0; no field values
        are interpolated. You may specify a different size, s, for each
        type of k -facet to be processed. For example, set_field_size( 2, 3
        ) would associate 3 field value coordinates with each input and
        output point of an adaptively_sample2_facet call, but does not say
        anything about input or output points of adaptively_sample1_facet.
        Call set_field_size( -1, s ) to specify the same dimension for all
        possible k values.s may not exceed
        StreamingTessellator::MaxFieldSize. This is a compile-time
        constant that defaults to 18, which is large enough for a scalar,
        vector, tensor, normal, and texture coordinate to be included at
        each point.
        
        Normally, you will not call set_field_size() directly; instead,
        subclasses of EdgeSubdivisionCriterion, such as
        ShoeMeshSubdivisionAlgorithm, will call it for you.
        
        In any event, setting field_size to a non-zero value means you
        must pass field values to the adaptively_samplek_facet routines;
        For example,
            StreamingTessellator* t = StreamingTessellator::New();
            t->_set_field_size( 1, 3 );
            t->_set_embedding_dimension( 1, 1 ); // not really required, this is the default
            double p0[3+1+3] = { x0, y0, z0, r0, fx0, fy0, fz0 };
            double p1[3+1+3] = { x1, y1, z1, r1, fx1, fy1, fz1 };
            t->_adaptively_sample1_facet( p0, p1 );
          This would adaptively sample an curve (1-facet) with geometry
        and a vector field at every output point on the curve.
        """
        ret = self._wrap_call(self._vtk_obj.SetFieldSize, *args)
        return ret

    def _get_subdivision_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetSubdivisionAlgorithm())
    def _set_subdivision_algorithm(self, arg):
        old_val = self._get_subdivision_algorithm()
        self._wrap_call(self._vtk_obj.SetSubdivisionAlgorithm,
                        deref_vtk(arg))
        self.trait_property_changed('subdivision_algorithm', old_val, arg)
    subdivision_algorithm = traits.Property(_get_subdivision_algorithm, _set_subdivision_algorithm, help=\
        """
        Get/Set the algorithm used to determine whether an edge should be
        subdivided or left as-is. This is used once for each call to
        adaptively_sample1_facet (which is recursive and will call itself
        resulting in additional edges to be checked) or three times for
        each call to adaptively_sample2_facet (also recursive).
        """
    )

    def get_embedding_dimension(self, *args):
        """
        V.get_embedding_dimension(int) -> int
        C++: int GetEmbeddingDimension(int k)
        Get/Set the number of parameter-space coordinates associated with
        each input and output point. The default is k for k -facets. You
        may specify a different dimension, d, for each type of k -facet
        to be processed. For example, set_embedding_dimension( 2, 3 ) would
        associate r, s, andt coordinates with each input and output point
        generated by adaptively_sample2_facet but does not say anything
        about input or output points generated by_adaptively_sample1_facet.
        Call set_embedding_dimension( -1, d ) to specify the same dimension
        for all possible k values.d may not exceed 8, as that would be
        plain silly.
        """
        ret = self._wrap_call(self._vtk_obj.GetEmbeddingDimension, *args)
        return ret

    def set_embedding_dimension(self, *args):
        """
        V.set_embedding_dimension(int, int)
        C++: virtual void SetEmbeddingDimension(int k, int d)
        Get/Set the number of parameter-space coordinates associated with
        each input and output point. The default is k for k -facets. You
        may specify a different dimension, d, for each type of k -facet
        to be processed. For example, set_embedding_dimension( 2, 3 ) would
        associate r, s, andt coordinates with each input and output point
        generated by adaptively_sample2_facet but does not say anything
        about input or output points generated by_adaptively_sample1_facet.
        Call set_embedding_dimension( -1, d ) to specify the same dimension
        for all possible k values.d may not exceed 8, as that would be
        plain silly.
        """
        ret = self._wrap_call(self._vtk_obj.SetEmbeddingDimension, *args)
        return ret

    def _get_private_data(self):
        return self._vtk_obj.GetPrivateData()
    def _set_private_data(self, arg):
        old_val = self._get_private_data()
        self._wrap_call(self._vtk_obj.SetPrivateData,
                        arg)
        self.trait_property_changed('private_data', old_val, arg)
    private_data = traits.Property(_get_private_data, _set_private_data, help=\
        """
        Get/Set a void pointer passed to the triangle and edge output
        functions.
        """
    )

    maximum_number_of_subdivisions = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Get/Set the maximum number of subdivisions that may occur.
        """
    )
    def _maximum_number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSubdivisions,
                        self.maximum_number_of_subdivisions)

    def get_case_count(self, *args):
        """
        V.get_case_count(int) -> int
        C++: IdType GetCaseCount(int c)
        Reset/access the histogram of subdivision cases encountered. The
        histogram may be used to examine coverage during testing as well
        as characterizing the tessellation algorithm's performance. You
        should call reset_counts() once, at the beginning of a stream of
        tetrahedra. It must be called before adaptively_sample3_facet() to
        prevent uninitialized memory reads.
        
        These functions have no effect (and return 0) when
        PARAVIEW_DEBUG_TESSELLATOR has not been defined. By default,
        PARAVIEW_DEBUG_TESSELLATOR is not defined, and your code will be
        fast and efficient. Really!
        """
        ret = self._wrap_call(self._vtk_obj.GetCaseCount, *args)
        return ret

    def get_subcase_count(self, *args):
        """
        V.get_subcase_count(int, int) -> int
        C++: IdType GetSubcaseCount(int casenum, int sub)
        Reset/access the histogram of subdivision cases encountered. The
        histogram may be used to examine coverage during testing as well
        as characterizing the tessellation algorithm's performance. You
        should call reset_counts() once, at the beginning of a stream of
        tetrahedra. It must be called before adaptively_sample3_facet() to
        prevent uninitialized memory reads.
        
        These functions have no effect (and return 0) when
        PARAVIEW_DEBUG_TESSELLATOR has not been defined. By default,
        PARAVIEW_DEBUG_TESSELLATOR is not defined, and your code will be
        fast and efficient. Really!
        """
        ret = self._wrap_call(self._vtk_obj.GetSubcaseCount, *args)
        return ret

    def reset_counts(self):
        """
        V.reset_counts()
        C++: void ResetCounts()
        Reset/access the histogram of subdivision cases encountered. The
        histogram may be used to examine coverage during testing as well
        as characterizing the tessellation algorithm's performance. You
        should call reset_counts() once, at the beginning of a stream of
        tetrahedra. It must be called before adaptively_sample3_facet() to
        prevent uninitialized memory reads.
        
        These functions have no effect (and return 0) when
        PARAVIEW_DEBUG_TESSELLATOR has not been defined. By default,
        PARAVIEW_DEBUG_TESSELLATOR is not defined, and your code will be
        fast and efficient. Really!
        """
        ret = self._vtk_obj.ResetCounts()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),
    ('maximum_number_of_subdivisions', 'GetMaximumNumberOfSubdivisions'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display',
    'maximum_number_of_subdivisions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamingTessellator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamingTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['maximum_number_of_subdivisions']),
            title='Edit StreamingTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamingTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

