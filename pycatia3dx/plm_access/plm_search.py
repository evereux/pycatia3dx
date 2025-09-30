"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.plm_application_context.plm_app_context import PLMAppContext


class PLMSearch(PLMAppContext):

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
                |                        PLMApplicationContextIDLItf.PLMAppContext
                |                             PLMSearch
                | 
                | 
                | Deprecated:
                |     R216 Use SearchService and related interfaces instead. Interface
                |     representing a PLMSearch object. Interactively it corresponds to a tab page in
                |     the PLM Search result window.
                | 
                | 
                |     Role: Define the attribute criteria and trigger a Search in
                |     database.
                | 
                |     Example of how to create a new Search from PLMSearches
                |     collection:
                | 
                |      Dim aSearchSrv as PLMSearchService
                |      Set aSearchSrv = CATIA.GetSessionService("PLMSearch")
                |      Dim cPLMSearches as PLMSearches
                |      Set cPLMSearches = aSearchSrv.Searches
                |      Dim aPLMSearch as PLMSearch
                |      Set aPLMSearch = cPLMSearches.Add
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def editor(self) -> Editor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Editor() As Editor (Read Only)
                |     Returns the editor associated with the current tab page. The editor gathers
                |     the results of the search.
                | 
                |     Example:
                | 
                |             This example retrieves PLMEntities collection representing the
                |             results of the Search:
                |             
                | 
                |             ...
                |             Dim aPLMSearch As PLMSearch
                |             ...
                |             aPLMSearch.Search()
                |            
                |             Dim cPLMEntities As PLMEntities
                |             Dim cPLMEntities = aPLMSearch.EditedContent

        :return: Editor
        """

        return Editor(self.com_object.Editor)

    @property
    def type(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type(CATBSTR iTypeBSTR) (Write Only)
                |     Returns or sets the type of objects to search for.

        :return: False
        """

        return None

    @type.setter
    def type(self, value: False):
        """
        :param False value:
        """

        self.com_object.Type = value

    def add_attribute_criteria(self, i_attr_id_bstr: str, i_attr_value_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddAttributeCriteria(CATBSTR iAttrIdBSTR,CATBSTR
                | iAttrValueBSTR)
                |     Add an attribute criteria to the query considering that:
                | 
                |         An attributes is identified by a string and should be only of string
                |         type
                |         A value is a string
                |         Wildcard '*' is supported in attribute value

        :param str i_attr_id_bstr:
        :param str i_attr_value_bstr:
        :return: None
        """
        return self.com_object.AddAttributeCriteria(i_attr_id_bstr, i_attr_value_bstr)

    def search(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Search()
                |     Triggers the search. All attributes are combined through a "AND" condition,
                |     thus leading to a search of objects which match all the attributes of the set
                |     and matching the case of the values (i.e. search is case sensitive). If
                |     attribute value does not contain any wildcard objects have to match
                |     exactly.
                | 
                |     Example:
                | 
                |             This example retrieves the objects matching all the following
                |             constraints:
                |
                |             attribute Attr1 is strictly equal to val1
                |             attribute Attr2 starts with val2
                |             attribute Attr3 ends with val3
                |             attribute Attr4 contains val4
                |             Dim aPLMSearch As PLMSearch
                |             ...
                |             aPLMSearch.AddAttributeCriteria ("Attr1", "val1")
                |             aPLMSearch.AddAttributeCriteria ("Attr2", "val2*")
                |             aPLMSearch.AddAttributeCriteria ("Attr3", "*val3")
                |             aPLMSearch.AddAttributeCriteria ("Attr4",
                |             "*val4*")
                |             aPLMSearch.Search()

        :return: None
        """
        return self.com_object.Search()

    def __repr__(self):
        return f'PlmSearch(name="{ self.name }")'
