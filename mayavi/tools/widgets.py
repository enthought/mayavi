from tvtk.api import tvtk
from .tools import gcf


class SliderWidget:

    slider_rep = tvtk.SliderRepresentation2D()
    slider_widget = tvtk.SliderWidget()
    title = slider_rep._get_title_property()
    label = slider_rep._get_label_property()
    slider = slider_rep._get_slider_property()
    cap = slider_rep._get_cap_property()
    tube  = slider_rep._get_tube_property()
    point1 = slider_rep._get_point1_coordinate()
    point2 = slider_rep._get_point2_coordinate()

    def __init__(self):
        self.value_setup(0, 1)
        self.title_setup("Slider", (0,0,0))
        self.slider_setup((0.3,0.2,0.9), (1,0,0))
        self.label_setup((1,1,1))
        self.cap_setup((0,0,0), 0)
        self.tube_setup((0,0,0), 1)
        self.position_setup((0.8,0.9,0), (1,0.9,0))

    def return_value(self):
        return self.slider_widget._get_representation().value

    def position_setup(self, point1, point2):
        self.point1.coordinate_system = "normalized_display"
        self.point1.value = point1
        self.point2.coordinate_system = "normalized_display"
        self.point2.value = point2

    def value_setup(self, min_val, max_val):
        self.slider_rep.minimum_value = min_val
        self.slider_rep.maximum_value = max_val
        self.slider_rep.value = min_val

    def title_setup(self, title_text, color):
        self.slider_rep.title_text = title_text
        self.title.color = color
        self.title.shadow = 0

    def slider_setup(self, color1, color2):
        self.slider.color = color1
        self.slider_rep._get_selected_property().color = color2

    def cap_setup(self, color, opacity):
        self.cap.color = color
        self.cap.opacity = opacity

    def tube_setup(self, color, opacity):
        self.tube.color = color
        self.tube.opacity = opacity

    def label_setup(self, color):
        self.label.color = color
        self.label.shadow = 0

    def _widget_setup(self, figure):
        self.slider_widget.set(interactor=figure().scene.interactor)
        self.slider_widget.set(representation=self.slider_rep)
        self.slider_widget.animation_mode = "animate"
        self.slider_widget.enabled = 1

    def callback(self, callback):
        self.slider_widget.add_observer("InteractionEvent", callback)


class ButtonWidget:

    button_rep = tvtk.TexturedButtonRepresentation2D()
    button_widget = tvtk.ButtonWidget()

    def __init__(self):
        self.button_rep.set_number_of_states(1)
        self.add_text("Button", (1,1,0), 25)
        self.place_widget((-70,70,-70,70,0,0))

    def add_image(self, location):
        reader = tvtk.JPEGReader()
        if location[-3:] == "png":
            reader = tvtk.PNGReader()
        reader.set(file_name = location)
        reader.update()
        image = tvtk.ImageData()
        image = reader._get_output()
        self.button_rep.set_button_texture(0, image)


    def add_text(self, text, color, font_size):
        free_type = tvtk.FreeTypeStringToImage()
        text_property = tvtk.TextProperty()
        text_property.color = color
        text_property.font_size = font_size
        text_image = tvtk.ImageData()
        free_type.render_string(text_property, text, 0, text_image)
        self.button_rep.set_button_texture(0, text_image)

    def place_widget(self, a):
        self.button_rep.place_widget(a)

    def _widget_setup(self, figure):
        self.button_widget.set(interactor=figure().scene.interactor)
        self.button_widget.set(representation=self.button_rep)
        self.button_widget.enabled = 1

    def callback(self, callback):
        self.button_widget.add_observer("StateChangedEvent", callback)


def slider_widget(figure=gcf):
    slider = SliderWidget()
    slider._widget_setup(figure)
    return slider

def button_widget(figure=gcf):
    button = ButtonWidget()
    button._widget_setup(figure)
    return button
