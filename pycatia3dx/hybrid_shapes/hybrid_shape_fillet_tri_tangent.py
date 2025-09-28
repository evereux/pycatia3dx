"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeFilletTriTangent(HybridShape):

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
                |                         HybridShapeFilletTriTangent
                | 
                | Fillet Tri-Tangent feature.
                | Role: Manipulation of Fillet Tri-Tangent feature Allows to access data of the
                | Fillet Tri-Tangent feature created by using three support surfaces, their
                | orientation, and options (supports trimming and fillet extremities
                | type)
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstElem() As Reference
                |     Returns or sets the first support surface feature.
                | 
                |     Example:
                |         This example retrieves in FirstElem the first support element used by
                |         the HybShpFilletTriTangent hybrid shape feature.
                | 
                |          Dim FirstElem As Reference 
                |          Set FirstElem = HybShpFilletTriTangent.FirstElem

        :return: Reference
        """

        return Reference(self.com_object.FirstElem)

    @first_elem.setter
    def first_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstElem = value

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstOrientation() As long
                |     Returns or sets the first orientation used to specify fillet center
                |     position.
                |     Note; Orientation is same or inverse than the normal to the first surface
                |     support

        :return: int
        """

        return self.com_object.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstOrientation = value

    @property
    def remove_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RemoveElem() As Reference
                |     Returns or sets the support surface to remove feature.

        :return: Reference
        """

        return Reference(self.com_object.RemoveElem)

    @remove_elem.setter
    def remove_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RemoveElem = value

    @property
    def remove_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RemoveOrientation() As long
                |     Returns or sets the third orientation used to specify fillet center
                |     position.
                |     note: Orientation is same or inverse than the normal to the surface support
                |     to remove

        :return: int
        """

        return self.com_object.RemoveOrientation

    @remove_orientation.setter
    def remove_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.RemoveOrientation = value

    @property
    def ribbon_relimitation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RibbonRelimitationMode() As long
                |     Returns or sets fillet ribbon relimitation mode (or fillet extremities
                |     mode).
                |     note: Smooth(0) or Straight(1) or Maximum(2) or Minimum(3)

        :return: int
        """

        return self.com_object.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.RibbonRelimitationMode = value

    @property
    def second_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondElem() As Reference
                |     Returns or sets the Second support surface feature.
                | 
                |     Example:
                |         This example retrieves in SecondElem the Second support element used by
                |         the HybShpFilletTriTangent hybrid shape feature.
                | 
                |          Dim SecondElem As Reference 
                |          Set SecondElem = HybShpFilletTriTangent.SecondElem
                |          
                | 
                |     Parameters:
                | 
                |         oElem
                |             Second support surface feature.

        :return: Reference
        """

        return Reference(self.com_object.SecondElem)

    @second_elem.setter
    def second_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondElem = value

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondOrientation() As long
                |     Returns or sets the Second orientation used to specify fillet center
                |     position.
                |     note: Orientation is same or inverse than the normal to the Second surface
                |     support

        :return: int
        """

        return self.com_object.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondOrientation = value

    @property
    def supports_trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SupportsTrimMode() As long
                |     Returns or sets whether support surfaces are trimmed or
                |     not.
                |     Trim (1) or NoTrim(0)
                |     note: if "Trim" the 2 supports are trimmed and assembled with the fillet
                |     ribbon.

        :return: int
        """

        return self.com_object.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.SupportsTrimMode = value

    def invert_first_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertFirstOrientation()
                |     Inverts first orientation used to specify fillet center position.

        :return: None
        """
        return self.com_object.InvertFirstOrientation()

    def invert_remove_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertRemoveOrientation()
                |     Inverts third orientation used to specify fillet center position.

        :return: None
        """
        return self.com_object.InvertRemoveOrientation()

    def invert_second_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertSecondOrientation()
                |     Inverts second orientation used to specify fillet center position.

        :return: None
        """
        return self.com_object.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeFilletTriTangent(name="{ self.name }")'
