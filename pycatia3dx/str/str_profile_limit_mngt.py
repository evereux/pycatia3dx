"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfileLimitMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileLimitMngt
                | 
                | Object to manage limits of the Profile.
                | Role: To manage Profile's limits.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def explicit_limits(self, i_extr: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExplicitLimits(long iExtr)
                |     In case the profile support is a Panel/Plate(s), it will set the limit
                |     ancestor of the DelimitedMoldedSurface edge stopping the CanonicTrace as a
                |     limit.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile that will be set with the Plate limit. If
                |             iExtr=-1, we reset both extremities.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity.

        :param int i_extr:
        :return: None
        """
        return self.com_object.ExplicitLimits(i_extr)

    def get_limit_type(self, i_extr: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLimitType(long iExtr) As long
                |     Returns the type of the limit applied on the Profile. This info is just
                |     captured at the support level and then realized at the Profile level in
                |     SDD.
                |     limit type can have following values
                |     -1 = Undefined limit
                |     0 = Short Point
                |     1 = Long Point
                |     2 = Weld
                |     3 = Miter Start
                |     4 = Miter End
                |     5 = Metal To Metal
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the limit type.
                |              
                | 
                |               Type = ObjStrProfileLimitMngt.GetLimitType

        :param int i_extr:
        :return: int
        """
        return self.com_object.GetLimitType(i_extr)

    def get_limiting_object(self, i_extr: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLimitingObject(long iExtr) As Reference
                |     Returns the feature set by the user on the extremity
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile where to Set the Limiting
                |             Object.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in Start limiting object of the
                |              profile.
                |              
                | 
                |              Set RefLimitingObject = ObjStrProfileLimitMngt.GetLimitingObject(1)

        :param int i_extr:
        :return: Reference
        """
        return Reference(self.com_object.GetLimitingObject(i_extr))

    def get_offset(self, i_extr: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffset(long iExtr) As Parameter
                |     Returns the limit offset
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in limit offset.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrProfileLimitMngt.GetOffset

        :param int i_extr:
        :return: Parameter
        """
        return Parameter(self.com_object.GetOffset(i_extr))

    def invert_profile(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InvertProfile()
                |     Invert the definition of the start and end for the selected profile.

        :return: None
        """
        return self.com_object.InvertProfile()

    def remove_limit(self, i_extr: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLimit(long iExtr)
                |     Removes the limit associated to the extremity. Remove the Limit +
                |     EndCut.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                | 
                |     Example:
                | 
                | 
                |              This example Removes Start limit of the profile.
                |              
                | 
                |               ObjStrProfileLimitMngt.RemoveLimit (1)

        :param int i_extr:
        :return: None
        """
        return self.com_object.RemoveLimit(i_extr)

    def set_limit_type(self, i_extr: int, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLimitType(long iExtr,long iType)
                |     Sets the type of the limit applied on the Profile.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                |         iType
                |             limit type
                |             It can have following values
                |             -1 = Undefined limit
                |             0 = Short Point
                |             1 = Long Point
                |             2 = Weld
                |             3 = Miter Start
                |             4 = Miter End
                |             5 = Metal To Metal 
                | 
                |     Example:
                | 
                | 
                |              This example sets the limit type.
                |              
                | 
                |               Type = ObjStrProfileLimitMngt.SetLimitType 1, 1

        :param int i_extr:
        :param int i_type:
        :return: None
        """
        return self.com_object.SetLimitType(i_extr, i_type)

    def set_limiting_object(self, i_extr: int, i_limiting_object: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLimitingObject(long iExtr,Reference iLimitingObject)
                |     Sets a feature selected by the user on the extremity
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity of the Profile where to Set the Limiting
                |             Object.
                |             If iExtr == 1 : Start extremity.
                |             If iExtr == 2 : End extremity. 
                |         iLimitingObject
                |             the feature to be set on the extremity. 
                | 
                |     Example:
                | 
                | 
                |              This example sets in Start limiting object of the
                |              profile.
                |              
                | 
                |               Set ObjLimit1 = Manager.GetReferencePlane(ObjPart, 1, "DECK.8")
                |               Set Limit1 = ObjPart.CreateReferenceFromObject(ObjLimit1)
                |               Dim ObjStrProfileLimitMngt As
                |               StrProfileLimitMngt
                |               Set ObjStrProfileLimitMngt = ObjSfdMember.StrProfileLimitMngt
                |               ObjStrProfileLimitMngt.SetLimitingObject 1,
                |               Limit1

        :param int i_extr:
        :param Reference i_limiting_object:
        :return: None
        """
        return self.com_object.SetLimitingObject(i_extr, i_limiting_object.com_object)

    def __repr__(self):
        return f'StrProfileLimitMngt(name="{ self.name }")'
