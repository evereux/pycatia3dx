"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeHelix(HybridShape):

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
                |                         HybridShapeHelix
                | 
                | Represents the hybrid shape helix feature object.
                | Role: Allows to access data of the Helix feature. This data
                | includes:
                | 
                |     axis
                |     a starting point
                |     a pitch
                |     a height
                |     2 angle values
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Axis() As Reference
                |     Reads / Changes the Helix axis.
                | 
                |     Parameters:
                | 
                |         Axis
                |             Helix axis.
                |             Sub-element(s) supported (see Boundary object):
                |             CATIARectlinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Axis)

    @axis.setter
    def axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Axis = value

    @property
    def clockwise_revolution(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ClockwiseRevolution() As boolean
                |     Reads / Modifies the sense of revolutions .
                | 
                |     Parameters:
                | 
                |         Clockwise
                |             FALSE means that revolutions are counter-clockwise. TRUE means that
                |             revolutions are clockwise.

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
    def height(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Height() As Length (Read Only)
                |     Reads the height of the Helix.
                | 
                |     Parameters:
                | 
                |         oHeight
                |             Height.

        :return: Length
        """

        return Length(self.com_object.Height)

    @property
    def invert_axis(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InvertAxis() As boolean
                |     Reads / Modifies the orientation .
                | 
                |     Parameters:
                | 
                |         Invert
                |             FALSE means that there is no invertion (natural orientation). TRUE
                |             to invert this orientation.

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
                | Property Pitch() As Length (Read Only)
                |     Reads the pitch of the Helix.
                | 
                |     Parameters:
                | 
                |         oPitch
                |             Pitch.

        :return: Length
        """

        return Length(self.com_object.Pitch)

    @property
    def pitch2(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Pitch2() As Length (Read Only)
                |     Reads the Helix pitch2.
                | 
                |     Parameters:
                | 
                |         Pitch2
                |             Pitch2 for Helix.

        :return: Length
        """

        return Length(self.com_object.Pitch2)

    @property
    def pitch_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PitchLawType() As long
                |     Reads / Changes the Helix pitch law type.
                | 
                |     Parameters:
                | 
                |         LawType
                |             LawType for Helix.

        :return: int
        """

        return self.com_object.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PitchLawType = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Profile() As Reference
                |     Reads / Changes the Helix profile.
                | 
                |     Parameters:
                | 
                |         Profile
                |             Profile for Helix.

        :return: Reference
        """

        return Reference(self.com_object.Profile)

    @profile.setter
    def profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Profile = value

    @property
    def revol_number(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RevolNumber() As RealParam (Read Only)
                |     Reads the revolution number of the Helix.
                | 
                |     Parameters:
                | 
                |         oNbRevol
                |             Revolutions.

        :return: RealParam
        """

        return RealParam(self.com_object.RevolNumber)

    @property
    def starting_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartingAngle() As Angle (Read Only)
                |     Reads the helix starting angle.
                | 
                |     Parameters:
                | 
                |         oStartingAngle
                |             Starting angle.

        :return: Angle
        """

        return Angle(self.com_object.StartingAngle)

    @property
    def starting_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartingPoint() As Reference
                |     Reads / Changes the starting point of the Helix. The starting point must
                |     not be on the Helix axis.
                | 
                |     Parameters:
                | 
                |         StartingPoint
                |             Starting point.
                |             Sub-element(s) supported (see Boundary object): Vertex.

        :return: Reference
        """

        return Reference(self.com_object.StartingPoint)

    @starting_point.setter
    def starting_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.StartingPoint = value

    @property
    def taper_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TaperAngle() As Angle (Read Only)
                |     Reads the helix taper angle.
                | 
                |     Parameters:
                | 
                |         oTaperAngle
                |             Taper angle.

        :return: Angle
        """

        return Angle(self.com_object.TaperAngle)

    @property
    def taper_outward(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TaperOutward() As boolean
                |     Reads / Modifies the taper angle sense of variation.
                | 
                |     Parameters:
                | 
                |         TaperOutward
                |             FALSE means that helix radius decreases. TRUE means that helix
                |             radius increases.

        :return: bool
        """

        return self.com_object.TaperOutward

    @taper_outward.setter
    def taper_outward(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TaperOutward = value

    def set_height(self, i_height: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetHeight(double iHeight)
                |     Sets the helix height.
                | 
                |     Parameters:
                | 
                |         iHeight
                |             Height.

        :param float i_height:
        :return: None
        """
        return self.com_object.SetHeight(i_height)

    def set_pitch(self, i_pitch: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPitch(double iPitch)
                |     Sets the helix pitch.
                | 
                |     Parameters:
                | 
                |         iPitch
                |             Pitch.

        :param float i_pitch:
        :return: None
        """
        return self.com_object.SetPitch(i_pitch)

    def set_pitch2(self, i_pitch2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPitch2(double iPitch2)
                |     Changes the Helix pitch2 .
                | 
                |     Parameters:
                | 
                |         Pitch2
                |             Pitch2 for Helix.

        :param float i_pitch2:
        :return: None
        """
        return self.com_object.SetPitch2(i_pitch2)

    def set_revolution_number(self, i_nb_revol: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRevolutionNumber(double iNbRevol)
                |     Changes the Revolution Numbers.
                | 
                |     Parameters:
                | 
                |         NbRevol
                |             Number of revolutions for Helix.

        :param float i_nb_revol:
        :return: None
        """
        return self.com_object.SetRevolutionNumber(i_nb_revol)

    def set_starting_angle(self, i_starting_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartingAngle(double iStartingAngle)
                |     Sets the helix starting angle.
                | 
                |     Parameters:
                | 
                |         oTaperAngle
                |             Starting angle.

        :param float i_starting_angle:
        :return: None
        """
        return self.com_object.SetStartingAngle(i_starting_angle)

    def set_taper_angle(self, i_taper_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTaperAngle(double iTaperAngle)
                |     Sets the helix taper angle.
                | 
                |     Parameters:
                | 
                |         iTaperAngle
                |             Taper angle.

        :param float i_taper_angle:
        :return: None
        """
        return self.com_object.SetTaperAngle(i_taper_angle)

    def __repr__(self):
        return f'HybridShapeHelix(name="{ self.name }")'
