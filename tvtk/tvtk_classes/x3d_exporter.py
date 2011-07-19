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

from tvtk.tvtk_classes.exporter import Exporter


class X3DExporter(Exporter):
    """
    X3DExporter - create an x3d file
    
    Superclass: Exporter
    
    X3DExporter is a render window exporter which writes out the
    renderered scene into an x3d file. x3d is an XML-based format for
    representation 3d scenes (similar to VRML). Check out
    http://www.web3d.org/x3d/ for more details.
    
    Thanks:
    
    x3d_exporter is contributed by Christophe Mouton at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkX3DExporter, obj, update, **traits)
    
    binary = tvtk_base.false_bool_trait(help=\
        """
        Turn on binary mode
        """
    )
    def _binary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinary,
                        self.binary_)

    fastest = tvtk_base.false_bool_trait(help=\
        """
        In binary mode use fastest instead of best compression
        """
    )
    def _fastest_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFastest,
                        self.fastest_)

    speed = traits.Float(4.0, enter_set=True, auto_set=False, help=\
        """
        Specify the Speed of navigation. Default is 4.
        """
    )
    def _speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpeed,
                        self.speed)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the output file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_binary_max_value(self):
        return self._vtk_obj.GetBinaryMaxValue()
    binary_max_value = traits.Property(_get_binary_max_value, help=\
        """
        Turn on binary mode
        """
    )

    def _get_binary_min_value(self):
        return self._vtk_obj.GetBinaryMinValue()
    binary_min_value = traits.Property(_get_binary_min_value, help=\
        """
        Turn on binary mode
        """
    )

    def _get_fastest_max_value(self):
        return self._vtk_obj.GetFastestMaxValue()
    fastest_max_value = traits.Property(_get_fastest_max_value, help=\
        """
        In binary mode use fastest instead of best compression
        """
    )

    def _get_fastest_min_value(self):
        return self._vtk_obj.GetFastestMinValue()
    fastest_min_value = traits.Property(_get_fastest_min_value, help=\
        """
        In binary mode use fastest instead of best compression
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('fastest', 'GetFastest'), ('binary',
    'GetBinary'), ('reference_count', 'GetReferenceCount'), ('file_name',
    'GetFileName'), ('speed', 'GetSpeed'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['binary', 'debug', 'fastest', 'global_warning_display', 'file_name',
    'speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(X3DExporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['binary', 'fastest'], [], ['file_name', 'speed']),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

