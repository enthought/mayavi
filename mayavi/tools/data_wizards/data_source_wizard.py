
from numpy import ones, resize, linspace, atleast_3d

from traits.api import Property, Str, Button, Trait, \
    Any, Instance, HasStrictTraits, false, Dict, HasTraits, \
    CArray, Bool
from traitsui.api import EnumEditor, View, Item, HGroup, \
    VGroup, spring, Group, TextEditor, HTMLEditor, InstanceEditor, \
    TabularEditor, TitleEditor, Label, ArrayEditor, ImageEditor

from traitsui.tabular_adapter import TabularAdapter
from traitsui.image.image import ImageLibrary

from pyface.api import ImageResource

from .data_source_factory import DataSourceFactory
from .preview_window import PreviewWindow
from mayavi.modules.api import Surface, Glyph
from mayavi.filters.api import ExtractEdges


############################################################################
# The DataSourceWizard class
############################################################################
class DataSourceWizard(HasTraits):

    data_sources = Dict

    _data_sources_names = Property(depends_on='data_sources')

    def _get__data_sources_names(self):
        names = []
        for name in self.data_sources:
            try:
                self.data_sources[name] + 1
                names.append(name)
            except TypeError:
                pass
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
                      'Implicitely positioned on a regular grid':
                        'image data',
                      'On an orthogonal grid with varying spacing':
                        'orthogonal grid',
                        })

    # The array that is used for finding out the shape of the grid,
    # when creating an ImageData
    grid_shape_source = Property(depends_on='grid_shape_source_')

    def _get_grid_shape_source(self):
        if self.grid_shape_source_ == '':
            # catter for improperly initialized view
            keys = self._data_sources_names
            if not self.grid_shape.any():
                self.grid_shape = \
                        self.data_sources[keys[0]].shape
            return keys[0]
        elif self.grid_shape_source_[:16] == 'Shape of array: ':
            return self.grid_shape_source_[17:-1]
        else:
            return ""

    # Shadow traits for grid_shape_source
    grid_shape_source_ = Str

    def _grid_shape_source_changed(self):
        if not self.grid_shape_source == '':
            array_shape = \
                    atleast_3d(self.data_sources[self.grid_shape_source]).shape
            grid_shape = ones((3, ))
            grid_shape[:len(array_shape)] = array_shape
            self.grid_shape = grid_shape

    _grid_shape_source_labels = Property(depends_on='_data_sources_names')

    def _get__grid_shape_source_labels(self):
        values = ['Shape of array: "%s"' % name
                    for name in  self._data_sources_names]
        values.sort
        values.append('Specified explicitly')
        return values

    # The shape of the grid array. Used when position is implicit
    grid_shape = CArray(shape=(3,), dtype='i')

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

    vector_w = Str

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

    def guess_arrays(self):
        """ Do some guess work on the arrays to find sensible default.
        """
        array_names = set(self._data_sources_names)
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
        factory = DataSourceFactory()
        # Keep a reference to the factory to be able to replay it, say
        # on other data.
        self._factory = factory
        if self.data_type_ == 'point':
            # The user wants to explicitly position vector,
            # thus only sensible data structures for points is with
            # explicit positioning.
            self.position_type_ == 'explicit'
            # In addition, this view does not allow for
            # connectivity.
            factory.unstructured = True
            factory.connected = False
        else:
            factory.connected = True

        if (self.position_type_ == "image data"
                and not self.data_type_ == "point"):
            if not self.has_scalar_data and not self.vector_u == '':
                # With image data we need a scalar array always:
                factory.scalar_data = ones(self.grid_shape)
            factory.position_implicit = True
        else:
            factory.position_x = self.get_sdata(self.position_x)
            factory.position_y = self.get_sdata(self.position_y)
            factory.position_z = self.get_sdata(self.position_z)
        if self.position_type_ == "orthogonal grid":
            factory.orthogonal_grid = True
        if self.position_type_ == "explicit" and self.data_type_ == "surface":
            factory.connectivity_triangles = self.get_data(
                                                self.connectivity_triangles)
        if self.lines and self.data_type_ == "point":
            factory.lines = True

        if self.has_vector_data or self.data_type_ == 'vector':
            # In the vector view, the user is not explicitly asked to
            # Enable vectors.
            factory.has_vector_data = True
            factory.vector_u = self.get_sdata(self.vector_u)
            factory.vector_v = self.get_sdata(self.vector_v)
            factory.vector_w = self.get_sdata(self.vector_w)

        if self.has_scalar_data or self.data_type_ == 'volumetric':
            # In the volumetric view, the user is not explicitly asked to
            # Enable scalars.
            factory.scalar_data = self.get_sdata(self.scalar_data)

        if self.connectivity_triangles == '':
            factory.connectivity_triangles = None

        self.data_source = factory.build_data_source()

        if self.has_scalar_data:
            if hasattr(self.data_source, 'scalar_name'):
                self.data_source.scalar_name = self.scalar_data
            elif hasattr(self.data_source, 'point_scalar_name'):
                self.data_source.point_scalar_name = self.scalars

    #----------------------------------------------------------------------
    # Private interface
    #----------------------------------------------------------------------
    def get_data(self, name):
        return self.data_sources[name]

    def get_sdata(self, name):
        ary = self.data_sources[name]
        if not self.data_type_ == 'point':
            ary = resize(ary, self.grid_shape)
        return ary

    def active_arrays(self):
        """ Return the list of the active array-selection drop-downs.
        """
        arrays = []
        if self.data_type_ == 'point' or self.position_type_ == 'explicit':
            arrays.extend(
                    ['position_x', 'position_y', 'position_z', ])
        if self.data_type_ == 'vector' or self.has_vector_data:
            arrays.extend(['vector_u', 'vector_v', 'vector_w'])
        if self.has_scalar_data or self.data_type_ == 'volumetric':
            arrays.extend(['scalar_data'])
        return arrays

    def check_arrays(self):
        """ Checks that all the array have the right size.
        """
        arrays_to_check = self.active_arrays()
        if len(arrays_to_check) == 0:
            return True
        size = self.get_data(getattr(self, arrays_to_check.pop())).size
        for attr in arrays_to_check:
            if not self.get_data(getattr(self, attr)).size == size:
                return False
        if (self.data_type_ == 'surface'
                and self.position_type_ == "explicit"):
            if not self.connectivity_triangles.size / 3 == size:
                return False
        return True


