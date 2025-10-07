"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_endcut import StrEndcut


class StrEndcutMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrEndcutMngt
                | 
                | Object to manage Structure Functional Modeler Endcuts on the
                | Profile.
                | Role: To Manage Endcuts.
                | 
                | See also:
                |     StrDetailFeature, StrEndcut, StrProfileLimitMngt
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_endcut(self, i_extr: int) -> StrEndcut:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddEndcut(long iExtr) As StrEndcut
                |     Returns an Endcut created under this Profile Role:Create a Endcut under
                |     this Profile at a specific extremity.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity, 1 for start, 2 for end. 
                | 
                |     Example:
                | 
                | 
                |              This example creates an Endcut at start of
                |              profile.
                |              
                | 
                |              Dim ObjStrEndcutMngt As StrEndcutMngt
                |              Set ObjStrEndcutMngt = ObjSfdStiffener.StrEndcutMngt
                |              Dim ObjStrEndcut as StrEndcut
                |              Set ObjStrEndcut = ObjStrEndcutMngt.AddEndcut(1)

        :param int i_extr:
        :return: StrEndcut
        """
        return StrEndcut(self.com_object.AddEndcut(i_extr))

    def get_endcut(self, i_extr: int) -> StrEndcut:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEndcut(long iExtr) As StrEndcut
                |     Returns the Endcut that is at a specific extremity of this
                |     profile.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity, 1 for start, 2 for end. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves start Endcut of profile.
                |              
                | 
                |               Dim ObjStrEndcut As StrEndcut
                |               Set ObjStrEndcut = ObjStrEndcutMngt.GetEndcut(1)

        :param int i_extr:
        :return: StrEndcut
        """
        return StrEndcut(self.com_object.GetEndcut(i_extr))

    def remove_endcut(self, i_extr: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveEndcut(long iExtr)
                |     Removes the Endcut that is at a specific extremity of this
                |     profile.
                | 
                |     Parameters:
                | 
                |         iExtr
                |             Extremity, 1 for start, 2 for end. 
                | 
                |     Example:
                | 
                | 
                |              This example removes start Endcut of profile.
                |              
                | 
                |               ObjStrEndcutMngt.RemoveEndcut (1)

        :param int i_extr:
        :return: None
        """
        return self.com_object.RemoveEndcut(i_extr)

    def __repr__(self):
        return f'StrEndcutMngt(name="{ self.name }")'
