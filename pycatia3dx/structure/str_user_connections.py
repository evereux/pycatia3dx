"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_user_connection import StrUserConnection
from pycatia3dx.types.general import CATVariant


class StrUserConnections(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrUserConnections
                | 
                | Object for StrUserConnections
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrUserConnection)
        self.com_object = com_object

    def add(self) -> StrUserConnection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrUserConnection
                |     Returns the UserConnection created under this Member.
                | 
                |     Example:
                | 
                | 
                |              This example creates a UserConnection.
                |              
                | 
                |               Dim ObjStrUserConnections As StrUserConnections
                |               Set ObjStrUserConnections = ObjSfdMember.StrUserConnections
                |               Dim ObjUserConnection As StrUserConnection
                |               Set ObjUserConnection = ObjStrUserConnections.Add

        :return: StrUserConnection
        """
        return StrUserConnection(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrUserConnection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrUserConnection
                |     Returns a StrUserConnection
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrUserConnection
                | 
                |         Example:
                | 
                | 
                |                  This example retrieves in first UserConnection from the list
                |                  of UserConnections.
                |                  
                | 
                |                   'Get all created UserConnections on the
                |                   object
                |                   Dim ObjStrUserConnections As
                |                   StrUserConnections
                |                   Set ObjStrUserConnections = ObjStrUserConnectionMngt.GetUserConnections
                |                   'Get first UserConnection from the list of
                |                   UserConnections
                |                   Dim ObjStrUserConnection As
                |                   StrUserConnection
                |                   set ObjStrUserConnection = ObjStrUserConnections.Item(1)

        :param CATVariant i_index:
        :return: StrUserConnection
        """
        return StrUserConnection(self.com_object.Item(i_index))

    def remove(self, i_user_connection: StrUserConnection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrUserConnection iUserConnection)
                |     Removes the UserConnection of this Member.
                | 
                |     Parameters:
                | 
                |         iUserConnection
                |             UserConnection.
                | 
                |         Example:
                | 
                | 
                |                  This example removes the UserConnection.
                |                  
                | 
                |                   ObjStrUserConnections.Remove
                |                   ObjUserConnection

        :param StrUserConnection i_user_connection:
        :return: None
        """
        return self.com_object.Remove(i_user_connection.com_object)

    def __repr__(self):
        return f'StrUserConnections(name="{self.name}")'
