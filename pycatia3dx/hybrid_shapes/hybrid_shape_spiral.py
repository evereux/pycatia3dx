"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSpiral(HybridShape):

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
                |                         HybridShapeSpiral
                | 
                | Represents the hybrid shape Spiral feature object.
                | Role: Allows to access data of the Spiral feature. This data
                | includes:
                | 
                |     type
                |     support
                |     centre point
                |     axis
                |     starting radius
                |     orientation
                |     ending angle
                |     ending radius
                |     revolution
                |     pitch
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Axis() As HybridShapeDirection
                |     Reads / Changes the Spiral axis (Reference direction).

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Axis)

    @axis.setter
    def axis(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Axis = value

    @property
    def center_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CenterPoint() As Reference
                |     Reads / Changes the center point of the Spiral.

        :return: Reference
        """

        return Reference(self.com_object.CenterPoint)

    @center_point.setter
    def center_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CenterPoint = value

    @property
    def clockwise_revolution(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ClockwiseRevolution() As boolean
                |     Reads / Modifies the sense of revolutions .
                |     FALSE means that revolutions are counter-clockwise.
                |     TRUE means that revolutions are clockwise.

        :return: bool
        """

        return self.com_object.ClockwiseRevolution

    @clockwise_revolution.setter
    def clockwise_revolution(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ClockwiseRevolution = value

    @property
    def ending_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndingAngle() As Angle
                |     Reads / Changes the Ending Angle of the Spiral.

        :return: Angle
        """

        return Angle(self.com_object.EndingAngle)

    @ending_angle.setter
    def ending_angle(self, value: Angle):
        """
        :param Angle value:
        """

        self.com_object.EndingAngle = value

    @property
    def ending_radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndingRadius() As Length
                |     Reads / Changes the ending radius of the Spiral.

        :return: Length
        """

        return Length(self.com_object.EndingRadius)

    @ending_radius.setter
    def ending_radius(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.EndingRadius = value

    @property
    def invert_axis(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InvertAxis() As boolean
                |     Reads / Modifies the orientation .
                |     FALSE means that there is no invertion (natural
                |     orientation).
                |     TRUE to invert this orientation.

        :return: bool
        """

        return self.com_object.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InvertAxis = value

    @property
    def pitch(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Pitch() As Length
                |     Reads / Changes the pitch of the Spiral.

        :return: Length
        """

        return Length(self.com_object.Pitch)

    @pitch.setter
    def pitch(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.Pitch = value

    @property
    def revol_number(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RevolNumber() As RealParam
                |     Reads / Changes the revolution number of the Spiral.

        :return: RealParam
        """

        return RealParam(self.com_object.RevolNumber)

    @revol_number.setter
    def revol_number(self, value: RealParam):
        """
        :param RealParam value:
        """

        self.com_object.RevolNumber = value

    @property
    def starting_radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartingRadius() As Length
                |     Reads / Changes the starting radius of the Spiral.

        :return: Length
        """

        return Length(self.com_object.StartingRadius)

    @starting_radius.setter
    def starting_radius(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.StartingRadius = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Reads / Changes the spiral plane support.

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Type() As long
                |     Reads / Changes the spiral type.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def set_angle_pitch_param(self, i_end_angle: float, i_revol_number: float, i_pitch: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAnglePitchParam(double iEndAngle,double iRevolNumber,double
                | iPitch)
                |     Sets Angle pitch parameter.

        :param float i_end_angle:
        :param float i_revol_number:
        :param float i_pitch:
        :return: None
        """
        return self.com_object.SetAnglePitchParam(i_end_angle, i_revol_number, i_pitch)

    def set_angle_radius_param(self, i_end_angle: float, i_revol_number: float, i_end_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngleRadiusParam(double iEndAngle,double iRevolNumber,double
                | iEndRadius)
                |     Sets Angle radius parameters.

        :param float i_end_angle:
        :param float i_revol_number:
        :param float i_end_radius:
        :return: None
        """
        return self.com_object.SetAngleRadiusParam(i_end_angle, i_revol_number, i_end_radius)

    def set_radius_pitch_param(self, i_end_radius: float, i_pitch: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRadiusPitchParam(double iEndRadius,double iPitch)
                |     Sets Radius pitch parameter.

        :param float i_end_radius:
        :param float i_pitch:
        :return: None
        """
        return self.com_object.SetRadiusPitchParam(i_end_radius, i_pitch)

    def __repr__(self):
        return f'HybridShapeSpiral(name="{ self.name }")'