###########################################################################
# class ArrayColumnWrapper
###########################################################################
class ArrayColumnWrapper(HasStrictTraits):

    name = Str
    shape = Str


############################################################################
# class ArrayColumnAdapter
############################################################################
class ArrayColumnAdapter(TabularAdapter):

    columns = [('name',  'name'),
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

    _info_text = Str('Array size do not match')

    _array_label = Str('Available arrays')

    _data_type_text = Str("What does your data represents?")

    _lines_text = Str("Connect the points with lines")

    _scalar_data_text = Str("Array giving the value of the scalars")

    _optional_scalar_data_text = Str("Associate scalars with the data points")

    _connectivity_text = Str("Array giving the triangles")

    _vector_data_text = Str("Associate vector components")

    _position_text = Property(depends_on="position_type_")

    _position_text_dict = {'explicit':
                'Coordinnates of the data points:',
                           'orthogonal grid':
                'Position of the layers along each axis:',
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

    _preview_button = Button(label='Preview structure')

    def __preview_button_fired(self):
        if self.ui:
            self.build_data_source()
            self.preview()

    _ok_button = Button(label='OK')

    def __ok_button_fired(self):
        if self.ui:
            self.ui.dispose()
            self.build_data_source()

    _cancel_button = Button(label='Cancel')

    def __cancel_button_fired(self):
        if self.ui:
            self.ui.dispose()

    _is_ok = Bool

    _is_not_ok = Bool

    def _anytrait_changed(self):
        """ Validates if the OK button is enabled.
        """
        if self.ui:
            self._is_ok = self.check_arrays()
            self._is_not_ok = not self._is_ok

    _preview_window = Instance(PreviewWindow, ())

    _info_image = Instance(ImageResource,
                    ImageLibrary.image_resource('@std:alert16',))

    #----------------------------------------------------------------------
    # TraitsUI views
    #----------------------------------------------------------------------
    _coordinates_group = \
                        HGroup(
                           Item('position_x', label='x',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('position_y', label='y',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('position_z', label='z',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                       )

    _position_group = \
                    Group(
                       Item('position_type'),
                       Group(
                           Item('_position_text', style='readonly',
                                    resizable=False,
                                    show_label=False),
                           _coordinates_group,
                           visible_when='not position_type_=="image data"',
                       ),
                       Group(
                           Item('grid_shape_source_',
                            label='Grid shape',
                            editor=EnumEditor(
                                name='_grid_shape_source_labels',
                                        invalid='_is_not_ok')),
                           HGroup(
                            spring,
                            Item('grid_shape', style='custom',
                                    editor=ArrayEditor(width=-60),
                                    show_label=False),
                           enabled_when='grid_shape_source==""',
                            ),
                           visible_when='position_type_=="image data"',
                       ),
                       label='Position of the data points',
                       show_border=True,
                       show_labels=False,
                   ),

    _connectivity_group = \
                   Group(
                       HGroup(
                         Item('_connectivity_text', style='readonly',
                                resizable=False),
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
                           resizable=False,
                           show_label=False),
                       HGroup(
                           spring,
                           Item('scalar_data',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           show_labels=False,
                           ),
                       label='Scalar value',
                       show_border=True,
                       show_labels=False,
                   )

    _optional_scalar_data_group = \
                   Group(
                       HGroup(
                       'has_scalar_data',
                       Item('_optional_scalar_data_text',
                            resizable=False,
                            style='readonly'),
                       show_labels=False,
                       ),
                       Item('_scalar_data_text', style='readonly',
                            resizable=False,
                            enabled_when='has_scalar_data',
                           show_label=False),
                       HGroup(
                           spring,
                           Item('scalar_data',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok'),
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
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('vector_v', label='v',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('vector_w', label='w',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                       ),
                       label='Vector data',
                       show_border=True,
                   ),

    _optional_vector_data_group = \
                   VGroup(
                        HGroup(
                            Item('has_vector_data', show_label=False),
                            Item('_vector_data_text', style='readonly',
                                resizable=False,
                                show_label=False),
                        ),
                       HGroup(
                           Item('vector_u', label='u',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('vector_v', label='v',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
                           Item('vector_w', label='w',
                               editor=EnumEditor(name='_data_sources_names',
                                        invalid='_is_not_ok')),
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
                          adapter=ArrayColumnAdapter(),
                      ),
                    ),
                    show_border=True,
                    show_labels=False
                ))

    _questions_view = View(
                Item('_top_label', editor=TitleEditor(),
                        show_label=False),
                HGroup(
                    Item('_data_type_text', style='readonly',
                                resizable=False),
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
                        # FIXME: Giving up on context sensitive help
                        # because of lack of time.
                        #Group(
                        #    Item('_shown_help_text', editor=HTMLEditor(),
                        #        width=300,
                        #        label='Help',
                        #        ),
                        #    show_labels=False,
                        #    label='Help',
                        #),
                        #Group(
                            Item('_preview_button',
                                    enabled_when='_is_ok'),
                            Item('_preview_window', style='custom',
                                    label='Preview structure'),
                            show_labels=False,
                            #label='Preview structure',
                        #),
                        #layout='tabbed',
                        #dock='tab',
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
                       'lines',
                       Item('_lines_text', style='readonly',
                                        resizable=False),
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
                   _optional_vector_data_group,
                ))

    _wizard_view = View(
          Group(
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
            HGroup(
                Item('_info_image', editor=ImageEditor(),
                    visible_when="_is_not_ok"),
                Item('_info_text', style='readonly', resizable=False,
                    visible_when="_is_not_ok"),
                spring,
                '_cancel_button',
                Item('_ok_button', enabled_when='_is_ok'),
                show_labels=False,
            ),
          ),
        title='Import arrays',
        resizable=True,
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
        self.grid_shape_source
        self._is_ok
        self.ui = self.edit_traits(view='_wizard_view')

    def preview(self):
        """ Display a preview of the data structure in the preview
            window.
        """
        self._preview_window.clear()
        self._preview_window.add_source(self.data_source)
        data = lambda name: self.data_sources[name]
        g = Glyph()
        g.glyph.glyph_source.glyph_source = \
                    g.glyph.glyph_source.glyph_list[0]
        g.glyph.scale_mode = 'data_scaling_off'
        if not (self.has_vector_data or self.data_type_ == 'vector'):
            g.glyph.glyph_source.glyph_source.glyph_type = 'cross'
            g.actor.property.representation = 'points'
            g.actor.property.point_size = 3.
        self._preview_window.add_module(g)
        if not self.data_type_ in ('point', 'vector') or self.lines:
            s = Surface()
            s.actor.property.opacity = 0.3
            self._preview_window.add_module(s)
        if not self.data_type_ == 'point':
            self._preview_window.add_filter(ExtractEdges())
            s = Surface()
            s.actor.property.opacity = 0.2
            self._preview_window.add_module(s)


if __name__ == '__main__':
    from numpy import mgrid

    x, y, z = mgrid[-5:5, -5:5, -5:5]
    r = x ** 2 + y ** 2 + z ** 2
    X = linspace(0, 8)

    data_sources = {
            'x': X,
            'y': y,
            'z': z,
            'r': r
        }

    wizard = DataSourceWizardView(data_sources=data_sources)
    wizard.init_arrays()
    wizard.guess_arrays()
    wizard.view_wizard()
