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


class Math(Object):
    """
    Math - performs common math operations
    
    Superclass: Object
    
    Math provides methods to perform common math operations. These
    include providing constants such as Pi; conversion from degrees to
    radians; vector operations such as dot and cross products and vector
    norm; matrix determinant for 2x2 and 3x3 matrices; univariate
    polynomial solvers; and for random number generation (for backward
    compatibility only).
    
    See Also:
    
    MinimalStandardRandomSequence, BoxMuellerRandomSequence
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMath, obj, update, **traits)
    
    def get_adjusted_scalar_range(self, *args):
        """
        V.get_adjusted_scalar_range(DataArray, int, [float, float]) -> int
        C++: static int GetAdjustedScalarRange(DataArray *array,
            int comp, double range[2])
        Get a DataArray's scalar range for a given component. If the
        DataArray's data type is unsigned char (VTK_UNSIGNED_CHAR) the
        range is adjusted to the whole data type range [0, 255.0]. Same
        goes for unsigned short (VTK_UNSIGNED_SHORT) but the upper bound
        is also adjusted down to 4095.0 if was between ]255, 4095.0].
        Return 1 on success, 0 otherwise.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', ['float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.GetAdjustedScalarRange, *my_args)
        return ret

    def get_scalar_type_fitting_range(self, *args):
        """
        V.get_scalar_type_fitting_range(float, float, float, float) -> int
        C++: static int GetScalarTypeFittingRange(double range_min,
            double range_max, double scale=1.0, double shift=0.0)
        Return the scalar type that is most likely to have enough
        precision to store a given range of data once it has been scaled
        and shifted (i.e. [range_min * scale + shift, range_max * scale +
        shift]. If any one of the parameters is not an integer number
        (decimal part != 0), the search will default to float types only
        (float or double) Return -1 on error or no scalar type found.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarTypeFittingRange, *args)
        return ret

    def _get_seed(self):
        return self._vtk_obj.GetSeed()
    seed = traits.Property(_get_seed, help=\
        """
        Return the current seed used by the random number generator.
        
        DON'T USE Random(), random_seed(), get_seed(), Gaussian() THIS IS
        STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR REGRESSION
        TESTS) THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY. Instead, for
        a sequence of random numbers with a uniform distribution create a
        MinimalStandardRandomSequence object. For a sequence of random
        numbers with a gaussian/normal distribution create a
        BoxMuellerRandomSequence object.
        """
    )

    def add(self, *args):
        """
        V.add((float, float, float), (float, float, float), [float, float,
             float])
        C++: static void Add(const double a[3], const double b[3],
            double c[3])
        Addition of two 3-vectors (double version). Result is stored in
        c.
        """
        ret = self._wrap_call(self._vtk_obj.Add, *args)
        return ret

    def are_bounds_initialized(self, *args):
        """
        V.are_bounds_initialized([float, float, float, float, float, float])
             -> int
        C++: static int AreBoundsInitialized(double bounds[6])
        Are the bounds initialized?
        """
        ret = self._wrap_call(self._vtk_obj.AreBoundsInitialized, *args)
        return ret

    def binomial(self, *args):
        """
        V.binomial(int, int) -> int
        C++: static TypeInt64 Binomial(int m, int n)
        The number of combinations of n objects from a pool of m objects
        (m>n). This is commonly known as "m choose n" and sometimes
        denoted $_m_c_n $ or $\left(\begin{array}{c}m \
        n\end{array}\right) $.
        """
        ret = self._wrap_call(self._vtk_obj.Binomial, *args)
        return ret

    def bounds_is_within_other_bounds(self, *args):
        """
        V.bounds_is_within_other_bounds([float, float, float, float, float,
            float], [float, float, float, float, float, float], [float,
            float, float]) -> int
        C++: static int BoundsIsWithinOtherBounds(double bounds1[6],
            double bounds2[6], double delta[3])
        Return true if first 3d bounds is within the second 3d bounds
        Bounds is x-min, x-max, y-min, y-max, z-min, z-max Delta is the
        error margin along each axis (usually a small number)
        """
        ret = self._wrap_call(self._vtk_obj.BoundsIsWithinOtherBounds, *args)
        return ret

    def ceil(self, *args):
        """
        V.ceil(float) -> int
        C++: static int Ceil(double x)
        Rounds a double to the nearest integer not less than itself. This
        is faster than ceil() but provides undefined output on overflow.
        """
        ret = self._wrap_call(self._vtk_obj.Ceil, *args)
        return ret

    def clamp_and_normalize_value(self, *args):
        """
        V.clamp_and_normalize_value(float, (float, float)) -> float
        C++: static double ClampAndNormalizeValue(double value,
            const double range[2])
        Clamp a value against a range and then normalized it between 0
        and 1. If range[0]==range[1], the result is 0.
        \pre valid_range: range[0]<=range[1]
        \post valid_result: result>=0.0 && result<=1.0
        """
        ret = self._wrap_call(self._vtk_obj.ClampAndNormalizeValue, *args)
        return ret

    def cross(self, *args):
        """
        V.cross((float, float, float), (float, float, float), [float,
            float, float])
        C++: static void Cross(const double x[3], const double y[3],
            double z[3])
        Cross product of two 3-vectors. Result (a x b) is stored in z.
        (double-precision version)
        """
        ret = self._wrap_call(self._vtk_obj.Cross, *args)
        return ret

    def degrees_from_radians(self, *args):
        """
        V.degrees_from_radians(float) -> float
        C++: static double DegreesFromRadians(double radians)
        Convert radians into degrees
        """
        ret = self._wrap_call(self._vtk_obj.DegreesFromRadians, *args)
        return ret

    def degrees_to_radians(self):
        """
        V.degrees_to_radians() -> float
        C++: static float DegreesToRadians()
        @deprecated Replaced by Math::RadiansFromDegrees() as of VTK
        5.4.
        """
        ret = self._vtk_obj.DegreesToRadians()
        return ret
        

    def determinant2x2(self, *args):
        """
        V.determinant2x2(float, float, float, float) -> float
        C++: static double Determinant2x2(double a, double b, double c,
            double d)
        V.determinant2x2((float, float), (float, float)) -> float
        C++: static double Determinant2x2(const double c1[2],
            const double c2[2])
        Calculate the determinant of a 2x2 matrix: | a b | | c d |
        """
        ret = self._wrap_call(self._vtk_obj.Determinant2x2, *args)
        return ret

    def determinant3x3(self, *args):
        """
        V.determinant3x3([[float, float, float], [float, float, float],
            [float, float, float]]) -> float
        C++: static double Determinant3x3(double A[3][3])
        V.determinant3x3((float, float, float), (float, float, float), (
            float, float, float)) -> float
        C++: static double Determinant3x3(const double c1[3],
            const double c2[3], const double c3[3])
        V.determinant3x3(float, float, float, float, float, float, float,
            float, float) -> float
        C++: static double Determinant3x3(double a1, double a2, double a3,
             double b1, double b2, double b3, double c1, double c2,
            double c3)
        Return the determinant of a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.Determinant3x3, *args)
        return ret

    def diagonalize3x3(self, *args):
        """
        V.diagonalize3x3(((float, float, float), (float, float, float), (
            float, float, float)), [float, float, float], [[float, float,
            float], [float, float, float], [float, float, float]])
        C++: static void Diagonalize3x3(const double A[3][3], double w[3],
             double V[3][3])
        Diagonalize a symmetric 3x3 matrix and return the eigenvalues in
        w and the eigenvectors in the columns of V.  The matrix V will
        have a positive determinant, and the three eigenvectors will be
        aligned as closely as possible with the x, y, and z axes.
        """
        ret = self._wrap_call(self._vtk_obj.Diagonalize3x3, *args)
        return ret

    def distance2_between_points(self, *args):
        """
        V.distance2_between_points((float, float, float), (float, float,
            float)) -> float
        C++: static double Distance2BetweenPoints(const double x[3],
            const double y[3])
        Compute distance squared between two points x and y(double
        precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Distance2BetweenPoints, *args)
        return ret

    def dot(self, *args):
        """
        V.dot((float, float, float), (float, float, float)) -> float
        C++: static double Dot(const double x[3], const double y[3])
        Dot product of two 3-vectors (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Dot, *args)
        return ret

    def dot2d(self, *args):
        """
        V.dot2d((float, float), (float, float)) -> float
        C++: static double Dot2D(const double x[2], const double y[2])
        Dot product of two 2-vectors. (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Dot2D, *args)
        return ret

    def double_degrees_to_radians(self):
        """
        V.double_degrees_to_radians() -> float
        C++: static double DoubleDegreesToRadians()
        @deprecated Replaced by Math::RadiansFromDegrees() as of VTK
        5.4.
        """
        ret = self._vtk_obj.DoubleDegreesToRadians()
        return ret
        

    def double_pi(self):
        """
        V.double_pi() -> float
        C++: static double DoublePi()
        A mathematical constant (double-precision version). This version
        is 3.1415926535897932384626.
        """
        ret = self._vtk_obj.DoublePi()
        return ret
        

    def double_radians_to_degrees(self):
        """
        V.double_radians_to_degrees() -> float
        C++: static double DoubleRadiansToDegrees()
        @deprecated Replaced by Math::DegreesFromRadians() as of VTK
        5.4.
        """
        ret = self._vtk_obj.DoubleRadiansToDegrees()
        return ret
        

    def double_two_pi(self):
        """
        V.double_two_pi() -> float
        C++: static double DoubleTwoPi()
        A mathematical constant (double-precision version). This version
        is 6.283185307179586.
        """
        ret = self._vtk_obj.DoubleTwoPi()
        return ret
        

    def extent_is_within_other_extent(self, *args):
        """
        V.extent_is_within_other_extent([int, int, int, int, int, int], [int,
            int, int, int, int, int]) -> int
        C++: static int ExtentIsWithinOtherExtent(int extent1[6],
            int extent2[6])
        Return true if first 3d extent is within second 3d extent Extent
        is x-min, x-max, y-min, y-max, z-min, z-max
        """
        ret = self._wrap_call(self._vtk_obj.ExtentIsWithinOtherExtent, *args)
        return ret

    def factorial(self, *args):
        """
        V.factorial(int) -> int
        C++: static TypeInt64 Factorial(int N)
        Compute N factorial, N! = N*(N-1) * (N-2)...*3*2*1. 0! is taken
        to be 1.
        """
        ret = self._wrap_call(self._vtk_obj.Factorial, *args)
        return ret

    def floor(self, *args):
        """
        V.floor(float) -> int
        C++: static int Floor(double x)
        Rounds a double to the nearest integer not greater than itself.
        This is faster than floor() but provides undefined output on
        overflow.
        """
        ret = self._wrap_call(self._vtk_obj.Floor, *args)
        return ret

    def gaussian(self, *args):
        """
        V.gaussian() -> float
        C++: static double Gaussian()
        V.gaussian(float, float) -> float
        C++: static double Gaussian(double mean, double std)
        Generate pseudo-random numbers distributed according to the
        standard normal distribution.
        
        DON'T USE Random(), random_seed(), get_seed(), Gaussian() THIS IS
        STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR REGRESSION
        TESTS) THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY. Instead, for
        a sequence of random numbers with a uniform distribution create a
        MinimalStandardRandomSequence object. For a sequence of random
        numbers with a gaussian/normal distribution create a
        BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.Gaussian, *args)
        return ret

    def gaussian_amplitude(self, *args):
        """
        V.gaussian_amplitude(float, float) -> float
        C++: static double GaussianAmplitude(const double variance,
            const double distanceFromMean)
        V.gaussian_amplitude(float, float, float) -> float
        C++: static double GaussianAmplitude(const double mean,
            const double variance, const double position)
        Compute the amplitude of a Gaussian function with mean=0 and
        specified variance. That is, 1./(sqrt(2 Pi * variance)) *
        exp(-distance_from_mean^_2/(_2.*variance)).
        """
        ret = self._wrap_call(self._vtk_obj.GaussianAmplitude, *args)
        return ret

    def gaussian_weight(self, *args):
        """
        V.gaussian_weight(float, float) -> float
        C++: static double GaussianWeight(const double variance,
            const double distanceFromMean)
        V.gaussian_weight(float, float, float) -> float
        C++: static double GaussianWeight(const double mean,
            const double variance, const double position)
        Compute the amplitude of an unnormalized Gaussian function with
        mean=0 and specified variance. That is,
        exp(-distance_from_mean^_2/(_2.*variance)). When distance_from_mean =
        0, this function returns 1.
        """
        ret = self._wrap_call(self._vtk_obj.GaussianWeight, *args)
        return ret

    def hsv_to_rgb(self, *args):
        """
        V.hsv_to_rgb((float, float, float)) -> (float, float, float)
        C++: static double *HSVToRGB(const double hsv[3])
        V.hsv_to_rgb(float, float, float) -> (float, float, float)
        C++: static double *HSVToRGB(double h, double s, double v)
        V.hsv_to_rgb((float, float, float), [float, float, float])
        C++: static void HSVToRGB(const double hsv[3], double rgb[3])
        Convert color in HSV format (Hue, Saturation, Value) to RGB
        format (Red, Green, Blue). The input color is not modified.
        """
        ret = self._wrap_call(self._vtk_obj.HSVToRGB, *args)
        return ret

    def identity3x3(self, *args):
        """
        V.identity3x3([[float, float, float], [float, float, float],
            [float, float, float]])
        C++: static void Identity3x3(double A[3][3])
        Set A to the identity matrix.
        """
        ret = self._wrap_call(self._vtk_obj.Identity3x3, *args)
        return ret

    def inf(self):
        """
        V.inf() -> float
        C++: static double Inf()
        Special IEEE-754 number used to represent positive infinity.
        """
        ret = self._vtk_obj.Inf()
        return ret
        

    def invert3x3(self, *args):
        """
        V.invert3x3(((float, float, float), (float, float, float), (float,
             float, float)), [[float, float, float], [float, float,
            float], [float, float, float]])
        C++: static void Invert3x3(const double A[3][3], double AI[3][3])
        Invert a 3x3 matrix. The input matrix is A. The output is stored
        in AI.
        """
        ret = self._wrap_call(self._vtk_obj.Invert3x3, *args)
        return ret

    def is_inf(self, *args):
        """
        V.is_inf(float) -> int
        C++: static int IsInf(double x)
        Test if a number is equal to the special floating point value
        infinity.
        """
        ret = self._wrap_call(self._vtk_obj.IsInf, *args)
        return ret

    def is_nan(self, *args):
        """
        V.is_nan(float) -> int
        C++: static int IsNan(double x)"""
        ret = self._wrap_call(self._vtk_obj.IsNan, *args)
        return ret

    def lu_factor3x3(self, *args):
        """
        V.lu_factor3x3([[float, float, float], [float, float, float],
            [float, float, float]], [int, int, int])
        C++: static void LUFactor3x3(double A[3][3], int index[3])
        LU Factorization of a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.LUFactor3x3, *args)
        return ret

    def lu_solve3x3(self, *args):
        """
        V.lu_solve3x3(((float, float, float), (float, float, float), (
            float, float, float)), (int, int, int), [float, float, float])
        C++: static void LUSolve3x3(const double A[3][3],
            const int index[3], double x[3])
        LU back substitution for a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.LUSolve3x3, *args)
        return ret

    def lab_to_rgb(self, *args):
        """
        V.lab_to_rgb((float, float, float), [float, float, float])
        C++: static void LabToRGB(const double lab[3], double rgb[3])
        Convert color from the CIE-L*ab system to RGB.
        """
        ret = self._wrap_call(self._vtk_obj.LabToRGB, *args)
        return ret

    def lab_to_xyz(self, *args):
        """
        V.lab_to_xyz((float, float, float), [float, float, float])
        C++: static void LabToXYZ(const double lab[3], double xyz[3])
        Convert color from the CIE-L*ab system to CIE XYZ.
        """
        ret = self._wrap_call(self._vtk_obj.LabToXYZ, *args)
        return ret

    def linear_solve3x3(self, *args):
        """
        V.linear_solve3x3(((float, float, float), (float, float, float), (
            float, float, float)), (float, float, float), [float, float,
            float])
        C++: static void LinearSolve3x3(const double A[3][3],
            const double x[3], double y[3])
        Solve Ay = x for y and place the result in y.  The matrix A is
        destroyed in the process.
        """
        ret = self._wrap_call(self._vtk_obj.LinearSolve3x3, *args)
        return ret

    def matrix3x3_to_quaternion(self, *args):
        """
        V.matrix3x3_to_quaternion(((float, float, float), (float, float,
            float), (float, float, float)), [float, float, float, float])
        C++: static void Matrix3x3ToQuaternion(const double A[3][3],
            double quat[4])
        Convert a 3x3 matrix into a quaternion.  This will provide the
        best possible answer even if the matrix is not a pure rotation
        matrix. The method used is that of B.K.P. Horn.
        """
        ret = self._wrap_call(self._vtk_obj.Matrix3x3ToQuaternion, *args)
        return ret

    def multiply3x3(self, *args):
        """
        V.multiply3x3(((float, float, float), (float, float, float), (
            float, float, float)), (float, float, float), [float, float,
            float])
        C++: static void Multiply3x3(const double A[3][3],
            const double in[3], double out[3])
        V.multiply3x3(((float, float, float), (float, float, float), (
            float, float, float)), ((float, float, float), (float, float,
            float), (float, float, float)), [[float, float, float],
            [float, float, float], [float, float, float]])
        C++: static void Multiply3x3(const double A[3][3],
            const double B[3][3], double C[3][3])
        Multiply a vector by a 3x3 matrix.  The result is placed in out.
        """
        ret = self._wrap_call(self._vtk_obj.Multiply3x3, *args)
        return ret

    def multiply_scalar(self, *args):
        """
        V.multiply_scalar([float, float, float], float)
        C++: static void MultiplyScalar(double a[3], double s)
        Multiplies a 3-vector by a scalar (double version). This modifies
        the input 3-vector.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyScalar, *args)
        return ret

    def multiply_scalar2d(self, *args):
        """
        V.multiply_scalar2d([float, float], float)
        C++: static void MultiplyScalar2D(double a[2], double s)
        Multiplies a 2-vector by a scalar (double version). This modifies
        the input 2-vector.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyScalar2D, *args)
        return ret

    def nan(self):
        """
        V.nan() -> float
        C++: static double Nan()
        Special IEEE-754 number used to represent Not-A-Number (Nan).
        """
        ret = self._vtk_obj.Nan()
        return ret
        

    def neg_inf(self):
        """
        V.neg_inf() -> float
        C++: static double NegInf()
        Special IEEE-754 number used to represent negative infinity.
        """
        ret = self._vtk_obj.NegInf()
        return ret
        

    def norm(self, *args):
        """
        V.norm((float, float, float)) -> float
        C++: static double Norm(const double x[3])
        Compute the norm of 3-vector (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Norm, *args)
        return ret

    def norm2d(self, *args):
        """
        V.norm2d((float, float)) -> float
        C++: static double Norm2D(const double x[2])
        Compute the norm of a 2-vector. (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Norm2D, *args)
        return ret

    def normalize(self, *args):
        """
        V.normalize([float, float, float]) -> float
        C++: static double Normalize(double x[3])
        Normalize (in place) a 3-vector. Returns norm of vector
        (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Normalize, *args)
        return ret

    def normalize2d(self, *args):
        """
        V.normalize2d([float, float]) -> float
        C++: static double Normalize2D(double x[2])
        Normalize (in place) a 2-vector. Returns norm of vector.
        (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Normalize2D, *args)
        return ret

    def orthogonalize3x3(self, *args):
        """
        V.orthogonalize3x3(((float, float, float), (float, float, float),
            (float, float, float)), [[float, float, float], [float, float,
             float], [float, float, float]])
        C++: static void Orthogonalize3x3(const double A[3][3],
            double B[3][3])
        Orthogonalize a 3x3 matrix and put the result in B.  If matrix A
        has a negative determinant, then B will be a rotation plus a flip
        i.e. it will have a determinant of -1.
        """
        ret = self._wrap_call(self._vtk_obj.Orthogonalize3x3, *args)
        return ret

    def outer(self, *args):
        """
        V.outer((float, float, float), (float, float, float), [[float,
            float, float], [float, float, float], [float, float, float]])
        C++: static void Outer(const double x[3], const double y[3],
            double A[3][3])
        Outer product of two 3-vectors (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Outer, *args)
        return ret

    def outer2d(self, *args):
        """
        V.outer2d((float, float), (float, float), [[float, float], [float,
             float]])
        C++: static void Outer2D(const double x[2], const double y[2],
            double A[2][2])
        Outer product of two 2-vectors (float version).
        """
        ret = self._wrap_call(self._vtk_obj.Outer2D, *args)
        return ret

    def perpendiculars(self, *args):
        """
        V.perpendiculars((float, float, float), [float, float, float],
            [float, float, float], float)
        C++: static void Perpendiculars(const double x[3], double y[3],
            double z[3], double theta)
        Given a unit vector x, find two unit vectors y and z such that x
        cross y = z (i.e. the vectors are perpendicular to each other).
        There is an infinite number of such vectors, specify an angle
        theta to choose one set.  If you want only one perpendicular
        vector, specify NULL for z.
        """
        ret = self._wrap_call(self._vtk_obj.Perpendiculars, *args)
        return ret

    def pi(self):
        """
        V.pi() -> float
        C++: static float Pi()
        A mathematical constant. This version is 3.14159265358979f.
        """
        ret = self._vtk_obj.Pi()
        return ret
        

    def point_is_within_bounds(self, *args):
        """
        V.point_is_within_bounds([float, float, float], [float, float, float,
             float, float, float], [float, float, float]) -> int
        C++: static int PointIsWithinBounds(double point[3],
            double bounds[6], double delta[3])
        Return true if point is within the given 3d bounds Bounds is
        x-min, x-max, y-min, y-max, z-min, z-max Delta is the error
        margin along each axis (usually a small number)
        """
        ret = self._wrap_call(self._vtk_obj.PointIsWithinBounds, *args)
        return ret

    def project_vector(self, *args):
        """
        V.project_vector((float, float, float), (float, float, float),
            [float, float, float]) -> bool
        C++: static bool ProjectVector(const double a[3],
            const double b[3], double projection[3])
        Compute the projection of vector a on vector b and return it in
        projection[3]. If b is a zero vector, the function returns false
        and 'projection' is invalid. Otherwise, it returns true.
        """
        ret = self._wrap_call(self._vtk_obj.ProjectVector, *args)
        return ret

    def project_vector2d(self, *args):
        """
        V.project_vector2d((float, float), (float, float), [float, float])
            -> bool
        C++: static bool ProjectVector2D(const double a[2],
            const double b[2], double projection[2])
        Compute the projection of 2d vector 'a' on 2d vector 'b' and
        returns the result in projection[2]. If b is a zero vector, the
        function returns false and 'projection' is invalid. Otherwise, it
        returns true.
        """
        ret = self._wrap_call(self._vtk_obj.ProjectVector2D, *args)
        return ret

    def quaternion_to_matrix3x3(self, *args):
        """
        V.quaternion_to_matrix3x3((float, float, float, float), [[float,
            float, float], [float, float, float], [float, float, float]])
        C++: static void QuaternionToMatrix3x3(const double quat[4],
            double A[3][3])
        Convert a quaternion to a 3x3 rotation matrix.  The quaternion
        does not have to be normalized beforehand.
        """
        ret = self._wrap_call(self._vtk_obj.QuaternionToMatrix3x3, *args)
        return ret

    def rgb_to_hsv(self, *args):
        """
        V.rgb_to_hsv((float, float, float)) -> (float, float, float)
        C++: static double *RGBToHSV(const double rgb[3])
        V.rgb_to_hsv(float, float, float) -> (float, float, float)
        C++: static double *RGBToHSV(double r, double g, double b)
        V.rgb_to_hsv((float, float, float), [float, float, float])
        C++: static void RGBToHSV(const double rgb[3], double hsv[3])
        Convert color in RGB format (Red, Green, Blue) to HSV format
        (Hue, Saturation, Value). The input color is not modified.
        """
        ret = self._wrap_call(self._vtk_obj.RGBToHSV, *args)
        return ret

    def rgb_to_lab(self, *args):
        """
        V.rgb_to_lab((float, float, float), [float, float, float])
        C++: static void RGBToLab(const double rgb[3], double lab[3])
        Convert color from the RGB system to CIE-L*ab.
        """
        ret = self._wrap_call(self._vtk_obj.RGBToLab, *args)
        return ret

    def rgb_to_xyz(self, *args):
        """
        V.rgb_to_xyz((float, float, float), [float, float, float])
        C++: static void RGBToXYZ(const double rgb[3], double xyz[3])
        Convert color from the RGB system to CIE XYZ.
        """
        ret = self._wrap_call(self._vtk_obj.RGBToXYZ, *args)
        return ret

    def radians_from_degrees(self, *args):
        """
        V.radians_from_degrees(float) -> float
        C++: static double RadiansFromDegrees(double degrees)
        Convert degrees into radians
        """
        ret = self._wrap_call(self._vtk_obj.RadiansFromDegrees, *args)
        return ret

    def radians_to_degrees(self):
        """
        V.radians_to_degrees() -> float
        C++: static float RadiansToDegrees()
        @deprecated Replaced by Math::DegreesFromRadians() as of VTK
        5.4.
        """
        ret = self._vtk_obj.RadiansToDegrees()
        return ret
        

    def random(self, *args):
        """
        V.random() -> float
        C++: static double Random()
        V.random(float, float) -> float
        C++: static double Random(double min, double max)
        Generate pseudo-random numbers distributed according to the
        uniform distribution between 0.0 and 1.0. This is used to provide
        portability across different systems.
        
        DON'T USE Random(), random_seed(), get_seed(), Gaussian() THIS IS
        STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR REGRESSION
        TESTS) THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY. Instead, for
        a sequence of random numbers with a uniform distribution create a
        MinimalStandardRandomSequence object. For a sequence of random
        numbers with a gaussian/normal distribution create a
        BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.Random, *args)
        return ret

    def random_seed(self, *args):
        """
        V.random_seed(int)
        C++: static void RandomSeed(int s)
        Initialize seed value. NOTE: Random() has the bad property that
        the first random number returned after random_seed() is called is
        proportional to the seed value! To help solve this, call
        random_seed() a few times inside seed. This doesn't ruin the
        repeatability of Random().
        
        DON'T USE Random(), random_seed(), get_seed(), Gaussian() THIS IS
        STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR REGRESSION
        TESTS) THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY. Instead, for
        a sequence of random numbers with a uniform distribution create a
        MinimalStandardRandomSequence object. For a sequence of random
        numbers with a gaussian/normal distribution create a
        BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.RandomSeed, *args)
        return ret

    def round(self, *args):
        """
        V.round(float) -> int
        C++: static int Round(double f)
        Rounds a float to the nearest integer.
        """
        ret = self._wrap_call(self._vtk_obj.Round, *args)
        return ret

    def singular_value_decomposition3x3(self, *args):
        """
        V.singular_value_decomposition3x3(((float, float, float), (float,
            float, float), (float, float, float)), [[float, float, float],
             [float, float, float], [float, float, float]], [float, float,
             float], [[float, float, float], [float, float, float],
            [float, float, float]])
        C++: static void SingularValueDecomposition3x3(
            const double A[3][3], double U[3][3], double w[3],
            double VT[3][3])
        Perform singular value decomposition on a 3x3 matrix.  This is
        not done using a conventional SVD algorithm, instead it is done
        using Orthogonalize3x3 and Diagonalize3x3.  Both output matrices
        U and VT will have positive determinants, and the w values will
        be arranged such that the three rows of VT are aligned as closely
        as possible with the x, y, and z axes respectively.  If the
        determinant of A is negative, then the three w values will be
        negative.
        """
        ret = self._wrap_call(self._vtk_obj.SingularValueDecomposition3x3, *args)
        return ret

    def solve3_point_circle(self, *args):
        """
        V.solve3_point_circle((float, float, float), (float, float, float),
            (float, float, float), [float, float, float]) -> float
        C++: static double Solve3PointCircle(const double p1[3],
            const double p2[3], const double p3[3], double center[3])
        In Euclidean space, there is a unique circle passing through any
        given three non-collinear points P1, P2, and P3. Using Cartesian
        coordinates to represent these points as spatial vectors, it is
        possible to use the dot product and cross product to calculate
        the radius and center of the circle. See:
        http://en.wikipedia.org/wiki/Circumcircle and more specifically
        the section Barycentric coordinates from cross- and dot-products
        """
        ret = self._wrap_call(self._vtk_obj.Solve3PointCircle, *args)
        return ret

    def solve_cubic(self, *args):
        """
        V.solve_cubic(float, float, float, float) -> (float, float, float,
            float, float)
        C++: static double *SolveCubic(double c0, double c1, double c2,
            double c3)
        Solves a cubic equation c0*t^3 + c1*t^2 + c2*t + c3 = 0 when c0,
        c1, c2, and c3 are REAL.  Solution is motivated by Numerical
        Recipes In C 2nd Ed.  Return array contains number of (real)
        roots (counting multiple roots as one) followed by roots
        themselves. The value in roots[4] is a integer giving further
        information about the roots (see return codes for int
        solve_cubic() ).
        """
        ret = self._wrap_call(self._vtk_obj.SolveCubic, *args)
        return ret

    def solve_linear(self, *args):
        """
        V.solve_linear(float, float) -> (float, float, float)
        C++: static double *SolveLinear(double c0, double c1)
        Solves a linear equation c2*t  + c3 = 0 when c2 and c3 are REAL.
        Solution is motivated by Numerical Recipes In C 2nd Ed. Return
        array contains number of roots followed by roots themselves.
        """
        ret = self._wrap_call(self._vtk_obj.SolveLinear, *args)
        return ret

    def solve_quadratic(self, *args):
        """
        V.solve_quadratic(float, float, float) -> (float, float, float,
            float)
        C++: static double *SolveQuadratic(double c0, double c1,
            double c2)
        Solves a quadratic equation c1*t^2 + c2*t + c3 = 0 when c1, c2,
        and c3 are REAL.  Solution is motivated by Numerical Recipes In C
        2nd Ed. Return array contains number of (real) roots (counting
        multiple roots as one) followed by roots themselves. Note that
        roots[3] contains a return code further describing solution - see
        documentation for solve_cubic() for meaning of return codes.
        """
        ret = self._wrap_call(self._vtk_obj.SolveQuadratic, *args)
        return ret

    def spiral_points(self, *args):
        """
        V.spiral_points(int, Points)
        C++: static void SpiralPoints(IdType num, Points *offsets)
        Calculate num points, at a regular interval, along a parametric
        spiral. Note this spiral is only in two dimensions having a
        constant z value.
        """
        my_args = deref_array(args, [('int', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.SpiralPoints, *my_args)
        return ret

    def subtract(self, *args):
        """
        V.subtract((float, float, float), (float, float, float), [float,
            float, float])
        C++: static void Subtract(const double a[3], const double b[3],
            double c[3])
        Subtraction of two 3-vectors (double version). Result is stored
        in c according to c = a - b.
        """
        ret = self._wrap_call(self._vtk_obj.Subtract, *args)
        return ret

    def transpose3x3(self, *args):
        """
        V.transpose3x3(((float, float, float), (float, float, float), (
            float, float, float)), [[float, float, float], [float, float,
            float], [float, float, float]])
        C++: static void Transpose3x3(const double A[3][3],
            double AT[3][3])
        Transpose a 3x3 matrix. The input matrix is A. The output is
        stored in AT.
        """
        ret = self._wrap_call(self._vtk_obj.Transpose3x3, *args)
        return ret

    def uninitialize_bounds(self, *args):
        """
        V.uninitialize_bounds([float, float, float, float, float, float])
        C++: static void UninitializeBounds(double bounds[6])
        Set the bounds to an uninitialized state
        """
        ret = self._wrap_call(self._vtk_obj.UninitializeBounds, *args)
        return ret

    def xyz_to_lab(self, *args):
        """
        V.xyz_to_lab((float, float, float), [float, float, float])
        C++: static void XYZToLab(const double xyz[3], double lab[3])
        Convert Color from the CIE XYZ system to CIE-L*ab.
        """
        ret = self._wrap_call(self._vtk_obj.XYZToLab, *args)
        return ret

    def xyz_to_rgb(self, *args):
        """
        V.xyz_to_rgb((float, float, float), [float, float, float])
        C++: static void XYZToRGB(const double xyz[3], double rgb[3])
        Convert color from the CIE XYZ system to RGB.
        """
        ret = self._wrap_call(self._vtk_obj.XYZToRGB, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Math, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

