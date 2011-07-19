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

from tvtk.tvtk_classes.tree_algorithm import TreeAlgorithm


class XMLTreeReader(TreeAlgorithm):
    """
    XMLTreeReader - reads an XML file into a Tree
    
    Superclass: TreeAlgorithm
    
    XMLTreeReader parses an XML file and uses the nesting structure of
    the XML tags to generate a tree.  Node attributes are assigned to
    node arrays, and the special arrays .tagname and .chardata contain
    the tag type and the text internal to the tag, respectively.  The
    arrays are of type StringArray.  There is an array for each
    attribute type in the XML file, even if it appears in only one tag. 
    If an attribute is missing from a tag, its value is the empty string.
    
    If mask_arrays is on (the default is off), the filter will
    additionally make bit arrays whose names are prepended with ".valid."
    which are 1 if the element contains that attribute, and 0 otherwise.
    
    For example, the XML file containing the text:
    
    &lt;node name="jeff" age="26"&gt;
      this is text in jeff's node
      &lt;node name="joe"&gt;
        &lt;node name="al" initials="amb" other="something"/&gt;
        &lt;node name="dave" age="30"/&gt;
      &lt;/node&gt;
      &lt;node name="lisa"&gt;this is text in lisa's node&lt;/node&gt;
      &lt;node name="darlene" age="29"/&gt; &lt;/node&gt; 
    
    would be parsed into a tree with the following node IDs and
    structure:
    
    0 (jeff) - children: 1 (joe), 4 (lisa), 5 (darlene) 1 (joe)  -
    children: 2 (al), 3 (dave) 2 (al) 3 (dave) 4 (lisa) 5 (darlene) 
    
    and the node data arrays would be as follows:
    
    name      initials  other     age       .tagname  .chardata
    ----------------------------------------------------------------------
        -------------------------- jeff      (empty)   (empty)   26      
      node     "  this is text in jeff's node\n  \n  \n  \n" joe      
        (empty)   (empty)   (empty)    node     "\n    \n    \n  " al    
       amb       something (empty)    node     (empty) dave      (empty) 
     (empty)   30         node     (empty) lisa      (empty)   (empty)  
        (empty)    node     "this is text in lisa's node" darlene  
        (empty)   (empty)   29         node     (empty) 
    
    There would also be the following bit arrays if mask_arrays is on:
    
    .valid.name   .valid.initials   .valid.other   .valid.age
    --------------------------------------------------------- 1          
      0                 0              1 1             0                
        0              0 1             1                 1              0
        1             0                 0              1 1             0 
                   0              0 1             0                 0    
             1 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLTreeReader, obj, update, **traits)
    
    generate_edge_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        Set whether to use an property from the XML file as pedigree ids
        (off), or generate a new array with integer values starting at
        zero (on). Default is on.
        """
    )
    def _generate_edge_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateEdgePedigreeIds,
                        self.generate_edge_pedigree_ids_)

    generate_vertex_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        Set whether to use an property from the XML file as pedigree ids
        (off), or generate a new array with integer values starting at
        zero (on). Default is on.
        """
    )
    def _generate_vertex_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertexPedigreeIds,
                        self.generate_vertex_pedigree_ids_)

    read_char_data = tvtk_base.false_bool_trait(help=\
        """
        If on, stores the XML character data (i.e. textual data between
        tags) into an array named char_data_field, otherwise this field is
        skipped. Default is off.
        """
    )
    def _read_char_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadCharData,
                        self.read_char_data_)

    mask_arrays = tvtk_base.false_bool_trait(help=\
        """
        If on, makes bit arrays for each attribute with name
        .valid.attribute_name for each attribute.  Default is off.
        """
    )
    def _mask_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskArrays,
                        self.mask_arrays_)

    read_tag_name = tvtk_base.true_bool_trait(help=\
        """
        If on, stores the XML tag name data in a field called .tagname
        otherwise this field is skipped. Default is on.
        """
    )
    def _read_tag_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadTagName,
                        self.read_tag_name_)

    edge_pedigree_id_array_name = traits.String(r"edge id", enter_set=True, auto_set=False, help=\
        """
        The name of the edge pedigree ids. Default is "edge id".
        """
    )
    def _edge_pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgePedigreeIdArrayName,
                        self.edge_pedigree_id_array_name)

    vertex_pedigree_id_array_name = traits.String(r"vertex id", enter_set=True, auto_set=False, help=\
        """
        The name of the vertex pedigree ids. Default is "vertex id".
        """
    )
    def _vertex_pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexPedigreeIdArrayName,
                        self.vertex_pedigree_id_array_name)

    xml_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        If set, and file_name is not set, reads in the XML string.
        """
    )
    def _xml_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMLString,
                        self.xml_string)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        If set, reads in the XML file specified.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('xml_string', 'GetXMLString'), ('read_char_data',
    'GetReadCharData'), ('file_name', 'GetFileName'),
    ('generate_edge_pedigree_ids', 'GetGenerateEdgePedigreeIds'),
    ('reference_count', 'GetReferenceCount'), ('read_tag_name',
    'GetReadTagName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('vertex_pedigree_id_array_name',
    'GetVertexPedigreeIdArrayName'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('generate_vertex_pedigree_ids', 'GetGenerateVertexPedigreeIds'),
    ('edge_pedigree_id_array_name', 'GetEdgePedigreeIdArrayName'),
    ('progress', 'GetProgress'), ('mask_arrays', 'GetMaskArrays'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_edge_pedigree_ids',
    'generate_vertex_pedigree_ids', 'global_warning_display',
    'mask_arrays', 'read_char_data', 'read_tag_name', 'release_data_flag',
    'edge_pedigree_id_array_name', 'file_name', 'progress_text',
    'vertex_pedigree_id_array_name', 'xml_string'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLTreeReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLTreeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_edge_pedigree_ids',
            'generate_vertex_pedigree_ids', 'mask_arrays', 'read_char_data',
            'read_tag_name'], [], ['edge_pedigree_id_array_name', 'file_name',
            'vertex_pedigree_id_array_name', 'xml_string']),
            title='Edit XMLTreeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLTreeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

