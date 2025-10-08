"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.sfd_connection_set import SfdConnectionSet
from pycatia3dx.structure.str_sfd_project_data import StrSfdProjectData


class SfdPart(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdPart
                | 
                | Object to manage attributes on the Part.
                | Role: To manage attributes on the Part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_connections_set(self) -> SfdConnectionSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConnectionsSet() As SfdConnectionSet
                |     Returns the ConnectionSet under the part.
                | 
                |     Example:
                | 
                | 
                |              This example returns the ConnectionSet under the
                |              part.
                |              
                | 
                |               Dim ObjSfdConnectionsSet As SfdConnectionSet
                |               Set ObjSfdConnectionsSet = ObjSfdPart.GetConnectionsSet

        :return: SfdConnectionSet
        """
        return SfdConnectionSet(self.com_object.GetConnectionsSet())

    def get_project_data(self) -> StrSfdProjectData:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProjectData() As StrSfdProjectData
                |     Returns the ProjectData tool.
                | 
                |     Example:
                | 
                | 
                |              This example returns the project data of this SFD
                |              part.
                |              
                | 
                |               Dim ProjectData As SfdProjectData
                |               Set ProjectData = ObjSfdPart.GetProjectData

        :return: StrSfdProjectData
        """
        return StrSfdProjectData(self.com_object.GetProjectData())

    def is_sfd_system(self, o_diagnostic: int, o_incorrect_discipline_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsSFDSystem(long oDiagnostic,CATBSTR
                | oIncorrectDisciplineName)
                |     Verifies that the reference has the correct V_Discipline
                |     value.
                | 
                |     Parameters:
                | 
                |         oDiagnostic
                |             Project data tool. 
                |         oIncorrectDisciplineName
                |             Returns the V_Discipline if there is already one. 
                | 
                |     Example:
                | 
                | 
                |              This example checks whether this system is SFD or
                |              not.
                |              
                | 
                |               Dim Diagnosis As Long
                |               Dim oIncorrectDiscName As String
                |               ObjSfdPart.IsSFDSystem Diagnosis,
                |               oIncorrectDiscName

        :param int o_diagnostic:
        :param str o_incorrect_discipline_name:
        :return: None
        """
        return self.com_object.IsSFDSystem(o_diagnostic, o_incorrect_discipline_name)

    def set_as_sfd_system(self, o_diagnostic: int, o_incorrect_discipline_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAsSFDSystem(long oDiagnostic,CATBSTR
                | oIncorrectDisciplineName)
                |     Initiliazes the Reference as a SFD system by setting the
                |     V_Discipline.
                | 
                |     Parameters:
                | 
                |         oDiagnostic
                | 
                |             0 - V_discipline was successfully set for SFD.
                |             1 - V_discipline is already set for SFD.
                |             2 - V_discipline set not succeeded.
                |             3 - V_discipline set not succeeded.
                |             4 - V_discipline set not succeeded.
                |             5 - V_discipline set not succeeded. 
                |         oIncorrectDisciplineName
                |             Returns the V_Discipline if there is already one. 
                | 
                |     Example:
                | 
                | 
                |              This example sets this system to SFD system.
                |              
                | 
                |               Dim ObjSfdPart As SfdPart
                |               ObjSelection.Add ObjPart
                |               Set ObjSfdPart = ObjSelection.FindObject("CATIASfdPart")
                |               Dim Diagnosis As Long
                |               Dim oIncorrectDiscName As String
                |               ObjSfdPart.SetAsSFDSystem Diagnosis,
                |               oIncorrectDiscName

        :param int o_diagnostic:
        :param str o_incorrect_discipline_name:
        :return: None
        """
        return self.com_object.SetAsSFDSystem(o_diagnostic, o_incorrect_discipline_name)

    def __repr__(self):
        return f'SfdPart(name="{self.name}")'
