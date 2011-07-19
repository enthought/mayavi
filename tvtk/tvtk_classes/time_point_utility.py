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

from tvtk.tvtk_classes.object import Object


class TimePointUtility(Object):
    """
    TimePointUtility - performs common time operations
    
    Superclass: Object
    
    TimePointUtility is provides methods to perform common time
    operations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTimePointUtility, obj, update, **traits)
    
    def get_date(self, *args):
        """
        V.get_date(int, int, int, int)
        C++: static void GetDate(TypeUInt64 time, int &year,
            int &month, int &day)
        Retrieve the year, month, and day of a time point. Everything but
        the first argument are output parameters.
        """
        ret = self._wrap_call(self._vtk_obj.GetDate, *args)
        return ret

    def get_date_time(self, *args):
        """
        V.get_date_time(int, int, int, int, int, int, int, int)
        C++: static void GetDateTime(TypeUInt64 time, int &year,
            int &month, int &day, int &hour, int &minute, int &second,
            int &millis)
        Retrieve the date and time of a time point. Everything but the
        first argument are output parameters.
        """
        ret = self._wrap_call(self._vtk_obj.GetDateTime, *args)
        return ret

    def get_day(self, *args):
        """
        V.get_day(int) -> int
        C++: static int GetDay(TypeUInt64 time)
        Retrieve the day of the month from a time point.
        """
        ret = self._wrap_call(self._vtk_obj.GetDay, *args)
        return ret

    def get_hour(self, *args):
        """
        V.get_hour(int) -> int
        C++: static int GetHour(TypeUInt64 time)
        Retrieve the hour of the day from the time point.
        """
        ret = self._wrap_call(self._vtk_obj.GetHour, *args)
        return ret

    def get_millisecond(self, *args):
        """
        V.get_millisecond(int) -> int
        C++: static int GetMillisecond(TypeUInt64 time)
        Retrieve the milliseconds from the start of the last second.
        """
        ret = self._wrap_call(self._vtk_obj.GetMillisecond, *args)
        return ret

    def get_minute(self, *args):
        """
        V.get_minute(int) -> int
        C++: static int GetMinute(TypeUInt64 time)
        Retrieve the number of minutes from the start of the last hour.
        """
        ret = self._wrap_call(self._vtk_obj.GetMinute, *args)
        return ret

    def get_month(self, *args):
        """
        V.get_month(int) -> int
        C++: static int GetMonth(TypeUInt64 time)
        Retrieve the month from a time point.
        """
        ret = self._wrap_call(self._vtk_obj.GetMonth, *args)
        return ret

    def get_second(self, *args):
        """
        V.get_second(int) -> int
        C++: static int GetSecond(TypeUInt64 time)
        Retrieve the number of seconds from the start of the last minute.
        """
        ret = self._wrap_call(self._vtk_obj.GetSecond, *args)
        return ret

    def get_time(self, *args):
        """
        V.get_time(int, int, int, int, int)
        C++: static void GetTime(TypeUInt64 time, int &hour,
            int &minute, int &second, int &millis)
        Retrieve the hour, minute, second, and milliseconds of a time
        point. Everything but the first argument are output parameters.
        """
        ret = self._wrap_call(self._vtk_obj.GetTime, *args)
        return ret

    def get_year(self, *args):
        """
        V.get_year(int) -> int
        C++: static int GetYear(TypeUInt64 time)
        Retrieve the year from a time point.
        """
        ret = self._wrap_call(self._vtk_obj.GetYear, *args)
        return ret

    def date_time_to_time_point(self, *args):
        """
        V.date_time_to_time_point(int, int, int, int, int, int, int) -> int
        C++: static TypeUInt64 DateTimeToTimePoint(int year, int month,
             int day, int hour, int minute, int sec, int millis=0)
        Return the time point for a date and time.
        """
        ret = self._wrap_call(self._vtk_obj.DateTimeToTimePoint, *args)
        return ret

    def date_to_time_point(self, *args):
        """
        V.date_to_time_point(int, int, int) -> int
        C++: static TypeUInt64 DateToTimePoint(int year, int month,
            int day)
        Return the time point for 12:00am on a specified day.
        """
        ret = self._wrap_call(self._vtk_obj.DateToTimePoint, *args)
        return ret

    def time_point_to_iso8601(self, *args):
        """
        V.time_point_to_iso8601(int, int) -> string
        C++: static const char *TimePointToISO8601(TypeUInt64,
            int format=ISO8601_DATETIME_MILLIS)
        Converts a VTK timepoint into one of the following ISO8601
        formats.  The default format is ISO8601_DATETIME_MILLIS.
        
        <PRE> Type                      Format / Example 0
        ISO8601_DATETIME_MILLIS [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[SSS]
                                  2006-_01-_02t03:_04:_05._678 1
        ISO8601_DATETIME        [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss]
                                  2006-_01-_02t03:_04:_05 2 ISO8601_DATE     
              [YYYY]-[MM]-[DD]
                                  2006-01-02 3 ISO8601_TIME_MILLIS    
        [hh]:[mm]:[ss].[SSS]
                                  03:04:05.678 4 ISO8601_TIME           
        [hh]:[mm]:[ss]
                                  03:04:05 </PRE>
        """
        ret = self._wrap_call(self._vtk_obj.TimePointToISO8601, *args)
        return ret

    def time_to_time_point(self, *args):
        """
        V.time_to_time_point(int, int, int, int) -> int
        C++: static TypeUInt64 TimeToTimePoint(int hour, int minute,
            int second, int millis=0)
        Return the time point for a time of day (the number of
        milliseconds from 12:00am. The hour should be from 0-23.
        """
        ret = self._wrap_call(self._vtk_obj.TimeToTimePoint, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TimePointUtility, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TimePointUtility properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TimePointUtility properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TimePointUtility properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

