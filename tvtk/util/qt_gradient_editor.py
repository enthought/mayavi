""" A Qt based color gradient editor for vtkLookupTables and
color transfer functions.

This code is distributed under the conditions of the BSD license.

Based on a wxPython by Pete Schmitt <schmitt@colorado.edu>

Author: Prabhu Ramachandran <prabhu@enthought.com>
Copyright (c) 2012-2020 Enthought, Inc., Mumbai, India.
"""

import sys

# Enthought library imports
from pyface.qt import QtCore, QtGui

# Local imports
from tvtk.util.gradient_editor import (
    ColorControlPoint, ChannelBase, FunctionControl, GradientEditorWidget
)


##########################################################################
# `QGradientControl` class.
##########################################################################
class QGradientControl(QtGui.QWidget):
    """Widget which displays the gradient represented by an GradientTable
    object (and does nothing beyond that)"""
    def __init__(self, parent=None, gradient_table=None, width=100, height=100):
        """master: panel in which to place the control. GradientTable is the
        Table to which to attach."""
        super(QGradientControl, self).__init__(parent=parent)
        self.resize(width, height)
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent, True)

        self.width = width
        self.height = height
        self.gradient_table = gradient_table
        assert gradient_table.size == width
        self.setMinimumSize(100, 50)
        # currently only able to use gradient tables in the same size as the
        # canvas width

    def paintEvent(self, event):
        """Paint handler."""
        super(QGradientControl, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0) )
        painter.setBrush(brush)
        painter.setBackgroundMode(QtCore.Qt.OpaqueMode)
        sz = self.size()
        width, height = sz.width(), sz.height()

        xform = self.gradient_table.scaling_function
        start_y = 0
        end_y = height
        if xform:
            # if a scaling transformation is provided, paint the original
            # gradient under the scaled gradient.
            start_y = height/2

        # paint the original gradient as it stands in the table.
        color = QtGui.QColor()
        for x in range(width):
            (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(float(x)/(width-1))
            color.setRgb(int(255*r), int(255*g), int(255*b))
            painter.setPen(color)
            brush.setColor(color)
            painter.drawLine(x, start_y, x, end_y)
        if xform:
            # paint the scaled gradient below
            end_y = start_y
            start_y = 0
            for x in range(width):
                f = float(x)/(width-1)
                (r,g,b,a) = self.gradient_table.get_pos_rgba_color_lerped(xform(f))
                color.set(int(255*r), int(255*g), int(255*b))
                brush.setColor(color)
                painter.drawLine(x, start_y, x, end_y)


##########################################################################
# `Channel` class.
##########################################################################
class Channel(ChannelBase):
    def paint(self, painter):
        """Paint current channel into Canvas (a canvas of a function control
        object).

        Contents of the canvas are not deleted prior to painting,
        so more than one channel can be painted into the same canvas.
        """

        table = self.control.table
        # only control points which are active for the current channel
        # are to be painted. filter them out.
        relevant_control_points = [
            x for x in table.control_points if self.name in x.active_channels
        ]
        # lines between control points
        color = QtGui.QColor(*self.rgb_color)
        painter.setPen(color)
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        painter.setBackgroundMode(QtCore.Qt.OpaqueMode)
        for k in range( len(relevant_control_points) - 1 ):
            cur_point = relevant_control_points[k]
            next_point = relevant_control_points[1+k]

            painter.drawLine(self.get_pos_index(cur_point.pos),
                             self.get_value_index(cur_point.color),
                             self.get_pos_index(next_point.pos),
                             self.get_value_index(next_point.color))

        # control points themself.
        color = QtCore.Qt.black
        painter.setPen(color)
        for control_point in relevant_control_points:
            x = self.get_pos_index( control_point.pos )
            y = self.get_value_index( control_point.color )
            radius=6
            #print(x,y)
            painter.drawRect(x-(radius/2.0), y-(radius/2.0), radius, radius)
            painter.drawRect(100,80,6,6)


##########################################################################
# `QFunctionControl` class.
##########################################################################
class QFunctionControl(QtGui.QWidget, FunctionControl):
    """Widget which displays a rectangular regions on which hue, sat, val
    or rgb values can be modified. An function control can have one or more
    attached color channels."""

    # Radius around a control point center in which we'd still count a
    # click as "clicked the control point"
    control_pt_click_tolerance = 4

    ChannelFactory = Channel

    def __init__(self, master=None, gradient_table=None, color_space=None,
                 width=100, height=100):
        """Initialize a function control widget on tkframe master.

        Parameters:
        -----------

        master: The master widget.  Note that this widget *must* have
             the methods specified in the `AbstractGradientEditorWidget`
             interface.

        on_table_changed: Callback function taking a bool argument of meaning
            'FinalUpdate'. FinalUpdate is true if a control point is dropped,
            created or removed and false if the update is due to a control point
            currently beeing dragged (but not yet dropped)

        color_space: String which specifies the channels painted on this control.
             May be any combination of h,s,v,r,g,b,a in which each channel
             occurs only once.

        set_status_text: a callback used to set the status text
             when using the editor.
        """
        kw = dict(
            master=master, gradient_table=gradient_table,
            color_space=color_space, width=width,
            height=height
        )
        super().__init__(**kw)
        self.resize(width, height)
        self.setMinimumSize(100, 50)

    ######################################################################
    # Qt event handlers.
    ######################################################################
    def paintEvent(self, event):
        super(QFunctionControl, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        painter.setBrush(brush)
        width, height = self.size().width(), self.size().height()
        painter.drawRect(0, 0, width, height)
        for channel in self.channels:
            channel.paint(painter)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.cur_drag = self.find_control_point(event.x(), event.y())
        super(QFunctionControl, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.cur_drag:
                self.table_config_changed( final_update = True )
                self.cur_drag = None
        elif event.button() == QtCore.Qt.RightButton:
            # toggle control point. check if there is a control point
            # under the mouse. If yes, delete it, if not, create one
            # at that point.
            cur_control_point = self.find_control_point(event.x(), None)
            if cur_control_point:
                # found a marker at the click position. delete it and return,
                # unless it is a fixed marker (at pos 0 or 1)..
                if ( cur_control_point[1].fixed ):
                    # in this case do nothing. Fixed markers cannot be deleted.
                    return
                self.table.control_points.remove(cur_control_point[1])
                self.table_config_changed(final_update=True)
            else:
                # since there was no marker to remove at the point, we assume
                # that we should place one there
                new_control_point = ColorControlPoint(active_channels=self.active_channels_string)
                new_control_point.set_pos(self.channels[0].get_index_pos(event.x()))

                # set new control point color to the color currently present
                # at its designated position
                new_control_point.color = self.table.get_pos_color(new_control_point.pos)

                self.table.insert_control_point(new_control_point)
                self.table_config_changed(final_update = True)

        if isinstance(event, QtGui.QMouseEvent):
            super(QFunctionControl, self).mouseReleaseEvent(event)

    def leaveEvent(self, event):
        if self.cur_drag:
            self.table_config_changed( final_update = True )
            self.cur_drag = None
        super(QFunctionControl, self).leaveEvent(event)

    def resizeEvent(self, event):
        sz = self.size()
        self.width = sz.width()
        self.height = sz.height()

    def mouseMoveEvent(self, event):
        # currently dragging a control point?
        channel = None
        point = None
        if self.cur_drag:
            channel = self.cur_drag[0]
            point = self.cur_drag[1]
            if ( not point.fixed ):
                point.set_pos( channel.get_index_pos(event.x()) )
                point.activate_channels( self.active_channels_string )
                self.table.sort_control_points()
            channel.set_value_index( point.color, event.y() )
            self.table_config_changed( final_update = False )

        screenX = event.x()
        screenY = event.y()
        width, height = self.size().width(), self.size().height()
        master = self.master
        s1, s2 = master.get_table_range()
        if channel is not None:
            name = self.text_map[channel.name]
            pos = s1 + (s2 - s1)*point.pos
            val = channel.get_value(point.color)
            txt = '%s: (%.3f, %.3f)'%(name, pos, val)
        else:
            x = s1 + (s2 - s1)*float(screenX)/(width-1)
            y = 1.0 - float(screenY)/(height-1)
            txt = "position: (%.3f, %.3f)"%(x, y)

        self.master.set_status_text(txt)

##########################################################################
# `QGradientEditorWidget` class.
##########################################################################
class QGradientEditorWidget(QtGui.QWidget, GradientEditorWidget):
    """A Gradient Editor widget that can be used anywhere.
    """
    def __init__(self, master, vtk_table, on_change_color_table=None,
                 colors=None):
        """

        Parameters:
        -----------

        vtk_table : the `tvtk.LookupTable` or `tvtk.VolumeProperty` object
                    to set.

        on_change_color_table : A callback called when the color table
                                changes.

        colors : list of 'rgb', 'hsv', 'h', 's', 'v', 'a'
                 (Default : ['rgb', 'hsv', 'a'])

                 'rgb' creates one panel to edit Red, Green and Blue
                 colors.

                 'hsv' creates one panel to edit Hue, Saturation and
                 Value.

                 'h', 's', 'v', 'r', 'g', 'b', 'a' separately
                 specified creates different panels for each.
        """
        kw = dict(master=master, vtk_table=vtk_table,
                    on_change_color_table=on_change_color_table,
                    colors=colors)
        super().__init__(**kw)

        gradient_preview_width = self.gradient_preview_width
        gradient_preview_height = self.gradient_preview_height
        channel_function_width = self.channel_function_width
        channel_function_height = self.channel_function_height

        # set up all the panels in a grid
        # 6x2 size:  6 rows, 2 columns...
        grid = QtGui.QGridLayout()
        grid.setColumnStretch(0, 0)
        grid.setColumnStretch(1, 1)

        # "Gradient Viewer" panel, in position (0,1) for sizer
        self.gradient_control = QGradientControl(self,
                                                 self.gradient_table,
                                                 gradient_preview_width,
                                                 gradient_preview_height)
        self.setToolTip('Right click for menu')
        grid.addWidget(QtGui.QLabel("", self), 0, 0)
        grid.addWidget(self.gradient_control, 0, 1)

        # Setup the context menu to fire for the Gradient control alone.
        gc = self.gradient_control
        gc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        gc.customContextMenuRequested.connect(self.contextMenuEventOnGradient)

        # Add the function controls:
        function_controls = self.function_controls
        editor_data = self.editor_data

        row = 1
        for color in self.colors:
            data = editor_data[color]
            control = QFunctionControl(self, self.gradient_table, color,
                                       channel_function_width,
                                       channel_function_height)
            txt = data[0] + self.tooltip_text
            control.setToolTip(txt)
            # Add name of editor (to left side of editor)
            grid.addWidget(QtGui.QLabel(data[1], self), row, 0)
            # Add the "RGB" control point editor
            grid.addWidget(control, row, 1)
            function_controls.append(control)
            row += 1

        # The status text.
        self.text = QtGui.QLabel('status', self)
        grid.addWidget(self.text, row, 0, 1, 2)

        self.setLayout(grid)
        self.show()

    ######################################################################
    # `GradientEditorWidget` interface.
    ######################################################################
    def set_status_text(self, msg):
        self.text.setText(msg)

    ######################################################################
    # Qt event methods.
    ######################################################################
    def contextMenuEventOnGradient(self, pos):
        menu = QtGui.QMenu(self)
        saveAction = menu.addAction("Save as")
        loadAction = menu.addAction("Load")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == saveAction:
            self.on_save()
        elif action == loadAction:
            self.on_load()

    def on_save(self, event=None):
        """
        Open "Save" dialog, write lookuptable to 3 files: ``*.lut``
        (lookuptable) ``*.grad`` (gradient table for use with this program),
        and ``*.jpg`` (image of the gradient)
        """
        wildcard = "Gradient Files (*.grad);;All Files (*.*)"
        filename, filter = QtGui.QFileDialog.getSaveFileName(self,
                                                "Save LUT to...",
                                                '',
                                                wildcard)
        if filename:
            self.save(filename)

    def on_load(self, event=None):
        """
        Load a ``*.grad`` lookuptable file.
        """
        wildcard = "Gradient Files (*.grad);;All Files (*.*)"
        filename, filter = QtGui.QFileDialog.getOpenFileName(self,
                                                "Open gradient file...",
                                                '',
                                                wildcard)
        if filename:
            self.load(filename)


##########################################################################
# `QGradientEditor` class.
##########################################################################
class QGradientEditor(QtGui.QMainWindow):
    """ QMainWindow that displays the gradient editor window,
    i.e. the thing that contains the gradient display, the function
    controls and the buttons.
    """
    def __init__(self, vtk_table, on_change_color_table=None, colors=None):
        """Initialize the gradient editor window.

        Parameters
        ----------
        vtk_table: Instance of vtkLookupTable, designating the table which is
            to be edited.
        on_change_color_table: Callback function taking no arguments. Called
            when the color table was changed and rendering is
            requested.
        """
        super(QGradientEditor, self).__init__()
        self.setWindowTitle("Color Gradient Editor")
        self.widget = QGradientEditorWidget(
            master=self, vtk_table=vtk_table,
            on_change_color_table=on_change_color_table,
            colors=colors
        )

        self.setCentralWidget(self.widget)
        self.resize(300, 500)

        self.statusBar()
        ## Set up the MenuBar
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        file_action = QtGui.QAction("&Save", self)
        file_action.setStatusTip("Save CTF")
        file_action.triggered.connect(self.widget.on_save)
        file_menu.addAction(file_action)

        load_action = QtGui.QAction("&Load", self)
        load_action.setStatusTip("Load CTF")
        load_action.triggered.connect(self.widget.on_load)
        file_menu.addAction(load_action)

        quit_action = QtGui.QAction("&Quit", self)
        quit_action.setStatusTip("Quit application")
        quit_action.triggered.connect(QtGui.QApplication.instance().quit)
        file_menu.addAction(quit_action)

        help_menu = menu.addMenu("&Help")
        action = QtGui.QAction("&Help", self)
        action.setStatusTip("Help")
        action.triggered.connect(self.on_help)
        help_menu.addAction(action)
        action = QtGui.QAction("&About", self)
        action.setStatusTip("About application")
        action.triggered.connect(self.on_about)
        help_menu.addAction(action)


    def on_help(self, event=None):
        """ Help defining the mouse interactions """
        message = "Right click to add control points.  Left click to move control points"
        QtGui.QMessageBox.information(self, 'Help', message)

    def on_about(self, event=None):
        """ Who wrote the program?"""
        message = 'tk Gradient Editor for MayaVi1: Gerald Knizia (cgk.d@gmx.net)\n'\
                  'wxPython port: Pete Schmitt (schmitt@colorado.edu)\n'\
                  'Qt port: Prabhu Ramachandran\n'\
                  'Enhanced for Mayavi2: Prabhu Ramachandran'
        QtGui.QMessageBox.information(self, 'About gradient editor', message)


def main():
    from tvtk.util.traitsui_gradient_editor import make_test_table
    import sys
    table, ctf, otf = make_test_table(lut=False)
    # the actual gradient editor code.
    def on_color_table_changed():
        """If we had a vtk window running, update it here"""
        # print("Update Render Window")
        pass

    app = QtGui.QApplication.instance()
    editor = QGradientEditor(table,
                             on_color_table_changed,
                             colors=['rgb', 'a', 'h', 's', 'v'],
    )
    editor.setWindowTitle("Gradient editor")
    editor.show()
    sys.exit(app.exec_())


##########################################################################
# Test application.
##########################################################################
if __name__ == "__main__":
    main()
