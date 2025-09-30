"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Person(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Person
                | 
                | Represents the current connected Person.
                | Role: Allows getting current session information about the current connected
                | Person.
                | 
                | Example:
                | 
                |      This example shows how to retrieve the current connected Person from the
                |      PnOService service.
                |      
                | 
                |      Dim zePnOService as PnOService
                |      Set zePnOService = CATIA.GetSessionService("PnOService") 
                |      Dim zePerson as Person
                |      Set zePerson = zePnOService.Person
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def collaborative_space_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CollaborativeSpaceID() As CATBSTR (Read Only)
                |     Returns the Collaborative Space ID of the connected
                |     Person.
                | 
                |     Example:
                | 
                |          This example shows how to retrieve the Collaborative Space ID of the
                |          connected Person.
                |          
                | 
                |          Dim zeCollaborativeSpaceID As String
                |          Set zeCollaborativeSpaceID = zePerson.CollaborativeSpaceID

        :return: str
        """

        return self.com_object.CollaborativeSpaceID

    @property
    def organization_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrganizationID() As CATBSTR (Read Only)
                |     Returns the Organization ID of the connected Person.
                | 
                |     Example:
                | 
                |          This example shows how to retrieve the Organization ID of the
                |          connected Person.
                |          
                | 
                |          Dim zeOrganizationID As String
                |          Set zeOrganizationID = zePerson.OrganizationID

        :return: str
        """

        return self.com_object.OrganizationID

    @property
    def person_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PersonID() As CATBSTR (Read Only)
                |     Returns the Person ID of the connected Person.
                | 
                |     Example:
                | 
                |          This example shows how to retrieve the Person ID of the connected
                |          Person.
                |          
                | 
                |          Dim zePersonID As String
                |          Set zePersonID = zePerson.PersonID

        :return: str
        """

        return self.com_object.PersonID

    @property
    def role_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RoleID() As CATBSTR (Read Only)
                |     Returns the Role ID of the connected Person.
                | 
                |     Example:
                | 
                |          This example shows how to retrieve the Role ID of the connected
                |          Person.
                |
                |          Dim zeRoleID As String
                |          Set zeRoleID = zePerson.RoleID
        :return: str
        """

        return self.com_object.RoleID

    def __repr__(self):
        return f'Person(name="{ self.name }")'
