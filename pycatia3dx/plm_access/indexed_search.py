"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.system.any_object import AnyObject


class IndexedSearch(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     IndexedSearch
                | 
                | Represents indexed search object.
                | Role IndexedSearch is used for doing search in 3DSpace index only. It will not
                | display results in the 3DSearch browser. This works with how the 3DSpace data
                | index is build out of the box, or as customized. As the index is built with
                | certain lag, index search results may differ from the real time search
                | (database search).
                | 
                | Search is case insensitive.
                | This example shows getting IndexedSearch from a searchService
                | object.
                | 
                | Example:
                | 
                |      Dim searchService As searchService
                |      Set searchService = CATIA.GetSessionService("Search")
                |      Dim IndexedSearch As IndexedSearch
                |      Set IndexedSearch = searchService.GetItem("IndexedSearch")
                |      IndexedSearch.Types = "VPMReference , 3DShape , Material Part"
                |      IndexedSearch.Predicate "ds6w:label", "prd*"
                |      IndexedSearch.Predicate "ds6w:description", "test"
                |      IndexedSearch.MaxSearchResultCount = 60
                |      IndexedSearch.SortBy "ds6w:label",
                |      SearchSortOrder_Ascending
                |      IndexedSearch.SortBy "ds6w:created",
                |      SearchSortOrder_Descending
                |      IndexedSearch.Search
                |      Dim oResults As PLMEntities
                |      Set oResults = IndexedSearch.Results
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def extensions(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Extensions(CATBSTR iExtension) (Write Only)
                |     Sets the PLM object extensions to search for.
                |     Role:Only the PLM objects having one the specified extension type are
                |     returned. If invalid extension in list, then results will be listed only for
                |     valid extensions. Sets extension only if exactly 1 PLM object type is set. If
                |     more than 1 types set or extension types does not exists, extension call is
                |     ignored. If called multiple times, it will overwrite last
                |     values.
                | 
                |     Parameters:
                | 
                |         iExtension
                |             Extensions of the base type. It is string containing list of
                |             extension types seperated by comma. Extension type is referenced as internal
                |             type.

        :return: False
        """

        return None

    @extensions.setter
    def extensions(self, value: False):
        """
        :param False value:
        """

        self.com_object.Extensions = value

    @property
    def max_search_result_count(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxSearchResultCount(long iMaxResultCount) (Write
                | Only)
                |     Sets maximum count of results to be retrieved.
                | 
                |     Parameters:
                | 
                |         iMaxResultCount
                |             Maximum count of results to retrieve. The default value is 40. The
                |             maximum is 200. If set greater than 200 , then it is taken as 200.

        :return: False
        """

        return None

    @max_search_result_count.setter
    def max_search_result_count(self, value: False):
        """
        :param False value:
        """

        self.com_object.MaxSearchResultCount = value

    @property
    def results(self) -> PLMEntities:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Results() As PLMEntities (Read Only)
                |     Returns a limited list of PLM Objects matching search
                |     criteria.
                |     Role:The property returns a possibly limited list of PLM objects matching
                |     the search criteria. The real count of elements matching the search criteria in
                |     the indexed database is returned by IndexedSearch.get_SearchCount. This call
                |     must be done after IndexedSearch.Search.
                | 
                |     Parameters:
                | 
                |         oResults
                |             Search results

        :return: PLMEntities
        """

        return PLMEntities(self.com_object.Results)

    @property
    def search_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SearchCount() As long (Read Only)
                |     Returns the total count of indexed PLM objects matching the search
                |     criteria.
                |     Role:The count of PLM elements returned by IndexedSearch.Search method is
                |     limited as explained by the IndexedSearch.put_MaxSearchResultCount. This call
                |     returns the exact count of PLM elements existing in the indexed database and
                |     matching the search criteria. This call must be done after
                |     IndexedSearch.Search.
                | 
                |     Parameters:
                | 
                |         oSearchCount
                |             Search count

        :return: int
        """

        return self.com_object.SearchCount

    @property
    def types(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Types(CATBSTR iBaseType) (Write Only)
                |     Sets PLM object types to search for. If called multiple times, it will
                |     overwrite last values.
                | 
                |     Parameters:
                | 
                |         iBaseType
                |             It is a string containing a list of PLM object types, each one
                |             separated by a comma. A type is referenced by its internal name.

        :return: False
        """

        return None

    @types.setter
    def types(self, value: False):
        """
        :param False value:
        """

        self.com_object.Types = value

    def predicate(self, i_predicate: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Predicate(CATBSTR iPredicate,CATBSTR iValue)
                |     Adds search criterion based on 6W predicate value. You can call method
                |     multiple times for same predicate if want to set multiple
                |     values.
                | 
                |     Parameters:
                | 
                |         iPredicate
                |             The 6W predicate name with its 6w format. For eg. ds6w:label
                |             
                |         iValue
                |             The 6W predicate value.

        :param str i_predicate:
        :param str i_value:
        :return: None
        """
        return self.com_object.Predicate(i_predicate, i_value)

    def search(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Search()
                |     Launches the search with 3DSpace index.
                |     Role:The search logic is:
                | 
                |         OR with the PLM types and extension types.
                |         AND between 6W predicates.
                |         OR between same 6W predicate added with multiple
                |         values.
                | 
                |     If the criteria is wrong, the results is an empty list except if one value
                |     criterion is a wrong wildcard string. For the latter case, the method
                |     fails.

        :return: None
        """
        return self.com_object.Search()

    def sort_by(self, i_sort_by_predicate: str, i_sort_order: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SortBy(CATBSTR iSortByPredicate,SearchSortOrder
                | iSortOrder)
                |     Adds 6W predicate and order for sorting search results.
                |     Role:It adds a sorting criterion with a 6W predicate and its order
                |     (ascending or descending). By default sort order is descending for a predicate
                |     defined server side. In case of wrong predicate, results will be ordered only
                |     for right predicates. If method is called with same predicate multiple times,
                |     last value is kept. This method can be called several times (max 3 ) for
                |     multiple sorting criteria.
                | 
                |     Parameters:
                | 
                |         iSortByPredicate
                |             The predicate to use for sorting the results. 
                |         iSortOrder

        :param str i_sort_by_predicate:
        :param int i_sort_order:
        :return: None
        """
        return self.com_object.SortBy(i_sort_by_predicate, i_sort_order)

    def __repr__(self):
        return f'IndexedSearch(name="{ self.name }")'
