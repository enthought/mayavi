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


class FastNumericConversion(Object):
    """
    FastNumericConversion - Enables fast conversion of floating point
    to fixed point
    
    Superclass: Object
    
    FastNumericConversion uses a portable (assuming IEEE format)
    method for converting single and double precision floating point
    values to a fixed point representation. This allows fast integer
    floor operations on platforms, such as Intel X86, in which CPU
    floating point conversion algorithms are very slow. It is based on
    the techniques described in Chris Hecker's article, "Let's Get to the
    (Floating) Point", in Game Developer Magazine, Feb/Mar 1996, and the
    techniques described in Michael Herf's website,
    http://www.stereopsis.com/FPU.html.  The Hecker article can be found
    at http://www.d6.com/users/checker/pdfs/gdmfp.pdf.  Unfortunately,
    each of these techniques is incomplete, and doesn't convert properly,
    in a way that depends on how many bits are reserved for fixed point
    fractional use, due to failing to properly account for the default
    round-towards-even rounding mode of the X86. Thus, my implementation
    incorporates some rounding correction that undoes the rounding that
    the FPU performs during denormalization of the floating point value.
    Note that the rounding affect I'm talking about here is not the
    effect on the fistp instruction, but rather the effect that occurs
    during the denormalization of a value that occurs when adding it to a
    much larger value. The bits must be shifted to the right, and when a
    "1" bit falls off the edge, the rounding mode determines what happens
    next, in order to avoid completely "losing" the 1-bit. Furthermore,
    my implementation works on Linux, where the default precision mode is
    64-bit extended precision.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFastNumericConversion, obj, update, **traits)
    
    def convert_fixed_point(self, *args):
        """
        V.convert_fixed_point(float, int) -> int
        C++: int ConvertFixedPoint(const double &val, int &fracPart)
        Convert the value to a fixed point representation, returning the
        integer portion as function value, and returning the fractional
        part in the second parameter.
        """
        ret = self._wrap_call(self._vtk_obj.ConvertFixedPoint, *args)
        return ret

    def performance_tests(self):
        """
        V.performance_tests()
        C++: void PerformanceTests(void)
        Conduct timing tests so that the usefulness of this class can be
        ascertained on whatever platform it is being used. Output can be
        retrieved via Print method.
        """
        ret = self._vtk_obj.PerformanceTests()
        return ret
        

    def quick_floor(self, *args):
        """
        V.quick_floor(float) -> int
        C++: static int QuickFloor(const double &val)
        Perform a quick flooring of the double-precision floating point
        value. The result is sometimes incorrect, but in a way that makes
        it acceptable for most uses. The naive way to implement floor(),
        given that the x86 FPU does round() by default, is to define
        floor(x) as round(x-.5).  This would work fine except for the
        fact that the x86 FPU breaks rounding ties by selecting the even
        number. Thus, floor(4.0) = round(3.5) = 4, but floor(3.0) =
        round(2.5) = 2. As a result, subtracting .5 gives the wrong
        answer for odd integers. So, let's subtract just a TEENSY bit
        less than .5, to swing the odd-integer results up to their corect
        value. How teensy? Well, if it's too teensy, it will be
        insignificant compared to 0.5, and will become equivalent to 0.5.
         And if it's not teensy enough, we'll overshoot, causing results
        like floor(N-epsilon)==N, for some epsilon. Furthermore, the "too
        teensy" problem is exacerbated when trying to floor larger
        numbers, due to limitations of the representation's dynamic
        range. See the definition of rounding_tie_breaker() for details.
        """
        ret = self._wrap_call(self._vtk_obj.QuickFloor, *args)
        return ret

    def round(self, *args):
        """
        V.round(float) -> int
        C++: static int Round(const double &val)
        Round to nearest int.  This is pretty sweet in the default
        round-to-nearest FPU mode, since it is generally immaterial how
        ties are broken when rounding. I.e., either "2" or "3" are
        acceptable results for "Round(2.5)", but only one of them (the
        one naively not chosen without jumping through the hoops in
        quick_floor and safe_floor) is the acceptable result for the
        analogous "Floor(3)". Therefore, we don't need to worry at all
        about adding a teensy but not too teensy tie breaker, or shifting
        off a half-integer bit. This makes it exceptionally fast.
        """
        ret = self._wrap_call(self._vtk_obj.Round, *args)
        return ret

    def rounding_tie_breaker(self):
        """
        V.rounding_tie_breaker() -> float
        C++: static double RoundingTieBreaker()
        Small amount to use as a rounding tie-breaker to prevent
        round-to-nearest-and-even mode from flooring-down odd numbered
        integers. But number to nudge by depends on number of bits
        mantissa in our floating point representation minus number of
        mantissa bits in the range of signed ints we need to handle. In
        order to ensure that flooring-down doesn't happen even for very
        large odd-integer values, the number of bits used to represent
        the tie-breaker (i.e. to the right of the binary-point), plus the
        number of bits needed to represent the integer (to the left of
        the binary point), can not exceeds the number of bits in the
        current precision mode. Thus, in selecting the tie-breaker value,
        we select the largest number of bits to the right of the binary
        point as possible while still maintaining that inequality. Thus,
        extended precision mode allows a larger number of bits to the
        right of the binary point.  This, in turn, implies a smaller
        value of the tie-breaker. And a smaller tie-breaker will impose a
        tighter window on the range of values that are erroneously
        rounded-up by a floor operation. Under double precision, a
        quick_floor of 0.9999998 (six 9's and an 8) correctly yields
        0. A value must be very close to 1.0, in fact, at least as close
           as 0.9999999 (seven 9's)in order for the tie-breaker to bump
           it up to 1. Under extended precision, an even smaller
           tie-breaker can be used. In this mode, a quick_floor of
           0.9999999999 (ten 9's) correctly yields 0. A quick_floor of
           0.99999999999 (eleven 9's) gets rounded up to 1. Since these
           spurious round-ups occur only when the given value is
           virtually indistinguishable from the next higher integer, the
           results should be acceptable in most situations where
           performance is of the essence. Make this public so that
           clients can account for the rounding_tie_breaker if necessary
           Compute (0.5 ^ (EXT_BITS-INT_BITS)) as a compile-time const ...
         [Truncated]
        """
        ret = self._vtk_obj.RoundingTieBreaker()
        return ret
        

    def safe_floor(self, *args):
        """
        V.safe_floor(float) -> int
        C++: static int SafeFloor(const double &val)
        Perform a SAFE flooring. Similar to quick_floor, but modified to
        return the correct result always. Use this when it absolutely
        positively needs to be the correct answer all the time, and
        considering 0.9999999 as being equal to 1.0 is simply not
        acceptable.  It works similarly to quick_floor, but it retains one
        extra bit of fixed point precision in the conversion process, so
        that the problem with quick_floor affects only an unneeded bit,
        and then it ditches that bit from the resulting integer with a
        right-shift. In other words, it rounds to the nearest one-half,
        choosing the EVEN one-half (i.e. the integer) as a tie-breaker,
        and then shifting off that half-integer bit. As a result of
        maintaining one extra bit of fixed point precision in the
        intermediate calculation, the range of integers supported is
        reduced by one bit. Plus, it takes a little longer to execute,
        due to the final bit shift.
        """
        ret = self._wrap_call(self._vtk_obj.SafeFloor, *args)
        return ret

    def set_reserved_frac_bits(self, *args):
        """
        V.set_reserved_frac_bits(int)
        C++: void SetReservedFracBits(int bits)
        Set the number of bits reserved for fractional precision that are
        maintained as part of the flooring process. This number affects
        the flooring arithmetic. It may be useful if the factional part
        is to be used to index into a lookup table of some sort. However,
        if you are only interested in knowing the fractional remainder
        after flooring, there doesn't appear to be any advantage to using
        these bits, either in terms of a lookup table, or by directly
        multiplying by some unit fraction, over simply subtracting the
        floored value from the original value. Note that since only 32
        bits are used for the entire fixed point representation,
        increasing the number of reserved fractional bits reduces the
        range of integer values that can be floored to.
        """
        ret = self._wrap_call(self._vtk_obj.SetReservedFracBits, *args)
        return ret

    def test_convert_fixed_point_frac_part(self, *args):
        """
        V.test_convert_fixed_point_frac_part(float) -> int
        C++: int TestConvertFixedPointFracPart(double val)
        Wrappable method for script-testing of correct cross-platform
        functionality
        """
        ret = self._wrap_call(self._vtk_obj.TestConvertFixedPointFracPart, *args)
        return ret

    def test_convert_fixed_point_int_part(self, *args):
        """
        V.test_convert_fixed_point_int_part(float) -> int
        C++: int TestConvertFixedPointIntPart(double val)
        Wrappable method for script-testing of correct cross-platform
        functionality
        """
        ret = self._wrap_call(self._vtk_obj.TestConvertFixedPointIntPart, *args)
        return ret

    def test_quick_floor(self, *args):
        """
        V.test_quick_floor(float) -> int
        C++: int TestQuickFloor(double val)
        Wrappable method for script-testing of correct cross-platform
        functionality
        """
        ret = self._wrap_call(self._vtk_obj.TestQuickFloor, *args)
        return ret

    def test_round(self, *args):
        """
        V.test_round(float) -> int
        C++: int TestRound(double val)
        Wrappable method for script-testing of correct cross-platform
        functionality
        """
        ret = self._wrap_call(self._vtk_obj.TestRound, *args)
        return ret

    def test_safe_floor(self, *args):
        """
        V.test_safe_floor(float) -> int
        C++: int TestSafeFloor(double val)
        Wrappable method for script-testing of correct cross-platform
        functionality
        """
        ret = self._wrap_call(self._vtk_obj.TestSafeFloor, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FastNumericConversion, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FastNumericConversion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit FastNumericConversion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FastNumericConversion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

