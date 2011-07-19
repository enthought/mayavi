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


class XMLDataElement(Object):
    """
    XMLDataElement - Represents an XML element and those nested inside.
    
    Superclass: Object
    
    XMLDataElement is used by XMLDataParser to represent an XML
    element.  It provides methods to access the element's attributes and
    nested elements in a convenient manner.  This allows easy traversal
    of an input XML file by XMLReader and its subclasses.
    
    See Also:
    
    XMLDataParser
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLDataElement, obj, update, **traits)
    
    character_data_width = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the width (in number of fields) that character data (that
        between open and closing tags ie. <X> ... </X>) is printed. If
        the width is less than one the tag's character data is printed
        all on one line. If it is greater than one the character data is
        streamed insterting line feeds every width number of fields. See
        print_xml.
        """
    )
    def _character_data_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCharacterDataWidth,
                        self.character_data_width)

    name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the element.  This is its XML tag.
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Set/Get the parent of this element.
        """
    )

    attribute = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the attribute with the given name and value. If it doesn't
        exist, adds it.
        """
    )
    def _attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttribute,
                        self.attribute)

    xml_byte_index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the offset from the beginning of the XML document to this
        element.
        """
    )
    def _xml_byte_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMLByteIndex,
                        self.xml_byte_index)

    character_data = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Set/Get the character data between XML start/end tags.
        """
    )
    def _character_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCharacterData,
                        self.character_data)

    id = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the value of the id attribute of the element, if any.
        """
    )
    def _id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetId,
                        self.id)

    attribute_encoding = traits.Trait(3, traits.Range(0, 20, enter_set=True, auto_set=False), help=\
        """
        Get/Set the internal character encoding of the attributes.
        Default type is VTK_ENCODING_UTF_8. Note that a XMLDataParser
        has its own attributes_encoding ivar. If this ivar is set to
        something other than VTK_ENCODING_NONE, it will be used to set
        the attribute encoding of each XMLDataElement created by this
        XMLDataParser.
        """
    )
    def _attribute_encoding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeEncoding,
                        self.attribute_encoding)

    def get_attribute_name(self, *args):
        """
        V.get_attribute_name(int) -> string
        C++: const char *GetAttributeName(int idx)
        Get the n-th attribute name. Returns 0 if there is no such
        attribute.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeName, *args)
        return ret

    def get_attribute_value(self, *args):
        """
        V.get_attribute_value(int) -> string
        C++: const char *GetAttributeValue(int idx)
        Get the n-th attribute value. Returns 0 if there is no such
        attribute.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeValue, *args)
        return ret

    def get_nested_element(self, *args):
        """
        V.get_nested_element(int) -> XMLDataElement
        C++: XMLDataElement *GetNestedElement(int index)
        Get the element nested in this one at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetNestedElement, *args)
        return wrap_vtk(ret)

    def _get_number_of_attributes(self):
        return self._vtk_obj.GetNumberOfAttributes()
    number_of_attributes = traits.Property(_get_number_of_attributes, help=\
        """
        Get the number of attributes.
        """
    )

    def _get_number_of_nested_elements(self):
        return self._vtk_obj.GetNumberOfNestedElements()
    number_of_nested_elements = traits.Property(_get_number_of_nested_elements, help=\
        """
        Get the number of elements nested in this one.
        """
    )

    def _get_root(self):
        return wrap_vtk(self._vtk_obj.GetRoot())
    root = traits.Property(_get_root, help=\
        """
        Get root of the XML tree this element is part of.
        """
    )

    def get_scalar_attribute(self, *args):
        """
        V.get_scalar_attribute(string, int) -> int
        C++: int GetScalarAttribute(const char *name, int &value)
        V.get_scalar_attribute(string, float) -> int
        C++: int GetScalarAttribute(const char *name, double &value)
        V.get_scalar_attribute(string, int) -> int
        C++: int GetScalarAttribute(const char *name,
            unsigned long &value)
        Get the attribute with the given name and converted to a scalar
        value.  Returns whether value was extracted.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarAttribute, *args)
        return ret

    def get_word_type_attribute(self, *args):
        """
        V.get_word_type_attribute(string, int) -> int
        C++: int GetWordTypeAttribute(const char *name, int &value)
        Get the attribute with the given name and converted to a word
        type such as VTK_FLOAT or VTK_UNSIGNED_LONG.
        """
        ret = self._wrap_call(self._vtk_obj.GetWordTypeAttribute, *args)
        return ret

    def add_character_data(self, *args):
        """
        V.add_character_data(string, int)
        C++: void AddCharacterData(const char *c, size_t length)
        Set/Get the character data between XML start/end tags.
        """
        ret = self._wrap_call(self._vtk_obj.AddCharacterData, *args)
        return ret

    def add_nested_element(self, *args):
        """
        V.add_nested_element(XMLDataElement)
        C++: void AddNestedElement(XMLDataElement *element)
        Add nested element
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddNestedElement, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(XMLDataElement)
        C++: virtual void DeepCopy(XMLDataElement *elem)
        Copy this element from another of the same type (elem),
        recursively. Old attributes and nested elements are removed, new
        ones are created given the contents of 'elem'. Warning: Parent is
        ignored.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def find_nested_element(self, *args):
        """
        V.find_nested_element(string) -> XMLDataElement
        C++: XMLDataElement *FindNestedElement(const char *id)
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ret = self._wrap_call(self._vtk_obj.FindNestedElement, *args)
        return wrap_vtk(ret)

    def find_nested_element_with_name(self, *args):
        """
        V.find_nested_element_with_name(string) -> XMLDataElement
        C++: XMLDataElement *FindNestedElementWithName(
            const char *name)
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ret = self._wrap_call(self._vtk_obj.FindNestedElementWithName, *args)
        return wrap_vtk(ret)

    def find_nested_element_with_name_and_attribute(self, *args):
        """
        V.find_nested_element_with_name_and_attribute(string, string, string)
            -> XMLDataElement
        C++: XMLDataElement *FindNestedElementWithNameAndAttribute(
            const char *name, const char *att_name, const char *att_value)
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ret = self._wrap_call(self._vtk_obj.FindNestedElementWithNameAndAttribute, *args)
        return wrap_vtk(ret)

    def find_nested_element_with_name_and_id(self, *args):
        """
        V.find_nested_element_with_name_and_id(string, string)
            -> XMLDataElement
        C++: XMLDataElement *FindNestedElementWithNameAndId(
            const char *name, const char *id)
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ret = self._wrap_call(self._vtk_obj.FindNestedElementWithNameAndId, *args)
        return wrap_vtk(ret)

    def is_equal_to(self, *args):
        """
        V.is_equal_to(XMLDataElement) -> int
        C++: virtual int IsEqualTo(XMLDataElement *elem)
        Check if the instance has the same name, attributes, character
        data and nested elements contents than the given element (this
        method is applied recursively on the nested elements, and they
        must be stored in the same order). Warning: Id, Parent,
        xml_byte_index are ignored.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsEqualTo, *my_args)
        return ret

    def lookup_element(self, *args):
        """
        V.lookup_element(string) -> XMLDataElement
        C++: XMLDataElement *LookupElement(const char *id)
        Lookup the element with the given id, starting at this scope.
        """
        ret = self._wrap_call(self._vtk_obj.LookupElement, *args)
        return wrap_vtk(ret)

    def lookup_element_with_name(self, *args):
        """
        V.lookup_element_with_name(string) -> XMLDataElement
        C++: XMLDataElement *LookupElementWithName(const char *name)
        Find the first nested element with given name. WARNING: the
        search is performed on the whole XML tree.
        """
        ret = self._wrap_call(self._vtk_obj.LookupElementWithName, *args)
        return wrap_vtk(ret)

    def print_xml(self, *args):
        """
        V.print_xml(string)
        C++: void PrintXML(const char *fname)
        Prints element tree as XML.
        """
        ret = self._wrap_call(self._vtk_obj.PrintXML, *args)
        return ret

    def remove_all_attributes(self):
        """
        V.remove_all_attributes()
        C++: virtual void RemoveAllAttributes()
        Remove one or all attributes.
        """
        ret = self._vtk_obj.RemoveAllAttributes()
        return ret
        

    def remove_all_nested_elements(self):
        """
        V.remove_all_nested_elements()
        C++: virtual void RemoveAllNestedElements()
        Remove all nested elements.
        """
        ret = self._vtk_obj.RemoveAllNestedElements()
        return ret
        

    def remove_attribute(self, *args):
        """
        V.remove_attribute(string)
        C++: virtual void RemoveAttribute(const char *name)
        Remove one or all attributes.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveAttribute, *args)
        return ret

    def remove_nested_element(self, *args):
        """
        V.remove_nested_element(XMLDataElement)
        C++: virtual void RemoveNestedElement(XMLDataElement *)
        Remove nested element.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNestedElement, *my_args)
        return ret

    def set_double_attribute(self, *args):
        """
        V.set_double_attribute(string, float)
        C++: void SetDoubleAttribute(const char *name, double value)
        Set the attribute with the given name. We can not use the same
        get_scalar_attribute() construct since the compiler will not be
        able to resolve between set_attribute(..., int) and
        set_attribute(..., unsigned long).
        """
        ret = self._wrap_call(self._vtk_obj.SetDoubleAttribute, *args)
        return ret

    def set_float_attribute(self, *args):
        """
        V.set_float_attribute(string, float)
        C++: void SetFloatAttribute(const char *name, float value)
        Set the attribute with the given name. We can not use the same
        get_scalar_attribute() construct since the compiler will not be
        able to resolve between set_attribute(..., int) and
        set_attribute(..., unsigned long).
        """
        ret = self._wrap_call(self._vtk_obj.SetFloatAttribute, *args)
        return ret

    def set_int_attribute(self, *args):
        """
        V.set_int_attribute(string, int)
        C++: void SetIntAttribute(const char *name, int value)
        Set the attribute with the given name. We can not use the same
        get_scalar_attribute() construct since the compiler will not be
        able to resolve between set_attribute(..., int) and
        set_attribute(..., unsigned long).
        """
        ret = self._wrap_call(self._vtk_obj.SetIntAttribute, *args)
        return ret

    def set_unsigned_long_attribute(self, *args):
        """
        V.set_unsigned_long_attribute(string, int)
        C++: void SetUnsignedLongAttribute(const char *name,
            unsigned long value)
        Set the attribute with the given name. We can not use the same
        get_scalar_attribute() construct since the compiler will not be
        able to resolve between set_attribute(..., int) and
        set_attribute(..., unsigned long).
        """
        ret = self._wrap_call(self._vtk_obj.SetUnsignedLongAttribute, *args)
        return ret

    _updateable_traits_ = \
    (('name', 'GetName'), ('character_data', 'GetCharacterData'),
    ('attribute', 'GetAttribute'), ('debug', 'GetDebug'),
    ('character_data_width', 'GetCharacterDataWidth'), ('xml_byte_index',
    'GetXMLByteIndex'), ('reference_count', 'GetReferenceCount'),
    ('attribute_encoding', 'GetAttributeEncoding'), ('id', 'GetId'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'attribute',
    'attribute_encoding', 'character_data', 'character_data_width', 'id',
    'name', 'xml_byte_index'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLDataElement, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLDataElement properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['attribute', 'attribute_encoding',
            'character_data', 'character_data_width', 'id', 'name',
            'xml_byte_index']),
            title='Edit XMLDataElement properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLDataElement properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

