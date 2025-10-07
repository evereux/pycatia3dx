"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfilePtLimit(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfilePtLimit
                | 
                | Object to manage Profile created with a point and a limit.
    
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
                |     Returns or Sets the Profile's Direction.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves the profile's direction
                |              
                | 
                |              Dim ObjStrProfilePtLimit As StrProfilePtLimit
                |              Set ObjStrProfilePtLimit = ObjSfdMember.StrProfilePtLimit
                |              Set RefDirection = ObjStrProfilePtLimit.Direction

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
    def start_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartPoint() As Reference
                |     Returns or Sets the Profile's Start point.

        :return: Reference
        """

        return Reference(self.com_object.StartPoint)

    @start_point.setter
    def start_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.StartPoint = value

    @property
    def up_to_limit(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpToLimit() As Reference
                |     Returns or Sets the Profile's UpToLimit.

        :return: Reference
        """

        return Reference(self.com_object.UpToLimit)

    @up_to_limit.setter
    def up_to_limit(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.UpToLimit = value

    def get_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrientation() As long
                |     Orientation Returns the orientation associated to the
                |     direction.
                |     Legal values for Orientation:
                |     -1 = InvertOrientation
                |     0 = UnknownOrientation
                |     1 = SameOrientation
                |     2 = X+ ( X+ vector = ( 1, 0, 0) )
                |     3 = X- ( X- vector = (-1, 0, 0) )
                |     4 = Y+ ( Y+ vector = ( 0, 1, 0) )
                |     5 = Y- ( Y- vector = ( 0,-1, 0) )
                |     6 = Z+ ( Z+ vector = ( 0, 0, 1) )
                |     7 = Z- ( Z- vector = ( 0, 0,-1) )
                |     8 = Inside
                |     9 = Outside
                |     10 = Inboard ( Toward center line )
                |     11 = Outboard ( Opposite of previous one )
                |     12 = Inboard ( Toward midship )
                |     13 = Outboard ( Opposite of previous one )
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves the orientation associated to the
                |              direction
                |              
                | 
                |              Orientation = ObjStrProfilePtLimit.GetOrientation

        :return: int
        """
        return self.com_object.GetOrientation()

    def reverse_direction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseDirection()
                |     Reverses Direction 

        :return: None
        """
        return self.com_object.ReverseDirection()

    def __repr__(self):
        return f'StrProfilePtLimit(name="{ self.name }")'
