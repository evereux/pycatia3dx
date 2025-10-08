"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_connections import StrConnections


class SfdConnectionSet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdConnectionSet
                | 
                | Object to manage the structure object connectivities.
                | Role: To access connections.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_connections(self) -> StrConnections:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConnections() As StrConnections
                |     Returns all the connections from the ConnecionsSet.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in list of connections from the
                |              ConnecionsSet.
                |              
                | 
                |              'Retrieve SfdPart object
                |              Dim ObjSfdPart As SfdPart
                |              ObjSelection.Add (ObjPart)
                |              Set ObjSfdPart = ObjSelection.FindObject("CATIASfdPart")
                |              Dim ObjSfdConnectionSet As SfdConnectionSet
                |              Set ObjSfdConnectionSet = ObjSfdPart.GetConnectionsSet
                |              Set ListOfConnections = ObjSfdConnectionSet.GetConnections

        :return: StrConnections
        """
        return StrConnections(self.com_object.GetConnections())

    def update_connections_set(self, o_updated_cnx: int, o_removed_cnx: int, o_unkown: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UpdateConnectionsSet(long oUpdatedCnx,long oRemovedCnx,long
                | oUnkown)
                |     Updates the connectionsSet.
                | 
                |     Parameters:
                | 
                |         oUpdatedCnx
                |             Output the number of updated connections. 
                |         oRemovedCnx
                |             Output the number of removed connections. 
                |         oUnkown
                |             Output the number of unknown status connections. 
                | 
                |     Example:
                | 
                | 
                |              This example update the ConnecionsSet.
                |              
                | 
                |              ObjSfdConnectionSet.UpdateConnectionsSet UpdatedCnx, RemovedCnx,
                |              UnkStatusCnx

        :param int o_updated_cnx:
        :param int o_removed_cnx:
        :param int o_unkown:
        :return: None
        """
        return self.com_object.UpdateConnectionsSet(o_updated_cnx, o_removed_cnx, o_unkown)

    def __repr__(self):
        return f'SfdConnectionSet(name="{self.name}")'
