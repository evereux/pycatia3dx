"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeRevol(HybridShape):

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
                |                         HybridShapeRevol
                | 
                | The Revol feature : an Revol is made up of a face to process and one Revol parameter.
                | Role: To access the data of the hybrid shape revol feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
    
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
                |     Role: To get_Axis on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

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
    def begin_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginAngle() As Angle (Read Only)
                |     Role: To get_BeginAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.BeginAngle)

    @property
    def begin_angle_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginAngleOffset() As double
                |     Gets/Sets the first angle offset value of first upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oAng1
                |             first angle offset value.

        :return: float
        """

        return self.com_object.BeginAngleOffset

    @begin_angle_offset.setter
    def begin_angle_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.BeginAngleOffset = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Context() As long
                |     Returns or sets the context on Revolve feature.
                |     Legal values:
                | 
                |         0 This option creates surface of revolution.
                |         1 This option creates volume of revolution.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Revol hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Revol.Context

        :return: int
        """

        return self.com_object.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.com_object.Context = value

    @property
    def end_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndAngle() As Angle (Read Only)
                |     Role: To get_EndAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.EndAngle)

    @property
    def end_angle_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndAngleOffset() As double
                |     Gets/Sets the second angle offset value of second upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oAng2
                |             second angle offset value.

        :return: float
        """

        return self.com_object.EndAngleOffset

    @end_angle_offset.setter
    def end_angle_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.EndAngleOffset = value

    @property
    def first_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstLimitType() As long
                |     Returns or sets the First limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim1Type the first limit type for the Revolve
                |     hybrid shape feature.
                | 
                |      Dim oLim1Type
                |      Set oLim1Type = Revolve.FirstLimitType

        :return: int
        """

        return self.com_object.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstUptoElement() As Reference
                |     Returns or sets the First up-to element used to limit
                |     Revolution.
                | 
                |     Example:
                |         This example retrieves in Lim1Elem the First up-to element for the
                |         Revolve hybrid shape feature.
                | 
                |          Dim Lim1Elem As Reference 
                |          Set Lim1Elem = Revolve.FirstUptoElement

        :return: Reference
        """

        return Reference(self.com_object.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstUptoElement = value

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation(boolean iOrientation)
                |     Gets or sets orientation of the revolution. Orientation = TRUE : The natural orientation of the axis is taken. = FALSE : The opposite orientation is taken This example retrieves in IsInverted orientation of the revolution for the Revol hybrid shape feature.
                | 
                |      Dim IsInverted As boolean
                |      IsInverted = Revol.Orientation

        :return: bool
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Orientation = value

    @property
    def profil(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Profil() As Reference
                |     Role: To get_Profil on the object.
                | 
                |     Parameters:
                | 
                |         oProfil
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.Profil)

    @profil.setter
    def profil(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Profil = value

    @property
    def second_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondLimitType() As long
                |     Returns or sets the Second limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim2Type the second limit type for the Revolve
                |     hybrid shape feature.
                | 
                |      Dim oLim2Type
                |      Set oLim2Type = RevolveSecondLimitType

        :return: int
        """

        return self.com_object.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondUptoElement() As Reference
                |     Returns or sets the Second up-to element used to limit
                |     Revolution.
                | 
                |     Example:
                |         This example retrieves in Lim2Elem the Second up-to element for the
                |         Revolve hybrid shape feature.
                | 
                |          Dim Lim2Elem As Reference 
                |          Set Lim2Elem = Revolve.SecondUptoElement

        :return: Reference
        """

        return Reference(self.com_object.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondUptoElement = value

    def __repr__(self):
        return f'HybridShapeRevol(name="{ self.name }")'
