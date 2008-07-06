
from enthought.traits.api import Property, Str, Button, \
    Any, Instance, HasStrictTraits
from enthought.traits.ui.api import EnumEditor, View, Item, HGroup, \
    VGroup, spring, Group, TextEditor, HTMLEditor, InstanceEditor, \
    TabularEditor, Label, TitleEditor

from enthought.traits.ui.tabular_adapter import TabularAdapter

from data_source_factory import DataSourceFactory


############################################################################
# class ArrayColumnWrapper
############################################################################
class ArrayColumnWrapper(HasStrictTraits):

    name = Str
    shape = Str


############################################################################
# class ArrayColumnAdapter
############################################################################
class ArrayColumnAdapter(TabularAdapter):

    columns = [ ('name',  'name'),
                ('shape', 'shape'), ]

    width = 100



############################################################################
# The DataSourceWizardView class
############################################################################
class DataSourceWizardView(DataSourceFactory):

    _data_sources_wrappers = Property(depends_on='data_sources')

    def _get__data_sources_wrappers(self):
         return [
            ArrayColumnWrapper(name=name, 
                shape=repr(self.data_sources[name].shape))
                    for name in self._data_sources_names
                ]
            

    #----------------------------------------------------------------------
    # Private traits
    #----------------------------------------------------------------------

    _top_label = Str('Describe your data')

    _array_label = Str('Available arrays')

    _top_text = Str("This dialog helps you import data arrays in "
                    "Mayavi.")

    _data_type_text = Str("What does your data represents?" )

    _lines_text = Str("Connect the points with lines:" )

    _scalar_data_text = Str("The array giving the value of the scalars:")

    _optional_scalar_data_text = Str("Associate scalars with the data points:")

    _connectivity_text = Str("The array giving the of triangles:")

    _vector_data_text = Str("Associate vector components:")

    _position_text = Str("The positions of the various datapoints " )

    _shown_help_text = Str

    # A traits pointing to the object, to play well with traitsUI
    _self = Instance(DataSourceFactory)

    _suitable_traits_view = Property(depends_on="data_type")

    def _get__suitable_traits_view(self):
        return self.view_mapping[self.data_type]

    ui = Any(False)

    _ok_button = Button(label='OK')

    def __ok_button_fired(self):
        if self.ui:
            self.ui.dispose()
            self.build_data_source()


    _cancel_button = Button(label='Cancel')

    def __cancel_button_fired(self):
        if self.ui:
            self.ui.dispose()

    _is_ok = Property()

    def _get__is_ok(self):
        """ Validates if the OK button is enabled.
        """
        if self.data_type == 'A surface':
            return False
        elif self.data_type == 'A planar surface':
            return False
        elif self.data_type == 'A set of vectors':
            return False
        elif self.data_type == 'Volumetric data':
            return False
        elif self.data_type == \
                'A set of points, that can be connected by lines':
            return False
        return True


    #----------------------------------------------------------------------
    # TraitsUI views
    #----------------------------------------------------------------------


    _data_point_group = \
                    Group(
                       HGroup(
                           Item('position_implicit', label='implicit'),
                           spring,
                       visible_when=
                """not data_type in (
                    "A set of points, that can be connected by lines",
                    "A surface",
                )""",
                       ),
                       HGroup(
                           Item('x_position', label='x',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('y_position', label='y',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('z_position', label='z',
                               editor=EnumEditor(name='_data_sources_names')), 
                           enabled_when='not position_implicit',
                       ),
                       label='Position of the data points',
                       show_border=True,
                   ),


    _scalar_data_group = \
                   Group(
                       Item('_scalar_data_text', style='readonly', 
                           show_label=False),
                       HGroup(
                           Item('scalar_data', 
                               editor=EnumEditor(name='_data_sources_names')),
                           spring,
                           show_labels=False,
                           ),
                       label='Scalar value',
                       show_border=True,
                       show_labels=False,
                   ),


    _connectivity_group = \
                   Group(
                       Item('_connectivity_text', style='readonly'),
                       HGroup(
                        Item('connectivity_implicit', 
                                label='Implicit'),
                        spring,
                        Item('connectivity',
                                editor=EnumEditor(name='_data_sources_names'),
                                enabled_when='not connectivity_implicit',
                                show_label=False,
                                ),
                       ),
                       label='Connectivity information',
                       show_border=True,
                       show_labels=False,
                   ),

    _optional_scalar_data_group = \
                   Group(
                       HGroup(
                       Item('_optional_scalar_data_text', style='readonly'),
                       'scalar_data_option',
                       show_labels=False,
                       ),
                       Item('_scalar_data_text', style='readonly', 
                            enabled_when='scalar_data_option',
                           show_label=False),
                       HGroup(
                           spring, 
                           Item('scalar_data', 
                               editor=EnumEditor(name='_data_sources_names'),
                               enabled_when='scalar_data_option'),
                           show_labels=False,
                           ),
                       label='Scalar data',
                       show_border=True,
                       show_labels=False,
                   ),


    _vector_data_group = \
                   VGroup(
                       HGroup(
                           Item('vector_u', label='u',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_v', label='v',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_w', label='w',
                               editor=EnumEditor(name='_data_sources_names')), 
                       ),
                       label='Vector data',
                       show_border=True,
                   ),


    _optional_vector_data_group = \
                   VGroup(
                        HGroup(
                            Item('_vector_data_text', style='readonly', 
                                editor=TextEditor(multi_line=True),
                                show_label=False),
                            Item('vector_data', show_label=False),
                        ),
                       HGroup(
                           Item('vector_u', label='u',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_v', label='v',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_w', label='w',
                               editor=EnumEditor(name='_data_sources_names')), 
                           enabled_when='vector_data',
                       ),
                       label='Vector data',
                       show_border=True,
                   ),


    _array_view = \
                View(
                    Item('_array_label', editor=TitleEditor(),
                        show_label=False),
                    Group(    
                    Item('_data_sources_wrappers', 
                      editor=TabularEditor(
                          adapter = ArrayColumnAdapter(),
                      ), 
                    ),
                    show_border=True,
                    show_labels=False
                ))

    _questions_view = View(
                Item('_top_label', editor=TitleEditor(),
                        show_label=False),
                Group(
                Item('_top_text', style='readonly', ),
                HGroup(
                    Item('_data_type_text', style='readonly'),
                    spring,
                    'data_type',
                    spring,
                    show_border=True,
                    show_labels=False,
                  ),
                HGroup(
                    Item('_self', style='custom', 
                        editor=InstanceEditor(
                                    view_name='_suitable_traits_view'),
                        ),
                    Group(
                        Item('_shown_help_text', editor=HTMLEditor(), 
                            width=300,
                            ),
                        show_labels=False,
                        show_border=True,
                        label='Help',
                    ),
                    show_labels=False,
                ),
                show_border=True,
                show_labels=False,
                ),
            )

    _set_of_points_view = \
                View(Group(
                   _data_point_group,
                   HGroup(
                       Item('_lines_text', style='readonly'), 
                       'lines',
                       label='Lines',
                       show_labels=False,
                       show_border=True,
                   ),
                   _optional_scalar_data_group,
                   _optional_vector_data_group,
                ))


    _surface_view = \
                View(Group(
                   _data_point_group,
                   _connectivity_group,
                   _optional_scalar_data_group,
                   _optional_vector_data_group,
                ))


    _planar_surface_view = \
                View(Group( 
                   _scalar_data_group,
                   # Ugly trick to force the width.
                   Group(_data_point_group, visible_when='False'),
                ))


    _set_of_vectors_view = \
                View(Group(
                   _vector_data_group,
                   _data_point_group,
                   _optional_scalar_data_group,
                ))


    _volumetric_data_view = \
                View(Group(
                   _scalar_data_group,
                   _data_point_group,
                ))


    _wizard_view = View(
            HGroup(
                Item('_self', style='custom', show_label=False,
                     editor=InstanceEditor(view='_array_view'),
                     width=0.2,
                     ),
                '_',
                Item('_self', style='custom', show_label=False,
                     editor=InstanceEditor(view='_questions_view'),
                     ),
                ),
            '_',
            HGroup(spring, 
                '_cancel_button', 
                Item('_ok_button', enabled_when='_is_ok'),
                show_labels=False
            ),
            title='Import arrays',
            )



    #----------------------------------------------------------------------
    # Public interface
    #----------------------------------------------------------------------

    def __init__(self, **traits):
        DataSourceFactory.__init__(self, **traits)
        self._self = self


    def view_wizard(self):
        """ Pops up the view of the wizard, and keeps the reference it to
            be able to close it.
        """
        self.ui = self.edit_traits(view='_wizard_view')



if __name__ == '__main__':
    from numpy import mgrid

    x, y, z = mgrid[-5:5, -5:5, -5:5]
    r = x**2 + y**2 + z**2

    data_sources = {
            'x':x,
            'y':y,
            'z':z,
            'r':r
        }

    wizard = DataSourceWizardView(data_sources=data_sources)

    wizard.view_wizard()

