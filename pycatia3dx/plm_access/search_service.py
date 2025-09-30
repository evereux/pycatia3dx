"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_access.database_search import DatabaseSearch


class SearchService(Service):

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
                |                         SearchService
                | 
                | This Interface is starting point to automate the search.
                | 
                | Example of how to retrieve such an object using
                | Application.GetSessionService:
                | 
                |   Dim aSearchSrv as SearchService
                |   Set aSearchSrv = CATIA.GetSessionService("Search")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def database_search(self) -> DatabaseSearch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DatabaseSearch() As DatabaseSearch (Read Only)
                |     Returns a Search object that can prepare search with the database. This
                |     provides APIs to simulate the "Advanced Search" provided in the UI.

        :return: DatabaseSearch
        """

        return DatabaseSearch(self.com_object.DatabaseSearch)

    @property
    def title(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Title(CATBSTR iTitle) (Write Only)
                |     Sets the title of the Search Browser.

        :return: False
        """

        return None

    @title.setter
    def title(self, value: False):
        """
        :param False value:
        """

        self.com_object.Title = value

    def search(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Search()
                |     Launch the Search and display the results in the Search Browser.

        :return: None
        """
        return self.com_object.Search()

    def __repr__(self):
        return f'SearchService(name="{ self.name }")'
