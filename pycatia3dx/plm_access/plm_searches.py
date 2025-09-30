"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_access.plm_search import PLMSearch
from pycatia3dx.types.general import CATVariant


class PLMSearches(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMSearches
                | 
                | 
                | Deprecated:
                |     R216 Use SearchService and related interfaces instead. Interface
                |     representing a collection of PLMSearch objects. Interactively it corresponds to
                |     the tab pages available in the PLM Search result window.
                | 
                |     Example of how to retrieve such an object:
                | 
                |      Dim aSearchSrv as PLMSearchService
                |      Set aSearchSrv = CATIA.GetSessionService("PLMSearch")
                |      Dim cPLMSearches as PLMSearches
                |      Set cPLMSearches = aSearchSrv.Searches
                |      
                | 
                |     PLMSearchService.Searches.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def current(self) -> PLMSearch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Current() As PLMSearch
                |     Returns (and sets) the current PLMSearchContext. Interactively, it enables
                |     the activation of the related tab page.
                | 
                |     Returns:
                |         The current PLMSearchContext 
                |     Example:
                | 
                |             This example retrieves the current oPLMSearchContext PLM
                |             Search
                |             from the cPLMSearchContexts collection.
                |             
                | 
                |             Set oPLMSearchContext = cPLMSearchContexts.Current

        :return: PLMSearch
        """

        return PLMSearch(self.com_object.Current)

    @current.setter
    def current(self, value: PLMSearch):
        """
        :param PLMSearch value:
        """

        self.com_object.Current = value

    def add(self) -> PLMSearch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As PLMSearch
                |     Creates a PLMSearchContext and adds it to the PLMSearchContexts collection.
                |     Interactively, a new tab page is created in the PLM Search result
                |     window.
                | 
                |     Returns:
                |         The created PLMSearchContext 
                |     Example:
                | 
                |             This example creates a new PLMSearchContext in the
                |             cPLMSearchContexts collection.
                |             
                | 
                |             Set oPLMSearchContext = cPLMSearchContexts.Add

        :return: PLMSearch
        """
        return PLMSearch(self.com_object.Add())

    def item(self, i_index: CATVariant) -> PLMSearch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As PLMSearch
                |     Returns a PLMSearchContext using its index or its name from the
                |     PLMSearchContexts collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the PLMSearchContext to retrieve from the
                |             collection of PLMSearchContexts. As a numerics, this index is the rank of the
                |             PLMSearchContexts in the collection. The index of the first PLMSearchContext in
                |             the collection is 1, and the index of the last PLMSearchContext is Count. As a
                |             string, it is the name you assigned to the PLMSearchContext.
                |             
                | 
                |     Returns:
                |         The retrieved PLMSearchContext 
                |     Example:
                | 
                |             This example retrieves in oThisPLMSearchContext the ninth
                |             PLMSearchContext,
                |             and in oThatPLMSearchContext the PLMSearchContext
                |             named
                |             PLMSearchContext3 from the cPLMSearchContexts collection.
                |             
                |             
                | 
                |             Set oThisPLMSearchContext = cPLMSearchContexts.Item(9)
                |             Set oThatPLMSearchContext = cPLMSearchContexts.Item("PLMSearchContext3")

        :param CATVariant i_index:
        :return: PLMSearch
        """
        return PLMSearch(self.com_object.Item(i_index))

    def remove(self, i_plm_search_context: PLMSearch) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(PLMSearch iPLMSearchContext)
                |     Removes a PLMSearchContext from the PLMSearchContexts collection.
                |     Interactively, Closes the related tab page.
                | 
                |     Parameters:
                | 
                |         iPLMSearchContext
                |             The PLMSearchContext to retrieve from the collection of
                |             PLMSearchContexts.

        :param PLMSearch i_plm_search_context:
        :return: None
        """
        return self.com_object.Remove(i_plm_search_context.com_object)

    def __repr__(self):
        return f'PlmSearches(name="{ self.name }")'
