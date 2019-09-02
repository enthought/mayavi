from tvtk.api import tvtk
from .tools import gcf


class SliderWidget:

    slider_rep = tvtk.SliderRepresentation2D()
    slider_widget = tvtk.SliderWidget()

    def __init__(self):
        self.value = Values()
        self.title = Title()
        self.slider = Slider()
        self.label = Label()
        self.cap = Cap()
        self.tube = Tube()
        self.position = Position()
        self.slider_setup()

    def edit_slider_rep(self):
        self.slider_rep.edit_traits()

    def get_value(self):
        return self.slider_widget._get_representation().value

    def position(self, point1=(0.8, 0.9, 0), point2=(1, 0.9, 0)):
        self.slider_rep._get_point1_coordinate().coordinate_system = "normalized_display"
        self.slider_rep._get_point2_coordinate().coordinate_system = "normalized_display"

    def _slider_setup(self, figure):
        self.slider_widget.set(interactor=figure().scene.interactor)
        self.slider_widget.set(representation=self.slider_rep)
        self.slider_widget.animation_mode = "animate"
        self.slider_widget.enabled = 1

    def callback(self, callback):
        self.slider_widget.add_observer("InteractionEvent", callback)


class Values(SliderWidget):
        def __init__(self):
            self.minimum_value(0)
            self.maximum_value(1)
            self.value(0.1)

        def minimum_value(self, min_val):
            SliderWidget.slider_rep.minimum_value = min_val

        def maximum_value(self, max_val):
            SliderWidget.slider_rep.maximum_value = max_val

        def value(self,value):
            SliderWidget.slider_rep.value = value

        def edit(self):
            self.slider_rep.edit_traits()\


class Title(SliderWidget):
    def __init__(self):
        self.color((1,1,1))
        self.title_text("Slider")
        SliderWidget.slider_rep._get_title_property().shadow = 0

    def color(self, color):
        SliderWidget.slider_rep._get_title_property().color = color

    def title_text(self, text):
        SliderWidget.slider_rep.title_text = text

    def edit(self):
        SliderWidget.slider_rep._get_title_property().edit_traits()


class Slider(SliderWidget):
    def __init__(self):
        self.color((0.3,0.2,0.9))
        self.selected_color((1,0,0))

    def color(self, color):
        SliderWidget.slider_rep._get_slider_property().color = color

    def selected_color(self, color):
        SliderWidget.slider_rep._get_selected_property().color = color

    def edit(self):
        SliderWidget.slider_rep._get_slider_property().edit_traits()

    def selected_edit(self):
        SliderWidget.slider_rep._get_selected_property().edit_traits()


class Label(SliderWidget):
    def __init__(self):
        self.color((1,1,1))
        self.opacity(1)
        SliderWidget.slider_rep._get_label_property().shadow = 0

    def color(self,color):
        SliderWidget.slider_rep._get_label_property().color = color

    def opacity(self, opacity):
        SliderWidget.slider_rep._get_label_property().opacity = opacity

    def edit(self):
        SliderWidget.slider_rep._get_label_property().edit_traits()


class Cab(SliderWidget):
    def __init__(self):
        self.color((1,1,1))
        self.opacity(0)

    def color(self, color):
        SliderWidget.slider_rep._get_cap_property().color = color

    def opacity(self, opacity);
        SliderWidget.slider_rep._get_cap_property().opacity = opacity

    def edit(self):
        SliderWidget.slider_rep._get_cap_property().edit_traits()


class Tube(SliderWidget):
    def __init__(self):
        self.color((0,0,0))
        self.opacity(1)

    def color(self, color):
        SliderWidget.slider_rep._get_tube_property().color = color

    def opacity(self, color):
        SliderWidget.slider_rep._get_tube_property().opacity = opacity

    def edit(self):
        SliderWidget.slider_rep._get_tube_property().edit_traits()


class Position(SliderWidget):
    def __init__(self):
        self.position((0.8, 0.9, 0))
        self.position2((1, 0.9, 0))
        SliderWidget.slider_rep._get_point1_coordinate().coordinate_system = "normalized_display"
        SliderWidget.slider_rep._get_point2_coordinate().coordinate_system = "normalized_display"

    def position(self, pos):
        SliderWidget.slider_rep._get_point1_coordinate().value = pos

    def position2(self, pos):
        SliderWidget.slider_rep._get_point2_coordinate().value = pos


def empty_call(event, observer):
    pass

def slider_widget(figure=gcf, callback=empty_call):
    slider = SliderWidget()
    slider._slider_setup(figure)
    slider.callback(callback)
    return slider
