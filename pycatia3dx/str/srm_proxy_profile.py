"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.srm_planning_break import SrmPlanningBreak
from pycatia3dx.str.structure_profile import StructureProfile


class SrmProxyProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrmProxyProfile
                | 
                | Object to manage the Proxy Profile.
                | Planning breaks are treated similar like limits.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_location(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLocation() As long
                |     Returns the proxy profile location. Return Values
                |     1 : IN.
                |     2 : OUT.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the location of
                |              SrmProxyProfile.
                |              
                | 
                |               Dim ObjSrmProxyProfile As SrmProxyProfile
                |               Set ObjSrmProxyProfile = ObjSrmProxyProfiles.Item(1)
                |               Location = ObjSrmProxyProfile.GetLocation

        :return: int
        """
        return self.com_object.GetLocation()

    def get_planning_breaks(self, o_start_pb: SrmPlanningBreak, o_end_pb: SrmPlanningBreak) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPlanningBreaks(SrmPlanningBreak oStartPB,SrmPlanningBreak
                | oEndPB)
                |     Returns the planning breaks under the Proxy Profile.
                | 
                |     Parameters:
                | 
                |         oStartPB
                |             output Start Planning Break. 
                |         oEndPB
                |             output End Planning Break.

        :param SrmPlanningBreak o_start_pb:
        :param SrmPlanningBreak o_end_pb:
        :return: None
        """
        return self.com_object.GetPlanningBreaks(o_start_pb.com_object, o_end_pb.com_object)

    def get_profile(self) -> StructureProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfile() As StructureProfile
                |     Returns the Profile pointed by the proxy. 

        :return: StructureProfile
        """
        return StructureProfile(self.com_object.GetProfile())

    def __repr__(self):
        return f'SrmProxyProfile(name="{ self.name }")'
