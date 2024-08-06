from tvtk.api import tvtk
from .tools import gcf
from mayavi.sources.widget_source import WidgetSource
from traits.api import RGBColor, Str, on_trait_change, Array, Float, Int, File, Bool
from traitsui.api import ArrayEditor
from traitsui.api import Group, View, Item


class SliderWidget(WidgetSource):

    title_color = RGBColor
    title_text = Str
    minimum_value = Float
    maximum_value = Float
    position_1 = Array(dtype="float64", shape=(3, ), editor=ArrayEditor(),
                       desc="x, y, z coordinates of the bottom left point")
    position_2 = Array(dtype="float64", shape=(3, ), editor=ArrayEditor(),
                       desc="x, y, z coordinates of the top right point")

    slider_color = RGBColor
    slider_color_2 = RGBColor(desc="color of the slider when it's picked")

    cap_color = RGBColor
    cap_opacity = Float

    tube_color = RGBColor
    tube_opacity = Float

    label_color = RGBColor

    slider_rep = tvtk.SliderRepresentation2D()
    slider_widget = tvtk.SliderWidget()
    title = slider_rep._get_title_property()
    label = slider_rep._get_label_property()
    slider = slider_rep._get_slider_property()
    cap = slider_rep._get_cap_property()
    tube = slider_rep._get_tube_property()
    point1 = slider_rep._get_point1_coordinate()
    point2 = slider_rep._get_point2_coordinate()

    traits_view = View(Group(Item(name="title_color"),
                             Item(name="title_text"),
                             Item(name="position_1"),
                             Item(name="position_2"),
                             Item(name="minimum_value"),
                             Item(name="maximum_value"),
                             Item(name="slider_color"),
                             Item(name="slider_color_2"),
                             Item(name="cap_color"),
                             Item(name="cap_opacity"),
                             Item(name="tube_color"),
                             Item(name="tube_opacity"),
                             Item(name="label_color"),
                             label="Properties")
                       )

    def get_value(self):
        return self.slider_widget._get_representation().value

    @on_trait_change('position+')
    def _position_config(self):
        self.point1.value = self.position_1
        self.point2.value = self.position_2

    @on_trait_change("minimum_value, maximum_value")
    def _value_config(self):
        self.slider_rep.minimum_value = self.minimum_value
        self.slider_rep.maximum_value = self.maximum_value

    @on_trait_change('title+')
    def _title_config(self):
        color = self.title_color
        self.title.color = (color if color is not "white" else (1, 1, 1))
        self.slider_rep.title_text = self.title_text
        self.title.shadow = 0

    @on_trait_change('slider+')
    def _slider_config(self):
        color = self.slider_color_2
        self.slider.color = self.slider_color
        self.slider_rep._get_selected_property().color = \
            (color if color is not "white" else (1, 1, 1))

    @on_trait_change("cap+")
    def cap_setup(self):
        self.cap.color = self.cap_color
        self.cap.opacity = self.cap_opacity

    @on_trait_change("tube+")
    def tube_setup(self):
        self.tube.color = self.tube_color
        self.tube.opacity = self.tube_opacity

    @on_trait_change("label+")
    def label_setup(self):
        self.label.color = self.label_color

    def _widget_setup(self, figure):
        self.slider_widget.set(interactor=figure().scene.interactor)
        self.slider_widget.set(representation=self.slider_rep)
        self.slider_widget.animation_mode = "animate"
        self.slider_widget.enabled = 1
        self.default_slider()

    def default_slider(self):
        self.title_text = "Slider"
        self.title_color = (0, 0, 0)
        self.point1.coordinate_system = "normalized_display"
        self.point2.coordinate_system = "normalized_display"
        self.position_1 = (0.8, 0.9, 0)
        self.position_2 = (1, 0.9, 0)
        self.minimum_value = 0
        self.maximum_value = 1
        self.slider_rep.value = self.minimum_value
        self.slider_color = (0.3, 0.2, 0.9)
        self.slider_color_2 = (1, 0, 0)
        self.cap_color = (0, 0, 0)
        self.cap_opacity = 0
        self.tube_color = (0, 0, 0)
        self.tube_opacity = 1
        self.label_color = (1, 1, 1)
        self.label.shadow = 0

    def add_callback(self, callback):
        self.slider_widget.add_observer("InteractionEvent", callback)

    def _update(self):
        if self.scene is None:
            return
        self.widgets = [self.slider_widget]

    def _visible_changed(self, value):
        if value:
            if not self._actors_added:
                self.scene.add_widgets(self.widgets)
                self._actors_added = True
        super(SliderWidget, self)._visible_changed(value)


