"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_access.plm_searches import PLMSearches


class PLMSearchService(Service):

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
                |                         PLMSearchService
                | 
                | 
                | Deprecated:
                |     R216 Use SearchService instead. Interface representing the service to get a
                |     new PLMSearch object.
                | 
                |     Example of how to retrieve such an object using
                |     Application.GetSessionService:
                | 
                |      Dim aSearchSrv as PLMSearchService
                |      Set aSearchSrv = CATIA.GetSessionService("PLMSearch")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def searches(self) -> PLMSearches:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Searches() As PLMSearches (Read Only)
                |     Returns the collection of the PLM Searches currently managed by the
                |     PLMSearch service.

        :return: PLMSearches
        """

        return PLMSearches(self.com_object.Searches)

    def __repr__(self):
        return f'PlmSearchService(name="{ self.name }")'
