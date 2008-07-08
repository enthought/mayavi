
from numpy import ones_like

from enthought.traits.api import Property, Str, Button, Trait, \
    Any, Instance, HasStrictTraits, false, Enum, Dict, HasTraits
from enthought.traits.ui.api import EnumEditor, View, Item, HGroup, \
    VGroup, spring, Group, TextEditor, HTMLEditor, InstanceEditor, \
    TabularEditor, TitleEditor, Label

from enthought.traits.ui.tabular_adapter import TabularAdapter

from data_source_factory import DataSourceFactory
from data_source_factory import view as view_data_source

############################################################################
# The DataSourceWizard class
############################################################################
class DataSourceWizard(HasTraits):

    data_sources = Dict

    _data_sources_names = Property(depends_on='data_sources')

    def _get__data_sources_names(self):
        names = self.data_sources.keys()
        names.sort()
        return names


    # Dictionnary mapping the views
    data_type = Trait('point',
            {'A surface':
                    'surface',
            'A set of points, that can be connected by lines':
                    'point',
            'A set of vectors':
                    'vector',
            'Volumetric data':
                    'volumetric',
            })


    position_type = Trait('image data',
                     {'Specified explicitly':
                        'explicit',
                      'Given by the shape of the data array':
                        'image data',
                      'On an orthogonal grid with varying spacing':
                        'orthogonal grid',
                        })


    # Whether or not the data points should be connected.
    lines = false

    # The scalar data selection
    scalar_data = Str('', help="Select the array that gives the value of the "
                            "scalars plotted.")

    position_x = Str(help="Select the array that gives the x "
                        "position of the data points")
    
    position_y = Str(help="Select the array that gives the y "
                        "position of the data points")
    
    position_z = Str(help="Select the array that gives the z "
                        "position of the data points")

    connectivity_triangles = Str

    has_vector_data = false(help="""Do you want to plot vector components?""")

    # A boolean to ask the user if he wants to load scalar data
    has_scalar_data = false

    vector_u = Str

    vector_v = Str

    vector_w =  Str


    #----------------------------------------------------------------------
    # Public interface
    #----------------------------------------------------------------------

    def init_arrays(self):
        # Force all the array names to be properly initialized
        array_names = set(self.data_sources.keys())
        if len(array_names) == 0:
            # We should probably bail out here.
            return False
        for attr in ('position_x', 'position_y', 'position_z',
                     'scalar_data', 'vector_u', 'vector_v',
                     'vector_w', 'connectivity_triangles',
                     ):
            if len(array_names) > 0:
                array_name = array_names.pop()
            setattr(self, attr, array_name)
            


    def guess_array_names(self):
        """ Do some guess work on the arrays to find sensible default.
        """
        array_names = set(self.data_sources.keys())
        found_some = False
        if set(('x', 'y', 'z')).issubset(array_names):
            self.position_x = 'x'
            self.position_y = 'y'
            self.position_z = 'z'
            array_names = array_names.difference(('x', 'y', 'z'))
            found_some = True
        elif set(('X', 'Y', 'Z')).issubset(array_names):
            self.position_x = 'X'
            self.position_y = 'Y'
            self.position_z = 'Z'
            array_names = array_names.difference(('X', 'Y', 'Z'))
            found_some = True

        if set(('u', 'v', 'w')).issubset(array_names):
            self.vector_u = 'u'
            self.vector_v = 'v'
            self.vector_w = 'w'
            array_names = array_names.difference(('u', 'v', 'w'))
            found_some = True
        elif set(('U', 'V', 'W')).issubset(array_names):
            self.vector_u = 'U'
            self.vector_v = 'V'
            self.vector_w = 'W'
            array_names = array_names.difference(('U', 'V', 'W'))
            found_some = True

        if found_some:
            # Need to re-attribute the guessed names.
            for attr in ('scalar_data', 'vector_u', 'vector_v',
                        'vector_w', 'connectivity_triangles'):
                if len(array_names) > 0:
                    setattr(self, attr, array_names.pop())
                else:
                    break


    def build_data_source(self):
        """ This is where we apply the selections made by the user in
            in the wizard to build the data source.
        """
        data = lambda name: self.data_sources[name]
        factory = DataSourceFactory()
        if self.has_vector_data or self.data_type_ == 'vector':
            # In the vector view, the user is not explicitly asked to 
            # Enable vectors.
            factory.has_vector_data = True
            factory.vector_u = data(self.vector_u)
            factory.vector_v = data(self.vector_v)
            factory.vector_w = data(self.vector_w)
        
        if self.has_scalar_data or self.data_type_ == 'volumetric':
            # In the volumetric view, the user is not explicitly asked to 
            # Enable scalars.
            factory.scalar_data = data(self.scalar_data)

        if self.data_type_ == 'point':
            # The only sensible data structures for points is with
            # explicit positioning.
            self.position_type_ = 'explicit'
            # In addition, this view does not allow for
            # connectivity with triangles.
            self.connectivity_triangles = ''
            factory.unstructured = True

        if self.position_type_ == "image data":
            factory.position_implicit = True
            if not self.has_scalar_data:
                # With image data we need a scalar array always:
                factory.scalar_data = ones_like(data(self.vector_u))
        else:
            factory.position_x = data(self.position_x)
            factory.position_y = data(self.position_y)
            factory.position_z = data(self.position_z)
        if self.position_type_ == "orthogonal grid":
            factory.orthogonal_grid = True
        if self.position_type_ == "explicit" and self.data_type_ == "surface":
            factory.connectivity_triangles = data(self.connectivity_triangles)
        if self.lines:
            factory.lines = True

        if self.connectivity_triangles == '':
            factory.connectivity_triangles = None

        self.factory = factory

        self.data_source = factory.build_data_source()
        view_data_source(self.data_source)
        from enthought.mayavi.mlab import show_engine
        show_engine()


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
class DataSourceWizardView(DataSourceWizard):

    #----------------------------------------------------------------------
    # Private traits
    #----------------------------------------------------------------------

    _top_label = Str('Describe your data')

    _array_label = Str('Available arrays')

    _data_type_text = Str("What does your data represents?" )

    _lines_text = Str("Connect the points with lines:" )

    _scalar_data_text = Str("Array giving the value of the scalars:")

    _optional_scalar_data_text = Str("Associate scalars with the data points:")

    _connectivity_text = Str("Array giving the triangles:")

    _vector_data_text = Str("Associate vector components:")

    _position_text = Property(depends_on="position_type_")

    _position_text_dict = {'explicit':
                'Coordinnates of the data points:',
                           'orthogonal grid':
                'Position of the layers along each axis:'
            }

    def _get__position_text(self):
        return self._position_text_dict.get(self.position_type_, "")

    _shown_help_text = Str

    _data_sources_wrappers = Property(depends_on='data_sources')

    def _get__data_sources_wrappers(self):
         return [
            ArrayColumnWrapper(name=name, 
                shape=repr(self.data_sources[name].shape))
                    for name in self._data_sources_names
                ]
            

    # A traits pointing to the object, to play well with traitsUI
    _self = Instance(DataSourceWizard)

    _suitable_traits_view = Property(depends_on="data_type_")

    def _get__suitable_traits_view(self):
        return "_%s_data_view" % self.data_type_

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
        # XXX punt on this right now
        return True
        if self.data_type == 'A surface':
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

    _coordinates_group = \
                        HGroup(
                           Item('position_x', label='x',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('position_y', label='y',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('position_z', label='z',
                               editor=EnumEditor(name='_data_sources_names')), 
                       )


    _position_group = \
                    Group(
                       Item('position_type'),
                       Item('_position_text', style='readonly'),
                       Group(_coordinates_group,
                           enabled_when='not position_type_=="image data"',
                       ),
                       label='Position of the data points',
                       show_border=True,
                       show_labels=False,
                   ),


    _connectivity_group = \
                   Group(
                       HGroup(
                         Item('_connectivity_text', style='readonly'),
                         spring,
                         Item('connectivity_triangles',
                                editor=EnumEditor(name='_data_sources_names'),
                                show_label=False,
                                ),
                         show_labels=False,
                       ),
                       label='Connectivity information',
                       show_border=True,
                       show_labels=False,
                       enabled_when='position_type_=="explicit"',
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
                   )


    _optional_scalar_data_group = \
                   Group(
                       HGroup(
                       Item('_optional_scalar_data_text', style='readonly'),
                       'has_scalar_data',
                       show_labels=False,
                       ),
                       Item('_scalar_data_text', style='readonly', 
                            enabled_when='has_scalar_data',
                           show_label=False),
                       HGroup(
                           spring, 
                           Item('scalar_data', 
                               editor=EnumEditor(name='_data_sources_names'),
                               enabled_when='has_scalar_data'),
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
                            Item('has_vector_data', show_label=False),
                        ),
                       HGroup(
                           Item('vector_u', label='u',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_v', label='v',
                               editor=EnumEditor(name='_data_sources_names')), 
                           Item('vector_w', label='w',
                               editor=EnumEditor(name='_data_sources_names')), 
                           enabled_when='has_vector_data',
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
                    show_border=True,
                ),
            )

    _point_data_view = \
                View(Group(
                   Group(_coordinates_group,
                        label='Position of the data points',
                        show_border=True,
                   ),
                   HGroup(
                       Item('_lines_text', style='readonly'), 
                       'lines',
                       label='Lines',
                       show_labels=False,
                       show_border=True,
                   ),
                   _optional_scalar_data_group,
                   _optional_vector_data_group,
                   # XXX: hack to have more vertical space
                   Label('\n'),
                   Label('\n'),
                   Label('\n'),
                ))


    _surface_data_view = \
                View(Group(
                   _position_group,
                   _connectivity_group,
                   _optional_scalar_data_group,
                   _optional_vector_data_group,
                ))


    _vector_data_view = \
                View(Group(
                   _vector_data_group,
                   _position_group,
                   _optional_scalar_data_group,
                ))


    _volumetric_data_view = \
                View(Group(
                   _scalar_data_group,
                   _position_group,
                ))


    _wizard_view = View(
            HGroup(
                Item('_self', style='custom', show_label=False,
                     editor=InstanceEditor(view='_array_view'),
                     width=0.17,
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
                show_labels=False,
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
        # FIXME: Workaround for traits bug in enabled_when
        self.position_type_
        self.data_type_
        self._suitable_traits_view
        self._is_ok
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
    wizard.init_arrays()
    wizard.guess_array_names()
    wizard.view_wizard()

