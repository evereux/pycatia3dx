"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.system.any_object import AnyObject


class DatabaseSearch(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatabaseSearch
                | 
                | Interface representing a Search object.
                | Interactively it corresponds to a tab page in the Search
                | browser.
                | 
                | 
                | Role: Define the attribute criteria and trigger a Search in
                | database.
                | 
                | Example of how to create a new DatabaseSearch from
                | CATIASearchService:
                | 
                |  Dim aSearchSrv as SearchService
                |  Set aSearchSrv = CATIA.GetSessionService("Search") 
                |  Dim aDBSearch as DatabaseSearch
                |  Set aDBSearch = aSearchSrv.DatabaseSearch
                |  You can add the different criteria on this object to prepare your
                |  search.
                |  Finally call 
                | SearchService.Search to execute the search and bring the results.
                | Note : Trying to get another DatabaseSearch on the same SearchService
                | instance is not allowed.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_minor_versions(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllMinorVersions(long iAllMinorVersions) (Write Only)
                | 
                |     Role: Specifies if search should return the All Minor version of an
                |     object.
                | 
                |     Parameters:
                | 
                |         iLatestVersion
                |             iAllMinorVersions = 1 : search will return All Minor versions
                |             iAllMinorVersions = 0 : search BSF version only
                | 
                |     Returns:
                | 
                |         S_OKAllMinorVersions criteria was successfully set

        :return: None
        """

        return None

    @all_minor_versions.setter
    def all_minor_versions(self, value: int):
        """
        :param int value:
        """

        self.com_object.AllMinorVersions = value

    @property
    def base_type(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BaseType(CATBSTR iBaseType) (Write Only)
                | 
                |     Role: Sets the type of object to search for, the string must be an internal
                |     name of the type
                | 
                |     Parameters:
                | 
                |         iBaseType
                |             Type of the object 
                | 
                |     Returns:
                | 
                |         S_OKType was successfully set
                |         E_INVALIDARGCould not find the model type corresponding to the input
                |         type


        :return: None
        """

        return None

    @base_type.setter
    def base_type(self, value: str):
        """
        :param str value: common types "VPMReference" (Physical Product), "3DShape" (Part), "Drawing", "Document" (Excel/Text)
        """

        self.com_object.BaseType = value

    @property
    def condition(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Condition(SearchCondition iCondition) (Write Only)
                | 
                |     Role: Sets the condition to use between attribute criteria Applicable only
                |     for Extended mode.
                | 
                |     Parameters:
                | 
                |         iCondition
                | 
                |     Returns:
                | 
                |         S_OKCondition was successfully set
                |         E_FAILSearch mode is not Extended mode

        :return: None
        """

        return None

    @condition.setter
    def condition(self, value: int):
        """
        :param int value:
        """

        self.com_object.Condition = value

    @property
    def extension(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Extension(CATBSTR iExtension) (Write Only)
                | 
                |     Role: Sets the extension type of object to search for, the string must be
                |     an internal name of the extension
                | 
                |     Parameters:
                | 
                |         iExtension
                |             Extension of the base type 
                | 
                |     Returns:
                | 
                |         S_OKExtension was successfully set
                |         E_FAILCould not find the model type corresponding to the input type or
                |         input type is not an extension

        :return: None
        """

        return None

    @extension.setter
    def extension(self, value: str):
        """
        :param str value:
        """

        self.com_object.Extension = value

    @property
    def latest_version(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LatestVersion(long iLatestVersion) (Write Only)
                | 
                |     Role: Specifies if search should return the latest version of an
                |     object.
                | 
                |     Parameters:
                | 
                |         iLatestVersion
                |             iLatestVersion = 1 : search will return the latest version iLatestVersion = 0 : normal search 
                | 
                |     Returns:
                | 
                |         S_OKLatestVersion criteria was successfully set

        :return: None
        """

        return None

    @latest_version.setter
    def latest_version(self, value: int):
        """
        :param int value:
        """

        self.com_object.LatestVersion = value

    @property
    def mode(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode(SearchMode iMode) (Write Only)
                | 
                |     Role: Sets the mode of the search
                | 
                |     Parameters:
                | 
                |         iMode
                |             Mode of the search, see enum CATIASearchEnum.SearchMode
                |             
                | 
                |     Returns:
                | 
                |         S_OKMode was set correctly

        :return: None
        """

        return None

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def page_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PageCount() As long (Read Only)
                | 
                |     Role: Returns the total number of search fetch query calls required to
                |     retrieve all search results from the server. This call must be done after
                |     SearchService.Search is done to execute the search.
                | 
                |     Parameters:
                | 
                |         page
                |             Number of pages 
                | 
                |     Returns:
                | 
                |         S_OKOn Sucess
                |         E_FAILFailed to get the search count

        :return: int
        """

        return self.com_object.PageCount

    @property
    def results(self) -> PLMEntities:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Results() As PLMEntities (Read Only)
                | 
                |     Role: Get the search results fetched till now. This call must be done after
                |     SearchService.Search is done to execute the search.
                | 
                |     Parameters:
                | 
                |         oResults
                |             Search results 
                | 
                |     Returns:
                | 
                |         S_OKAll the displayed results were retrieved successfully from the
                |         Search Browser
                |         E_FAILFailed to get the results from the Search
                |         Browser

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
                | 
                |     Role: Returns the total count of objects found matching the search criteria.
                |     NOTE : Search results are retrieved from server in form of "fetch page"(s) of size 50 each.
                |     By default only results of first page are displayed in the UI (i.e. max 50)
                |     Search count is the total no. of results avaialable for the given criteria.
                |     This call must be done after SearchService.Search is done to execute the
                |     search.
                | 
                |     Parameters:
                | 
                |         oSearchCount
                |             Search count 
                | 
                |     Returns:
                | 
                |         S_OKOn Sucess
                |         E_FAILFailed to get the search count

        :return: int
        """

        return self.com_object.SearchCount

    @property
    def title(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Title(CATBSTR iTitle) (Write Only)
                |     Sets the title of the tab in the search browser displaying results of this
                |     search

        :return: None
        """

        return None

    @title.setter
    def title(self, value: str):
        """
        :param str value:
        """

        self.com_object.Title = value

    def add_easy_criteria(self, i_attr_id: str, i_attr_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddEasyCriteria(CATBSTR iAttrId,CATBSTR iAttrValue)
                | 
                |     Role: Add an attribute criteria to the query Applicable only in case of
                |     Easy mode, see enum CATIASearchEnum.SearchMode. Operator used the first
                |     applicable operator depending upon the attribute type
                | 
                |     Parameters:
                | 
                |         iAttrId
                |             Attribute Id, it must belong to the EZQuery mask 
                |         iAttrValue
                |             Attribute value 
                | 
                |     Returns:
                | 
                |         S_OKAttribute criteria was successfully added
                |         E_FAILWhen Easy mode is not set
                |         E_INVALIDARGType is not set or attribute not found on the EZ query mask
                |         either for type or extension

        :param str i_attr_id:
        :param str i_attr_value:
        :return: None
        """
        return self.com_object.AddEasyCriteria(i_attr_id, i_attr_value)

    def add_extended_criteria(self, i_attr_id: str, i_attr_value: str, i_operator: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddExtendedCriteria(CATBSTR iAttrId,CATBSTR iAttrValue,SearchOperator
                | iOperator)
                | 
                |     Role: Add an attribute criteria to the query Applicable only in case of
                |     Extended mode, see enum CATIASearchEnum.SearchMode.
                | 
                |     Parameters:
                | 
                |         iAttrId
                |             Attribute Id, it must belong to the Query mask 
                |         iAttrValue
                |             Attribute value 
                |         iOperator
                |             See enum CATIASearchEnum#SearchOperator, note that available
                |             operators depend upon the type of the attribute To know the available operators
                |             refer to the "Extended" tab of "Advanced Search" UI Range operators (BETWEEN
                |             and NOT_BETWEEN) are not supported by this call, instead use
                |             #AddExtenedRangeCriteria 
                | 
                |     Returns:
                | 
                |         S_OKAttribute criteria was successfully added
                |         E_FAILWhen Extended mode is not set or range operator is given as
                |         input
                |         E_INVALIDARGType is not set or attribute not found on the Query mask
                |         either for type or extension or input operator not applicable to use with the
                |         attribute

        :param str i_attr_id:
        :param str i_attr_value:
        :param int i_operator:
        :return: None
        """
        return self.com_object.AddExtendedCriteria(i_attr_id, i_attr_value, i_operator)

    def add_extended_range_criteria(
            self,
            i_attr_id: str,
            i_attr_start_value: str,
            i_attr_end_value: str,
            i_operator: int
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddExtendedRangeCriteria(CATBSTR iAttrId,CATBSTR iAttrStartValue,CATBSTR
                | iAttrEndValue,SearchOperator iOperator)
                | 
                |     Role: Add an attribute criteria in form of range to the query. Applicable
                |     only in case of Extended mode, see enum
                |     CATIASearchEnum.SearchMode.
                | 
                |     Parameters:
                | 
                |         iAttrId
                |             Attribute Id, it must belong to the Query mask 
                |         iAttrValue
                |             Attribute value 
                |         iOperator
                |             It must be either BETWEEN or NOT_BETWEEN, See enum
                |             CATIASearchEnum.SearchOperator 
                | 
                |     Returns:
                | 
                |         S_OKAttribute criteria was successfully added
                |         E_FAILWhen Extended mode is not set or range operator is not given as
                |         input
                |         E_INVALIDARGType is not set or attribute not found on the Query mask
                |         either for type or extension or input operator not applicable to use with the
                |         attribute

        :param str i_attr_id:
        :param str i_attr_start_value:
        :param str i_attr_end_value:
        :param int i_operator:
        :return: None
        """
        return self.com_object.AddExtendedRangeCriteria(i_attr_id, i_attr_start_value, i_attr_end_value, i_operator)

    def add_predefined_criteria(self, i_criteria_with_pq_abbreviation: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPredefinedCriteria(CATBSTR iCriteriaWithPQAbbreviation)
                | 
                |     Role: Add a criteria With a PQ Abbreviation, e.g "prd:MyProduct" Applicable
                |     only in case of Predefined mode, see enum
                |     CATIASearchEnum.SearchMode.
                | 
                |     Parameters:
                | 
                |         iCriteriaWithPQAbbreviation
                |             Criteria With a PQ Abbreviation, e.g "prd:MyProduct" The input
                |             string must contain an abbreviation seperated from the criteria by ":" The PQ
                |             abbreviation (i.e. "prd" in above example) is NLS compliant, so same script
                |             must be modified to use on another language OS. 
                | 
                |     Returns:
                | 
                |         S_OKCriteria was successfully added
                |         E_FAILWhen Predefined mode is not set
                |         E_INVALIDARGInput string is not in good format, or input abbreviation
                |         is invalid

        :param str i_criteria_with_pq_abbreviation:
        :return: None
        """
        return self.com_object.AddPredefinedCriteria(i_criteria_with_pq_abbreviation)

    def next_page(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub NextPage()
                | 
                |     Role: Fetch the results of next page, these results are appended to the
                |     existing results. This call must be done after SearchService.Search is done to
                |     execute the search.
                | 
                |     Returns:
                | 
                |         S_OKResults of next page were fetched successfully
                |         E_FAILFailed to get the next page of results
                |         E_INVALIDARGAsking for next page after end page is already
                |         reached

        :return: None
        """
        return self.com_object.NextPage()

    def set_expert_expression(self, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExpertExpression(CATBSTR iExpression)
                | 
                |     Role: Set the expression to use for the search. Applicable only in case of
                |     Expert mode, see enum CATIASearchEnum.SearchMode.
                | 
                |     Parameters:
                | 
                |         iExpression
                |             Query Expression to use. You can directly copy an expression from
                |             the "Expert" tab of the "Adavnced Search" UI and uset it here. It is an NLS
                |             compliant expressio so same script must be modified to use on another language
                |             OS. 
                | 
                |     Returns:
                | 
                |         S_OKExpression was successfully set.
                |         E_FAILExpert mode is not set

        :param str i_expression:
        :return: None
        """
        return self.com_object.SetExpertExpression(i_expression)

    def sort_by(self, i_sort_by_attr: str, i_sort_order: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SortBy(CATBSTR iSortByAttr,SearchSortOrder iSortOrder)
                | 
                |     Role: Sets the sort definition for search results.
                | 
                |     Parameters:
                | 
                |         iSortByAttr
                |             The attribute to use for sorting the results 
                |         iSortOrder
                |             The sort order, see CATIASearchEnum#SearchSortOrder
                |             
                | 
                |     Returns:
                | 
                |         S_OKSort definition was successfully added
                |         E_FAILBase type for search is not set, or attribute does not belong to
                |         either type or extension

        :param str i_sort_by_attr:
        :param int i_sort_order:
        :return: None
        """
        return self.com_object.SortBy(i_sort_by_attr, i_sort_order)

    def __repr__(self):
        return f'DatabaseSearch(name="{self.name}")'
