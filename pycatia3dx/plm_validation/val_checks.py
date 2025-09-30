"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_validation.val_check import VALCheck
from pycatia3dx.types.general import CATVariant


class VALChecks(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALChecks
                | 
                | A collection of Checks.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> VALCheck:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As VALCheck
                |     Creates a Check and adds it to the Check collection.
                | 
                |     Returns:
                |         The created Check 
                |     Example:
                | 
                |             This example creates a new Check in the cChecks
                |             collection.
                |
                |             Dim oNewCheckText As Check
                |             Set oNewCheckText = cChecks.Add

        :return: VALCheck
        """
        return VALCheck(self.com_object.Add())

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Check using its index from the Checks
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Check to retrieve from the collection
                |             of Checks. As a numerics, this index is the rank of the Check in the
                |             collection. The index of the first Check in the collection is 1, and the index
                |             of the last Check is Count. As a string, it is the name you assigned to the
                |             Check. 
                | 
                |     Returns:
                |         The retrieved Check 
                |     Example:
                | 
                |             This example retrieves in oCheck1 the ninth Check,
                |             and in oCheck2 the Check named
                |             Check3 from the cChecks collection. 
                | 
                |             Dim oCheck1 As Check
                |             Set oCheck1 = cChecks.Item(9)
                |             Dim oCheck2 As Check
                |             Set oCheck2 = cChecks.Item("Check3")

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Check from the Checks collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Check to retrieve from the collection
                |             of Checks. As a numerics, this index is the rank of the Check in the
                |             collection. The index of the first Check in the collection is 1, and the index
                |             of the last Check is Count. As a string, it is the name you assigned to the
                |             Check. 
                | 
                |     Example:
                | 
                |             The following example removes the tenth Check and the Check
                |             named
                |             Check2 from the cChecks collection.
                |             
                | 
                |             cChecks.Remove(10)
                |             cChecks.Remove("Check2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'ValChecks(name="{ self.name }")'
