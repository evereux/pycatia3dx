"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeCircle(HybridShape):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeCircle
                | 
                | Represents the hybrid shape circle object.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle radius
                |     Two circle center
                |     The circle arc limitation mode
                |     The circle start and end angles
                | 
                | All interfaces for different type of circle derivates
                | HybridShapeCircle.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_computation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisComputation() As boolean
                |     Returns or sets the axis computation mode.
                | 
                |     Example:
                | 
                |          This example retrieves the axis computation mode of
                |          the hybShpCircle
                |          
                | 
                |          Dim axisComp As Boolean
                |          axisComp = hybShpCircle.AxisComputation

        :return: bool
        """

        return self.com_object.AxisComputation

    @axis_computation.setter
    def axis_computation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AxisComputation = value

    @property
    def axis_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisDirection() As HybridShapeDirection
                |     Role: To get_Direction on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         HybridShapeDirection
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.AxisDirection)

    @axis_direction.setter
    def axis_direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.AxisDirection = value

    @property
    def end_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndAngle() As Angle (Read Only)
                |     Returns the circle end angle.
                | 
                |     Example:
                |         This example retrieves in ShpCircleEndAngle the end angle of the
                |         ShpCircle hybrid shape circle.
                | 
                |          Dim ShpCircleEndAngle As Angle
                |          ShpCircleEndAngle = ShpCircle.EndAngle

        :return: Angle
        """

        return Angle(self.com_object.EndAngle)

    @property
    def start_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartAngle() As Angle (Read Only)
                |     Returns the circle start angle.
                | 
                |     Example:
                |         This example retrieves in ShpCircleStartAngle the end angle of the
                |         ShpCircle hybrid shape circle.
                | 
                |          Dim ShpCircleStartAngle As Angle
                |          ShpCircleStartAngle = ShpCircle.StartAngle

        :return: Angle
        """

        return Angle(self.com_object.StartAngle)

    def get_axis(self, i_position: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetAxis(long iPosition,Reference oAxis)
                |     Returns the axis of the Circle.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of axis to be retrived. 3 - CATGSMAxisLineType_NormalToCircle
                |             2 - CATGSMAxisLineType_NormalToDirection 1 -
                |             CATGSMAxisLineType_AlignedWithDirection 
                |         oAxis
                |             Reference to the element.
                | 
                |             Example:
                |                 This example retrieves the axis of the circle. HybShpCircle
                |                 hybrid shape circle.
                | 
                |                  Dim AxisRef As Reference
                |                  HybShpCircle.GetAxis 1, AxisRef

        :param int i_position:
        :return: Reference
        """
        # todo: check this method, does it require system service?
        return Reference(self.com_object.GetAxis(i_position))

    def get_center(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetCenter(double oCenterX,double oCenterY,double oCenterZ)
                |     Gets the mathematical center of the circle. This information is available
                |     once the circle has been computed.
                | 
                |     Parameters:
                | 
                |         oCenterX,
                |             oCenterY, oCenterZ, circle center

        :return: tuple
        """
        return self.com_object.GetCenter()

    def get_free_center(self, io_center: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFreeCenter(CATSafeArrayVariant ioCenter)
                |     Returns the circle center.
                | 
                |     Parameters:
                | 
                |         oCenter
                |             The circle center. It is returned as an array of three coordinates
                |             in SafeArrayVariant 
                | 
                |     Example:
                |         This example retrieves in HybShpCircleCenter the center of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleCenter
                |          ReDim HybShpCircleCenter(2)
                |          ShpCircle.GetFreeRadius(HybShpCircleCenter)
                |          
                | 
                |         You can access each center coordinate as follows:
                | 
                |             x is in HybShpCircleCenter(0)
                |             y is in HybShpCircleCenter(1)
                |             z is in HybShpCircleCenter(2)

        :param tuple io_center:
        :return: None
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetFreeCenter(io_center)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise, completely remove all this.
        # # vba_function_name = 'get_free_center'
        # # vba_code = """
        # # Public Function get_free_center(hybrid_shape_circle)
        # #     Dim ioCenter (2)
        # #     hybrid_shape_circle.GetFreeCenter ioCenter
        # #     get_free_center = ioCenter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_free_radius(self, o_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFreeRadius(double oRadius)
                |     Returns the circle radius.
                | 
                |     Parameters:
                | 
                |         oRadius
                |             The circle radius 
                | 
                |     Example:
                |         This example retrieves in HybShpCircleRadius the radius of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          double HybShpCircleRadius
                |          ShpCircle.GetFreeRadius(HybShpCircleRadius)

        :param float o_radius:
        :return: None
        """
        return self.com_object.GetFreeRadius(o_radius)

    def get_limitation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLimitation() As long
                |     Gets the limitation type for the circle.
                | 
                |     Parameters:
                | 
                |         oLimit
                |             (Angles = 0, Whole = 1, Trimmed = 2, Complementary = 3). circle limitation

        :return: int
        """
        return self.com_object.GetLimitation()

    def set_limitation(self, i_limitation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLimitation(long iLimitation)
                |     Set the circle limitation type.
                | 
                |     Parameters:
                | 
                |         iLimitation
                |             The circle limitation type
                |             Legal values:
                | 
                |             0
                |                 Angles 
                |             1
                |                 Whole 
                |             2
                |                 Trimmed 
                |             3
                |                 Complementary 
                | 
                |     Example:
                |         This example sets the limitiation type of the ShpCircle hybrid shape
                |         circle to trim.
                | 
                |          ShpCircle.SetLimitation 2

        :param int i_limitation:
        :return: None
        """
        return self.com_object.SetLimitation(i_limitation)

    def __repr__(self):
        return f'HybridShapeCircle(name="{self.name}")'
