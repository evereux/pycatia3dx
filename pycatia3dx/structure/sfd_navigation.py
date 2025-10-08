"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.sfd_panel import SfdPanel
from pycatia3dx.structure.structure_profile import StructureProfile


class SfdNavigation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdNavigation
                | 
                | Object to manage to retrieve the SFD Panel/Profile from any
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_panel(self) -> SfdPanel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPanel() As SfdPanel
                |     Returns the SFD Panel.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example shows how to call GetPanel method
                |              
                | 
                |              Dim ObjSfdNavigation As SfdNavigation
                |              ObjSelection.Add ObjSfdStiffener
                |              Set ObjSfdNavigation = ObjSelection.FindObject("CATIASfdNavigation")
                |              Dim ObjSfdPanel As SfdPanel
                |              Set ObjSfdPanel = ObjSfdNavigation.GetPanel

        :return: SfdPanel
        """
        return SfdPanel(self.com_object.GetPanel())

    def get_profile(self) -> StructureProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfile() As StructureProfile
                |     Returns the SFD Profile. 

        :return: StructureProfile
        """
        return StructureProfile(self.com_object.GetProfile())

    def __repr__(self):
        return f'SfdNavigation(name="{self.name}")'
