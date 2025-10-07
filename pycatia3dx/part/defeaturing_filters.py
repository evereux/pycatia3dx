"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.defeaturing_filter import DefeaturingFilter
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DefeaturingFilters(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DefeaturingFilters
                | 
                | Represents the filter collection of a defeaturing object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_filter_type_to_add: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iFilterTypeToAdd) As long
                |     Creates a new filter and adds it to the Defeaturing filters
                |     collection.
                | 
                |     Parameters:
                | 
                |         iFilterTypeToAdd
                |             The type of the new filter to add among : - "DefeaturingFilletFilter" - "DefeaturingHoleFilter" - or any user-defined filter's type 
                | 
                |     Returns:
                |         oAddedFilterIndex The added filter's index - equals to 0 if
                |         FAILED
                | 
                |         Example:
                |             The following example adds a new filter of type theFilterType to
                |             defeaturing colelction firstDefeaturingFilters and returns the index theIndex
                |             of the new filter
                | 
                |              Set theIndex = firstDefeaturingFilters.Add(theFilterType)

        :param str i_filter_type_to_add:
        :return: int
        """
        return self.com_object.Add(i_filter_type_to_add)

    def item(self, i_filter_id: CATVariant) -> DefeaturingFilter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iFilterId) As DefeaturingFilter
                |     Returns the filter of the Defeaturing filters collection using its index or
                |     its name.
                | 
                |     Parameters:
                | 
                |         iFilterId
                |             The index or the name of the filter to retrieve As a numerics, must
                |             be in [1;Count]) 
                | 
                |     Returns:
                |         oFilter The filter (see DefeaturingFilter for list of possible
                |         actions)
                | 
                |         Example:
                |             The following example returns in myFilter the filter number
                |             theIndex of Defeaturing collection
                |             firstDefeaturingFilters:
                | 
                |              Set myFilter = firstDefeaturingFilters.Item(theIndex)

        :param CATVariant i_filter_id:
        :return: DefeaturingFilter
        """
        return DefeaturingFilter(self.com_object.Item(i_filter_id))

    def remove(self, i_filter_id: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iFilterId)
                |     Removes a filter from the Defeaturing filters collection and deletes it,
                |     using its index or its name.
                | 
                |     Parameters:
                | 
                |         iFilterId
                |             The index or the name of the filter to retrieve As a numerics, must
                |             be in [1;Count])
                | 
                |             Example:
                |                 The two following examples remove the filter number theIndex
                |                 from Defeaturing collection
                |                 firstDefeaturingFilters:
                | 
                |                  Call firstDefeaturingFilters.Remove(theIndex)
                |                  firstDefeaturingFilters.Remove theIndex

        :param CATVariant i_filter_id:
        :return: None
        """
        return self.com_object.Remove(i_filter_id)

    def __repr__(self):
        return f'DefeaturingFilters(name="{ self.name }")'