class ButtonWidget(WidgetSource):

    button_rep = tvtk.TexturedButtonRepresentation2D()
    button_widget = tvtk.ButtonWidget()
    text_image = tvtk.ImageData()

    file_location = File(exists=True)
    position = Array(dtype="float64", shape=(6,), editor=ArrayEditor(),
                     desc="position as xmin, xmax, ymin, ymax, zmin, zmax")

    add_image = Bool
    text_color = RGBColor
    text = Str
    text_font_size = Int

    box_group = Group(
        Item(name="add_image"),
        Item(name="position")
                     )

    text_group = Group(
        Item(name="text"),
        Item(name="text_color"),
        Item(name="text_font_size"),
        enabled_when="add_image is False"
                      )

    image_group = Group(
        Item(name="file_location"),
        enabled_when="add_image is True"
                       )

    default_view = View(
        Group(
            box_group,
            text_group,
            image_group
             )
                        )

    @on_trait_change("add_image")
    def image_conifg(self):
        if self.add_image == 1 and self.file_location is not "":
            self.image()
        if self.add_image == 0:
            self.add_text()

    @on_trait_change("file_location")
    def image(self):
        d = {'bmp': tvtk.BMPReader(),
             'jpg': tvtk.JPEGReader(),
             'png': tvtk.PNGReader(),
             'pnm': tvtk.PNMReader(),
             'dcm': tvtk.DICOMImageReader(),
             'tiff': tvtk.TIFFReader(),
             'ximg': tvtk.GESignaReader(),
             'dem': tvtk.DEMReader(),
             'mha': tvtk.MetaImageReader(),
             'mhd': tvtk.MetaImageReader(),
             }
        reader = d[self.file_location[-3:]]
        reader.set(file_name=self.file_location)
        reader.update()
        image = tvtk.ImageData()
        image = reader._get_output()
        self.button_rep.set_button_texture(0, image)

    @on_trait_change("text+")
    def add_text(self):
        free_type = tvtk.FreeTypeStringToImage()
        text_property = tvtk.TextProperty()
        color = self.text_color
        text_property.color = (color if color is not "white" else (1, 1, 1))
        text_property.font_size = self.text_font_size
        text_image = tvtk.ImageData()
        free_type.render_string(text_property, self.text, 0, text_image)
        self.button_rep.set_button_texture(0, text_image)

    @on_trait_change("position")
    def place_widget(self):
        self.button_rep.place_widget(self.position)

    def _widget_setup(self, figure):
        self.button_widget.set(interactor=figure().scene.interactor)
        self.button_widget.set(representation=self.button_rep)
        self.button_widget.enabled = 1
        self.default_button()

    def default_button(self):
        self.button_rep.set_number_of_states(1)
        self.text = "Button"
        self.text_color = (1, 1, 0)
        self.text_font_size = 25
        self.position = (-70, 70, -70, 70, 0, 0)

    def add_callback(self, callback):
        self.button_widget.add_observer("StateChangedEvent", callback)

    def _update(self):
        if self.scene is None:
            return
        self.widgets = [self.button_widget]

    def _visible_changed(self, value):
        if value:
            if not self._actors_added:
                self.scene.add_widgets(self.widgets)
                self._actors_added = True
        super(ButtonWidget, self)._visible_changed(value)

    def remove_actors(self):
        """Removes `self.widgets` from the scene.
        """
        if self._actors_added:
            self.scene.remove_widgets(self.widgets)
            self._actors_added = False
            self.button_rep.set_button_texture(0, self.text_image)
            self.scene.render()


def slider_widget(figure=None):
    if figure is None:
        figure = gcf
    slider = SliderWidget()
    slider._widget_setup(figure)
    return slider


def button_widget(figure=None):
    if figure is None:
        figure = gcf
    button = ButtonWidget()
    button._widget_setup(figure)
    return button
