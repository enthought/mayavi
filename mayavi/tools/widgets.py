from tvtk.api import tvtk
from .tools import gcf


class SliderWidget():
    def __init__(self):
        self.slider_rep = tvtk.SliderRepresentation2D()
        self.slider_widget = tvtk.SliderWidget()
        self.slider()
        self.title()
        self.set_values()
        self.cap()
        self.tube()
        self.position()

    def edit_slider_rep(self):
        self.slider_rep.edit_traits()

    def set_values(self, min_value=0, max_value=1, value=0.1):
        self.slider_rep.set(minimum_value=min_value)
        self.slider_rep.set(maximum_value=max_value)
        self.slider_rep.set(value=value)

    def return_value(self):
        return self.slider_widget._get_representation().value

    def edit_title(self):
        self.slider_rep._get_title_property().edit_traits()

    def title(self, title_text="Slider", color=(1, 1, 1)):
        self.slider_rep.set(title_text=title_text)
        self.slider_rep._get_title_property().set(color=color)

    def edit_slider(self):
        self.slider_rep._get_slider_property().edit_traits()

    def edit_slider_select(self):
        self.slider_rep._get_selected_property().edit_traits()

    def slider(self, color=(0.3, 0.2, 0.9), selected_color=(1, 0, 0), opacity=1):
        self.slider_rep._get_slider_property().set(color=color)
        self.slider_rep._get_selected_property().set(color=selected_color)
        self.slider_rep._get_selected_property().set(opacity=opacity)

    def edit_label(self):
        self.slider_rep._get_label_property().edit_traits()

    def label(self, label=(1, 1, 1), opacity=1):
        self.slider_rep._get_label_property().set(color=label)
        self.slider_rep._get_label_property().opacity = opacity

    def edit_cap(self):
        self.slider_rep._get_cap_property().edit_traits()

    def cap(self, color=(1, 1, 1), opacity=0):
        self.slider_rep._get_cap_property().set(color=color)
        self.slider_rep._get_cap_property().opacity = opacity

    def edit_tube(self):
        self.slider_rep._get_tube_property().edit_traits()

    def tube(self, color=(0, 0, 0), opacity=1):
        self.slider_rep._get_tube_property().set(color=color)
        self.slider_rep._get_tube_property().opacity = opacity

    def position(self, point1=(0.8, 0.9, 0), point2=(1, 0.9, 0)):
        self.slider_rep._get_point1_coordinate().coordinate_system = "normalized_display"
        self.slider_rep._get_point1_coordinate().set(value=point1)
        self.slider_rep._get_point2_coordinate().coordinate_system = "normalized_display"
        self.slider_rep._get_point2_coordinate().set(value=point2)

    def _slider_setup(self, figure):
        self.slider_widget.set(interactor=figure().scene.interactor)
        self.slider_widget.set(representation=self.slider_rep)
        self.slider_rep._get_title_property().shadow = 0
        self.slider_rep._get_label_property().shadow = 0
        self.slider_widget.animation_mode = "animate"
        self.slider_widget.enabled = 1

    def callback(self, callback):
        self.slider_widget.add_observer("InteractionEvent", callback)


def empty_call(event, observer):
    pass


def slider_widget(figure=gcf, callback=empty_call):
    slider = SliderWidget()
    slider._slider_setup(figure)
    slider.callback(callback)
    return slider
