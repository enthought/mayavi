""" Abstracts the Gradient editors provided for Qt and wxPython so these
can be used from TraitsUI.


Author: Prabhu Ramachandran
Copyright (c) 2012-2020  Enthought Inc., Mumbai, India.
"""

from traits.etsconfig.api import ETSConfig
from traitsui.api import CustomEditor
from tvtk.api import tvtk

##########################################################################
# Traits UI factory functions.
##########################################################################
def gradient_editor_factory(parent, trait_editor):
    """This is a factory function for `traitsui.CustomEditor` and allows us to
    use the `wxGradientEditorWidget` or `QGradientEditorWidget` as a traits
    UI editor.
    """
    tvtk_obj = getattr(trait_editor.object, trait_editor.name)
    if ETSConfig.toolkit == 'wx':
        from .wx_gradient_editor import wxGradientEditorWidget
        widget = wxGradientEditorWidget(parent, tvtk_obj)
    elif ETSConfig.toolkit == 'qt4':
        from .qt_gradient_editor import QGradientEditorWidget
        widget = QGradientEditorWidget(None, tvtk_obj)
    else:
        msg = 'Toolkit %s does not implement gradient_editors.'%ETSConfig.toolkit
        raise NotImplementedError(msg)
    return widget


##########################################################################
# Editor for VolumeProperty
##########################################################################
VolumePropertyEditor = CustomEditor(gradient_editor_factory)

##########################################################################
# Test case related code.
##########################################################################
def make_test_table(lut=False):
    from .ctf import ColorTransferFunction, PiecewiseFunction
    if lut:
        table = tvtk.LookupTable()
        table.table_range = (255, 355)
        return table, None, None
    else:
        table = tvtk.VolumeProperty()
        ctf = ColorTransferFunction()
        mins, maxs = 255, 355
        ds = (maxs-mins)/4.0
        try:
            ctf.range = (mins, maxs)
        except Exception:
            # VTK versions < 5.2 don't seem to need this.
            pass
        ctf.add_rgb_point(mins,      0.00, 0.0, 1.00)
        ctf.add_rgb_point(mins+ds,   0.25, 0.5, 0.75)
        ctf.add_rgb_point(mins+2*ds, 0.50, 1.0, 0.50)
        ctf.add_rgb_point(mins+3*ds, 0.75, 0.5, 0.25)
        ctf.add_rgb_point(maxs,      1.00, 0.0, 0.00)
        otf = PiecewiseFunction()
        otf.add_point(255, 0.0)
        otf.add_point(355, 0.2)
        table.set_color(ctf)
        table.set_scalar_opacity(otf)
        return table, ctf, otf

def test_trait_ui():
    from traits.api import HasTraits, Instance, Button
    from traitsui.api import View, Item, Group

    class Test(HasTraits):
        p = Instance(tvtk.VolumeProperty, ())
        b = Button('Click me')

        view = View(Group(
                        Item(name='p', style='custom',
                            resizable=True,
                            editor=VolumePropertyEditor),
                        Item('b'),
                        show_labels=False),
                    resizable=True
                    )

    table, otf, ctf = make_test_table(False)
    t = Test(p=table)
    # We need to hang on to these so these don't go out of scope.
    t.otf = otf
    t.ctf = ctf
    return t


if __name__ == '__main__':
    t = test_trait_ui()
    t.configure_traits()
