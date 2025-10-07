"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_detail_feature import StrDetailFeature


class StrEndcut(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrEndcut
                | 
                | Object to manage Endcut of a Profile.
                | Role: Allows accessing of Endcut's data.
                | 
                | See also:
                |     StrEndcutMngt
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_detail_feature(self) -> StrDetailFeature:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrDetailFeature() As StrDetailFeature (Read Only)
                |     Returns StrDetailFeature object.

        :return: StrDetailFeature
        """

        return StrDetailFeature(self.com_object.StrDetailFeature)

    def get_candidate_context(self, i_name: str) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCandidateContext(CATBSTR iName) As Reference
                |     Returns a candidate context for the endcut that is the limit already set on
                |     the Profile.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name.

        :param str i_name:
        :return: Reference
        """
        return Reference(self.com_object.GetCandidateContext(i_name))

    def get_extremity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetExtremity() As long
                |     Returns the extremity on which this Endcut is applied to.
                |     values:
                |     1: Start Extremity
                |     2: End Extremity
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Extremity of the Endcut.
                |              
                | 
                |              Dim ObjStrEndCut As StrEndCut
                |              Set ObjStrEndCut = ObjStrEndcutMngt.AddEndCut(1)
                |              Extr = ObjStrEndcut.GetExtremity

        :return: int
        """
        return self.com_object.GetExtremity()

    def __repr__(self):
        return f'StrEndcut(name="{ self.name }")'
