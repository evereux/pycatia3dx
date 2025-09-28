"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.line import Line
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeLineAngle(Line):

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
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineAngle
                | 
                | Line defined from a reference curve, a plane or a surface, a point and an
                | angle.
                | Role: Allows to access data of the line feature created with an angle to a
                | curve.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Angle() As Angle (Read Only)
                |     Role: Get the angle to the reference curve of the line.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             angle

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginOffset() As Length (Read Only)
                |     Role: Get the start length of the line.
                | 
                |     Parameters:
                | 
                |         oStart
                |             start length

        :return: Length
        """

        return Length(self.com_object.BeginOffset)

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Curve() As Reference
                |     Role: Get the reference curve.
                | 
                |     Parameters:
                | 
                |         oCurve
                |             reference curve.

        :return: Reference
        """

        return Reference(self.com_object.Curve)

    @curve.setter
    def curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve = value

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndOffset() As Length (Read Only)
                |     Role: Get the end length of the line.
                | 
                |     Parameters:
                | 
                |         oEnd
                |             end length

        :return: Length
        """

        return Length(self.com_object.EndOffset)

    @property
    def geodesic(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Geodesic() As boolean
                |     Role: Get geodesic mode. If geodesic, the line lies on the support surface,
                |     otherwise the surface is only used to compute the line
                |     direction.
                | 
                |     Parameters:
                | 
                |         oGeod
                |             Geodesic boolean

        :return: bool
        """

        return self.com_object.Geodesic

    @geodesic.setter
    def geodesic(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Geodesic = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Role: Get the line orientation. Orientation allows to reverse the line
                |     direction from the reference point. For a line of L length, it is the same as
                |     creating this line with -L length.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             orientation : can be 1 or -1

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Role: Get the starting point of the line.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             starting point.

        :return: Reference
        """

        return Reference(self.com_object.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Point = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Surface() As Reference
                |     Role: Get the support surface.
                | 
                |     Parameters:
                | 
                |         oSurface
                |             support surface.

        :return: Reference
        """

        return Reference(self.com_object.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Surface = value

    def get_length_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLengthType() As long
                |     Gets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         oType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :return: int
        """
        return self.com_object.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSymmetricalExtension() As boolean
                |     Gets whether the symmetrical extension of the line is
                |     active.
                | 
                |     Parameters:
                | 
                |         oSym
                |             Symetry flag

        :return: bool
        """
        return self.com_object.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLengthType(long iType)
                |     Sets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         iType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :param int i_type:
        :return: None
        """
        return self.com_object.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSymmetricalExtension(boolean iSym)
                |     Sets the symmetrical extension of the line (start = -end).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :param bool i_sym:
        :return: None
        """
        return self.com_object.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineAngle(name="{ self.name }")'
