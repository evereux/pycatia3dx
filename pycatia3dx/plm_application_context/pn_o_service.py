"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_application_context.person import Person


class PnOService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PnOService
                | 
                | Represents the service to access the current connected Person.
                | 
                | Example:
                | 
                |      This example shows how to retrieve the PnO Service.
                |      
                | 
                |       Dim zePnOService as PnOService
                |       Set zePnOService = CATIA.GetSessionService("PnOService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def person(self) -> Person:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Person() As Person (Read Only)
                |     Returns a Person object that represents the current connected
                |     Person.
                | 
                |     Example:
                | 
                |          This example shows how to retrieve the current connected
                |          Person.
                |          
                | 
                |          Dim zePerson as Person
                |          Set zePerson = zePnOService.Person

        :return: Person
        """

        return Person(self.com_object.Person)

    def __repr__(self):
        return f'PnOService(name="{ self.name }")'
