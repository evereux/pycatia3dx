"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrOpeningOutputProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningOutputProfile
                | 
                | Object to manage the Structure Opening in OutputProfile mode.
                | An Opening can specify the length of the negative extrusion will be done thanks
                | to the limit. A limit is a keyword that applies to the OutputProfile and
                | StandardOpening modes only. It applies to both sides of the contour and can
                | be:
                | - UpToLast: the opening will pierce everything in both direction of the support
                | plane of the contour.
                | - Dimensions: the user can specify two offsets piloting the length of the
                | extrusion removal.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Direction() As Reference
                |     Returns or Sets the direction of extrusion of this
                |     Opening.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in Direction of the
                |              opening.
                |              
                | 
                |              Set RefDirection = ObjStrOpeningOutputProfile.Direction

        :return: Reference
        """

        return Reference(self.com_object.Direction)

    @direction.setter
    def direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Direction = value

    @property
    def limit_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitMode() As long
                |     Returns or Sets the LimitMode.of the opening LimitMode can be UpToLast(0)
                |     or Dimensions(1)
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in LimitMode of the
                |              opening.
                |              
                | 
                |              lLimitMode = ObjStrOpeningOutputProfile.LimitMode

        :return: int
        """

        return self.com_object.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.LimitMode = value

    @property
    def output_profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OutputProfile() As Reference
                |     Returns or Sets the output profile.of the opening
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in OutputProfile of the opening created in
                |              sketch mode.
                |              
                | 
                |              Dim ObjStrOpeningOutputProfile As
                |              StrOpeningOutputProfile
                |              Set ObjStrOpeningOutputProfile = ObjStrOpening.StrOpeningOutputProfile
                |              Set RefOutPutProfile = ObjStrOpeningOutputProfile.OutputProfile

        :return: Reference
        """

        return Reference(self.com_object.OutputProfile)

    @output_profile.setter
    def output_profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.OutputProfile = value

    def __repr__(self):
        return f'StrOpeningOutputProfile(name="{ self.name }")'
